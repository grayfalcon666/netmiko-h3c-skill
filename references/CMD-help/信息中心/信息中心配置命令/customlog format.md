::::: {#-1106116250 .myid}
[]{#_Toc404797442}[]{#struct_0_13409_16130_1862352287}[]{#_Toc360605553}

**信息中心 \-- 信息中心配置命令 \-- customlog format**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_914111773}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_273291959}
:::

[ ]{lang="EN-US"}

[**[customlog format]{lang="EN-US"}**]{#struct_0_13409_16130_x698009722}[命令用来设置发往日志主机的用户定制的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[日志信息的输出格式。]{style="font-family:宋体"}

[**[undo customlog format]{lang="EN-US"}**]{#struct_0_13409_16130_1862679967}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1747049657}

[**[customlog format ]{lang="EN-US"}**[{ **unicom** \| **telecom** \| **cmcc** }]{lang="EN-US"}]{#struct_0_13409_16130_288349626}

[**[undo ]{lang="EN-US"}[customlog format]{lang="EN-US"}**]{#struct_0_13409_16130_64115881}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x851535530}

[[设备不产生用户定制的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_13409_16130_1907469154}[的日志信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1862745503}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1697553010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_586807863}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1006461455}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1565562936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_1117265927}

[**[unicom]{lang="EN-US"}**]{#struct_0_13409_16130_1862548895}**[：]{style="font-family:宋体"}**[设置发往日志主机的用户定制]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[日志信息的输出格式为中国联通格式。]{style="font-family:宋体"}

[**[telecom]{lang="EN-US"}**]{#struct_0_13409_16130_1773317722}**[：]{style="font-family:宋体"}**[设置发往日志主机的用户定制]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[日志信息的输出格式为中国电信格式。]{style="font-family:宋体"}

[**[cmcc]{lang="EN-US"}**]{#struct_0_13409_16130_x877954002}**[：]{style="font-family:宋体"}**[设置发往日志主机的用户定制]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[日志信息的输出格式为中国移动格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_22795600}

[[NAT444]{lang="EN-US"}]{#struct_0_13409_16130_1690051820}[日志的相关信息请参考]{style="font-family:宋体"}[NAT]{lang="EN-US"}[手册。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1367088109}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1862614431}[设置发往日志主机的用户定制]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[日志信息的输出格式为中国联通格式。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_13409_16130_938157555}

[\[Sysname\] customlog format unicom]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_95476731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[customlog host]{lang="EN-US"}**]{#struct_0_13409_16130_x712458140}
:::::

::::: {#-1164436724 .myid}
[]{#_Toc404797443}[]{#struct_0_13409_16130_x1224706184}[]{#_Toc360605554}

**信息中心 \-- 信息中心配置命令 \-- customlog host**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1862942111}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x1429324836}
:::

[ ]{lang="EN-US"}

[**[customlog host]{lang="EN-US"}**]{#struct_0_13409_16130_34468052}[命令用来指定用户定制日志发送的日志主机并设置相关参数。]{style="font-family:宋体"}

[**[undo customlog host]{lang="EN-US"}**]{#struct_0_13409_16130_67753470}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1568566121}

[**[customlog]{lang="EN-US"}**[ **host** \[ **vpn-instance** *vpn-instance-name* \] { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* } \[ **port** *port-number* \] **export** { **cmcc-sessionlog** \| **cmcc-userlog** \| **telecom-sessionlog** \| **telecom-userlog** \| **unicom-sessionlog** \| **unicom-userlog** } \*]{lang="EN-US"}]{#struct_0_13409_16130_1058868940}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[customlog]{lang="EN-US"}**[ **host** \[ **vpn-instance** *vpn-instance-name* \] { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* } \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_13409_16130_1863007647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1835432947}

[[没有指定日志主机和相关参数。]{style="font-family:宋体"}]{#struct_0_13409_16130_1749252559}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_452680422}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1828866826}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1424640420}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x866465527}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x536844211}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1150283605}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13409_16130_1742733363}[：指定日志主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示日志主机位于公网中。]{style="font-family:宋体"}

[*[hostname]{lang="EN-US"}*]{#struct_0_13409_16130_x1498820909}[：指定日志的主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_13409_16130_x542516015}[：指定日志主机的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13409_16130_x537700981}[：指定日志主机的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_13409_16130_608028800}[：指定日志主机接收日志信息的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[514]{lang="EN-US"}[。该参数的值需要和日志主机侧的设置一致，否则日志主机接收不到日志信息。]{style="font-family:宋体"}

[**[cmcc-sessionlog]{lang="EN-US"}**]{#struct_0_13409_16130_1632089299}**[：]{style="font-family:宋体"}**[设备向指定的日志主机发送中国移动格式的基于]{style="font-family:宋体"}[session]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志。]{style="font-family:宋体"}

[**[cmcc-userlog]{lang="EN-US"}**]{#struct_0_13409_16130_x1698740912}**[：]{style="font-family:宋体"}**[设备向指定的日志主机发送中国移动格式的基于用户的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志。]{style="font-family:宋体"}

[**[telecom-sessionlog]{lang="EN-US"}**]{#struct_0_13409_16130_x866399991}**[：]{style="font-family:宋体"}**[设备向指定的日志主机发送中国电信格式的基于]{style="font-family:宋体"}[session]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志。]{style="font-family:宋体"}

[**[telecom-userlog]{lang="EN-US"}**]{#struct_0_13409_16130_x1182928721}**[：]{style="font-family:宋体"}**[设备向指定的日志主机发送中国电信格式的基于用户的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志。]{style="font-family:宋体"}

[**[unicom-sessionlog]{lang="EN-US"}**]{#struct_0_13409_16130_618924842}**[：]{style="font-family:宋体"}**[设备向指定的日志主机发送中国联通格式的基于]{style="font-family:宋体"}[session]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志。]{style="font-family:宋体"}

[**[unicom-userlog]{lang="EN-US"}**]{#struct_0_13409_16130_x1443253039}**[：]{style="font-family:宋体"}**[设备向指定的日志主机发送中国联通格式的基于用户的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_860939232}

[[用户最多可以指定]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_13409_16130_x866596599}[台不同主机同时接收设备产生的用户定制日志信息。]{style="font-family:宋体"}

[[在配置设备向指定的日志主机发送指定格式的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}]{#struct_0_13409_16130_x2068652848}[用户定制日志前，需要通过]{style="font-family:宋体"}**[customlog format]{lang="EN-US"}**[命令设置相应的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[日志输出格式，否则可以配置成功，但设备不产生相应的日志，日志主机将接收不到日志。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_375831945}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_2109623397}[配置系统向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的日志主机发送中国联通格式的基于]{style="font-family:宋体"}[session]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT444]{lang="EN-US"}[用户定制日志日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1044226825}

[\[Sysname\] customlog host 1.1.1.1 port 1000 export unicom-sessionlog unicom-userlog]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1301444492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[customlog host source]{lang="EN-US"}**]{#struct_0_13409_16130_x866531063}
:::::

::::: {#2022788933 .myid}
[]{#_Toc404797444}[]{#struct_0_13409_16130_x1657760318}[]{#_Toc360605555}

**信息中心 \-- 信息中心配置命令 \-- customlog host source**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_241880656}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_313123032}
:::

[ ]{lang="EN-US"}

[**[customlog host]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_13409_16130_x906884007}[命令用来配置发送的日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **customlog host** **source**]{lang="EN-US"}]{#struct_0_13409_16130_x866203383}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2071101845}

[**[customlog host source]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13409_16130_x501762862}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[customlog host source]{lang="EN-US"}**]{#struct_0_13409_16130_1359218768}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x343815635}

[[将根据路由来确定发送日志信息的出接口，使用该接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13409_16130_368096258}[地址作为发送的日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x866137847}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_301551866}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x714628642}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1390180282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1734256506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_838424162}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13409_16130_x866334455}[：指定发送日志信息的]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[出接口的类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1295977644}

[[配置日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13409_16130_x959383163}[地址后，不管实际使用哪个物理接口发送日志信息，日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址均为指定接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_746820701}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1642687040}[配置使用]{style="font-family:宋体"}[Loopback0]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为发送的日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x866268919}

[\[Sysname\] interface loopback 0]{lang="EN-US"}

[\[Sysname-LoopBack0\] ip address 2.2.2.2 32]{lang="EN-US"}

[\[Sysname-LoopBack0\] quit]{lang="EN-US"}

[\[Sysname\] customlog host source loopback 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_347962313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[customlog host]{lang="EN-US"}**]{#struct_0_13409_16130_x2100715165}
:::::

::::: {#1519609111 .myid}
[]{#_Toc404797445}[]{#struct_0_13409_16130_x1900642809}[]{#_Toc360605556}

**信息中心 \-- 信息中心配置命令 \-- customlog timestamp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x571159831}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x116987767}
:::

[ ]{lang="EN-US"}

[**[customlog]{lang="EN-US"}**[ **timestamp localtime**]{lang="EN-US"}]{#struct_0_13409_16130_x865941239}[命令用来设置发往日志主机的用户定制日志信息的时间戳为设备本地时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **customlog** **timestamp** **localtime**]{lang="EN-US"}]{#struct_0_13409_16130_x768305597}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1704421376}

[**[customlog]{lang="EN-US"}**[ **timestamp localtime**]{lang="EN-US"}]{#struct_0_13409_16130_x261842945}

[**[undo ]{lang="EN-US"}[customlog timestamp localtime]{lang="EN-US"}**]{#struct_0_13409_16130_829623034}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x865875703}

[[发往日志主机的用户定制日志信息的时间戳为格林威治时间。]{style="font-family:宋体"}]{#struct_0_13409_16130_x14128945}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1764108826}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_914403030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1171022174}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x686023102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x866465528}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x537171891}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_375287147}[设置发往日志主机的用户定制日志信息的时间戳系统本地时间。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_606774918}

[\[Sysname\] customlog timestamp localtime]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_217122043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[customlog host]{lang="EN-US"}**]{#struct_0_13409_16130_x866399992}
:::::

::::: {#-97264439 .myid}
[]{#_Toc276478850}[]{#_Toc264040792}[]{#_Toc72751616}[]{#_Toc404797446}[]{#struct_0_13409_16130_603301982}[]{#_Toc339625631}[]{#_Toc128041267}

**信息中心 \-- 信息中心配置命令 \-- diagnostic-logfile save**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1919952853}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x703259955}
:::

[ ]{lang="EN-US"}

[**[diagnostic-logfile]{lang="EN-US"}**[ **save**]{lang="EN-US"}]{#struct_0_13409_16130_x927790545}[命令用来手动将诊断日志文件缓冲区中的内容全部保存到诊断日志文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2038562441}

[**[diagnostic-logfile]{lang="EN-US"}**[ **save**]{lang="EN-US"}]{#struct_0_13409_16130_1575893614}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x591850219}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x309451095}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x276142588}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_535161642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_661936431}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1400129175}

[[诊断日志文件的保存路径可以通过]{style="font-family:宋体"}**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** **directory**]{lang="EN-US"}]{#struct_0_13409_16130_x1380555747}[命令设置。]{style="font-family:宋体"}

[[诊断日志文件保存成功后，诊断日志文件缓冲区中的内容会被清空。]{style="font-family:宋体"}]{#struct_0_13409_16130_351545457}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1957179499}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x591915755}[手动将诊断日志文件缓冲区中的内容保存到诊断日志文件。]{style="font-family:宋体"}

[[\<Sysname\> diagnostic-logfile save]{lang="EN-US"}]{#struct_0_13409_16130_470516821}

[The contents in the diagnostic log file buffer have been saved to the file flash:/ diagfile/diagfile.log.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_858567518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center diagnostic-logfile enable]{lang="EN-US"}**]{#struct_0_13409_16130_1261623255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center diagnostic-logfile directory]{lang="EN-US"}**]{#struct_0_13409_16130_x767577770}
:::::

::::: {#1258653932 .myid}
[]{#_Toc404797447}[]{#struct_0_13409_16130_x2023665306}[]{#_Toc339625603}

**信息中心 \-- 信息中心配置命令 \-- display diagnostic-logfile summary**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image002.png){width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_854454921}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_1638495885}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **diagnostic-logfile** **summary**]{lang="EN-US"}]{#struct_0_13409_16130_x2093167209}[命令用来显示诊断日志文件的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x591981291}

[**[display]{lang="EN-US"}**[ **diagnostic-logfile** **summary**]{lang="EN-US"}]{#struct_0_13409_16130_1231401461}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1918803962}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1873172910}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1418587983}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x142378715}

[[network-operator]{lang="EN-US"}]{#struct_0_13409_16130_1249424838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_140144871}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13409_16130_1888798781}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x592046827}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1567420808}[显示诊断日志文件配置。]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic-logfile summary]{lang="EN-US"}]{#struct_0_13409_16130_1633256594}

[  Diagnostic log file: Enabled.]{lang="EN-US"}

[  Diagnostic log file size quota: 10 MB]{lang="EN-US"}

[  Diagnostic log file directory: flash:/diagfile]{lang="EN-US"}

[  Writing frequency: 24 hour 0 min 0 sec]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display logfile summary]{lang="EN-US"}]{#struct_0_13409_16130_x1630131169}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1636064754}[[字段]{style="font-family:黑体"}]{#struct_0_13409_16130_x1580148668}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_1387546784}

[[Diagnostic log file]{lang="EN-US"}]{#struct_0_13409_16130_x592112363}

[[诊断日志文件当前的状态（]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_13409_16130_342178921}[表示已开启，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Diagnostic log file size quota]{lang="EN-US"}]{#struct_0_13409_16130_x1177205515}

[[单个诊断日志文件最大能占用的存储空间的大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}]{#struct_0_13409_16130_x1108814622}

[[Diagnostic log file directory]{lang="EN-US"}]{#struct_0_13409_16130_77049771}

[[诊断日志文件存储的路径]{style="font-family:宋体"}]{#struct_0_13409_16130_1503228225}

[[Writing frequency]{lang="EN-US"}]{#struct_0_13409_16130_x10368767}

[[系统自动保存诊断日志文件的频率]{style="font-family:宋体"}]{#struct_0_13409_16130_x592177899}

[ ]{lang="EN-US"}

::: {#-1721728658 .myid}
[]{#_Toc404797448}[]{#struct_0_13409_16130_x4154829}

**信息中心 \-- 信息中心配置命令 \-- display info-center**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **info-center**]{lang="EN-US"}]{#struct_0_13409_16130_930613930}[命令用来显示各个输出方向的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1406884678}

[**[display]{lang="EN-US"}**[ **info-center**]{lang="EN-US"}]{#struct_0_13409_16130_x874056365}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_2090319163}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1730530796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x599713810}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1660761995}

[[network-operator]{lang="EN-US"}]{#struct_0_13409_16130_x591194859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_80607240}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13409_16130_530585409}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1544428575}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_844102574}[显示各个输出方向的信息。（该命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display info-center]{lang="EN-US"}]{#struct_0_13409_16130_x591260395}

[Information Center: Enabled]{lang="EN-US"}

[Console: Enabled]{lang="EN-US"}

[Monitor: Enabled]{lang="EN-US"}

[Log host: Enabled]{lang="EN-US"}

[    IP address: 192.168.0.1, port number: 5000, host facility: local7]{lang="EN-US"}

[    IP address: 192.168.0.2, port number: 5001, host facility: local5]{lang="EN-US"}

[Log buffer: Enabled]{lang="EN-US"}

[    Max buffer size 1024, current buffer size 512,]{lang="EN-US"}

[    Current messages 0, dropped messages 0, overwritten messages 0]{lang="EN-US"}

[Log file: Enabled]{lang="EN-US"}

[Security log file: Enabled]{lang="EN-US"}

[Information timestamp format:]{lang="FR"}

[    ]{lang="FR"}[Loghost: Date]{lang="EN-US"}

[    Other output destination: Date]{lang="EN-US"}

[]{#struct_0_13409_16130_1657939323}[]{#_Toc138214778}[]{#_Toc106534823}[]{#_Toc106534487}[]{#_Toc73275852}[[表1-2 ]{lang="EN-US"}[display info-center]{lang="EN-US"}]{#_Toc73275451}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1638096658}[[字段]{style="font-family:黑体"}]{#struct_0_13409_16130_556815400}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_1842681108}

[[Information Center]{lang="EN-US"}]{#struct_0_13409_16130_442480687}

[[信息中心当前的状态（]{style="font-family:宋体"}[enabled]{lang="EN-US"}]{#struct_0_13409_16130_1021981754}[表示已开启，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Console]{lang="IT"}]{#struct_0_13409_16130_x591719146}

[[控制台方向当前的状态（]{style="font-family:宋体"}[enabled]{lang="EN-US"}]{#struct_0_13409_16130_x1828778792}[表示已开启，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Monitor]{lang="EN-US"}]{#struct_0_13409_16130_55993539}

[[监视终端方向当前的状态（]{style="font-family:宋体"}[enabled]{lang="EN-US"}]{#struct_0_13409_16130_379906718}[表示已开启，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Log host: Enabled]{lang="EN-US"}]{#struct_0_13409_16130_939312333}

[[    IP address: 192.168.0.1, port number: 5000, host facility: local7]{lang="EN-US"}]{#struct_0_13409_16130_1686837444}

[[    IP address: 192.168.0.2, port number: 5001, host facility: local5]{lang="EN-US"}]{#struct_0_13409_16130_x591784682}

[[日志主机方向的信息]{style="font-family:宋体"}]{#struct_0_13409_16130_1226045627}[（]{style="font-family:宋体"}[只有通过]{style="font-family:宋体"}**[info-center]{lang="IT"}**[ **loghost**]{lang="IT"}[命令设置后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[才有下面具体的显示内容]{style="font-family:宋体"}[），]{style="font-family:宋体"}[包括日志主机的]{style="font-family:宋体"}[IP]{lang="IT"}[地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[日志主机接收日志信息的端口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[日志主机的记录工具]{style="font-family:宋体"}

[[Log buffer: Enabled]{lang="EN-US"}]{#struct_0_13409_16130_1374279185}

[[    Max buffer size 1024, current buffer size 512,]{lang="EN-US"}]{#struct_0_13409_16130_x653714482}

[[    Current messages 0, dropped messages 0, overwritten messages 0]{lang="EN-US"}]{#struct_0_13409_16130_x745660345}

[[日志缓冲区方向的信息，包括开启状态、最大容量、当前容量、当前信息数、已丢弃的信息数、被覆盖的信息数]{style="font-family:宋体"}]{#struct_0_13409_16130_1890652563}

[[Log file]{lang="EN-US"}]{#struct_0_13409_16130_x591850218}

[[日志文件方向当前的状态（]{style="font-family:宋体"}[enabled]{lang="EN-US"}]{#struct_0_13409_16130_x309385559}[表示已开启，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Security log file]{lang="EN-US"}]{#struct_0_13409_16130_x1073072115}

[[安全日志文件方向当前的状态（]{style="font-family:宋体"}[enabled]{lang="EN-US"}]{#struct_0_13409_16130_1186705232}[表示已开启，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Information timestamp format:]{lang="FR"}]{#struct_0_13409_16130_x550912485}

[[    Loghost]{lang="FR"}[: Date]{lang="EN-US"}]{#struct_0_13409_16130_x591915754}

[[    Other output destination: Date]{lang="EN-US"}]{#struct_0_13409_16130_470582357}

[[信息时间戳设置]{style="font-family:宋体"}]{#struct_0_13409_16130_120756448}[，包括]{style="font-family:宋体"}[日志主机输出方向和非日志主机输出方向日志信息的时间戳类型]{style="font-family:宋体"}[，]{style="font-family:宋体"}[分为]{style="font-family:宋体"}[boot]{lang="FR"}[、]{style="font-family:宋体"}[date]{lang="FR"}[、]{style="font-family:宋体"}[iso]{lang="FR"}[、]{style="font-family:宋体"}[none]{lang="FR"}[和]{style="font-family:宋体"}[no-year-date]{lang="FR"}[五种]{style="font-family:宋体"}

[ ]{lang="FR"}

::: {#-1632812546 .myid}
[]{#_Toc404797449}[]{#struct_0_13409_16130_x1842350661}[]{#_Toc276478851}[]{#_Toc264537251}[]{#_Toc127779656}

**信息中心 \-- 信息中心配置命令 \-- display logbuffer**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_523763445}[命令用来显示日志缓冲区的状态和日志缓冲区记录的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1166134668}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13409_16130_x591981290}

[**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}[ \[ **reverse** \] \[ **level** *severity* \| **size** *buffersize* \| **cpu** *cpu-number* \] \*]{lang="EN-US"}]{#struct_0_13409_16130_1231335925}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13409_16130_787009081}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}[ \[ **reverse** \] \[ **level** *severity* \| **size** *buffersize* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_13409_16130_x1099752576}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13409_16130_1751635666}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}[ \[ **reverse** \] \[ **level** *severity* \| **size** *buffersize* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_13409_16130_x812261951}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x408789669}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1810560266}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1399689043}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x592046826}

[[network-operator]{lang="EN-US"}]{#struct_0_13409_16130_x1567486344}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_2079655359}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13409_16130_x273774946}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x727788278}

[**[reverse]{lang="EN-US"}**]{#struct_0_13409_16130_112240211}[：指定日志的显示顺序为从新到旧。如果不指定该参数，将先显示旧日志，最后显示最新的日志。]{style="font-family:宋体"}

[**[level]{lang="EN-US"}**[ *severity*]{lang="EN-US"}]{#struct_0_13409_16130_x1566434159}[：显示日志缓存中指定级别日志的信息，]{style="font-family:宋体"}*[severity]{lang="EN-US"}*[表示信息级别，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。不带该参数时将显示系统日志缓冲区内所有级别的日志信息。]{style="font-family:
宋体"}

[]{#struct_0_13409_16130_x1772546040}[]{#_Ref276051035}[]{#_Toc138214779}[]{#_Ref127266393}[[表1-3 ]{lang="EN-US"}[信息级别]{style="font-family:黑体"}]{#_Toc98429685}[列表]{style="font-family:黑体"}

[]{#table_struct_0_1635077426}[[数值]{style="font-family:黑体"}]{#struct_0_13409_16130_x592112362}
:::

[[信息级别]{style="font-family:黑体"}]{#struct_0_13409_16130_342244457}

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_x1591584393}

[[0]{lang="EN-US"}]{#struct_0_13409_16130_x1711191693}

[[emergency]{lang="EN-US"}]{#struct_0_13409_16130_x2022288413}

[[表示设备不可用的信息，如系统授权已到期]{style="font-family:宋体"}]{#struct_0_13409_16130_x1687137696}

[[1]{lang="EN-US"}]{#struct_0_13409_16130_336350693}

[[alert]{lang="EN-US"}]{#struct_0_13409_16130_x592177898}

[[表示设备出现重大故障，需要立刻做出反应的信息，如流量超出接口上限]{style="font-family:宋体"}]{#struct_0_13409_16130_x4089293}

[[2]{lang="EN-US"}]{#struct_0_13409_16130_1191193629}

[[critical]{lang="EN-US"}]{#struct_0_13409_16130_x410256709}

[[表示严重信息，如设备温度已经超过预警值，设备电源、风扇出现故障等]{style="font-family:宋体"}]{#struct_0_13409_16130_x1461339343}

[[3]{lang="EN-US"}]{#struct_0_13409_16130_x299842698}

[[error]{lang="EN-US"}]{#struct_0_13409_16130_x591194858}

[[表示错误信息，如接口链路状态变化，存储卡拔出等]{style="font-family:宋体"}]{#struct_0_13409_16130_80672776}

[[4]{lang="EN-US"}]{#struct_0_13409_16130_567440663}

[[warning]{lang="EN-US"}]{#struct_0_13409_16130_x408494037}

[[表示警告信息，如接口连接断开，内存耗尽告警等]{style="font-family:宋体"}]{#struct_0_13409_16130_x1417755697}

[[5]{lang="EN-US"}]{#struct_0_13409_16130_x591260394}

[[notification]{lang="EN-US"}]{#struct_0_13409_16130_1657873787}

[[表示正常出现但是重要的信息，如通过终端登录设备，设备重启等]{style="font-family:宋体"}]{#struct_0_13409_16130_x1718499777}

[[6]{lang="EN-US"}]{#struct_0_13409_16130_1372399449}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_249830323}

[[表示需要记录的通知信息，如通过命令行输入命令的记录信息，执行]{style="font-family:宋体"}**[ping]{lang="EN-US"}**]{#struct_0_13409_16130_x591719149}[命令的日志信息等]{style="font-family:宋体"}

[[7]{lang="EN-US"}]{#struct_0_13409_16130_x1828188968}

[[debugging]{lang="EN-US"}]{#struct_0_13409_16130_786268870}

[[表示调试过程产生的信息]{style="font-family:宋体"}]{#struct_0_13409_16130_991335496}

**[ ]{lang="EN-US"}**

[**[size]{lang="EN-US"}**[ *buffersize*]{lang="EN-US"}]{#struct_0_13409_16130_545912250}[：显示日志缓冲区中指定条数的最新日志。]{style="font-family:宋体"}*[buffersize]{lang="EN-US"}*[表示要显示的日志缓冲区中最新的日志信息的条数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。不带该参数时将显示系统日志缓冲区内所有的日志信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*]{#struct_0_13409_16130_2115185336}[：显示指定单板的日志缓冲区状态及日志缓冲区中记录的日志信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如不指定本参数，将显示所有单板的日志缓冲区状态及日志缓冲区中记录的日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*]{#struct_0_13409_16130_x591784685}[：显示指定成员设备的日志缓冲区状态及日志缓冲区中记录的日志信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如不指定该参数，将显示所有成员设备的日志缓冲区状态及日志缓冲区中记录的日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13409_16130_x451660754}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的日志缓冲区状态及日志缓冲区中记录的日志信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的日志缓冲区状态及日志缓冲区中记录的日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13409_16130_1225980091}[：显示指定成员设备上指定单板的日志缓冲区状态及日志缓冲区中记录的日志信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如不指定该参数，则显示所有单板的日志缓冲区状态及日志缓冲区中记录的日志信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13409_16130_x451726290}[：显示指定单板的日志缓冲区状态及日志缓冲区中记录的日志信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如不指定该参数，则显示所有单板上的日志缓冲区状态及日志缓冲区中记录的日志信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_13409_16130_x1427633776}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的日志缓冲区状态及日志缓冲区中记录的日志信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_331690690}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1116674894}[显示系统日志缓冲区的状态和缓冲区记录的日志信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer]{lang="EN-US"}]{#struct_0_13409_16130_716374983}

[Log buffer: Enabled]{lang="EN-US"}

[Max buffer size: 1024]{lang="EN-US"}

[Actual buffer size: 512]{lang="EN-US"}

[Dropped messages: 0]{lang="EN-US"}

[Overwritten messages: 718]{lang="EN-US"}

[Current messages: 512]{lang="EN-US"}

[ ]{lang="EN-US"}

[%Jun 17 15:57:09:578 2006 Sysname SYSLOG/7/SYS_RESTART:System restarted \--]{lang="EN-US"}

[[......略......]{style="font-family:宋体"}]{#struct_0_13409_16130_281086275}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x591850221}[显示系统日志缓冲区的状态和缓冲区记录的日志信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer slot 1]{lang="EN-US"}]{#struct_0_13409_16130_x308926806}

[Log buffer: Enabled]{lang="EN-US"}

[Max buffer size: 1024]{lang="EN-US"}

[Actual buffer size: 512]{lang="EN-US"}

[Dropped messages: 0]{lang="EN-US"}

[Overwritten messages: 0]{lang="EN-US"}

[Current messages: 127]{lang="EN-US"}

[ ]{lang="EN-US"}

[%Jun 19 18:03:24:55 2006 Sysname SYSLOG /7/SYS_RESTART:System restarted]{lang="EN-US"}

[[......略......]{style="font-family:宋体"}]{#struct_0_13409_16130_x1104094467}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1794201602}[显示系统日志缓冲区的状态和缓冲区记录的日志信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer chassis 0 slot 1]{lang="EN-US"}]{#struct_0_13409_16130_x591915757}

[Log buffer: Enabled]{lang="EN-US"}

[Max buffer size: 1024]{lang="EN-US"}

[Actual buffer size: 512]{lang="EN-US"}

[Dropped messages: 0]{lang="EN-US"}

[Overwritten messages: 0]{lang="EN-US"}

[Current messages: 127]{lang="EN-US"}

[ ]{lang="EN-US"}

[%Jun 19 18:03:24:55 2006 Sysname SYSLOG/7/SYS_RESTART:System restarted]{lang="EN-US"}

[[......略......]{style="font-family:宋体"}]{#struct_0_13409_16130_470647893}

[]{#struct_0_13409_16130_767145027}[[表1-4 ]{lang="EN-US"}[display logbuffer]{lang="EN-US"}]{#_Toc138214780}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1631234130}[[字段]{style="font-family:黑体"}]{#struct_0_13409_16130_657332887}

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_x1416334835}

[[Log buffer]{lang="EN-US"}]{#struct_0_13409_16130_x1743248875}

[[是否允许输出到日志缓冲区方向（]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_13409_16130_x736627702}[表示允许，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[表示不允许）]{style="font-family:宋体"}

[[Max buffer size]{lang="EN-US"}]{#struct_0_13409_16130_231048451}

[[允许的日志缓冲区可存储的最大信息条数]{style="font-family:宋体"}]{#struct_0_13409_16130_x591981293}

[[Actual buffer size]{lang="EN-US"}]{#struct_0_13409_16130_1231270389}

[[当前设置的日志缓冲区可存储的最大信息条数]{style="font-family:宋体"}]{#struct_0_13409_16130_x845671083}

[[Dropped messages]{lang="EN-US"}]{#struct_0_13409_16130_x865761741}

[[被丢弃的信息数（内存分配失败或分配日志缓冲区过小时丢失的信息数）]{style="font-family:宋体"}]{#struct_0_13409_16130_1948882430}

[[Overwritten messages]{lang="EN-US"}]{#struct_0_13409_16130_x1333175911}

[[被覆盖的信息数（如果缓冲区存储空间不足，最早收到的信息数会被新的信息覆盖掉）]{style="font-family:宋体"}]{#struct_0_13409_16130_x592046829}

[[Current messages]{lang="EN-US"}]{#struct_0_13409_16130_x1568076168}

[[当前记录的信息数]{style="font-family:宋体"}]{#struct_0_13409_16130_811847027}

[[ ]{lang="EN-US"}]{#_Toc264537252}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1558191685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_1497215054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_x85412157}

::: {#-2033474735 .myid}
[]{#_Toc404797450}[]{#struct_0_13409_16130_1598127462}[]{#_Toc276478852}

**信息中心 \-- 信息中心配置命令 \-- display logbuffer summary**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **logbuffer** **summary**]{lang="EN-US"}]{#struct_0_13409_16130_x592112365}[命令用来显示系统日志缓冲区的概要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_341785705}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13409_16130_501968849}

[**[display]{lang="EN-US"}**[ **logbuffer** **summary** \[ **level** *severity* \| **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_13409_16130_x1779918410}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13409_16130_x1307351279}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **logbuffer** **summary** \[ **level** *severity* \| **slot** *slot-number* * *\[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_13409_16130_20440351}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13409_16130_1764873703}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **logbuffer** **summary** \[ **level** *severity* \| **chassis** *chassis-number* **slot** *slot-number* * *\[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_13409_16130_805679252}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x592177901}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1959945668}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x663499724}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x370020088}

[[network-operator]{lang="EN-US"}]{#struct_0_13409_16130_x444792429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1276893123}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13409_16130_1436578291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_1734981977}

[**[level]{lang="EN-US"}**[ *severity*]{lang="EN-US"}]{#struct_0_13409_16130_x1528586403}[：显示日志缓存中指定级别日志的概要信息，]{style="font-family:宋体"}*[severity]{lang="EN-US"}*[表示信息级别，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，具体内容请参见]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)[。不带该参数时，将显示系统日志缓冲区内所有级别的日志概要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*]{#struct_0_13409_16130_x591194861}[：显示指定单板的日志缓冲区的概要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如不指定该参数，将显示所有单板的日志缓冲区概要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*]{#struct_0_13409_16130_81131531}[：显示指定成员设备的日志缓冲区的概要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如不指定该参数，将显示所有成员设备上的日志缓冲区概要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*]{#struct_0_13409_16130_x451267538}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的日志缓冲区的概要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如不指定该参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的日志缓冲区概要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13409_16130_x534210465}[：显示指定成员设备上指定单板的日志缓冲区的概要信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如不指定该参数，将显示所有单板上的日志缓冲区的概要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13409_16130_x451333074}[：显示指定单板的日志缓冲区的概要信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如不指定该参数，将显示所有单板上的日志缓冲区的概要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_13409_16130_x1427109487}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的日志缓冲区的概要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1274470890}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1231342454}[显示系统日志缓冲区的概要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer summary]{lang="EN-US"}]{#struct_0_13409_16130_x1897308350}

[EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG]{lang="EN-US"}

[    0     0     0     0    22     0     1     0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_315497825}[显示系统日志缓冲区的概要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer summary]{lang="EN-US"}]{#struct_0_13409_16130_x591260397}

[  SLOT EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG]{lang="EN-US"}

[     1     0     0     0     7     0    34    38     0]{lang="EN-US"}

[     2     0     0     0     0     0     0     0     0]{lang="EN-US"}

[     3     0     0     0     0     0     0     0     0]{lang="EN-US"}

[     4     0     0     0     0     0     0     0     0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1658070395}[显示系统日志缓冲区的概要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer summary]{lang="EN-US"}]{#struct_0_13409_16130_x1160829687}

[  SLOT EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG]{lang="EN-US"}

[     0     0     0     0     0     0     0     0     0]{lang="EN-US"}

[     1     0     0     0     0     0     0     0     0]{lang="EN-US"}

[     2     0     0     0     0     0     0     0     0]{lang="EN-US"}

[     3     0     0     0     0    16     0     1     0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_480488732}[显示系统日志缓冲区的概要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display logbuffer summary]{lang="EN-US"}]{#struct_0_13409_16130_x591719148}

[ CHASSIS  SLOT EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG]{lang="EN-US"}

[       1     0     0     0     0     1   238     0     1     0]{lang="EN-US"}

[       1     1     0     0     0     0     0     0     0     0]{lang="EN-US"}

[       1     2     0     0     0     0     1     0     0     0]{lang="EN-US"}

[       2     0     0     0     0     0     5     0     0     0]{lang="EN-US"}

[       2     1     0     0     0     0     1     0     0     0]{lang="EN-US"}

[]{#struct_0_13409_16130_x1828123432}[[表1-5 ]{lang="EN-US"}[display logbuffer summary]{lang="EN-US"}]{#_Toc138214781}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1656812114}[[字段]{style="font-family:黑体"}]{#struct_0_13409_16130_1242113167}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_x1377120482}

[[CHASSIS]{lang="EN-US"}]{#struct_0_13409_16130_1093030238}

[[IRF]{lang="EN-US"}]{#struct_0_13409_16130_x319661906}[中设备的成员编号（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[SLOT]{lang="EN-US"}]{#struct_0_13409_16130_x942318012}

[[单板所在的槽位号（分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13409_16130_x198265402}[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[SLOT]{lang="EN-US"}]{#struct_0_13409_16130_x591784684}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13409_16130_1225914555}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[EMERG]{lang="EN-US"}]{#struct_0_13409_16130_742744146}

[[emergency]{lang="EN-US"}]{#struct_0_13409_16130_x1851159029}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[ALERT]{lang="EN-US"}]{#struct_0_13409_16130_x545771689}

[[alert]{lang="EN-US"}]{#struct_0_13409_16130_x698841581}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[CRIT]{lang="EN-US"}]{#struct_0_13409_16130_x591850220}

[[critical]{lang="EN-US"}]{#struct_0_13409_16130_x308861270}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[ERROR]{lang="EN-US"}]{#struct_0_13409_16130_x1440651650}

[[error]{lang="EN-US"}]{#struct_0_13409_16130_1794492904}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[WARN]{lang="EN-US"}]{#struct_0_13409_16130_x1426952462}

[[warning]{lang="EN-US"}]{#struct_0_13409_16130_x591915756}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[NOTIF]{lang="EN-US"}]{#struct_0_13409_16130_470713429}

[[notification]{lang="EN-US"}]{#struct_0_13409_16130_x1957437190}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[INFO]{lang="EN-US"}]{#struct_0_13409_16130_x1709089820}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_x413887515}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[DEBUG]{lang="EN-US"}]{#struct_0_13409_16130_x591981292}

[[debugging]{lang="EN-US"}]{#struct_0_13409_16130_1231204853}[级别的信息数，请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)

[[ ]{lang="EN-US"}]{#_Toc264537253}

::::: {#797784079 .myid}
[]{#_Toc404797451}[]{#struct_0_13409_16130_1557545716}[]{#_Toc276478853}

**信息中心 \-- 信息中心配置命令 \-- display logfile summary**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 1 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1344527717}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_1029766189}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **logfile** **summary**]{lang="EN-US"}]{#struct_0_13409_16130_2138655297}[命令用来显示日志文件的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_510771662}

[**[display]{lang="EN-US"}**[ **logfile** **summary**]{lang="EN-US"}]{#struct_0_13409_16130_842595525}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x592046828}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1568141704}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x185383074}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_372625397}

[[network-operator]{lang="EN-US"}]{#struct_0_13409_16130_x270366485}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1807106616}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13409_16130_1917858854}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_217360632}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x592112364}[显示日志文件配置。]{style="font-family:宋体"}

[[\<Sysname\> display logfile summary]{lang="EN-US"}]{#struct_0_13409_16130_341851241}

[  Log file: Enabled.]{lang="EN-US"}

[  Log file size quota: 10 MB]{lang="EN-US"}

[  Log file directory: flash:/logfile]{lang="EN-US"}

[  Writing frequency: 0 hour 1 min 10 sec]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display logfile summary]{lang="EN-US"}]{#struct_0_13409_16130_x53996589}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1654584466}[[字段]{style="font-family:黑体"}]{#struct_0_13409_16130_x1348953097}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_1567173084}

[[Log file]{lang="EN-US"}]{#struct_0_13409_16130_x696733323}

[[是否允许输出到日志文件方向（]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_13409_16130_x1775318924}[表示已开启，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Log file size quota]{lang="EN-US"}]{#struct_0_13409_16130_x592177900}

[[单个日志文件最大能占用的存储空间的大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}]{#struct_0_13409_16130_x1959880132}

[[Log file directory]{lang="EN-US"}]{#struct_0_13409_16130_1343910345}

[[日志文件存储的路径]{style="font-family:宋体"}]{#struct_0_13409_16130_1156465331}

[[Writing frequency]{lang="EN-US"}]{#struct_0_13409_16130_x1550328441}

[[系统自动保存日志文件的频率]{style="font-family:宋体"}]{#struct_0_13409_16130_194229180}

[ ]{lang="EN-US"}

::::: {#-107519684 .myid}
[]{#_Toc404797452}[]{#struct_0_13409_16130_x591194860}[]{#_Toc276478854}

**信息中心 \-- 信息中心配置命令 \-- display security-logfile summary**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 2 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_81197067}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_976936804}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x217330398}**[summary]{lang="IT"}**[命令用来显示安全日志文件的概要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x516107707}

[**[display]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x1309129036}**[summary]{lang="IT"}**

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_784707445}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x2125244441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x591260396}

[[security-audit]{lang="EN-US"}]{#struct_0_13409_16130_1658004859}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1099095425}

[[只有配置了安全日志管理员权限的本地用户才能使用本命令。安全日志管理员的配置请参见"安全命令参考"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_13409_16130_15709824}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x108327303}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1787290842}[显示安全日志文件概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display security-logfile summary]{lang="EN-US"}]{#struct_0_13409_16130_203323319}

[  Security log file: Enabled]{lang="EN-US"}

[  Security log file size quota: 10 MB]{lang="EN-US"}

[  Security log file directory: flash:/seclog]{lang="EN-US"}

[  Alarm threshold: 80%]{lang="EN-US"}

[  Current usage: 30%]{lang="EN-US"}

[  Writing frequency: 1 hour 0 min 0 sec]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display security-logfile summary]{lang="EN-US"}]{#struct_0_13409_16130_1912896764}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1656616370}[[字段]{style="font-family:黑体"}]{#struct_0_13409_16130_155708761}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_13409_16130_x1803815724}

[[Security log file]{lang="EN-US"}]{#struct_0_13409_16130_1646341040}

[[安全日志文件当前的状态（]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_13409_16130_1787356378}[表示已开启，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[表示未开启）]{style="font-family:宋体"}

[[Security log file size quota]{lang="EN-US"}]{#struct_0_13409_16130_1386504395}

[[单个安全日志文件最大能占用的存储空间的大小]{style="font-family:宋体"}]{#struct_0_13409_16130_x1083422396}

[[Security log file directory]{lang="EN-US"}]{#struct_0_13409_16130_326137717}

[[安全日志文件存储的路径]{style="font-family:宋体"}]{#struct_0_13409_16130_x1172800735}

[[Alarm-threshold]{lang="EN-US"}]{#struct_0_13409_16130_x1800023015}

[[安全日志文件使用率告警门限]{style="font-family:宋体"}]{#struct_0_13409_16130_1787421914}

[[Current usage]{lang="EN-US"}]{#struct_0_13409_16130_578677641}

[[当前的安全日志文件使用率]{style="font-family:宋体"}]{#struct_0_13409_16130_x211660727}

[[Writing frequency]{lang="EN-US"}]{#struct_0_13409_16130_x1326001443}

[[系统自动保存安全日志文件的频率]{style="font-family:宋体"}]{#struct_0_13409_16130_x1316809733}

[[ ]{lang="EN-US"}]{#_Toc264040793}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x139914248}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization-attribute]{lang="EN-US"}**]{#struct_0_13409_16130_501682312}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

::: {#1100162152 .myid}
[]{#_Toc276478855}[]{#_Toc404797453}[]{#struct_0_13409_16130_1787487450}[]{#_Toc313433014}[]{#_Toc291661824}[]{#_Toc257709975}[]{#_Toc187302745}

**信息中心 \-- 信息中心配置命令 \-- enable log updown**

------------------------------------------------------------------------

[**[enable]{lang="EN-GB"}**]{#struct_0_13409_16130_1807471803}[ **log** **updown**]{lang="EN-GB"}[命令用来设置允许端口在状态发生改变时生成]{style="font-family:宋体"}[Link up]{lang="EN-US"}[和]{style="font-family:宋体"}[Link down]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-GB"}**]{#struct_0_13409_16130_1496029185}[ **enable** **log** **updown**]{lang="EN-GB"}[命令用来禁止端口在状态发生改变时生成]{style="font-family:宋体"}[Link up]{lang="EN-US"}[和]{style="font-family:宋体"}[Link down]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1215480014}

[**[enable]{lang="EN-US"}**[ **log** **updown**]{lang="EN-US"}]{#struct_0_13409_16130_x173860202}

[**[undo]{lang="EN-US"}**[ **enable** **log** **updown**]{lang="EN-US"}]{#struct_0_13409_16130_367002371}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x889937632}

[[允许所有端口在状态发生改变时生成端口]{style="font-family:宋体"}[Link up]{lang="EN-US"}]{#struct_0_13409_16130_x389045473}[和]{style="font-family:宋体"}[Link down]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787552986}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13409_16130_972721568}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x627444768}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1176817935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1918781450}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_428582606}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_54610487}[禁止端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在状态发生改变时生成]{style="font-family:宋体"}[Link up]{lang="EN-US"}[和]{style="font-family:宋体"}[Link down]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1787618522}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo enable log updown]{lang="EN-US"}
:::

::::: {#-727569464 .myid}
[]{#_Toc404797454}[]{#struct_0_13409_16130_x507915691}[]{#_Toc339625621}

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_152713428}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_1850368332}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1303852529}[命令用来开启诊断日志同步保存功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **diagose-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_406643870}[命令用来关闭诊断日志同步保存功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1759929739}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1341374770}

[**[undo]{lang="EN-US"}**[ **info-center** **diagnostic-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1787684058}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1005537688}

[[允许诊断日志信息输出到诊断日志文件。]{style="font-family:宋体"}]{#struct_0_13409_16130_1510965536}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1446797775}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_2114911349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_304775868}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x323166137}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_669521822}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787749594}

[[开启诊断日志同步保存功能后，系统将诊断日志进行集中处理：当生成的诊断日志时，系统会将诊断日志信息同步保存到诊断日志文件。这样既实现了诊断日志的集中管理，又有利于用户随时快捷地查看诊断日志，了解设备状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_x2075900198}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x699680792}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1969478033}[开启诊断日志同步保存功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_2077312642}

[\[Sysname\] info-center diagnostic-logfile enable]{lang="EN-US"}
:::::

::::: {#676628130 .myid}
[]{#_Toc404797455}[]{#struct_0_13409_16130_1512771861}[]{#_Toc339625622}

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile frequency**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_574328866}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_56416229}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_1786766554}[命令用来设置设备自动保存诊断日志文件的频率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **diagnostic-logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_2125750337}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1689508031}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** **frequency** *freq-sec*]{lang="EN-US"}]{#struct_0_13409_16130_1215911551}

[**[undo]{lang="EN-US"}**[ **info-center** **diagnostic-logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_1925484392}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_807690487}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13409_16130_1507992104}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1318336908}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1761874306}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1786832090}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1000639804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1004223771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x22171758}

[*[freq-sec]{lang="EN-US"}*]{#struct_0_13409_16130_x1724740376}[：系统自动保存诊断日志文件的频率，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，不同设备支持的缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_658925823}

[[设置设备自动保存诊断日志文件的频率后，诊断日志会先被输出到诊断日志文件缓冲区（]{style="font-family:宋体"}[diagnostic-logfile buffer]{lang="EN-US"}]{#struct_0_13409_16130_x566577965}[），系统会按照配置中指定的频率将诊断日志文件缓冲区的内容写入诊断日志文件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1654083943}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1490274115}[设置诊断日志自动保存到文件的频率为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1787290843}

[\[Sysname\] info-center diagnostic-logfile frequency 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_203257783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center ]{lang="EN-US"}**]{#struct_0_13409_16130_x396055831}**[diagnostic]{lang="EN-US"}[-logfile enable]{lang="EN-US"}**
:::::

::::: {#1549314801 .myid}
[]{#_Toc404797456}[]{#struct_0_13409_16130_1833141011}[]{#_Toc339625623}

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile quota**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x712073118}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x1182501912}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="IT"}**]{#struct_0_13409_16130_1685568845}[ **diagnostic-logfile** **quota**]{lang="IT"}[命令用来设置单个诊断日志文件最大能占用的存储空间的大小。]{style="font-family:
宋体"}

[**[undo]{lang="IT"}**]{#struct_0_13409_16130_1027723762}[ **info-center** **diagnostic-logfile** **quota**]{lang="IT"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787356379}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_1386438859}**[quota]{lang="IT"}**[ *size*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_13409_16130_563794449}[ **info-center** **diagnostic-logfile** **quota**]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1449447270}

[[本命令的缺省情况与设备的型号有关]{style="font-family:宋体"}]{#struct_0_13409_16130_x1186947978}[，]{style="font-family:
宋体"}[请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1572396405}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x479114541}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1031787620}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1787421915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_578743177}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2103256173}

[*[size]{lang="IT"}*]{#struct_0_13409_16130_1435130394}[：]{style="font-family:宋体"}[单个诊断日志文件可使用的存储空间的最大值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[单位为]{style="font-family:宋体"}[MB]{lang="IT"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x452651787}

[[\# ]{lang="IT"}]{#struct_0_13409_16130_x589857224}[设置单个诊断日志文件最大能占用的存储空间的大小为]{style="font-family:宋体"}[6MB]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x614423744}

[[\[Sysname\] info-center diagnostic-logfile quota 6]{lang="EN-US"}]{#struct_0_13409_16130_x300780337}
:::::

::::: {#-1447036953 .myid}
[]{#_Toc404797457}[]{#struct_0_13409_16130_1787487451}[]{#_Toc339625624}

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile directory**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1807537339}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x1584299753}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x786430857}**[directory]{lang="IT"}**[命令用来修改存储诊断日志文件的路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_634406126}

[**[info-center]{lang="EN-US"}**[ **diagnostic-logfile** **directory** *dir-name*]{lang="EN-US"}]{#struct_0_13409_16130_1420663530}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_61772140}

[[存储诊断日志文件路径为存储设备根目录下的]{style="font-family:宋体"}[diagfile]{lang="EN-US"}]{#struct_0_13409_16130_x879364401}[文件夹。对于支持]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡分区的设备，存储诊断日志文件目录与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x152578934}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1787552987}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_972656032}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_2042450278}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x471189544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1507268475}

[*[dir-name]{lang="EN-US"}*]{#struct_0_13409_16130_572143366}[：诊断日志文件存储的路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1477017290}

[[在执行该配置前，存储诊断日志文件的文件夹必须为当前已创建的目录。]{style="font-family:宋体"}]{#struct_0_13409_16130_1087659898}

[[配置时，请注意：]{style="font-family:宋体"}]{#struct_0_13409_16130_1787618523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在设备重启后失效（集中式设备）。]{style="font-family:宋体"}]{#struct_0_13409_16130_x507981227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在设备重启或主备倒换后失效（分布式设备－独立运行模式）。]{style="font-family:宋体"}]{#struct_0_13409_16130_x1425709469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13409_16130_548250225}[重启或]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Slave]{lang="EN-US"}[倒换后失效（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在]{style="font-family:宋体"}]{#struct_0_13409_16130_1207467426}[IRF]{lang="EN-US"}[重启或全局主用主控板和全局备用主控板主备倒换后失效（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x273514183}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_805426388}[设置存放诊断日志文件的目录为]{style="font-family:宋体"}[flash:/test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir test]{lang="EN-US"}]{#struct_0_13409_16130_1787684059}

[Creating directory flash:/test\... Done.]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] info-center diagnostic-logfile directory flash:/test]{lang="EN-US"}
:::::

::: {#-78093409 .myid}
[]{#_Toc404797458}[]{#struct_0_13409_16130_1005603224}[]{#_Toc354844509}

**信息中心 \-- 信息中心配置命令 \-- info-center logfile overwrite-protection**

------------------------------------------------------------------------

[**[info-center logfile overwrite-protection]{lang="EN-US"}**]{#struct_0_13409_16130_x1572163829}[命令用来开启日志文件的写满保护功能。如果日志文件已经达到限额或空间不足，不允许覆盖写入新的日志。]{style="font-family:宋体"}

[**[undo info-center logfile overwrite-protection]{lang="EN-US"}**]{#struct_0_13409_16130_688011494}[命令用来关闭日志文件的写满保护功能。如果日志文件已经达到限额或空间不足，则允许覆盖写入新的日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1349463036}

[**[info-center logfile overwrite-protection]{lang="EN-US"}**[ \[ **all-port-powerdown** \]]{lang="EN-US"}]{#struct_0_13409_16130_x2001613128}

[**[undo info-center logfile overwrite-protection]{lang="EN-US"}**]{#struct_0_13409_16130_x1414565468}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787749595}

[[日志文件的写满保护功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_x2075834662}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x659678452}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1553700775}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1206115160}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1996610629}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1256282217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_57031708}

[**[all-port-powerdown]{lang="EN-US"}**]{#struct_0_13409_16130_x1445260374}[：表示]{style="font-family:宋体"}[如果日志文件已经达到限额或空间不足，则关闭所有的业务接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1786766555}

[[本命令仅]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_13409_16130_2125815873}[模式下支持。]{style="font-family:宋体"}

[[日志文件的写满保护功能处于关闭状态：]{style="font-family:宋体"}]{#struct_0_13409_16130_699946094}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持单个日志文件的设备：当存储介质的空间达到设备支持的最大值，新产生的日志会从日志文件开头覆盖写入。此后如果用户先开启，再关闭日志写满保护功能，日志从日志文件开头覆盖写入，此时覆盖的有可能不是最旧的日志。]{style="font-family:宋体"}]{#struct_0_13409_16130_678378152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持多个日志文件的设备：当日志文件的个数达到设备支持的最大值或者设备可用存储介质的空间不足时，系统会删除最旧的日志文件再创建新的日志文件。]{style="font-family:宋体"}]{#struct_0_13409_16130_699749486}

[[日志文件的写满保护功能处于开启状态，日志将从当前日志文件的尾部开始进行记录。在记录日志的过程中，如果日志文件的个数达到设备支持的最大值或者设备可用存储介质的空间不足，不再覆盖旧日志或删除最旧的日志文件，而是停止记录日志文件。]{style="font-family:宋体"}]{#struct_0_13409_16130_x2017618848}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x375033263}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x315787724}[开启日志文件的写满保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1786832091}

[\[Sysname\] info-center logfile overwrite-protection]{lang="EN-US"}
:::

::: {#1954517010 .myid}
[]{#_Toc404797459}[]{#struct_0_13409_16130_1000574268}

**信息中心 \-- 信息中心配置命令 \-- info-center enable**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1383331245}[命令用来开启信息中心功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_748612652}[命令用来关闭信息中心功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1804646651}

[**[info-center]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1635371726}

[**[undo]{lang="EN-US"}**[ **info-center** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x480805108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_527010933}

[[信息中心处于开启状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_x1363146128}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787290840}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_203454391}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_243170647}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x955900086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1799222006}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x601788488}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x622225820}[开启信息中心功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x2109955358}

[\[Sysname\] info-center enable]{lang="EN-US"}

[Information center is enabled.]{lang="EN-US"}
:::

::: {#-888046713 .myid}
[]{#_Toc404797460}[]{#struct_0_13409_16130_1787356376}[]{#_Toc330997218}[]{#_Toc257709979}[]{#_Toc185927308}[]{#_Toc123026768}

**信息中心 \-- 信息中心配置命令 \-- info-center format**

------------------------------------------------------------------------

[**[info-center format]{lang="EN-US"}**]{#struct_0_13409_16130_1386635467}[命令用来设置发往日志主机的日志信息的输出格式。]{style="font-family:宋体"}

[**[undo info-center format]{lang="EN-US"}**]{#struct_0_13409_16130_x322060751}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1048182895}

[**[info-center format { unicom \| cmcc }]{lang="EN-US"}**]{#struct_0_13409_16130_640768634}

[**[undo info-center format]{lang="EN-US"}**]{#struct_0_13409_16130_x822219151}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1070668324}

[[发往日志主机的日志信息的格式为非定制格式。]{style="font-family:宋体"}]{#struct_0_13409_16130_1498386411}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_508183047}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1787421912}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_578284425}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_39729006}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x596630271}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x293919127}

[**[unicom]{lang="EN-US"}**]{#struct_0_13409_16130_x1203827435}**[：]{style="font-family:宋体"}**[设置发往日志主机的日志信息的输出格式为中国联通格式。]{style="font-family:宋体"}

[**[cmcc]{lang="EN-US"}**]{#struct_0_13409_16130_x1141302605}**[：]{style="font-family:宋体"}**[设置发往日志主机的日志信息的输出格式为中国移动格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_862734548}

[[发往日志主机的日志信息有三种格式：非定制格式、中国联通格式和中国移动格式。有关日志信息格式的详细介绍请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}]{#struct_0_13409_16130_x24514560}[]{#_Toc223770295}[]{#_Toc123194244}[]{#_Toc123194228}[信息中心"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787487448}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1806947514}[设置发往日志主机的日志信息的格式为中国联通格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x848396139}

[\[Sysname\] info-center format unicom]{lang="EN-US"}
:::

::: {#359355723 .myid}
[]{#_Toc404797461}[]{#struct_0_13409_16130_x339782322}[]{#_Toc276478856}[]{#_Toc263079897}[]{#_Toc72751620}

**信息中心 \-- 信息中心配置命令 \-- info-center logbuffer**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_1498401774}[命令用来允许日志信息输出到日志缓冲区。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_x1403788405}[命令用来禁止日志信息输出日志缓冲区。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1968051051}

[**[info-center]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_x1276000150}

[**[undo]{lang="EN-US"}**[ **info-center** **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_1787552984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_972852640}

[[允许日志信息输出到日志缓冲区。]{style="font-family:宋体"}]{#struct_0_13409_16130_x1999280082}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1439825197}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x726545133}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_2071044968}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x854983944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1839950567}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1520822581}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1787618520}[配置允许日志信息输出到日志缓冲区。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x507784619}

[\[Sysname\] info-center logbuffer]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1701168111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_1893910689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_13409_16130_954292110}
:::

::: {#2036864726 .myid}
[]{#_Toc404797462}[]{#struct_0_13409_16130_x563816607}

**信息中心 \-- 信息中心配置命令 \-- info-center logbuffer size**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **logbuffer** **size**]{lang="EN-US"}]{#struct_0_13409_16130_x1266688663}[命令用来配置日志缓冲区可存储的信息条数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **logbuffer** **size**]{lang="EN-US"}]{#struct_0_13409_16130_1875933681}[命令用来恢复日志缓冲区可存储的信息条数为默认值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1309583491}

[**[info-center]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}[ **size** *buffersize*]{lang="EN-US"}]{#struct_0_13409_16130_1787684056}

[**[undo]{lang="EN-US"}**[ **info-center** **logbuffer** **size**]{lang="EN-US"}]{#struct_0_13409_16130_1005930904}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1194992323}

[[日志缓冲区可存储]{style="font-family:宋体"}[512]{lang="EN-US"}]{#struct_0_13409_16130_113471054}[条信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x394980162}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1522280068}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1079364573}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1256226473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1787749592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2076031270}

[*[buffersize]{lang="EN-US"}*]{#struct_0_13409_16130_2088055347}[：日志缓冲区可存储的信息条数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[512]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1820832252}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_450042897}[配置日志缓冲区可存储的信息条数为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_126006343}

[\[Sysname\] info-center logbuffer size 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1584378270}[恢复日志缓冲区可存储的信息条数为]{style="font-family:宋体"}[512]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1317130941}

[\[Sysname\] undo info-center logbuffer size]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1786766552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_2125881409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x536110350}
:::

::::: {#654942288 .myid}
[]{#_Toc404797463}[]{#struct_0_13409_16130_x796073462}[]{#_Toc276478857}[]{#_Toc264123592}[]{#_Toc264120166}

**信息中心 \-- 信息中心配置命令 \-- info-center logfile enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 3 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_333956973}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_1511603518}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1652250862}[命令用来允许日志信息输出到日志文件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1645288669}[命令用来禁止日志信息输出到日志文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_2059188989}

[**[info-center]{lang="EN-US"}**[ **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1786832088}

[**[undo]{lang="EN-US"}**[ **info-center** **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1001164091}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1743849936}

[[允许日志信息输出到日志文件。]{style="font-family:宋体"}]{#struct_0_13409_16130_1836738726}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1324071316}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x256137094}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1065827902}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x716051368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_902520091}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787290841}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_203388855}[配置允许日志信息输出到日志文件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_289778799}

[\[Sysname\] info-center logfile enable]{lang="EN-US"}
:::::

::::: {#-355005467 .myid}
[]{#_Toc404797464}[]{#struct_0_13409_16130_x1254375265}[]{#_Toc276478858}[]{#_Toc264123593}[]{#_Toc264120167}[]{#_Toc300306397}[]{#_Toc300306398}[]{#_Toc300306399}

**信息中心 \-- 信息中心配置命令 \-- info-center logfile frequency**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 4 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x249890396}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x1042935335}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_x1481089310}[命令用来设置系统自动保存日志文件的频率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_1787356377}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1386569931}

[**[info-center]{lang="EN-US"}**[ **logfile** **frequency** ]{lang="EN-US"}*[freq-sec]{lang="EN-US"}*]{#struct_0_13409_16130_1350977169}

[**[undo]{lang="EN-US"}**[ **info-center** **logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_255062959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1098888955}

[[系统自动保存日志文件的频率与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13409_16130_41785327}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1036317216}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x947449364}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1120217799}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1787421913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_578349961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_894580405}

[*[freq-sec]{lang="EN-US"}*]{#struct_0_13409_16130_x1827304448}[：系统自动保存日志文件的频率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，不同设备支持的缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1586857854}

[[设置系统自动保存日志文件的频率后，系统会按照指定的频率将日志文件缓冲区的内容写入日志文件。]{style="font-family:宋体"}]{#struct_0_13409_16130_x868683439}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x646807724}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1990904524}[设置设备自动保存日志文件的频率为]{style="font-family:宋体"}[60000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x1091687952}

[\[Sysname\] info-center logfile frequency 60000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787487449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1807013050}
:::::

::::: {#-599577767 .myid}
[]{#_Toc404797465}[]{#struct_0_13409_16130_x1185173678}[]{#_Toc276478859}[]{#_Toc264123594}[]{#_Toc264120168}

**信息中心 \-- 信息中心配置命令 \-- info-center logfile size-quota**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 5 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1895135908}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_859027039}
:::

**[ ]{lang="EN-US"}**

[**[info-center]{lang="EN-US"}**[ **logfile** **size-quota**]{lang="EN-US"}]{#struct_0_13409_16130_486503038}[命令用来设置单个日志文件最大能占用的存储空间的大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **logfile** **size-quota**]{lang="EN-US"}]{#struct_0_13409_16130_x1532739887}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1141613186}

[**[info-center]{lang="IT"}**]{#struct_0_13409_16130_x1314402559}[ **logfile** **size-quota**]{lang="IT"}[ *size*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_13409_16130_1787552985}[ **info-center** **logfile** **size-quota**]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_972787104}

[[单个日志文件最大能占用的存储空间的大小与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13409_16130_x1462778098}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1982409815}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_556779355}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_465412418}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_315440456}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1294224041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787618521}

[*[size]{lang="EN-US"}*]{#struct_0_13409_16130_x507850155}[：单个日志文件可使用的存储空间的最大值，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1789529630}

[[当日志文件的大小达到设置的最大值时：]{style="font-family:宋体"}]{#struct_0_13409_16130_x685317211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于只支持单个日志文件的设备，系统会使用最新日志覆盖最旧日志；]{style="font-family:宋体"}]{#struct_0_13409_16130_x1417764232}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持多个日志文件的设备，系统会自动创建新的日志文件来保存新信息，日志文件的名称为]{style="font-family:宋体"}]{#struct_0_13409_16130_x1523277044}[logfile1.log]{lang="EN-US"}[、]{style="font-family:宋体"}[logfile2.log]{lang="EN-US"}[、......。当日志文件的个数达到设备支持的最大值或者设备可用存储介质的空间不足时，系统会删除最旧的日志文件再创建新的日志文件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_499877256}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1112693467}[设置单个日志文件最大能占用的存储空间的大小为]{style="font-family:宋体"}[6MB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1787684057}

[\[Sysname\] info-center logfile size-quota 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1005996440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1612706819}
:::::

::::: {#1493164393 .myid}
[]{#_Toc404797466}[]{#struct_0_13409_16130_x992038760}[]{#_Toc276478860}[]{#_Toc264123595}

**信息中心 \-- 信息中心配置命令 \-- info-center logfile directory**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 6 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1177649255}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_2107775821}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **logfile** **directory**]{lang="EN-US"}]{#struct_0_13409_16130_x1184735661}[命令用来设置存储日志文件的目录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x362593944}

[**[info-center]{lang="EN-US"}**[ **logfile** **directory**]{lang="EN-US"}[ *dir-name*]{lang="EN-US"}]{#struct_0_13409_16130_x1092976902}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787749593}

[[存储日志文件的目录与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13409_16130_x2075965734}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1656157556}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1756755127}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1924980134}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1945292104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x774445895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2131861416}

[*[dir-name]{lang="EN-US"}*]{#struct_0_13409_16130_x856001985}[：存储日志文件的路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1786766553}

[[在执行该配置前，存储日志文件的目录必须为当前已创建的目录。]{style="font-family:宋体"}]{#struct_0_13409_16130_2125946945}

[[生成的日志文件的后缀名为]{style="font-family:宋体"}[.log]{lang="EN-US"}]{#struct_0_13409_16130_x462668580}[，当缺省的存储器已满时，可以设置一个新的目录来存放新的日志信息。]{style="font-family:宋体"}

[[配置时，请注意：]{style="font-family:宋体"}]{#struct_0_13409_16130_x188056394}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在设备重启后失效（集中式设备）。]{style="font-family:宋体"}]{#struct_0_13409_16130_2009279795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在设备重启或主备倒换后失效（分布式设备－独立运行模式）。]{style="font-family:宋体"}]{#struct_0_13409_16130_1988898979}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在]{style="font-family:宋体"}]{#struct_0_13409_16130_x1363553897}[IRF]{lang="EN-US"}[重启或主从设备倒换后失效（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在]{style="font-family:宋体"}]{#struct_0_13409_16130_x1441811356}[IRF]{lang="EN-US"}[重启或全局主用主控板和全局备用主控板主备倒换后失效（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1786832089}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1001098555}[在根目录]{style="font-family:宋体"}[flash:]{lang="EN-US"}[下创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir test]{lang="EN-US"}]{#struct_0_13409_16130_1766901957}

[Creating directory flash:/test\... Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1983920318}[设置存放日志文件的目录为]{style="font-family:宋体"}[flash:/test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1269461162}

[\[Sysname\] info-center logfile directory flash:/test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1036044257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x672841038}
:::::

::: {#-1824120872 .myid}
[]{#_Toc404797467}[]{#struct_0_13409_16130_1325305450}[]{#_Toc276478861}

**信息中心 \-- 信息中心配置命令 \-- info-center logging suppress duplicates**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **logging** **suppress** **duplicates**]{lang="EN-US"}]{#struct_0_13409_16130_1787290838}[命令用来开启抑制重复日志输出功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **logging** **suppress** **duplicate**]{lang="EN-US"}]{#struct_0_13409_16130_202930098}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_545203908}

[**[info-center]{lang="EN-US"}**[ **logging** **suppress** **duplicates**]{lang="EN-US"}]{#struct_0_13409_16130_2093171794}

[**[undo]{lang="EN-US"}**[ **info-center** **logging** **suppress** **duplicates**]{lang="EN-US"}]{#struct_0_13409_16130_x335947977}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2012904158}

[[抑制重复日志输出功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_661275336}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x564950843}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1415848356}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787356374}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1386766539}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1860345782}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1928672325}

[[当设备持续向某个方向发送同一条日志信息时（发送间隔小于]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_13409_16130_x317055790}[秒），大量重复的信息会浪费设备资源和网络资源，并导致有用的信息被淹没，不利于设备的维护。为了避免此问题，可开启重复日志抑制功能。]{style="font-family:宋体"}

[[开启重复日志抑制功能后，设备每产生一条新日志信息，在输出该日志信息的同时会启动该日志的抑制周期：]{style="font-family:宋体"}]{#struct_0_13409_16130_x1893322879}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该日志抑制周期内：如果设备后续连续生成的日志信息均与该日志信息相同（要求日志信息的如下字段均完全相同：模块名、信息等级、日志助记符、定位信息和信息文本），则系统会认为后续生成的日志是该日志的相同日志，后续生成的日志信息不再输出。]{style="font-family:宋体"}]{#struct_0_13409_16130_x1684081799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该日志抑制周期结束后：如果设备后续仍连续生成该日志，系统输出被抑制的日志信息以及被抑制的数量，并启动下一个日志抑制周期。日志信息的第一个抑制周期为]{style="font-family:宋体"}]{#struct_0_13409_16130_x641811681}[30]{lang="EN-US"}[秒，第二个抑制周期为]{style="font-family:宋体"}[2]{lang="EN-US"}[分钟，以后的抑制周期都是]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在日志抑制周期内有其它新日志信息产生：系统会先输出被抑制的日志信息以及被抑制的数量，再输出新的日志信息，并开始新日志的抑制周期。]{style="font-family:宋体"}]{#struct_0_13409_16130_1590265460}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787421910}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_578415497}[开启抑制重复日志输出功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[假设设备上]{style="font-family:宋体"}]{#struct_0_13409_16130_732313783}[Vlan-interface100]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和网络中某设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突，设备会频繁输出如下日志信息。]{style="font-family:宋体"}

[[%Jan  1 07:27:48:636 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}]{#struct_0_13409_16130_x101407325}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启抑制重复日志输出功能。]{style="font-family:宋体"}]{#struct_0_13409_16130_1964461877}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_624478176}

[\[Sysname\] info-center logging suppress duplicates]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备会继续输出如下日志。]{style="font-family:宋体"}]{#struct_0_13409_16130_417176035}

[[%Jan  1 07:27:48:636 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}]{#struct_0_13409_16130_1787487446}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[%Jan  1 07:28:19:639 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[ This message repeated 4 times in last 30 seconds.]{lang="EN-US"}

[[以上显示信息表明：开启开启抑制重复日志输出功能后，设备生成了一条]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13409_16130_1807340730}[地址冲突的日志，第一个抑制周期为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[%Jan  1 07:30:19:643 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}]{#struct_0_13409_16130_x1954864112}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[ This message repeated 20 times in last 2 minutes.]{lang="EN-US"}

[[以上显示信息表明抑制周期延长为]{style="font-family:宋体"}[120]{lang="EN-US"}]{#struct_0_13409_16130_297533500}[秒。]{style="font-family:宋体"}

[[%Jan  1 07:30:20:541 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}]{#struct_0_13409_16130_1118799284}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[ This message repeated 1 times in last 1 second.]{lang="EN-US"}

[%Jan  1 07:30:19:542 2000 Sysname CFGMAN/5/CFGMAN_CFGCHANGED: -EventIndex=\[12\]-CommandSource=\[2\]-ConfigSource=\[4\]-ConfigDestination=\[2\]; Configuration is changed.]{lang="EN-US"}

[[以上显示信息表明在抑制周期内有新的日志产生。]{style="font-family:宋体"}]{#struct_0_13409_16130_x828230407}

[[%Jan  1 07:30:24:643 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}]{#struct_0_13409_16130_1787552982}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[%Jan  1 07:30:55:645 2000 Sysname ARP/6/DUPIFIP:]{lang="EN-US"}

[Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d]{lang="EN-US"}

[ This message repeated 4 times in last 30 seconds.]{lang="EN-US"}

[[以上显示信息表明开始新一轮抑制。]{style="font-family:宋体"}]{#struct_0_13409_16130_972983712}
:::

::: {#-2108160874 .myid}
[]{#_Toc404797468}[]{#struct_0_13409_16130_x62530090}[]{#_Toc276478862}[]{#_Toc72751621}

**信息中心 \-- 信息中心配置命令 \-- info-center loghost**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **loghost**]{lang="EN-US"}]{#struct_0_13409_16130_487391510}[命令用来指定日志主机并设置相关输出参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **loghost**]{lang="EN-US"}]{#struct_0_13409_16130_x1277854580}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1961111763}

[**[info-center]{lang="EN-US"}**[ **loghost** \[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}[{ *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* } \[ **port** *port-number* \] \[ **facility** *local-number* \]]{lang="EN-US"}]{#struct_0_13409_16130_x312752054}

[**[undo]{lang="EN-US"}**[ **info**]{lang="EN-US"}**[-center]{lang="EN-US"}**[ **loghost**]{lang="EN-US"}[ \[ **vpn-instance** *vpn-instance-name* \] { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_13409_16130_x486479481}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1787618518}

[[没有指定日志主机和相关参数。]{style="font-family:宋体"}]{#struct_0_13409_16130_x507260328}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_2133061821}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1350669313}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x570731253}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_597790217}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_611847213}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1178599959}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13409_16130_x2036315468}[：指定日志主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示日志主机位于公网中。]{style="font-family:宋体"}

[*[hostname]{lang="EN-US"}*]{#struct_0_13409_16130_1338859012}[：指定日志的主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_13409_16130_1787684054}[：指定日志主机的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13409_16130_1005799832}[：指定日志主机的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_13409_16130_x1984283393}[：指定日志主机接收日志信息的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[514]{lang="EN-US"}[。该参数的值需要和日志主机侧的设置一致，否则日志主机接收不到日志信息。]{style="font-family:宋体"}

[**[facility]{lang="EN-US"}**[ ]{lang="EN-US"}*[local]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_13409_16130_x94736028}[：设置日志主机的记录工具。取值范围为]{style="font-family:宋体"}[local0]{lang="EN-US"}[～]{style="font-family:宋体"}[local7]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[local7]{lang="EN-US"}[。主要用于在日志主机端标志不同的日志来源，查找、过滤对应日志源的日志。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_379392245}

[[用户只有使用]{style="font-family:宋体"}**[info-center]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x974035480}[命令开启了信息中心功能，配置]{style="font-family:宋体"}**[info-center]{lang="EN-US"}**[ **loghost**]{lang="EN-US"}[命令才会生效。]{style="font-family:宋体"}

[[用户最多可以指定]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_13409_16130_1100504932}[台不同主机同时接收设备产生的日志信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1915423310}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1687874112}[配置系统向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的日志主机发送日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_1787749590}

[\[Sysname\] info-center loghost 1.1.1.1]{lang="EN-US"}
:::

::: {#1721571836 .myid}
[]{#_Toc404797469}[]{#struct_0_13409_16130_x2076162342}[]{#_Toc276478863}

**信息中心 \-- 信息中心配置命令 \-- info-center loghost source**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **loghost** **source**]{lang="EN-US"}]{#struct_0_13409_16130_109317273}[命令用来配置发送的日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **loghost** **source**]{lang="EN-US"}]{#struct_0_13409_16130_1231449943}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x836811568}

[**[info-center]{lang="EN-US"}**[ **loghost** **source** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13409_16130_x2138673542}

[**[undo]{lang="EN-US"}**[ **info-center** **loghost** **source**]{lang="EN-US"}]{#struct_0_13409_16130_2059332914}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_401092278}

[[将根据路由来确定发送日志信息的出接口，使用该接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13409_16130_1786766550}[地址作为发送的日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_2126012481}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1686835341}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1571798388}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x2134339627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1263916386}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x857797661}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13409_16130_x768949651}[：指定发送日志信息的]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[出接口的类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_588050790}

[[配置日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13409_16130_1786832086}[地址后，不管实际使用哪个物理接口发送日志信息，日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址均为指定接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[用户只有使用]{style="font-family:宋体"}**[info-center enable]{lang="EN-US"}**]{#struct_0_13409_16130_1001033019}[命令开启了信息中心功能，配置]{style="font-family:宋体"}**[info-center loghost source]{lang="EN-US"}**[命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1797828430}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1158106417}[配置使用]{style="font-family:宋体"}[Loopback0]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为发送的日志信息的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_292940812}

[\[Sysname\] interface loopback 0]{lang="EN-US"}

[\[Sysname-LoopBack0\] ip address 2.2.2.2 32]{lang="EN-US"}

[\[Sysname-LoopBack0\] quit]{lang="EN-US"}

[\[Sysname\] info-center loghost source loopback 0]{lang="EN-US"}
:::

::::: {#-1099027211 .myid}
[]{#_Toc404797470}[]{#struct_0_13409_16130_x335950659}[]{#_Toc276478864}[]{#_Toc264548156}[]{#_Toc263079904}[]{#_Toc245283984}

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile alarm-threshold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 7 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x1703025931}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_1787290839}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_202864562}**[alarm-threshold]{lang="IT"}**[命令用来设置安全日志文件使用率的告警门限。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x181876274}**[alarm-threshold]{lang="IT"}**[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x177787231}

[**[info-center]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_1649035692}**[alarm-threshold]{lang="IT"}**[ *usage*]{lang="IT"}

[**[undo]{lang="EN-US"}**[ **info-center** **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_670492157}**[alarm-threshold]{lang="IT"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_881884073}

[[安全日志文件使用率的告警门限是]{style="font-family:宋体"}[80]{lang="EN-US"}]{#struct_0_13409_16130_x453435467}[（即当安全日志文件使用率达到]{style="font-family:宋体"}[80]{lang="EN-US"}[％时，系统会提醒用户）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_958638984}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1787356375}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1386701003}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_893709228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1147004958}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_14699570}

[*[usage]{lang="IT"}*]{#struct_0_13409_16130_x1990429627}[：安全日志文件使用率的告警门限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[的整数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1923047329}

[[当安全日志文件大小达到上限时，新的安全日志会覆盖旧的安全日志，从而导致安全日志丢失。为防止这种情况发生，用户可以使用本命令设置安全日志文件使用率的告警门限。当使用率超过此门限值时，系统会发出日志提醒用户，此时，用户可以将安全日志文件进行备份，以防重要历史数据丢失。]{style="font-family:宋体"}]{#struct_0_13409_16130_x454046857}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x270125570}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1787421911}[设置当安全日志文件使用率达到]{style="font-family:宋体"}[90%]{lang="EN-US"}[时进行告警。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_578481033}

[\[Sysname\] info-center security-logfile alarm-threshold 90]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x437623544}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="IT"}**]{#struct_0_13409_16130_1399019380}[ **security-logfile** **size-quota**]{lang="IT"}
:::::

::::: {#-1988571595 .myid}
[]{#_Toc404797471}[]{#struct_0_13409_16130_97861426}[]{#_Toc276478865}[]{#_Toc264548152}[]{#_Toc264547787}

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 8 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x1920696472}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x1836015727}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **security-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1519339598}[命令用来开启安全日志同步保存功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **security-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1787487447}[命令用来关闭安全日志同步保存功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1807406266}

[**[info-center]{lang="EN-US"}**[ **security-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1977021286}

[**[undo]{lang="EN-US"}**[ **info-center** **security-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_894476650}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x675110470}

[[安全日志同步保存功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_1565524472}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1768348271}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1255559710}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1909509993}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1787552983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_972918176}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_741721705}

[[开启安全日志同步保存功能后，系统将安全日志进行集中处理：当生成的日志信息中有安全日志，在不影响日志信息现有输出规则的前提下，系统会将安全日志信息同步保存到专用的安全日志文件。这样既实现了安全日志的集中管理，又有利于用户随时快捷地查看安全日志，了解设备状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_493314043}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1722155080}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_587665759}[开启安全日志同步保存功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_774859719}

[\[Sysname\] info-center security-logfile enable]{lang="EN-US"}
:::::

::::: {#1866400550 .myid}
[]{#_Toc404797472}[]{#struct_0_13409_16130_1244455612}[]{#_Toc276478866}[]{#_Toc264548153}[]{#_Toc264547788}

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile frequency**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 9 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_1787618519}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x507325864}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **security-logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_x1454884831}[命令用来设置设备自动保存安全日志文件的频率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **security-logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_x1778147531}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1291342373}

[**[info-center]{lang="EN-US"}**[ **security-logfile** **frequency** *freq-sec*]{lang="EN-US"}]{#struct_0_13409_16130_x1304875256}

[**[undo]{lang="EN-US"}**[ **info-center** **security-logfile** **frequency**]{lang="EN-US"}]{#struct_0_13409_16130_1468521343}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_109496256}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13409_16130_1787684055}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1005865368}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x435131921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x797938317}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1174503856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1436985596}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x981086986}

[*[freq-sec]{lang="EN-US"}*]{#struct_0_13409_16130_390671668}[：系统自动保存安全日志文件的频率，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，不同设备支持的缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1440611143}

[[设置设备自动保存安全日志文件的频率后，安全日志会先被输出到安全日志文件缓冲区（]{style="font-family:宋体"}[security-logfile buffer]{lang="EN-US"}]{#struct_0_13409_16130_1787749591}[），系统会按照配置中指定的频率将安全日志文件缓冲区的内容写入安全日志文件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2076096806}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x2142845335}[设置安全日志自动保存到文件的频率为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x231076484}

[\[Sysname\] info-center security-logfile frequency 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x816121743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **security-logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_x1485152901}
:::::

::::: {#479164658 .myid}
[]{#_Toc404797473}[]{#struct_0_13409_16130_x863617197}[]{#_Toc276478867}[]{#_Toc264548154}[]{#_Toc264547789}

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile size-quota**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 10 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x255241782}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_1786766551}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="IT"}**]{#struct_0_13409_16130_2126078017}[ **security-logfile** **size-quota**]{lang="IT"}[命令用来设置单个安全日志文件最大能占用的存储空间的大小。]{style="font-family:宋体"}

[**[undo]{lang="IT"}**]{#struct_0_13409_16130_110873656}[ **info-center** **security-logfile** **size-quota**]{lang="IT"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x912978747}

[**[info-center]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x671123498}**[size-quota]{lang="IT"}**[ *size*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_13409_16130_x2058586483}[ **info-center** **security-logfile** **size-quota**]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1660690709}

[[本命令的缺省情况与设备的型号有关]{style="font-family:宋体"}]{#struct_0_13409_16130_x1926013559}[，]{style="font-family:
宋体"}[请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_711450093}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1786832087}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1000967483}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1726316388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_666520956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_294454733}

[*[size]{lang="IT"}*]{#struct_0_13409_16130_902426734}[：]{style="font-family:宋体"}[单个安全日志文件可使用的存储空间的最大值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[单位为]{style="font-family:宋体"}[MB]{lang="IT"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1080894189}

[[\# ]{lang="IT"}]{#struct_0_13409_16130_x1202856956}[设置单个安全日志文件最大能占用的存储空间的大小为]{style="font-family:宋体"}[6MB]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x941592513}

[\[Sysname\] info-center security-logfile size-quota 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_13409_16130_7809018}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x2099791809}**[alarm-threshold]{lang="IT"}**
:::::

::::: {#-112774623 .myid}
[]{#_Toc404797474}[]{#struct_0_13409_16130_x1424630442}[]{#_Toc276478868}[]{#_Toc264548155}[]{#_Toc264547790}

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile directory**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 11 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x1732983810}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x623799602}
:::

[ ]{lang="EN-US"}

[**[info-center]{lang="EN-US"}**[ **security-logfile** ]{lang="EN-US"}]{#struct_0_13409_16130_x1049093395}**[directory]{lang="IT"}**[命令用来修改存储安全日志文件的路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2066239559}

[**[info-center]{lang="EN-US"}**[ **security-logfile** **directory** *dir-name*]{lang="EN-US"}]{#struct_0_13409_16130_420504181}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941526977}

[[存储安全日志文件路径为存储设备根目录下的]{style="font-family:宋体"}[seclog]{lang="EN-US"}]{#struct_0_13409_16130_1197364624}[文件夹。对于支持]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡分区的设备，存储安全日志文件目录与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1569860414}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x454208828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x728656195}

[[security-audit]{lang="EN-US"}]{#struct_0_13409_16130_1098258540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x844084500}

[*[dir-name]{lang="EN-US"}*]{#struct_0_13409_16130_x941461441}[：安全日志文件存储的路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1919518189}

[[在执行该配置前，存储安全日志文件的文件夹必须为当前已创建的目录。]{style="font-family:宋体"}]{#struct_0_13409_16130_1249683810}

[[配置时，请注意：]{style="font-family:宋体"}]{#struct_0_13409_16130_x284242184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在设备重启后失效（集中式设备）。]{style="font-family:宋体"}]{#struct_0_13409_16130_x726443254}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在设备重启或主备倒换后失效（分布式设备－独立运行模式）。]{style="font-family:宋体"}]{#struct_0_13409_16130_x691773651}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在]{style="font-family:宋体"}]{#struct_0_13409_16130_x594491271}[IRF]{lang="EN-US"}[重启或主从设备倒换后失效（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置会在]{style="font-family:宋体"}]{#struct_0_13409_16130_220180880}[IRF]{lang="EN-US"}[重启或全局主用主控板和全局备用主控板主备倒换后失效（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1080444103}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x941395905}[设置存放安全日志文件的目录为]{style="font-family:宋体"}[flash:/test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir test]{lang="EN-US"}]{#struct_0_13409_16130_809349916}

[Creating directory flash:/test\... Done.]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] info-center security-logfile directory flash:/test]{lang="EN-US"}
:::::

::: {#-540823941 .myid}
[]{#_Toc404797475}[]{#struct_0_13409_16130_x1077520295}[]{#_Toc276478869}[]{#_Toc72751625}

**信息中心 \-- 信息中心配置命令 \-- info-center source**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_13409_16130_x433150580}[命令用来配置日志信息的输出规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info**]{lang="EN-US"}[-**center** **source**]{lang="EN-US"}]{#struct_0_13409_16130_x324869624}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1467671727}

[**[info-center]{lang="EN-US"}**[ **source** { *module-name* \| **default** } { **console** \| **logbuffer** \| **logfile** \| **loghost** \| **monitor** } { **deny** \| **level** *severity* }]{lang="EN-US"}]{#struct_0_13409_16130_1160630724}

[**[undo]{lang="EN-US"}**[ **info-center** **source** { *module-name* \| **default** } { **console** \| **logbuffer** \| **logfile** \| **loghost** \| **monitor** }]{lang="EN-US"}]{#struct_0_13409_16130_x941330369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1989930765}

[[日志信息的输出规则请参见]{style="font-family:宋体"}]{#struct_0_13409_16130_x1485814442}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?-540823941#_Ref152648258)[：]{style="font-family:宋体"}

[]{#struct_0_13409_16130_x767884951}[[表1-8 ]{lang="EN-US"}[输出方向的缺省输出规则]{style="font-family:
黑体"}]{#_Ref152648258}

[]{#table_struct_0_1648615346}[[输出方向]{style="font-family:黑体"}]{#struct_0_13409_16130_1090581552}
:::

[[允许输出的模块]{style="font-family:黑体"}]{#struct_0_13409_16130_2140398444}

[[log]{lang="EN-US"}]{#struct_0_13409_16130_x1751721082}

[[security]{lang="EN-US"}]{#struct_0_13409_16130_x476746200}

[[diagnostic]{lang="EN-US"}]{#struct_0_13409_16130_x941264833}

[[hide]{lang="EN-US"}]{#struct_0_13409_16130_395460157}

[[控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_1392683067}

[[所有支持的模块]{style="font-family:宋体"}]{#struct_0_13409_16130_x680527212}

[[debugging]{lang="EN-US"}]{#struct_0_13409_16130_799122074}

[[不能输出到控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_1668890345}

[[不能输出到控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_x941199297}

[[不能输出到控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_x848287177}

[[监视终端]{style="font-family:宋体"}]{#struct_0_13409_16130_x1911699042}

[[所有支持的模块]{style="font-family:宋体"}]{#struct_0_13409_16130_x1043357706}

[[debugging]{lang="EN-US"}]{#struct_0_13409_16130_x1279207914}

[[不能输出到控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_x941133761}

[[不能输出到控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_x1189045206}

[[不能输出到控制台]{style="font-family:宋体"}]{#struct_0_13409_16130_x297815885}

[[日志主机]{style="font-family:宋体"}]{#struct_0_13409_16130_1586726018}

[[所有支持的模块]{style="font-family:宋体"}]{#struct_0_13409_16130_x811507643}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_x942116801}

[[不能输出到日志主机]{style="font-family:宋体"}]{#struct_0_13409_16130_x1277471447}

[[不能输出到日志主机]{style="font-family:宋体"}]{#struct_0_13409_16130_x637333365}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_1645827814}

[[日志缓冲区]{style="font-family:宋体"}]{#struct_0_13409_16130_1791425479}

[[所有支持的模块]{style="font-family:宋体"}]{#struct_0_13409_16130_x942051265}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_x1745255165}

[[不能输出到日志缓冲区]{style="font-family:宋体"}]{#struct_0_13409_16130_x985085220}

[[不能输出到日志缓冲区]{style="font-family:宋体"}]{#struct_0_13409_16130_478186255}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_x2127464501}

[[日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x941592512}

[[所有支持的模块]{style="font-family:宋体"}]{#struct_0_13409_16130_7874554}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_1799091949}

[[不能输出到日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_1332339733}

[[不能输出到日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x941526976}

[[informational]{lang="EN-US"}]{#struct_0_13409_16130_1197299088}

[[安全日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_1582055284}

[[所有支持的模块，不能过滤]{style="font-family:宋体"}]{#struct_0_13409_16130_x1369260432}

[[不能输出到安全日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x941461440}

[[debugging]{lang="EN-US"}]{#struct_0_13409_16130_1919452653}[（不能过滤）]{style="font-family:宋体"}

[[不能输出到安全日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_1680022374}

[[不能输出到安全日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x1916826046}

[[诊断日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x941395904}

[[所有支持的模块，不能过滤]{style="font-family:宋体"}]{#struct_0_13409_16130_809415452}

[[不能输出到诊断日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_677659843}

[[不能输出到诊断日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x941330368}

[[debugging]{lang="EN-US"}]{#struct_0_13409_16130_x1989865229}[（不能过滤）]{style="font-family:宋体"}

[[不能输出到诊断日志文件]{style="font-family:宋体"}]{#struct_0_13409_16130_x1165771710}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1438468712}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x1150502546}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941264832}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_395394621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_1950048199}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1127560736}

[*[module-name]{lang="EN-US"}*]{#struct_0_13409_16130_x1156943128}[：设置指定应用模块日志信息的输出规则。比如要输出关于]{style="font-family:宋体"}[FTP]{lang="EN-US"}[的日志信息，就把该参数设置成]{style="font-family:宋体"}[FTP]{lang="EN-US"}[。系统支持的来源模块可以通过在系统视图下输入]{style="font-family:宋体"}**[info-center]{lang="EN-US"}**[ **source** **?**]{lang="EN-US"}[进行查看。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_13409_16130_1946720030}[：设置当前允许输出的所有模块日志信息的输出规则，包含在系统视图下输入]{style="font-family:宋体"}**[info-center]{lang="EN-US"}**[ **source** ]{lang="EN-US"}**[？]{style="font-family:宋体"}**[查看到的所有具体模块。]{style="font-family:宋体"}

[**[console]{lang="EN-US"}**]{#struct_0_13409_16130_x16759944}[：]{style="font-family:宋体"}[输出到控制台。]{style="font-family:宋体"}

[**[logbuffer]{lang="EN-US"}**]{#struct_0_13409_16130_1570500844}[：输出到日志缓冲区。]{style="font-family:宋体"}

[**[logfile]{lang="EN-US"}**]{#struct_0_13409_16130_x941199296}[：输出到日志文件。]{style="font-family:宋体"}

[**[loghost]{lang="EN-US"}**]{#struct_0_13409_16130_x848221641}[：输出到日志主机。]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**]{#struct_0_13409_16130_x1930721981}[：输出到监视终端。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_13409_16130_1554024846}[：]{style="font-family:宋体"}[禁止输出信息。]{style="font-family:宋体"}

[**[level]{lang="EN-US"}**[ *severity*]{lang="EN-US"}]{#struct_0_13409_16130_678908584}[：指定信息级别，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，具体内容请参见]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?-1632812546#_Ref127266393)[。通过该参数可以控制允许]{style="font-family:宋体"}[/]{lang="EN-US"}[禁止输出的日志信息的最低级别。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1564254455}

[[该命令用来配置日志信息的输出规则。例如实现]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13409_16130_1740646014}[模块的日志信息输出的过滤规则，用户可以设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[模块的日志信息高于]{style="font-family:宋体"}[warning]{lang="EN-US"}[级别的可以输出到日志主机，而高于]{style="font-family:宋体"}[informational]{lang="EN-US"}[级别的可以输出到日志缓冲区。同时可以设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[模块的告警信息发送到特定的方向等功能。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13409_16130_x949909518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有使用]{style="font-family:宋体"}]{#struct_0_13409_16130_1343302439}*[module-name]{lang="EN-US"}*[参数为应用模块单独设置输出规则，则该模块使用缺省的或者]{style="font-family:宋体"}**[default]{lang="EN-US"}**[参数设置的输出规则，否则使用单独设置的输出规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次使用本命令配置]{style="font-family:宋体"}]{#struct_0_13409_16130_x941133760}**[default]{lang="EN-US"}**[或者某个模块的输出规则，则以最新的配置生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果应用模块单独设置输出规则后，必须使用]{style="font-family:宋体"}]{#struct_0_13409_16130_x1188979670}*[module-name]{lang="EN-US"}*[参数来修改或删除该规则，使用]{style="font-family:宋体"}**[default]{lang="EN-US"}**[参数进行的新配置对该模块不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_182703723}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1855209658}[只允许]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[模块的信息输出控制台，且输出信息的级别为]{style="font-family:宋体"}[emergency]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x2128352031}

[\[Sysname\] info-center source default console deny]{lang="EN-US"}

[\[Sysname\] info-center source vlan console level emergency]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x553881144}[在前面例子基础上撤销控制台方向上]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[模块的输出（即全部信息不在控制台显示）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x46039443}

[\[Sysname\] undo info-center source vlan console]{lang="EN-US"}

::: {#-1001874651 .myid}
[]{#_Ref128045691}[]{#_Ref128045679}[]{#_Toc98581711}[]{#_Toc98214427}[]{#_Toc92946537}[]{#_Toc404797476}[]{#struct_0_13409_16130_x942116800}[]{#_Toc276478870}[]{#_Toc264040794}

**信息中心 \-- 信息中心配置命令 \-- info-center synchronous**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **synchronous**]{lang="EN-US"}]{#struct_0_13409_16130_x1277405911}[命令用来开启命令行输入回显功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **synchronous**]{lang="EN-US"}]{#struct_0_13409_16130_1558746795}[命令用来关闭命令行输入回显功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1187747564}

[**[info-center]{lang="EN-US"}**[ **synchronous**]{lang="EN-US"}]{#struct_0_13409_16130_1121687974}

[**[undo]{lang="EN-US"}**[ **info-center** **synchronous**]{lang="EN-US"}]{#struct_0_13409_16130_1722466044}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1914653217}

[[命令行输入回显功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_1595975441}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_210023770}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x942051264}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1745189629}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1136218930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x178993604}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1633323137}

[[当用户进行命令行、参数或者]{style="font-family:宋体"}[Y/N]{lang="EN-US"}]{#struct_0_13409_16130_x1691714438}[确认信息输入时，如果被大量的日志信息打断，用户可能记不清已经输入了哪些字符串，还需要输入哪些字符串。使用命令行输入回显功能，能够协助用户配置。系统会在日志信息输出完毕后回显用户已有的输入或者]{style="font-family:宋体"}[Y/N]{lang="EN-US"}[确认信息，以便用户继续执行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x579513327}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1927252228}[开启设备命令行输入回显功能，输入]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **current-configuration**]{lang="EN-US"}[命令查看设备当前配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x941592515}

[\[Sysname\] info-center synchronous]{lang="EN-US"}

[Info-center synchronous output is on]{lang="EN-US"}

[\[Sysname\] display current-]{lang="EN-US"}

[[此时，收到日志报文，则系统在所有的日志报文显示完以后，附加显示用户的输入（此例为"]{style="font-family:宋体"}[display current-]{lang="EN-US"}]{#struct_0_13409_16130_7940090}["）。]{style="font-family:宋体"}

[[%May 21 14:33:19:425 2007 Sysname SHELL/4/LOGIN: VTY login from 192.168.1.44]{lang="EN-US"}]{#struct_0_13409_16130_x2089405613}

[\[Sysname\] display current-]{lang="EN-US"}

[[此时，用户可以继续输入]{style="font-family:宋体"}[configuration]{lang="EN-US"}]{#struct_0_13409_16130_1810174861}[（完成命令]{style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**[的完整输入），回车，即可执行该命令。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_2045761396}[开启设备命令行输入回显功能，保存当前配置（输入交互信息）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_968928200}

[\[Sysname\] info-center synchronous]{lang="EN-US"}

[Info-center synchronous output is on]{lang="EN-US"}

[\[Sysname\] save]{lang="EN-US"}

[The current configuration will be written to the device. Are you sure? \[Y/N\]:]{lang="EN-US"}

[[此时，收到日志信息，则系统会在所有的日志报文显示完以后，附加显示]{style="font-family:宋体"}[\[Y/N\]:]{lang="EN-US"}]{#struct_0_13409_16130_x1712215035}[。]{style="font-family:宋体"}

[[%May 21 14:33:19:425 2007 Sysname SHELL/4/LOGIN: VTY login from 192.168.1.44]{lang="EN-US"}]{#struct_0_13409_16130_x941526979}

[\[Y/N\]:]{lang="EN-US"}

[[此时，用户可以输入]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_13409_16130_1198019984}[或者]{style="font-family:宋体"}[N]{lang="EN-US"}[，继续日志信息输出前的操作。]{style="font-family:宋体"}
:::

::: {#-361717861 .myid}
[]{#_Toc404797477}[]{#struct_0_13409_16130_986201906}[]{#_Toc276478871}[]{#_Toc264123590}[]{#_Toc264120164}

**信息中心 \-- 信息中心配置命令 \-- info-center timestamp**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **timestamp**]{lang="EN-US"}]{#struct_0_13409_16130_1748779293}[命令用来设置发往控制台、监视终端、日志缓冲区和日志文件方向的日志信息的时间戳输出格式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **timestamp**]{lang="EN-US"}]{#struct_0_13409_16130_x1956029202}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x250055695}

[**[info-center]{lang="EN-US"}**[ **timestamp**]{lang="EN-US"}[ { **boot** \| **date** \| **none** }]{lang="EN-US"}]{#struct_0_13409_16130_x1866290539}

[**[undo]{lang="IT"}**]{#struct_0_13409_16130_1523213243}[ **info-center** **timestamp**]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1063153162}

[[时间戳输出格式为]{style="font-family:宋体"}**[date]{lang="EN-US"}**]{#struct_0_13409_16130_x941461443}[格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1919649261}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1232811290}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1747345537}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1320886855}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x919079433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_91881975}

[**[boot]{lang="EN-US"}**]{#struct_0_13409_16130_x123484561}[：系统启动后经历的时间，格式为：]{style="font-family:宋体"}[xxx.yyy]{lang="EN-US"}[，其中]{style="font-family:宋体"}[xxx]{lang="EN-US"}[是系统自启动后经历时间的毫秒数高]{style="font-family:宋体"}[32]{lang="EN-US"}[位，]{style="font-family:宋体"}[yyy]{lang="EN-US"}[是低]{style="font-family:宋体"}[32]{lang="EN-US"}[位，形如]{style="font-family:宋体"}[0.21990989]{lang="EN-US"}[（等效于]{style="font-family:宋体"}[Jun 25 14:09:26:881 2007]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[date]{lang="EN-US"}**]{#struct_0_13409_16130_392376050}[：系统当前的日期和时间，格式为"]{style="font-family:宋体"}[MMM DD hh:mm:ss:xxx YYYY]{lang="EN-US"}["，形如]{style="font-family:宋体"}[Dec  8 10:12:21:708 2007]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}["]{lang="EN-US" style="font-family:宋体"}[MMM]{lang="EN-US"}]{#struct_0_13409_16130_x941395907}["为英语月份的缩写，具体取值如下：]{lang="EN-US" style="font-family:宋体"}[Jan]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Feb]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Mar]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Apr]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[May]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Jun]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Jul]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Aug]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Sep]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Oct]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Nov]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Dec]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}["]{style="font-family:宋体"}]{#struct_0_13409_16130_809480988}[DD]{lang="EN-US"}["表示日期，如果日期的值小于]{style="font-family:宋体"}[10]{lang="EN-US"}[，则格式为"空格＋日期"，如"]{style="font-family:宋体"}[ 7]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}["]{style="font-family:宋体"}]{#struct_0_13409_16130_x769304125}[hh:mm:ss:xxx]{lang="EN-US"}["表示本地时间，]{style="font-family:宋体"}[hh]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[00]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[mm]{lang="EN-US"}[和]{style="font-family:宋体"}[ss]{lang="EN-US"}[的取值范围均为]{style="font-family:宋体"}[00]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，]{style="font-family:宋体"}[xxx]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}["]{lang="EN-US" style="font-family:宋体"}[YYYY]{lang="EN-US"}]{#struct_0_13409_16130_141751148}["表示年份。]{lang="EN-US" style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13409_16130_x1434152977}[：不带时间信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1290240974}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x324577040}[设置日志信息时间戳输出格式为]{style="font-family:宋体"}[boot]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_919309474}

[\[Sysname\] info-center timestamp boot]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941330371}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **timestamp** **loghost**]{lang="EN-US"}]{#struct_0_13409_16130_x1990455052}
:::

::: {#556428956 .myid}
[]{#_Toc404797478}[]{#struct_0_13409_16130_x1405326343}[]{#_Toc276478872}[]{#_Toc264123591}[]{#_Toc264120165}

**信息中心 \-- 信息中心配置命令 \-- info-center timestamp loghost**

------------------------------------------------------------------------

[**[info-center]{lang="EN-US"}**[ **timestamp** **loghost**]{lang="EN-US"}]{#struct_0_13409_16130_x347386344}[命令用来设置发往日志主机的日志信息的时间戳输出格式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **info-center** **timestamp** **loghost**]{lang="EN-US"}]{#struct_0_13409_16130_x1806740145}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x120059943}

[**[info-center]{lang="EN-US"}**[ **timestamp**]{lang="EN-US"}[ **loghost** { **date** \| **iso** \| **no-year-date** \| **none** }]{lang="EN-US"}]{#struct_0_13409_16130_x1453057565}

[**[undo]{lang="EN-US"}**[ **info-center** **timestamp**]{lang="EN-US"}[ **loghost**]{lang="EN-US"}]{#struct_0_13409_16130_x960104442}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_454030121}

[[发往日志主机的日志信息的时间戳输出格式为]{style="font-family:宋体"}**[date]{lang="EN-US"}**]{#struct_0_13409_16130_x941264835}[格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_395591229}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1019621947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x598241212}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1116188904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1794397730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_1144173122}

[**[date]{lang="EN-US"}**]{#struct_0_13409_16130_x1185362150}[：系统当前日期和时间，格式为：]{style="font-family:宋体"}[mmm dd hh:mm:ss yyyy]{lang="EN-US"}[，形如]{style="font-family:宋体"}[Dec  8 10:12:21 2007]{lang="EN-US"}[，但最终显示格式由日志主机决定。]{style="font-family:宋体"}

[**[iso]{lang="EN-US"}**]{#struct_0_13409_16130_x1314015482}[：设置时间戳采用]{style="font-family:宋体"}[ISO 8601]{lang="EN-US"}[标准格式，形如：]{style="font-family:宋体"}[2009-09-21T15:32:55]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-year-date]{lang="EN-US"}**]{#struct_0_13409_16130_x941199299}[：系统当前日期和时间，但不包含年份信息。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13409_16130_x849204681}[：不带时间信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1137230280}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x968509918}[设置发往日志主机的日志信息的时间戳为]{style="font-family:宋体"}[no-year-date]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_x2054098711}

[\[Sysname\] info-center timestamp loghost no-year-date]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1362424533}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **timestamp**]{lang="EN-US"}]{#struct_0_13409_16130_2019286013}
:::

::: {#296352252 .myid}
[]{#_Toc98581713}[]{#_Toc98214429}[]{#_Toc92946539}[]{#_Toc276478873}[]{#_Toc264123596}[]{#_Toc404797479}[]{#struct_0_13409_16130_x205725287}[]{#_Toc342410168}

**信息中心 \-- 信息中心配置命令 \-- info-center trace-logfile quota**

------------------------------------------------------------------------

[**[info-center trace-logfile quota]{lang="EN-US"}**]{#struct_0_13409_16130_x941133763}[命令用]{style="font-family:宋体"}[来设置调试跟踪日志文件最大能占用的存储空间的大小。]{style="font-family:宋体"}

[**[undo info-center trace-logfile quota]{lang="EN-US"}**]{#struct_0_13409_16130_x1189176278}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1730381020}

[**[info-center trace-logfile quota ]{lang="EN-US"}**]{#struct_0_13409_16130_x870018412}*[size]{lang="IT"}*

[**[undo info-center trace-logfile quota]{lang="EN-US"}**]{#struct_0_13409_16130_x707437374}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_1564167993}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_13409_16130_1392673760}[调试跟踪日志文件最大能占用的存储空间的大小为]{style="font-family:宋体"}[1MB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_1290599060}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13409_16130_65552017}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x942116803}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x1277340375}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x865033139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_1978236466}

[*[size]{lang="IT"}*]{#struct_0_13409_16130_33878253}[：调试跟踪日志文件最大能占用的存储空间的大小，单位为]{style="font-family:宋体"}[MB]{lang="IT"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1221373554}

[[\# ]{lang="IT"}]{#struct_0_13409_16130_595759569}[设置调试跟踪日志文件最大能占用的存储空间的大小为]{style="font-family:宋体"}[6MB]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13409_16130_178638180}

[\[Sysname\] info-center trace-logfile quota 6]{lang="EN-US"}
:::

::::: {#-396064908 .myid}
[]{#_Toc404797480}[]{#struct_0_13409_16130_x942051267}

**信息中心 \-- 信息中心配置命令 \-- logfile save**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 12 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_x1745124093}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_x1245417844}
:::

[ ]{lang="EN-US"}

[**[logfile]{lang="EN-US"}**[ **save**]{lang="EN-US"}]{#struct_0_13409_16130_x285430183}[命令用来手动将日志文件缓冲区中的内容全部保存到日志文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_849429746}

[**[logfile]{lang="EN-US"}**[ **save**]{lang="EN-US"}]{#struct_0_13409_16130_x1551833327}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1974175811}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_617569519}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1743227866}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x941592514}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_8005626}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_298057258}

[[日志文件的保存路径可以通过]{style="font-family:宋体"}**[info-center]{lang="EN-US"}**[ **logfile** **directory**]{lang="EN-US"}]{#struct_0_13409_16130_x1592688170}[命令设置。]{style="font-family:
宋体"}

[[日志文件保存成功后，日志文件缓冲区中的内容会被清空。]{style="font-family:宋体"}]{#struct_0_13409_16130_x578306577}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1584774616}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_468797819}[手动将日志文件缓冲区中的内容保存到日志文件。]{style="font-family:宋体"}

[[\<Sysname\> logfile save]{lang="EN-US"}]{#struct_0_13409_16130_485014598}

[The contents in the log file buffer have been saved to the file flash:/logfile/logfile.log.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941526978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **logfile** **enable**]{lang="EN-US"}]{#struct_0_13409_16130_1197954448}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="EN-US"}**[ **logfile** **directory**]{lang="EN-US"}]{#struct_0_13409_16130_1941776886}
:::::

::: {#-706131822 .myid}
[]{#_Toc404797481}[]{#struct_0_13409_16130_x763787317}[]{#_Toc276478874}

**信息中心 \-- 信息中心配置命令 \-- reset logbuffer**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_x1760079454}[命令用来清除日志缓冲区中的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_676320438}

[**[reset]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_x1377171336}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1837400622}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x507967854}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941461442}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_1919583725}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_929539759}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1331227516}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1797081205}[清除日志缓冲区中的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset logbuffer]{lang="EN-US"}]{#struct_0_13409_16130_x1709099572}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_1414646121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **logbuffer**]{lang="EN-US"}]{#struct_0_13409_16130_223669783}
:::

::::: {#1412118989 .myid}
[]{#_Toc404797482}[]{#struct_0_13409_16130_x941395906}[]{#_Toc276478875}[]{#_Toc264548157}[]{#_Toc263079915}[]{#_Toc245283992}

**信息中心 \-- 信息中心配置命令 \-- security-logfile save**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心命令.files/image001.png){#图片 13 border="0" width="62" height="27"}]{lang="EN-US"}]{#struct_0_13409_16130_809546524}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13409_16130_300273567}
:::

[ ]{lang="EN-US"}

[**[security-logfile]{lang="IT"}**]{#struct_0_13409_16130_94200469}[ **save**]{lang="IT"}[命令用来手动将安全日志文件缓冲区中的内容全部保存到安全日志文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1592116267}

[**[security-logfile]{lang="IT"}**]{#struct_0_13409_16130_1363552706}[ **save**]{lang="IT"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1484243873}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13409_16130_599396534}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1524737135}

[[security-audit]{lang="EN-US"}]{#struct_0_13409_16130_x941330370}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1828902541}

[[安全日志文件保存成功后，安全日志文件缓冲区中的内容会被立即清空。]{style="font-family:宋体"}]{#struct_0_13409_16130_x489510625}

[[需要注意的是，只有配置了安全日志管理员权限的本地用户才能使用本命令。安全日志管理员的配置请参见"安全命令参考"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_13409_16130_x770292535}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_2021452561}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_x1994911465}[手动将安全日志缓冲区中的内容保存到安全日志文件。]{style="font-family:宋体"}

[[\<Sysname\> security-logfile save]{lang="EN-US"}]{#struct_0_13409_16130_x1888047080}

[The contents in the security log file buffer have been saved to the file flash:/seclog/seclog.log.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941264834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[info-center]{lang="IT"}**]{#struct_0_13409_16130_395525693}[ **security-logfile** **switch-directory**]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization-attribute]{lang="EN-US"}**]{#struct_0_13409_16130_x1269997396}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::: {#856427860 .myid}
[]{#_Toc276478877}[]{#_Toc263079917}[]{#_Toc72751632}[]{#_Toc404797483}[]{#struct_0_13409_16130_x1602413288}[]{#_Toc324754235}[]{#_Toc363733665}[]{#_Toc363733666}[]{#_Toc363733667}[]{#_Toc363733668}[]{#_Toc363733669}[]{#_Toc363733670}[]{#_Toc363733671}[]{#_Toc363733672}[]{#_Toc363733673}[]{#_Toc363733674}[]{#_Toc363733675}[]{#_Toc363733676}[]{#_Toc363733677}[]{#_Toc363733678}[]{#_Toc363733679}[]{#_Toc363733680}[]{#_Toc363733681}[]{#_Toc363733682}[]{#_Toc363733683}[]{#_Toc363733684}[]{#_Toc363733685}

**信息中心 \-- 信息中心配置命令 \-- terminal debugging**

------------------------------------------------------------------------

[**[terminal]{lang="EN-US"}**[ **debugging**]{lang="EN-US"}]{#struct_0_13409_16130_x83143692}[命令用来开启当前终端对调试信息的显示功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **terminal** **debugging**]{lang="EN-US"}]{#struct_0_13409_16130_1020787039}[命令用来关闭当前终端对调试信息的显示功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x942116802}

[**[terminal]{lang="EN-US"}**[ **debugging**]{lang="EN-US"}]{#struct_0_13409_16130_x1277274839}

[**[undo]{lang="EN-US"}**[ **terminal** **debugging**]{lang="EN-US"}]{#struct_0_13409_16130_x672567023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_523389288}

[[当前终端对调试信息的显示功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13409_16130_1000401885}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_654284809}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x975844313}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_1879430510}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x508873598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x942051266}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1745058557}

[[如果需要在控制台显示调试信息，请先配置]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[ **debugging**]{lang="EN-US"}]{#struct_0_13409_16130_1615523488}[命令，再使能信息中心功能（信息中心功能缺省处于使能状态），最后使用]{style="font-family:宋体"}**[debugging]{lang="EN-US"}**[命令打开功能模块的调试信息开关。]{style="font-family:宋体"}

[[如果需要在监控终端上显示调试信息，请先配置]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[ **monitor**]{lang="EN-US"}]{#struct_0_13409_16130_x411180630}[和]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[ **debugging**]{lang="EN-US"}[命令，再使能信息中心功能（信息中心功能缺省处于使能状态），最后使用]{style="font-family:宋体"}**[debugging]{lang="EN-US"}**[命令打开功能模块的调试信息开关。]{style="font-family:宋体"}

[[需要注意的是，本命令只对当前连接有效。当终端与设备重新建立连接后，本命令会恢复到缺省情况。]{style="font-family:宋体"}]{#struct_0_13409_16130_851104281}

[[执行]{style="font-family:宋体"}**[terminal logging level]{lang="EN-US"}**[ 7]{lang="EN-US"}]{#struct_0_13409_16130_x1427175028}[命令或]{style="font-family:宋体"}**[terminal debugging]{lang="EN-US"}**[命令，都可以开启当前终端对调试信息的显示功能，但两条命令有如下区别：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[terminal logging level]{lang="EN-US"}**[ 7]{lang="EN-US"}]{#struct_0_13409_16130_x1575395373}[命令，当前终端允许输出]{lang="EN-US" style="font-family:宋体"}[级别为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:
宋体"}[7]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[所有]{style="font-family:宋体"}[日志。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[terminal debugging]{lang="EN-US"}**]{#struct_0_13409_16130_193630135}[命令，当前终端仅输出]{lang="EN-US" style="font-family:
宋体"}**[terminal logging level]{lang="EN-US"}**[命令设置的日志信息和级别为]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[的调试信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_449480583}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1627037714}[允许]{style="font-family:宋体"}[debugging]{lang="EN-US"}[日志信息输出到控制台或者监视终端。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_13409_16130_x1585660091}

[The current terminal is enabled to display debugging information.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941592517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminal logging level]{lang="EN-US"}**]{#struct_0_13409_16130_8071162}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminal monitor]{lang="EN-US"}**]{#struct_0_13409_16130_219221832}
:::

::: {#133162017 .myid}
[]{#_Toc404797484}[]{#struct_0_13409_16130_x1472289096}

**信息中心 \-- 信息中心配置命令 \-- terminal logging level**

------------------------------------------------------------------------

[**[terminal]{lang="EN-US"}**[ **logging** **level**]{lang="EN-US"}]{#struct_0_13409_16130_817107750}[命令用来配置当前终端允许输出的日志信息的最低级别。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **terminal** **logging** **level**]{lang="EN-US"}]{#struct_0_13409_16130_x1867672169}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1589567480}

[**[terminal]{lang="EN-US"}**[ **logging** **level**]{lang="EN-US"}[ *severity*]{lang="EN-US"}]{#struct_0_13409_16130_x1249274599}

[**[undo]{lang="EN-US"}**[ **terminal** **logging** **level**]{lang="EN-US"}]{#struct_0_13409_16130_1615457952}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_517241144}

[[当前终端允许输出的日志信息的最低级别均为]{style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_13409_16130_765636592}[（]{style="font-family:宋体"}[Informational]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_628605988}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13409_16130_x791926344}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1633808453}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x754684793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_504307815}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13409_16130_x2054695003}

[*[severity]{lang="EN-US"}*]{#struct_0_13409_16130_292692976}[：当前终端允许输出的日志信息的最低级别，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1750450301}

[[在配置了当前终端允许输出的日志信息的最低级别后，当系统输出信息时，所有信息等级高于或等于设置等级的信息都会被输出。例如，当配置的允许输出的日志信息的最低级别]{style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_13409_16130_1615654560}[（]{style="font-family:宋体"}[informational]{lang="EN-US"}[）时，等级]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[的信息均会被输出。]{style="font-family:
宋体"}

[[本命令配置的显示属性只对当前连接有效，当终端与设备的连接超时、重新建立连接后，显示属性将恢复到缺省情况。]{style="font-family:宋体"}]{#struct_0_13409_16130_x1886857400}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_1252559688}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1848726707}[配置当前终端监控的最低日志级别为]{style="font-family:宋体"}[debugging]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> terminal logging level 7]{lang="EN-US"}]{#struct_0_13409_16130_x1513977901}
:::

::: {#1639216089 .myid}
[]{#_Toc404797485}[]{#struct_0_13409_16130_1435215632}

**信息中心 \-- 信息中心配置命令 \-- terminal monitor**

------------------------------------------------------------------------

[**[terminal]{lang="EN-US"}**[ **monitor**]{lang="EN-US"}]{#struct_0_13409_16130_1895878227}[命令用来允许日志信息输出到当前终端。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **terminal** **monitor**]{lang="EN-US"}]{#struct_0_13409_16130_854045391}[命令用来禁止日志信息输出到当前终端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13409_16130_773384286}

[**[terminal]{lang="EN-US"}**[ **monitor**]{lang="EN-US"}]{#struct_0_13409_16130_511632852}

[**[undo]{lang="EN-US"}**[ **terminal** **monitor**]{lang="EN-US"}]{#struct_0_13409_16130_517839134}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941526981}

[[允许日志信息输出到控制台，不允许日志信息输出到监视终端。]{style="font-family:宋体"}]{#struct_0_13409_16130_1197495701}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13409_16130_777631226}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13409_16130_1616708699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13409_16130_x1657624158}

[[network-admin]{lang="EN-US"}]{#struct_0_13409_16130_x414537070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13409_16130_x563853540}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13409_16130_1484095380}

[[本命令只对当前连接有效。当终端与设备重新建立连接后，本命令会恢复到缺省情况。]{style="font-family:宋体"}]{#struct_0_13409_16130_660389489}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13409_16130_x941461445}

[[\# ]{lang="EN-US"}]{#struct_0_13409_16130_1919780333}[允许日志信息输出到监视终端。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_13409_16130_1290536135}

[The current terminal is enabled to display logs.]{lang="EN-US"}[]{#_Toc262810703}[]{#_Toc262810704}[]{#_Toc262810705}[]{#_Toc262810711}[]{#_Toc262810712}[]{#_Toc262810714}
:::
