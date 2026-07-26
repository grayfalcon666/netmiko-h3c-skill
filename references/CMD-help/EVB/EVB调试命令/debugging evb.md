::: {#-1058522838 .myid}
[]{#_Toc404798095}[]{#struct_0_x1180_10099_x1370237617}

**EVB \-- EVB调试命令 \-- debugging evb**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1180_10099_1497085477}

[**[debugging evb]{lang="EN-US"}**[ { ]{lang="EN-US"}**[all]{lang="EN-US"}**[ \| **error**]{lang="EN-US"}**[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[event]{lang="EN-US"}**[ \| **packet** \[ **verbose** \] \[ **interface** *interface-type* ]{lang="EN-US"}[{ *interface-number* \| *interface-number*:]{lang="EN-US"}]{#struct_0_x1180_10099_x872368509}*[channel-id]{lang="PT-BR"}*[ } ]{lang="PT-BR"}[\] }]{lang="EN-US"}

[**[undo debugging evb]{lang="EN-US"}**[ { ]{lang="EN-US"}**[all]{lang="EN-US"}**[ \| **error**]{lang="EN-US"}**[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[event]{lang="EN-US"}**[ \| **packet** \[ **verbose** \] \[ **interface** *interface-type* ]{lang="EN-US"}[{ *interface-number* \| *interface-number*:]{lang="EN-US"}]{#struct_0_x1180_10099_1881038150}*[channel-id]{lang="PT-BR"}*[ }]{lang="PT-BR"}[\] }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1180_10099_x31505748}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1180_10099_927483468}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1180_10099_x1279318533}

[[network-admin]{lang="EN-US"}]{#struct_0_x1180_10099_x1761753700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1180_10099_1578103476}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1180_10099_x1513444985}

[**[all]{lang="EN-US"}**]{#struct_0_x1180_10099_x155695483}[：表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1180_10099_1285204940}[：表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1180_10099_1643203108}[：表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1180_10099_x31702356}[：表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[协议报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1180_10099_x714181658}[：表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[协议报文详细信息调试开关。若未指定本参数，表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[协议报文摘要信息调试开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type ]{lang="EN-US"}*]{#struct_0_x1180_10099_x1673699975}[{ ]{lang="PT-BR"}*[interface-number]{lang="EN-US"}*[ \| *interface-number*:*channel-id* }]{lang="PT-BR"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[二层以太网接口、]{style="font-family:宋体"}[二层聚合接口、]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口。]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type]{lang="PT-BR"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为接口编号，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号。]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[二层以太网接口和]{style="font-family:宋体"}[二层聚合接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[的形式；对于]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口和]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[:*channel-id*]{lang="PT-BR"}[的形式。如果未指定本参数，表示所有接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1180_10099_x1147214124}

[]{#OLE_LINK1}[**[debugging evb]{lang="EN-US"}**]{#struct_0_x1180_10099_328004523}[命令用来打开]{style="font-family:宋体"}[EVB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging evb]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EVB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x1180_10099_x2063550988}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging evb error]{lang="EN-US"}]{#struct_0_x1180_10099_638041253}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1037951619}[[字段]{style="font-family:黑体"}]{#struct_0_x1180_10099_2062118966}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1180_10099_x673734132}

[[The role value of received CDCP packet on phyport *IfName* is illegal.]{lang="EN-US"}]{#struct_0_x1180_10099_x31636820}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1949071124}[收到的远端]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文的角色值非法]{style="font-family:宋体"}

[[The channel capability value of received CDCP packet on phyport *IfName* is illegal.]{lang="EN-US"}]{#struct_0_x1180_10099_1750775923}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x411509338}[收到的远端]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文的能力值非法]{style="font-family:宋体"}

[[The SCID *SCID* SVID *SVID* in received CDCP packet is illegal.]{lang="EN-US"}]{#struct_0_x1180_10099_1223557818}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_107855523}[收到的远端]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[SCID]{lang="EN-US"}[和]{style="font-family:宋体"}[SVID]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[The first SCID/SVID info is not the default S-Channel.]{lang="EN-US"}]{#struct_0_x1180_10099_x31309140}

[[第一个]{style="font-family:宋体"}[SCID/SVID]{lang="EN-US"}]{#struct_0_x1180_10099_x529048290}[对不是默认的]{style="font-family:宋体"}[S]{lang="EN-US"}[通道]{style="font-family:宋体"}

[[The length of received CDCP packet on phyport *IfName* is less than 7 bytes.]{lang="EN-US"}]{#struct_0_x1180_10099_1609606468}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1610419415}[收到的]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文长度小于]{style="font-family:宋体"}[7]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[Phyport *IfName* found that EVB is disabled after analyzing a received CDCP packet.]{lang="EN-US"}]{#struct_0_x1180_10099_1485714654}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x31243604}[在解析收到的]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文后，发现]{style="font-family:宋体"}[EVB]{lang="EN-US"}[未使能]{style="font-family:宋体"}

[[EVB is disabled on phyport *IfName* that received a CDCP packet.]{lang="EN-US"}]{#struct_0_x1180_10099_1826929623}

[[接收]{style="font-family:宋体"}[CDCP]{lang="EN-US"}]{#struct_0_x1180_10099_403917866}[报文的接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[未使能]{style="font-family:宋体"}[EVB]{lang="EN-US"}

[[The port *IfName* that received a CDCP packet is not a L2-phyport.]{lang="EN-US"}]{#struct_0_x1180_10099_x1673419635}

[[接收]{style="font-family:宋体"}[CDCP]{lang="EN-US"}]{#struct_0_x1180_10099_2013603497}[报文的接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[不是二层物理接口]{style="font-family:宋体"}

[[The length of EVB TLV received on S-Channel port *IfName* is illegal.]{lang="EN-US"}]{#struct_0_x1180_10099_x31833431}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1784718505}[收到的]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[的长度非法]{style="font-family:宋体"}

[[The *IfName* of EVB TLV received on S-Channel port *IfName* is illegal.]{lang="EN-US"}]{#struct_0_x1180_10099_352309816}

[[接收]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1180_10099_2018693167}[的]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[The MODE value of EVB TLV received on S-Channel port *IfName* is illegal.]{lang="EN-US"}]{#struct_0_x1180_10099_587504407}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x31767895}[收到的]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[的模式非法]{style="font-family:宋体"}

[[Failed to negotiate according to EVB TLV packet received on S-Channel port *IfName*.]{lang="EN-US"}]{#struct_0_x1180_10099_1539274682}

[[根据]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1180_10099_x535084312}[通道接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[收到的]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[协商运行值失败]{style="font-family:宋体"}

[[Failed to send EVB message to LLDP.]{lang="EN-US"}]{#struct_0_x1180_10099_1289817923}

[[向]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1180_10099_x1458187203}[进程发送]{style="font-family:宋体"}[EVB]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[Invalid VDP packet on interface *IfName* with invalid filter format or instanceId format.]{lang="EN-US"}]{#struct_0_x1180_10099_x31964503}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x2101333843}[收到的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文中，过滤信息格式或实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[格式非法]{style="font-family:宋体"}

[[Process an invalid packet on interface *IfName* without filter info.]{lang="EN-US"}]{#struct_0_x1180_10099_x715303007}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1843295370}[处理没有过滤信息的非法报文]{style="font-family:宋体"}

[[VDP packet on interface *IfName*, length of filter information is inconsistent with filter format and number.]{lang="EN-US"}]{#struct_0_x1180_10099_x31898967}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x1732705478}[收到的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文中，过滤信息长度与过滤的格式与个数冲突]{style="font-family:宋体"}

[[Received a VDP packet on interface *IfName* with VLAN 0 in filter, but number of filters is not 1.]{lang="EN-US"}]{#struct_0_x1180_10099_1394879954}

[[接口]{style="font-family:宋体"}*[ifName]{lang="EN-US"}*]{#struct_0_x1180_10099_1218199093}[收到]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文中，过滤信息]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，但过滤信息的个数不为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[The new VDP request packet not consistent with the last one.]{lang="EN-US"}]{#struct_0_x1180_10099_x31571287}

[[新的]{style="font-family:宋体"}[VDP]{lang="EN-US"}]{#struct_0_x1180_10099_x971904631}[请求报文与上一次的冲突]{style="font-family:宋体"}

[[Received a packet on interface *IfName* with invalid VDP TLV type.]{lang="EN-US"}]{#struct_0_x1180_10099_x1370434225}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x2049925281}[接收的报文的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型非法]{style="font-family:宋体"}

[[Received a VDP packet on interface *IfName* with invalid length *length*.]{lang="EN-US"}]{#struct_0_x1180_10099_x31505751}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x1411168685}[接收的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文长度非法]{style="font-family:宋体"}

[[Failed to process de-association packet on interface *IfName*, because managerid is different from associate request.]{lang="EN-US"}]{#struct_0_x1180_10099_x224204443}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x1995821498}[处理去关联报文失败，因为管理地址与关联请求时不同]{style="font-family:宋体"}

[[Failed to process VDP packet on interface *IfName* for invlaid managerID TLV.]{lang="EN-US"}]{#struct_0_x1180_10099_x31702359}

[[处理接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x714181665}[收到的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文失败，管理地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[Received a VDP packet with invalid MAC in filter information.]{lang="EN-US"}]{#struct_0_x1180_10099_x1673372292}

[[接收的]{style="font-family:宋体"}[VDP]{lang="EN-US"}]{#struct_0_x1180_10099_x31636823}[报文，过滤信息中]{style="font-family:宋体"}[MAC]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[Received a VDP packet with invalid instance ID of MAC format.]{lang="EN-US"}]{#struct_0_x1180_10099_1949071127}

[[接收的]{style="font-family:宋体"}[VDP]{lang="EN-US"}]{#struct_0_x1180_10099_1750579315}[报文中]{style="font-family:宋体"}[MAC]{lang="EN-US"}[格式的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[No manager address to use.]{lang="EN-US"}]{#struct_0_x1180_10099_x31309143}

[[无管理地址可以使用]{style="font-family:宋体"}]{#struct_0_x1180_10099_x529048289}

[[Req/Ack bit is not 0 in VDP request packet on interface *IfName*.]{lang="EN-US"}]{#struct_0_x1180_10099_1609147715}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x1903656550}[接收的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[请求报文的请求]{style="font-family:宋体"}[/]{lang="EN-US"}[应答位不是]{style="font-family:宋体"}[0]{lang="EN-US"}

[[There are not enough resources to create S-Channel with SCID *SCID* on phyport *IfName*.]{lang="EN-US"}]{#struct_0_x1180_10099_x31243607}

[[在物理口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1826929624}[上没有足够资源创建]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口，其]{style="font-family:宋体"}[SCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[SCID]{lang="EN-US"}*

[[ ]{lang="EN-US"}]{#_Toc130718926}

[[表1-2 ]{lang="EN-US"}[debugging evb event]{lang="EN-US"}]{#struct_0_x1180_10099_404114474}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1029303811}[[字段]{style="font-family:黑体"}]{#struct_0_x1180_10099_x31833430}

[[描述]{style="font-family:黑体"}]{#struct_0_x1180_10099_1784718504}

[[The server port connected to phyport *IfName* that received a CDCP packet does not support s-component.]{lang="EN-US"}]{#struct_0_x1180_10099_352375352}

[[与收到]{style="font-family:宋体"}[CDCP]{lang="EN-US"}]{#struct_0_x1180_10099_2049804627}[报文的物理口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[相连的服务器的接口不支持]{style="font-family:宋体"}[S]{lang="EN-US"}[组件]{style="font-family:宋体"}

[[CDCP packet received on phyport *IfName* has only default S-Channel.]{lang="EN-US"}]{#struct_0_x1180_10099_x1632541725}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_877699825}[收到的]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文中只有缺省]{style="font-family:宋体"}[S]{lang="EN-US"}[通道]{style="font-family:宋体"}

[[CDCP packet received on phyport *IfName* has a remaining length less than the SCID/SVID pair.]{lang="EN-US"}]{#struct_0_x1180_10099_x31767894}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1539274683}[收到的]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文中剩余长度小于]{style="font-family:宋体"}[SCID/SVID]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Number of S-Channels supported by the remote end is less than that in the CDCP packet received on phyport *IfName*.]{lang="EN-US"}]{#struct_0_x1180_10099_x535149848}

[[远端支持的]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1180_10099_1701581384}[通道个数少于接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[收到的]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[报文中]{style="font-family:宋体"}[S]{lang="EN-US"}[通道个数]{style="font-family:宋体"}

[[The request url of online is: *string.*]{lang="EN-US"}]{#struct_0_x1180_10099_390174697}

[[向]{style="font-family:宋体"}[iMC]{lang="EN-US"}]{#struct_0_x1180_10099_2108490948}[发送的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[上线]{style="font-family:宋体"}[URL]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[The request url of offline is: *string.*]{lang="EN-US"}]{#struct_0_x1180_10099_x31964502}

[[向]{style="font-family:宋体"}[iMC]{lang="EN-US"}]{#struct_0_x1180_10099_x2101333842}[发送的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下线]{style="font-family:宋体"}[URL]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Received a de-association packet on interface *IfName* but the VSI does not exist.]{lang="EN-US"}]{#struct_0_x1180_10099_2013580348}

[[在接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x927467317}[上收到去关联报文，但]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口不存在]{style="font-family:宋体"}

[[Successfully get the managerid TLV on interface *IfName*.]{lang="EN-US"}]{#struct_0_x1180_10099_x113537860}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x31898966}[解析到合法的管理地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Received a VDP packet on interface *IfName* with type *type*.]{lang="EN-US"}]{#struct_0_x1180_10099_x1732705479}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x171203987}[收到]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received an ACK or invalid packet through by ECP on interface *IfName*.]{lang="EN-US"}]{#struct_0_x1180_10099_x653166992}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_2063808090}[通过]{style="font-family:宋体"}[ECP]{lang="EN-US"}[收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[或者非法报文]{style="font-family:宋体"}

[[Received a VDP packet with VLAN 0 in filter information.]{lang="EN-US"}]{#struct_0_x1180_10099_x31571286}

[[收到的]{style="font-family:宋体"}[VDP]{lang="EN-US"}]{#struct_0_x1180_10099_x971904632}[报文中，过滤信息中]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Create VSI by local server manager.]{lang="EN-US"}]{#struct_0_x1180_10099_x1370630833}

[[本地创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_x1774263373}

[[Delete VSI by local server manager.]{lang="EN-US"}]{#struct_0_x1180_10099_1033491485}

[[本地删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_x31505750}

[[Current VSI status is waiting; delete VSI for reason *reason*.]{lang="EN-US"}]{#struct_0_x1180_10099_x1411168684}

[[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_x1790288384}[当前状态为]{style="font-family:宋体"}[waiting]{lang="EN-US"}[，删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*

[[VSI *IfName* status changed into *Pre-Association/ Association.*]{lang="EN-US"}]{#struct_0_x1180_10099_x1344225239}

[[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_x31702358}[关联状态切换]{style="font-family:宋体"}

[[Current VSI status is pre-association; delete VSI for reason *reason.*]{lang="EN-US"}]{#struct_0_x1180_10099_x714181664}

[[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_x1673437828}[当前状态为预关联，删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*

[[VSI successfully sent a request to and received a response from iMC to get online.]{lang="EN-US"}]{#struct_0_x1180_10099_x286009136}

[[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_x31636822}[上线，向]{style="font-family:宋体"}[iMC]{lang="EN-US"}[发送请求并接收回应成功]{style="font-family:宋体"}

[[VSI successfully sent a request to and received a response from iMC to get offline.]{lang="EN-US"}]{#struct_0_x1180_10099_1949071126}

[[VSI]{lang="EN-US"}]{#struct_0_x1180_10099_1750644851}[下线，向]{style="font-family:宋体"}[iMC]{lang="EN-US"}[发送请求并接收回应成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging evb packet]{lang="EN-US"}]{#struct_0_x1180_10099_x12692897}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1025286275}[[字段]{style="font-family:黑体"}]{#struct_0_x1180_10099_932488848}

[[描述]{style="font-family:黑体"}]{#struct_0_x1180_10099_x31309142}

[*[PacketType]{lang="EN-US"}*[ packet received on interface *IfName* with length *length*]{lang="EN-US"}]{#struct_0_x1180_10099_x529048288}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_1609082179}[收到类型为]{style="font-family:宋体"}*[PacketType]{lang="EN-US"}*[、长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[*[PacketType]{lang="EN-US"}*]{#struct_0_x1180_10099_x63217926}[的取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CDCP]{lang="EN-US"}]{#struct_0_x1180_10099_x63217923}[：表示]{lang="EN-US" style="font-family:宋体"}[CDCP]{lang="EN-US"}[协议报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1180_10099_x63217924}[：表示]{lang="EN-US" style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[协议报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VDP]{lang="EN-US"}]{#struct_0_x1180_10099_x1662578104}[：表示]{lang="EN-US" style="font-family:宋体"}[VDP]{lang="EN-US"}[协议报文]{lang="EN-US" style="font-family:宋体"}

[*[PacketType]{lang="EN-US"}*[ packet sent on interface *IfName* with *length*]{lang="EN-US"}]{#struct_0_x1180_10099_1981102778}

[[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*]{#struct_0_x1180_10099_x804811232}[发送类型为]{style="font-family:宋体"}*[PacketType]{lang="EN-US"}*[、长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[*[PacketType]{lang="EN-US"}*]{#struct_0_x1180_10099_1504272116}[的取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CDCP]{lang="EN-US"}]{#struct_0_x1180_10099_1504272119}[：表示]{lang="EN-US" style="font-family:宋体"}[CDCP]{lang="EN-US"}[协议报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1180_10099_1504272118}[：表示]{lang="EN-US" style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[协议报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VDP]{lang="EN-US"}]{#struct_0_x1180_10099_1504272121}[：表示]{lang="EN-US" style="font-family:宋体"}[VDP]{lang="EN-US"}[协议报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="PT-BR"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1180_10099_x1456380286}

[[\# ]{lang="PT-BR"}]{#struct_0_x1180_10099_1501107208}[打开]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging evb event]{lang="EN-US"}]{#struct_0_x1180_10099_x31243606}

[\*Mar  6 22:33:50:188 2012 ]{lang="PT-BR"}[Sysname]{lang="EN-US"}[ EVB/7/Event: -MDC=1; The request url of online is:http://\[1122:3344:5566:7788:9900:AABB:CCDD:EEFF\]:8080/evb/vdp/profile?vsi_inst=11:2233:4455:6677:8899:1234:5678:9010&vsi_type=100&vsi_ver=0&vlan_mac=1000_0022-3344-5566&schannel=S-Channel1/0/1/3:2&vsi_local_id=0&pre-associate=0.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1180_10099_1826929625}*[向]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器发送上线请求的]{style="font-family:宋体"}[URL]{lang="PT-BR"}[信息]{style="font-family:宋体"}*

[[\*Mar  6 22:33:50:187 2012 ]{lang="PT-BR"}[Sysname]{lang="EN-US"}]{#struct_0_x1180_10099_404048938}[ EVB/7/Event: -MDC=1; Received a VDP packet on interface ]{lang="PT-BR"}[S-Channe1]{lang="SV"}[/0]{lang="PT-BR"}[/1:10]{lang="SV"}[ with type 3.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1180_10099_x384087870}*[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1]{lang="PT-BR"}*[/0*/1:10*]{lang="PT-BR"}*[上收到类型为]{style="font-family:宋体"}[3]{lang="PT-BR"}[的]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x1180_10099_241869268}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[创建]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并打开]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[协议报文详细调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging evb packet verbose]{lang="EN-US"}]{#struct_0_x1180_10099_x453636184}

[Dec 19 05:31:38:033 2011 Sysname EVB/7/Packet: -MDC=1; VDP packet received on interface S-Channe1]{lang="SV"}[/0]{lang="PT-BR"}[/1:10 with length 57:]{lang="SV"}

[10 01 00 02 0a 10 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 04 21 04 00 00 64 00 02 00 11]{lang="SV"}

[22 33 44 55 66 77 88 99 12 34 56 78 90 10 02 00]{lang="SV"}

[01 00 11 22 33 44 55 03 e8]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_x1180_10099_x578537679}*[在]{style="font-family:宋体"}[S]{lang="SV"}[通道接口]{style="font-family:宋体"}[S-Channel1]{lang="PT-BR"}*[/0*/1:10*]{lang="PT-BR"}*[上]{style="font-family:宋体"}[收到长度为]{style="font-family:宋体"}[57]{lang="SV"}[的]{style="font-family:宋体"}[VDP]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Dec 19 05:31:38:048 2011 Sysname EVB/7/Packet: -MDC=1; VDP packet sent on interface S-Channe1]{lang="SV"}]{#struct_0_x1180_10099_x31833433}[/0]{lang="PT-BR"}[/1:10 with length 53:]{lang="SV"}

[0a 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 04 21 00 00 00 64 00 02 00 11 22 33 44 55]{lang="SV"}

[66 77 88 99 12 34 56 78 90 10 02 00 01 00 11 22]{lang="SV"}

[33 44 55 03 e8]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_x1180_10099_1784718507}*[通过]{style="font-family:宋体"}[S]{lang="SV"}[通道接口]{style="font-family:宋体"}[S-Channel1]{lang="PT-BR"}*[/0*/1:10*]{lang="PT-BR"}*[发送长度为]{style="font-family:宋体"}[53]{lang="SV"}[的]{style="font-family:宋体"}[VDP]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Dec 19 05:35:53:692 2011 Sysname EVB/7/Packet: -MDC=1; CDCP packet received on interface GigabitEthernet1/0/1 with length 25:]{lang="SV"}]{#struct_0_x1180_10099_352178744}

[98 00 00 a7 00 10 01 00 20 02 00 30 00 00 40 04]{lang="SV"}

[00 60 00 00 a0 0a 00 b0 00]{lang="SV"}

[\*Dec 19 05:38:20:119 2011 Sysname EVB/7/Packet: -MDC=1; CDCP packet sent on interface GigabitEthernet1/0/1 with length 19:]{lang="SV"}

[18 00 00 a7 00 10 01 00 20 02 00 30 03 00 a0 0a]{lang="SV"}

[00 b0 06]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_x1180_10099_241940201}*[本地物理端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上的信息变化时，向]{style="font-family:宋体"}[LLDP]{lang="SV"}[进程同步信息]{style="font-family:宋体"}*

[[\*Dec 19 05:39:02:788 2011 Sysname EVB/7/Packet: -MDC=1; EVB TLV packet received on interface S-Channe1]{lang="SV"}]{#struct_0_x1180_10099_1492520947}[/0]{lang="PT-BR"}[/1:10 with length 5:]{lang="SV"}

[00 07 b4 91 17]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_x1180_10099_x195143674}*[在]{style="font-family:宋体"}[S]{lang="SV"}[通道接口]{style="font-family:宋体"}[S-Channel1]{lang="PT-BR"}*[/0*/1:10*]{lang="PT-BR"}*[上]{style="font-family:宋体"}[收到长度为]{style="font-family:宋体"}[5]{lang="SV"}[的]{style="font-family:宋体"}[EVB TLV]{lang="SV"}*

[[\*Dec 19 05:45:33:257 2011 Sysname EVB/7/Packet: -MDC=1; EVB TLV packet sent on interface S-Channe1]{lang="SV"}]{#struct_0_x1180_10099_x31767897}[/0]{lang="PT-BR"}[/1:10 with length 5:]{lang="SV"}

[03 07 b4 54 14]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_x1180_10099_1539274680}*[通过]{style="font-family:宋体"}[S]{lang="SV"}[通道接口]{style="font-family:宋体"}[S-Channel1]{lang="PT-BR"}*[/0*/1:10*]{lang="PT-BR"}*[发送长度为]{style="font-family:宋体"}[5]{lang="SV"}[的]{style="font-family:宋体"}[EVB TLV]{lang="SV"}[给]{style="font-family:宋体"}[LLDP]{lang="SV"}*
