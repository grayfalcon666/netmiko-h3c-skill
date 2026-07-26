::: {#-1475171570 .myid}
[]{#struct_0_x9138_21976_1582375386}[]{#_Toc404797498}

**OAP \-- OAP调试命令 \-- debugging oap**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9138_21976_973586067}

[**[debugging oap ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** \| **fsm** }]{lang="EN-US"}]{#struct_0_x9138_21976_x2006305871}

[**[undo debugging oap ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** \| **fsm** }]{lang="EN-US"}]{#struct_0_x9138_21976_1656040002}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9138_21976_577774864}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9138_21976_x654147627}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9138_21976_x1996352234}

[[network-admin]{lang="EN-US"}]{#struct_0_x9138_21976_x1173137837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9138_21976_452244900}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9138_21976_2035366099}

[**[all]{lang="EN-US"}**]{#struct_0_x9138_21976_620437192}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[OAP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x9138_21976_x914720161}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[OAP]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x9138_21976_x372190530}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[OAP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x9138_21976_1379205627}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[OAP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x9138_21976_959288088}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[OAP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x9138_21976_1535473460}

[**[debugging oap]{lang="EN-US"}**]{#struct_0_x9138_21976_x1996286698}[命令用来打开]{style="font-family:宋体"}[OAP]{lang="EN-US"}[的调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo debugging oap]{lang="EN-US"}**]{#struct_0_x9138_21976_x1068266726}[命令用来]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[OAP]{lang="EN-US"}[的调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_1200545607}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}**[debugging oap error]{lang="EN-US"}**]{#struct_0_x9138_21976_x1084528050}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_220803745}[[字段]{style="font-family:黑体"}]{#struct_0_x9138_21976_2112130717}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9138_21976_x1524107198}

[[Failed to save OAP [multicast MAC address ]{style="color:black"}01:0F:E2:00:00:21[. Can't ]{style="color:black"}enable [OAP function on interface ]{style="color:black"}*interface-name.*]{lang="EN-US"}]{#struct_0_x9138_21976_x1735974975}

[[保存]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_1920855122}[协议组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[(01:0F:E2:00:00:21)]{lang="EN-US"}[失败，不能在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[启用]{style="font-family:宋体"}[OAP]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Failed to save OAP [unicast MAC address 58:66:BA:4D:FB:2A. Can't ]{style="color:black"}enable [OAP function on interface ]{style="color:black"}*interface-name.*]{lang="EN-US"}]{#struct_0_x9138_21976_x1996876525}

[[保存]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x2030649265}[协议单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[([58:66:BA:4D:FB:2A]{style="color:black"})]{lang="EN-US"}[失败，不能在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[启用]{style="font-family:宋体"}[OAP]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Failed to [send reply message. File handle: *socketfd*; Error code: *error-code*.]{style="color:black"}]{lang="EN-US"}]{#struct_0_x9138_21976_267656046}

[[发送]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_1061169322}[回应消息失败，]{style="font-family:宋体"}*[socketfd]{lang="EN-US"}*[为文件句柄*，*]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*[为返回错误码]{style="font-family:宋体"}

[[Failed to save client information to the local running DBM.]{lang="EN-US"}]{#struct_0_x9138_21976_x204922002}

[[保存]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1311242095}[客户端信息到本地运行数据库失败]{style="font-family:宋体"}

[[Failed to save OAP status to the configuration DBM.]{lang="EN-US"}]{#struct_0_x9138_21976_x1996810989}

[[保存]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x46080527}[使能状态到配置数据库失败]{style="font-family:宋体"}

[[Failed to save monitor time to the configuration DBM.]{lang="EN-US"}]{#struct_0_x9138_21976_x1303877428}

[[保存监控定时器时间到配置数据库失败]{style="font-family:宋体"}]{#struct_0_x9138_21976_x1040094930}

[[Failed to save clock synchronization time to the configuration DBM.]{lang="EN-US"}]{#struct_0_x9138_21976_1156385849}

[[保存时钟同步定时器时间到配置数据库失败]{style="font-family:宋体"}]{#struct_0_x9138_21976_x1518150103}

[[In[terface *ifindex* is dow]{style="color:black"}n.]{lang="EN-US"}]{#struct_0_x9138_21976_x1996745453}

[[报文接收接口已经]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x9138_21976_1704476173}[，]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[为接口索引]{style="font-family:宋体"}

[[OAP is disabled[ on interface ]{style="color:black"}*interface-name*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1458565990}

[[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_1921122627}[协议在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上未启用]{style="font-family:宋体"}

[[Discarded packet: Invalid packet length *packet-length*.]{lang="EN-US"}]{#struct_0_x9138_21976_1026628853}

[[丢弃报文，因为报文长度非法，]{style="font-family:宋体"}*[packet-length]{lang="EN-US"}*]{#struct_0_x9138_21976_x1996679917}[为非法的报文长度，这里和下面涉及到的长度都以字节为单位]{style="font-family:宋体"}

[[Discar[ded packet: Invalid vers]{style="color:black"}ion *version*.]{lang="EN-US"}]{#struct_0_x9138_21976_x90319075}

[[丢弃]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1146031908}[协议版本号非法的报文，]{style="font-family:宋体"}*[version]{lang="EN-US"}*[为非法的协议版本号]{style="font-family:宋体"}

[[Discar[ded packet: The packet was from another OAP man]{style="color:black"}ager.]{lang="EN-US"}]{#struct_0_x9138_21976_x605594850}

[[丢弃来自其他]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}]{#struct_0_x9138_21976_1124910001}[的报文]{style="font-family:宋体"}

[[Discard[ed packet: Invalid packet type *pack*]{style="color:black"}*et-type*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1997138669}

[[丢弃报文，]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}]{#struct_0_x9138_21976_x824062509}[收到非法的报文类型]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*

[[Disca[rded *packet-type-description* packet: Invalid OAP head length. OAP head length: *oaphead-length*; remaining le]{style="color:black"}ngth: *remaining-length*.]{lang="EN-US"}]{#struct_0_x9138_21976_162916778}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_x215630051}[报文，原因是]{style="font-family:
  宋体"}[OAP]{lang="EN-US"}[协议头长度字段非法，其中]{style="font-family:宋体"}*[oaphead-length]{lang="EN-US"}*[为头部中长度字段的值，]{style="font-family:宋体"}*[remaining-length]{lang="EN-US"}*[为报文剩余长度，]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register]{lang="EN-US"}]{#struct_0_x9138_21976_1937691362}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_x1997073133}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x1252152988}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister]{lang="EN-US"}]{#struct_0_x9138_21976_1277088992}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Disc[arded *packet-type-description* packet: Invalid client ID *client-id*.]{style="color:black"}]{lang="EN-US"}]{#struct_0_x9138_21976_173445158}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_x1997007597}[报文，原因是]{style="font-family:
  宋体"}[OAP]{lang="EN-US"}[协议头]{style="font-family:宋体"}[client ID]{lang="EN-US"}[字段]{style="font-family:宋体"}*[client-id]{lang="EN-US" style="color:black"}*[非法，]{style="font-family:
  宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_1111219951}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x619367001}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[Disca[rded register request packet: Invalid client ID *clien*]{style="color:black"}*t-id*.]{lang="EN-US"}]{#struct_0_x9138_21976_962545398}

[[丢弃注册请求报文，原因是]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_94940876}[协议头]{style="font-family:宋体"}[client ID]{lang="EN-US"}[字段]{style="font-family:宋体"}*[client-id]{lang="EN-US" style="color:black"}*[非法]{style="font-family:宋体"}

[[Discar[ded register request packet: Invalid destination MAC address *d*]{style="color:black"}*st-mac*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1996942061}

[[丢弃注册请求报文，原因是目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9138_21976_1917790015}[地址]{style="font-family:宋体"}*[dst-mac]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[Discard[ed *packet-type-description* packet: Invalid destination MAC address *dst-ma*]{style="color:black"}*c*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1643903803}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_x1996352237}[报文，原因是目的]{style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[dst-mac]{lang="EN-US"}*[非法，]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_1555745518}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x1307189849}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister]{lang="EN-US"}]{#struct_0_x9138_21976_1840040314}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Discard[ed deregister packet: Invalid source MAC address *src-*]{style="color:black"}*mac*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1996286701}

[[丢弃注销报文，原因是源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9138_21976_1304845020}[地址]{style="font-family:宋体"}*[src-mac]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[Discard[ed *packet-type-description*]{style="color:black"} [packet: Inconsistent interfaces. Client ID: *client-id;* Registered interface: ]{style="color:black"}*client-interface-name*; Inbound interface: *[packet-]{style="color:black"}interface-name.*]{lang="EN-US"}]{#struct_0_x9138_21976_405760491}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_x1356841367}[报文，原因是报文接收接口与客户端]{style="font-family:
  宋体"}*[client-id]{lang="EN-US"}*[注册时的接口不一致，其中]{style="font-family:宋体"}*[packet-]{lang="EN-US" style="color:black"}[interface-name]{lang="EN-US"}*[为报文接收接口名，]{style="font-family:宋体"}*[client-interface-name]{lang="EN-US"}*[为客户端注册时的接口名，]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_x1996876524}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_698234090}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister]{lang="EN-US"}]{#struct_0_x9138_21976_x928949942}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Discard[ed *packet-type-description* packet: Inconsistent source MAC addresses. Client ID: *client-id;* Registered MAC: *cli*]{style="color:black"}*ent-Mac*; Source MAC in packet: *[packet-srcMac]{style="color:black"}.*]{lang="EN-US"}]{#struct_0_x9138_21976_x1996810988}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_x1612164468}[报文，原因是报文的源]{style="font-family:
  宋体"}[MAC]{lang="EN-US"}[与客户端]{style="font-family:
  宋体"}*[client-id]{lang="EN-US"}*[注册信息中的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不一致，其中]{style="font-family:宋体"}*[packet-srcMac]{lang="EN-US"}*[为报文以太头源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[client-Mac]{lang="EN-US"}*[为客户端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_1854691561}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x1996745452}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister]{lang="EN-US"}]{#struct_0_x9138_21976_x1024407182}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Discard[ed *packet-type-description*]{style="color:black"} [packet: Inconsistent protocol types. Client ID: *client-id;* Registered protocol type: ]{style="color:black"}*client-protocoltype*; [Protocol type]{style="color:black"} in packet: *[packet-protocoltype]{style="color:black"}.*]{lang="EN-US"}]{#struct_0_x9138_21976_1154385864}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_x1996679916}[报文，原因是报文的以太网协议类型与客户端]{style="font-family:
  宋体"}*[client-id]{lang="EN-US"}*[注册信息中的不一致，其中]{style="font-family:宋体"}*[packet-protocoltype]{lang="EN-US"}*[为报文以太头中的协议类型，]{style="font-family:宋体"}*[client-protocoltype]{lang="EN-US"}*[为客户端注册时的协议类型，]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_x1656403016}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x541698468}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister]{lang="EN-US"}]{#struct_0_x9138_21976_x1251887511}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Discard[ed *packet-type-description* packet: Client *client-id* doesn't exis]{style="color:black"}t.]{lang="EN-US"}]{#struct_0_x9138_21976_x1997138668}

[[丢弃]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*]{#struct_0_x9138_21976_1904820846}[报文，原因是指定客户端]{style="font-family:
  宋体"}*[client-id]{lang="EN-US"}*[不存在，]{style="font-family:宋体"}*[packet-type-[description]{style="color:black"}]{lang="EN-US"}*[取值如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[information]{lang="EN-US"}]{#struct_0_x9138_21976_x1249369370}[：信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x1997073132}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister]{lang="EN-US"}]{#struct_0_x9138_21976_1476730367}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Disca[rded packet: Invalid inner head length *oapInnerH*]{style="color:black"}*ead-length.*]{lang="EN-US"}]{#struct_0_x9138_21976_x1151257428}

[[丢弃报文，原因是]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1997007596}[协议内部头中的长度字段非法，]{style="font-family:宋体"}*[oapInnerHead-length]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[OAP]{lang="EN-US"}[内部头长度值]{style="font-family:宋体"}

[[Discard[ed register request packet: Invalid inner code *oapInnerH*]{style="color:black"}*ead-code*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1617663404}

[[丢弃注册请求报文，原因是]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1138718910}[协议内部头中的]{style="font-family:宋体"}[code]{lang="EN-US"}[字段非法，]{style="font-family:宋体"}*[oapInnerHead-code]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[code]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Discard[ed monitor packet]{style="color:black"}:[ Unsupported subtype *oapInnerHead-code*.]{style="color:black"}]{lang="EN-US"}]{#struct_0_x9138_21976_x1996942060}

[[丢弃监控报文，原因是]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}]{#struct_0_x9138_21976_x811093340}[收到暂不支持的监控报文子类型，]{style="font-family:宋体"}[oapInnerHead-code]{lang="EN-US"}[为非法的]{style="font-family:宋体"}[code]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Discard[ed register request packet]{style="color:black"}: Invalid[ MUMA MAC TLV length *tlv-length*.]{style="color:black"}]{lang="EN-US"}]{#struct_0_x9138_21976_508589028}

[[丢弃注册请求报文，原因是携带的]{style="font-family:宋体"}[MUMA  MAC]{lang="EN-US"}]{#struct_0_x9138_21976_x1996352236}[类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度非法，]{style="font-family:宋体"}*[tlv-length]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Disca[rded register request packet: The packet format is too old and not supporte]{style="color:black"}d.]{lang="EN-US"}]{#struct_0_x9138_21976_x10338423}

[[丢弃注册请求报文，原因是老报文格式目前已不支持]{style="font-family:宋体"}]{#struct_0_x9138_21976_x1996286700}

[[Discarded monitor request packet: Invalid ma[gic number TLV length *tlv-length*]{style="color:black"}.]{lang="EN-US"}]{#struct_0_x9138_21976_x1424038335}

[[丢弃监控请求报文，原因是携带的魔术数字类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_x1061150260}[长度非法，]{style="font-family:宋体"}*[tlv-length]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Discarded monitor ACK packet: Invalid m[agic number TLV length *tlv-length*]{style="color:black"}.]{lang="EN-US"}]{#struct_0_x9138_21976_365094106}

[[丢弃监控确认报文，原因是携带的魔术数字类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_1337239270}[长度非法，]{style="font-family:宋体"}*[tlv-length]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Discarded monitor ACK packet: Inconsistent identifiers or magic numbers. In received packet: Identifier=*[packet-identifier]{style="color:black"}*  Magic number=*[packet-magicnum]{style="color:black"}*. In client *client-id*:      Identifier*=client-identifier*  Magic number=*client-magicnum*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1054653029}

[[丢弃监控确认报文，原因是收到客户端]{style="font-family:宋体"}*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_365028570}[的]{style="font-family:宋体"}[监控确认报文中的序列号或魔术数字与客户端注册信息中保存的不一致。其中]{style="font-family:宋体"}*[packet-identifier]{lang="EN-US"}*[为报文中的报文序列号，]{style="font-family:宋体"}*[packet-magicnum]{lang="EN-US"}*[为报文中携带的魔术数字，]{style="font-family:宋体"}*[client-identifier]{lang="EN-US"}*[为客户端注册信息中的报文序列号，]{style="font-family:宋体"}*[client-magicnum]{lang="EN-US"}*[为客户端注册信息中的魔术数字]{style="font-family:宋体"}

[[Discarded extended monitor request packet: Invalid co[okie TLV length *tlv-length*]{style="color:black"}.]{lang="EN-US"}]{#struct_0_x9138_21976_177329477}

[[丢弃扩展监控请求报文，原因是携带]{style="font-family:宋体"}[Cookie]{lang="EN-US"}]{#struct_0_x9138_21976_365225178}[类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度非法，]{style="font-family:宋体"}*[tlv-length]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Invalid T[LV length *tlv-length* in information pa]{style="color:black"}cket.]{lang="EN-US"}]{#struct_0_x9138_21976_x731469895}

[[客户端信息通告报文携带的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_365159642}[长度非法，]{style="font-family:宋体"}*[tlv-length]{lang="EN-US"}*[为非法的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Unsuppor[ted TLV type *tlv-type* in information p]{style="color:black"}acket.]{lang="EN-US"}]{#struct_0_x9138_21976_573268303}

[[客户端信息通告报文携带暂不支持的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_x1445955210}[类型，]{style="font-family:宋体"}*[tlv-type]{lang="EN-US"}*[为不支持的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Disc[arded information packet: All TLVs are in]{style="color:black"}valid.]{lang="EN-US"}]{#struct_0_x9138_21976_365356250}

[[丢弃信息通告报文，原因是客户端信息通告报文携带的所有]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_x1909509187}[都非法]{style="font-family:宋体"}

[[Disca[rded monitor request packet: No magic number TL]{style="color:black"}V.]{lang="EN-US"}]{#struct_0_x9138_21976_365290714}

[[丢弃监控请求报文，原因是没有携带魔术数字类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_446622534}

[[Discard[ed monitor ACK packet: N]{style="color:black"}o magic number TLV.]{lang="EN-US"}]{#struct_0_x9138_21976_x1696496106}

[[丢弃监控确认报文，原因是没有携带魔术数字类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_365487322}

[[Disc[arded extended monitor request packet: No cookie ]{style="color:black"}TLV.]{lang="EN-US"}]{#struct_0_x9138_21976_334150995}

[[丢弃扩展监控请求报文，原因是没有携带]{style="font-family:宋体"}[Cookie]{lang="EN-US"}]{#struct_0_x9138_21976_365421786}[类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Failed to add client because memory is insufficient.]{lang="EN-US"}]{#struct_0_x9138_21976_1143532557}

[[内存不够，添加]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_365618394}[客户端失败]{style="font-family:宋体"}

[[Failed to send packet on interface *interface-name*.]{lang="EN-US"}]{#struct_0_x9138_21976_1761132186}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_1862417626}[发送报文失败]{style="font-family:宋体"}

[[Announce timer failed.]{lang="EN-US"}]{#struct_0_x9138_21976_365552858}

[[通知定时器失败]{style="font-family:宋体"}]{#struct_0_x9138_21976_x131350077}

[[Connect timer failed.]{lang="EN-US"}]{#struct_0_x9138_21976_365094107}

[[定时器连接失败]{style="font-family:宋体"}]{#struct_0_x9138_21976_1337239269}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}**[debugging oap event]{lang="EN-US"}**]{#struct_0_x9138_21976_x1054194276}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_239973749}[[字段]{style="font-family:黑体"}]{#struct_0_x9138_21976_493340193}

[[描述]{style="font-family:黑体"}]{#struct_0_x9138_21976_365028571}

[[Number of monitor request packets with no responses reached the upper limit.]{lang="EN-US"}]{#struct_0_x9138_21976_177329478}

[[没有得到回应的监控请求报文数达到上限]{style="font-family:宋体"}]{#struct_0_x9138_21976_706611116}

[[OAP *event-type* event occurred on interface *interface-name* because *reason*.]{lang="EN-US"}]{#struct_0_x9138_21976_182496960}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_x634106836}[发生]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[事件]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[registered]{lang="EN-US"}]{#struct_0_x9138_21976_x2108753702}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[注册事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregistered]{lang="EN-US"}]{#struct_0_x9138_21976_x811151466}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[注销事件]{lang="EN-US" style="font-family:宋体"}

[*[reason]{lang="EN-US"}*]{#struct_0_x9138_21976_365225179}[包括如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register packet was received]{lang="EN-US"}]{#struct_0_x9138_21976_x731469894}[：收到注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAP was disabled]{lang="EN-US"}]{#struct_0_x9138_21976_995627736}[：]{lang="EN-US" style="font-family:
  宋体"}[关闭]{style="font-family:宋体"}[OAP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor was timed out]{lang="EN-US"}]{#struct_0_x9138_21976_2078216864}[：监控超时]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deregister packet was received]{lang="EN-US"}]{#struct_0_x9138_21976_2033443808}[：收到注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface was inactive]{lang="EN-US"}]{#struct_0_x9138_21976_x1575584327}[：接口去激活]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}**[debugging oap packet]{lang="EN-US"}**]{#struct_0_x9138_21976_365159643}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_243140081}[[字段]{style="font-family:黑体"}]{#struct_0_x9138_21976_573268302}

[[描述]{style="font-family:黑体"}]{#struct_0_x9138_21976_x1445955211}

[[Sent OAP packet]{lang="EN-US"}]{#struct_0_x9138_21976_x326877368}

[[发送]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x387412673}[协议报文]{style="font-family:宋体"}

[[Received OAP packet]{lang="EN-US"}]{#struct_0_x9138_21976_927226809}

[[接收]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x327111168}[协议报文]{style="font-family:宋体"}

[[Interface: *interface-name*]{lang="EN-US"}]{#struct_0_x9138_21976_365356251}

[[报文承载接口名]{style="font-family:宋体"}]{#struct_0_x9138_21976_x1909509188}

[[Destination MAC: *dst-mac*]{lang="EN-US"}]{#struct_0_x9138_21976_x1363639964}

[[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9138_21976_x179754162}[地址]{style="font-family:宋体"}

[[Source MAC: *src-mac*]{lang="EN-US"}]{#struct_0_x9138_21976_1859245324}

[[报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9138_21976_152100426}[地址]{style="font-family:宋体"}

[[Protocol Type: *protocol-type*]{lang="EN-US"}]{#struct_0_x9138_21976_365290715}

[[以太网协议类型]{style="font-family:宋体"}]{#struct_0_x9138_21976_446622533}

[[Sub-Type: *sub-type*]{lang="EN-US"}]{#struct_0_x9138_21976_x1696496107}

[[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x2088417986}[协议子类型]{style="font-family:宋体"}

[[Reserved: *reserved-value*]{lang="EN-US"}]{#struct_0_x9138_21976_x1430056393}

[[报文子协议保留位]{style="font-family:宋体"}]{#struct_0_x9138_21976_365487323}

[[Version: *version*]{lang="EN-US"}]{#struct_0_x9138_21976_334150996}

[[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1464642262}[协议版本]{style="font-family:宋体"}

[[Sender:*Client or Manager*]{lang="EN-US"}]{#struct_0_x9138_21976_764880762}

[[报文的发送者，]{style="font-family:宋体"}*[Client]{lang="EN-US"}*]{#struct_0_x9138_21976_x2046565298}[表示]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[发送的报文，]{style="font-family:宋体"}*[Manager]{lang="EN-US"}*[表示]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[发送的报文。]{style="font-family:宋体"}

[[Packet Type: *packet-type*]{lang="EN-US"}]{#struct_0_x9138_21976_x425962591}

[[报文类型，]{style="font-family:宋体"}*[ packet-type]{lang="EN-US"}*]{#struct_0_x9138_21976_365421787}[取值如下]{style="font-family:宋体"}[:]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_x9138_21976_1143532558}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inform]{lang="EN-US"}]{#struct_0_x9138_21976_1287543290}[：信息通告报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operate]{lang="EN-US"}]{#struct_0_x9138_21976_333513277}[：操作通告报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Monitor]{lang="EN-US"}]{#struct_0_x9138_21976_365618395}[：监控报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deregister]{lang="EN-US"}]{#struct_0_x9138_21976_1761132185}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[Client ID: *client-id*]{lang="EN-US"}]{#struct_0_x9138_21976_1862221018}

[[客户端标识]{style="font-family:宋体"}]{#struct_0_x9138_21976_2095892648}

[[Length: *length*]{lang="EN-US"}]{#struct_0_x9138_21976_302735858}

[[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_365552859}[协议头中长度字段的值，包括]{style="font-family:宋体"}[OAP]{lang="EN-US"}[头和后续实际报文数据的长度]{style="font-family:宋体"}

[[Code: *code*]{lang="EN-US"}]{#struct_0_x9138_21976_x131350078}

[[注册或监控报文的子类型]{style="font-family:宋体"}]{#struct_0_x9138_21976_1035919929}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[注册报文分为以下三种，]{style="font-family:宋体"}]{#struct_0_x9138_21976_x152419281}[code]{lang="EN-US"}[取值如下：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Register request]{lang="EN-US"}]{#struct_0_x9138_21976_365094104}[：注册请求]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Register ACK]{lang="EN-US"}]{#struct_0_x9138_21976_1337239272}[：注册确认]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Register reject]{lang="EN-US"}]{#struct_0_x9138_21976_x1054521957}[：注册拒绝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监控报文分为以下四种，]{style="font-family:宋体"}]{#struct_0_x9138_21976_615943844}[code]{lang="EN-US"}[取值如下：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Monitor request]{lang="EN-US"}]{#struct_0_x9138_21976_365028568}[：监控请求]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Monitor ACK]{lang="EN-US"}]{#struct_0_x9138_21976_2133644621}[：监控确认]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Extended monitor request]{lang="EN-US"}]{#struct_0_x9138_21976_x633653650}[：扩展监控请求]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Extended monitor ACK]{lang="EN-US"}]{#struct_0_x9138_21976_x77375628}[：扩展监控确认]{lang="EN-US" style="font-family:宋体"}

[[Identifier: *identifier*]{lang="EN-US"}]{#struct_0_x9138_21976_365225176}

[[注册或监控报文的序列号]{style="font-family:宋体"}]{#struct_0_x9138_21976_x731469905}

[[Length: *length*]{lang="EN-US"}]{#struct_0_x9138_21976_x1342958897}

[[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1790564178}[协议内部头中]{style="font-family:宋体"}[长度字段的值，包括]{style="font-family:宋体"}[OAP]{lang="EN-US"}[协议内部头和后续实际报文数据的长度]{style="font-family:宋体"}

[[TLV info:     ]{lang="EN-US"}]{#struct_0_x9138_21976_365159640}

[[报文]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_573268305}[信息提示，表示后续内容为报文携带]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息，每个]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息单独打印]{style="font-family:宋体"}

[[Type: *tlv-type*]{lang="EN-US"}]{#struct_0_x9138_21976_x1445955204}

[[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_365356248}[类型，]{style="font-family:宋体"}*[tlv-type]{lang="EN-US"}*[为报文携带的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型，不识别的类型显示为"]{style="font-family:宋体"}[Unknown TLV]{lang="EN-US"}["]{style="font-family:宋体"}

[[Length: *tlv-length*]{lang="EN-US"}]{#struct_0_x9138_21976_429142965}

[[单个]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_487729856}[的长度]{style="font-family:宋体"}

[[Value: *tlv-value*]{lang="EN-US"}]{#struct_0_x9138_21976_x1442612364}

[[TLV]{lang="EN-US"}]{#struct_0_x9138_21976_365290712}[中的]{style="font-family:宋体"}[Value]{lang="EN-US"}[值，如果]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[，则该处显示为]{style="font-family:宋体"}["None"]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}**[debugging oap fsm]{lang="EN-US"}**]{#struct_0_x9138_21976_446622536}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_237991481}[[字段]{style="font-family:黑体"}]{#struct_0_x9138_21976_x1696496104}

[[描述]{style="font-family:黑体"}]{#struct_0_x9138_21976_x1685133459}

[[Client *client-id* in *status* state: Sending *pkt-type* packet on interface *interface-name.*]{lang="EN-US"}]{#struct_0_x9138_21976_1367660814}

[[OAP manager]{lang="EN-US"}]{#struct_0_x9138_21976_365487320}[将在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[向状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*[的客户端发送]{style="font-family:宋体"}*[pkt-type]{lang="EN-US"}*[报文，]{style="font-family:宋体"}[其中：]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_334150997}[：]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_x1464642261}[：客户端注册接口]{style="font-family:宋体"}

[*[pkt-type]{lang="EN-US"}*]{#struct_0_x9138_21976_361596235}[：发送的报文类型，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register ACK]{lang="EN-US"}]{#struct_0_x9138_21976_x1459416480}[：表示发送注册确认报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register reject]{lang="EN-US"}]{#struct_0_x9138_21976_x907386954}[：表示发送注册拒绝报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[clock synchronization]{lang="EN-US"}]{#struct_0_x9138_21976_1698617916}[：表示发送时钟同步信息报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[time zone synchronization]{lang="EN-US"}]{#struct_0_x9138_21976_365421784}[：表示发送时区同步信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port context information]{lang="EN-US"}]{#struct_0_x9138_21976_1143532555}[：表示发送]{lang="EN-US" style="font-family:宋体"}[Port Context]{lang="EN-US"}[信息报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor request]{lang="EN-US"}]{#struct_0_x9138_21976_1288264186}[：表示发送监控请求报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[monitor ACK]{lang="EN-US"}]{#struct_0_x9138_21976_x662943208}[：表示发送监控确认报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extended monitor ACK]{lang="EN-US"}]{#struct_0_x9138_21976_x1565687943}[：表示发送扩展监控确认报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[close operation]{lang="EN-US"}]{#struct_0_x9138_21976_28300614}[：表示发送关闭操作报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reboot operation]{lang="EN-US"}]{#struct_0_x9138_21976_365618392}[：表示发送重启操作报文]{lang="EN-US" style="font-family:
  宋体"}

[*[status]{lang="EN-US"}*]{#struct_0_x9138_21976_1761132188}[：客户端状态，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[registered]{lang="EN-US"}]{#struct_0_x9138_21976_1862548698}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[成功注册]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unregistered]{lang="EN-US"}]{#struct_0_x9138_21976_x1374835110}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[未注册]{lang="EN-US" style="font-family:宋体"}

[[Client *client-id* in *status* state, interface *interface-name*: Received *event-type* event*.*]{lang="EN-US"}]{#struct_0_x9138_21976_1610963257}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_365552856}[下注册的客户端在状态]{style="font-family:宋体"}*[status]{lang="EN-US"}*[下收到]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[事件，其中：]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_x131350067}[：]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_1035199032}[：客户端注册接口]{style="font-family:宋体"}

[*[event-type]{lang="EN-US"}*]{#struct_0_x9138_21976_x596097736}[：事件类型，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface_Inactive]{lang="EN-US"}]{#struct_0_x9138_21976_1223727582}[：接口去激活]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface_LinkUp]{lang="EN-US"}]{#struct_0_x9138_21976_365094105}[：接口]{lang="EN-US" style="font-family:
  宋体"}[UP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface_LinkDown]{lang="EN-US"}]{#struct_0_x9138_21976_1337239271}[：接口]{lang="EN-US" style="font-family:
  宋体"}[DOWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Oap_Disable]{lang="EN-US"}]{#struct_0_x9138_21976_x1054718565}[：]{lang="EN-US" style="font-family:宋体"}[OAP]{lang="EN-US"}[去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation_Close]{lang="EN-US"}]{#struct_0_x9138_21976_1658190565}[：关闭操作]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation_Reboot]{lang="EN-US"}]{#struct_0_x9138_21976_365028569}[：重启操作]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Client_Delete]{lang="EN-US"}]{#struct_0_x9138_21976_2133644622}[：删除客户端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MonitorTimer_Pause]{lang="EN-US"}]{#struct_0_x9138_21976_x633850258}[：暂停监控定时器]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RegisterRequest_Receive]{lang="EN-US"}]{#struct_0_x9138_21976_723510035}[：收到注册请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MonitorTimer_Expire]{lang="EN-US"}]{#struct_0_x9138_21976_365225177}[：监控定时器超时]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MonitorResponse_Receive]{lang="EN-US"}]{#struct_0_x9138_21976_x731469904}[：收到监控确认报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MonitorRequest_Receive]{lang="EN-US"}]{#struct_0_x9138_21976_x1343024433}[：收到监控请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ExtendedMonitorRequest_Receive]{lang="EN-US"}]{#struct_0_x9138_21976_215044322}[：收到监控扩展请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ClockSyncTimer_Expire]{lang="EN-US"}]{#struct_0_x9138_21976_365159641}[：时钟同步定时器超时]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Information_Receive]{lang="EN-US"}]{#struct_0_x9138_21976_573268304}[：收到信息通告报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deregister_Receive]{lang="EN-US"}]{#struct_0_x9138_21976_x1445955205}[：收到注销请求报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Context_Change]{lang="EN-US"}]{#struct_0_x9138_21976_1642556636}[：收到驱动报文头信息]{lang="EN-US" style="font-family:宋体"}

[*[status]{lang="EN-US"}*]{#struct_0_x9138_21976_365356249}[：客户端状态，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[registered]{lang="EN-US"}]{#struct_0_x9138_21976_429142964}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[成功注册]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unregistered]{lang="EN-US"}]{#struct_0_x9138_21976_487729855}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[未注册]{lang="EN-US" style="font-family:宋体"}

[[Client *client-id*, interface *interface-name*: Entered *status* state.]{lang="EN-US"}]{#struct_0_x9138_21976_x1442612365}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_365290713}[下注册的客户端进入]{style="font-family:宋体"}*[status]{lang="EN-US"}*[状态]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_446622535}[：]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_x1696496105}[：客户端注册接口]{style="font-family:宋体"}

[*[status]{lang="EN-US"}*]{#struct_0_x9138_21976_1043749896}[：客户端状态，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[registered]{lang="EN-US"}]{#struct_0_x9138_21976_365487321}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[成功注册]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unregistered]{lang="EN-US"}]{#struct_0_x9138_21976_334150998}[：]{lang="EN-US" style="font-family:宋体"}[Client]{lang="EN-US"}[未注册]{lang="EN-US" style="font-family:宋体"}

[[Client *client-id*, interface *interface-name*: Number of monitor request packets with no responses changed from *old-value* to *new-value*.]{lang="EN-US"}]{#struct_0_x9138_21976_x1464642268}

[[打印没有得到回应的监控请求报文数从]{style="font-family:宋体"}*[old-value]{lang="EN-US"}*]{#struct_0_x9138_21976_365421785}[变到]{style="font-family:宋体"}*[new-value]{lang="EN-US"}*[，其中：]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_1143532556}[：]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[Interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_1288198650}[：客户端注册接口]{style="font-family:宋体"}

[[Client *client-id*, interface *interface-name*, *info-type* info: *info-context*.]{lang="EN-US"}]{#struct_0_x9138_21976_365618393}

[[打印驱动报文头信息或]{style="font-family:宋体"}[Cookie]{lang="EN-US"}]{#struct_0_x9138_21976_1761132187}[信息，其中：]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_1862352090}[：]{style="font-family:宋体"}[唯一标识一个]{style="font-family:宋体"}[Client]{lang="EN-US"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_531315998}[：承载接口名]{style="font-family:宋体"}

[*[info-type]{lang="EN-US"}*]{#struct_0_x9138_21976_365552857}[：信息类型，取值包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[context]{lang="EN-US"}]{#struct_0_x9138_21976_x131350068}[：驱动报文头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[cookie]{lang="EN-US"}]{#struct_0_x9138_21976_1035919928}[：]{lang="EN-US" style="font-family:宋体"}[Cookie]{lang="EN-US"}[信息]{lang="EN-US" style="font-family:宋体"}

[*[info-context]{lang="EN-US"}*]{#struct_0_x9138_21976_365094102}[：驱动报文头信息或]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[信息内容，如果长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[，该字段显示"]{style="font-family:宋体"}[None]{lang="EN-US"}["]{style="font-family:宋体"}

[[Updating client information of client *client-id.*]{lang="EN-US"}]{#struct_0_x9138_21976_1337239274}

[[更新客户端]{style="font-family:宋体"}*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_x1054915173}[信息]{style="font-family:宋体"}

[[Client *client-id*, interface *interface-name*: Monitor timer expired, number of monitor request packets with no responses is *new-value*.]{lang="EN-US"}]{#struct_0_x9138_21976_365028566}

[[监控定时器超时，没有得到回应的监控请求报文数变为]{style="font-family:宋体"}*[new-value]{lang="EN-US"}*]{#struct_0_x9138_21976_2133644611}[，其中]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_365225174}[：]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_x731469907}[：客户端注册接口]{style="font-family:宋体"}

[[Handling registering client which has same interface index and same source MAC address as a registered client.]{lang="EN-US"}]{#struct_0_x9138_21976_x1343089969}

[[处理注册]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_365159638}[客户端的接口索引与]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和已注册的客户端相同]{style="font-family:宋体"}

[[Handling registering client which has same interface index as a registered client but their source MAC addresses are different.]{lang="EN-US"}]{#struct_0_x9138_21976_x618372791}

[[处理注册]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_1771563292}[客户端的接口索引与已注册的客户端相同，但]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不同]{style="font-family:宋体"}

[[Handling registering client which has same source MAC address as a registered client but their interface indexes are different.]{lang="EN-US"}]{#struct_0_x9138_21976_365356246}

[[处理注册]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_429142975}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与已注册的客户端相同，但接口索引不同]{style="font-family:宋体"}

[[Handling registering client which has different interface index and different source MAC address as a registered client.]{lang="EN-US"}]{#struct_0_x9138_21976_x1850922304}

[[处理注册]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_365290710}[客户端的接口索引与]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和已注册的客户端都不相同]{style="font-family:宋体"}

[[Failed to register on interface *interface-name*: *reject-reason.*]{lang="EN-US"}]{#struct_0_x9138_21976_446622538}

[[客户端在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_365487318}[下]{style="font-family:宋体"}[注册失败，注册拒绝原因]{style="font-family:宋体"}*[reject-reason]{lang="EN-US"}*[有]{style="font-family:宋体"}[如下情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The client has been registered with the client ID client-id OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1239827123}[客户端]{lang="EN-US" style="font-family:宋体"}[client-id]{lang="EN-US"}[重复注册]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No client ID available ]{lang="EN-US"}]{#struct_0_x9138_21976_1536700992}[没有可分配的合法客户端]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown reason ]{lang="EN-US"}]{#struct_0_x9138_21976_365421782}[未知原因]{lang="EN-US" style="font-family:
  宋体"}

[[Registered a new client on interface *interface-name*. Client: *client-id;* Protocol: *protocol-type;* MAC: *client-mac*; MUMA MAC: *muma-mac;* Register time: *register-time*.]{lang="EN-US"}]{#struct_0_x9138_21976_1143532561}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9138_21976_1288002039}[成功注册新的客户端，其中：]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_x9138_21976_365618390}[：新注册的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[protocol-type]{lang="EN-US"}*]{#struct_0_x9138_21976_1761132190}[：客户端注册时的协议类型]{style="font-family:宋体"}

[*[client-mac]{lang="EN-US"}*]{#struct_0_x9138_21976_365552854}[：客户端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[muma-mac]{lang="EN-US"}*]{#struct_0_x9138_21976_x131350065}[：客户端携带的]{style="font-family:宋体"}[MUMA  MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[register-time]{lang="EN-US"}*]{#struct_0_x9138_21976_1035067960}[：注册时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9138_21976_365094103}

[[\# OAP client]{lang="EN-US"}]{#struct_0_x9138_21976_1337239273}[向]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[注册。]{style="font-family:宋体"}

[[打开]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_x9138_21976_x1054587493}[所有调试开关，]{style="font-family:宋体"}[在接口]{style="font-family:宋体"}*[Gigabit]{lang="EN-US"}[Ethernet 1/0/1]{lang="EN-US"}*[上启用]{style="font-family:宋体"}[OAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_x9138_21976_x1598235025}

[[\<Sysname\> debugging oap all]{lang="EN-US"}]{#struct_0_x9138_21976_538938598}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9138_21976_x523522672}

[[\[Sysname\] interface Ethernet 1/1]{lang="EN-US"}]{#struct_0_x9138_21976_1278339699}

[[\[Sysname-Ethernet1/1\] oap enable]{lang="EN-US"}]{#struct_0_x9138_21976_1234901936}

[[\*Apr 17 08:00:33:224 2012 Sysname OAP/7/PKT: -MDC=1; Received OAP packet.]{lang="EN-US"}]{#struct_0_x9138_21976_x1050173608}

[[  Interface: Ethernet1/1;]{lang="EN-US"}]{#struct_0_x9138_21976_365028567}

[[  Destination MAC: 010f-e200-0021;  Source MAC: 0000-5e61-8901;]{lang="EN-US"}]{#struct_0_x9138_21976_2133644612}

[[  Protocol Type: 88a7;  Sub-Type: 0007;  Reserved: 0000;]{lang="EN-US"}]{#struct_0_x9138_21976_x633850255}

[[  Version: 1;  Sender: Client;  Packet Type: Register;]{lang="EN-US"}]{#struct_0_x9138_21976_724362003}

[[  Client ID: 0;  Length: 18;]{lang="EN-US"}]{#struct_0_x9138_21976_x199874261}

[[  Code: Register request;  Identifier: 1;  Length: 12.]{lang="EN-US"}]{#struct_0_x9138_21976_x604374765}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Apr 17 08:00:33:224 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_324256646}

[[  Type: Client MUMA MAC;  Length: 8;  Value: 0011-2233-4455.]{lang="EN-US"}]{#struct_0_x9138_21976_x950632427}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_x1441527405}*[报文调试信息：]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[在接口]{style="font-family:宋体"}[Ethernet 1/1]{lang="EN-US"}[上]{style="font-family:宋体"}[收到]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[（]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0000-5e61-8901]{lang="EN-US"}[）发送的注册请求报文，携带的]{style="font-family:宋体"}[MUMA MAC]{lang="EN-US"}[为]{style="font-family:宋体"}[0011-2233-4455]{lang="EN-US"}*

[[\*Apr 17 08:00:33:224 2012 Sysname OAP/7/FSM: -MDC=1; Client 0 in unregistered state, interface Ethernet1/1: Received RegisterRequest_Receive event.]{lang="EN-US"}]{#struct_0_x9138_21976_2060149883}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_365225175}*[状态机调试信息：]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[在接口]{style="font-family:宋体"}[Ethernet 1/1]{lang="EN-US"}[上接受到注册请求报文]{style="font-family:宋体"}*

[[\*Apr 17 08:00:33:224 2012 Sysname OAP/7/FSM: -MDC=1; Handling registering client which has different interface index and different source MAC address as a registered client.]{lang="EN-US"}]{#struct_0_x9138_21976_x731469906}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_x1343155505}*[状态机调试信息：]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[在接口]{style="font-family:宋体"}[Ethernet 1/1]{lang="EN-US"}[上处理接口索引和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[都不相同的注册客户端]{style="font-family:宋体"}*

[[\*Apr 17 08:00:33:225 2012 Sysname OAP/7/EVENT: -MDC=1; OAP registered event occurred on interface Ethernet1/1 because register packet was received.]{lang="EN-US"}]{#struct_0_x9138_21976_1943474738}

[*[//]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}*]{#struct_0_x9138_21976_239694055}*[事件调试信息：接口]{style="font-size:10.5pt;font-family:宋体"}[Ethernet 1/1]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[发生]{style="font-size:10.5pt;font-family:宋体"}[OAP]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[注册事件，原因是收到注册报文]{style="font-size:10.5pt;font-family:宋体"}*

[[\*Apr 17 08:00:33:226 2012 Sysname OAP/7/FSM: -MDC=1; Registered a new client on interface Ethernet 1/1. Client: 1; Protocol: 0x88a7; MAC: 0000-5e61-8901; MUMA MAC: 0011-2233-4455; Register time: 04/17/2012 08:00:33.]{lang="EN-US"}]{#struct_0_x9138_21976_x1717548322}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_x743663944}*[状态机调试信息：接口]{style="font-family:宋体"}[Ethernet 1/1]{lang="EN-US"}[成功注册客户端，客户端]{style="font-family:宋体"}[ID(1)]{lang="EN-US"}[，协议号]{style="font-family:宋体"}[(0x88a7)]{lang="EN-US"}[，客户端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[(0000-5e61-8901)]{lang="EN-US"}[，客户端携带]{style="font-family:宋体"}[MUMA MAC(0011-2233-4455)]{lang="EN-US"}[，注册时间]{style="font-family:宋体"}[(04/17/2012 08:00:33)]{lang="EN-US"}*

[[\*Apr 17 08:00:33:226 2012 Sysname OAP/7/FSM: -MDC=1; Client 1, interface Ethernet1/1, context info:]{lang="EN-US"}]{#struct_0_x9138_21976_1277205752}

[[  0x4f 41 50 20 64 72 76 20 74 65 73 74 00. ]{lang="EN-US"}]{#struct_0_x9138_21976_365159639}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_x618372792}*[状态机调试信息：获取]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[的驱动报文头信息，按单字节十六进制格式打印]{style="font-family:宋体"}*

[[\*Apr 17 08:00:33:226 2012 Sysname OAP/7/FSM: -MDC=1; Client 1 in registered state: Sending register ACK packet on interface Ethernet1/1.]{lang="EN-US"}]{#struct_0_x9138_21976_1771628828}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_x1831825430}*[状态机调试信息：]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[在接口]{style="font-family:宋体"}[Ethernet 1/1]{lang="EN-US"}[向客户端]{style="font-family:宋体"}[1]{lang="EN-US"}[发送注册确认报文]{style="font-family:宋体"}*

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; Sent OAP packet.]{lang="EN-US"}]{#struct_0_x9138_21976_x1798697794}

[[  Interface: Ethernet1/1;]{lang="EN-US"}]{#struct_0_x9138_21976_x827751126}

[[  Destination MAC: 0000-5e61-8901;  Source MAC: 5866-ba4d-fb2a;]{lang="EN-US"}]{#struct_0_x9138_21976_1643345432}

[[  Protocol Type: 88a7;  Sub-Type: 0007;  Reserved: 0000;]{lang="EN-US"}]{#struct_0_x9138_21976_690218532}

[[  Version: 1;  Sender: Manager;  Packet Type: Register;]{lang="EN-US"}]{#struct_0_x9138_21976_x786019063}

[[  Client ID: 1;  Length: 93;]{lang="EN-US"}]{#struct_0_x9138_21976_245240774}

[[  Code: Register ACK;  Identifier: 1;  Length: 87.]{lang="EN-US"}]{#struct_0_x9138_21976_365356247}

[ ]{lang="EN-US"}

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_429142974}

[[  Type: Internal port attribute;  Length: 10;]{lang="EN-US"}]{#struct_0_x9138_21976_x1850922305}

[[  Value (interface index, attribute): 20, 3.]{lang="EN-US"}]{#struct_0_x9138_21976_1707877164}

[ ]{lang="EN-US"}

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_1939439800}

[[  Type: Driver context;  Length: 15;]{lang="EN-US"}]{#struct_0_x9138_21976_2110342356}

[[  Value:]{lang="EN-US"}]{#struct_0_x9138_21976_1333202630}

[[  0x4f 41 50 20 64 72 76 20 74 65 73 74 00.]{lang="EN-US"}]{#struct_0_x9138_21976_x1574371696}

[ ]{lang="EN-US"}

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_329727720}

[[  Type: Internal port slot number;  Length: 10;]{lang="EN-US"}]{#struct_0_x9138_21976_365290711}

[[  Value (interface index, slot number): 20, 0.]{lang="EN-US"}]{#struct_0_x9138_21976_446622537}

[ ]{lang="EN-US"}

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_x1696496103}

[[  Type: Internal port subslot number;  Length: 10;]{lang="EN-US"}]{#struct_0_x9138_21976_237180842}

[[  Value (interface index, subslot number): 20, 1.]{lang="EN-US"}]{#struct_0_x9138_21976_x781024600}

[ ]{lang="EN-US"}

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_x201255311}

[[  Type: Internal port name;  Length: 26;]{lang="EN-US"}]{#struct_0_x9138_21976_x1111607354}

[[  Value (interface index, port name): 20, Ethernet1/1.]{lang="EN-US"}]{#struct_0_x9138_21976_x2125409218}

[ ]{lang="EN-US"}

[[\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:]{lang="EN-US"}]{#struct_0_x9138_21976_1298680805}

[[  Type: Manager MUMA MAC;  Length: 12;]{lang="EN-US"}]{#struct_0_x9138_21976_365487319}

[[  Value (interface index, MUMA MAC): 20, 5866-ba4d-fb2a.]{lang="EN-US"}]{#struct_0_x9138_21976_x1239827122}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_x29382949}*[报文调试信息：]{style="font-family:宋体"}[OAP manager]{lang="EN-US"}[在接口]{style="font-family:宋体"}[Ethernet 1/1]{lang="EN-US"}[向客户端]{style="font-family:宋体"}[1]{lang="EN-US"}[发送注册确认报文]{style="font-family:宋体"}*

[[\*Apr 17 08:16:49:519 2012 Sysname OAP/7/ERROR: -MDC=1; Discarded packet: Invalid version (2).]{lang="EN-US"}]{#struct_0_x9138_21976_1902513469}

[*[//]{lang="EN-US"}*]{#struct_0_x9138_21976_811904678}*[错误调试信息：]{style="font-family:宋体"}[OAP]{lang="EN-US"}[协议版本号非法]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
