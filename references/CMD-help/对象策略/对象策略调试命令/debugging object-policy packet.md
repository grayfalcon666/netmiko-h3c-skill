::: {#2012553608 .myid}
[]{#_Toc404793587}[]{#struct_0_17035_14030_x1401575625}[]{#_Toc383018331}[]{#_Toc372742484}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**对象策略 \-- 对象策略调试命令 \-- debugging object-policy packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17035_14030_x1783800706}

[**[debugging]{lang="EN-US"}**[ **object-policy** **packet** { **ip** \| **ipv6** } \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_17035_14030_x363140672}

[**[undo]{lang="EN-US"}**[ **debugging** **object-policy** **packet** { **ip** \| **ipv6** }]{lang="EN-US"}]{#struct_0_17035_14030_x302047044}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17035_14030_x1025094069}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17035_14030_58580170}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17035_14030_x714218349}

[[network-admin]{lang="EN-US"}]{#struct_0_17035_14030_x1332250930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17035_14030_x1412254702}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17035_14030_918282479}

[**[ip]{lang="EN-US"}**]{#struct_0_17035_14030_2054908005}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17035_14030_1085848607}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17035_14030_x184954478}[：表示输出指定编号]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配报文的调试信息。若未指定，则输出指定类型所有报文的调试信息。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_17035_14030_1115363254}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[：若指定]{style="font-family:宋体"}**[ip]{lang="EN-US"}**[关键字，则表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，若指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，则表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_17035_14030_x1645107340}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：若指定]{style="font-family:宋体"}**[ip]{lang="EN-US"}**[关键字，则表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，若指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，则表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17035_14030_1116340275}

[**[debugging]{lang="EN-US"}**[ **object-policy packet**]{lang="EN-US"}]{#struct_0_17035_14030_1725564231}[命令用来打开对象策略报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **object-policy packet**]{lang="EN-US"}[命令用来关闭对象策略报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，对象策略报文调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_17035_14030_x2108661551}

[[表1-1 ]{lang="EN-US"}[debugging object-policy packet]{lang="EN-US"}]{#struct_0_17035_14030_2075143230}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1397122425}[[字段]{style="font-family:黑体"}]{#struct_0_17035_14030_38706365}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17035_14030_291627180}

[[The packet is permitted]{lang="EN-US"}]{#struct_0_17035_14030_1880916935}

[[允许报文通过]{style="font-family:宋体"}]{#struct_0_17035_14030_187522944}

[[The packet is denied]{lang="EN-US"}]{#struct_0_17035_14030_x595059750}

[[丢弃报文]{style="font-family:宋体"}]{#struct_0_17035_14030_x137425974}

[[Src-Zone=*source-zone-name*(matched=Any)]{lang="EN-US"}]{#struct_0_17035_14030_288988049}

[[报文的源安全域名称]{style="font-family:宋体"}]{#struct_0_17035_14030_x349541902}

[[当报文匹配上可匹配任意源安全域的域间实例时，此处会附加显示]{style="font-family:宋体"}[(matched=Any)]{lang="EN-US"}]{#struct_0_17035_14030_x1643805238}[信息]{style="font-family:宋体"}

[[Dst-Zone=*destination-zone-name*(matched=Any)]{lang="EN-US"}]{#struct_0_17035_14030_1116274739}

[[报文的目的安全域名称]{style="font-family:宋体"}]{#struct_0_17035_14030_x1436821552}

[[当报文匹配上可匹配任意目的安全域的域间实例时，此处会附加显示]{style="font-family:宋体"}[(matched=Any)]{lang="EN-US"}]{#struct_0_17035_14030_2046083864}[信息]{style="font-family:宋体"}

[[If-In=*inbound-interface-name*(*ifIndexIn*)]{lang="EN-US"}]{#struct_0_17035_14030_x287063360}

[[入接口名称（入接口索引号）]{style="font-family:宋体"}]{#struct_0_17035_14030_x2000826519}

[[If-Out=*outbound-interface-name*(*ifIndexOut*)]{lang="EN-US"}]{#struct_0_17035_14030_x1618297359}

[[出接口名称（出接口索引号）]{style="font-family:宋体"}]{#struct_0_17035_14030_575001488}

[[VLAN-In]{lang="EN-US"}]{#struct_0_17035_14030_x9420376}

[[入]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_17035_14030_1917250438}[，该字段仅在报文转发相关接口工作在二层模式时可见]{style="font-family:宋体"}

[[VLAN-Out]{lang="EN-US"}]{#struct_0_17035_14030_1861813604}

[[出]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_17035_14030_1116995635}[，该字段仅在报文转发相关接口工作在二层模式时可见]{style="font-family:宋体"}

[[Packet Info]{lang="EN-US"}]{#struct_0_17035_14030_2072338894}

[[报文信息（该信息来自报文本身）]{style="font-family:宋体"}]{#struct_0_17035_14030_x1712356590}

[[Match Info]{lang="EN-US"}]{#struct_0_17035_14030_313659738}

[[匹配信息（该信息由设备提取自相关的会话表项，用于匹配包过滤策略）]{style="font-family:宋体"}]{#struct_0_17035_14030_x123556059}

[[Src-IP=*source-ip-address*]{lang="EN-US"}]{#struct_0_17035_14030_x1163126776}

[[报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17035_14030_1479549507}[地址]{style="font-family:宋体"}

[[Dst-IP=*destination-ip-address*]{lang="EN-US"}]{#struct_0_17035_14030_x73262351}

[[报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17035_14030_1116930099}[地址]{style="font-family:宋体"}

[[VPN-Instance=*VPN-instance-name*]{lang="EN-US"}]{#struct_0_17035_14030_1349452807}

[[报文所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_17035_14030_1091721756}[索引名称]{style="font-family:宋体"}

[[Src-Port=*source-port-number*]{lang="EN-US"}]{#struct_0_17035_14030_x1357061194}

[[报文源端口]{style="font-family:宋体"}]{#struct_0_17035_14030_388384833}

[[Dst-Port=*destination-port-number*]{lang="EN-US"}]{#struct_0_17035_14030_473286829}

[[报文目的端口]{style="font-family:宋体"}]{#struct_0_17035_14030_828416894}

[[Protocol=*protocol*(*number*)]{lang="EN-US"}]{#struct_0_17035_14030_x1447760826}

[[报文的协议类型（协议号）]{style="font-family:宋体"}]{#struct_0_17035_14030_1116471350}

[[ObjectPolicy=*policy-name*]{lang="EN-US"}]{#struct_0_17035_14030_1333497857}

[[对象策略名称]{style="font-family:宋体"}]{#struct_0_17035_14030_27375297}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17035_14030_78263613}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据报文信息输出]{style="font-family:宋体"}]{#struct_0_17035_14030_742823927}[debug]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17035_14030_x1309330544}[打开]{style="font-family:宋体"}[OBJP]{lang="EN-US"}[报文调试信息开关，使用基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[进行过滤]{style="font-family:宋体"}

[[\<Sysname\> debugging object-policy packet ip acl 2000]{lang="EN-US"}]{#struct_0_17035_14030_x289163411}

[\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Src-Zone=DMZ, Dst-Zone=TRUST; If-In=Ten-GigabitEthernet7/0/17(472), If-Out=Ten-GigabitEthernet7/0/18(473); Packet Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17035_14030_553504717}*[允许通过的]{style="font-family:宋体"}[ipv4]{lang="EN-US"}[报文信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17035_14030_x629365180}[打开]{style="font-family:宋体"}[OBJP]{lang="EN-US"}[报文调试信息开关，使用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[进行过滤]{style="font-family:宋体"}

[[\<Sysname\> debugging object-policy packet ipv6 acl 2000]{lang="EN-US"}]{#struct_0_17035_14030_x992959683}

[\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Src-Zone=DMZ, Dst-Zone=TRUST; If-In=Ten-GigabitEthernet7/0/17(472), If-Out=Ten-GigabitEthernet7/0/18(473); Packet Info: SrcIP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17035_14030_394267935}*[被丢弃的]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据数据包匹配信息输出]{style="font-family:宋体"}]{#struct_0_17035_14030_951145740}[debug]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17035_14030_1116405814}[打开]{style="font-family:宋体"}[OBJP]{lang="EN-US"}[报文调试信息开关，使用基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[进行过滤]{style="font-family:宋体"}

[[\<Sysname\> debugging object-policy packet ip acl 2000]{lang="EN-US"}]{#struct_0_17035_14030_x580296079}

[\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Src-Zone= DMZ, Dst-Zone=TRUST; Match Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17035_14030_x1640813192}*[允许通过的]{style="font-family:宋体"}[ipv4]{lang="EN-US"}[报文信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17035_14030_1920917953}[打开]{style="font-family:宋体"}[OBJP]{lang="EN-US"}[报文调试信息开关，使用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[进行过滤]{style="font-family:宋体"}

[[\<Sysname\> debugging object-policy packet ipv6 acl 2000]{lang="EN-US"}]{#struct_0_17035_14030_1835384355}

[\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Src-Zone= DMZ, Dst-Zone= TRUST; Match Info: Src-IP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17035_14030_x1973206321}*[被丢弃的]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
