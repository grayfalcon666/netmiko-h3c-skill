::: {#-378564463 .myid}
[]{#_Toc253298421}[]{#_Toc130718952}[]{#_Toc404797997}[]{#struct_0_x1051_20145_x1634914151}[]{#_Toc87257691}

**SPBM \-- SPBM调试命令 \-- debugging spbm adj-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1628541430}

[**[debugging spbm adj-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1051_20145_1266936609}

[**[undo debugging spbm adj-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1051_20145_x389542329}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_303346400}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x813745487}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1634848615}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_1812571040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1211658269}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_2125321478}

[**[receive]{lang="EN-US"}**]{#struct_0_x1051_20145_x515597484}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文接收调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1051_20145_759580448}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1051_20145_x1365765486}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文详细信息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1443078452}

[**[debugging spbm adj-packet]{lang="EN-US"}**]{#struct_0_x1051_20145_303346403}[命令用来打开]{style="font-family:
宋体"}[SPBM Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:
宋体"}**[undo ]{lang="EN-US"}[debugging spbm adj-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM Hello]{lang="EN-US"}]{#struct_0_x1051_20145_x813745490}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging spbm adj-packet]{lang="EN-US"}]{#struct_0_x1051_20145_x1634389862}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2061242914}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1042505297}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x168083426}

[[ADJ: The MCID received from circuit *circuitName* is different from local value.]{lang="EN-US"}]{#struct_0_x1051_20145_x1385923021}

[[端口收到的]{style="font-family:宋体"}[MCID]{lang="EN-US"}]{#struct_0_x1051_20145_532494934}[与本地值不一致，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: The mapping between ECT and B-VLAN received from circuit *circuitName* is different from local value.]{lang="EN-US"}]{#struct_0_x1051_20145_303346402}

[[接收到的]{style="font-family:宋体"}[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x813745489}[与]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[映射关系与本地值不一致，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: The B-VLAN *bvlan-number* in the mapping between ECT and B-VLAN is different from local value.]{lang="EN-US"}]{#struct_0_x1051_20145_x1634979687}

[[接收到的]{style="font-family:宋体"}[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x996740151}[与]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[映射关系与本地值不一致的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[表示不一致的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[ADJ: The neighbor\'s system ID changed on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1856035259}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_303346405}[邻居系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[变化，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: The neighbor changed from circuit *circuitName* to circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x813745484}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_x1634652007}[邻居端口间迁移，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid protocol support.]{lang="EN-US"}]{#struct_0_x1051_20145_692762169}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1660384823}[Hello]{lang="EN-US"}[报文被丢弃，原因是非法的协议支持信息]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: packet length is too small.]{lang="EN-US"}]{#struct_0_x1051_20145_303346404}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x813745483}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文长度太小]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid packet length.]{lang="EN-US"}]{#struct_0_x1051_20145_x1634586471}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_200283718}[Hello]{lang="EN-US"}[报文被丢弃，原因是非法的报文长度]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: authentication failed.]{lang="EN-US"}]{#struct_0_x1051_20145_1652388922}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_303346391}[Hello]{lang="EN-US"}[报文被丢弃，原因是没有通过认证，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: system is in disable state.]{lang="EN-US"}]{#struct_0_x1051_20145_372736439}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x646162281}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程处于]{style="font-family:宋体"}[disable]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit is being deleted.]{lang="EN-US"}]{#struct_0_x1051_20145_x1502533748}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_303346390}[Hello]{lang="EN-US"}[报文被丢弃，原因是端口正在被删除，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit\'s link state is down.]{lang="EN-US"}]{#struct_0_x1051_20145_372736440}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_1310152848}[Hello]{lang="EN-US"}[报文被丢弃，原因是端口链路状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit\'s protocol state is disable.]{lang="EN-US"}]{#struct_0_x1051_20145_2010586068}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_1904534015}[Hello]{lang="EN-US"}[报文被丢弃，原因是端口的协议状态为]{style="font-family:宋体"}[disable]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit is in disable state.]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968737}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_540640890}[Hello]{lang="EN-US"}[报文被丢弃，原因是端口处于]{style="font-family:宋体"}[disable]{lang="EN-US"}[状态，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: conflicted system ID.]{lang="EN-US"}]{#struct_0_x1051_20145_1134803010}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x764114771}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文携带的]{style="font-family:宋体"}[system ID]{lang="EN-US"}[和本系统的相同]{style="font-family:宋体"}

[[ADJ: Received a P2P Hello packet from ]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968738}*[system-id]{lang="EN-US"}*[ on circuit *circuitName*.]{lang="EN-US"}

[[接收到]{style="font-family:宋体"}]{#struct_0_x1051_20145_1300155777}[Hello]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968735}[：报文携带的]{lang="EN-US" style="font-family:宋体"}[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_1703440304}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: SPB area address check failed.]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968736}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_2106724831}[Hello]{lang="EN-US"}[报文被丢弃，原因是区域地址与本系统不一致]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: MSTP 4092 Instance not configured.]{lang="EN-US"}]{#struct_0_x1051_20145_848751031}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_588681397}[Hello]{lang="EN-US"}[报文被丢弃，原因是没有配置]{style="font-family:宋体"}[MSTP 4092]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid protocol descriminator.]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968733}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1784957938}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部的]{style="font-family:宋体"}[protocol descriminator]{lang="EN-US"}[字段非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid version.]{lang="EN-US"}]{#struct_0_x1051_20145_x762024656}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_176419528}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部的]{style="font-family:宋体"}[version]{lang="EN-US"}[字段非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid protocol ID.]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968734}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1025443051}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部的]{style="font-family:宋体"}[protocol ID]{lang="EN-US"}[字段非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid system ID length.]{lang="EN-US"}]{#struct_0_x1051_20145_456739269}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968731}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部的]{style="font-family:宋体"}[system ID]{lang="EN-US"}[长度字段非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid max area address number.]{lang="EN-US"}]{#struct_0_x1051_20145_x622158524}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_948872622}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部的最大区域地址个数字段非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid packet type.]{lang="EN-US"}]{#struct_0_x1051_20145_x397246895}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968732}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部的]{style="font-family:宋体"}[packet type]{lang="EN-US"}[字段非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid header length.]{lang="EN-US"}]{#struct_0_x1051_20145_x218873997}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_1987605847}[Hello]{lang="EN-US"}[报文被丢弃，原因是报文头部长度值非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid circuit type.]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968745}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_1703636912}[Hello]{lang="EN-US"}[报文被丢弃，原因是非法的链路类型]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: area address TLV decode error.]{lang="EN-US"}]{#struct_0_x1051_20145_1447562462}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968746}[Hello]{lang="EN-US"}[报文被丢弃，原因是区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解析错误]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: protocol support TLV decode error.]{lang="EN-US"}]{#struct_0_x1051_20145_2106921439}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x749434184}[Hello]{lang="EN-US"}[报文被丢弃，原因是协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解析错误]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: authentication TLV decode error.]{lang="EN-US"}]{#struct_0_x1051_20145_x843664673}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1516945627}[Hello]{lang="EN-US"}[报文被丢弃，原因是认证]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解析错误]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: GR TLV decode error.]{lang="EN-US"}]{#struct_0_x1051_20145_x1200005653}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x843664674}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[GR TLV]{lang="EN-US"}[解析错误]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid MT-Port-Cap TLV length.]{lang="EN-US"}]{#struct_0_x1051_20145_x1517273307}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_491268158}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[MT-Port-Cap TLV]{lang="EN-US"}[长度非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid MT-Port-Cap sub-TLV length.]{lang="EN-US"}]{#struct_0_x1051_20145_x843664671}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1517076699}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[MT-Port-Cap TLV]{lang="EN-US"}[的子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: MT-Port-Cap TLV decode error.]{lang="EN-US"}]{#struct_0_x1051_20145_81585115}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x843664672}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[MT-Port-Cap TLV]{lang="EN-US"}[解析错误]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid multi topology ID of MT-Port-Cap TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x1516880091}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x88394897}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[MT-Port-Cap TLV]{lang="EN-US"}[的]{style="font-family:宋体"}[MTID]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid SPB MCID sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x843664669}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1517600986}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPB MCID sub-TLV]{lang="EN-US"}[的长度非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: different MCIDs in SPB MCID sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x493113860}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x843664670}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPB MCID sub-TLV]{lang="EN-US"}[中含有多个不同的]{style="font-family:宋体"}[MCID]{lang="EN-US"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid SPB Digest sub-TLV length.]{lang="EN-US"}]{#struct_0_x1051_20145_x1517011163}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x92121058}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPB Digest sub-TLV]{lang="EN-US"}[的长度非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: different digests in SPB Digest sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x843664667}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1517207770}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPB MCID sub-TLV]{lang="EN-US"}[中含有多个不同的]{style="font-family:宋体"}[Digest]{lang="EN-US"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid SPB Base VLAN-Identifiers sub-TLV length.]{lang="EN-US"}]{#struct_0_x1051_20145_x843664668}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1517535450}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPB Base VLAN-Identifiers sub TLV]{lang="EN-US"}[的长度非法]{style="font-family:宋体"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid B-VLAN in SPB Base VLAN-Identifiers sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x2018585720}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x843664681}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[SPB Base VLAN-Identifiers sub TLV]{lang="EN-US"}[中含有非法]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[ADJ: Discarded a P2P Hello packet. Reason: invalid TLV length.]{lang="EN-US"}]{#struct_0_x1051_20145_x1517076692}

[[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_1291438696}[Hello]{lang="EN-US"}[报文被丢弃，原因是]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度非法]{style="font-family:宋体"}

[[ADJ: Sent a P2P Hello packet on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x843664682}

[[端口上发送]{style="font-family:宋体"}[P2P ]{lang="EN-US"}]{#struct_0_x1051_20145_x1516880084}[Hello]{lang="EN-US"}[报文，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: The circuit *circuitName* is silent. IIH not sent.]{lang="EN-US"}]{#struct_0_x1051_20145_1494987487}

[[端口处于]{style="font-family:宋体"}[silent]{lang="EN-US"}]{#struct_0_x1051_20145_x1557607383}[状态，]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1300421514}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x894658560}[打开]{style="font-family:宋体"}[SPBM Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm adj-packet]{lang="EN-US"}]{#struct_0_x1051_20145_x1501396591}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_1494987486}[端口]{style="font-family:宋体"}[GigabitEthernet0/1/3]{lang="EN-US"}[下使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，]{style="font-family:宋体"}[输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> sysem-view]{lang="EN-US"}]{#struct_0_x1051_20145_x1557541847}

[\[Sysname\] interface gigabitethernet 0/1/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet0/1/3\] spbm enable]{lang="EN-US"}

[\*Sep 18 14:13:14:386 2012 Sysname SPBM/7/SPBM_1_ADJ: -MDC=1;]{lang="EN-US"}

[ADJ: Sent a P2P Hello packet on circuit(GigabitEthernet0/1/3).]{lang="EN-US"}

*[// ]{lang="EN-US"}[端口]{style="font-family:
宋体"}[GigabitEthernet0/1/3]{lang="EN-US"}[上发送]{style="font-family:宋体"}[P2P Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[\*Sep 18 14:13:17:445 2012 Sysname SPBM/7/SPBM_1_ADJ: -MDC=1;]{lang="EN-US"}

[ADJ: Received a P2P Hello packet from 0011.2200.0a01 on circuit(GigabitEthernet0/1/3).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1051_20145_x1213731541}*[端口]{style="font-family:宋体"}[GigabitEthernet0/1/3]{lang="EN-US"}[接收到系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0011.2200.0a01]{lang="EN-US"}[的设备发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#1228622240 .myid}
[]{#_Toc404797998}[]{#struct_0_x1051_20145_332392759}

**SPBM \-- SPBM调试命令 \-- debugging spbm agreement-protocol**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x143870555}

[**[debugging spbm agreement-protocol]{lang="EN-US"}**[ { **all** \| **packet** \| **prt** \| **pst** \| **topology** }]{lang="EN-US"}]{#struct_0_x1051_20145_x1853091379}

[**[undo debugging spbm agreement-protocol ]{lang="EN-US"}**[{ **all** \| **packet** \| **prt** \| **pst** \| **topology** }]{lang="EN-US"}]{#struct_0_x1051_20145_1508401944}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1632593924}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_1494987489}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1557738455}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1925542102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x823539442}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_276175536}

[**[all]{lang="EN-US"}**]{#struct_0_x1051_20145_1837796920}[：表示]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1051_20145_610544518}[：表示]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[的接收摘要报文调试信息开关。]{style="font-family:宋体"}

[**[prt]{lang="EN-US"}**]{#struct_0_x1051_20145_x1026601744}[：表示]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[端口角色迁移的调试信息开关。]{style="font-family:宋体"}

[**[pst]{lang="EN-US"}**]{#struct_0_x1051_20145_1697238122}[：表示]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[端口状态迁移的调试信息开关。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**]{#struct_0_x1051_20145_1494987488}[：表示]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[拓扑变化处理的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1557672919}

[**[debugging spbm agreement-protocol]{lang="EN-US"}**]{#struct_0_x1051_20145_x367443529}[命令用来打开]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm agreement-protocol]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[SPBM AP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}]{#struct_0_x1051_20145_638942999}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging spbm agreement-protocal packet]{lang="EN-US"}]{#struct_0_x1051_20145_1102588213}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2047722026}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_233752608}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_540745599}

[[FLUSH: Received a digest on port(*PortName*), RxAN is *an-value*, RxDAN is d*an-value*, RxDigest is [*digest-value*]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_714300008}

[[接收到摘要报文，包括端口名]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987491}[、摘要信息]{style="font-family:宋体"}[*[digest-value]{lang="EN-US"}*]{.TableTextChar}[、收到的序列号]{style="font-family:宋体"}[RxAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[an-value]{lang="EN-US"}*[ ]{lang="EN-US"}[以及]{style="font-family:宋体"} [收到的确认序列号]{style="font-family:宋体"}[RxDAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[dan-value]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging spbm agreement-protocal prt]{lang="EN-US"}]{#struct_0_x1051_20145_x1557214166}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2049443893}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_898908500}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_964876290}

[[FLUSH: Port(*PortName*) entered *state-value* state in ECT *ect-index*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1716815770}

[[端口角色迁移信息，包括端口名]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987490}[、新角色]{style="font-family:宋体"}*[state-value]{lang="EN-US"}*[以及]{style="font-family:宋体"}[ECT]{lang="EN-US"}[索引，新状态]{style="font-family:宋体"}*[state-value]{lang="EN-US"}*[的取值如下：]{style="font-family:宋体"}

[[PRT%ROOT_PORT]{lang="EN-US"}]{#struct_0_x1051_20145_x1557148630}[、]{style="font-family:宋体"}[PRT%ROOT_PROPOSED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_AGREED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_SYNCED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_REROOT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_REROOTED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_DISCARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_FORWARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIS_DESIPORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIS_AGREED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIS_SYNCED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIS_RETIRED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIS_DISCARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIS_FORWARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%STATE_INVALID]{lang="EN-US"}

[[各字段]{style="font-family:宋体"}[%]{lang="EN-US"}]{#struct_0_x1051_20145_x1094051478}[之前表示状态机名称，]{style="font-family:宋体"}[%]{lang="EN-US"}[之后表示具体状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging spbm agreement-protocal pst]{lang="EN-US"}]{#struct_0_x1051_20145_645613670}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2079532707}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_703679369}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_1494987493}

[[FLUSH: Port(*PortName*) entered *state-value* state in ECT *ect-index*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1557345238}

[[端口状态迁移信息，包括端口名]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_x1051_20145_2088418886}[、新状态]{style="font-family:宋体"}*[state-value]{lang="EN-US"}*[以及]{style="font-family:宋体"}[ECT]{lang="EN-US"}[索引]{style="font-family:宋体"}*[ect-index]{lang="EN-US"}*[，新状态]{style="font-family:宋体"}*[state-value]{lang="EN-US"}*[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PST%PST_DISCARDING]{lang="EN-US"}]{#struct_0_x1051_20145_286181013}[：丢弃状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PST%PST_LEARNING]{lang="EN-US"}]{#struct_0_x1051_20145_1848657478}[：学习状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PST%PST_FORWARDING]{lang="EN-US"}]{#struct_0_x1051_20145_x739181434}[：转发状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PST%PST_INVALID]{lang="EN-US"}]{#struct_0_x1051_20145_1494987492}[：非法状态]{lang="EN-US" style="font-family:
  宋体"}

[[各字段]{style="font-family:宋体"}[%]{lang="EN-US"}]{#struct_0_x1051_20145_x1557279702}[之前表示状态机名称，]{style="font-family:宋体"}[%]{lang="EN-US"}[之后表示具体状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging spbm agreement-protocal topo]{lang="EN-US"}]{#struct_0_x1051_20145_x808382096}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2080322192}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_206047188}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x206848926}

[[FLUSH: Topology change started, new digest is [*digest-value*]{.TableTextChar}, edge count is [*edge-value*]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_1271895744}

[[接收到拓扑变化开始通知，包括新摘要以及拓扑边数]{style="font-family:宋体"}]{#struct_0_x1051_20145_1704432084}

[[FLUSH: Topology change ended, new digest is [*digest-value*]{.TableTextChar}, edge count is [*edge-value*]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_1494987479}

[[接收到拓扑变化结束通知，包括新摘要以及拓扑边数]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1557738460}

[[FLUSH: Received a port role change message in ECT *ect-index* on port(*PortName*), the new port role is [*role-name*]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_1609844771}

[[接收到端口角色变化通知，包括]{style="font-family:宋体"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_824964436}[、端口名以及新的端口角色，端口角色名]{style="font-family:宋体"}[*[role-name]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_x1051_20145_933857975}[：根端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DESIGNATED]{lang="EN-US"}]{#struct_0_x1051_20145_343106266}[：指定端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALTERNATE]{lang="EN-US"}]{#struct_0_x1051_20145_1494987478}[：不在树上端口]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1557672924}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x1483123240}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[SPBM AP]{lang="EN-US"}[消息调试信息开关，当接收到拓扑变化通知时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm agreement-protocal all]{lang="EN-US"}]{#struct_0_x1051_20145_x76827937}

[\*Sep 17 10:41:12:183 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Received a digest on port(GigabitEthernet0/1/3), RxAN is 1, RxDAN is 2,]{lang="EN-US"}

[ RxDigest is 0000000000000000000.]{lang="EN-US"}

[\*Sep 17 10:41:13:034 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Topology change started, new digest is 000000183d64c91f892, edge count is 0.]{lang="EN-US"}

[\*Sep 17 10:41:13:038 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Topology change ended, new digest is 000000183d64c91f892, edge count is 0.]{lang="EN-US"}

[\*Sep 17 10:41:15:876 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Received a port role change message in ECT 1 on port(GigabitEthernet0/1/3), the new port role is ROOT.]{lang="EN-US"}

[\*Sep 17 10:41:15:876 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_PORT state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:876 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_AGREED state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_REROOT state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_FORWARD state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PST%PST_DISCARDING state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PST%PST_FORWARDING state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_REROOTED state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Received a port role change message in ECT-Index 1 on circuit(GigabitEthernet0/1]{lang="EN-US"}

[/3), the new port role is DESIGNATED.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%DESIS_DESIPORT state in ECT 1.]{lang="EN-US"}

[\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;]{lang="EN-US"}

[FLUSH: Port(GigabitEthernet0/1/3) entered PRT%DESIS_AGREED state in ECT 1.]{lang="EN-US"}

::: {#-147300003 .myid}
[]{#_Toc404797999}[]{#struct_0_x1051_20145_x613289889}

**SPBM \-- SPBM调试命令 \-- debugging spbm error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1750860335}

[**[debugging spbm error]{lang="EN-US"}**]{#struct_0_x1051_20145_1492722699}

[**[undo debugging spbm error]{lang="EN-US"}**]{#struct_0_x1051_20145_1746038543}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1790777167}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x76827938}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x613289892}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_1751581232}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1989234733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x115897932}

[[无]{style="font-family:宋体"}]{#struct_0_x1051_20145_705644477}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_2145466420}

[**[debugging spbm error]{lang="EN-US"}**]{#struct_0_x1051_20145_1566604345}[命令用来打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x332913167}[错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging spbm error]{lang="EN-US"}]{#struct_0_x1051_20145_x76827935}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2079294223}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x613289887}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_1751253551}

[[ADJ: IF index *if-index* set ADJ socket option [*operation*]{.TableTextChar} failed.]{lang="EN-US"}]{#struct_0_x1051_20145_1921828742}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1051_20145_x2118395980}[选项失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x76827936}[：端口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x613289890}[[：选项]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[ADJ: Failed to start Level-1 Hello timer.]{lang="EN-US"}]{#struct_0_x1051_20145_x76827933}

[[Hello]{lang="EN-US"}]{#struct_0_x1051_20145_x613289885}[定时器创建失败]{style="font-family:宋体"}

[[ADJ: System state is disabled.]{lang="EN-US"}]{#struct_0_x1051_20145_1751122479}

[[进程处于]{style="font-family:宋体"}[disable]{lang="EN-US"}]{#struct_0_x1051_20145_x76827934}[状态]{style="font-family:宋体"}

[[ADJ: Failed to start hold timer.]{lang="EN-US"}]{#struct_0_x1051_20145_x76827931}

[[邻居维持定时器创建失败]{style="font-family:宋体"}]{#struct_0_x1051_20145_x76827932}

[[ADJ: Failed to encode SPB MCID sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x613289886}

[[封装]{style="font-family:宋体"}[SPB-MCID sub TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1751319087}[失败]{style="font-family:宋体"}

[[ADJ: Failed to encode SPB digest sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x2039065240}

[[封装]{style="font-family:宋体"}[SPB-Digest sub TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x648433940}[失败]{style="font-family:宋体"}

[[ADJ: Failed to encode SPB Base VLAN-Identifiers sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_x76827945}

[[封装]{style="font-family:宋体"}[SPB-Base VID sub TLV]{lang="EN-US"}]{#struct_0_x1051_20145_960688225}[失败]{style="font-family:宋体"}

[[ADJ: Failed to encode packet header on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x971220664}

[[封装专用报文头编码失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_602931671}[表示端口名]{style="font-family:宋体"}

[[ADJ: Failed to encode area address TLV on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1767844993}

[[封装区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x76827946}[编码失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Failed to encode protocol support TLV on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_960688222}

[[封装协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x971220667}[编码失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Failed to encode graceful restart TLV on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_603128279}

[[封装优雅重启]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143073}[失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Failed to encode MT-Port-Cap TLV on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1695599943}

[[封装]{style="font-family:宋体"}[MT-Port-Cap TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x974448813}[失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Failed to send P2P Hello packet. Reason: *reason*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1159438938}

[[P2P Hello]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143074}[报文发送失败，其中]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[表示失败原因]{style="font-family:宋体"}

[[ADJ: Failed to send P2P Hello packet. Reason: socket not create.]{lang="EN-US"}]{#struct_0_x1051_20145_x2098884470}

[[P2P Hello]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143071}[报文因套接字未创建发送失败]{style="font-family:宋体"}

[[ADJ: Failed to send P2P Hello packet. Reason: out of memory.]{lang="EN-US"}]{#struct_0_x1051_20145_1436567939}

[[P2P Hello]{lang="EN-US"}]{#struct_0_x1051_20145_x2084587866}[报文因内存不足发送失败]{style="font-family:宋体"}

[[ADJ: Failed to create P2P Hello timer on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1349580093}

[[P2P hello]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143072}[定时器创建失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: LSP with too long area address.]{lang="EN-US"}]{#struct_0_x1051_20145_1033283412}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_709134839}[报文中携带的区域地址长度超过最大区域地址长度，丢弃报文]{style="font-family:宋体"}

[[UPDT:  LSP with wrong area address length.]{lang="EN-US"}]{#struct_0_x1051_20145_1772394999}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143069}[报文中携带的区域地址长度错误，丢弃报文]{style="font-family:宋体"}

[[UPDT:  LSP with invalid area address.]{lang="EN-US"}]{#struct_0_x1051_20145_1080272043}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_830901890}[报文中携带的区域地址长度不合法，丢弃报文]{style="font-family:宋体"}

[[MAIN: Failed to process the LSP lifetime change event.]{lang="EN-US"}]{#struct_0_x1051_20145_829088331}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143070}[报文生存时间变化时间失败]{style="font-family:宋体"}

[[MAIN: Failed to activate the interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x129516002}

[[端口激活失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x21161981}[表示端口名]{style="font-family:宋体"}

[[MAIN: Failed to process the circuit MTU change event.]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143067}

[[端口]{style="font-family:宋体"}]{#struct_0_x1051_20145_629933349}[MTU]{lang="EN-US"}[变化处理失败]{style="font-family:宋体"}

[[MAIN: The event type and disable phase mismatched.]{lang="EN-US"}]{#struct_0_x1051_20145_702405819}

[[进程的]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1901936839}[Reset]{lang="EN-US"}[状态和阶段不一致]{style="font-family:宋体"}

[[UPDT: Wrong format of neighbor TLV in LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143068}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x485811898}[报文中携带的邻居格式错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: Wrong format of I-SID TLV in LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x55133680}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143081}[报文中携带的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[格式错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: Wrong format of MT-Capability TLV in LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_1435847043}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_1922020934}[报文中携带的多拓扑能力格式错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: Wrong format of Instance sub-TLV in LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_539046881}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143082}[报文中携带的实例格式错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: Supported protocol wrong.]{lang="EN-US"}]{#struct_0_x1051_20145_1032562516}

[[协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x827327057}[中携带的协议支持与本系统不匹配]{style="font-family:宋体"}

[[UPDT: Failed to create UPDT sockets.]{lang="EN-US"}]{#struct_0_x1051_20145_305509087}

[[创建]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x34202488}[套接字失败]{style="font-family:宋体"}

[[UPDT: Bad TLV in the received LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x762298890}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_305509086}[报文中携带的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[错误（该]{style="font-family:宋体"}[TLV]{lang="EN-US"}[没有长度字节），丢弃报文]{style="font-family:宋体"}

[[UPDT: Bad TLV length in the received LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x34202487}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x762298885}[报文中携带的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: Failed to start CSNP timer on circuit *circuitName.*]{lang="EN-US"}]{#struct_0_x1051_20145_305509089}

[[端口]{style="font-family:宋体"}]{#struct_0_x1051_20145_x34202474}[CSNP]{lang="EN-US"}[定时器创建失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: Failed to start PSNP timer on circuit *circuitName.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1571602950}

[[端口]{style="font-family:宋体"}]{#struct_0_x1051_20145_305509088}[PSNP]{lang="EN-US"}[定时器创建失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: Failed to start P2P retransmit timer on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x34202473}

[[端口]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1571602945}[P2P]{lang="EN-US"}[重传]{style="font-family:宋体"}[定时器创建失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: Failed to start LSP flood timer on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_305509091}

[[端口]{style="font-family:宋体"}]{#struct_0_x1051_20145_1922112654}[LSP]{lang="EN-US"}[泛洪]{style="font-family:宋体"}[定时器创建失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: Failed to stop LSP flood timer on circuit *circuitName.*]{lang="EN-US"}]{#struct_0_x1051_20145_305509090}

[[关闭端口]{style="font-family:宋体"}]{#struct_0_x1051_20145_1922112655}[LSP]{lang="EN-US"}[泛洪定时器失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: Failed to stop level-1 timer on circuit *circuitName.*]{lang="EN-US"}]{#struct_0_x1051_20145_508370172}

[[关闭端口]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_x1051_20145_305509093}[定时器失败，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: LSP information update failed.]{lang="EN-US"}]{#struct_0_x1051_20145_1922112652}

[[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_508304636}[中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息更新失败]{style="font-family:宋体"}

[[UPDT: LSP insert failed.]{lang="EN-US"}]{#struct_0_x1051_20145_305509092}

[[向]{style="font-family:宋体"}]{#struct_0_x1051_20145_1922112653}[LSP]{lang="EN-US"}[中添加邻居信息失败]{style="font-family:宋体"}

[[UPDT: Bad TLV length in the process of LSP authentication.]{lang="EN-US"}]{#struct_0_x1051_20145_305509079}

[[认证]{style="font-family:宋体"}]{#struct_0_x1051_20145_303504534}[LSP]{lang="EN-US"}[时]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: LSP\'s sequence number is 0.]{lang="EN-US"}]{#struct_0_x1051_20145_x931871346}

[[接收到的]{style="font-family:宋体"}]{#struct_0_x1051_20145_305509078}[LSP]{lang="EN-US"}[报文的序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[UPDT: Illegal IS type in level-1 LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_303504535}

[[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x931871347}[报文的]{style="font-family:宋体"}[IS-TYPE]{lang="EN-US"}[字段非法，丢弃报文]{style="font-family:宋体"}

[[UPDT: Checksum is zero.]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806049}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1979118033}[报文的校验和为]{style="font-family:宋体"}[0]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[UPDT: Checksum error.]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806050}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x56738196}[报文的校验和错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: Failed to set UPDT socket option.]{lang="EN-US"}]{#struct_0_x1051_20145_1598789015}

[[设置]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1650806047}[UPDT]{lang="EN-US"}[套接字失败]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because its size(]{lang="EN-US"}]{#struct_0_x1051_20145_1509280209}*[PDUSize]{lang="EN-US"}*[) is greater than received buffer size(]{lang="EN-US"}*[reveiveBufSize]{lang="EN-US"}*[).]{lang="EN-US"}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806048}[报文长度大于接收缓冲区大小，丢弃报文]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because its size(]{lang="EN-US"}]{#struct_0_x1051_20145_x413034092}*[PDUSize]{lang="EN-US"}*[) is less than common PDU header size(]{lang="EN-US"}*[PDUCommonHeaderSize]{lang="EN-US"}*[).]{lang="EN-US"}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x451042276}[报文长度小于公共报文头大小，丢弃报文]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because its size(]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806045}*[PDUSize]{lang="EN-US"}*[) is less than fixed PDU header size(]{lang="EN-US"}*[PDUFixedHeaderSize]{lang="EN-US"}*[).]{lang="EN-US"}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_x1051_20145_346480795}[报文长度小于固定报文头大小，丢弃报文]{style="font-family:宋体"}

[[UPDT: The PDU was discarded due to length mismatch: receive length= ]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806046}*[recvLen]{lang="EN-US"}*[, encode length= ]{lang="EN-US"}*[encodeLen.]{lang="EN-US"}*

[[LSP/SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x1219603146}[报文长度和报文中的长度字段不相等，丢弃报文]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because the SPBM process is not available.]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806043}

[[进程不可用，忽略]{style="font-family:宋体"}]{#struct_0_x1051_20145_x460088259}[LSP/SNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because circuit *circuitName* was being deleted.]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806044}

[[端口正在删除，忽略]{style="font-family:宋体"}]{#struct_0_x1051_20145_1912564736}[LSP/SNP]{lang="EN-US"}[报文，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because circuit *circuitName* was not up.]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806057}

[[端口链路状态没有]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x1051_20145_1509345745}[，忽略]{style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because circuit *circuitName* was in silence state.]{lang="EN-US"}]{#struct_0_x1051_20145_x807769321}

[[端口处于]{style="font-family:宋体"}[Silence]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806058}[状态，忽略]{style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: The PDU was discarded due to LSP or SNP PDU common header error.]{lang="EN-US"}]{#struct_0_x1051_20145_x412968556}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x841501985}[公共报文头错误，丢弃报文]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because no active adjacency exist on cicuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x969570862}

[[端口上没有激活的邻居，忽略]{style="font-family:宋体"}]{#struct_0_x1051_20145_x841501986}[LSP/SNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[UPDT: Failed to process SNP PDU.]{lang="EN-US"}]{#struct_0_x1051_20145_x969636398}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x841501983}[报文处理失败]{style="font-family:宋体"}

[[UPDT: Failed to process LSP PDU.]{lang="EN-US"}]{#struct_0_x1051_20145_x969964078}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x841501984}[报文处理失败]{style="font-family:宋体"}

[[UPDT: The PDU was discarded because received PDU was not LSP or SNP.]{lang="EN-US"}]{#struct_0_x1051_20145_x969505326}

[[接收到的报文不是]{style="font-family:宋体"}]{#struct_0_x1051_20145_x841501981}[LSP]{lang="EN-US"}[或]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文，丢弃报文]{style="font-family:宋体"}

[[UPDT: LSP size(]{lang="EN-US"}]{#struct_0_x1051_20145_x969833006}*[LSPSize]{lang="EN-US"}*[) is larger than circuit MTU(]{lang="EN-US"}*[circuitMtu]{lang="EN-US"}*[).]{lang="EN-US"}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x841501982}[报文大小大于发送端口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[*LSPSize*]{lang="EN-US"}]{#struct_0_x1051_20145_x841501979}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitMtu]{lang="EN-US"}*]{#struct_0_x1051_20145_x841501980}[：发送端口的]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}

[[UPDT: Failed to send LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x969767470}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x841501993}[报文发送失败]{style="font-family:宋体"}

[[UPDT: Failed to send level-1 PSNP PDU.]{lang="EN-US"}]{#struct_0_x1051_20145_x969964077}

[[level-1 P]{lang="EN-US"}]{#struct_0_x1051_20145_x841501994}[SNP]{lang="EN-US"}[发送失败]{style="font-family:宋体"}

[[UPDT: Failed to send level-1 CSNP PDU.]{lang="EN-US"}]{#struct_0_x1051_20145_x969505325}

[[level-1 C]{lang="EN-US"}]{#struct_0_x1051_20145_1497150175}[SNP]{lang="EN-US"}[发送失败]{style="font-family:宋体"}

[[UPDT: Invalid LSP-ID reported in SNP.]{lang="EN-US"}]{#struct_0_x1051_20145_1497150174}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2012653423}[报文中的]{style="font-family:宋体"}[LSP ENTRY]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[UPDT: Wrong LSP entry TLV length(]{lang="EN-US"}]{#struct_0_x1051_20145_1497150177}*[LSPEntryTlvLen]{lang="EN-US"}*[) in SNP.]{lang="EN-US"}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2012456815}[报文中的]{style="font-family:宋体"}[LSP ENTRY TLV]{lang="EN-US"}[长度错误，其中]{style="font-family:宋体"}*[LSPEntryTlvLen]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LSP ENTRY TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[UPDT: SNP contain too many LSP entries.]{lang="EN-US"}]{#struct_0_x1051_20145_1497150176}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2012522351}[报文中的]{style="font-family:宋体"}[LSP ENTRY]{lang="EN-US"}[个数多过]{style="font-family:宋体"}

[[UPDT: Invalid TLV in SNP.]{lang="EN-US"}]{#struct_0_x1051_20145_1497150179}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_1497150178}[报文中的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[UPDT: Wrong TLV length in SNP.]{lang="EN-US"}]{#struct_0_x1051_20145_1497150181}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2012325754}[报文中的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度错误]{style="font-family:宋体"}

[[UPDT: Failed to install LSP with seq number zero.]{lang="EN-US"}]{#struct_0_x1051_20145_x96292031}

[[安装序列号为]{style="font-family:宋体"}]{#struct_0_x1051_20145_x96292034}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[UPDT: Invalid type of SNP PDU.]{lang="EN-US"}]{#struct_0_x1051_20145_x96292033}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x96292028}[报文类型非法]{style="font-family:宋体"}

[[UPDT: Failed to create zero-frag LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x96292027}

[[创建零分片失败]{style="font-family:宋体"}]{#struct_0_x1051_20145_x449175132}

[[UPDT: Failed to initiate zero-frag LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607166}

[[初始化零分片失败]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2052607165}

[[UPDT: LSP\'s PDU length is smaller than LSP\'s header length.]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607176}

[[安装]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_x1051_20145_x1151641879}[长度小于头长度的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[UPDT: Illegal LSP level.]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607175}

[[安装非]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1051_20145_286044993}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[UPDT: Illegal IS type in level-1 LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x2015488107}

[[安装非]{style="font-family:宋体"}]{#struct_0_x1051_20145_286044990}[IS_UPDT_LSP_L1_ISTYPE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[UPDT: SNP\'s PDU length is smaller than SNP\'s header length.]{lang="EN-US"}]{#struct_0_x1051_20145_286044991}

[[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2015488109}[的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[长度小于]{style="font-family:宋体"}[SNP]{lang="EN-US"}[的头长度]{style="font-family:宋体"}

[[UPDT: Bad TLV in the received SNP.]{lang="EN-US"}]{#struct_0_x1051_20145_286044996}

[[收到的]{style="font-family:宋体"}[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2015488112}[里存在没有]{style="font-family:宋体"}[Length]{lang="EN-US"}[字节的]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[UPDT: Bad TLV in the received LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_286044997}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_286044994}[里存在没有]{style="font-family:宋体"}[Length]{lang="EN-US"}[字节的]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[UPDT: Failed to add area address *address.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2015488114}

[[添加区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_286044995}[失败，其中]{style="font-family:宋体"}*[address]{lang="EN-US"}*[表示区域地址]{style="font-family:宋体"}

[[UPDT: Failed to add protocol support *protocol.*]{lang="EN-US"}]{#struct_0_x1051_20145_286044984}

[[添加协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x59172978}[失败，其中]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[表示协议]{style="font-family:宋体"}

[[UPDT: Failed to add host name *name.*]{lang="EN-US"}]{#struct_0_x1051_20145_286044985}

[[添加]{style="font-family:宋体"}[host name TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270144}[失败，其中]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示主机名]{style="font-family:宋体"}

[[UPDT: Failed to delete host name *name.*]{lang="EN-US"}]{#struct_0_x1051_20145_x518136812}

[[删除]{style="font-family:宋体"}[host name TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270143}[失败，其中]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示主机名]{style="font-family:宋体"}

[[UPDT: Failed to add Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*]{lang="EN-US"}]{#struct_0_x1051_20145_1854516183}

[[添加]{style="font-family:宋体"}[Instance TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270146}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270140}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[u-bit]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270142}[：]{lang="EN-US" style="font-family:宋体"}[u]{lang="EN-US"}[比特位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-algorithm]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270152}[：]{lang="EN-US" style="font-family:
  宋体"}[ECT]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Failed to modify Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*]{lang="EN-US"}]{#struct_0_x1051_20145_288497778}

[[修改]{style="font-family:宋体"}[Instance TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270151}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966079}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[u-bit]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966081}[：]{lang="EN-US" style="font-family:宋体"}[u]{lang="EN-US"}[比特位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-algorithm]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966075}[：]{lang="EN-US" style="font-family:
  宋体"}[ECT]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Failed to delete Instance sub-TLV: B-VLAN= *bvlan-number*]{lang="EN-US"}]{#struct_0_x1051_20145_x860966078}

[[删除]{style="font-family:宋体"}[Instance TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1714954938}[失败，其中]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{style="font-family:宋体"}

[[UPDT: Failed to add I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*]{lang="EN-US"}]{#struct_0_x1051_20145_x860966077}

[[添加]{style="font-family:宋体"}[I-SID TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x860966088}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686080}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686078}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[t-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686084}[：]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[r-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686082}[：]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Failed to modify I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*]{lang="EN-US"}]{#struct_0_x1051_20145_1477686083}

[[修改]{style="font-family:宋体"}[I-SID TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1477686072}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129344}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129346}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[t-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129339}[：]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[r-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129341}[：]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Failed to delete I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid.*]{lang="EN-US"}]{#struct_0_x1051_20145_779262992}

[[删除]{style="font-family:宋体"}[I-SID TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x94129352}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444480}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444481}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Failed to add neighbor TLV: neighbor system ID= *system-id*, cost= *cost.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2050444476}

[[添加邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1230234776}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444477}[：邻居系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444487}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Failed to modify neighbor TLV: neighbor system ID= *system-id*, cost= *cost.*]{lang="EN-US"}]{#struct_0_x1051_20145_288207680}

[[修改邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_288207681}[失败，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[system-id]{lang="EN-US"}]{#struct_0_x1051_20145_x1897180120}[：邻居系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_x1051_20145_288207678}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Failed to delete neighbor TLV: neighbor system ID= *system-id.*]{lang="EN-US"}]{#struct_0_x1051_20145_288207679}

[[删除邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1588483104}[失败，其中]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[表示邻居系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: Wrong format of authentication TLV in the SNP.]{lang="EN-US"}]{#struct_0_x1051_20145_288207685}

[[CSNP/PSNP]{lang="EN-US"}]{#struct_0_x1051_20145_288207683}[报文中的认证]{style="font-family:宋体"}[TLV]{lang="EN-US"}[的长度或模式字段错误，报文丢弃]{style="font-family:宋体"}

[[UPDT: Wrong format of authentication TLV in the LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_288207672}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107456}[报文中的认证]{style="font-family:宋体"}[TLV]{lang="EN-US"}[的长度或模式字段错误，报文丢弃]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1198238054}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x958232339}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[错误信息调试信息开关，输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm error]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107455}

[\*Sep 18 11:33:39:706 2012 Sysname SPBM/7/SPBM_1_ERR: -MDC=1;]{lang="EN-US"}

[UPDT: Failed to stop LSP flood timer on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

::: {#-1329932804 .myid}
[]{#_Toc404798000}[]{#struct_0_x1051_20145_367845887}

**SPBM \-- SPBM调试命令 \-- debugging spbm event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_2065532979}

[**[debugging spbm event]{lang="EN-US"}**]{#struct_0_x1051_20145_1510092965}

[**[undo debugging spbm event]{lang="EN-US"}**]{#struct_0_x1051_20145_x112124940}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x339237758}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x18775013}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1033717008}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107458}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x391669000}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_663424244}

[[无]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1778458483}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_610357645}

[**[debugging spbm event]{lang="EN-US"}**]{#struct_0_x1051_20145_x2080575791}[命令用来打开]{style="font-family:宋体"}[SPBM ]{lang="EN-US"}[事件的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM ]{lang="EN-US"}[事件的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM ]{lang="EN-US"}]{#struct_0_x1051_20145_x59813640}[事件的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging spbm event]{lang="EN-US"}]{#struct_0_x1051_20145_321064663}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2098898008}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1668107457}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_1530645301}

[[ADJ: Received Hello timer reset event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1186450897}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_1057781493}[模块端口重置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[ADJ: Received digest change event on interface *circuitName*. Send speed is *state*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1729843186}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_251619684}[模块摘要变化事件处理，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107452}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[state]{lang="EN-US"}*]{#struct_0_x1051_20145_1127360774}[：]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器状态]{lang="EN-US" style="font-family:宋体"}

[[ADJ: Received state change event on interface *circuitName*: *eventType*.]{lang="EN-US"}]{#struct_0_x1051_20145_1355035650}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_1537728013}[模块收到端口状态改变事件，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_1929034128}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventType]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107451}[：事件类型]{lang="EN-US" style="font-family:宋体"}

[[ADJ: Received Instance 4092 delete event.]{lang="EN-US"}]{#struct_0_x1051_20145_x1601522581}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_x1024301686}[模块收到]{style="font-family:宋体"}[Instance 4092]{lang="EN-US"}[删除消息]{style="font-family:宋体"}

[[ADJ: Received control address change event.]{lang="EN-US"}]{#struct_0_x1051_20145_x1433422493}

[[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_x539996709}[模块收到]{style="font-family:宋体"}[control address]{lang="EN-US"}[变化事件]{style="font-family:宋体"}

[[FLUSH: Notified  MSTP B-VLAN change, message length= *length-value*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107454}

[[FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_1933929828}[模块发送]{style="font-family:宋体"}[MSTP B-VLAN]{lang="EN-US"}[变化消息，其中]{style="font-family:宋体"}*[length-value]{lang="EN-US"}*[表示消息长度]{style="font-family:宋体"}

[[FLUSH: [*Operation*]{.TableTextChar} SPBM on interface *circuitName*, result= *result*.]{lang="EN-US"}]{#struct_0_x1051_20145_x2083503057}

[[FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_x785366943}[模块发送接口使能]{style="font-family:宋体"}[/]{lang="EN-US"}[去使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x1668107464}[：使能或去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803392}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803394}[：处理结果]{lang="EN-US" style="font-family:宋体"}

[[MAIN: Notified to modify P2P Hello timer on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_155620675}

[[通知邻居模块端口]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1051_20145_x858803393}[定时器配置发生变化，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Notified to modify SPB Base VLAN-Identifiers sub-TLV.]{lang="EN-US"}]{#struct_0_x1051_20145_155161923}

[[通知修改]{style="font-family:宋体"}[SPB Base VLAN-Identifiers sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1513007862}

[[MAIN: *flag-value* SPBM PDU up to CPU on interface *circuitName*, control mac: *mac-addr*, result: *result*.]{lang="EN-US"}]{#struct_0_x1051_20145_x858803387}

[[通知驱动使能报文上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1051_20145_155424068}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag-value]{lang="EN-US"}*]{#struct_0_x1051_20145_622011722}[：是否使能标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_212246877}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mac-addr]{lang="EN-US"}*]{#struct_0_x1051_20145_1535298746}[：]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803390}[：处理结果]{lang="EN-US" style="font-family:宋体"}

[[MAIN: Notified metric change event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_155358531}

[[通知邻居模块端口]{style="font-family:宋体"}[cost]{lang="EN-US"}]{#struct_0_x1051_20145_1544412517}[配置发生变化，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Refreshed the SPBM interface parameter on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_864180764}

[[刷新端口参数变化，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803389}[表示端口名]{style="font-family:宋体"}

[[MAIN: Received delete event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_155817284}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_1474247615}[模块接收到端口删除事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Received pre-delete event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1312324687}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x858803400}[模块接收到端口删除前的]{style="font-family:宋体"}[Deactive]{lang="EN-US"}[事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Received active event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1729336636}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x835761463}[模块接收到板插入事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示]{style="font-family:宋体"}[端口名]{style="font-family:宋体"}

[[MAIN: Received deactive event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x858803399}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_155817283}[模块接收到板拔出事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Received join aggregation group event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1474247612}

[[端口加入聚合组，清除配置，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_1311997007}[表示端口名]{style="font-family:宋体"}

[[MAIN: Received leave aggregation group event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848768}

[[端口离开聚合组，清除配置，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1257599187}[表示端口名]{style="font-family:宋体"}

[[MAIN: Received up event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_26690626}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_1158425828}[模块接收到物理端口]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[到]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Received down event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848769}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x1257664723}[模块接收到物理端口]{style="font-family:宋体"}[UP]{lang="EN-US"}[到]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Received speed change event on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x769155723}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_1479848766}[模块接收到物理端口速率变化事件，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[MAIN: Notified interface state change: *changestate*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1256943827}

[[通知端口状态变化，其中]{style="font-family:宋体"}*[changestate]{lang="EN-US"}*]{#struct_0_x1051_20145_x104493657}[表示状态变化]{style="font-family:宋体"}

[[MAIN: Received time message from SPBM to License daemon, ignored.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848767}

[[License Daemon]{lang="EN-US"}]{#struct_0_x1051_20145_x1257009363}[接收到定时通知消息]{style="font-family:宋体"}

[[MAIN: Started timer to reconnect to License daemon. Time value is *Millisecond* ms.]{lang="EN-US"}]{#struct_0_x1051_20145_x1275953189}

[[创建]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_1479848772}[进程与]{style="font-family:宋体"}[License]{lang="EN-US"}[进程的重连定时器，其中]{style="font-family:宋体"}*[Millisecond]{lang="EN-US"}*[表示定时器的当前事件间隔]{style="font-family:宋体"}

[[MAIN: Failed to start timer for reconnecting to License daemon.]{lang="EN-US"}]{#struct_0_x1051_20145_x1257205972}

[[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x1312421050}[进程与]{style="font-family:宋体"}[License]{lang="EN-US"}[进程的重连定时器创建失败]{style="font-family:宋体"}

[[MAIN: Trying to connect with MSTP.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848773}

[[尝试与]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1051_20145_x1257271508}[连接]{style="font-family:宋体"}

[[MAIN: Connected with MSTP successfully.]{lang="EN-US"}]{#struct_0_x1051_20145_1407640993}

[[与]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1051_20145_1479848770}[连接成功]{style="font-family:宋体"}

[[MAIN: Reset finished, reset reason= *event-id.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1257074900}

[[进程]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_x1051_20145_377635029}[结束事件，其中]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*[表示触发]{style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[MAIN: Processing with reset backinfo: module= *moudle-id*, event= *event-id*, phase= *phase-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848771}

[[进程]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_x1051_20145_x1257140436}[的阶段信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[moudle]{lang="EN-US"}*]{#struct_0_x1051_20145_1612716257}*[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：模块]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848760}*[-]{lang="EN-US"}[id]{lang="EN-US"}*[：触发]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[phase]{lang="EN-US"}*]{#struct_0_x1051_20145_x1257074899}*[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[所处的阶段]{lang="EN-US" style="font-family:宋体"}

[[MAIN: Invalid phase= *phase-id*, ignore event.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848761}

[[进程]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_x1051_20145_x1257140435}[的阶段错误，忽略消息，其中]{style="font-family:宋体"}*[phase-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[reset]{lang="EN-US"}[所处的阶段]{style="font-family:宋体"}

[[MAIN: Reset change into phase *phase-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1116167098}

[[进程]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_x1051_20145_x100617408}[进入下一个阶段，其中]{style="font-family:宋体"}*[phase-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[reset]{lang="EN-US"}[所处的阶]{style="font-family:宋体"}

[[MAIN: Received resetting message, triggered type= *event-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1930080395}

[[进程收到]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_x1051_20145_x48789686}[触发事件，其中]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*[表示触发]{style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[MAIN: Notified other module to enter reset process.]{lang="EN-US"}]{#struct_0_x1051_20145_x100617407}

[[通知其他模块进入]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_x1051_20145_x1929228427}[处理]{style="font-family:宋体"}

[[MAIN: LSP MTU changed from *oldLspBuf* to *newLspBuf*, notified UPDT MTU to change.]{lang="EN-US"}]{#struct_0_x1051_20145_x100617410}

[[进程]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1929556108}[缓冲区的大小改变，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[oldLspBuf]{lang="EN-US"}*]{#struct_0_x1051_20145_x1477629723}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[缓冲区之前的大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[newLspBuf]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617409}[：新的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[缓冲区的大小]{lang="EN-US" style="font-family:宋体"}

[[MAIN: Notified to add SPB Instance sub-TLV: process-ID= *proc-id*, ECT-index= *ect-index*, B-VLAN= *bvlan-number*, u-bit= *u-bit*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1930145931}

[[通知添加]{style="font-family:宋体"}[SPB Instance sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x100617404}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[proc]{lang="EN-US"}*]{#struct_0_x1051_20145_x1929293963}*[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x931320756}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617403}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[u-bit]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617405}[：]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[下是否已配置]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}

[[MAIN: Notified to modify SPB Instance sub-TLV: process-ID= *proc-id*, ECT-index= *ect-index*, B-VLAN= *bvlan-number*, u-bit= *bUsed*.]{lang="EN-US"}]{#struct_0_x1051_20145_x100617416}

[[通知修改]{style="font-family:宋体"}[SPB Instance sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x100617415}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[proc]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932544}*[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x905420852}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932543}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bUsed]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932552}[：]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[下是否已配置]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}

[[MAIN: Notified to delete SPB Instance sub-TLV: process-ID= *proc-id*, B-VLAN= *bvlan-number*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1711924370}

[[通知删除]{style="font-family:宋体"}[SPB Instance sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_281719616}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[proc]{lang="EN-US"}*]{#struct_0_x1051_20145_1688068467}*[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_281719617}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[MAIN: Notified AP mode change to *ap-mode*.]{lang="EN-US"}]{#struct_0_x1051_20145_1688068466}

[[通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_281719614}[模块]{style="font-family:宋体"}[AP]{lang="EN-US"}[模式变化，其中]{style="font-family:宋体"}*[ap-mode]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP ]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[MAIN: Notified ADJ to reset Hello timer.]{lang="EN-US"}]{#struct_0_x1051_20145_1688068469}

[[通知]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_1873466015}[模块重置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[MAIN: Received MSTP MCID change event.]{lang="EN-US"}]{#struct_0_x1051_20145_281719615}

[[接收到]{style="font-family:宋体"}[MSTP MCID]{lang="EN-US"}]{#struct_0_x1051_20145_1688068468}[变化事件]{style="font-family:宋体"}

[[MAIN: Received MSTP B-VLAN change event.]{lang="EN-US"}]{#struct_0_x1051_20145_281719620}

[[接收到]{style="font-family:宋体"}[MSTP B-VLAN]{lang="EN-US"}]{#struct_0_x1051_20145_x650583687}[变化信息]{style="font-family:宋体"}

[[MAIN: Trying to connect with SNMP.]{lang="EN-US"}]{#struct_0_x1051_20145_281719621}

[[尝试与]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1051_20145_x650583688}[建立连接]{style="font-family:宋体"}

[[MAIN: Connected with SNMP successfully.]{lang="EN-US"}]{#struct_0_x1051_20145_281719618}

[[与]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1051_20145_1688068481}[建立连接成功]{style="font-family:宋体"}

[[MAIN: Notified neighbor down event to UPDT.]{lang="EN-US"}]{#struct_0_x1051_20145_281719619}

[[通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_1688068480}[模块邻居]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[MAIN: Notified neighbor up event to UPDT.]{lang="EN-US"}]{#struct_0_x1051_20145_281719608}

[[通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x268246655}[模块邻居]{style="font-family:宋体"}[UP]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[MAIN: Notified ADJ that Instance 4092 had been deleted.]{lang="EN-US"}]{#struct_0_x1051_20145_281719609}

[[通知]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_x1051_20145_x268246656}[模块]{style="font-family:宋体"}[4092]{lang="EN-US"}[实例被删除]{style="font-family:宋体"}

[[MAIN: Started to set replicate mode on VSI *vsi-name*: VSI-index= *vsi-index*, replicate mode= *rep-mode*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595520}

[[设置复制模式，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_1207971382}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsi-name]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595519}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsi-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x1164878221}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[re]{lang="EN-US"}[p-mode]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595522}[：模式值]{lang="EN-US" style="font-family:宋体"}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x1924196500}[：]{style="font-family:宋体"}[ Ended to set replicate mode on VSI *vsi-name*: result= *result*]{lang="EN-US"}

[[设置复制模式完成，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1674595521}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsi-name]{lang="EN-US"}*]{#struct_0_x1051_20145_x1520911973}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[re]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595516}*[sul]{lang="EN-US"}[t]{lang="EN-US"}*[：返回值]{lang="EN-US" style="font-family:宋体"}

[[MAIN: Started to create VSI control block: VSI-name *vsi-name*, VSI-index= *vsi-index,* I-SID= *i-sid.*]{lang="EN-US"}]{#struct_0_x1051_20145_44975360}

[[创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595515}[控制块，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsi-name]{lang="EN-US"}*]{#struct_0_x1051_20145_448259887}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsi-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595518}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1564005134}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595517}[：]{style="font-family:宋体"}[ Notified multicast replicate mode to change. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number.*]{lang="EN-US"}

[[通知组播复制模式变化，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_1611059301}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595528}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1564201742}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595527}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_1611255909}[：]{style="font-family:宋体"}[ Notified to add SPBM Service Identifier sub-TLV. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, replicate mode= *rep-mode*.]{lang="EN-US"}

[[通知添加]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x865291456}[服务标识子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291455}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x355363528}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291458}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[re]{lang="EN-US"}[p-mode]{lang="EN-US"}*]{#struct_0_x1051_20145_x355691208}[：模式值]{lang="EN-US" style="font-family:宋体"}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x865291457}[：]{style="font-family:宋体"}[ Notified to modify SPBM Service Identifier sub-TLV. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number,* replicate mode= *rep-mode*.]{lang="EN-US"}

[[通知修改]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x355232456}[服务标识子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291452}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x355035848}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291451}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[re]{lang="EN-US"}[p-mode]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291454}[：模式值]{lang="EN-US" style="font-family:宋体"}

[[MAIN]{lang="EN-US"}]{#struct_0_x1051_20145_x355429064}[：]{style="font-family:宋体"}[ Notified to delete SPBM Service Identifier sub-TLV. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*.]{lang="EN-US"}

[[通知删除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x865291453}[服务标识子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_x354970312}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291464}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291463}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[MAIN: VSI *vsi-name* link state changed from up to down.]{lang="EN-US"}]{#struct_0_x1051_20145_x354970313}

[[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_1473360704}[链路状态从]{style="font-family:宋体"}[UP]{lang="EN-US"}[到]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{style="font-family:宋体"}

[[MAIN: VSI *vsi-name* link state changed from down to up.]{lang="EN-US"}]{#struct_0_x1051_20145_x1273875158}

[[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_1473360705}[链路状态从]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[到]{style="font-family:宋体"}[UP]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{style="font-family:宋体"}

[[MAIN: Started to modify VSI control block: VSI-name *vsi-name*, VSI-index= *vsi-index*, I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_1473360702}

[[修改]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_x1274006230}[控制块，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[vsi-name]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360703}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[vsi-index]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360708}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x1274661590}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[MAIN: Started to delete VSI control block: VSI-name *vsi-name*.]{lang="EN-US"}]{#struct_0_x1051_20145_1473360709}

[[删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_x1274727126}[控制块，其中]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名]{style="font-family:宋体"}

[[MAIN: Received VSI add event.]{lang="EN-US"}]{#struct_0_x1051_20145_1473360706}

[[接收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_1473360707}[添加事件]{style="font-family:宋体"}

[[MAIN: Received VSI delete event.]{lang="EN-US"}]{#struct_0_x1051_20145_x1273809622}

[[接收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_1473360696}[删除事件]{style="font-family:宋体"}

[[MAIN: Received VSI I-SID change event.]{lang="EN-US"}]{#struct_0_x1051_20145_1064908067}

[[接收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_1473360697}[和]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[变化事件]{style="font-family:宋体"}

[[MAIN: Received VSI state change event.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454720}

[[接收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1051_20145_2038866588}[状态变化事件]{style="font-family:宋体"}

[[MAIN: Received VSI AC state change event.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454719}

[[接收到]{style="font-family:宋体"}[VSI AC]{lang="EN-US"}]{#struct_0_x1051_20145_x98454722}[侧状态变化事件]{style="font-family:宋体"}

[[MAIN: Received L2VPN global disable event.]{lang="EN-US"}]{#struct_0_x1051_20145_2038866586}

[[接收到]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x1051_20145_x98454721}[全局去使能事件]{style="font-family:宋体"}

[[MAIN: L2VPN started to push VSI information.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454716}

[[L2VPN]{lang="EN-US"}]{#struct_0_x1051_20145_464888478}[开始上报]{style="font-family:宋体"}[VSI]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[MAIN: L2VPN stopped to push VSI information.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454715}

[[L2VPN]{lang="EN-US"}]{#struct_0_x1051_20145_x98454718}[上报]{style="font-family:宋体"}[VSI]{lang="EN-US"}[事件结束]{style="font-family:宋体"}

[[MAIN: Trying to connect with L2VPN.]{lang="EN-US"}]{#struct_0_x1051_20145_464888484}

[[尝试与]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x1051_20145_x98454717}[连接]{style="font-family:宋体"}

[[UPDT: Received LSP change event.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454728}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_2038866596}[模块收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文改变事件]{style="font-family:宋体"}

[[UPDT: Received state change event on interface *circuitName*: *eventType*.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454727}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769856}[模块收到端口状态改变事件，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1173889330}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventType]{lang="EN-US"}*]{#struct_0_x1051_20145_x2054769855}[：事件类型]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Received authentication change event.]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769858}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x723550636}[模块收到认证改变事件]{style="font-family:宋体"}

[[UPDT: Received level-1 fast flood event.]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769857}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769854}[模块收到]{style="font-family:宋体"}[fast flood]{lang="EN-US"}[快速扩散事件]{style="font-family:宋体"}

[[UPDT: Received control address change event. Socket recreated.]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769853}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769864}[模块收到控制地址改变事件]{style="font-family:宋体"}

[[UPDT: ECT migration All-no-T timer started. I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_1958344088}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_283882302}[迁移的]{style="font-family:宋体"}[All-no-T]{lang="EN-US"}[定时器启动信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_805796911}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1051_20145_283882303}[：]{lang="EN-US" style="font-family:宋体"}[T-flag]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[UPDT: ECT migration All-R timer started. I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_283882308}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_283882307}[迁移的]{style="font-family:宋体"}[All-R]{lang="EN-US"}[定时器启动信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_283882296}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1051_20145_283882297}[：]{lang="EN-US" style="font-family:宋体"}[R-flag]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[UPDT: ECT migration Finish timer started. I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1187254065}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432832}[迁移的全网同步定时器启动信息，其中]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[为]{style="font-family:宋体"}[I-SID]{lang="EN-US"}

[[UPDT: ECT migration All-no-T timer stopped. I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432831}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432828}[迁移的]{style="font-family:宋体"}[All-no-T]{lang="EN-US"}[定时器停止信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432827}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432830}[：]{lang="EN-US" style="font-family:宋体"}[T-flag]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[UPDT: ECT migration All-R timer stopped. I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432829}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x863128768}[迁移的]{style="font-family:宋体"}[All-R]{lang="EN-US"}[定时器停止信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x863128767}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1051_20145_x863128770}[：]{lang="EN-US" style="font-family:宋体"}[R-flag]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[UPDT: ECT migration Finish timer stopped. I-SID= *i-sid*.]{lang="EN-US"}]{#struct_0_x1051_20145_2132900836}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x863128769}[迁移的全网同步定时器停止信息，其中]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[表示]{style="font-family:宋体"}[I-SID]{lang="EN-US"}

[[UPDT: Received I-SID FSM state change event: sysIndex= *sysindex*, I-SID= *i-sid*, event= *event type*.]{lang="EN-US"}]{#struct_0_x1051_20145_x863128764}

[[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x863128763}[状态机变化信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_2132966371}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x863128766}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event type]{lang="EN-US"}*]{#struct_0_x1051_20145_x863128765}[：事件类型]{lang="EN-US" style="font-family:宋体"}

[[UPDT: I-SID FSM notified UPDT to add SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*.]{lang="EN-US"}]{#struct_0_x1051_20145_x863128776}

[[创建]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x863128775}[状态机时通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}[模块添加]{style="font-family:宋体"}[Service Identifier sub-TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523392}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1714006280}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523393}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[UPDT: I-SID FSM notified UPDT to add SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *transmit flag*, R-flag= *receive flag*.]{lang="EN-US"}]{#struct_0_x1051_20145_1475523390}

[[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_1475523391}[状态机变化通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}[模块添加]{style="font-family:宋体"}[Service Identifier sub-TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_1713809672}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523396}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523397}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[transmit flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523394}[：转发标记]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[receive flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523395}[：接收标记]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: I-SID FSM notified UPDT to delete SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*.]{lang="EN-US"}]{#struct_0_x1051_20145_1713547528}

[[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_1475523384}[状态机变化通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}[模块删除]{style="font-family:宋体"}[Service Identifier sub-TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523385}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641280}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641279}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[UPDT: I-SID FSM notified UPDT to modify SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *transmit flag*, R-flag= *receive flag*.]{lang="EN-US"}]{#struct_0_x1051_20145_x87641282}

[[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_849079223}[状态机变化通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}[模块修改]{style="font-family:宋体"}[Service Identifier sub-TLV]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysindex]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641281}[：系统索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641276}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641275}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[transmit flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641278}[：转发标记]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[receive flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641277}[：接收标记]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1569123258}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_280605056}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm event]{lang="EN-US"}]{#struct_0_x1051_20145_x441641105}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x212498901}[端口上去使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1051_20145_x87641288}

[\[Sysname\] interface gigabitethernet 0/1/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet0/1/3\] undo spbm enable]{lang="EN-US"}

[\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[MAIN: Disable SPBM PDU up to CPU on interface GigabitEthernet0/1/3, control mac= 0180-c200-002e, result= 0.]{lang="EN-US"}

[\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_EVT: -MDC=1;]{lang="EN-US"}

[MAIN: Disable VSI AC packet up to interface GigabitEthernet0/1/3, result= 0.]{lang="EN-US"}

[\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[MAIN: Notified interface state change: Enable \--\> Disable.]{lang="EN-US"}

[\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[MAIN: Notified interface state change: Up \--\> Down.]{lang="EN-US"}

[\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[ADJ: Received state change event on interface GigabitEthernet0/1/3: Disable.]{lang="EN-US"}

[\*Dec 26 12:57:09:815 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[ADJ: Received state change event on interface GigabitEthernet0/1/3: Up\--\>Down.]{lang="EN-US"}

[%Dec 26 12:57:09:815 2012 Sysname SPBM/5/SPB_NBR_CHG: -MDC=1; SPBM 1, Level-1 adjace]{lang="EN-US"}

[ncy 0011.2200.0101 (GigabitEthernet0/1/3), state changed to DOWN.]{lang="EN-US"}

[\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[UPDT: Received state change event on interface GigabitEthernet0/1/3: Disable.]{lang="EN-US"}

[\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[UPDT: Received state change event on interface GigabitEthernet0/1/3: Up\--\>Down.]{lang="EN-US"}

[\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[MAIN: Notified neighbor down event to UPDT.]{lang="EN-US"}

[\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[UPDT: Received LSP change event.]{lang="EN-US"}

::: {#1699184023 .myid}
[]{#_Toc404798001}[]{#struct_0_x1051_20145_849079229}

**SPBM \-- SPBM调试命令 \-- debugging spbm flush**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1463847156}

[**[debugging spbm flush]{lang="EN-US"}**[ { **all** \| **event** \| **message** { **multicast-fib** \| **multicast-pw** \| **unicast-fib** \| **unicast-pw** } }]{lang="EN-US"}]{#struct_0_x1051_20145_x1033665788}

[**[undo debugging spbm flush]{lang="EN-US"}**[ { **all** \| **event** \| **message** { **multicast-fib** \| **multicast-pw** \| **unicast-fib** \| **unicast-pw** } }]{lang="EN-US"}]{#struct_0_x1051_20145_x87641287}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_849079226}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_1463847159}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1034386684}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_537988101}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1004884481}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_574581204}

[**[all]{lang="EN-US"}**]{#struct_0_x1051_20145_x1596635089}[：表示]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1051_20145_x1083505688}[：表示]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[的接收事件调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_x1051_20145_x2043956416}[：表示发送]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[添加、组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[删除、组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[出端口添加、组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[出端口删除、组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[添加、组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[删除、单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[刷新、单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[删除、单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[添加、单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[删除消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1095510509}

[**[debugging spbm flush]{lang="EN-US"}**]{#struct_0_x1051_20145_207546023}[命令用来打开]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm flush]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_1597319437}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging spbm flush event]{lang="EN-US"}]{#struct_0_x1051_20145_548487001}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2138694493}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x2032769787}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x971211357}

[[FLUSH: Received topology message, state([*state-value*]{.TableTextChar}), new digest([*digest-value*]{.TableTextChar}), edge count([*edge-value*)]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956415}

[[接收到拓扑变化消息，状态为]{style="font-family:宋体"}[*[state-value]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x1498795036}[，新摘要为]{style="font-family:宋体"}[*[digest-value]{lang="EN-US"}*]{.TableTextChar}[，拓扑边数为]{style="font-family:宋体"}[*[edge-value]{lang="EN-US"}*]{.TableTextChar}[，]{style="font-family:宋体"}[*[state-value]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Start]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956418}[：拓扑变化开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[End]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956412}[：拓扑变化结束]{style="font-family:宋体"}

[[FLUSH: Received digest packet message, system ID (*system-id*), Port(*PortName*).]{lang="EN-US"}]{#struct_0_x1051_20145_873857959}

[[接收到摘要报文消息，包括系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1051_20145_422665876}[为]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[和端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*

[[FLUSH: Received SPSource-ID change message, system ID(*system-id*), SPSource-ID(*spsource-id*).]{lang="EN-US"}]{#struct_0_x1051_20145_x629881735}

[[接收到]{style="font-family:宋体"}[SPSource-ID]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956411}[变化消息，包括系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[和最短路径源标识]{style="font-family:宋体"}*[spsource-id]{lang="EN-US"}*

[[FLUSH: Received SPSource-ID delete message, system ID(*system-id*), SPSource-ID(*spsource-id*).]{lang="EN-US"}]{#struct_0_x1051_20145_470573432}

[[接收到]{style="font-family:宋体"}[SPSource-ID]{lang="EN-US"}]{#struct_0_x1051_20145_495772085}[删除消息，包括系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[和最短路径源标识]{style="font-family:宋体"}*[spsource-id]{lang="EN-US"}*

[[FLUSH: Received ECT B-VLAN mapping message, Operation([*operation*]{.TableTextChar}), B-VLAN(*bvlan-number*), ECT([*ect-index*]{.TableTextChar}).]{lang="EN-US"}]{#struct_0_x1051_20145_x691269514}

[[接收到]{style="font-family:宋体"}[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_1788283920}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[映射关系变化消息，包括]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[ECT]{lang="EN-US"}[为]{style="font-family:宋体"}[*[ect-index]{lang="EN-US"}*]{.TableTextChar}[，操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Refresh]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956413}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956423}[：删除]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received BMAC message, system ID(*system-id*), Operation([*operation*]{.TableTextChar}), BMAC(*macaddr-value*), B-VLAN(*bvlan-number*).]{lang="EN-US"}]{#struct_0_x1051_20145_x692422590}

[[接收到]{style="font-family:宋体"}[BMAC]{lang="EN-US"}]{#struct_0_x1051_20145_x727171849}[变化消息，包括系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[[、]{style="font-family:宋体"}]{.TableTextChar}[B[MAC]{.TableTextChar}]{lang="EN-US"}[[为]{style="font-family:宋体"}]{.TableTextChar}*[macaddr-value]{lang="EN-US"}*[[、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{.TableTextChar}[[为]{style="font-family:宋体"}]{.TableTextChar}*[bvlan-number]{lang="EN-US"}*[[、操作类型]{style="font-family:宋体"}*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Refresh]{lang="EN-US"}]{#struct_0_x1051_20145_294695745}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_294695742}[：删除]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received port role message, system ID (*system-id*), ECT ([*ect-index*]{.TableTextChar}), PortRole([*role-name*]{.TableTextChar}), Port(*PortName*).]{lang="EN-US"}]{#struct_0_x1051_20145_294695743}

[[接收到端口角色变化消息，包括系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1051_20145_x23597310}[为]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[、]{style="font-family:宋体"}[ECT]{lang="EN-US"}[为]{style="font-family:宋体"}[*[ect-index]{lang="EN-US"}*]{.TableTextChar}[、端口角色为]{style="font-family:宋体"}[*[role-name]{lang="EN-US"}*]{.TableTextChar}[和端口名]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，端口角色名]{style="font-family:宋体"}[*[role-name]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_x1051_20145_294695749}[：根端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DESIGNATED]{lang="EN-US"}]{#struct_0_x1051_20145_294695746}[：指定端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALTERNATE]{lang="EN-US"}]{#struct_0_x1051_20145_294695736}[：不在树上端口]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received reset message, type([*operation*]{.TableTextChar}).]{lang="EN-US"}]{#struct_0_x1051_20145_1932717823}

[[接收到]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_x1051_20145_x94325013}[过程中主线程和其他线程的交互消息，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Stopwork]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619392}[：停止工作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619394}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619388}[：使能]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received I-SID B-VLAN mapping message, I-SID([*i-sid*]{.TableTextChar}), TRB-VLAN(*bvlan-number*), RB-VLAN(*bvlan-number*).]{lang="EN-US"}]{#struct_0_x1051_20145_x102184785}

[[接收到拓扑中]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x517487805}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[映射关系变化消息，包括]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}[*[i-sid]{lang="EN-US"}*]{.TableTextChar}[、]{style="font-family:宋体"}[TRB-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[和]{style="font-family:宋体"}[RB-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*

[[FLUSH: Received I-SID B-VLAN item message, system ID(*system-id*), Operation([*operation*]{.TableTextChar}), I-SID([*i-sid*]{.TableTextChar}), B-VLAN(*bvlan-number*).]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619387}

[[接收到节点]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_657330102}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[映射关系变化消息，包括]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[、]{style="font-family:宋体"}[system ID]{lang="EN-US"}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Refresh]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619389}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619400}[：删除]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received AP mode message, AP mode([*value*]{.TableTextChar}).]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619399}

[[接收到]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1051_20145_1463964692}[模式变化消息，]{style="font-family:宋体"}[*[value]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Mcast]{lang="EN-US"}]{#struct_0_x1051_20145_x852315327}[：仅支持组播]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Both]{lang="EN-US"}]{#struct_0_x1051_20145_x852315329}[：两种都支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1051_20145_x852315323}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[关闭]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received configuration message.  ]{lang="EN-US"}]{#struct_0_x1051_20145_x1369855197}

[[接收到命令行消息]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1711753949}

[[FLUSH: Received thread message, type([*operation*]{.TableTextChar}).]{lang="EN-US"}]{#struct_0_x1051_20145_1113520132}

[[接收到线程操作消息，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x852315326}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Stop_Work]{lang="EN-US"}]{#struct_0_x1051_20145_x852315336}[：停止工作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Start_Work]{lang="EN-US"}]{#struct_0_x1051_20145_x852315335}[：开始工作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Quit]{lang="EN-US"}]{#struct_0_x1051_20145_1486336833}[：退出]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received FDB smooth start message(support GR).]{lang="EN-US"}]{#struct_0_x1051_20145_1486336830}

[[接收]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_1486336825}[表项平滑开始消息（支持]{style="font-family:宋体"}[GR]{lang="EN-US"}[）]{style="font-family:宋体"}

[[FLUSH: Received FDB smooth start message(not support GR).]{lang="EN-US"}]{#struct_0_x1051_20145_x2141429555}

[[接收]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x85478590}[表项平滑开始消息（不支持]{style="font-family:宋体"}[GR]{lang="EN-US"}[）]{style="font-family:宋体"}

[[FLUSH:Received FDB smooth end message.]{lang="EN-US"}]{#struct_0_x1051_20145_1295100837}

[[接收]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x85478589}[表项平滑结束消息]{style="font-family:宋体"}

[[FLUSH: Received PW smooth start message(support GR).]{lang="EN-US"}]{#struct_0_x1051_20145_x1043551314}

[[接收]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_x2041793724}[表项平滑开始消息（支持]{style="font-family:宋体"}[GR]{lang="EN-US"}[）]{style="font-family:宋体"}

[[FLUSH: Received PW smooth start message(not support GR).]{lang="EN-US"}]{#struct_0_x1051_20145_x438879694}

[[接收]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_296858433}[表项平滑开始消息（不支持]{style="font-family:宋体"}[GR]{lang="EN-US"}[）]{style="font-family:宋体"}

[[FLUSH:Received PW smooth end message.]{lang="EN-US"}]{#struct_0_x1051_20145_296858430}

[[接收]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_302062042}[表项平滑结束消息]{style="font-family:宋体"}

[[FLUSH: Received PW reflush message.]{lang="EN-US"}]{#struct_0_x1051_20145_x1599919198}

[[接收到]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_296858431}[表项重刷消息]{style="font-family:宋体"}

[[FLUSH:Received set egress-flag message, system ID(*system-id*), Operation([*operation*]{.TableTextChar}), I-SID(*i-sid*).]{lang="EN-US"}]{#struct_0_x1051_20145_302062041}

[[接收到设置]{style="font-family:宋体"}[egress-flag]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456706}[消息，包括系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[、操作类型为]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[，]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Refresh]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456700}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456702}[：删除]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: Received replicate mode change message, I-SID(*i-sid*), replicate mode (*rep-mode*).]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456701}

[[接收到模式改变消息，包括]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x850152638}[为]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[、工作模式为]{style="font-family:宋体"}*[rep-mode]{lang="EN-US"}*[，]{style="font-family:宋体"}*[rep-mode]{lang="EN-US"}*[的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[tandem]{lang="EN-US"}]{#struct_0_x1051_20145_x850152648}[：核心复制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[head-end]{lang="EN-US"}]{#struct_0_x1051_20145_1488499520}[：头端复制]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging spbm flush message unicast-fib]{lang="EN-US"}]{#struct_0_x1051_20145_x1537915213}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1882812399}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x404727777}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_1488499521}

[[FLUSH: Sent the message for [*operation* ]{.TableTextChar}unicast MAC entry[*,* ]{.TableTextChar} length= *length-value.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1537849677}

[[具体某一个单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x411214392}[表项消息的头部，包括消息长度为]{style="font-family:宋体"}*[length-value]{lang="EN-US"}*[（不包括本消息头）和消息操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[refreshing]{lang="EN-US"}]{#struct_0_x1051_20145_1488499519}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_1488499525}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*).]{lang="EN-US"}]{#struct_0_x1051_20145_x1537587533}

[[具体某一个单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_1488499522}[表项消息的内容，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[Port]{lang="EN-US"}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*

[[Sent the message for starting to smooth FDB entry.]{lang="EN-US"}]{#struct_0_x1051_20145_x1537784141}

[[发送]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x371379375}[平滑开始消息]{style="font-family:宋体"}

[[Sent the message for ending to smooth FDB entry.]{lang="EN-US"}]{#struct_0_x1051_20145_x405280590}

[[发送]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x1108938569}[平滑结束消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging spbm flush message multicast-fib]{lang="EN-US"}]{#struct_0_x1051_20145_1648617145}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1910317938}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_1488499523}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1537718605}

[[FLUSH: Sent the message for [*operation*]{.TableTextChar} multicast MAC entry, length= *length-value.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2051063471}

[[具体某一个组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_1029019448}[表项消息的头部，包括消息长度（不包括本消息头）和消息类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[refreshing]{lang="EN-US"}]{#struct_0_x1051_20145_1488499513}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_x91966655}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan -number*) OutIFNum(*number*) RouteFlag(*flag-value*).]{lang="EN-US"}]{#struct_0_x1051_20145_x91966658}

[[具体某一个组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_1287896093}[表项消息的内容，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，出端口数目为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*

[[FLUSH: Port List:]{lang="EN-US"}]{#struct_0_x1051_20145_301817767}

[[         Port(*PortName*)]{lang="EN-US"}]{#struct_0_x1051_20145_x567119578}

[[出端口列表，]{style="font-family:宋体"}[Port]{lang="EN-US"}]{#struct_0_x1051_20145_x1036849024}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*

[[FLUSH: Sent the message for [*operation*]{.TableTextChar} multicast MAC iflist, length= *length-value.*]{lang="EN-US"}]{#struct_0_x1051_20145_x91966657}

[[具体某一个组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_1287896086}[出端口消息的头部，包括消息长度为]{style="font-family:宋体"}*[length-value]{lang="EN-US"}*[（不包括本消息头）和消息类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[adding]{lang="EN-US"}]{#struct_0_x1051_20145_x91966651}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_x91966653}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*).]{lang="EN-US"}]{#struct_0_x1051_20145_1287896082}

[[具体某一个组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x91966664}[出端口消息的内容，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，出端口为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*

[[Sent the message for starting to smooth FDB entry.]{lang="EN-US"}]{#struct_0_x1051_20145_x286082023}

[[发送]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_1489328850}[平滑开始消息]{style="font-family:宋体"}

[[Sent the message for ending to smooth FDB entry.]{lang="EN-US"}]{#struct_0_x1051_20145_782553786}

[[发送]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_1024959778}[平滑结束消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging spbm flush message unicast-pw]{lang="EN-US"}]{#struct_0_x1051_20145_x91966663}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1905823335}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x286082030}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_1489263313}

[[FLUSH: Sent the message for [*operation*]{.TableTextChar} unicast MINM entry, I-SID(*i-sid*), B-VLAN(*bvlan-number*), Port(*PortName*) , VSI-name(*vsi-name*), Flag(*flag-value*),D-BMAC(*macaddr-value*), S-BMAC(*macaddr-value*), S-CMAC(*macaddr-value*).]{lang="EN-US"}]{#struct_0_x1051_20145_x772078824}

[[发送单播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281791}[表项消息，包括]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[、端口]{style="font-family:宋体"}[Port]{lang="EN-US"}[、]{style="font-family:宋体"}[VSI-name]{lang="EN-US"}[、]{style="font-family:宋体"}[Flag]{lang="EN-US"}[、]{style="font-family:宋体"}[MINM]{lang="EN-US"}[连接]{style="font-family:宋体"}[key]{lang="EN-US"}[信息中的]{style="font-family:宋体"}[DBMAC]{lang="EN-US"}[、]{style="font-family:宋体"}[MINM]{lang="EN-US"}[表项信息中骨干网源]{style="font-family:宋体"}[BMAC]{lang="EN-US"}[、用户源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MINM_SPB \| MINM_UNICAST \| MINM_COREREPLICATE]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281788}[：]{lang="EN-US" style="font-family:宋体"}[SPB]{lang="EN-US"}[单播核心复制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MINM_SPB \| MINM_UNICAST \| MINM_HEADREPLICATE]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281790}[：]{lang="EN-US" style="font-family:宋体"}[SPB]{lang="EN-US"}[单播头端复制]{lang="EN-US" style="font-family:宋体"}

[[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x1079779604}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[adding]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281799}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_290370369}[：删除]{lang="EN-US" style="font-family:宋体"}

[[FLUSH: For receiving packet only, B-VLAN (*bvlan-number*), Port(*PortName*).]{lang="EN-US"}]{#struct_0_x1051_20145_x1551392090}

[[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_1737819119}[迁移过程中只收报文的单播端口信息，包括]{style="font-family:宋体"}[B-VLAN *bvlan-number*]{lang="EN-US"}[和端口名]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*

[[Sent the message for starting to smooth PW entry.]{lang="EN-US"}]{#struct_0_x1051_20145_1003308112}

[[发送平滑]{style="font-family:宋体"}[pw]{lang="EN-US"}]{#struct_0_x1051_20145_290370366}[开始消息]{style="font-family:宋体"}

[[Sent the message for ended to smooth PW entry.]{lang="EN-US"}]{#struct_0_x1051_20145_x1551392075}

[[发送平滑]{style="font-family:宋体"}[pw]{lang="EN-US"}]{#struct_0_x1051_20145_x1796977930}[结束消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging spbm flush message multicast-pw]{lang="EN-US"}]{#struct_0_x1051_20145_2016579296}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1906858459}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x443864837}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_290370367}

[[FLUSH: Sent the message for [*operation*]{.TableTextChar} multicast MINM entry, I-SID (*i-sid*), B-VLAN(*bvlan-number*), Port number(*number*), VSI-name(*vsi-name*), Flag(*flag-value*), D-BMAC(*macaddr-value*), S-BMAC(*macaddr-value*), S-CMAC(*macaddr-value*).]{lang="EN-US"}]{#struct_0_x1051_20145_x1551392076}

[[发送组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_x1393693403}[表项消息，包括]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[、端口个数]{style="font-family:宋体"}[Port number]{lang="EN-US"}[、]{style="font-family:宋体"}[VSI-name]{lang="EN-US"}[、]{style="font-family:宋体"}[Flag]{lang="EN-US"}[、]{style="font-family:宋体"}[MINM]{lang="EN-US"}[连接]{style="font-family:宋体"}[key]{lang="EN-US"}[信息中的]{style="font-family:宋体"}[D-BMAC]{lang="EN-US"}[、]{style="font-family:宋体"}[MINM]{lang="EN-US"}[表项信息中骨干网源]{style="font-family:宋体"}[BMAC]{lang="EN-US"}[、用户源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MINM_SPB \| MINM_MULTICAST \| MINM_COREREPLICATE]{lang="EN-US"}]{#struct_0_x1051_20145_290370373}[：]{lang="EN-US" style="font-family:宋体"}[SPB]{lang="EN-US"}[组播核心复制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MINM_SPB \| MINM_MULTICAST \| MINM\_ HEADREPLICATE]{lang="EN-US"}]{#struct_0_x1051_20145_290370360}[：]{lang="EN-US" style="font-family:宋体"}[SPB]{lang="EN-US"}[组播头端复制]{lang="EN-US" style="font-family:宋体"}

[[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x1551392081}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[adding]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944768}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944769}[：删除]{lang="EN-US" style="font-family:宋体"}

[[ FLUSH: Port List:]{lang="EN-US"}]{#struct_0_x1051_20145_x1445580109}

[[          Port(*PortName*)]{lang="EN-US"}]{#struct_0_x1051_20145_x583145962}

[[出端口列表，]{style="font-family:宋体"}[Port]{lang="EN-US"}]{#struct_0_x1051_20145_x534672533}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*

[[FLUSH: Sent the message for [*operation*]{.TableTextChar} multicast MINM port, I-SID (*i-sid*), B-VLAN(*bvlan-number*), Port (*PortName*) VSI-name(*name*), Flag(*flag-value*),]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944764}

[[D-BMAC(*macaddr-value*), S-BMAC(*macaddr-value*), S-CMAC(*macaddr-value*).]{lang="EN-US"}]{#struct_0_x1051_20145_2089872300}

[[发送组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944766}[出端口消息，包括]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[、端口名]{style="font-family:宋体"}[Port]{lang="EN-US"}[、]{style="font-family:宋体"}[VSI-name]{lang="EN-US"}[、]{style="font-family:宋体"}[Flag]{lang="EN-US"}[、]{style="font-family:宋体"}[MINM]{lang="EN-US"}[连接]{style="font-family:宋体"}[key]{lang="EN-US"}[信息中的]{style="font-family:宋体"}[DBMAC]{lang="EN-US"}[、]{style="font-family:宋体"}[MINM]{lang="EN-US"}[表项信息中骨干网源]{style="font-family:宋体"}[BMAC]{lang="EN-US"}[、用户源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MINM_SPB \| MINM_MULTICAST \| MINM_COREREPLICATE]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944775}[：]{lang="EN-US" style="font-family:宋体"}[SPB]{lang="EN-US"}[组播核心复制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MINM_SPB \| MINM_MULTICAST \| MINM\_ HEADREPLICATE]{lang="EN-US"}]{#struct_0_x1051_20145_x856640703}[：]{lang="EN-US" style="font-family:宋体"}[SPB]{lang="EN-US"}[组播头端复制]{lang="EN-US" style="font-family:宋体"}

[[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_676590283}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[adding]{lang="EN-US"}]{#struct_0_x1051_20145_x856640700}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_x856640702}[：删除]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_676655819}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_741380258}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开单播]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[事件调试信息开关，当]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[接收到事件通知时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm flush event]{lang="EN-US"}]{#struct_0_x1051_20145_x856640712}

[\<Sysname\> \*Sep 17 10:08:54:792 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received SPSource-ID change message, system ID(0011.2200.0001), SPSource-ID(90967).]{lang="EN-US"}

[\*Sep 17 10:08:54:793 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received ECT B-VLAN mapping message, Operation(Refresh), B-VLAN(1), ECT (1).]{lang="EN-US"}

[\*Sep 17 10:08:54:793 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received ECT B-VLAN mapping message, Operation(Refresh), B-VLAN(2), ECT (1).]{lang="EN-US"}

[\*Sep 17 10:08:54:794 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received BMAC message, system ID(0011.2200.0001), Operation(Refresh), BMAC(0011-2200-0001) , B-VLAN(1).]{lang="EN-US"}

[\*Sep 17 10:08:54:794 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received BMAC message, system ID(0011.2200.0001), Operation(Refresh), BMAC(0011-2200-0001), B-VLAN(2).]{lang="EN-US"}

[\*Sep 17 10:11:00:412 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received digest packet message, system ID(0011.2200.0a01), Port(GigabitEthernet0/1/3).]{lang="EN-US"}

[\*Sep 17 10:11:03:296 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received topology message, state(Start), new digest(000000365981264d9ff), edge count(2).]{lang="EN-US"}

[\*Sep 17 10:11:03:297 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received port role message, system ID(0011.2200.0a01), ECT (1), PortRole(ROOT), Port(GigabitEthernet0/1/3).]{lang="EN-US"}

[\*Sep 17 10:11:03:299 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received topology message, state(End), new digest(000000365981264d9ff), edge count(2).]{lang="EN-US"}

[\*Sep 17 10:16:54:461 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received I-SID B-VLAN item message, system ID(0011.2200.0a01), Operation(Refresh), I-SID (256), B-VLAN(1).]{lang="EN-US"}

[\*Sep 17 10:18:05:372 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received I-SID B-VLAN mapping message, I-SID(256), TRB-VLAN(1), RB-VLAN(65535).]{lang="EN-US"}

[\*Sep 17 10:18:08:625 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received I-SID message, system ID(0011.2200.0001), I-SID(256), ECT(1), Port(GigabitEthernet0/1/3).]{lang="EN-US"}

[\*Sep 17 10:15:58:873 2012 Sysname SPBM/7/SPBM_EVT: -MDC=1;]{lang="EN-US"}

[FLUSH: Received configuration message.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_676655818}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开单播]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[SPBM FLUSH]{lang="EN-US"}[消息调试信息开关，当用户态进程向内核发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[消息时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm flush message unicast-fib]{lang="EN-US"}]{#struct_0_x1051_20145_741380257}

[\*Sep 17 10:11:03:329 2012 Sysname SPBM/7/SPBM_1_MSG: -MDC=1;]{lang="EN-US"}

[FLUSH: Sent the message for refreshing unicast MAC entry, length= 32.]{lang="EN-US"}

[Unicast MAC: MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T).]{lang="EN-US"}

[\<Sysname\> debugging spbm flush message multicast-fib]{lang="EN-US"}

[\*Sep 17 10:18:08:626 2012 Sysname SPBM/7/SPBM_1_MSG: -MDC=1;]{lang="EN-US"}

[FLUSH: Sent the message for adding multicast MAC iflist, length= 40.]{lang="EN-US"}

[Multicast MAC: MAC(1363-5700-0100) B-VLAN(1) Port(GE0/1/3) RouteFlag(TE).]{lang="EN-US"}

[\<Sysname\> debugging spbm flush message unicast-pw]{lang="EN-US"}

[\*Sep 17 10:18:05:372 2012 Sysname SPBM/7/SPBM_1_MSG: -MDC=1;]{lang="EN-US"}

[FLUSH: Sent the message for adding unicast MINM entry, I-SID(256), B-VLAN(1), Port(GE0/1/3)]{lang="EN-US"}

[ VSI-name(1), Flag(MINM_SPB \| MINM_UNICAST \| MINM_COREREPLICATE), D-BMAC(0011-2200-0a01), S-BMAC(0011-2200-0001), S-CMAC(0011-2200-0001).]{lang="EN-US"}

::: {#-2089217763 .myid}
[]{#_Toc404798002}[]{#struct_0_x1051_20145_x1215102094}

**SPBM \-- SPBM调试命令 \-- debugging spbm graceful-restart**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_689298110}

[**[debuging spbm graceful-restart]{lang="EN-US"}**]{#struct_0_x1051_20145_x856640711}

[**[undo debuging spbm graceful-restart]{lang="EN-US"}**]{#struct_0_x1051_20145_676721354}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_339973081}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1924575153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_410233151}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x480541854}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1363232405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1352376292}

[[无]{style="font-family:宋体"}]{#struct_0_x1051_20145_1296132491}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1482011456}

[**[debugging spbm graceful-re]{lang="EN-US"}[start]{lang="EN-US"}**]{#struct_0_x1051_20145_x341316592}[命令用来打开]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging spbm graceful-restart]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}]{#struct_0_x1051_20145_1313101140}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-13 ]{lang="EN-US"}[debugging spbm graceful-restart]{lang="EN-US"}]{#struct_0_x1051_20145_685215855}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1903153341}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1411011578}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_754402652}

[[ADJ: All T1 timers have stopped.]{lang="EN-US"}]{#struct_0_x1051_20145_x1453691221}

[[所有的]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x1051_20145_1482011455}[定时器已停止]{style="font-family:宋体"}

[[ADJ: All Level-1 T1 timers have stopped.]{lang="EN-US"}]{#struct_0_x1051_20145_x341382128}

[[所有]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1051_20145_1482011448}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器已停止]{style="font-family:宋体"}

[[ADJ: Adjacency(*system-id*) on *circuitName* (Level-1) changed to normal mode.]{lang="EN-US"}]{#struct_0_x1051_20145_x342234095}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x89803968}[状态发生变化，由]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态变为非]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x89803963}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x2046119104}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ADJ: Adjacency(*system-id*) on *circuitName* (Level-1) changed to restart mode.]{lang="EN-US"}]{#struct_0_x1051_20145_1497955107}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119106}[状态发生变化，由非]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2046119101}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_292533054}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ADJ: Neighbor(*system-id*) SA bit set, adjacency not advertised.]{lang="EN-US"}]{#struct_0_x1051_20145_x791206216}

[[邻居报文]{style="font-family:宋体"}[GRTLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782078}[中的]{style="font-family:宋体"}[SA]{lang="EN-US"}[比特位被设置上，其中]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[表示邻居的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[ADJ: Neighbor(*system-id*) SA bit cleared, adjacency advertised.]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782077}

[[邻居报文]{style="font-family:宋体"}[GRTLV]{lang="EN-US"}]{#struct_0_x1051_20145_x854478024}[中的]{style="font-family:宋体"}[SA]{lang="EN-US"}[比特位被清除，其中]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[表示邻居]{style="font-family:宋体"}[的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[ADJ: Received P2P Hello with RR bit set from neighbor *system-id* on *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x854478023}

[[从邻居接收到]{style="font-family:宋体"}[RR]{lang="EN-US"}]{#struct_0_x1051_20145_1484174145}[比特位被置位的]{style="font-family:宋体"}[P2P Hello]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1484174146}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990527}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ADJ: Received P2P Hello with RA bit set from neighbor *system-id* on *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x78990530}

[[从邻居接收到]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_x1051_20145_x78990524}[比特位被置位的]{style="font-family:宋体"}[P2P Hello]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990535}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305659}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ADJ: Circuit(*circuitName*) Level-1 T1 timer expired count: ]{lang="EN-US"}]{#struct_0_x1051_20145_1558040243}*[T1TimerExpCnt]{lang="EN-US"}*[.]{lang="EN-US"}

[[端口的]{style="font-family:宋体"}[Level-1 T1]{lang="EN-US"}]{#struct_0_x1051_20145_x2035305672}[定时器超时次数，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_303346495}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[T1TimerExpCnt]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968641}[：]{lang="EN-US" style="font-family:
  宋体"}[T1]{lang="EN-US"}[定时器超时的次数，超时]{lang="EN-US" style="font-family:
  宋体"}[10]{lang="EN-US"}[次之后取消]{lang="EN-US" style="font-family:宋体"}[T1]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[ADJ: Circuit(*circuitName*) Level-1 timer expired count has arrived max.]{lang="EN-US"}]{#struct_0_x1051_20145_x621961915}

[[T1]{lang="EN-US"}]{#struct_0_x1051_20145_x843664574}[定时器超时次数达到最大次数]{style="font-family:宋体"}[10]{lang="EN-US"}[次，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名称]{style="font-family:宋体"}

[[MAIN: Graceful restart completed.]{lang="EN-US"}]{#struct_0_x1051_20145_821378853}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x843664583}[完成]{style="font-family:宋体"}

[[MAIN: Entered phase(*GrPhase*).]{lang="EN-US"}]{#struct_0_x1051_20145_821706540}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x76827842}[进入下一阶段，其中]{style="font-family:宋体"}[GrPhase]{lang="EN-US"}[表示]{style="font-family:宋体"}[GR]{lang="EN-US"}[阶段，包括]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步阶段、第一次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算阶段、引入计算阶段、第二次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算阶段、]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成阶段、]{style="font-family:宋体"}[GR]{lang="EN-US"}[完成阶段]{style="font-family:宋体"}

[[MAIN: Received Level-1 T2 timer cancel event(*T2StopEvent*).]{lang="EN-US"}]{#struct_0_x1051_20145_x76827841}

[[收到触发]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_x1051_20145_x841501883}[停止的事件，事件类型包括"所有]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止"和"]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成"。两个事件都发生时才真正停止]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器，其中]{style="font-family:宋体"}*[T2StopEvent]{lang="EN-US"}*[表示触发停止]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器的事件，包括"所有]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止"和"]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成"]{style="font-family:宋体"}

[[MAIN: Level-1 T2 timer stopped.]{lang="EN-US"}]{#struct_0_x1051_20145_1368688082}

[[停止]{style="font-family:宋体"}[Level-1 T2]{lang="EN-US"}]{#struct_0_x1051_20145_1497150274}[定时器]{style="font-family:宋体"}

[[MAIN: Level-1 T2 timer expired.]{lang="EN-US"}]{#struct_0_x1051_20145_x56338287}

[[Level-1 T2]{lang="EN-US"}]{#struct_0_x1051_20145_x96292197}[定时器超时]{style="font-family:宋体"}

[[MAIN: Graceful restart entered *GrTypeStr* phase(*LSDB synchronization*).]{lang="EN-US"}]{#struct_0_x1051_20145_x96292198}

[[开始]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_286044825}[，]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式]{style="font-family:宋体"}*[GrTypeStr]{lang="EN-US"}*[分为]{style="font-family:宋体"}[restarting]{lang="EN-US"}[方式和]{style="font-family:宋体"}[starting]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[MAIN: Received module(*module*) phase(*GrPhase*), current phase(*GrPhase*).]{lang="EN-US"}]{#struct_0_x1051_20145_286044824}

[[模块]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270308}[阶段结束信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[module]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966243}[：模块名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[GrPhase]{lang="EN-US"}*]{#struct_0_x1051_20145_1477685917}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[MAIN: Entered GR smooth process: sysIndex= *sysindex.*]{lang="EN-US"}]{#struct_0_x1051_20145_1477685916}

[[进程进入]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x94129499}[平滑处理，其中]{style="font-family:宋体"}*[sysindex]{lang="EN-US"}*[表示系统索引]{style="font-family:宋体"}

[[MAIN: Exited GR smooth process: sysIndex= *sysindex.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1920778697}

[[进程离开]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_288207511}[平滑处理，其中]{style="font-family:宋体"}*[sysindex]{lang="EN-US"}*[表示系统索引]{style="font-family:宋体"}

[[MAIN: Notified FLUSH to leave GR smooth process.]{lang="EN-US"}]{#struct_0_x1051_20145_1567535609}

[[所有进程]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107611}[平滑都结束后，]{style="font-family:宋体"}[MAIN]{lang="EN-US"}[通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[平滑结束消息，开始下发表项]{style="font-family:宋体"}

[[UPDT: Started to purge local Level-1 LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_x1601784723}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x858803562}[完成，开始将本地原来生成、现在失效的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[清除]{style="font-family:宋体"}

[[UPDT: Purged Level-1 LSP *Lsp-id.*]{lang="EN-US"}]{#struct_0_x1051_20145_x227109574}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_281719453}[完成，将本地原来生成、现在失效的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[清除，其中]{style="font-family:宋体"}*[Lsp-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}

[[UPDT: Ended to purge local Level-1 LSP.]{lang="EN-US"}]{#struct_0_x1051_20145_2086193836}

[[清除失效]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_281719446}[结束]{style="font-family:宋体"}

[[UPDT: Synchronized CSNP from *Source-id* on circuit *circuitName*. LSP-ID ranges from *StartLspid* to *EndLspid.*]{lang="EN-US"}]{#struct_0_x1051_20145_129878697}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x865291625}[过程中收到]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端发送的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360549}[：]{lang="EN-US" style="font-family:宋体"}[Helper]{lang="EN-US"}[的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x98454888}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[StartLspId]{lang="EN-US"}*]{#struct_0_x1051_20145_x2054770026}[：]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文中开始的]{lang="EN-US" style="font-family:宋体"}[LSP-ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[EndLspId]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432995}[：]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文中结束的]{lang="EN-US" style="font-family:宋体"}[LSP-ID]{lang="EN-US"}

[[UPDT: Level-1 LSDB synchronization was complete.]{lang="EN-US"}]{#struct_0_x1051_20145_x1358023089}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x863128931}[过程中]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[UPDT: Level-1 CSNP set synchronization was complete on circuit *circuitName.*]{lang="EN-US"}]{#struct_0_x1051_20145_221150184}

[[GR]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956584}[过程中]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[接收完全，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_67747658}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x1907719633}[打开]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm graceful-restart]{lang="EN-US"}]{#struct_0_x1051_20145_x983602217}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956585}[执行]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[操作，输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> reset spbm all graceful-restart]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956586}

[Reset SPBM process? \[Y/N\]:y]{lang="EN-US"}

[\<Sysname\> \*Sep 10 00:24:19:183 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Graceful-restart enter restarting phase(Initialization).]{lang="EN-US"}

[\*Sep 10 00:24:19:201 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[ADJ: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 1.]{lang="EN-US"}

[%Sep 10 00:24:19:208 2012 Sysname SPBM/5/SPB_NBR_CHG: -MDC=1; SPBM 1, Level-1 adjacency 0011.2200.1401 (GigabitEthernet1/0/2), state change to: UP.]{lang="EN-US"}

[\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[ADJ: All T1 timers have stopped.]{lang="EN-US"}

[\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[ADJ: Received p2p hello with RA bit set from nbr 0011.2200.1401, on GigabitEthernet1/0/2.]{lang="EN-US"}

[\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[UPDT: Synchronized CSNP from 0011.2200.1401 on circuit GigabitEthernet1/0/2 range from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff]{lang="EN-US"}

[\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[UPDT: Level-1 CSNP set synchronization is complete on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[\*Sep 10 00:24:19:210 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[ADJ: All T1 timers have stopped.]{lang="EN-US"}

[\*Sep 10 00:24:19:211 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Received Level-1 T2 timer cancel event(All T1 stopped).]{lang="EN-US"}

[\*Sep 10 00:24:19:211 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Received Level-1 T2 timer cancel event(All T1 stopped).]{lang="EN-US"}

[\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[UPDT: LSDB synchronization is complete]{lang="EN-US"}

[\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Received Level-1 T2 timer cancel event(LSDB sync).]{lang="EN-US"}

[\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Level-1 T2 timer stopped]{lang="EN-US"}

[\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Entered phase(LSP stability)]{lang="EN-US"}

[\*Sep 10 00:24:19:269 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Received module(updt) phase(LSP stability), current phase(LSP stability).]{lang="EN-US"}

[MAIN: Entered phase(LSP generation)]{lang="EN-US"}

[\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[UPDT: Started to purge local Level-1 LSP.]{lang="EN-US"}

[\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[UPDT: Ended to purge local Level-1 LSP.]{lang="EN-US"}

[\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Received module(updt) phase(LSP generation), current phase(LSP generation).]{lang="EN-US"}

[\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Entered phase(First SPF computation)]{lang="EN-US"}

[\*Sep 10 00:24:20:902 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Received module(dec) phase(First SPF computation), current phase(First SPF computation).]{lang="EN-US"}

[\*Sep 10 00:24:20:902 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Entered phase(Finish)]{lang="EN-US"}

[\*Sep 10 00:24:20:902 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;]{lang="EN-US"}

[MAIN: Graceful restart completed.]{lang="EN-US"}

::: {#1675083332 .myid}
[]{#_Toc404798003}[]{#struct_0_x1051_20145_x1095051756}

**SPBM \-- SPBM调试命令 \-- debugging spbm ha-event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x2043956571}

[**[debuging spbm ha-event]{lang="EN-US"}**]{#struct_0_x1051_20145_470704505}

[**[undo debuging spbm ha-event]{lang="EN-US"}**]{#struct_0_x1051_20145_1151620584}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1963795671}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_1106156153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x760345338}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_677275654}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_294769176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_24423476}

[[无]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2043956572}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_873989032}

[**[debugging spbm]{lang="EN-US"}**[ **ha-event**]{lang="EN-US"}]{#struct_0_x1051_20145_79310765}[命令用来打开]{style="font-family:宋体"}[SPBM HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging spbm]{lang="EN-US"}**[ **ha-event**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[SPBM HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM HA]{lang="EN-US"}]{#struct_0_x1051_20145_895228770}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-14 ]{lang="EN-US"}[debugging spbm ha-event]{lang="EN-US"}]{#struct_0_x1051_20145_801771167}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1796730153}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_176321174}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_176386710}

[[Failed to send real-time SPBM backup data.]{lang="EN-US"}]{#struct_0_x1051_20145_x1411087616}

[[发送]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_176452246}[实时备份数据失败]{style="font-family:宋体"}

[[Successful data batch backup for interface *interface-name*.]{lang="EN-US"}]{#struct_0_x1051_20145_425147484}

[[接口信息批量备份成功，其中]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1051_20145_176517782}[表示接口名]{style="font-family:宋体"}

[[Sequence number rollover timer backed up successfully.]{lang="EN-US"}]{#struct_0_x1051_20145_x336165909}

[[成功备份序列号翻转定时器]{style="font-family:宋体"}]{#struct_0_x1051_20145_176583318}

[[SPBM process stopped because an HA stop event was received.]{lang="EN-US"}]{#struct_0_x1051_20145_176648854}

[[接收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x1051_20145_1534176875}[停止事件，停止进程工作]{style="font-family:宋体"}

[[Notified the ADJ, UPDT, DEC, and FLUSH threads to stop.]{lang="EN-US"}]{#struct_0_x1051_20145_176714390}

[[通知线程（]{style="font-family:宋体"}[ADJ/UPDT/DEC/FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_x1667452547}[）停止工作]{style="font-family:宋体"}

[[Threads exited incorrectly before SPBM stopped.]{lang="EN-US"}]{#struct_0_x1051_20145_176124567}

[[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x881026281}[停止工作前，线程异常退出，这里的线程指]{style="font-family:宋体"}[ADJ/UPDT/DEC/FLUSH]{lang="EN-US"}[四个线程或其中若干]{style="font-family:宋体"}

[[Active SPBM process changed to standby state, and all its SPBM data was deleted.]{lang="EN-US"}]{#struct_0_x1051_20145_176190103}

[[降级（主进程变为备进程），删除进程所有相关数据]{style="font-family:宋体"}]{#struct_0_x1051_20145_1479329600}

[[Received HA upgrade event.]{lang="EN-US"}]{#struct_0_x1051_20145_176255639}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x1051_20145_137826001}[升级事件]{style="font-family:宋体"}

[[Failed to send cached data.]{lang="EN-US"}]{#struct_0_x1051_20145_176321175}

[[发送缓存数据失败，这里的数据指系统反压机制当中用于暂存数据的反压数据链上的数据]{style="font-family:宋体"}]{#struct_0_x1051_20145_x211367763}

[[Finished sending batch backup data in the cache.]{lang="EN-US"}]{#struct_0_x1051_20145_176386711}

[[缓存数据当中的批量备份相关数据已发送完毕]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1411087615}

[[Batch backup event finished.]{lang="EN-US"}]{#struct_0_x1051_20145_176452247}

[[批量备份事件结束]{style="font-family:宋体"}]{#struct_0_x1051_20145_425147483}

[[Upgrade event finished.]{lang="EN-US"}]{#struct_0_x1051_20145_176517783}

[[升级事件结束]{style="font-family:宋体"}]{#struct_0_x1051_20145_x336165910}

[[Stop event finished.]{lang="EN-US"}]{#struct_0_x1051_20145_176583319}

[[停止事件结束]{style="font-family:宋体"}]{#struct_0_x1051_20145_176648855}

[[Degrade event finished.]{lang="EN-US"}]{#struct_0_x1051_20145_1534176876}

[[降级事件结束]{style="font-family:宋体"}]{#struct_0_x1051_20145_176714391}

[[Notified other threads to start batch backup. Thread ID: *thread id*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1667452548}

[[通知其他线程进入批量备份流程，其中]{style="font-family:宋体"}*[thread id]{lang="EN-US"}*]{#struct_0_x1051_20145_176124564}[表示线程编号，]{style="font-family:宋体"}[1]{lang="EN-US"}[为]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[线程，]{style="font-family:宋体"}[2]{lang="EN-US"}[为]{style="font-family:宋体"}[UPDT]{lang="EN-US"}[线程，]{style="font-family:宋体"}[3]{lang="EN-US"}[为]{style="font-family:宋体"}[DEC]{lang="EN-US"}[线程，]{style="font-family:宋体"}[4]{lang="EN-US"}[为]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[线程]{style="font-family:宋体"}

[[Batch backup of SPBM data started.]{lang="EN-US"}]{#struct_0_x1051_20145_x881026280}

[[开始批量备份]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_176190100}[数据]{style="font-family:宋体"}

[[Connected to L2VPN successfully.]{lang="EN-US"}]{#struct_0_x1051_20145_1479329599}

[[与二层]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1051_20145_176255636}[连接成功]{style="font-family:宋体"}

[[Failed to connect to L2VPN.]{lang="EN-US"}]{#struct_0_x1051_20145_137825992}

[[与二层]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1051_20145_176321172}[连接失败]{style="font-family:宋体"}

[[Backup SPBM data, type: *type*]{lang="EN-US"}]{#struct_0_x1051_20145_x211367770}

[[备份]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_176386708}[所有数据，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[字段为数据类型，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process config]{lang="EN-US"}]{#struct_0_x1051_20145_927564552}[ ]{lang="EN-US"}[(basic&]{lang="EN-US"}[ECT-BVLAN]{lang="EN-US"}[)]{lang="EN-US"}[（包括进程基本配置数据及]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法与]{lang="EN-US" style="font-family:宋体"}[BVLAN]{lang="EN-US"}[的映射关系数据）：进程全局配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface config]{lang="EN-US"}]{#struct_0_x1051_20145_176452244}[：接口配置]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hostname]{lang="EN-US"}]{#struct_0_x1051_20145_176517780}[：动态主机名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MSTP]{lang="EN-US"}]{#struct_0_x1051_20145_x336165911}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface basic]{lang="EN-US"}]{#struct_0_x1051_20145_176583316}[：接口激活、]{lang="EN-US" style="font-family:
  宋体"}[updown]{lang="EN-US"}[状态及接口类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sequence number rollover timer]{lang="EN-US"}]{#struct_0_x1051_20145_832549018}[：序列号翻转定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPSourceID]{lang="EN-US"}]{#struct_0_x1051_20145_176648852}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overload]{lang="EN-US"}]{#struct_0_x1051_20145_176714388}[：过载机制，启动此项机能时，表示设备此时不具备处理流量数据的能力]{style="font-family:宋体"}

[[Received Main event, type: type]{lang="EN-US"}]{#struct_0_x1051_20145_671199605}

[[收到]{style="font-family:宋体"}[main]{lang="EN-US"}]{#struct_0_x1051_20145_176124565}[主线程事件，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[表示事件类型，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete interface]{lang="EN-US"}]{#struct_0_x1051_20145_x881026279}[：接口删除事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[thread ]{lang="EN-US"}]{#struct_0_x1051_20145_176190101}*[threadname]{lang="EN-US"}*[ ]{lang="EN-US"}[reset process]{lang="EN-US"}[：进程重置事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[threadname]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[MAIN/ADJ/UPDT/DEC/FLUSH]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[thread ]{lang="EN-US"}]{#struct_0_x1051_20145_176255637}*[threadname]{lang="EN-US"}*[ ]{lang="EN-US"}[stop event]{lang="EN-US"}[：线程停止事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[threadname]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[ADJ/UPDT/DEC/FLUSH]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[thread *threadname* ]{lang="EN-US"}[cancel T2 timer for GR]{lang="EN-US"}]{#struct_0_x1051_20145_137825991}[：取消]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[T2]{lang="EN-US"}[定时器事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[threadname]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[ADJ/UPDT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[the]{lang="EN-US"}[ GR ]{lang="EN-US"}]{#struct_0_x1051_20145_176321173}*[phasename]{lang="EN-US"}[ ]{lang="EN-US"}*[phase]{lang="EN-US"}[ completed]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}[结束]{style="font-family:宋体"}[事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[phasename]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[LSP stability/LSP generation/SPF computation/Flush smooth]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[start overload T2 for neighbour]{lang="EN-US"}]{#struct_0_x1051_20145_x211367769}[：开启]{lang="EN-US" style="font-family:宋体"}[overload]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[T2]{lang="EN-US"}[定时器事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR smooth ]{lang="EN-US"}]{#struct_0_x1051_20145_176386709}[completed]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[平滑完成事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[started ]{lang="EN-US"}]{#struct_0_x1051_20145_176452245}[flush]{lang="EN-US"}[ smooth]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[内核数据平滑]{style="font-family:宋体"}[开始事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[thread *threadname* ]{lang="EN-US"}[NSR smooth ]{lang="EN-US"}]{#struct_0_x1051_20145_425147481}[completed]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}[平滑完成事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[threadname]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[ADJ/UPDT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[the NSR *phasename* phase completed]{lang="EN-US"}]{#struct_0_x1051_20145_176517781}[：]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}[阶段结束事件，]{lang="EN-US" style="font-family:宋体"}*[phasename]{lang="EN-US"}*[取值为：]{lang="EN-US" style="font-family:宋体"}[LSP stability/LSP generation/SPF computation/Flush smooth]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[continue to send cache data]{lang="EN-US"}]{#struct_0_x1051_20145_x336165912}[：继续发送缓存数据事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[thread *threadname* ]{lang="EN-US"}[NSR batch backup ]{lang="EN-US"}]{#struct_0_x1051_20145_176583317}[completed]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}[批量备份]{style="font-family:宋体"}[完成事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[threadname]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[MAIN/ADJ/UPDT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[thread *threadname* GR]{lang="EN-US"}[ batch backup ]{lang="EN-US"}]{#struct_0_x1051_20145_176648853}[completed]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[批量备份]{style="font-family:宋体"}[完成事件]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[threadname]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}[MAIN/ADJ/UPDT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hostname backup]{lang="EN-US"}]{#struct_0_x1051_20145_1534176882}[：动态主机名备份事件]{lang="EN-US" style="font-family:
  宋体"}

[[Backup data.]{lang="EN-US"}]{#struct_0_x1051_20145_176714389}

[[Data type: *Data type,* subtype: *subtype*]{lang="EN-US"}]{#struct_0_x1051_20145_671199604}

[[备份数据，]{style="font-family:宋体"}*[Data type]{lang="EN-US"}*]{#struct_0_x1051_20145_176124570}[表示数据类型，]{style="font-family:宋体"}*[subtype]{lang="EN-US"}*[表示数据的具体子类型。]{style="font-family:宋体"}

[*[Data type]{lang="EN-US"}*]{#struct_0_x1051_20145_176190106}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPBM config data]{lang="EN-US"}]{#struct_0_x1051_20145_1479329605}[：全局配置数据，其中所包含的子类型字段有以下：]{lang="EN-US" style="font-family:
  宋体"}

[[SPBM status/bridge priority/ADJ log peer/LSP refresh timer/LSP max-age timer/flash flood/hostname/SPSource/SPBM agreement mode/overload/GR status/restart interval/suppress-sa/SPF calculating time interval/SPF generating time interval/bandwidth-reference/circuit cost/MAC address for SPBM multicast message/multicast BVLAN/(area-authentication-mode)/(area-authentication sendonly)/SNMP-agent trap/NSR status/reset standby/debug switch]{lang="EN-US"}]{#struct_0_x1051_20145_176255642}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPBM running data]{lang="EN-US"}]{#struct_0_x1051_20145_947130060}[：全局运行数据，其中所包含的子类型字段为]{lang="EN-US" style="font-family:
  宋体"}*[hostname]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface config]{lang="EN-US"}]{#struct_0_x1051_20145_176321178}[：接口配置数据，其中所包含的子类型字段有以下：]{lang="EN-US" style="font-family:
  宋体"}

[[enable SPBM under the interface/SPBM cost on the basis of interface/hello timer/holding multiplier timer/LSP sending interval/(interface-authentication-mode)/(interface-authentication sendonly)]{lang="EN-US"}]{#struct_0_x1051_20145_x211367776}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface basic running data]{lang="EN-US"}]{#struct_0_x1051_20145_176386714}[：接口运行数据，其中包含的备份子类型字段有如下：]{lang="EN-US" style="font-family:宋体"}

[[if SPBM enable, create circ info/delete the interface/interface active status/interface LAGG type/interface basic running data, circuit ID: *circuit ID*]{lang="EN-US"}]{#struct_0_x1051_20145_176452250}[，]{style="font-family:宋体"}*[circuit ID]{lang="EN-US"}*[为端口]{style="font-family:宋体"}[ID]{lang="EN-US"}[（批量备份时]{style="font-family:宋体"}[subtype]{lang="EN-US"}[字段为]{style="font-family:宋体"}[interface basic running data]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VSI config]{lang="EN-US"}]{#struct_0_x1051_20145_x1531167650}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[配置，其中所包含的子类型字段：]{lang="EN-US" style="font-family:宋体"}[ISID/multicast dup-mod]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VSI running data]{lang="EN-US"}]{#struct_0_x1051_20145_176517786}[：]{lang="EN-US" style="font-family:
  宋体"}[VSI]{lang="EN-US"}[运行数据，其中所包含的子类型字段：]{lang="EN-US" style="font-family:
  宋体"}[add]{lang="EN-US"}[ed VSI data, VSI index]{lang="EN-US"}[: ]{lang="EN-US"}*[vsi index]{lang="EN-US"}*[/]{lang="EN-US"}[delet]{lang="EN-US"}[ed VSI data, VSI Index]{lang="EN-US"}[: ]{lang="EN-US"}*[vsi index]{lang="EN-US"}*[/]{lang="EN-US"}[upda]{lang="EN-US"}[ted VSI data, VSI Index]{lang="EN-US"}[: ]{lang="EN-US"}*[vsi index]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}*[vsi index]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{style="font-family:宋体"}[（批量备份时]{lang="EN-US" style="font-family:宋体"}*[s]{lang="EN-US"}[ubtype]{lang="EN-US"}*[字段为]{lang="EN-US" style="font-family:宋体"}[add]{lang="EN-US"}[ed VSI data]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ECT-BVLAN]{lang="EN-US"}]{#struct_0_x1051_20145_x336165905}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[BVLAN]{lang="EN-US"}[的映射关系数据，其中子类型表示]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[o]{lang="EN-US"}[verload]{lang="EN-US"}]{#struct_0_x1051_20145_176583322}[：]{lang="EN-US" style="font-family:宋体"}[o]{lang="EN-US"}[verload]{lang="EN-US"}[相关数据，子类型字段为]{lang="EN-US" style="font-family:宋体"}[o]{lang="EN-US"}[verload]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x741429098}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_2117216969}[打开]{style="font-family:宋体"}[SPBM HA]{lang="EN-US"}[报文调试信息开关。启动一个备用主控板，触发数据批量备份。输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm ha-event]{lang="EN-US"}]{#struct_0_x1051_20145_176648858}

[\*Nov 30 22:00:00:166 2013 Sysname DEV/2/BOARD_STATE_FAULT: -MDC=1; Board state changes to FAULT on Slot 1, type is unknown.]{lang="EN-US"}

[\*Nov 30 22:00:02:105 2013 Sysname DEV/5/BOARD_STATE_NORMAL: -MDC=1; Board state changes to NORMAL on Slot 1, type is Simware.]{lang="EN-US"}

[\*Nov 30 22:00:02:205 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Batch backup of SPBM data started.]{lang="EN-US"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1051_20145_1534176887}*[开始批量备份]{style="font-family:宋体"}[SPBM]{lang="NO-BOK"}[数据]{style="font-family:宋体"}*

[[\*Nov 30 22:00:02:206 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}]{#struct_0_x1051_20145_2125999037}

[MAIN: Backup SPBM data, type: MSTP.]{lang="EN-US"}

[\*Nov 30 22:00:02:206 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: VSI running data, subtype: added VSI data.]{lang="EN-US"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1051_20145_x951173242}*[备份]{style="font-family:宋体"}[SPBM]{lang="NO-BOK"}[全局运行数据]{style="font-family:宋体"}*

[[\*Nov 30 22:00:02:210 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}]{#struct_0_x1051_20145_176714394}

[MAIN: Backup data. Data type: SPBM config data, subtype: SPBM status.]{lang="EN-US"}

[\*Nov 30 22:00:02:210 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: ADJ log peer.]{lang="EN-US"}

[\*Nov 30 22:00:02:210 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: LSP refresh timer.]{lang="EN-US"}

[\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: LSP max-age timer.]{lang="EN-US"}

[\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: flash flood.]{lang="EN-US"}

[\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: overload.]{lang="EN-US"}

[\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: GR status.]{lang="EN-US"}

[\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Backup data. Data type: SPBM config data, subtype: restart interval.]{lang="EN-US"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1051_20145_x1667452543}*[备份]{style="font-family:宋体"}[SPBM]{lang="NO-BOK"}[全局配置数据]{style="font-family:宋体"}*

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_535716041}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_665195503}[打开]{style="font-family:宋体"}[SPBM HA]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm ha-event]{lang="EN-US"}]{#struct_0_x1051_20145_x202194646}

[\*Dec 12 20:56:47:926 2012 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Recieved HA stop event,stopped SPBM data.]{lang="EN-US"}

[\*Dec 12 20:56:47:943 2012 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Notifying thread to stop work.]{lang="EN-US"}

[\*Dec 12 20:56:47:954 2012 Sysname SPBM/7/SPBM_HA: -MDC=1;]{lang="EN-US"}

[MAIN: Degrade(master to slave), deleted SPBM data.]{lang="EN-US"}

::: {#1363731722 .myid}
[]{#_Toc404798004}[]{#struct_0_x1051_20145_1503642439}

**SPBM \-- SPBM调试命令 \-- debugging spbm self-originate-update**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1486336668}

[**[debugging spbm self-originate-update]{lang="EN-US"}**]{#struct_0_x1051_20145_535650505}

[**[undo debugging spbm self-originate-update]{lang="EN-US"}**]{#struct_0_x1051_20145_x117977744}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1368344473}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_1226253914}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_227906034}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x9557878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_1963647890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_331449294}

[[无]{style="font-family:宋体"}]{#struct_0_x1051_20145_1486336667}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_534798537}

[**[debugging spbm self-originate-update]{lang="EN-US"}**]{#struct_0_x1051_20145_2081543157}[命令用来打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[本地更新的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm self-originate-update]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[本地更新的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_2011100796}[本地更新的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-15 ]{lang="EN-US"}[debugging spbm self-originate-update]{lang="EN-US"}]{#struct_0_x1051_20145_x1178339254}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1972329442}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1014474574}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_705015731}

[[UPDT: Started to rebuild all LSPs.]{lang="EN-US"}]{#struct_0_x1051_20145_1486336676}

[[开始]{style="font-family:宋体"}[rebuild]{lang="EN-US"}]{#struct_0_x1051_20145_x85478761}[所有的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[UPDT: Stopped to rebuild all LSPs.]{lang="EN-US"}]{#struct_0_x1051_20145_x2041793894}

[[结束]{style="font-family:宋体"}[rebuild]{lang="EN-US"}]{#struct_0_x1051_20145_x2041793884}[所有的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[UPDT: MTU change triggers rebuild.]{lang="EN-US"}]{#struct_0_x1051_20145_296858263}

[[MTU]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456867}[变化触发]{style="font-family:宋体"}[rebuild]{lang="EN-US"}

[[UPDT: LSP lifetime change triggers rebuild.]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456874}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x850152803}[生存周期变化触发]{style="font-family:宋体"}[rebuild]{lang="EN-US"}

[[UPDT: Attempting to exceed max sequence number.]{lang="EN-US"}]{#struct_0_x1051_20145_x850152810}

[[生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_1488499353}[时，序列号达到最大]{style="font-family:宋体"}

[[UPDT: Generating LSP= ]{lang="EN-US"}]{#struct_0_x1051_20145_x1155381588}*[lsp-id]{lang="EN-US"}*[, sequence number]{lang="EN-US"}*[= sequence-number]{lang="EN-US"}*[, length= ]{lang="EN-US"}*[lsp-length]{lang="EN-US"}*[.]{lang="EN-US"}

[[生成]{style="font-family:宋体"}]{#struct_0_x1051_20145_1488499352}[LSP]{lang="EN-US"}[结束，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1488499365}[：生成]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sequence-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x91966821}[：生成]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[的序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-length]{lang="EN-US"}*]{#struct_0_x1051_20145_x91966825}[：生成]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的长度]{lang="EN-US" style="font-family:宋体"}

[[UPDT: TLV change triggers rebuild.]{lang="EN-US"}]{#struct_0_x1051_20145_x327977030}

[[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1971096865}[变化触发]{style="font-family:宋体"}[rebuild]{lang="EN-US"}

[[UPDT: Purging LSP= ]{lang="EN-US"}]{#struct_0_x1051_20145_x1335168849}*[lsp-id]{lang="EN-US"}*[.]{lang="EN-US"}

[[清除]{style="font-family:宋体"}]{#struct_0_x1051_20145_x91966826}[LSP]{lang="EN-US"}[报文，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[被清除]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: Added area address *address.*]{lang="EN-US"}]{#struct_0_x1051_20145_x327977031}

[[添加区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1971031329}[，其中]{style="font-family:宋体"}*[address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[区域地址]{style="font-family:宋体"}

[[UPDT: Added protocol support *protocol.*]{lang="EN-US"}]{#struct_0_x1051_20145_597803118}

[[添加协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1213706096}[，其中]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[表示协议]{style="font-family:宋体"}

[[UPDT: Added host name *name.*]{lang="EN-US"}]{#struct_0_x1051_20145_x91966811}

[[添加]{style="font-family:宋体"}[host name TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1246001078}[，其中]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示主机名]{style="font-family:宋体"}

[[UPDT: Deleted host name *name.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2016102282}

[[删除]{style="font-family:宋体"}[host name TLV]{lang="EN-US"}]{#struct_0_x1051_20145_680953865}[，其中]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示主机名]{style="font-family:宋体"}

[[UPDT: Added Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*]{lang="EN-US"}]{#struct_0_x1051_20145_x91966812}

[[添加]{style="font-family:宋体"}[Instance TLV]{lang="EN-US"}]{#struct_0_x1051_20145_1246001077}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x2048281961}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ubit]{lang="EN-US"}*]{#struct_0_x1051_20145_290370202}[：]{lang="EN-US" style="font-family:宋体"}[u]{lang="EN-US"}[比特位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-algorithm]{lang="EN-US"}*]{#struct_0_x1051_20145_x1665944932}[：]{lang="EN-US" style="font-family:
  宋体"}[ECT]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Modified Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*]{lang="EN-US"}]{#struct_0_x1051_20145_926745212}

[[修改]{style="font-family:宋体"}[Instance sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x1133290968}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x856640869}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ubit]{lang="EN-US"}*]{#struct_0_x1051_20145_x856640860}[：]{lang="EN-US" style="font-family:宋体"}[u]{lang="EN-US"}[比特位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-algorithm]{lang="EN-US"}*]{#struct_0_x1051_20145_x89804131}[：]{lang="EN-US" style="font-family:
  宋体"}[ECT]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Deleted Instance sub-TLV: B-VLAN= *bvlan-number.*]{lang="EN-US"}]{#struct_0_x1051_20145_136556709}

[[删除]{style="font-family:宋体"}[Instance sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x89804132}[，其中]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值]{style="font-family:宋体"}

[[UPDT: Added I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*]{lang="EN-US"}]{#struct_0_x1051_20145_136556712}

[[添加]{style="font-family:宋体"}[I-SID sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x840531100}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x89804124}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x2046119273}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[t-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_292532889}[：]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[r-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x1663782244}[：]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Modified I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782245}

[[修改]{style="font-family:宋体"}[I-SID sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x2133155512}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x854478179}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x854478186}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[t-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1484173976}[：]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[r-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990694}[：]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标志位]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Deleted I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid.*]{lang="EN-US"}]{#struct_0_x1051_20145_x388419968}

[[删除]{style="font-family:宋体"}[I-SID sub-TLV]{lang="EN-US"}]{#struct_0_x1051_20145_702551219}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305828}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305820}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Added neighbor TLV: neighbor system ID=  *system-id*, cost=  *cost.*]{lang="EN-US"}]{#struct_0_x1051_20145_x363946372}

[[添加邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_303346333}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_303346326}[：邻居系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968808}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Modified neighbor TLV: neighbor system ID= *system-id*, cost= *cost.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968809}

[[修改邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x265993701}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987420}[：邻居系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987428}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Deleted neighbor TLV: neighbor system ID=  *system-id.*]{lang="EN-US"}]{#struct_0_x1051_20145_x76828003}

[[删除邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1051_20145_x76827995}[，其中]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[邻居系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1298395233}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x528566620}[打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[错误信息调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm self-originate-update]{lang="EN-US"}]{#struct_0_x1051_20145_2076514308}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_1463941909}[端口下使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，]{style="font-family:宋体"}[输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1051_20145_x76827996}

[\[Sysname\] interface gigabitethernet 0/1/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet0/1/3\] spbm enable]{lang="EN-US"}

[\*Sep 18 13:36:04:360 2012 Sysname SPBM/7/SPBM_1_ORG: -MDC=1;]{lang="EN-US"}

[UPDT: Added neighbor TLV: neighbor system ID= 0011.2200.1401, cost= 16777215.]{lang="EN-US"}

[\[Sysname-GigabitEthernet0/1/3\] \*Sep 18 13:36:06:367 2012 Sysname SPBM/7/SPBM_1_ORG: -MDC=1;]{lang="EN-US"}

[UPDT: Generating LSP= 0011.2200.0001.00-01, sequence number= 0x0000000b, length= 76.]{lang="EN-US"}

::: {#-1388856714 .myid}
[]{#_Toc404798005}[]{#struct_0_x1051_20145_1298395230}

**SPBM \-- SPBM调试命令 \-- debugging spbm snp-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x528501084}

[**[debugging spbm snp-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1051_20145_x1487964709}

[**[undo debugging spbm snp-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1051_20145_448904316}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1153307186}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1135386681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1378573188}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_1080075436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1988214394}

[**[receive]{lang="EN-US"}**]{#struct_0_x1051_20145_x609859049}[：表示接收]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1051_20145_8063828}[：表示发送]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1051_20145_1959239688}[：表示]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x83143288}

[**[debugging spbm snp-packet]{lang="EN-US"}**]{#struct_0_x1051_20145_1390070737}[命令用来打开]{style="font-family:
宋体"}[SPBM SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm snp-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM SNP]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143140}[报文的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-16 ]{lang="EN-US"}[debugging spbm snp-packet]{lang="EN-US"}]{#struct_0_x1051_20145_x129450465}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2010952006}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_367853918}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_141628270}

[[UPDT: Received *psnp-type* from *system-id* on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x716170191}

[[收到]{style="font-family:宋体"}[PSNP]{lang="EN-US"}]{#struct_0_x1051_20145_305509018}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[psnp-type]{lang="EN-US"}*]{#struct_0_x1051_20145_305509014}[：]{lang="EN-US" style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1 PSNP]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2 PSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806116}[：发送]{lang="EN-US" style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806120}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Received *csnp-type* from *source-id* on circuit *circuitName*. LSP-ID ranges from *start-lsp-id* to *end-lsp-id.*]{lang="EN-US"}]{#struct_0_x1051_20145_x57196949}

[[收到]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_x1051_20145_x841502058}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[csnp-type]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150108}[：]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1 CSNP]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2 CSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150104}[：发送]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程的]{lang="EN-US" style="font-family:宋体"}[SOURCE ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150116}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[start-lsp-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x96292094}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[摘要的起始]{lang="EN-US" style="font-family:
  宋体"}[LSP-ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[end-lsp-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x96292106}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要的结束]{lang="EN-US" style="font-family:宋体"}[LSP-ID]{lang="EN-US"}

[[UPDT: Sent *snp-type* on circuit *circuitName.*]{lang="EN-US"}]{#struct_0_x1051_20145_1897371198}

[[发送]{style="font-family:宋体"}[CSNP/PSNP]{lang="EN-US"}]{#struct_0_x1051_20145_322954286}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[snp-type]{lang="EN-US"}*]{#struct_0_x1051_20145_x2052607232}[：]{lang="EN-US" style="font-family:宋体"}[SNP]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1 CSNP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L2 CSNP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L1 PSNP]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2 PSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x2052607227}[：端口名称]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: No current LSP entry is found to build CSNP.]{lang="EN-US"}]{#struct_0_x1051_20145_1577569155}

[[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_x1051_20145_x112387349}[报文时，在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中没有找到起始]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}[或第一个比起始]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}[大的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[UPDT: LSP entry *lsp-id* processed is newer than LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_1954694875}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_1474646620}[摘要比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的新，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: LSP entry *lsp-id* processed is older than LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607242}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_1174153556}[摘要比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的旧，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: LSP entry *lsp-id* processed is the same as LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_1759422856}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_2103655251}[摘要和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的新旧程度一样，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: LSP entry *lsp-id* processed does not exist in LSDB.]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607241}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_770869029}[摘要在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中不存在，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: LSP entry *lsp-id* processed has not been loaded in CSNP.]{lang="EN-US"}]{#struct_0_x1051_20145_x152368842}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x925460732}[摘要在]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[中没有安装，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[UPDT: Received *pdutype* could not pass authentication, system ID= *system-id*, SNP has been ignored.]{lang="EN-US"}]{#struct_0_x1051_20145_286044926}

[[无法通过认证，]{style="font-family:宋体"}[SNP]{lang="EN-US"}]{#struct_0_x1051_20145_1087838096}[报文被丢弃，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pdutype]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270208}[：报文类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966154}[：发送]{lang="EN-US" style="font-family:宋体"}[SNP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程的]{lang="EN-US" style="font-family:宋体"}[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x860966153}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_624287048}[打开]{style="font-family:宋体"}[SPBM Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm snp-packet]{lang="EN-US"}]{#struct_0_x1051_20145_x1755044015}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x678985815}[端口下使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，]{style="font-family:宋体"}[输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> sysem-view]{lang="EN-US"}]{#struct_0_x1051_20145_1986879667}

[\[Sysname\] interface gigabitethernet 0/1/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet0/1/3\] spbm enable]{lang="EN-US"}

[\*Sep 18 14:54:58:058 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;]{lang="EN-US"}

[UPDT: Received L1 CSNP from 0011.2200.0a01 on circuit GigabitEthernet0/1/3. LSP-ID ranges from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff.]{lang="EN-US"}

[\*Sep 18 14:54:58:059 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 CSNP on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 14:54:59:918 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;]{lang="EN-US"}

[UPDT: Received L1 PSNP from 0011.2200.0a01 on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 14:54:59:987 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 PSNP on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

::: {#-745558900 .myid}
[]{#_Toc404798006}[]{#struct_0_x1051_20145_1477686014}

**SPBM \-- SPBM调试命令 \-- debugging spbm spf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_382988390}

[**[debugging]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1051_20145_660965319}**[spbm]{lang="EN-US"}**[ ]{lang="EN-US"}**[spf ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ ]{lang="EN-US"}[\]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1051_20145_446861466}**[debugging]{lang="EN-US"}**[ ]{lang="EN-US"}**[spbm]{lang="EN-US"}**[ ]{lang="EN-US"}**[spf]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ ]{lang="EN-US"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_901124601}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1601434588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_36201480}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x886716230}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_1477686015}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_382922854}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1051_20145_x895168528}[：表示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1108836152}

[**[debugging spbm spf]{lang="EN-US"}**]{#struct_0_x1051_20145_x1697985206}[命令用来打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}**[undo debugging spbm spf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x518753224}[路由计算调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-17 ]{lang="EN-US"}[debugging spbm spf]{lang="EN-US"}]{#struct_0_x1051_20145_1688171756}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1997636834}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1676612624}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_1477686016}

 

[[DEC: (MT*topology-id*) Calculating topology digest at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_382857318}

[[开始摘要计算，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1298167412}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x162691319}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x202729952}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686017}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: Before calculating digest, the edge count is *count*.]{lang="EN-US"}]{#struct_0_x1051_20145_382791782}

[[计算摘要之前边得数目，其中]{style="font-family:宋体"}]{#struct_0_x1051_20145_60798366}*[coun]{lang="EN-US"}[t]{lang="EN-US"}*[表示边的数目]{style="font-family:宋体"}

 

[[DEC: Calculating digest: delete the link eigenvalue from digest, link Src= *source-id*, link Dst= *dest-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_505536527}

[[从摘要中删除]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_1120128304}[的特征值，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686018}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_382726246}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[DEC: Calculating digest: add the link eigenvalue to digest, link Src= *source-id*, link Dst= *dest-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_1643320400}

[[添加]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_282477560}[的特征值到摘要中，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_981191023}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686019}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[DEC: Calculating digest: update the link eigenvalue from digest, link Src= *source-id*, link Dst= *dest-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_382660710}

[[更新摘要]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_83932933}[的特征值，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1633086442}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686020}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[DEC: After calculating digest, the edge count is *count*.]{lang="EN-US"}]{#struct_0_x1051_20145_383250533}

[[拓扑摘要计算完成之后边的数目]{style="font-family:宋体"}*[count]{lang="EN-US"}*]{#struct_0_x1051_20145_x1090927110}

 

[[DEC: Deleted the link from eigenvalue change list, link Src= *source-id*, link Dst= *dest-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_x616002120}

[[将]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_1477686021}[从]{style="font-family:宋体"}[LINK]{lang="EN-US"}[特征值变化链中删除，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_383184997}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x195544217}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[DEC: Added the link to eigenvalue change list, link Src= *source-id*, link Dst= *dest-id.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1468467085}

[[将]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_1477686006}[添加到]{style="font-family:宋体"}[LINK]{lang="EN-US"}[特征值变化链中，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_382857319}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1298167411}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[DEC: (MT*topology-id*) Invalid node (*system-id*) calculation. Then, FLUSH deleted all FDB entries. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_240593208}

[[计算节点无效，通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_1477686007}[删除所有的]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_382791783}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_60798367}[：计算节点的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1833115633}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129410}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Local node started topology calculation at Sec= *xxx*, MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x391430592}

[[当前节点开始进行拓扑计算，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_630335020}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129409}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1947221559}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_393394358}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) invalid and notified FLUSH to delete all multicast FDB entries at Sec= *xxx,* MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x94129408}

[[组播源节点无效，通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_1947221560}[删除所有的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_392804533}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1081553526}[：组播源节点的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129407}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1947221561}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) multicast FDB is calculating at Sec= *xxx*, MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_392870069}

[[组播源节点进行组播计算，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x94129406}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1947221562}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_392935605}[：组播源节点的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129405}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1947221563}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) All phases of SPF work completed at Sec= *xxx,* MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_393001141}

[[所有]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1051_20145_x94129404}[计算完成，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1947221564}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_392542389}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129403}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) used ECT *ect-index*, worked out the circuit index at *circuit index.* Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_1947221565}

[[使用指定]{style="font-family:宋体"}[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_392607925}[算法计算出根节点到指定节点的出端口索引，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129418}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x391430600}[：指定节点系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x943774171}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129417}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x391430599}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_630662700}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) used ECT *ect-index* to calculate. Run started at Sec= *xxx*, MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2050444546}

[[指定节点使用指定]{style="font-family:宋体"}[ECT]{lang="EN-US"}]{#struct_0_x1051_20145_x1230300313}[算法进行选路计算，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444545}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1633584840}[：节点系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x1633645948}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444544}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x67500899}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) There is no VLAN using the ECT *ect-index*. Notified FLUSH to delete the unicast FDB. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_870472891}

[[当期没有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_x1051_20145_x2050444543}[配置使用指定的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法，通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[删除所有的单播表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x827015786}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444542}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_739068155}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1784858977}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) DEC received B-VLAN ECT mapping changed message: operator type= *operatorId*, ECT-Index= *ect-index* ,B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x2050444541}

[[DEC]{lang="EN-US"}]{#struct_0_x1051_20145_335783628}[收到]{style="font-family:宋体"}[B-VLAN-ECT]{lang="EN-US"}[变化的消息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444540}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[operatorId]{lang="EN-US"}*]{#struct_0_x1051_20145_1901867569}[：添加，修改，删除操作标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_1308852409}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444539}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x20119052}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444554}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID calculating: found a node in the I-SID hash: B-VLAN= *bvlan-number* I-SID= *i-sid*. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x67566435}

[[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x2050444553}[计算在全网]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[哈希中查找定的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x827081322}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1280079121}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_288207614}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1970820139}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_288207615}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Added a new multicast source(*system-id*). Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_1970820140}

[[新增组播源，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_288207616}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1970820141}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1754713085}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_288207617}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1970820142}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) added a new T-flag: I-SID= *i-sid,* B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_288207618}

[[组播源节点新增一个置位]{style="font-family:宋体"}[T Flag]{lang="EN-US"}]{#struct_0_x1051_20145_1970820127}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_288207619}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1970820128}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_288207620}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_14504999}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_288207621}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_14505000}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) added a new T-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*, count= *count*. Run started at Sec= xxx, MSec= yyy.]{lang="EN-US"}]{#struct_0_x1051_20145_288207606}

[[显示组播源节点]{style="font-family:宋体"}[T Flag]{lang="EN-US"}]{#struct_0_x1051_20145_x367832019}[置位的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[个数，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_994970365}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_288207607}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x367832018}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107522}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_x1051_20145_1127295237}[：]{lang="EN-US" style="font-family:宋体"}[T Flag]{lang="EN-US"}[置位的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[的个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107521}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1601588118}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) changed to non-multicast source. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107520}

[[节点有组播源变成非组播源，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x35504177}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107519}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1958015086}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107518}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x391931145}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) deleted a T-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107517}

[[组播源节点删除一个置位]{style="font-family:宋体"}[T Flag]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107516}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1198500199}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107515}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_367583742}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107530}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x35569713}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107529}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) added a R-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1957818478}

[[组播源节点添加一个置位]{style="font-family:宋体"}[R Flag]{lang="EN-US"}]{#struct_0_x1051_20145_x858803458}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803457}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1729402167}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803456}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1729467703}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803455}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1729533239}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) deleted a R-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x858803454}

[[组播源节点删除一个置位]{style="font-family:宋体"}[R Flag]{lang="EN-US"}]{#struct_0_x1051_20145_1729598775}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803453}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803452}[：组播源的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1729205559}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803451}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1729271095}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803466}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID incremental calculation started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x858803465}

[[组播增量计算开始，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_1729533242}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848702}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1257205977}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848703}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) was calculating multicast FDB. Run started at Sec= *xxx*, MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1257271513}

[[指定节点开始计算组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_x1051_20145_1479848704}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848705}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1256878297}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848706}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848707}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) UPDT notified node(*system-id*) to add the I-SID change list: I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1257009369}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_1479848708}[通知组播源节点增加]{style="font-family:宋体"}[I-SID,]{lang="EN-US"}[挂载到]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[变化链，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1257599193}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848709}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848694}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1081839406}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[T-]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848695}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-]{lang="EN-US"}*]{#struct_0_x1051_20145_1081773870}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617474}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617473}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) UPDT notified node(*system-id*) to modify the T-flag and the R-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1929490570}

[[UPDT]{lang="EN-US"}]{#struct_0_x1051_20145_x100617472}[通知组播源节点修改指定]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617471}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1929621642}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617470}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617469}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[T-]{lang="EN-US"}*]{#struct_0_x1051_20145_x1930145929}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617468}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617467}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1929228425}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) On the node(*system-id*) was deleted from the I-SID change list: I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec *= xxx,* MSec *= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x100617482}

[[在]{style="font-family:宋体"}]{#struct_0_x1051_20145_x100617481}[组播源节点上从]{style="font-family:宋体"}[I-SID ]{lang="EN-US"}[变化链上删除]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1929621635}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932610}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932609}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x952737164}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[T-]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932608}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932607}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1823200358}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932606}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) DEC added the count(*count*) of I-SID T-flag. The new multicast flag is *flag*. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2056932605}

[[组播源节点新增一个置位]{style="font-family:宋体"}[T-flag]{lang="EN-US"}]{#struct_0_x1051_20145_x2056932604}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x905682997}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932603}[：]{lang="EN-US" style="font-family:宋体"}[T-]{lang="EN-US"}[f]{lang="EN-US"}[lag]{lang="EN-US"}[置位的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[的个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932618}[：新增组播源标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1776211727}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932617}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) UPDT notified node(*system-id*) to add same I-SID and B-VLAN. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_281719550}

[[组播源节点新增一个相同]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_281719551}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x642689517}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_281719552}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_281719553}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x642689519}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) modified to add the count(*count*) of I-SID T-flag. The new multicast flag is *Flag*. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_281719554}

[[组播源修改]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_281719555}[，]{style="font-family:宋体"}[T Flag]{lang="EN-US"}[置位，计数增加，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_281719556}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x642689522}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_x1051_20145_281719557}[：]{lang="EN-US" style="font-family:宋体"}[T Flag]{lang="EN-US"}[置位的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[的个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Flag]{lang="EN-US"}*]{#struct_0_x1051_20145_281719542}[：新增组播源标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_281719543}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1695962641}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) modified to delete the count(*count*) of I-SID T-flag. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595586}

[[组播源修改]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595585}[，]{style="font-family:宋体"}[T Flag]{lang="EN-US"}[清零，计数减少，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595584}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1117234230}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595583}[：]{lang="EN-US" style="font-family:宋体"}[T Flag]{lang="EN-US"}[置位的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[的个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595582}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595581}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) deleted I-SID T-flag count(*count*) .]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595580}

[[组播源删除]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_1208364598}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595579}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595594}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595593}[：]{lang="EN-US" style="font-family:宋体"}[T Flag]{lang="EN-US"}[置位的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[的个数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: Deleted the node from I-SID hash: B-VLAN= *bvlan-number*, I-SID= *i-sid*. Run at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x865291522}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_1601279291}[哈希中删除指定的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291521}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i]{lang="EN-US"}[-]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291520}*[sid]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291519}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291518}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) added I-SID and B-VLAN to I-SID hash. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_1600623932}

[[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x865291517}[哈希中添加相同的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291516}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291515}[：组播源的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291530}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1601148218}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) received I-SID change message: operator type= *operator type*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x865291529}

[[DEC]{lang="EN-US"}]{#struct_0_x1051_20145_1473360638}[收到]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[变化的消息，显示消息内容，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360639}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360640}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[operator type]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360641}[：操作类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1064449318}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360642}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}[的值]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[T-]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360643}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[T]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360644}*[f]{lang="EN-US"}[lag]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[携带的]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360645}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360630}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [*Operation* link *linksrc*]{.TableTextChar} [\--\> *linkdst*, with attribute *Link-flag*1*,*]{.TableTextChar} [*Link-flag*2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_1473360631}

[[DEC]{lang="EN-US"}]{#struct_0_x1051_20145_1064449325}[处理]{style="font-family:宋体"}[LINK]{lang="EN-US"}[变化链时的]{style="font-family:宋体"}[LINK]{lang="EN-US"}[相关的调试信息，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x98454786}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[*[Operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x98454785}[：]{lang="EN-US" style="font-family:宋体"}[LINK]{lang="EN-US"}[的变化情况，有有]{style="font-family:宋体"}[Increased]{lang="EN-US"}[、]{style="font-family:宋体"}[Decreased]{lang="EN-US"}[和]{style="font-family:宋体"}[Destroyed]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[*[linksrc]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x98454784}[：]{lang="EN-US" style="font-family:宋体"}[LINK]{lang="EN-US"}[的源节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[*[linkdst]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x98454783}[：]{lang="EN-US" style="font-family:宋体"}[LINK]{lang="EN-US"}[的目的节点]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Link-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_283882242}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_283882243}[：]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Back]{lang="EN-US"}]{#struct_0_x1051_20145_283882244}[：]{style="font-family:宋体"}[回指链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Increase]{lang="EN-US"}]{#struct_0_x1051_20145_283882245}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[变大]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Decrease]{lang="EN-US"}]{#struct_0_x1051_20145_283882230}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[变小]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_283882231}[：待删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432898}[nvolve]{lang="EN-US"}[：受影响]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NewPath]{lang="EN-US"}]{#struct_0_x1051_20145_x954738561}[：新增路径]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [SRC node found,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432897}

[[找到源节点，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1672432896}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432895}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432894}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432893}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432892}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1475523329}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_1475523330}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_1475523331}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_1475523332}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_1475523333}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_1475523318}[：]{style="font-family:宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_1475523319}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [DST node found,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_x87641346}

[[找到目的节点，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x87641345}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641344}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641343}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641342}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641341}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_294695680}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_294695681}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_294695682}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_294695683}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_294695684}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_294695685}[：]{style="font-family:宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_294695670}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [Destroyed node,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_294695671}

[[销毁节点，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1661619458}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1661619457}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1661619456}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x1661619455}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x1661619454}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1486336767}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_1486336768}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_1486336769}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_1486336770}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_1486336771}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_1486336772}[：]{style="font-family:宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_1486336773}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [Changed node o]{.TableTextChar}verload[ flag,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_1486336758}

[[改变]{style="font-family:宋体"}[overload]{lang="EN-US"}]{#struct_0_x1051_20145_1486336759}[标志，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x85478658}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x85478657}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x85478656}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x85478655}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_296858367}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_296858368}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_296858369}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_296858370}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_296858371}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_296858372}[：]{style="font-family:宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_296858373}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [Created(new) node,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_296858358}

[[创建新节点，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_296858359}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1659456770}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1659456769}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x1659456768}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x1659456767}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_1488499455}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_x91966717}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{lang="EN-US" style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_x91966716}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_x91966715}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_x91966730}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_x91966729}[：]{style="font-family:宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281858}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [Created(exist) node,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281857}

[[节点已存在，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2048281856}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2048281855}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2048281854}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x2048281853}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x2048281852}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x1665944830}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944828}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944827}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944842}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944841}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_x856640770}[：]{style="font-family:
  宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x856640769}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [Set overload flag on node,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_x856640768}

[[设置]{style="font-family:宋体"}[overload]{lang="EN-US"}]{#struct_0_x1051_20145_x856640767}[标志，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x856640766}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x856640765}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x856640763}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x856640778}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x89804028}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_x89804027}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_x89804042}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_x89804041}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119170}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119169}[：]{style="font-family:
  宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119167}[：待删除]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) [Set direct flag on node,]{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, [with attribute ]{.TableTextChar}*Node-flag*[1, ]{.TableTextChar}*Node-flag*[2]{.TableTextChar}.]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119166}

[[设置和父节点直连的标志，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2046119165}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2046119164}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2046119163}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrcount]{lang="EN-US"}*]{#struct_0_x1051_20145_x2046119178}[：]{lang="EN-US" style="font-family:宋体"}[邻居个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentcount]{lang="EN-US"}*]{#struct_0_x1051_20145_292532990}[：]{lang="EN-US" style="font-family:
  宋体"}[父节点个数]{style="font-family:宋体"}

[[另外]{style="font-family:宋体"}*[Node-flag]{lang="EN-US"}*]{#struct_0_x1051_20145_x1663782154}[可能有多个，含义分别是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RmtNbr]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782153}[：]{lang="EN-US" style="font-family:宋体"}[忽略]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree]{lang="EN-US"}]{#struct_0_x1051_20145_x854478082}[：]{style="font-family:宋体"}[在树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tent]{lang="EN-US"}]{#struct_0_x1051_20145_x854478081}[：]{style="font-family:宋体"}[在备选链表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1051_20145_x854478079}[：]{lang="EN-US" style="font-family:宋体"}[与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overload]{lang="EN-US"}]{#struct_0_x1051_20145_x854478078}[：]{style="font-family:
  宋体"}[Overload]{lang="EN-US"}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x854478077}[：待删除]{style="font-family:宋体"}

 

[[DEC: Affected node not found.]{lang="EN-US"}]{#struct_0_x1051_20145_x854478076}

[[处理]{style="font-family:宋体"}]{#struct_0_x1051_20145_x854478075}[LINK]{lang="EN-US"}[变化量过程中，]{style="font-family:宋体"}[LINK]{lang="EN-US"}[变化受影响的节点没有找到]{style="font-family:宋体"}

 

[[DEC: DST node not found. 2-way check failed.]{lang="EN-US"}]{#struct_0_x1051_20145_x854478089}

[[目的系统]{style="font-family:宋体"}]{#struct_0_x1051_20145_1484174078}[ID]{lang="EN-US"}[没有找到，双向]{style="font-family:宋体"}[LINK]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

 

[[DEC: DST node was to be deleted. 2-way check failed.]{lang="EN-US"}]{#struct_0_x1051_20145_1484174079}

[[目的系统]{style="font-family:宋体"}]{#struct_0_x1051_20145_1484174080}[ID]{lang="EN-US"}[即将被删除，双向]{style="font-family:宋体"}[LINK]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

 

[[DEC: Src & Dst node were both in INIT state. 2-way check failed.]{lang="EN-US"}]{#struct_0_x1051_20145_1484174081}

[[源系统]{style="font-family:宋体"}]{#struct_0_x1051_20145_1484174083}[ID]{lang="EN-US"}[和目的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[都处于初始化状态，双向]{style="font-family:宋体"}[LINK]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

 

[[DEC: Backward link not found. 2-way check failed.]{lang="EN-US"}]{#struct_0_x1051_20145_1484174084}

[[回指]{style="font-family:宋体"}]{#struct_0_x1051_20145_1484174085}[LINK]{lang="EN-US"}[没有找到，双向]{style="font-family:宋体"}[LINK]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

 

[[DEC: Checking changed links.]{lang="EN-US"}]{#struct_0_x1051_20145_1484174070}

[[处理]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_1484174071}[变化链上的]{style="font-family:宋体"}[LINK]{lang="EN-US"}

 

[[DEC: Need rebuild SPT.]{lang="EN-US"}]{#struct_0_x1051_20145_x78990593}

[[ISPF]{lang="EN-US"}]{#struct_0_x1051_20145_x78990592}[决策出需要重新计算拓扑树]{style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Link(Src= *source-id*, Dst= *dest-id*) moved from parent list. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x78990591}

[[将指定的]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_x78990590}[源节点的父节点]{style="font-family:宋体"}[LIST]{lang="EN-US"}[中删除，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990589}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990588}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990602}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x78990601}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305730}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) added to candidate list. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2035305729}

[[将指定节点加入拓扑树中的候选链，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2035305727}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305726}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305725}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305724}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2035305723}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Link(Src = *source-id*, Dst = *dest-id*) added to parent list. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2035305737}

[[将指定的]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_303346430}[加入到源节点的父节点]{style="font-family:宋体"}[LIST]{lang="EN-US"}[中，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_303346431}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_303346432}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_303346433}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_303346435}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_303346436}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) The link is invalid. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_303346437}

[[拓扑计算过程中判断出]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_303346422}[是无效]{style="font-family:宋体"}[LINK]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968706}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968705}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968704}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) The node(*system-id*) is invalid. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968702}

[[拓扑计算过程中判断出]{style="font-family:宋体"}[NODE]{lang="EN-US"}]{#struct_0_x1051_20145_x1652968701}[是无效的，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968700}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968699}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1652968713}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x843664642}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Set SPF flag on link(Src = *source-id*, Dst = *dest-id*). Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x843664641}

[[将指定]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_x843664639}[打上]{style="font-family:宋体"}[IS_SPF_LINK]{lang="EN-US"}[标记，标明在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x843664638}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x843664637}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x843664635}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x843664650}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x843664649}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Running Dijkstra algorithm, current calculating root node is *system-id*. Run started at Sec*= xxx,* MSec*= yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_1494987519}

[[指定根节点正在执行]{style="font-family:宋体"}[Dijkstra]{lang="EN-US"}]{#struct_0_x1051_20145_1494987520}[算法计算拓扑树，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987521}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987523}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987524}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1494987525}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) added to order list. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_1494987511}

[[指定节点加入]{style="font-family:宋体"}[orderlist]{lang="EN-US"}]{#struct_0_x1051_20145_x76827906}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x76827905}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x76827903}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x76827902}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x76827901}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) The node(*system-id*) will be deleted. Run started at Sec*= xxx,* MSec*= yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x76827899}

[[在拓扑计算过程中将要删除节点，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x76827914}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x76827913}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2033143041}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x2033143040}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2033143038}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Checked reachability of node(*system-id*). Run started at Sec*= xxx,* MSec*= yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x2033143037}

[[检查节点拓扑是否可达，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2033143036}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2033143035}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2033143049}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_305509118}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_305509119}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Topology calculation ISPF decision at Sec*= xxx,* MSec*= yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_305509121}

[[拓扑增量决策，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_305509122}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_305509124}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_305509125}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_305509110}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Checked link(Src= *source-id*, Dst= *dest-id,* validCost*= cost*). Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806018}

[[检查]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_x1650806017}[是否有效]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806016}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806014}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806013}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806012}[：有效度量值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806026}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1650806025}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Reset SPF link information. Run started at Sec*= xxx,* MSec*= yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x841501953}

[[重置所有]{style="font-family:宋体"}[LINK]{lang="EN-US"}]{#struct_0_x1051_20145_x841501952}[拓扑计算的标志位，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x841501951}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x841501949}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x841501948}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID pruning calculation root node(*system-id*), destination node(*system-id*), calculate I-SID= *i-sid*, ECT-Index= *ect-index*, circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x841501962}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x841501961}[全计算过程中添加组播出端口，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150206}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150208}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150209}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150211}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150212}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1497150198}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID incremental calculation root node(*system-id*), destination node(*system-id*), calculate I-SID= *i-sid*, ECT-Index= *ect-index*, circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_1497150199}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x96291998}[增量计算过程中添加组播出端口，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x96291995}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x96292001}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x96292002}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x96291999}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x96292005}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x96292006}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2052607134}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID incremental calculation. DEC notified FLUSH to add designated port index= *circuit index,*ECT-Index= *ect-index*. Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607131}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x2052607137}[增量计算过程中]{style="font-family:宋体"}[DEC]{lang="EN-US"}[通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[添加指定端口]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2052607135}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2052607136}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2052607141}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_286045027}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_286045029}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID incremental calculation. DEC notified FLUSH to add I-SID= *i-sid*, B-VLAN= *bvlan-number*, ECT-Index= *ect-index,* circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_286045028}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_286045022}[增量计算过程中通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[添加组播转发表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_286045025}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_286045019}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_286045018}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270110}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[index]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270107}[：端口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270113}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1670270114}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Node(*system-id*) is calculating I-SID(*i-sid*) pruning*,* ECT-Index= *ect-index*, circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270112}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x1670270117}[全计算过程中添加组播出端口，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966045}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966046}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966044}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966050}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966047}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966053}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x860966054}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID pruning calculation. DEC notified FLUSH to delete I-SID= *i-sid*, B-VLAN= *bvlan-number*, ECT-Index= *ect-index,* circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_1477686114}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_1477686117}[剪枝中通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[删除组播转发表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686111}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686110}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686112}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_1477686106}[：]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129309}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129307}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129308}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) I-SID pruning calculation. DEC notified FLUSH to delete designated port index= *circuit index,* ECT-Index= *ect-index.* Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x94129314}

[[在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}]{#struct_0_x1051_20145_x94129312}[剪枝中]{style="font-family:宋体"}[DEC]{lang="EN-US"}[通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}[删除端口角色]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x94129317}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444445}[：]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444446}[：端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444444}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x2050444450}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Cleared all multicast FDB of the node(*system-id*). Run started at Sec*= xxx,* MSec*= yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x2050444447}

[[清除节点下的所有指定端口信息，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2050444453}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_288207715}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_288207714}[：节点的]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_288207716}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_288207710}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

 

[[DEC: (MT*topology-id*) Cleared all information of the node(*system-id*). Run started at Sec= *xxx,* MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_288207713}

[[拓扑计算过程中清除]{style="font-family:宋体"}[NODE]{lang="EN-US"}]{#struct_0_x1051_20145_288207707}[上的所有信息：包括节点的父节点]{style="font-family:宋体"}[LIST]{lang="EN-US"}[，节点到根节点的跳数以及到根节点的距离，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107421}[：]{lang="EN-US" style="font-family:
  宋体"}[拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107419}[：]{lang="EN-US" style="font-family:宋体"}[拓扑节点]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107420}[：]{lang="EN-US" style="font-family:宋体"}[秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1668107426}[：]{lang="EN-US" style="font-family:宋体"}[毫秒数]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) Reset SPF node information.  Run started at Sec= *xxx,* MSec= *yyy.*]{lang="EN-US"}]{#struct_0_x1051_20145_x1668107424}

[[清除节点上的所有标记]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1668107429}

[[DEC: (MT*topology-id*) Triggered SPF at Sec= *xxx,* MSec= *yyy*, scheduled event, old= *trigger  event*, new= *trigger* *event.*]{lang="EN-US"}]{#struct_0_x1051_20145_x858803357}

[[开始新的触发，显示旧的和新的触发类型，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x858803355}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803356}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trigger event]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803362}[：触发事件]{lang="EN-US" style="font-family:
  宋体"}[ ]{lang="EN-US"}[包括摘要计算、拓扑全计算、拓扑增量计算、]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN-ECT]{lang="EN-US"}[变化处理、]{lang="EN-US" style="font-family:宋体"}[I-SID-B-VLAN]{lang="EN-US"}[变化处理、停止计算]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803360}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x858803365}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) SPF event *trigger-event* was scheduled.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848803}

[[新旧触发类型合并后的触发类型，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_1479848802}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848804}[：]{lang="EN-US" style="font-family:
  宋体"}[拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trigger event]{lang="EN-US"}*]{#struct_0_x1051_20145_1479848798}[：]{lang="EN-US" style="font-family:
  宋体"}[合并之后的触发事件]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) SPF was not allowed to run for inactive topology state.]{lang="EN-US"}]{#struct_0_x1051_20145_1479848800}

[[当前系统处于]{style="font-family:宋体"}[RESET]{lang="EN-US"}]{#struct_0_x1051_20145_1479848795}[阶段，不允许拓扑计算]{style="font-family:宋体"}

[[DEC: (MT*topology-id*) SPF stopped current running work.]{lang="EN-US"}]{#struct_0_x1051_20145_x100617373}

[[当前来了优先级更高的拓扑触发事件，停止当前的操作，其中]{style="font-family:宋体"}]{#struct_0_x1051_20145_x100617371}*[topology-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[DEC: (MT*topology-id*) SPF needed to restart, current running flag= *trigger-event*, new trigger flag= *trigger-event*.]{lang="EN-US"}]{#struct_0_x1051_20145_x100617372}

[[拓扑事件能够合并，合并之前的事件，合并之后的事件，其中：]{style="font-family:宋体"}]{#struct_0_x1051_20145_x100617378}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617376}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trigger event]{lang="EN-US"}*]{#struct_0_x1051_20145_x100617381}[：]{lang="EN-US" style="font-family:
  宋体"}[合并之后的触发事件]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) Node(*system-id*) notified FLUSH to add ECT-Index= *ect-index* output port index= *circuit index*. Run started at Sec= *xxx,* MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x2056932509}

[[通知]{style="font-family:宋体"}[FLUSH]{lang="EN-US"}]{#struct_0_x1051_20145_x2056932507}[删除当前节点到指定节点在指定]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法下的出端口索引，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932508}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932514}[：指定]{lang="EN-US" style="font-family:宋体"}[系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ect-index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932512}[：指定]{lang="EN-US" style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit index]{lang="EN-US"}*]{#struct_0_x1051_20145_x2056932517}[：出端口索引]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_281719651}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_281719653}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) Notified node(*system-id*) to add egress FDB: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx,* MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_281719652}

[[通知节点添加]{style="font-family:宋体"}[egress]{lang="EN-US"}]{#struct_0_x1051_20145_281719646}[表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_281719648}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_281719643}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595485}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595483}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595489}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_x1674595490}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) Notified node(*system-id*) to delete egress FDB: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx,* MSec= *yyy*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595488}

[[通知节点删除]{style="font-family:宋体"}[egress]{lang="EN-US"}]{#struct_0_x1051_20145_x1674595494}[表项，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291422}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291419}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i-sid]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291425}[：]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bvlan-number]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291423}[：]{lang="EN-US" style="font-family:
  宋体"}[B-VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_x1051_20145_x865291429}[：秒数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360739}[：毫秒数]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) SPF node(*system-id*) was *updatedType*.]{lang="EN-US"}]{#struct_0_x1051_20145_1473360738}

[[通知]{style="font-family:宋体"}[DEC]{lang="EN-US"}]{#struct_0_x1051_20145_1473360740}[模块添加]{style="font-family:宋体"}[/]{lang="EN-US"}[修改]{style="font-family:宋体"}[/]{lang="EN-US"}[删除节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360734}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360736}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updatedType]{lang="EN-US"}*]{#struct_0_x1051_20145_1473360731}[：更新类型（添加]{lang="EN-US" style="font-family:
  宋体"}[/]{lang="EN-US"}[删除]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[修改）]{lang="EN-US" style="font-family:宋体"}

[[DEC: (MT*topology-id*) SPF link *source-id* \--\> *dest-id* was *updatedType*: cost*= cost*.]{lang="EN-US"}]{#struct_0_x1051_20145_x98454685}

[[通知]{style="font-family:宋体"}[DEC]{lang="EN-US"}]{#struct_0_x1051_20145_x98454683}[模块添加]{style="font-family:宋体"}[/]{lang="EN-US"}[修改]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[link]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x98454689}[：拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x98454687}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x98454688}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[updatedType]{lang="EN-US"}*]{#struct_0_x1051_20145_x98454694}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[修改）]{lang="EN-US" style="font-family:宋体"}[link]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_x1051_20145_x2054769822}[：]{lang="EN-US" style="font-family:宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_795282530}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x1578711668}[两台设备建邻居]{style="font-family:宋体"}[DUT1]{lang="EN-US"}[和]{style="font-family:宋体"}[DUT2]{lang="EN-US"}[，在]{style="font-family:宋体"}[DTU1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[I-SID 300]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[，打开]{style="font-family:宋体"}[SPF]{lang="EN-US"}[调试信息]{style="font-family:宋体"}[\
]{lang="EN-US"}[在]{style="font-family:宋体"}[DUT2]{lang="EN-US"}[上同样配置]{style="font-family:宋体"}[I-SID 300]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm spf]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769820}

[\*Jan 29 15:22:32:612 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Create(new) link 0011.2200.0001 \--\> 0011.2200.0a01.]{lang="EN-US"}

[\*Jan 29 15:22:32:612 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Adding new source entry for Link 0011.2200.0001 \--\> 0011.2200.0a01.]{lang="EN-US"}

[\*Jan 29 15:22:32:652 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Node(0011-2200-0a01) received I-SID change message: operator type= 1, I-SID= 300, B-VLAN= 1, T-flag= 1, R-flag= 1. Run started at Sec= 23513, MSec= 652.]{lang="EN-US"}

[\*Jan 29 15:22:32:652 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Create(new) link 0011.2200.0a01 \--\> 0011.2200.0001.]{lang="EN-US"}

[\*Jan 29 15:22:32:653 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Adding new source entry for Link 0011.2200.0a01 \--\> 0011.2200.0001.]{lang="EN-US"}

[\*Jan 29 15:22:32:653 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: Added the link to eigenvalue change list, link Src= 0011-2200-0a01, link Dst=  0011-2200-0001.]{lang="EN-US"}

[\*Jan 29 15:22:32:716 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Node(0011-2200-0001) received I-SID change message: operator type= 1, I-SID= 300, B-VLAN= 1, T-flag= 1, R-flag= 1. Run started at Sec= 23513, MSec= 716.]{lang="EN-US"}

[\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Topology digest is calculating at Sec= 23513, MSec= 907.]{lang="EN-US"}

[\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Local node topology is calculating at Sec= 23513, MSec= 907.]{lang="EN-US"}

[\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Running Dijkstra algorithm, current calculating root node is 0011-2200-0001. Run started at Sec= 23513, MSec= 907.]{lang="EN-US"}

[\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Node(0011-2200-0a01) multicast FDB is calculating at Sec= 23513, MSec= 907.]{lang="EN-US"}

[\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Running Dijkstra algorithm, current calculating root node is 0011-2200-0a01. Run started at Sec= 23513, MSec= 907.]{lang="EN-US"}

[\*Jan 29 15:22:32:908 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) All phases of SPF work completed at Sec= 23513, MSec= 908.]{lang="EN-US"}

::: {#823074074 .myid}
[]{#_Toc404798007}[]{#struct_0_x1051_20145_x367516884}

**SPBM \-- SPBM调试命令 \-- debugging spbm timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_558554319}

[**[debugging spbm timer]{lang="EN-US"}**]{#struct_0_x1051_20145_2066018862}

[**[undo debugging spbm timer]{lang="EN-US"}**]{#struct_0_x1051_20145_1818403449}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x2000509236}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x550259589}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1098374629}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x238834295}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x2054769825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_391998003}

[[无]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1044907137}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_90652865}

[**[debugging spbm timer]{lang="EN-US"}**]{#struct_0_x1051_20145_1438580891}[命令用来打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[定时器的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm timer]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[定时器的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x1197140863}[定时器的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-18 ]{lang="EN-US"}[debugging spbm timer]{lang="EN-US"}]{#struct_0_x1051_20145_x199732566}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1994662243}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x2054769826}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1174085938}

[[ADJ: Level-1 adjacency *system-id* hold timer expired on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1839286576}

[[Level-1]{lang="EN-US"}]{#struct_0_x1051_20145_x1959005041}[邻居]{style="font-family:宋体"}[hold time]{lang="EN-US"}[定时器超时，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1735514565}[：邻居系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x2054769823}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[[ADJ: P2P Hello timer expired on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x770801411}

[[P2P Hello]{lang="EN-US"}]{#struct_0_x1051_20145_75009640}[定时器超时，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[DEC: (MT*topology-id)* Started SPF timer, timer value is *Millisecond* ms.]{lang="EN-US"}]{#struct_0_x1051_20145_1363076572}

[[开启]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1051_20145_283882338}[定时器进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算调度，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1532855243}[：拓扑号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Millisecond]{lang="EN-US"}*]{#struct_0_x1051_20145_166606698}[：定时器的当前时间间隔]{lang="EN-US" style="font-family:
  宋体"}

[[DEC: (MT*topology-id*) Stopped SPF timer.]{lang="EN-US"}]{#struct_0_x1051_20145_x1004728475}

[[关闭]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1051_20145_283882337}[定时器停止]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算调度，其中]{style="font-family:宋体"}*[topology-id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[DEC: (MT*topology-id*) SPF timer expired.]{lang="EN-US"}]{#struct_0_x1051_20145_x1532855244}

[[关闭]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432798}[定时器超时，其中]{style="font-family:宋体"}*[topology-id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[MAIN: Hostname timer expired.]{lang="EN-US"}]{#struct_0_x1051_20145_x954738560}

[[动态主机名刷新定时器超时]{style="font-family:宋体"}]{#struct_0_x1051_20145_186029954}

[[MAIN: Stopped hostname timer.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432795}

[[关闭动态主机名刷新定时器]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1358023087}

[[MAIN: Started waiting timer for exceeded max sequence number, timer value is *Millisecond* ms.]{lang="EN-US"}]{#struct_0_x1051_20145_315404180}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_544581620}[序列号反转等待定时器启动，其中]{style="font-family:宋体"}*[Millisecond]{lang="EN-US"}*[表示定时器的当前时间间隔]{style="font-family:宋体"}

[[UPDT: Level-1 CSNP timer expired on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432796}

[[Level-1 CSNP]{lang="EN-US"}]{#struct_0_x1051_20145_208060854}[报文发送定时器超时，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: Level-1 PSNP timer expired on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1071593889}

[[Level-1 PSNP]{lang="EN-US"}]{#struct_0_x1051_20145_2072209347}[报文发送定时器超时，其中]{style="font-family:宋体"}[circuitName]{lang="EN-US"}[表示端口名]{style="font-family:宋体"}

[[UPDT: Level-1 P2P retransmit timer expired on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432801}

[[Level-1 P2P]{lang="EN-US"}]{#struct_0_x1051_20145_966985916}[重传定时器超时，其中]{style="font-family:宋体"}[circuitName]{lang="EN-US"}[表示端口名]{style="font-family:宋体"}

[[UPDT: Level-1 flood timer expired on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_406471204}

[[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1051_20145_304949352}[报文发送定时器超时，其中]{style="font-family:宋体"}[circuitName]{lang="EN-US"}[表示端口名]{style="font-family:宋体"}

[[UPDT: Level-1 fast flood timer expired.]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432802}

[[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1761897439}[快速扩散定时器超时，其中]{style="font-family:宋体"}*[circuitName]{lang="EN-US"}*[表示端口名]{style="font-family:宋体"}

[[UPDT: LSP *lsp-id* generate timer expired.]{lang="EN-US"}]{#struct_0_x1051_20145_x1350090812}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432799}[生成定时器超时，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}

[[UPDT: Started Level-1 LSP *lsp-id* generate timer, timer value is *Millisecond* ms.]{lang="EN-US"}]{#struct_0_x1051_20145_611345381}

[[启动]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1051_20145_460491084}[生成时间间隔定时器，其中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1968435815}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[-]{lang="EN-US"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Millisecond]{lang="EN-US"}*]{#struct_0_x1051_20145_x1672432800}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[生成定时器的当前时间间隔]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Stopped level-1 LSP *lsp-id* generate timer.]{lang="EN-US"}]{#struct_0_x1051_20145_x599098025}

[[关闭]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1051_20145_329810026}[生成时间间隔定时器，其中]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x109031406}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x902470375}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[定时器调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm timer]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432805}

[\*Sep 17 13:35:52:192 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[UPDT: Level-1 P2P retransmit timer expired on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 17 13:35:52:440 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[ADJ: P2P hello timer expired on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 17 13:35:54:612 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[UPDT: Level-1 PSNP timer expired on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 17 13:46:14:240 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[UPDT: Started Level-1 LSP 0011.2200.0001.00-00 generate timer, timer value is 2000 ms.]{lang="EN-US"}

[\*Sep 17 13:46:16:242 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[UPDT: LSP 0011.2200.0001.00-00 generate timer expired.]{lang="EN-US"}

[\*Sep 17 13:46:16:242 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) Started SPF timer, timer value is 450 ms.]{lang="EN-US"}

[\*Sep 17 13:46:16:694 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;]{lang="EN-US"}

[DEC: (MT0) SPF timer expired.]{lang="EN-US"}

::: {#-1335147762 .myid}
[]{#_Toc404798008}[]{#struct_0_x1051_20145_x1358612912}

**SPBM \-- SPBM调试命令 \-- debugging spbm update-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1885025029}

[**[debugging]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1051_20145_284475003}**[spbm]{lang="EN-US"}**[ ]{lang="EN-US"}**[update-packet]{lang="EN-US"}**[ \[]{lang="EN-US"}**[ receive ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ send ]{lang="EN-US"}**[\] \[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ ]{lang="EN-US"}[\]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1051_20145_x1672432806}**[debugging]{lang="EN-US"}**[ ]{lang="EN-US"}**[spbm]{lang="EN-US"}**[ ]{lang="EN-US"}**[update-packet ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ receive ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ send ]{lang="EN-US"}**[\] \[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ ]{lang="EN-US"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_207471029}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_63776862}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x103686143}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x896673058}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_714786969}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x2096872254}

[**[receive]{lang="EN-US"}**]{#struct_0_x1051_20145_x1037127696}[：表示接收]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1051_20145_x863128733}[：表示发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1051_20145_2132966376}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_2088443412}

[**[debugging spbm ]{lang="EN-US"}**]{#struct_0_x1051_20145_x92145957}**[update-packet]{lang="EN-US"}**[命令用来打开]{style="font-family:宋体"}[SPBM LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm ]{lang="EN-US"}[update-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM LSP]{lang="EN-US"}]{#struct_0_x1051_20145_216013520}[报文的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-19 ]{lang="EN-US"}[debugging spbm update-packet]{lang="EN-US"}]{#struct_0_x1051_20145_x1226011151}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1970069333}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_148066528}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x863128734}

[[UPDT: LSP with more than three area addresses.]{lang="EN-US"}]{#struct_0_x1051_20145_2133162984}

[[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1391070857}[报文中携带的区域地址个数多于]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}

[[UPDT: Parsed dynamic host name *HostName*.]{lang="EN-US"}]{#struct_0_x1051_20145_1754949207}

[[解析动态主机名]{style="font-family:宋体"}]{#struct_0_x1051_20145_1623217190}

[[UPDT: Updated dynamic host name advertised by *system-id*.]{lang="EN-US"}]{#struct_0_x1051_20145_x863128731}

[[更新由]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_2132835304}[宣告的动态主机名]{style="font-family:宋体"}

[[UPDT: (MT*topology-id*) *updatedType* SPF link(*source-id-\>dest-id*).]{lang="EN-US"}]{#struct_0_x1051_20145_x1801076597}

[[向路由计算模块更新]{style="font-family:宋体"}[SPF Link]{lang="EN-US"}]{#struct_0_x1051_20145_310684355}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_410756448}[：发布默认路由的]{lang="EN-US" style="font-family:
  宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updateType]{lang="EN-US"}*]{#struct_0_x1051_20145_x863128732}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[修改]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_x1051_20145_2133031912}[：源]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x985885696}[：目的]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[UPDT: (MT*topology-id*) *updatedType* SPF node(*nodesource-id*).]{lang="EN-US"}]{#struct_0_x1051_20145_1242991740}

[[向路由计算模块更新]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1051_20145_x614156466}[节点，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topology-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x863128737}[：]{lang="EN-US" style="font-family:
  宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updateType]{lang="EN-US"}*]{#struct_0_x1051_20145_2133228520}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[修改）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node]{lang="EN-US"}*]{#struct_0_x1051_20145_104770862}*[s]{lang="EN-US"}[ource]{lang="EN-US"}[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[UPDT: *PDUName system-id.pseudonodeNumber-LSPNumber* would be flooded on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x316676017}

[[扩散]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x863128738}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDUName]{lang="EN-US"}*]{#struct_0_x1051_20145_2133425128}[：]{lang="EN-US" style="font-family:宋体"}[L1 LSP/L2 LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1776172519}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_862067946}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x863128735}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_2133097448}[：扩散端口名]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Sent *PDUName* *system-id*.*pseudonodeNumber-LSPNumber* sequence number= *LSPSequenceNumber* holdtime= *holdTime* from snpa *mac-address* on circuit *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1831949619}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x87641245}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDUName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1151865928}[：]{lang="EN-US" style="font-family:宋体"}[L1 LSP/L2 LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_1967359581}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641246}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x1151865925}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPSequenceNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_1920305414}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文的序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[holdTime]{lang="EN-US"}*]{#struct_0_x1051_20145_x903227853}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的存活时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[snpa]{lang="EN-US"}]{#struct_0_x1051_20145_x87641243}[：子网接入点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mac-address]{lang="EN-US"}*]{#struct_0_x1051_20145_x1151865930}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文发送端口的]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1971311819}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文发送端口名]{lang="EN-US" style="font-family:
  宋体"}

[[UPDT: Received *pdutype* could not pass authentication, LSP-ID= *lsp-id*, LSP has been ignored.]{lang="EN-US"}]{#struct_0_x1051_20145_x87641244}

[[无法通过认证，]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_x1151865927}[报文被丢弃，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pdutype]{lang="EN-US"}*]{#struct_0_x1051_20145_x1211862468}[：报文类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp]{lang="EN-US"}*]{#struct_0_x1051_20145_x651738716}*[-i]{lang="EN-US"}[d]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[-]{lang="EN-US"}[ID]{lang="EN-US"}

[[UPDT: Local LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is newer than LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_x87641249}

[[处理比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_x1151865924}[中新的本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x87641254}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_1186786233}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x164863926}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Other LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is newer than LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956381}

[[处理比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_471032183}[中新的非本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_149781350}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x2043956382}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_874316710}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[UPDT: LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is older than LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_484382326}

[[处理比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956379}[中旧的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x2043956384}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_67747656}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_3965487}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[UPDT: LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is the same as LSDB copy.]{lang="EN-US"}]{#struct_0_x1051_20145_x2043956389}

[[处理和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_114801823}[中新旧一样的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_294695780}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_1977347845}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_294695775}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Own LSP *system-id*.*pseudonodeNumber*-*LSPNumber* processed does not exist in LSDB.]{lang="EN-US"}]{#struct_0_x1051_20145_x1597575424}

[[处理]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_294695774}[中不存在的本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x1661619361}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x1661619362}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_1417762493}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Other LSP *system-id*.*pseudonodeNumber*-*LSPNumber* processed does not exist in LSDB.]{lang="EN-US"}]{#struct_0_x1051_20145_137304967}

[[处理]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1051_20145_x1661619359}[中不存在的非本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1051_20145_x852315295}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_586066730}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LSPNumber]{lang="EN-US"}*]{#struct_0_x1051_20145_x1323142197}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[UPDT: Fast flooded level-1 *number* LSPs on interface *circuitName*.]{lang="EN-US"}]{#struct_0_x1051_20145_x852315296}

[[端口上快速泛洪的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1051_20145_586132266}[报文个数，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[number]{lang="EN-US"}*]{#struct_0_x1051_20145_666315815}[：报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_x1051_20145_x852315301}[：端口名]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1369986271}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_2032513087}[打开]{style="font-family:宋体"}[SPBM Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm update-packet]{lang="EN-US"}]{#struct_0_x1051_20145_x824214192}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_222768705}[端口下使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，]{style="font-family:宋体"}[输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1051_20145_x852315302}

[\[Sysname\] interface gigabitethernet 0/1/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet0/1/3\] spbm enable]{lang="EN-US"}

[\*Sep 18 15:36:07:918 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: L1 LSP 0011.2200.0001.00-00 would be flooded on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:918 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: L1 LSP 0011.2200.0001.00-01 would be flooded on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:919 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: L1 LSP 0011.2200.0a01.00-00 would be flooded on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:919 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: L1 LSP 0011.2200.0a01.00-01 would be flooded on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:957 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 LSP 0011.2200.0001.00-00 sequence number= 0x00000012 holdtime= 992 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:958 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 LSP 0011.2200.0001.00-01 sequence number= 0x00000018 holdtime= 1175 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:958 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 LSP 0011.2200.0a01.00-00 sequence number= 0x00000012 holdtime= 829 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:07:959 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 LSP 0011.2200.0a01.00-01 sequence number= 0x00000015 holdtime= 530 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:09:927 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: L1 LSP 0011.2200.0001.00-01 would be flooded on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

[\*Sep 18 15:36:09:957 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;]{lang="EN-US"}

[UPDT: Sent L1 LSP 0011.2200.0001.01 sequence number= 0x00000019 holdtime= 1199 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.]{lang="EN-US"}

::: {#82953226 .myid}
[]{#_Toc404798009}[]{#struct_0_x1051_20145_x1369920735}

**SPBM \-- SPBM调试命令 \-- debugging spbm-fdb bvlan-info**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1486336867}

[**[debugging spbm-fdb bvlan-info]{lang="EN-US"}**[ { **all** \| **driver** \| **message** }]{lang="EN-US"}]{#struct_0_x1051_20145_x2141560631}

[**[undo debugging spbm-fdb bvlan-info]{lang="EN-US"}**[ { **all** \| **driver** \| **message** }]{lang="EN-US"}]{#struct_0_x1051_20145_x1598411978}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_110903058}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1674107934}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x384275221}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1728083123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x1909263924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1173457594}

[**[all]{lang="EN-US"}**]{#struct_0_x1051_20145_1486336866}[：表示]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[相关的所有调试信息开关。]{style="font-family:宋体"}

[**[driver]{lang="EN-US"}**]{#struct_0_x1051_20145_x2141626167}[：表示]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[下发驱动调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_x1051_20145_1836655131}[：表示接收]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x943075889}

[**[debugging spbm-fdb bvlan-info]{lang="EN-US"}**]{#struct_0_x1051_20145_x899501423}[命令用来打开]{style="font-family:
宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm-fdb bvlan-info]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x1795116695}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-20 ]{lang="EN-US"}[debugging spbm-fdb bvlan-info message]{lang="EN-US"}]{#struct_0_x1051_20145_x527020087}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1979091570}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_1486336869}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x2140643127}

[[B-VLANChange VLANBitMap:]{lang="EN-US"}]{#struct_0_x1051_20145_x577756154}

[[BitMap(      0- 127): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2139046330}

[[BitMap(  128- 255): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x715995266}

[[BitMap(  256- 383): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1430204624}

[[BitMap(  384- 511): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336868}

[[BitMap(  512- 639): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2140708663}

[[BitMap(  640- 767): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x1402981971}

[[BitMap(  768- 895): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x1575206735}

[[BitMap(  896-1023): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336863}

[[BitMap(1024-1151): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2141298487}

[[BitMap(1152-1279): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x694311053}

[[BitMap(1280-1407): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_689090883}

[[BitMap(1408-1535): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1925748468}

[[BitMap(1536-1663): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336862}

[[BitMap(1664-1791): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2141364023}

[[BitMap(1792-1919): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x958000014}

[[BitMap(1920-2047): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1881207204}

[[BitMap(2048-2175): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336865}

[[BitMap(2176-2303): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2141429559}

[[BitMap(2304-2431): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_261468197}

[[BitMap(2432-2559): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x1074166705}

[[BitMap(2560-2687): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_169962032}

[[BitMap(2688-2815): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336864}

[[BitMap(2816-2943): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2141495095}

[[BitMap(2944-3071): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_685293121}

[[BitMap(3072-3199): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336859}

[[BitMap(3200-3327): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2140643128}

[[BitMap(3328-3455): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x530701987}

[[BitMap(3456-3583): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x1938985438}

[[BitMap(3584-3711): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_1486336858}

[[BitMap(3712-3839): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x2140708664}

[[BitMap(3840-3967): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x999697444}

[[BitMap(3968-4095): *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x822306042}

[[消息中携带的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1051_20145_x85478557}[位图内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[debugging spbm-fdb bvlan-info driver]{lang="EN-US"}]{#struct_0_x1051_20145_x705844316}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1976064040}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_497140818}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1710523480}

[[Before flush(CMD: SPBM ACTION, PARAM: [*operation*]{.TableTextChar})]{lang="EN-US"}]{#struct_0_x1051_20145_1486414430}

[[Driver Information: B-VLAN(*bvlan-number*)]{lang="EN-US"}]{#struct_0_x1051_20145_x85478558}

[[下驱动之前，下驱动命令字、参数以及]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_x1051_20145_x705844307}[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，参数]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x85478559}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x2041793694}[：删除]{lang="EN-US" style="font-family:宋体"}

[[After flush(CMD: SPBM ACTION, PARAM: [*operation*]{.TableTextChar}) result [*value*]{.TableTextChar}]{lang="EN-US"}]{#struct_0_x1051_20145_x439469519}

[[ Driver Information: B-VLAN(*bvlan-number*)]{lang="EN-US"}]{#struct_0_x1051_20145_1198854863}

[[下驱动之后，下驱动命令字、参数、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_x1051_20145_x245552617}[以及结果，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，参数]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[[的取值以及含义如下：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x2041793695}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_296858466}[：删除]{lang="EN-US" style="font-family:宋体"}

[[返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x1051_20145_1493703132}[的含义为下驱动的结果]{style="font-family:宋体"}

[[Refresh B-VLAN, result is 0x0, B-VLAN list is:]{lang="EN-US"}]{#struct_0_x1051_20145_296858469}

[[BitMap(2048-2175):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_1493703121}

[[BitMap(2176-2303):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_2143615613}

[[BitMap(2304-2431):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_511236551}

[[BitMap(2432-2559):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_296858468}

[[BitMap(2560-2687):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_1493703122}

[[BitMap(2688-2815):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_2143550077}

[[BitMap(2816-2943):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_x283297927}

[[BitMap(2944-3071):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_296858463}

[[BitMap(3072-3199):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_1493703127}

[[BitMap(3200-3327):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_2143222397}

[[BitMap(3328-3455):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_147344870}

[[BitMap(3456-3583):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_296858462}

[[BitMap(3584-3711):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_1493703128}

[[BitMap(3712-3839):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_2144205437}

[[BitMap(3840-3967):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_383834433}

[[BitMap(3968-4095):00000000 00000000 00000000 00000000]{lang="EN-US"}]{#struct_0_x1051_20145_296858465}

[[下驱动的消息中携带的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1051_20145_1493703133}[位图内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_2143484542}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_109864297}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[消息调试信息开关，当]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[收到]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[下发的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[变化消息会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm-fdb bvlan-info message]{lang="EN-US"}]{#struct_0_x1051_20145_x1182372050}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_1676989767}[下发添加]{style="font-family:宋体"}[VLAN ID 1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\*Sep 13 14:34:08:191 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN: -MDC=1;]{lang="EN-US"}]{#struct_0_x1051_20145_296858459}

[B-VLANChange VlanBitMap:]{lang="EN-US"}

[BitMap(   0- 127):feffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 128- 255):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 256- 383):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 384- 511):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 512- 639):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 640- 767):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 768- 895):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap( 896-1023):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1024-1151):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1152-1279):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1280-1407):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1408-1535):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1536-1663):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1664-1791):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1792-1919):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(1920-2047):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[\*Sep 13 14:34:08:191 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN: -MDC=1;]{lang="EN-US"}

[B-VLANChange VlanBitMap:]{lang="EN-US"}

[BitMap(2048-2175):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2176-2303):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2304-2431):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2432-2559):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2560-2687):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2688-2815):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2816-2943):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(2944-3071):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3072-3199):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3200-3327):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3328-3455):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3456-3583):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3584-3711):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3712-3839):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3840-3967):ffffffff ffffffff ffffffff ffffffff]{lang="EN-US"}

[BitMap(3968-4095):ffffffff ffffffff ffffffff ffffff7f]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x80274991}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[驱动调试信息开关，当]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[收到]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[下发的]{style="font-family:宋体"}[bvlan-info]{lang="EN-US"}[变化消息会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm-fdb bvlan-info driver]{lang="EN-US"}]{#struct_0_x1051_20145_x188282119}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_64576273}[下发删除]{style="font-family:宋体"}[VLAN ID 4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\*Sep 13 15:03:51:127 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN DRV: -MDC=1;]{lang="EN-US"}]{#struct_0_x1051_20145_1021633580}

[Before flush(CMD: SPBM ACTION, PARAM: Disable)]{lang="EN-US"}

[Driver Information: B-VLAN(4094)]{lang="EN-US"}

[\*Sep 13 15:03:51:127 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN DRV: -MDC=1;]{lang="EN-US"}

[After flush(CMD: SPBM ACTION, PARAM: Disable) result 0x0]{lang="EN-US"}

[Driver Information: B-VLAN(4094)]{lang="EN-US"}

::: {#-385529714 .myid}
[]{#_Toc404798010}[]{#struct_0_x1051_20145_738234743}

**SPBM \-- SPBM调试命令 \-- debugging spbm-fdb multicast-fib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_296858458}

[**[debugging spbm-fdb multicast-fib]{lang="EN-US"}**[ { **all** \| **driver** \| **message** }]{lang="EN-US"}]{#struct_0_x1051_20145_x80274990}

[**[undo debugging spbm-fdb multicast-fib]{lang="EN-US"}**[ { **all** \| **driver** \| **message** }]{lang="EN-US"}]{#struct_0_x1051_20145_x188282120}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_63986448}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x433710479}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_2004673205}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_1158652688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x938787935}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1659456669}

[**[all]{lang="EN-US"}**]{#struct_0_x1051_20145_x1702352077}[：表示组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[driver]{lang="EN-US"}**]{#struct_0_x1051_20145_x1710431966}[：表示组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[表项下发驱动调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_x1051_20145_x707127320}[：表示接收]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[添加、删除、出端口添加和删除消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1570262705}

[**[debugging spbm-fdb multicast-fib]{lang="EN-US"}**]{#struct_0_x1051_20145_1783504510}[命令用来打开组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging spbm-fdb multicast-fib]{lang="EN-US"}**[命令用来关闭组播]{style="font-family:
宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x1120777927}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-22 ]{lang="EN-US"}[debugging spbm-fdb multicast-fib message]{lang="EN-US"}]{#struct_0_x1051_20145_856335551}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1946836690}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1659456670}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_670366454}

[[Received the message for [*operation*]{.TableTextChar} multicast MAC entry, length= *length-value.*]{lang="EN-US"}]{#struct_0_x1051_20145_603838374}

[[具体某一个组播表项消息的头部，包括操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_1482714002}[和消息长度]{style="font-family:宋体"}*[length-value]{lang="EN-US"}*[（不包括本消息头），]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[refreshing]{lang="EN-US"}]{#struct_0_x1051_20145_x1659456671}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_x850152606}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Received the message for[ *operation*]{.TableTextChar} multicast MAC iflist, length= *length-value*.]{lang="EN-US"}]{#struct_0_x1051_20145_x1622406960}

[[具体某一个组播出端口消息的头部，包括操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x850152603}[和消息长度]{style="font-family:宋体"}*[length-value]{lang="EN-US"}*[（不包括本消息头），]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[adding]{lang="EN-US"}]{#struct_0_x1051_20145_x850152608}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_1488499557}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*) OutIFNum(*number*) RouteFlag(*flag-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x1537456468}

[[                         MulticastMACContext(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x2064160662}

[[具体某一个组播表项消息的内容，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x261026720}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，出端口数目为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[，表项中保存的驱动上下文为]{style="font-family:宋体"}*[context-value]{lang="EN-US"}*[，]{style="font-family:宋体"}

[[Port List:]{lang="EN-US"}]{#struct_0_x1051_20145_1488499556}

[[Port(*PortName*) OutIFContext(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x1537522004}

[[出端口列表，]{style="font-family:宋体"}[Port]{lang="EN-US"}]{#struct_0_x1051_20145_1456441139}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，出端口驱动上下文]{style="font-family:宋体"}

[[Started to smooth.]{lang="EN-US"}]{#struct_0_x1051_20145_329560051}

[[开始平滑]{style="font-family:宋体"}]{#struct_0_x1051_20145_1488499551}

[[Ended to smooth.]{lang="EN-US"}]{#struct_0_x1051_20145_x1537849684}

[[结束平滑]{style="font-family:宋体"}]{#struct_0_x1051_20145_x1976970653}

[[Received multicast MAC resource recovery message.]{lang="EN-US"}]{#struct_0_x1051_20145_1093879393}

[[驱动资源恢复时通知组播重新下驱动信息]{style="font-family:宋体"}]{#struct_0_x1051_20145_1488499550}

[[Port(*PortName*) Operation([*operation*]{.TableTextChar}).]{lang="EN-US"}]{#struct_0_x1051_20145_x1537915220}

[[端口是否使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_1161552772}[，]{style="font-family:宋体"}[Port]{lang="EN-US"}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x91966621}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x91966626}[：使能]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[debugging spbm-fdb multicast-fib driver]{lang="EN-US"}]{#struct_0_x1051_20145_x91966623}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1950541824}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_478592018}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_344219933}

[[Before flush(Operation: *[operation]{.TableTextChar}*)]{lang="EN-US"}]{#struct_0_x1051_20145_365057195}

[[下驱动之前，操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x2141935525}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AddEntry]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281755}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DeleteEntry]{lang="EN-US"}]{#struct_0_x1051_20145_x2048281760}[：删除]{lang="EN-US" style="font-family:宋体"}

[[After flush(Operation: *[operation]{.TableTextChar}*) result *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x1079058708}

[[下驱动之后，操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x387531427}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[AddEntry]{lang="EN-US"}]{#struct_0_x1051_20145_290370405}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DeleteEntry]{lang="EN-US"}]{#struct_0_x1051_20145_290370395}[：删除]{lang="EN-US" style="font-family:宋体"}

[[返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x1051_20145_x1506762062}[的含义为下驱动的结果]{style="font-family:宋体"}

[[Before flush(Operation: [*operation*]{.TableTextChar} Port: *PortName*)]{lang="EN-US"}]{#struct_0_x1051_20145_512982576}

[[下驱动之前，端口下的操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x1168653407}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944732}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x1665944742}[：使能]{lang="EN-US" style="font-family:宋体"}

[[After flush(Operation: [*operation*]{.TableTextChar} Port: *PortName*)  result *value*]{lang="EN-US"}]{#struct_0_x1051_20145_926941814}

[[下驱动之后，端口下的操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x2045588460}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x856640673}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_1482011491}[：使能]{lang="EN-US" style="font-family:宋体"}

[[返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x1051_20145_x341644284}[的含义为下驱动的结果]{style="font-family:宋体"}

[[Old Driver Information:]{lang="EN-US"}]{#struct_0_x1051_20145_1681473324}

[[MAC(*macaddr-value*) B-VLAN(*bvlan-number*) OutIFNum(*number*) RouteFlag(*flag-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_1985020500}

[[Driver Context(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_1482011490}

[[下驱动前信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x341709820}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，出端口数目为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[context-value]{lang="EN-US"}*

[[Port List:]{lang="EN-US"}]{#struct_0_x1051_20145_877144806}

[[Port(*PortName*) OutIFContext(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x310466223}

[[出端口列表，]{style="font-family:宋体"}[Port]{lang="EN-US"}]{#struct_0_x1051_20145_1482011493}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，出端口驱动上下文]{style="font-family:宋体"}

[[Added Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.]{lang="EN-US"}]{#struct_0_x1051_20145_x341513212}

[[资源不足重刷节点组播添加操作的信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_1482011488}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*

[[Deleted Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.]{lang="EN-US"}]{#struct_0_x1051_20145_1482011483}

[[资源不足重刷节点组播删除操作的信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x89803932}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x213185584}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x326750237}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关，当]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[收到]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[下发的组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[出端口添加消息会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm-fdb multicast-fib all]{lang="EN-US"}]{#struct_0_x1051_20145_x89803937}

[\*Sep 13 11:09:14:213 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;]{lang="EN-US"}

[Received the message for adding multicast MAC iflist, length= 40.]{lang="EN-US"}

[Multicast MAC: MAC(0362-3600-0100) B-VLAN(1) OutIFNum(1) RouteFlag(TE)]{lang="EN-US"}

[               MulticastMACContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 11:09:14:213 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;]{lang="EN-US"}

[Port List:]{lang="EN-US"}

[Port(GE0/1/3) OutIFContext(0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;]{lang="EN-US"}

[Before flush(Operation: AddEntry)]{lang="EN-US"}

[\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;]{lang="EN-US"}

[Driver Information:]{lang="EN-US"}

[MAC(0362-3600-0100) B-VLAN(1) OutIFNum(1) RouteFlag(TE)]{lang="EN-US"}

[DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;]{lang="EN-US"}

[Port List:]{lang="EN-US"}

[Port(GE0/1/3) OutIFContext(0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;]{lang="EN-US"}

[After flush(Operation:AddEntry) result 0x40010001]{lang="EN-US"}

[\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;]{lang="EN-US"}

[Driver Information:]{lang="EN-US"}

[MAC(0362-3600-0100) B-VLAN(1) OutIFNum(1) RouteFlag(TE)]{lang="EN-US"}

[DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;]{lang="EN-US"}

[Port List:]{lang="EN-US"}

[Port(GE0/1/3) OutIFContext(0xffffffff,0xffffffff)]{lang="EN-US"}

::: {#191140537 .myid}
[]{#_Toc404798011}[]{#struct_0_x1051_20145_x89803938}

**SPBM \-- SPBM调试命令 \-- debugging spbm-fdb unicast-fib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x213185594}

[**[debugging spbm-fdb unicast-fib]{lang="EN-US"}**[ { **all** \| **driver** \| **message** }]{lang="EN-US"}]{#struct_0_x1051_20145_x326750236}

[**[undo debugging spbm-fdb unicast-fib]{lang="EN-US"}**[ { **all** \| **driver** \| **message** }]{lang="EN-US"}]{#struct_0_x1051_20145_7799166}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1765002911}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1051_20145_x2007575750}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1791763098}

[[network-admin]{lang="EN-US"}]{#struct_0_x1051_20145_264331687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1051_20145_x89803935}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x213185591}

[**[all]{lang="EN-US"}**]{#struct_0_x1051_20145_x327077916}[：表示单播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[driver]{lang="EN-US"}**]{#struct_0_x1051_20145_1162185688}[：表示单播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[表项下发驱动调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_x1051_20145_x974021972}[：表示接收]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[添加和删除消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1182364419}

[**[debugging spbm-fdb unicast-fib]{lang="EN-US"}**]{#struct_0_x1051_20145_1326155329}[命令用来打开单播]{style="font-family:
宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关。]{style="font-family:
宋体"}**[undo ]{lang="EN-US"}[debugging spbm-fdb unicast-fib]{lang="EN-US"}**[命令用来关闭单播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，单播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}]{#struct_0_x1051_20145_x1545939474}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x1051_20145_x89803936}[[表1-24 ]{lang="EN-US"}[debugging spbm-fdb unicast-fib message]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1962697309}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_x213185588}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x326488093}

[[Received the message for [*operation*]{.TableTextChar} unicast MAC entry, length= *length-value.*]{lang="EN-US"}]{#struct_0_x1051_20145_x37837257}

[[具体某一个单播表项消息的头部，包括操作类型和消息长度（不包括本消息头），]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x598742181}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[refreshing]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119068}[：刷新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleting]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119077}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan- number*) Port(*PortName*) RouteFlag(*flag-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x1230731639}

[[                       UnicastMACContext(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x131482921}

[[具体某一个单播表项消息的内容，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x2046119078}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[Port]{lang="EN-US"}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[，表项中保存的驱动上下文为]{style="font-family:宋体"}*[context-value]{lang="EN-US"}*

[[Started to smooth.]{lang="EN-US"}]{#struct_0_x1051_20145_x114986392}

[[开始平滑]{style="font-family:宋体"}]{#struct_0_x1051_20145_x109003711}

[[Ended to smooth.]{lang="EN-US"}]{#struct_0_x1051_20145_275348450}

[[结束平滑]{style="font-family:宋体"}]{#struct_0_x1051_20145_292533091}

[[Received unicast MAC resource recovery message.]{lang="EN-US"}]{#struct_0_x1051_20145_1209738939}

[[驱动资源恢复时通知单播重新下驱动]{style="font-family:宋体"}]{#struct_0_x1051_20145_1046005860}

[[Port(*PortName*) Operation([*operation*]{.TableTextChar}]{lang="EN-US"}]{#struct_0_x1051_20145_x1432820213}[）]{style="font-family:宋体"}[.]{lang="EN-US"}

[[端口是否使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_x1051_20145_x816951916}[，]{style="font-family:宋体"}[Port]{lang="EN-US"}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_292533089}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782046}[：使能]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[debugging spbm-fdb unicast-fib driver]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782043}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1931852786}[[字段]{style="font-family:黑体"}]{#struct_0_x1051_20145_1355242728}

[[描述]{style="font-family:黑体"}]{#struct_0_x1051_20145_x1185399781}

[[Before flush(Operation: *[operation]{.TableTextChar}*)]{lang="EN-US"}]{#struct_0_x1051_20145_922587412}

[[下驱动之前，操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x25526266}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_x1051_20145_x1663782053}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_x854477980}[：删除]{lang="EN-US" style="font-family:宋体"}

[[After flush(Operation: *[operation]{.TableTextChar}*) result *value*]{lang="EN-US"}]{#struct_0_x1051_20145_107332180}

[[下驱动之后，操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_x854477985}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_x1051_20145_x854477990}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1051_20145_1484174174}[：删除]{lang="EN-US" style="font-family:宋体"}

[[返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x1051_20145_x1664267838}[的含义为下驱动的结果]{style="font-family:宋体"}

[[Before flush(Operation: [*operation*]{.TableTextChar} Port: *PortName*)]{lang="EN-US"}]{#struct_0_x1051_20145_x535704014}

[[下驱动之前，端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_x1051_20145_x1025372088}[下的操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x78990494}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x78990495}[：使能]{lang="EN-US" style="font-family:宋体"}

[[After flush(Operation: [*operation*]{.TableTextChar} Port: *PortName*) result *value*]{lang="EN-US"}]{#struct_0_x1051_20145_x78990496}

[[下驱动之后，端口下的操作类型]{style="font-family:宋体"}[*[operation]{lang="EN-US"}*]{.TableTextChar}]{#struct_0_x1051_20145_774379448}[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1051_20145_x2035305627}[：去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1051_20145_x2035305637}[：使能]{lang="EN-US" style="font-family:宋体"}

[[返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x1051_20145_39403685}[的含义为下驱动的结果]{style="font-family:宋体"}

[[Driver Information:]{lang="EN-US"}]{#struct_0_x1051_20145_426367150}

[[MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x2035305638}

[[DriverContext(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x7650482}

[[下发驱动时携带的信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x468804181}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[Port]{lang="EN-US"}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[context-value]{lang="EN-US"}*

[[Old Driver Information:]{lang="EN-US"}]{#struct_0_x1051_20145_92730428}

[[MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_303346531}

[[DriverContext(*context-value*)]{lang="EN-US"}]{#struct_0_x1051_20145_x1968650731}

[[下驱动前携带的信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_x434344610}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[Port]{lang="EN-US"}[为]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[RouteFlag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[context-value]{lang="EN-US"}*

[[Added Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.]{lang="EN-US"}]{#struct_0_x1051_20145_x1208348729}

[[资源不足重刷节点单播添加操作的信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_303346530}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*

[[Deleted Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.]{lang="EN-US"}]{#struct_0_x1051_20145_x1968650730}

[[资源不足重刷节点单播删除操作的信息，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1051_20145_1131739331}[为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[bvlan-number]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1051_20145_1014318330}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_303346533}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[单播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关，当]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[收到]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[下发的单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[刷新消息会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm-fdb unicast-fib all]{lang="EN-US"}]{#struct_0_x1051_20145_x1968650733}

[\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC: -MDC=1;]{lang="EN-US"}

[Received the message for refreshing unicast MAC entry, ength= 32.]{lang="EN-US"}

[Unicast MAC: MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)]{lang="EN-US"}

[             UnicastMACContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[Before flush(Operation: Add)]{lang="EN-US"}

[\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[Driver Information:]{lang="EN-US"}

[MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)]{lang="EN-US"}

[DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[After flush(Operation:Add) result 0x40010001]{lang="EN-US"}

[\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[Driver Information:]{lang="EN-US"}

[MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)]{lang="EN-US"}

[DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1051_20145_x1597144024}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[单播]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[调试信息开关，当]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}[收到]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[下发的单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[删除消息会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging spbm-fdb unicast-fib all]{lang="EN-US"}]{#struct_0_x1051_20145_303346532}

[\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC: -MDC=1;]{lang="EN-US"}

[Received the message for deleting unicast MAC entry, length= 32.]{lang="EN-US"}

[Unicast MAC: MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)]{lang="EN-US"}

[             UnicastMACContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[Before flush(Operation: Delete)]{lang="EN-US"}

[\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[Driver Information:]{lang="EN-US"}

[MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)]{lang="EN-US"}

[DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)]{lang="EN-US"}

[\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;]{lang="EN-US"}

[After flush(Operation:Delete) result 0x40010001]{lang="EN-US"}
