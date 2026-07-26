::: {#205717578 .myid}
[]{#_Toc404786683}[]{#struct_0_17203_65166_1694110537}[]{#_Toc130542926}[]{#_Toc69790789}

**UDP Helper \-- UDP Helper调试命令 \-- debugging udp-helper packet**

------------------------------------------------------------------------

[**[debugging udp-helper packet]{lang="EN-US" style="color:windowtext"}**]{#struct_0_17203_65166_x2068883314}[命令用来打开]{style="font-family:宋体;color:windowtext"}[UDP Helper]{lang="EN-US" style="color:windowtext"}[的报文调试信息开关。]{style="font-family:
宋体;color:windowtext"}

[**[undo debugging udp-helper packet]{lang="EN-US" style="color:windowtext"}**]{#struct_0_17203_65166_x718569185}[命令用来关闭]{style="font-family:宋体;
color:windowtext"}[UDP Helper]{lang="EN-US" style="color:windowtext"}[的报文调试信息开关。]{style="font-family:宋体;color:windowtext"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17203_65166_x1139731180}

[**[debugging udp-helper packet]{lang="EN-US"}**]{#struct_0_17203_65166_x848578973}

[**[undo debugging udp-helper packet]{lang="EN-US"}**]{#struct_0_17203_65166_711439882}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17203_65166_x111439852}

[[UDP Helper]{lang="EN-US"}]{#struct_0_17203_65166_1723531997}[的报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17203_65166_x1563449378}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17203_65166_x730022461}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17203_65166_232049378}

[[network-admin]{lang="EN-US"}]{#struct_0_17203_65166_x414546516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17203_65166_988527541}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17203_65166_x1139796716}

[[表1-1 ]{lang="EN-US"}[debugging udp-helper packet]{lang="EN-US"}]{#struct_0_17203_65166_469703925}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_653692105}[[字段]{style="font-family:黑体"}]{#struct_0_17203_65166_1007757873}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17203_65166_x2137489055}

[[Received a packet.]{lang="EN-US"}]{#struct_0_17203_65166_586385752}

[[收到一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_17203_65166_499806623}[报文]{style="font-family:宋体"}

[[Sent a packet.]{lang="EN-US"}]{#struct_0_17203_65166_1484139743}

[[发送一个中继后的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_17203_65166_1238754522}[报文]{style="font-family:宋体"}

[[src_addr]{lang="EN-US"}]{#struct_0_17203_65166_972440144}

[[UDP]{lang="EN-US"}]{#struct_0_17203_65166_x1734752870}[报文的源地址]{style="font-family:宋体"}

[[dst_addr]{lang="EN-US"}]{#struct_0_17203_65166_551948809}

[[UDP]{lang="EN-US"}]{#struct_0_17203_65166_x1510499979}[报文的目的地址]{style="font-family:宋体"}

[[dst_port]{lang="EN-US"}]{#struct_0_17203_65166_1904066343}

[[UDP]{lang="EN-US"}]{#struct_0_17203_65166_x904196828}[报文的目的端口号]{style="font-family:宋体"}

[[dst_vrf]{lang="EN-US"}]{#struct_0_17203_65166_1463669334}

[[UDP]{lang="EN-US"}]{#struct_0_17203_65166_1463538262}[报文的目的]{style="font-family:宋体"}[VRF]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[Failed to save packet header information to continuous storage space.]{lang="EN-US"}]{#struct_0_17203_65166_1238820058}

[[保存报文头在一块连续的空间里失败]{style="font-family:宋体"}]{#struct_0_17203_65166_1738675222}

[[Invalid UDP packet.]{lang="EN-US"}]{#struct_0_17203_65166_80661967}

[[无效的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_17203_65166_1687093369}[报文]{style="font-family:宋体"}

[[Destination address (*address*, vrf:*vrf_index*) is not reachable.]{lang="EN-US"}]{#struct_0_17203_65166_x591558289}

[[目的地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_17203_65166_x665681611}[不可达]{style="font-family:宋体"}

[[Failed to copy packet.]{lang="EN-US"}]{#struct_0_17203_65166_x1806717690}

[[复制报文失败]{style="font-family:宋体"}]{#struct_0_17203_65166_1238688986}

[[Failed to put the message to the queue.]{lang="EN-US"}]{#struct_0_17203_65166_1647229369}

[[报文入队列失败]{style="font-family:宋体"}]{#struct_0_17203_65166_417947020}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17203_65166_x2035081080}

[[\# ]{lang="EN-US"}]{#struct_0_17203_65166_x960635316}[打开]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[的收发报文调试信息开关，配置端口]{style="font-family:宋体"}[137]{lang="EN-US"}[收到的报文被转发到公网服务器]{style="font-family:宋体"}[192.168.3.252]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> terminal logging level 7]{lang="EN-US"}]{#struct_0_17203_65166_1239016666}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging udp-helper packet]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] udp-helper enable]{lang="EN-US"}

[\[Sysname\] udp-helper port 137]{lang="EN-US"}

[\[Sysname\] interface ethernet 1/1]{lang="EN-US"}

[\[Sysname-Ethernet1/1\] udp-helper server 192.168.3.252 global]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  8 11:11:45:238 2011 Sysname UDPH/7/PACKET: -MDC=1; Received a packet.]{lang="EN-US"}

[src_addr: 192.168.3.251, dst_addr: 255.255.255.255, dst_port: 137]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17203_65166_971844587}*[收到一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文，源地址为]{style="font-family:宋体"}[192.168.3.251]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[，目的端口号为]{style="font-family:宋体"}[137]{lang="EN-US"}*

[[\*Sep  8 11:11:45:239 2011 Sysname UDPH/7/PACKET: -MDC=1; Sent a packet. src_addr: 192.168.3.251, dst_addr: 192.168.3.252, dst_vrf: 0, dst_port: 137]{lang="EN-US"}]{#struct_0_17203_65166_x1658748904}

[*[// ]{lang="EN-US"}*]{#struct_0_17203_65166_x730207149}*[转发报文到公网服务器，被转发报文的源地址为]{style="font-family:宋体"}[192.168.3.251]{lang="EN-US"}[，目的地址被修改为]{style="font-family:宋体"}[192.168.3.252]{lang="EN-US"}[，目的端口号为]{style="font-family:宋体"}[137]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_17203_65166_1463603799}[打开]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[的收发报文调试信息开关，配置端口]{style="font-family:宋体"}[137]{lang="EN-US"}[收到的报文被转发到]{style="font-family:宋体"}[VPN a]{lang="EN-US"}[内的服务器]{style="font-family:宋体"}[192.168.3.252]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> terminal logging level 7]{lang="EN-US"}]{#struct_0_17203_65166_1463669335}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging udp-helper packet]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] udp-helper enable]{lang="EN-US"}

[\[Sysname\] udp-helper port 137]{lang="EN-US"}

[\[Sysname\] interface ethernet 1/1]{lang="EN-US"}

[\[Sysname-Ethernet1/1\] udp-helper server 192.168.3.252 vpn-instance a]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  8 11:11:45:238 2011 Sysname UDPH/7/PACKET: -MDC=1; Received a packet.]{lang="EN-US"}

[src_addr: 192.168.3.251, dst_addr: 255.255.255.255, dst_port: 137]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17203_65166_1463472727}*[收到一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文，源地址为]{style="font-family:宋体"}[192.168.3.251]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[，目的端口号为]{style="font-family:宋体"}[137]{lang="EN-US"}*

[[\*Sep  8 11:11:45:239 2011 Sysname UDPH/7/PACKET: -MDC=1; Sent a packet. src_addr: 192.168.3.251, dst_addr: 192.168.3.252, dst_vrf: 1, dst_port: 137]{lang="EN-US"}]{#struct_0_17203_65166_x1417134976}

[*[// ]{lang="EN-US"}*]{#struct_0_17203_65166_981833362}*[转发报文到私网索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[的服务器，被转发报文的源地址为]{style="font-family:宋体"}[192.168.3.251]{lang="EN-US"}[，目的地址被修改为]{style="font-family:宋体"}[192.168.3.252]{lang="EN-US"}[，目的端口号为]{style="font-family:宋体"}[137]{lang="EN-US"}*

[[\*May  30 15:06:20:484 2013 Sysname UDPH/7/PACKET: -MDC=1; Destination address(192.168.3.252, vrf:0) is not reachable*.*]{lang="EN-US"}]{#struct_0_17203_65166_1912653185}

[*[// ]{lang="EN-US"}*]{#struct_0_17203_65166_1463538263}*[私网索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[的目的地址]{style="font-family:宋体"}[192.168.3.252]{lang="EN-US"}[不可达]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
