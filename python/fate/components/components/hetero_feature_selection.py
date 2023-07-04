#
#  Copyright 2023 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import List

from fate.arch import Context
from fate.components.core import GUEST, HOST, Role, cpn, params


@cpn.component(roles=[GUEST, HOST])
def hetero_feature_selection(ctx, role):
    ...


@hetero_feature_selection.train()
def train(
        ctx: Context,
        role: Role,
        train_data: cpn.dataframe_input(roles=[GUEST, HOST]),
        input_models: cpn.json_model_inputs(roles=[GUEST, HOST]),
        method: cpn.parameter(type=List[params.string_choice(["manual", "binning", "statistic"])],
                              default=["manual"], optional=False,
                              desc="selection method, options: {manual, binning, statistic}"),
        select_col: cpn.parameter(type=List[str], default=None,
                                  desc="list of column names to be selected, if None, all columns will be considered"),
        iv_param: cpn.parameter(type=params.iv_filter_param(),
                                default=params.IVFilterParam(metrics="iv", take_high=True,
                                                             threshold=1, filter_type="threshold", host_thresholds=1,
                                                             host_take_high=True,
                                                             select_federated=True),
                                desc="iv filter param"),
        statistic_param: cpn.parameter(type=params.statistic_filter_param(),
                                       default=params.StatisticFilterParam(metrics="mean",
                                                                           threshold=1,
                                                                           filter_type="threshold",
                                                                           take_high=True),
                                       desc="statistic filter param"),
        manual_param: cpn.parameter(type=params.manual_filter_param(),
                                    default=params.ManualFilterParam(filter_out_col=[], keep_col=[]),
                                    desc="note that manual filter will always be processed as the last filter"),
        keep_one: cpn.parameter(type=bool,
                                default=True,
                                desc="whether to keep at least one feature among `select_col`"),
        use_anonymous: cpn.parameter(type=bool, default=False,
                                     desc="bool, whether interpret `select_col` & `filter_out_col` & `keep_col` "
                                          "as anonymous column names"),
        train_output_data: cpn.dataframe_output(roles=[GUEST, HOST]),
        train_output_model: cpn.json_model_output(roles=[GUEST, HOST])
):
    from fate.ml.feature_selection import HeteroSelectionModuleHost, HeteroSelectionModuleGuest

    sub_ctx = ctx.sub_ctx("train")
    isometric_model_dict = {}
    for model in input_models:
        model_type = model.artifact.metadata.metadata
        model = model.read()
        isometric_model_dict[model_type] = model

    train_data = train_data.read()
    columns = train_data.schema.columns.to_list()
    if use_anonymous:
        anonymous_columns = train_data.schema.anonymous_columns.to_list()
        if select_col is not None:
            select_col = [columns[anonymous_columns.index(col)] for col in select_col]
        if manual_param.filter_out_col is not None:
            filter_out_col = [columns[anonymous_columns.index(col)] for col in manual_param.filter_out_col]
            manual_param.filter_out_col = filter_out_col
        if manual_param.keep_col is not None:
            keep_col = [columns[anonymous_columns.index(col)] for col in manual_param.keep_col]
            manual_param.keep_col = keep_col

    if role.is_guest:
        selection = HeteroSelectionModuleGuest(method, select_col, isometric_model_dict,
                                               iv_param, statistic_param, manual_param,
                                               keep_one)
    elif role.is_host:
        selection = HeteroSelectionModuleHost(method, select_col, isometric_model_dict,
                                              iv_param, statistic_param, manual_param,
                                              keep_one)
    else:
        raise ValueError(f"role: {role} is not valid")
    selection.fit(sub_ctx, train_data)
    model = selection.to_model()
    train_output_model.write(model, metadata={"method": method})

    sub_ctx = ctx.sub_ctx("predict")
    output_data = train_data
    if method is not None:
        output_data = selection.transform(sub_ctx, train_data)
    train_output_data.write(output_data)


@hetero_feature_selection.predict()
def predict(
        ctx: Context,
        role: Role,
        test_data: cpn.dataframe_input(roles=[GUEST, HOST]),
        input_model: cpn.json_model_input(roles=[GUEST, HOST]),
        test_output_data: cpn.dataframe_output(roles=[GUEST, HOST])
):
    from fate.ml.feature_selection import HeteroSelectionModuleHost, HeteroSelectionModuleGuest

    sub_ctx = ctx.sub_ctx("predict")
    with input_model as model_reader:
        model = model_reader.read_model()
    if role.is_guest:
        selection = HeteroSelectionModuleGuest.from_model(model)
    elif role.is_host:
        selection = HeteroSelectionModuleHost.from_model(model)
    else:
        raise ValueError(f"role: {role} is not valid")

    model_meta = model["meta_data"]
    method = model_meta["method"]
    selection.method = method
    test_data = test_data.read()

    output_data = test_data
    if method is not None:
        output_data = selection.transform(sub_ctx, test_data)
    test_output_data.write(output_data)
