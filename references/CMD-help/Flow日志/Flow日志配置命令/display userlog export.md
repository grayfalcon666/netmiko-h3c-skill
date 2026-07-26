::: {#-731236473 .myid}
[]{#_Toc404797417}[]{#struct_0_13802_12782_x1022649695}[]{#_Toc142995321}

**Flow日志 \-- Flow日志配置命令 \-- display userlog export**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **userlog** **export**]{lang="EN-US"}]{#struct_0_13802_12782_x169665624}[命令用来查看输出到日志主机的]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志的配置和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_956328075}

[**[display]{lang="EN-US"}**[ **userlog** **export**]{lang="EN-US"}]{#struct_0_13802_12782_1482322330}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_x370546896}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13802_12782_1526578699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_989583387}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_x292284047}

[[network-operator]{lang="EN-US"}]{#struct_0_13802_12782_1451423723}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_x1629567298}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13802_12782_1588812274}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_1363184954}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_2042373662}[查看输出到日志主机的]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志的配置和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display userlog export]{lang="EN-US"}]{#struct_0_13802_12782_x371005648}

[Flow:]{lang="EN-US"}

[  Export flow log as UDP Packet.]{lang="EN-US"}

[  Version: 3.0]{lang="EN-US"}

[  Source address: 2.2.2.2]{lang="EN-US"}

[  Log load balance function: Disabled]{lang="EN-US"}

[  Log host numbers: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Log host 1:]{lang="EN-US"}

[    IP address/Port: 1.2.3.6/2000]{lang="EN-US"}

[    Total logs/UDP packets exported: 112/87]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Log host 2:]{lang="EN-US"}

[    VPN instance:abc]{lang="EN-US"}

[    IP address/Port:1.1.1.1/2000]{lang="EN-US"}

[    Total logs/UDP packets exported: 6553665536/409597846]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display userlog export]{lang="EN-US"}]{#struct_0_13802_12782_x443130008}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1307180628}[[字段]{style="font-family:黑体"}]{#struct_0_13802_12782_x349630261}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13802_12782_1094390162}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_1872779470}

[[表示该段显示的是]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_1115429690}[日志的相关配置和统计信息]{style="font-family:宋体"}

[[Export flow log as UDP Packet]{lang="EN-US"}]{#struct_0_13802_12782_x370940112}

[[表示]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_1906442981}[日志按照封装成]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文的方式发送]{style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_13802_12782_183581240}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x70976183}[日志的版本号]{style="font-family:宋体"}

[[Source address]{lang="EN-US"}]{#struct_0_13802_12782_949118492}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x2046539520}[日志]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Log load balancing function]{lang="EN-US"}]{#struct_0_13802_12782_x197870179}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x1953552730}[日志]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文负载分担功能是否使能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_13802_12782_708769768}[：使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_13802_12782_2027534991}[：未使能]{lang="EN-US" style="font-family:宋体"}

[[Log hosts numbers]{lang="EN-US"}]{#struct_0_13802_12782_1913345293}

[[已配置的]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x370874576}[日志主机数量]{style="font-family:宋体"}

[[Log host 1]{lang="EN-US"}]{#struct_0_13802_12782_x838019732}

[[日志主机]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_13802_12782_1198526957}[的相关信息]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_13802_12782_949502269}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_28609798}[日志主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[IP address/port]{lang="EN-US"}]{#struct_0_13802_12782_x936701080}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x1163694557}[日志主机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号]{style="font-family:宋体"}

[[Total logs]{lang="EN-US"}]{#struct_0_13802_12782_x562941181}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x838625717}[日志的总数]{style="font-family:宋体"}

[[UDP packets exported]{lang="EN-US"}]{#struct_0_13802_12782_x1493787699}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x370809040}[日志的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文总数，一条]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文中可能含有多条]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_768862604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[userlog flow export]{lang="EN-US"}**]{#struct_0_13802_12782_x149010953}

::: {#244120704 .myid}
[]{#_Toc404797418}[]{#struct_0_13802_12782_49942629}[]{#_Toc142995322}

**Flow日志 \-- Flow日志配置命令 \-- reset userlog flow export**

------------------------------------------------------------------------

[**[reset]{lang="DE"}**[ ]{lang="DE"}]{#struct_0_13802_12782_x1193910503}**[userlog]{lang="DE"}**[ ]{lang="DE"}**[flow]{lang="DE"}**[ **export**]{lang="DE"}[命令用来清除]{style="font-family:宋体"}[Flow]{lang="DE"}[日志的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_206060082}

[**[r]{lang="EN-US"}**]{#struct_0_13802_12782_1370048395}**[eset]{lang="DE"}**[ ]{lang="DE"}**[userlog]{lang="DE"}**[ ]{lang="DE"}**[flow]{lang="DE"}**[ **export**]{lang="DE"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_1167560742}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13802_12782_790254373}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_x770075351}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_809262952}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_2061916291}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1034616421}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_838877677}[清除]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset userlog flow export]{lang="EN-US"}]{#struct_0_13802_12782_1116174887}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_2137184106}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[userlog flow export]{lang="EN-US"}**]{#struct_0_13802_12782_1467299277}
:::

::: {#932111608 .myid}
[]{#_Toc404797419}[]{#struct_0_13802_12782_x370219216}[]{#_Toc142995324}

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export host**

------------------------------------------------------------------------

[**[userlog]{lang="DE"}**[ ]{lang="DE"}]{#struct_0_13802_12782_379775081}**[flow]{lang="DE"}**[ ]{lang="DE"}**[export]{lang="DE"}**[ ]{lang="DE"}**[host]{lang="DE"}**[命令用来配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机地址和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo userlog]{lang="DE"}**[ ]{lang="DE"}]{#struct_0_13802_12782_1482510412}**[flow]{lang="DE"}**[ ]{lang="DE"}**[export]{lang="DE"}**[ ]{lang="DE"}**[host]{lang="DE"}**[命令用来删除]{style="font-family:宋体"}[Flow]{lang="DE"}[日志主机配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_1224505040}

[**[userlog]{lang="DE"}**]{#struct_0_13802_12782_x31664792}[ **flow** **export** ]{lang="DE"}[\[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}**[host]{lang="DE"}**[ { *hostname* \| ]{lang="DE"}*[ipv4-address]{lang="EN-US"}*[ \| **ipv6** *ipv6-address* } **port** *udp-port*]{lang="EN-US"}

[**[undo userlog]{lang="EN-US"}**[ **flow** **export** \[ **vpn-instance** *vpn-instance-name* \] **host** { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_13802_12782_458049400}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13802_12782_x478464674}

[[没有配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x2084317968}[日志主机的]{style="font-family:宋体"}[IP]{lang="DE"}[地址和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1870106067}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13802_12782_1598376427}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_328745475}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_x2011282973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_1124684412}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13802_12782_x2080349903}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13802_12782_x370153680}[：指定]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[Flow]{lang="DE"}[日志主机位于公网中。该参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[hostname]{lang="EN-US"}*]{#struct_0_13802_12782_1143174799}[：指定]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_13802_12782_1338924544}[：指定]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，取值范围是合法的单播]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，且不能是环回地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *host-ipv6-address*]{lang="EN-US"}]{#struct_0_13802_12782_768885132}[：指定]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}***[ udp-port]{lang="EN-US"}*]{#struct_0_13802_12782_x265260732}[：指定]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，]{style="font-family:宋体"}*[udp-port]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1411702625}

[[为了避免与通用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_13802_12782_1880955207}[端口号冲突，建议使用]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="DE"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1415398062}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_x1671254563}[将]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志信息发送给]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机，]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机的地址为]{style="font-family:宋体"}[1.2.3.6]{lang="EN-US"}[，对应]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13802_12782_703164076}

[\[Sysname\] userlog flow export host 1.2.3.6 port 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1472595347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display userlog export]{lang="EN-US"}**]{#struct_0_13802_12782_979730371}
:::

::: {#-1766656194 .myid}
[]{#_Toc404797420}[]{#struct_0_13802_12782_1116995638}

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export load-balancing**

------------------------------------------------------------------------

[**[userlog flow export ]{lang="DE"}[load-balancing]{lang="EN-US"}**]{#struct_0_13802_12782_2072666574}[命令用来配置]{style="font-family:宋体"}[Flow]{lang="DE"}[日志按照负载分担方式输出到日志主机。]{style="font-family:宋体"}

[**[undo userlog flow export ]{lang="DE"}[load-balancing]{lang="EN-US"}**]{#struct_0_13802_12782_933487725}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_679204317}

[**[userlog]{lang="EN-US"}**[ **flow** ]{lang="EN-US"}]{#struct_0_13802_12782_1377688919}**[export ]{lang="DE"}[load-balancing]{lang="EN-US"}**

[**[undo userlog]{lang="EN-US"}**[ **flow** ]{lang="EN-US"}]{#struct_0_13802_12782_x35876884}**[export ]{lang="DE"}[load-balancing]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13802_12782_1116930102}

[[每一条]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x606403586}[日志复制发送给所有已配置的]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_203979982}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13802_12782_1800026298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_726666519}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_x1936097250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_1001109379}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13802_12782_1366768961}

[[配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x484135271}[日志按照负载分担方式输出到日志主机时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了]{style="font-family:宋体"}]{#struct_0_13802_12782_x1665234071}[Flow]{lang="EN-US"}[日志负载分担功能以后，一条]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志仅仅会发送到用户配置的所有日志主机中的某一台特定的日志主机。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_74123591}[日志按照会话源]{style="font-family:宋体"}[IP]{lang="EN-US"}[进行负载分担。在不改变配置的前提下，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[固定的会话对应的]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志始终发送到固定的一台日志主机。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置的日志主机不可达时，日志主机仍会参与]{style="font-family:宋体"}]{#struct_0_13802_12782_581510366}[Flow]{lang="EN-US"}[日志的负载分担，但负载分担到不可达的日志主机的]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志会直接被丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_x167995861}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_x2044696406}[设置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志负载分担发送。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13802_12782_x2001448568}

[\[Sysname\] userlog flow export load-balancing]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_x172484319}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[userlog flow export host]{lang="EN-US"}**]{#struct_0_13802_12782_704435434}
:::

::: {#586221020 .myid}
[]{#_Toc404797421}[]{#struct_0_13802_12782_1176574213}[]{#_Toc257625719}

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export source-ip**

------------------------------------------------------------------------

[**[userlog]{lang="EN-US"}**[ **flow** **export** **source-ip**]{lang="EN-US"}]{#struct_0_13802_12782_x1092811055}[命令用来[]{#_Toc172445345}[]{#_Toc196023730}[]{#_Ref193185129}[]{#_Ref172456615}[]{#_Ref172447289}配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志报文的源地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **userlog** **flow export**]{lang="EN-US"}[ **source-ip**]{lang="EN-US"}]{#struct_0_13802_12782_1952607963}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_x370743505}

[**[userlog]{lang="EN-US"}**[ **flow** **export** **source-ip** *ip-address*]{lang="EN-US"}]{#struct_0_13802_12782_x424642755}

[**[undo]{lang="EN-US"}**[ **userlog** **flow** **export** **source-ip**]{lang="EN-US"}]{#struct_0_13802_12782_x980030765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13802_12782_x802339836}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_1775700599}[日志报文的源地址为发送该报文的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_x980274004}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13802_12782_324605620}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_729776050}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_1646542434}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_x1124181507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13802_12782_x2082168830}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13802_12782_1627762143}[：]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_x831710032}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_1762124473}[将]{style="font-family:宋体"}[1.2.1.2]{lang="EN-US"}[配置为]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志报文的源地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13802_12782_x206100963}

[\[Sysname\] userlog flow export source-ip 1.2.1.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_924512473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[userlog flow export host]{lang="DE"}**]{#struct_0_13802_12782_x370677969}
:::

::: {#497549098 .myid}
[]{#_Toc404797422}[]{#struct_0_13802_12782_1125206474}[]{#_Toc142995326}

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export version**

------------------------------------------------------------------------

[**[userlog]{lang="EN-US"}**[ **flow** **export** **version**]{lang="EN-US"}]{#struct_0_13802_12782_x115848467}[命令用来配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志报文的版本号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **userlog** **flow export** **version**]{lang="EN-US"}]{#struct_0_13802_12782_x1314752521}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_x376094683}

[**[userlog]{lang="EN-US"}**[ **flow** **export** **version** *version-number*]{lang="EN-US"}]{#struct_0_13802_12782_x481766401}

[**[undo userlog]{lang="DE"}**]{#struct_0_13802_12782_x1385288125}[ **flow** **export**]{lang="DE"}[ ]{lang="DE"}**[version]{lang="DE"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13802_12782_813889221}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x1869276957}[日志报文的版本号为]{style="font-family:宋体"}[1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_1015101212}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13802_12782_x268595092}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_606300213}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_x1519640704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_878629538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13802_12782_1371658315}

[*[version-number]{lang="DE"}*]{#struct_0_13802_12782_x1967026196}[：]{style="font-family:宋体"}[Flow]{lang="DE"}[日志报文的版本号，取值为]{style="font-family:
宋体"}[1]{lang="DE"}[或]{style="font-family:宋体"}[3]{lang="DE"}[，分别对应]{style="font-family:宋体"}[Flow1.0]{lang="DE"}[和]{style="font-family:宋体"}[Flow3.0]{lang="DE"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13802_12782_x145120919}

[[同一时刻只能使用一个版本，如果多次使用该命令配置版本，则最新的配置生效。]{style="font-family:宋体"}]{#struct_0_13802_12782_x370612433}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_x49419276}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_807746662}[将]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志报文版本号设为]{style="font-family:宋体"}[3.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13802_12782_x470808116}

[\[Sysname\] userlog flow export version 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_1608080938}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[userlog flow export host]{lang="EN-US"}**]{#struct_0_13802_12782_x23321620}
:::

::: {#-758424073 .myid}
[]{#_Toc404797423}[]{#struct_0_13802_12782_x160892741}[]{#_Toc142995327}

**Flow日志 \-- Flow日志配置命令 \-- userlog flow syslog**

------------------------------------------------------------------------

[**[userlog]{lang="DE"}**[ ]{lang="DE"}]{#struct_0_13802_12782_728500986}**[flow]{lang="DE"}**[ ]{lang="DE"}**[syslog]{lang="DE"}**[命令用来配置]{style="font-family:宋体"}[Flow]{lang="DE"}[日志输出到信息中心。]{style="font-family:宋体"}

[**[undo userlog]{lang="DE"}**[ ]{lang="DE"}]{#struct_0_13802_12782_x269210191}**[flow]{lang="DE"}**[ ]{lang="DE"}**[syslog]{lang="DE"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1690361703}

[**[userlog]{lang="EN-US"}**[ **flow** **syslog**]{lang="EN-US"}]{#struct_0_13802_12782_x1463080853}

[**[undo userlog]{lang="EN-US"}**[ **flow** **syslog**]{lang="EN-US"}]{#struct_0_13802_12782_2051650974}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13802_12782_1394415829}

[[Flow]{lang="EN-US"}]{#struct_0_13802_12782_1557247484}[日志输出到]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志主机。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1392118515}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13802_12782_x768045829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13802_12782_1651795816}

[[network-admin]{lang="EN-US"}]{#struct_0_13802_12782_x370546897}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13802_12782_1526644235}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13802_12782_1840996656}

[[配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_13802_12782_x931559662}[日志输出到信息中心时，需要注意：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[日志主机和信息中心两种输出方向互斥，默认输出方向为日志主机。如果配置了信息中心方向，则会忽略日志主机方向。]{style="font-family:宋体"}]{#struct_0_13802_12782_x1213525325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下，用户访问网络会在短时间内产生大量]{style="font-family:宋体"}]{#struct_0_13802_12782_1116536885}[NAT]{lang="EN-US"}[会话日志。系统日志传输格式为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码，相比]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志的二进制格式传输效率低。所以，建议在日志量较小的情况下，使用输出到信心中心的方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[日志输出至信息中心时，日志信息的优先级为]{style="font-family:宋体"}]{#struct_0_13802_12782_x1036379470}[informational]{lang="EN-US"}[，即作为设备的一般提示信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13802_12782_x697311862}

[[\# ]{lang="EN-US"}]{#struct_0_13802_12782_x1024806590}[设置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[日志输出到信息中心。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13802_12782_116891286}

[\[Sysname\] userlog flow syslog]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13802_12782_x1808909347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[userlog]{lang="EN-US"}**[ **flow** **export** **host**]{lang="EN-US"}]{#struct_0_13802_12782_x694108177}
:::
