::: {#-1354926751 .myid}
[]{#_Toc404784359}[]{#struct_0_x6236_x9207_1385075080}[]{#_Toc217294344}[]{#_Toc212028161}[]{#_Toc87257691}

**环路检测 \-- 环路检测调试命令 \-- debugging loopback-detection**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x561660303}

[**[debugging loopback-detection]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **vlan** *vlan-list* \] }]{lang="EN-US"}]{#struct_0_x6236_x9207_1248141701}

[**[undo debugging loopback-detection]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **vlan** *vlan-list* \] }]{lang="EN-US"}]{#struct_0_x6236_x9207_x234571694}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x1483641374}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6236_x9207_x436025015}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6236_x9207_229874343}

[[network-admin]{lang="EN-US"}]{#struct_0_x6236_x9207_1375456780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6236_x9207_x1117327315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6236_x9207_887699853}

[**[all]{lang="EN-US"}**]{#struct_0_x6236_x9207_x314922272}[：表示环路检测所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6236_x9207_x608048697}[：表示环路检测错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6236_x9207_x354052786}[：表示环路检测事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x6236_x9207_1937508455}[：表示环路检测报文调试信息开关。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6236_x9207_1941092685}[：表示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内环路检测报文的调试信息开关。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果不指定该参数，表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内环路检测报文的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x1566025064}

[**[debugging loopback-detection]{lang="EN-US"}**]{#struct_0_x6236_x9207_x640549907}[命令用来打开环路检测调试信息开关。]{style="font-family:
宋体"}**[undo debugging loopback-detection]{lang="EN-US"}**[命令用来关闭环路检测调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，环路检测调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x6236_x9207_1375391244}

[]{#struct_0_x6236_x9207_x1489780597}[[表1-1 ]{lang="EN-US"}[debugging loopback-detection error]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x918564832}[[字段]{style="font-family:黑体"}]{#struct_0_x6236_x9207_1062468960}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x684544402}

[[Dropped a length-invalid packet on interface *interface-name*]{lang="EN-US"}]{#struct_0_x6236_x9207_920196918}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6236_x9207_834821190}[上丢弃一个长度无效的报文]{style="font-family:宋体"}

[[Received a TLV-invalid message packet]{lang="EN-US"}]{#struct_0_x6236_x9207_x2059546052}

[[收到一个带有无效]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x6236_x9207_469322313}[消息的报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x6236_x9207_1375325708}[[表1-2 ]{lang="EN-US"}[debugging loopback-detection event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x892154752}[[字段]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x720137477}

[[描述]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x674722762}

[[Dropped a packet because loopback-detection is disabled]{lang="EN-US"}]{#struct_0_x6236_x9207_x388109351}

[[由于环路检测未使能，因此丢弃报文]{style="font-family:宋体"}]{#struct_0_x6236_x9207_x1203235801}

[[Succeeded to process an packet, it's device MAC is *mac-address*]{lang="EN-US"}]{#struct_0_x6236_x9207_158490684}

[[成功处理了一个报文，其设备]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x6236_x9207_1679384452}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[[Loop occurred on interface *interface-name*]{lang="EN-US"}]{#struct_0_x6236_x9207_x1088747624}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6236_x9207_1375260172}[上出现环路]{style="font-family:宋体"}

[[Loop recovered on interface *interface-name*]{lang="EN-US"}]{#struct_0_x6236_x9207_x1455868598}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6236_x9207_x546986634}[上的环路恢复]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x6236_x9207_1127699985}[[表1-3 ]{lang="EN-US"}[debugging loopback-detection packet]{lang="EN-US"}]{#_Toc130718929}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x892844332}[[字段]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x1492824807}

[[描述]{style="font-family:黑体"}]{#struct_0_x6236_x9207_443382562}

[[Succeeded to send a packet on interface *interface-name* in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_857847719}

[[在]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x371419863}[的端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上成功发送了一个报文]{style="font-family:宋体"}

[[Failed to send a packet on interface *interface-name* in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_1376243212}

[[在]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x812602909}[的端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上发送报文失败]{style="font-family:宋体"}

[[Succeeded to send a packet in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_1168697769}

[[在]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x1404992575}[中成功发送了一个报文]{style="font-family:宋体"}

[[Failed to send a packet in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x676143556}

[[在]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_1832941201}[中发送报文失败]{style="font-family:宋体"}

[[Received a packet on interface *interface-name* in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x1113743527}

[[在]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_1376177676}[的端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上收到了一个报文]{style="font-family:宋体"}

[[Succeeded to process a packet on interface *interface-name* in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x2027717646}

[[在]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x6236_x9207_x719056435}[的端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上成功处理了一个报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6236_x9207_x1604142351}

[[\# ]{lang="EN-US"}]{#struct_0_x6236_x9207_x1298303481}[打开环路检测错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging loopback-detection error]{lang="EN-US"}]{#struct_0_x6236_x9207_x573425362}

[\*Dec 22 14:09:53:859 2011 Sysname LPDT/7/Error: -MDC=1; Received a TLV-invalid message packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6236_x9207_1643208789}*[收到一个带有无效]{style="font-family:宋体"}[TLV]{lang="EN-US"}[消息的报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6236_x9207_1375718925}[打开环路检测事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging loopback-detection event]{lang="EN-US"}]{#struct_0_x6236_x9207_942641104}

[\*Dec 22 11:59:33:391 2011 Sysname LPDT/7/Event: -MDC=1;]{lang="NL"}[ ]{lang="NL"}[Dropped a packet because loopback-detection is disabled.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6236_x9207_x1876965989}*[由于环路检测未使能，因此丢弃报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6236_x9207_x710268888}[打开环路检测报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging loopback-detection packet]{lang="EN-US"}]{#struct_0_x6236_x9207_x1072400694}

[\*Dec 22 11:57:31:453 2011 Sysname LPDT/7/Packet: -MDC=1; Succeeded to send a packet in VLAN 6.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6236_x9207_857096218}*[在]{style="font-family:宋体"}[VLAN 6]{lang="EN-US"}[中成功发送了一个报文]{style="font-family:宋体"}*
