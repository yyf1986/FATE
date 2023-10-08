package org.fedai.osx.core.constant;

public class UriConstants {

    //            "/v1/interconn/chan/pop":
//             "/v1/interconn/chan/push":
//             "/v1/interconn/chan/peek":
//             "/v1/interconn/chan/release":
//             "/v1/interconn/net/weave":
    //"/org.ppc.ptp.PrivateTransferTransport/peek":
    //"/org.ppc.ptp.PrivateTransferTransport/pop":
    // "/org.ppc.ptp.PrivateTransferTransport/push":
    //"/org.ppc.ptp.PrivateTransferTransport/release":



    public static  final String  POP= "/org.ppc.ptp.PrivateTransferTransport/pop";
    public static  final String  PEEK = "/org.ppc.ptp.PrivateTransferTransport/peek";
    public static  final String  PUSH = "/org.ppc.ptp.PrivateTransferTransport/push";
    public static  final String  RELEASE = "/org.ppc.ptp.PrivateTransferTransport/release";
    public static  final String  UNARYCALL = "/org.fedai.osx.proxy/unary";

    public static  final String  EGGROLL_PUSH = "/org.fedai.osx.proxy/push";
    public static  final String  CLUSTER_TOKEN_APPLY = "/org.fedai.osx.proxy/tokenApply";
    public static  final String  CLUSTER_TOPIC_APPLY = "/org.fedai.osx.proxy/topicApply";


}
