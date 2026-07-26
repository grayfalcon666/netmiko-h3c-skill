::: {#-313324664 .myid}
[]{#_Toc404793383}[]{#struct_0_78899_x1004_2039018304}[]{#_Toc215561776}[]{#_Toc135453993}

**ASPF \-- ASPF调试命令 \-- debugging aspf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78899_x1004_1059237234}

[**[debugging aspf]{lang="EN-US"}**[ { **all** \| **event** \| **packet** \[ **acl** *acl-number* \] }]{lang="EN-US"}]{#struct_0_78899_x1004_833221907}

[**[undo debugging aspf ]{lang="EN-US"}**[{ **all** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_78899_x1004_x1986502878}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78899_x1004_1263436104}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78899_x1004_668405482}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78899_x1004_x1374933930}

[[network-admin]{lang="EN-US"}]{#struct_0_78899_x1004_1336826177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78899_x1004_2098211554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78899_x1004_x1601206521}

[**[all]{lang="EN-US"}**]{#struct_0_78899_x1004_x187476588}[：表示所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_78899_x1004_1435643432}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_78899_x1004_717392241}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_78899_x1004_x1612773983}[：表示仅输出匹配指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的报文的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话的报文调试信息。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。若不指定该参数，则表示输出所有会话的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[报文调试信息。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78899_x1004_x600104788}

[**[debugging]{lang="EN-US"}**[ **aspf**]{lang="EN-US"}]{#struct_0_78899_x1004_x1750875326}[命令用来打开]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **aspf**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x1987515515}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging aspf event]{lang="EN-US"}]{#struct_0_78899_x1004_x1714507724}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x976674663}[[字段]{style="font-family:黑体"}]{#struct_0_78899_x1004_x21692183}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78899_x1004_x1600878841}

[[Received an active event for interface *interface-type interface-num*.]{lang="EN-US"}]{#struct_0_78899_x1004_1658390945}

[[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_722674999}[收到一个接口激活事件通知]{style="font-family:宋体"}

[[Received a deactive event for *interface-type interface-num*.]{lang="EN-US"}]{#struct_0_78899_x1004_x579521791}

[[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_451186123}[收到一个接口去激活事件通知]{style="font-family:宋体"}

[[Received a deleting event for interface *interface-type interface-num*.]{lang="EN-US"}]{#struct_0_78899_x1004_x1289455073}

[[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_1157241422}[收到一个接口删除事件通知]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging aspf ]{lang="EN-US"}]{#struct_0_78899_x1004_x1930907466}[packet]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x974952839}[[字段]{style="font-family:黑体"}]{#struct_0_78899_x1004_x1600813305}

[[描述]{style="font-family:黑体"}]{#struct_0_78899_x1004_667196092}

[[Interface]{lang="EN-US"}]{#struct_0_78899_x1004_704124966}

[[处理报文的接口名称]{style="font-family:宋体"}]{#struct_0_78899_x1004_x1930083449}

[[Direction]{lang="EN-US"}]{#struct_0_78899_x1004_x1259536759}

[[报文方向，取值为]{style="font-family:宋体"}[INBOUND]{lang="EN-US"}]{#struct_0_78899_x1004_739723138}[和]{style="font-family:宋体"}[OUTBOUND]{lang="EN-US"}

[[Src-Zone=*source-zone-name*]{lang="EN-US"}]{#struct_0_78899_x1004_x1750443055}

[[源安全域名称]{style="font-family:宋体"}]{#struct_0_78899_x1004_x286228764}

[[当报文匹配上可匹配任意源安全域的域间实例时，源安全域名称后会附加显示]{style="font-family:宋体"}[(matched=Any)]{lang="EN-US"}]{#struct_0_78899_x1004_706698757}[信息]{style="font-family:宋体"}

[[Dst-Zone=*destination-zone-name*]{lang="EN-US"}]{#struct_0_78899_x1004_x1750508591}

[[目的安全域名称]{style="font-family:宋体"}]{#struct_0_78899_x1004_x827665817}

[[当报文匹配上可匹配任意目的安全域的域间实例时，目的安全域名称后会附加显示]{style="font-family:宋体"}[(matched=Any)]{lang="EN-US"}]{#struct_0_78899_x1004_121138027}[信息]{style="font-family:宋体"}

[[If-In=*inbound-interface-name*(*ifIndexIn*)]{lang="EN-US"}]{#struct_0_78899_x1004_x1118395448}

[[入接口名称（入接口索引号）]{style="font-family:宋体"}]{#struct_0_78899_x1004_1975673203}

[[If-Out=*outbound-interface-name*(i*fIndexOut*)]{lang="EN-US"}]{#struct_0_78899_x1004_x1750049839}

[[出接口名称（出接口索引号）]{style="font-family:宋体"}]{#struct_0_78899_x1004_x907914936}

[[VLAN-In]{lang="EN-US"}]{#struct_0_78899_x1004_x729839265}

[[入接口所属]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_78899_x1004_x729773729}[，该字段仅在入接口工作在二层模式时可见]{style="font-family:宋体"}

[[VLAN-Out]{lang="EN-US"}]{#struct_0_78899_x1004_1872518985}

[[出接口所属]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_78899_x1004_1134006164}[，该字段仅在出接口工作在二层模式时可见]{style="font-family:宋体"}

[[Src-IP=*source-ip-address*]{lang="EN-US"}]{#struct_0_78899_x1004_x1601009913}

[[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_78899_x1004_x1220776870}[地址]{style="font-family:宋体"}

[[Dst-IP=*destination-ip-address*]{lang="EN-US"}]{#struct_0_78899_x1004_x1908290782}

[[报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_78899_x1004_1952030970}[地址]{style="font-family:宋体"}

[[VPN-Instance=*vpn-instance-name*]{lang="EN-US"}]{#struct_0_78899_x1004_1562977558}

[[报文所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_78899_x1004_1882489572}[实例]{style="font-family:宋体"}

[[Src-Port=*source-port-number*]{lang="EN-US"}]{#struct_0_78899_x1004_x1854126418}

[[报文的源端口]{style="font-family:宋体"}]{#struct_0_78899_x1004_x1600944377}

[[Dst-Port=*destination-port-number*]{lang="EN-US"}]{#struct_0_78899_x1004_x241124991}

[[报文的目的端口]{style="font-family:宋体"}]{#struct_0_78899_x1004_1931755096}

[[Protocol=*protocol*(*number*)]{lang="EN-US"}]{#struct_0_78899_x1004_781700524}

[[报文的四层协议名（协议号）]{style="font-family:宋体"}]{#struct_0_78899_x1004_2058832244}

[[The packet of no session was dropped by ASPF, because the ICMP error checking failed.]{lang="EN-US"}]{#struct_0_78899_x1004_x1376166315}

[[报文没有匹配任何会话，因为没有通过]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x1430203455}[的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文检查，被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃]{style="font-family:宋体"}

[[The packet of no session was dropped by ASPF, because the TCP SYN checking failed.]{lang="EN-US"}]{#struct_0_78899_x1004_x1482811160}

[[报文没有匹配任何会话，因为没有通过]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x274666985}[的]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}[检查，被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃]{style="font-family:宋体"}

[[The first packet was dropped by ASPF, because the TCP SYN checking failed.]{lang="EN-US"}]{#struct_0_78899_x1004_1510546307}

[[会话首报文没有通过]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x903746121}[的]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}[检查，被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃]{style="font-family:宋体"}

[[The non-first packet of child session was dropped by ASPF for invalid status.]{lang="EN-US"}]{#struct_0_78899_x1004_x1750180911}

[[子会话后续报文由于状态机非法，被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x761359733}[丢弃]{style="font-family:宋体"}

[[The non-first packet was dropped by ASPF for invalid status.]{lang="EN-US"}]{#struct_0_78899_x1004_x1163520085}

[[会话后续报文由于状态机非法，被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x1617247125}[丢弃]{style="font-family:宋体"}

[[The first packet of child session was set an ALG flag by ASPF.]{lang="EN-US"}]{#struct_0_78899_x1004_x1607864126}

[[子会话首报文被设置需要进行]{style="font-family:宋体"}[ALG]{lang="EN-US"}]{#struct_0_78899_x1004_x1750246447}[处理标记]{style="font-family:宋体"}

[[The gtp packet was dropped by ASPF.]{lang="EN-US"}]{#struct_0_78899_x1004_220030998}

[[GTP]{lang="EN-US"}]{#struct_0_78899_x1004_x1091882943}[报文在]{style="font-family:宋体"}[ALG]{lang="EN-US"}[处理中没有通过检查被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃]{style="font-family:宋体"}

[[The first packet was dropped by ASPF for nonexistent zone-pair.]{lang="EN-US"}]{#struct_0_78899_x1004_x1749787695}

[[首报文因域间实例不存在被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x865978874}[丢弃]{style="font-family:宋体"}

[[The first packet of child session was dropped by ASPF, because the TCP SYN checking failed.]{lang="EN-US"}]{#struct_0_78899_x1004_x1467777844}

[[子会话首报文没有通过]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x1749853231}[的]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}[检查，被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃]{style="font-family:宋体"}

[[The non-first packet of child session was dropped by ASPF for nonexistent zone pair.]{lang="EN-US"}]{#struct_0_78899_x1004_707026436}

[[子会话非首报文因域间实例不存在被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_x117641807}[丢弃]{style="font-family:宋体"}

[[The first packet of child session was dropped by ASPF for nonexistent zone pair.]{lang="EN-US"}]{#struct_0_78899_x1004_706567684}

[[子会话首报文因域间实例不存在被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_1872229566}[丢弃]{style="font-family:宋体"}

[[The non-first packet was dropped by ASPF for nonexistent zone pair.]{lang="EN-US"}]{#struct_0_78899_x1004_706633220}

[[非首报文因域间实例不存在被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_950739739}[丢弃]{style="font-family:宋体"}

[[The packet that matches no session was dropped by ASPF for nonexistent zone pair.]{lang="EN-US"}]{#struct_0_78899_x1004_706698756}

[[没有匹配任何会话的报文因域间实例不存在被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_78899_x1004_121138026}[丢弃]{style="font-family:宋体"}

[[The non-first packet was dropped because of config changes.]{lang="EN-US"}]{#struct_0_78899_x1004_706764292}

[[非首报文由于配置变更被丢弃]{style="font-family:宋体"}]{#struct_0_78899_x1004_536617560}

[[The non-first packet of child session was dropped by packet filter or object-policy.]{lang="EN-US"}]{#struct_0_78899_x1004_707354116}

[[子会话非首报文被]{style="font-family:宋体"}[packet filter]{lang="EN-US"}]{#struct_0_78899_x1004_178955849}[或]{style="font-family:宋体"}[object-policy]{lang="FR"}[丢弃]{style="font-family:宋体"}

[[The first packet of child session was dropped by packet filter or object-policy.]{lang="EN-US"}]{#struct_0_78899_x1004_707419652}

[[子会话首报文被]{style="font-family:宋体"}[packet filter]{lang="EN-US"}]{#struct_0_78899_x1004_x1569401082}[或]{style="font-family:宋体"}[object-policy]{lang="FR"}[丢弃]{style="font-family:宋体"}

[[The non-first packet was dropped by packet filter or object-policy.]{lang="EN-US"}]{#struct_0_78899_x1004_706829831}

[[非首报文被]{style="font-family:宋体"}[packet filter]{lang="EN-US"}]{#struct_0_78899_x1004_1590793515}[或]{style="font-family:宋体"}[object-policy]{lang="FR"}[丢弃]{style="font-family:宋体"}

[[The first packet was dropped by packet filter or object-policy.]{lang="EN-US"}]{#struct_0_78899_x1004_706895367}

[[首报文被]{style="font-family:宋体"}[packet filter]{lang="EN-US"}]{#struct_0_78899_x1004_x1550935809}[或]{style="font-family:宋体"}[object-policy]{lang="FR"}[丢弃]{style="font-family:宋体"}

[[The packet that matches no session was dropped by packet filter or object-policy.]{lang="EN-US"}]{#struct_0_78899_x1004_706960903}

[[报文因没有匹配任何会话被]{style="font-family:宋体"}[packet filter]{lang="EN-US"}]{#struct_0_78899_x1004_x1132459804}[或]{style="font-family:宋体"}[ object-policy]{lang="FR"}[丢弃]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78899_x1004_243436657}

[[\# ]{lang="EN-US"}]{#struct_0_78899_x1004_x1626988866}[在设备上配置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，在接口上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，并且打开]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[报文调试信息开关，当有报文被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging aspf packet]{lang="EN-US"}]{#struct_0_78899_x1004_1025406045}

[\*Aut 28 12:09:44:309 2011 Sysname ASPF/7/PACKET: -MDC=1; The packet of no session was dropped by ASPF, because the TCP SYN checking failed. Interface=GigabitEthernet1/0/2, Diretion=INBOUND; Packet Info: Src-IP=1.1.1.1, Dst-IP=1.1.1.2, VPN-Instance=none, Src-Port=12345, Dst-Port=21, Protocol=tcp]{lang="EN-US"}[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）]{style="font-family:宋体"}[.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78899_x1004_x670807518}*[报文没有匹配任何会话，通过]{style="font-family:宋体"}[PFILTER]{lang="EN-US"}[检查，但没有通过]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}[检查，因此被丢弃。该报文来自接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的入方向，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，不属于属于公网，源端口号为]{style="font-family:宋体"}[12345]{lang="EN-US"}[，目的端口号为]{style="font-family:宋体"}[21]{lang="EN-US"}[，协议类型为]{style="font-family:宋体"}[TCP]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78899_x1004_x1750311984}[在设备上配置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，在域间应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，并且打开]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[报文调试信息开关，当有报文被]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢弃时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging aspf packet]{lang="EN-US"}]{#struct_0_78899_x1004_1641386839}

[\*Aut 28 12:09:44:309 2011 Sysname ASPF/7/PACKET: -MDC=1; The first packet was dropped by ASPF, because the TCP SYN checking failed. Src-Zone=Zone1, Dst-Zone=Zone2; If-In=Ten-GigabitEthernet7/0/17(471), If-Out=Ten-GigabitEthernet7/0/18(472); Packet Info: Src-IP=1.1.1.1, Dst-IP=1.1.1.2, VPN-Instance=none, Src-Port=12345, Dst-Port=21, Protocol=tcp]{lang="EN-US"}[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）]{style="font-family:
宋体"}[.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_78899_x1004_x1750377520}*[ ]{lang="EN-US"}[报文]{style="font-family:宋体"}[没有匹配任何会话，通过]{style="font-family:宋体"}[PFILTER]{lang="EN-US"}[检查，但没有通过]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}[检查，因此被丢弃。该报文自安全域]{style="font-family:宋体"}[Zone1]{lang="EN-US"}[发往安全域]{style="font-family:宋体"}[Zone2]{lang="EN-US"}[，人接口为]{style="font-family:宋体"}[Ten-GigabitEthernet7/0/17]{lang="EN-US"}[，出接口为]{style="font-family:
宋体"}[Ten-GigabitEthernet7/0/18]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，属于公网，源端口号为]{style="font-family:宋体"}[12345]{lang="EN-US"}[，目的端口号为]{style="font-family:宋体"}[21]{lang="EN-US"}[，协议类型为]{style="font-family:宋体"}[TCP]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78899_x1004_x1601206520}[在设备上配置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，在接口上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，并且打开]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[事件调试开关时，当有接口事件上报时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging aspf event]{lang="EN-US"}]{#struct_0_78899_x1004_x1753560529}

[[\*Aut 28 12:13:44:290 2011 Sysname ASPF/7/EVENT: -MDC=1; Received an active event for interface GigabitEthernet1/0/2.]{lang="EN-US"}]{#struct_0_78899_x1004_1884905934}

[*[// ASPF]{lang="EN-US"}*]{#struct_0_78899_x1004_313900369}*[收到一个接口激活事件通知]{style="font-family:宋体"}*
