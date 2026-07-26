::: {#1253711789 .myid}
[]{#_Toc404786323}[]{#struct_0_x1628_17101_1451857782}[]{#_Toc237771564}[]{#_Toc185127721}[]{#_Toc87257691}

**NAT \-- NAT调试命令 \-- debugging nat**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1628_17101_350811092}

[**[debugging nat ]{lang="EN-US"}**[{ **event** \| **packet** \[ **acl** *acl-number* \] }]{lang="EN-US"}]{#struct_0_x1628_17101_x71558330}

[**[undo debugging nat ]{lang="EN-US"}**[{ **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1628_17101_x98798420}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1628_17101_1550522299}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1628_17101_x1842660546}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1496158146}

[[network-admin]{lang="EN-US"}]{#struct_0_x1628_17101_272830317}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1628_17101_1867875467}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1628_17101_680368593}

[**[event]{lang="EN-US"}**]{#struct_0_x1628_17101_x2086253499}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1628_17101_x952320701}[：]{style="font-family:宋体"} [表示报文调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1628_17101_x1586957784}[：指定仅对与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配的报文输出报文调试信息。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x874843830}

[**[debugging nat]{lang="EN-US"}**]{#struct_0_x1628_17101_2135521183}[命令用来打开]{style="font-family:宋体"}[NAT]{lang="EN-US"}[通用调试信息开关。]{style="font-family:宋体"}**[undo debugging nat]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[通用调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_817927194}[通用调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging nat event]{lang="EN-US"}]{#struct_0_x1628_17101_x1495961538}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_197355736}[[字段]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1416351525}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1628_17101_2076208450}

[[Deleted NAT session entry for configuration sequence changed!]{lang="EN-US"}]{#struct_0_x1628_17101_1123320681}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_400962555}[配置序号变化，删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话表项]{style="font-family:宋体"}

[[Deleted NAT session entry for out interface changed!]{lang="EN-US"}]{#struct_0_x1628_17101_x711305551}

[[会话接口检查发现出接口变化，删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_1692938279}[会话表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging nat packet]{lang="EN-US"}]{#struct_0_x1628_17101_x1114721614}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_200860583}[[字段]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1496027074}

[[描述]{style="font-family:黑体"}]{#struct_0_x1628_17101_x76293665}

[[PACKET: (*interface-type interface-number-direction*)]{lang="EN-US"}]{#struct_0_x1628_17101_1333779781}

[[报文信息：（接口名]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x1628_17101_1139361007}[报文方向）]{style="font-family:宋体"}

[[Protocol: *protocol*]{lang="EN-US"}]{#struct_0_x1628_17101_x280911709}

[[报文的协议类型]{style="font-family:宋体"}]{#struct_0_x1628_17101_1489091050}

[*[OrgSrcIP]{lang="EN-US"}*[: *OrgSrcPort* - *OrgDstIP*: *OrgDstPort* (VPN:    *OrgVpnIndex*) \-\-\-\-\--\>]{lang="EN-US"}]{#struct_0_x1628_17101_x1971655664}

[*[NewSrcIP]{lang="EN-US"}*[: *NewSrcPort* - *NewDstIP*: *NewDstPort* (VPN:    *NewVpnIndex*) ]{lang="EN-US"}]{#struct_0_x1628_17101_x1496485829}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_x1296374146}[转换前的报文原始五元组：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgSrcIP]{lang="EN-US"}*]{#struct_0_x1628_17101_x1966665555}[：]{lang="EN-US" style="font-family:宋体"}[原始源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgSrcPort]{lang="EN-US"}*]{#struct_0_x1628_17101_x1244826339}[：]{lang="EN-US" style="font-family:宋体"}[原始源端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgDstIP]{lang="EN-US"}*]{#struct_0_x1628_17101_28222413}[：]{lang="EN-US" style="font-family:宋体"}[原始目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgDstPort]{lang="EN-US"}*]{#struct_0_x1628_17101_207394907}[：]{lang="EN-US" style="font-family:宋体"}[原始目的端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgVpnIndex]{lang="EN-US"}*]{#struct_0_x1628_17101_x1496551365}[：]{lang="EN-US" style="font-family:
  宋体"}[原始报文所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_1065512252}[转换后的报文新五元组：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewSrcIP]{lang="EN-US"}*]{#struct_0_x1628_17101_1470381148}[：]{lang="EN-US" style="font-family:宋体"}[新源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewSrcPort]{lang="EN-US"}*]{#struct_0_x1628_17101_x788283253}[：]{lang="EN-US" style="font-family:宋体"}[新源端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewDstIP]{lang="EN-US"}*]{#struct_0_x1628_17101_x321531991}[：]{lang="EN-US" style="font-family:宋体"}[新目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewDstPort]{lang="EN-US"}*]{#struct_0_x1628_17101_x1546160675}[：]{lang="EN-US" style="font-family:宋体"}[新目的端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[New]{lang="EN-US"}*[V]{lang="EN-US"}]{#struct_0_x1628_17101_x1496354757}*[pnIndex]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[转换后报文所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[索引]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1524533184}

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_x1496420293}[在启用了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能的设备上打开]{style="font-family:宋体"}[NAT]{lang="EN-US"}[通用事件调试信息开关，有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文通过该设备，此时会创建]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。修改]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置，使得报文转换方式发生变化，如果上述]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文通过设备，则输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging nat event]{lang="EN-US"}]{#struct_0_x1628_17101_x2052305288}

[\*Apr 20 15:13:01:182 2012 Sysname NAT/7/COMMON: -MDC=1;]{lang="EN-US"}

[ EVENT: Deleted NAT session entry for configuration sequence changed!]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_x1327646878}*[因为]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置序号发生了变化，所以删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话表项]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_404896507}[在启用了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能的设备上打开]{style="font-family:宋体"}[NAT]{lang="EN-US"}[通用事件调试信息开关，有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文通过该设备，此时会创建]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话。关闭原来的报文出接口，使报文从另一个接口发送出去，如果上述]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文通过设备，则输出如下调试信息。]{style="font-family:宋体"}

[[[\<Sysname\> debugging nat event]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}]{#struct_0_x1628_17101_678481846}

[\*Apr 20 15:13:01:184 2012 Sysname NAT/7/COMMON: -MDC=1;]{lang="EN-US"}

[ EVENT: Deleted NAT session entry for out interface changed!]{lang="EN-US"}

[*[// NAT]{lang="EN-US"}*]{#struct_0_x1628_17101_x1985497570}*[会话在做接口检查时发现出接口变化，删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[会话表项]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_448182057}[在启用了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能的设备上打开]{style="font-family:宋体"}[NAT]{lang="EN-US"}[通用报文调试信息开关，有]{style="font-family:宋体"}[ping]{lang="EN-US"}[报文通过该设备时输出如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging nat packet]{lang="EN-US"}]{#struct_0_x1628_17101_x1496223685}

[\*Apr 20 15:13:01:178 2012 Sysname NAT/7/COMMON: -MDC=1;]{lang="EN-US"}

[ PACKET: (GigabitEthernet1/0/2-out) Protocol: ICMP]{lang="EN-US"}

[   192.168.1.100:    0 -       2.2.2.100:    0(VPN:    0) \-\-\-\-\--\>]{lang="EN-US"}

[       2.2.2.250:    0 -       2.2.2.100:    0(VPN:    0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_957834566}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[出方向对一个]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文进行了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换（转换了源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_x727076604}[在启用了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能的设备上打开]{style="font-family:宋体"}[NAT]{lang="EN-US"}[通用报文调试信息开关，有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文通过该设备时输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging nat packet]{lang="EN-US"}]{#struct_0_x1628_17101_2089228093}

[\*Apr 20 15:13:01:180 2012 Sysname NAT/7/COMMON: -MDC=1;]{lang="EN-US"}

[PACKET: (GigabitEthernet1/0/2-out) Protocol: TCP]{lang="EN-US"}

[   192.168.1.100: 2776 -       2.2.2.100:   21(VPN:    0) \-\-\-\-\--\>]{lang="EN-US"}

[       2.2.2.254: 1024 -       2.2.2.100:   21(VPN:    0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_x461257248}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[出方向对一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文进行了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换（转换了源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[+]{lang="EN-US"}[源端口号）]{style="font-family:宋体"}*

::: {#-913104485 .myid}
[]{#_Toc404786324}[]{#struct_0_x1628_17101_1416843483}

**NAT \-- NAT调试命令 \-- debugging nat alg**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1842174380}

[**[debugging nat alg ]{lang="EN-US"}**[{ **all** \| **event** \| **packet** \[ **acl** *acl-number* \] }]{lang="EN-US"}]{#struct_0_x1628_17101_1831631463}

[**[undo debugging nat alg ]{lang="EN-US"}**[{ **all** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1628_17101_x1496289221}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1628_17101_1048920476}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1628_17101_x477281614}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1628_17101_1608617281}

[[network-admin]{lang="EN-US"}]{#struct_0_x1628_17101_x359825024}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1628_17101_1262660616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1654434935}

[**[all]{lang="EN-US"}**]{#struct_0_x1628_17101_1886140161}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1628_17101_1344632661}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1628_17101_x1718265256}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1628_17101_x1496092613}[：指定仅对与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配的报文输出报文调试信息。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1277025573}

[**[debugging nat alg]{lang="EN-US"}**]{#struct_0_x1628_17101_122404191}[命令用来打开]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging nat alg]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}]{#struct_0_x1628_17101_x1203525510}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging nat alg event]{lang="EN-US"}]{#struct_0_x1628_17101_x1003504413}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_194197860}[[字段]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1426582831}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1453899354}

[[EVENT: (*interface-type interface-num*) The payload of DNS packet with domain *domain-name* will be translated.]{lang="EN-US"}]{#struct_0_x1628_17101_863493595}

[[接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_x1496158149}[收到]{style="font-family:
  宋体"}[DNS]{lang="EN-US"}[报文，]{style="font-family:宋体"}[NAT]{lang="EN-US"}[要处理的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的域名为]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging nat alg packet]{lang="EN-US"}]{#struct_0_x1628_17101_x1743592318}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_193030858}[[字段]{style="font-family:黑体"}]{#struct_0_x1628_17101_x1552394569}

[[描述]{style="font-family:黑体"}]{#struct_0_x1628_17101_260906302}

[[PACKET: (*interface-type interface-num*) ALG payload was translated according to *trans-type*:]{lang="EN-US"}]{#struct_0_x1628_17101_x1507286325}

[*[OrgIP/OrgPort]{lang="EN-US"}*[(VPN: *OrgVpnIndex*)\-\--\> *NewIP/NewPort*(VPN: *NewVpnIndex*)]{lang="EN-US"}]{#struct_0_x1628_17101_x1335687745}

[[在接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_x1205406009}[上]{style="font-family:
  宋体"}[对报文载荷中的地址进行了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换，转换类型为]{style="font-family:宋体"}*[trans-type]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[session table]{lang="EN-US"}]{#struct_0_x1628_17101_x1495961541}[：根据会话表转换]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[relation table(Local)]{lang="EN-US"}]{#struct_0_x1628_17101_x206301336}[：根据]{style="font-family:宋体"}[local]{lang="EN-US"}[类型的关联表的转换]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[relation table(Global)]{lang="EN-US"}]{#struct_0_x1628_17101_1270441375}[：根据]{style="font-family:宋体"}[global]{lang="EN-US"}[类型的关联表的转换]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[configuration]{lang="EN-US"}]{#struct_0_x1628_17101_x1012744219}[：根据配置信息转换]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_891462760}[转换前的报文载荷信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgIP]{lang="EN-US"}*]{#struct_0_x1628_17101_403477255}[：]{lang="EN-US" style="font-family:宋体"}[原始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgPort]{lang="EN-US"}*]{#struct_0_x1628_17101_x1496027077}[：]{lang="EN-US" style="font-family:宋体"}[原始端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgVpnIndex]{lang="EN-US"}*]{#struct_0_x1628_17101_326990862}[：]{lang="EN-US" style="font-family:
  宋体"}[原始报文所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_x91445939}[转换后的报文载荷信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewIP]{lang="EN-US"}*]{#struct_0_x1628_17101_1155728097}[：]{lang="EN-US" style="font-family:宋体"}[新]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewPort]{lang="EN-US"}*]{#struct_0_x1628_17101_1664141697}[：]{lang="EN-US" style="font-family:宋体"}[新端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewVpnInde]{lang="EN-US"}*]{#struct_0_x1628_17101_1835124798}*[x]{lang="EN-US"}*[：转换后]{lang="EN-US" style="font-family:宋体"}[报文所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[PACKET: (*interface-type interface-num*-*direction*) DNS *packet-type* packet was translated:]{lang="EN-US"}]{#struct_0_x1628_17101_x1496485828}

[*[OrgIP]{lang="EN-US"}*[\-\--\> *NewIP*]{lang="EN-US"}]{#struct_0_x1628_17101_1432509209}

[[在接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_x1531362123}[的]{style="font-family:
  宋体"}*[direction]{lang="EN-US"}*[方向上]{style="font-family:
  宋体"}[对]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文进行了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换，]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[，]{style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNS Query]{lang="EN-US"}]{#struct_0_x1628_17101_x694947321}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNS RRs]{lang="EN-US"}]{#struct_0_x1628_17101_x476079322}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_x1496551364}[转换前的报文载荷信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgIP]{lang="EN-US"}*]{#struct_0_x1628_17101_x1663371103}[：]{lang="EN-US" style="font-family:宋体"}[原始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_554609153}[转换后的报文载荷信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewIP]{lang="EN-US"}*]{#struct_0_x1628_17101_712615791}[：]{lang="EN-US" style="font-family:宋体"}[新]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PACKET: (*interface-type interface-num*-*direction*) ICMP error payload was translated:]{lang="EN-US"}]{#struct_0_x1628_17101_1883770735}

[[Pro: *protocol* *OrgIP*/*OrgPort*\-\--\> *NewIP*/*NewPort*]{lang="EN-US"}]{#struct_0_x1628_17101_1594980116}

[[在接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_1372739460}[的]{style="font-family:
  宋体"}*[direction]{lang="EN-US"}*[方向上]{style="font-family:
  宋体"}[对]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错控制报文中的载荷进行了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换]{style="font-family:宋体"}

[[引发该]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x1628_17101_x1496420292}[报文的报文的协议类型：]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_676578067}[转换前的报文载荷信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgIP]{lang="EN-US"}*]{#struct_0_x1628_17101_450311486}[：]{lang="EN-US" style="font-family:宋体"}[原始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgPort]{lang="EN-US"}*]{#struct_0_x1628_17101_802021615}[：]{lang="EN-US" style="font-family:宋体"}[原始端口号]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_347104370}[转换后的报文载荷信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewIP]{lang="EN-US"}*]{#struct_0_x1628_17101_x1496223684}[：]{lang="EN-US" style="font-family:宋体"}[新]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewPort]{lang="EN-US"}*]{#struct_0_x1628_17101_x608249375}[：]{lang="EN-US" style="font-family:宋体"}[新端口号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1628_17101_1183058477}

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_x1050946913}[在配置了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[和]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能的设备上打开]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}[事件调试信息开关，有]{style="font-family:宋体"}[FTP PORT]{lang="EN-US"}[报文通过设备时输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging nat alg event]{lang="EN-US"}]{#struct_0_x1628_17101_x1176650350}

[\*Apr 20 15:33:02:122 2012 Sysname NAT/7/ALG: -MDC=1;]{lang="EN-US"}

[ EVENT: (GigabitEthernet1/0/2) The payload of DNS packet with domain www.xxxxx.com will be translated.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_1399216825}*[接口]{style="font-family:宋体"}[Gigabit]{lang="EN-US"}[Ethernet1/0/2]{lang="EN-US"}[上收到]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文，其中的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名]{style="font-family:宋体"}[www.xxxxx.com]{lang="EN-US"}[需要进行]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_x1496289220}[在配置了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[和]{style="font-family:宋体"}[ALG]{lang="EN-US"}[功能的设备上打开]{style="font-family:宋体"}[NAT ALG]{lang="EN-US"}[报文调试信息开关，有]{style="font-family:宋体"}[FTP PORT]{lang="EN-US"}[报文通过设备时输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging nat alg packet]{lang="EN-US"}]{#struct_0_x1628_17101_x517163465}

[\*Apr 20 15:33:02:122 2012 Sysname NAT/7/ALG: -MDC=1;]{lang="EN-US"}

[ PACKET: (GigabitEthernet1/0/2) ALG payload was translated according to configuration:]{lang="EN-US"}

[    192.168.1.100/2787(VPN: 0) \-\--\> 2.2.2.254/10626(VPN: 0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_1501983814}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[对一个]{style="font-family:宋体"}[h225]{lang="EN-US"}[协议报文进行了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换]{style="font-family:宋体"}*

::: {#-1121825075 .myid}
[]{#_Toc404786325}[]{#struct_0_x1628_17101_x243814874}

**NAT \-- NAT调试命令 \-- debugging nat config**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1628_17101_237191011}

[**[debugging nat config ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1628_17101_x2000935108}

[**[undo debugging nat config ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1628_17101_x879337141}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1628_17101_1015367977}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1628_17101_x1496092612}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1628_17101_289058368}

[[network-admin]{lang="EN-US"}]{#struct_0_x1628_17101_x1210061194}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1628_17101_1379781122}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1628_17101_954712077}

[**[all]{lang="EN-US"}**]{#struct_0_x1628_17101_792486339}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1628_17101_1545304362}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1628_17101_x272862834}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1628_17101_x334566342}

[]{#OLE_LINK1}[**[debugging nat config]{lang="EN-US"}**]{#struct_0_x1628_17101_x1496158148}[命令用来打开]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置调试信息开关。]{style="font-family:宋体"}**[undo debugging nat config]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_x177508377}[配置调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x1628_17101_x1787929205}[[表1-5 ]{lang="EN-US"}[debugging nat config]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_196845707}[[字段]{style="font-family:黑体"}]{#struct_0_x1628_17101_x290749030}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1628_17101_76221656}

[[EVENT: Received lipc message, message type: *type*.]{lang="EN-US"}]{#struct_0_x1628_17101_x954088051}

[[收到]{style="font-family:宋体"}[lipc]{lang="EN-US"}]{#struct_0_x1628_17101_1388680824}[消息，消息类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[EVENT: Received ioctl message, message type: *type*.]{lang="EN-US"}]{#struct_0_x1628_17101_275019566}

[[收到]{style="font-family:宋体"}[ioctl]{lang="EN-US"}]{#struct_0_x1628_17101_x1495961540}[消息，消息类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，包括以下取值]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log enable]{lang="EN-US"}]{#struct_0_x1628_17101_x1772385277}[：使能日志开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log disable]{lang="EN-US"}]{#struct_0_x1628_17101_x614060598}[：关闭日志开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow active]{lang="EN-US"}]{#struct_0_x1628_17101_x1003443810}[：使能活跃流日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow deactive]{lang="EN-US"}]{#struct_0_x1628_17101_x614126134}[：关闭活跃流日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow begin]{lang="EN-US"}]{#struct_0_x1628_17101_x820330970}[：使能流创建日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow begin disable]{lang="EN-US"}]{#struct_0_x1628_17101_76397392}[：关闭流创建日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow end]{lang="EN-US"}]{#struct_0_x1628_17101_479002878}[：使能流结束日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow end disable]{lang="EN-US"}]{#struct_0_x1628_17101_256062672}[：关闭流结束日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set all log configration]{lang="EN-US"}]{#struct_0_x1628_17101_2108793444}[：使能所有日志功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set alg]{lang="EN-US"}]{#struct_0_x1628_17101_1448479754}[：使能]{style="font-family:宋体"}[ALG]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set]{lang="EN-US"}]{#struct_0_x1628_17101_x1496027076}[ all alg ]{lang="EN-US"}[configration]{lang="EN-US"}[：使能所有]{style="font-family:宋体"}[ALG]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set eim]{lang="EN-US"}]{#struct_0_x1628_17101_x1239093079}[：使能]{style="font-family:宋体"}[EIM]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add dns-map]{lang="EN-US"}]{#struct_0_x1628_17101_x1412062636}[：添加]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete dns-map]{lang="EN-US"}]{#struct_0_x1628_17101_9794731}[：删除]{style="font-family:宋体"}[DNS mapping]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add static inbound]{lang="EN-US"}]{#struct_0_x1628_17101_111269180}[：添加入方向静态地址转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete static inbound]{lang="EN-US"}]{#struct_0_x1628_17101_69598116}[：删除入方向静态地址转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add static outbound]{lang="EN-US"}]{#struct_0_x1628_17101_x1125605412}[：添加出方向静态地址转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete static outbound]{lang="EN-US"}]{#struct_0_x1628_17101_x818496035}[：删除出方向静态地址转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add address group]{lang="EN-US"}]{#struct_0_x1628_17101_x453329964}[：添加地址组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete address group]{lang="EN-US"}]{#struct_0_x1628_17101_x990109077}[：删除地址组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add address group member]{lang="EN-US"}]{#struct_0_x1628_17101_513477674}[：添加地址组成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete address group member]{lang="EN-US"}]{#struct_0_x1628_17101_69532580}[：删除地址组成员]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add server group]{lang="EN-US"}]{#struct_0_x1628_17101_1207941445}[：添加服务器组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete server group]{lang="EN-US"}]{#struct_0_x1628_17101_x1440573598}[：删除服务器组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add server group member]{lang="EN-US"}]{#struct_0_x1628_17101_x1604690233}[：添加服务器组成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete server group member]{lang="EN-US"}]{#struct_0_x1628_17101_869209963}[：删除服务器组成员]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set interface static]{lang="EN-US"}]{#struct_0_x1628_17101_69729188}[：设置接口下的静态使能开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set interface hairpin]{lang="EN-US"}]{#struct_0_x1628_17101_x2099937388}[：设置接口下的]{style="font-family:宋体"}[hairpin]{lang="EN-US"}[使能开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add dynamic]{lang="EN-US"}]{#struct_0_x1628_17101_x1774099820}[：添加动态转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete dynamic]{lang="EN-US"}]{#struct_0_x1628_17101_x20568352}[：删除动态转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add server]{lang="EN-US"}]{#struct_0_x1628_17101_603028743}[：添加内部服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete server]{lang="EN-US"}]{#struct_0_x1628_17101_69663652}[：删除内部服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[acl rule change]{lang="EN-US"}]{#struct_0_x1628_17101_159025710}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[get statistics]{lang="EN-US"}]{#struct_0_x1628_17101_x701575799}[：获取统计信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smoothing begin]{lang="EN-US"}]{#struct_0_x1628_17101_1916221520}[：平滑开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smoothing end]{lang="EN-US"}]{#struct_0_x1628_17101_69860260}[：平滑结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[get server group statistics]{lang="EN-US"}]{#struct_0_x1628_17101_x713535482}[：获取服务器组统计信息]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add port]{lang="EN-US"}]{#struct_0_x1628_17101_1818101135}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group]{lang="EN-US"}[：添加端口块组]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete port block group]{lang="EN-US"}]{#struct_0_x1628_17101_1818428815}[：删除端口块组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add port]{lang="EN-US"}]{#struct_0_x1628_17101_241871224}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group member]{lang="EN-US"}[：添加端口块组的地址成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete port block]{lang="EN-US"}]{#struct_0_x1628_17101_1818494351}[ ]{lang="EN-US"}[group member]{lang="EN-US"}[：删除端口块组的地址成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set port]{lang="EN-US"}]{#struct_0_x1628_17101_x1628907768}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group parameters]{lang="EN-US"}[：设置端口块组的参数]{style="font-family:宋体"}

[[EVENT: Received ioctl message, message type: *type*]{lang="EN-US"}]{#struct_0_x1628_17101_1818297743}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add outbound port]{lang="EN-US"}]{#struct_0_x1628_17101_x1990166010}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group]{lang="EN-US"}[：添加]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[delete outbound port]{lang="EN-US"}]{#struct_0_x1628_17101_1818363279}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group]{lang="EN-US"}[：删除]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[端口块静态映射配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[log NAT444 enable]{lang="EN-US"}]{#struct_0_x1628_17101_x1630099594}[：使能]{lang="EN-US" style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志或告警信息日志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[log NAT444 disable]{lang="EN-US"}]{#struct_0_x1628_17101_x613732918}[：关闭]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户日志或告警信息日志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set service slot]{lang="EN-US"}]{#struct_0_x1628_17101_x1073549202}[：设置接口与业务板号绑定关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add ]{lang="EN-US"}]{#struct_0_x1628_17101_492534739}[NAT]{lang="EN-US"}[ address]{lang="EN-US"}[：添加]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete ]{lang="EN-US"}]{#struct_0_x1628_17101_381725226}[NAT]{lang="EN-US"}[ address]{lang="EN-US"}[：删除]{style="font-family:宋体"}[NAT]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete all ]{lang="EN-US"}[NAT ]{lang="EN-US"}]{#struct_0_x1628_17101_x1429845098}[configurations on ]{lang="EN-US"}[interface]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}[接口上的所有]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}

[[EVENT: Received ACL event message, ACL number: *number*.]{lang="EN-US"}]{#struct_0_x1628_17101_1523134550}

[[收到]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1628_17101_122118487}[事件消息，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[EVENT: Received L3VPN message, event: *event*.]{lang="EN-US"}]{#struct_0_x1628_17101_69794724}

[[收到]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}]{#struct_0_x1628_17101_2101284247}[事件消息，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Create]{lang="EN-US"}]{#struct_0_x1628_17101_x1575360113}[：]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1628_17101_1097039312}[：]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[删除]{lang="EN-US" style="font-family:宋体"}

[[EVENT: Received interface event message, interface: *interface-type interface-num*, event: *event*.]{lang="EN-US"}]{#struct_0_x1628_17101_69991332}

[[收到接口事件消息，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_1595271737}[，事件类型为]{style="font-family:
  宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:
  宋体"}*[event]{lang="EN-US"}*[包括以下取值：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1628_17101_223208530}[：接口激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deactive]{lang="EN-US"}]{#struct_0_x1628_17101_x1752710765}[：去激活接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1628_17101_69925796}[：]{lang="EN-US" style="font-family:宋体"}[删除]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Push finish]{lang="EN-US"}]{#struct_0_x1628_17101_x280744301}[：事件补报结束]{style="font-family:宋体"}

[[EVENT: Received slot event message, slot number: *slot-num*, event: *event*.]{lang="EN-US"}]{#struct_0_x1628_17101_1844254585}

[[收到接口板事件消息，接口板所在槽位号为]{style="font-family:宋体"}*[slot-num]{lang="EN-US"}*]{#struct_0_x1628_17101_70122404}[，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inserted]{lang="EN-US"}]{#struct_0_x1628_17101_1702322784}[：板插入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remove]{lang="EN-US"}]{#struct_0_x1628_17101_x126207282}[：板拔出]{style="font-family:宋体"}

[[EVENT: Received link event message, interface: *interface*, event: *event*..]{lang="EN-US"}]{#struct_0_x1628_17101_x141101920}

[[收到接口链路事件消息，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_x1675000476}[，事件类型为]{style="font-family:
  宋体"}*[event]{lang="EN-US"}*[，包括以下取值：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Link up]{lang="EN-US"}]{#struct_0_x1628_17101_70056868}[：链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Push finish]{lang="EN-US"}]{#struct_0_x1628_17101_4586647}[：补充报告事件结束]{style="font-family:宋体"}

[[EVENT: Received IPADDR event message, interface: *interface*, event: *event*.]{lang="EN-US"}]{#struct_0_x1628_17101_1405469929}

[[收到地址事件消息，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x1628_17101_x290505509}[，事件类型为]{style="font-family:
  宋体"}*[event]{lang="EN-US"}*[，包括以下取值：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_x1628_17101_69598117}[：地址添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x1628_17101_830709724}[：地址删除]{lang="EN-US" style="font-family:宋体"}

[[EVENT: Added configuration in kernel: *configuration-type*.]{lang="EN-US"}]{#struct_0_x1628_17101_x118842552}

[[内核新增一条配置，配置类型为]{style="font-family:宋体"}*[configuration-type]{lang="EN-US"}*]{#struct_0_x1628_17101_69532581}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dns-map]{lang="EN-US"}]{#struct_0_x1628_17101_x1130710715}[：]{style="font-family:宋体"}[dns-map]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static inbound]{lang="EN-US"}]{#struct_0_x1628_17101_x2024899067}[：]{style="font-family:宋体"}[static inbound]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static outbound]{lang="EN-US"}]{#struct_0_x1628_17101_69729189}[：]{style="font-family:宋体"}[static outbound]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[address group]{lang="EN-US"}]{#struct_0_x1628_17101_238714772}[：地址组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[address group member]{lang="EN-US"}]{#struct_0_x1628_17101_x639842209}[：地址组成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server group]{lang="EN-US"}]{#struct_0_x1628_17101_69663653}[：内部服务器组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server group member]{lang="EN-US"}]{#struct_0_x1628_17101_x1797289426}[：内部服务器组成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_x1628_17101_x46880159}[：动态地址转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_x1628_17101_69860261}[：内部服务器配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port]{lang="EN-US"}]{#struct_0_x1628_17101_1818166670}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group]{lang="EN-US"}[：端口块组配置]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port]{lang="EN-US"}]{#struct_0_x1628_17101_x1634668993}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group member]{lang="EN-US"}[：端口块组的地址成员配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT address]{lang="EN-US"}]{#struct_0_x1628_17101_539523370}[：]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[EVENT: Deleted configuration in kernel: *configuration-type*.]{lang="EN-US"}]{#struct_0_x1628_17101_1625116678}

[[内核删除一条配置，配置类型为]{style="font-family:宋体"}*[configuration-type]{lang="EN-US"}*]{#struct_0_x1628_17101_46287503}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dns-map]{lang="EN-US"}]{#struct_0_x1628_17101_69794725}[：]{style="font-family:宋体"}[dns-map]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static inbound]{lang="EN-US"}]{#struct_0_x1628_17101_x237367913}[：]{style="font-family:宋体"}[static inbound]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static outbound]{lang="EN-US"}]{#struct_0_x1628_17101_69991333}[：]{style="font-family:宋体"}[static outbound]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[address group]{lang="EN-US"}]{#struct_0_x1628_17101_x743380423}[：地址组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[address group member]{lang="EN-US"}]{#struct_0_x1628_17101_85856522}[：地址组成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server group]{lang="EN-US"}]{#struct_0_x1628_17101_69925797}[：内部服务器组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server group member]{lang="EN-US"}]{#struct_0_x1628_17101_2057907859}[：内部服务器组成员]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_x1628_17101_1387652869}[：动态地址转换配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_x1628_17101_70122405}[：内部服务器配置]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port]{lang="EN-US"}]{#struct_0_x1628_17101_1818232206}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group]{lang="EN-US"}[：端口块组配置]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port]{lang="EN-US"}]{#struct_0_x1628_17101_1818035598}[ ]{lang="EN-US"}[block]{lang="EN-US"}[ ]{lang="EN-US"}[group member]{lang="EN-US"}[：端口块组的地址成员配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT address]{lang="EN-US"}]{#struct_0_x1628_17101_2105607311}[：]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[all ]{lang="EN-US"}[NAT ]{lang="EN-US"}]{#struct_0_x1628_17101_x623276044}[configurations on ]{lang="EN-US"}[interface]{lang="EN-US"}[：接口上的所有]{lang="EN-US" style="font-family:
  宋体"}[NAT]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}

[[EVENT: Set configuration in kernel: *configuration-type*.]{lang="EN-US"}]{#struct_0_x1628_17101_x2097417056}

[[内核中的]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x1628_17101_70056869}[配置被修改，配置类型为]{style="font-family:宋体"}*[configuration-type]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log enable]{lang="EN-US"}]{#struct_0_x1628_17101_1960901783}[：日志开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow active]{lang="EN-US"}]{#struct_0_x1628_17101_x1481259192}[：活跃流日志开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow begin]{lang="EN-US"}]{#struct_0_x1628_17101_69598114}[：流创建日志开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log flow end]{lang="EN-US"}]{#struct_0_x1628_17101_x1507942436}[：流删除日志开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[all log configration]{lang="EN-US"}]{#struct_0_x1628_17101_x138090197}[：所有日志配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[alg]{lang="EN-US"}]{#struct_0_x1628_17101_69532578}[：]{style="font-family:宋体"}[ALG]{lang="EN-US"}[开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[all alg configration]{lang="EN-US"}]{#struct_0_x1628_17101_1695015984}[：所有]{style="font-family:宋体"}[ALG]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[eim]{lang="EN-US"}]{#struct_0_x1628_17101_69729186}[：]{style="font-family:宋体"}[EIM]{lang="EN-US"}[开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface static]{lang="EN-US"}]{#struct_0_x1628_17101_x952926316}[：接口下静态使能开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface hairpin]{lang="EN-US"}]{#struct_0_x1628_17101_x15911091}[：接口下]{style="font-family:宋体"}[hairpin]{lang="EN-US"}[使能开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[acl rule change]{lang="EN-US"}]{#struct_0_x1628_17101_69663650}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth begin]{lang="EN-US"}]{#struct_0_x1628_17101_x223311314}[：平滑开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[smooth end]{lang="EN-US"}]{#struct_0_x1628_17101_69860258}[：平滑结束]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port block group parameters]{lang="EN-US"}]{#struct_0_x1628_17101_1818101134}[：]{lang="EN-US" style="font-family:宋体"}[端口块]{style="font-family:宋体"}[组参数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[service slot]{lang="EN-US"}]{#struct_0_x1628_17101_x1073614738}[：业务板号]{lang="EN-US" style="font-family:宋体"}

[[FLOWMGR *flowmgr-event*, Dest: *dest*, Priority: *priority*, MatchWildCard: *wildcard*, SrcKey: *sip*, DstKey: *dip*, *protocol*,  VPN: *vpn*.]{lang="EN-US"}]{#struct_0_x1628_17101_1818428814}

[[收到引流信息，事件类型为]{style="font-family:宋体"}*[flowmgr-event]{lang="EN-US"}*]{#struct_0_x1628_17101_241936760}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADD]{lang="EN-US"}]{#struct_0_x1628_17101_1818494350}[：]{lang="EN-US" style="font-family:宋体"}[删除引流]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1628_17101_1818297742}[EL]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[增加引流]{style="font-family:宋体"}

[[目的引擎为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*]{#struct_0_x1628_17101_x1990231546}

[[优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}*]{#struct_0_x1628_17101_1818363278}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_ADDRGRP_ADDR]{lang="EN-US"}]{#struct_0_x1628_17101_x1630034058}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_ADDRGRP_PORT]{lang="EN-US"}]{#struct_0_x1628_17101_1817642382}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_PORTBLOCK_LOCAL]{lang="EN-US"}]{#struct_0_x1628_17101_x1049158731}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_PORTBLOCK_GLOBAL]{lang="EN-US"}]{#struct_0_x1628_17101_1817707918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[NAT_FLOW_SRVGRP]{lang="EN-US"}]{#struct_0_x1628_17101_466450784}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_SERVER_LOCAL]{lang="EN-US"}]{#struct_0_x1628_17101_1818166669}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_SERVER_GLOBAL]{lang="EN-US"}]{#struct_0_x1628_17101_1818232205}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_STATIC_INBOUND_ORIGINAL]{lang="EN-US"}]{#struct_0_x1628_17101_1112611889}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_STATIC_INBOUND_NAT]{lang="EN-US"}]{#struct_0_x1628_17101_1818035597}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_STATIC_OUTBOUND_ORIGINAL]{lang="EN-US"}]{#struct_0_x1628_17101_x466656531}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NAT_FLOW_STATIC_OUTBOUND_NAT]{lang="EN-US"}]{#struct_0_x1628_17101_1818101133}

[[源地址信息为]{style="font-family:宋体"}*[sip]{lang="EN-US"}*]{#struct_0_x1628_17101_x2030006166}[，表示源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围]{style="font-family:宋体"}

[[目的地址信息为]{style="font-family:宋体"}*[dip, protocol]{lang="EN-US"}*]{#struct_0_x1628_17101_1818428813}[，]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[表示协议号，]{style="font-family:宋体"}*[dip]{lang="EN-US"}*[表示目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围]{style="font-family:宋体"}

[[所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1628_17101_1818494349}[名称为]{style="font-family:宋体"}*[vpn]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1628_17101_1648799191}

[[\# ]{lang="EN-US"}]{#struct_0_x1628_17101_974740718}[在启用了]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能的设备上打开所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置调试功能，并配置]{style="font-family:宋体"}**[nat service]{lang="EN-US"}**[命令和]{style="font-family:宋体"}**[nat outbound]{lang="EN-US"}**[命令。]{style="font-family:宋体"}**[nat service]{lang="EN-US"}**[命令及相关]{style="font-family:宋体"}[Debug]{lang="EN-US"}[信息的支持情况与设备的具体型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[\<Sysname\> debugging nat config all]{lang="EN-US"}]{#struct_0_x1628_17101_x1429910634}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] nat service slot 1]{lang="EN-US"}

[\*Nov 5 08:55:11:361 2013 H3C NAT/7/CONFIG: -MDC=1;  ]{lang="EN-US"}

[ EVENT: Received ioctl message, message type: set service slot.]{lang="EN-US"}

[\*Nov 5 08:55:11:361 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Set configuration in kernel: service slot.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_136173307}*[内核收到添加接口绑定业务板的]{style="font-family:宋体"}[IOCTL]{lang="EN-US"}[消息，并且成功添加。]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1\] nat outbound 2001 address-group 1 no-pat reversible]{lang="EN-US"}]{#struct_0_x1628_17101_1032919530}

[\*]{lang="EN-US"}[Nov 5 08:55:22:732 2013 H3C NAT/7/CONFIG: -MDC=1;  ]{lang="EN-US"}

[ EVENT: Received ioctl message, message type: add address group.]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:732 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Added configuration in kernel: address group.]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:733 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Received ioctl message, message type: set address group parameters.]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:733 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Received ioctl message, message type: add NAT address. ]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:733 2013 H3C NAT/7/CONFIG: -MDC=1; ]{lang="EN-US"}

[ EVENT: Added configuration in kernel: NAT address.]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:739 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Received ioctl message, message type: add NAT address. ]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:739 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Added configuration in kernel: NAT address.]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:742 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Received ioctl message, message type: add dynamic.]{lang="EN-US"}

[\*]{lang="EN-US"}[Nov 5 08:55:22:742 2013 H3C NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ EVENT: Added configuration in kernel: dynamic.]{lang="EN-US"}

[\*Nov 5 08:55:22:745 2013 Sysname NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ FLOWMGR ADD, Dest: 0x11, Priority: AddrGrp-Addr, MatchWildCard: IF_IN \| L3_DEST]{lang="EN-US"}

[ , SrcKey: 0.0.0.0 255.255.255.255, DstKey: 1.2.3.9-1.2.3.9, All protocols, VPN: vpn1.]{lang="EN-US"}

[\*Nov 5 08:55:22:745 2013 Sysname NAT/7/CONFIG: -MDC=1;]{lang="EN-US"}

[ FLOWMGR ADD, Dest: 0x19, Priority: AddrGrp-Addr, MatchWildCard: IF_IN \| L3_DEST]{lang="EN-US"}

[ , SrcKey: 0.0.0.0 255.255.255.255, DstKey: 1.2.3.10-1.2.3.10, All protocols, VPN: vpn1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1628_17101_x56736720}*[收到]{style="font-family:宋体"}[LIPC]{lang="EN-US"}[消息和]{style="font-family:宋体"}[IOCTL]{lang="EN-US"}[消息，并且在内核成功添加动态地址转换配置。]{style="font-family:宋体"}*
