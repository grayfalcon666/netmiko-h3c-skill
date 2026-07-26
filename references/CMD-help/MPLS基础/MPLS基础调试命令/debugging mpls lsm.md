::: {#-1297303585 .myid}
[]{#_Toc404790420}[]{#struct_0_x9704_x2783_2010473680}[]{#_Toc304293982}[]{#_Toc130266255}[]{#_Toc67195984}[]{#_Toc67145809}[]{#_Toc61012172}[]{#_Toc87257691}

**MPLS基础 \-- MPLS基础调试命令 \-- debugging mpls lsm**

------------------------------------------------------------------------

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x9704_x2783_x222385}

[**[debugging mpls lsm ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fec** \[ **asbr** \| **vpn-instance** *vpn-instance-name* \] { **ipv4** *destination mask* \| **ipv6** *destination mask* } \| **hsb** \| **label** \| **process** \| **tunnel** }]{lang="EN-US"}]{#struct_0_x9704_x2783_x1150171959}

[**[undo debugging mpls lsm]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fec** { **ipv4** \| **ipv6** } \| **hsb** \| **label** \| **process** \| **tunnel** }]{lang="EN-US"}]{#struct_0_x9704_x2783_x355853990}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_1993446723}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x444907167}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_718654118}

[[1]{lang="EN-US"}]{#struct_0_x9704_x2783_x931868180}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x427033693}

[**[all]{lang="EN-US"}**]{#struct_0_x9704_x2783_x1082630596}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x9704_x2783_444715899}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x9704_x2783_x253635759}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[fec]{lang="EN-US"}**]{#struct_0_x9704_x2783_x1611093049}[：表示指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_x9704_x2783_35574408}[：表示指定]{style="font-family:宋体"}[ASBR LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x9704_x2783_x1401613034}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[ipv4 ]{lang="EN-US"}***[destination mask]{lang="EN-US"}*]{#struct_0_x9704_x2783_x965493597}[：表示指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[IPv4 LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[调试信息开关信息。]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *destination mask*]{lang="EN-US"}]{#struct_0_x9704_x2783_x1744797924}[：表示指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[BGP-IPv6 LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hsb]{lang="EN-US"}**]{#struct_0_x9704_x2783_x427099229}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[热备份事件的调试信息开关。]{style="font-family:宋体"}

[**[label]{lang="EN-US"}**]{#struct_0_x9704_x2783_x1136846359}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[标签分配管理的调试信息开关。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}**]{#struct_0_x9704_x2783_1572575004}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[隧道管理的调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_x9704_x2783_x712338892}[：表示]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[处理过程的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x795379926}

[**[debugging mpls lsm]{lang="EN-US"}**]{#struct_0_x9704_x2783_1318784110}[命令用来打开]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[（]{style="font-family:宋体"}[Label Switch Management]{lang="EN-US"}[，标签交换管理）的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls lsm]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}]{#struct_0_x9704_x2783_x2135566543}[的调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x847964965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x426902621}[LSM]{lang="EN-US"}[运行出现问题时，可以通过]{style="font-family:宋体"}**[debugging mpls lsm]{lang="EN-US"}**[命令进行故障定位。但这条命令的执行会影响系统性能，因此建议谨慎使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9704_x2783_1999825649}**[debugging mpls lsm all]{lang="NO-BOK"}**[命令可以打开除]{lang="EN-US" style="font-family:
宋体"}**[fec]{lang="EN-US"}**[外]{lang="EN-US" style="font-family:宋体"}[所有的]{lang="EN-US" style="font-family:宋体"}[MPLS LSM]{lang="NO-BOK"}[调试信息开关；执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="NO-BOK"}[ debugging mpls lsm all]{lang="NO-BOK"}**[命令可以关闭包括]{lang="EN-US" style="font-family:宋体"}**[fec]{lang="EN-US"}**[在内的所有]{lang="EN-US" style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[调试开关。]{lang="EN-US" style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mpls lsm error]{lang="EN-US"}]{#struct_0_x9704_x2783_708162938}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x281536121}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x1093325695}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x730403821}

[[Failed to open the file]{lang="EN-US"}]{#struct_0_x9704_x2783_1037784879}

[[打开文件失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1250443861}

[[Failed to write the file]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1083652422}

[[写文件失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x426968157}

[[Failed to download a configuration command]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1905351022}

[[配置下发驱动失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1306694466}

[[Failed to recover from binary configurations]{lang="PT-BR"}]{#struct_0_x9704_x2783_x2121770715}

[[二进制配置信息恢复失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1956810330}

[[Failed to backup configurations in batches]{lang="PT-BR"}]{#struct_0_x9704_x2783_x289070070}

[[配置批量备份失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x426771549}

[[Invalid TLV]{lang="PT-BR"}]{#struct_0_x9704_x2783_1229157906}

[[接收消息中存在无效]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9704_x2783_1960623910}

[[Unknown signalling]{lang="PT-BR"}]{#struct_0_x9704_x2783_x696405670}

[[非法信令类型]{style="font-family:宋体"}]{#struct_0_x9704_x2783_136610812}

[[Unknown signalling message type]{lang="PT-BR"}]{#struct_0_x9704_x2783_1037676243}

[[非法的信令消息类型]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x426837085}

[[Failed to analyze the signalling message]{lang="PT-BR"}]{#struct_0_x9704_x2783_1249611081}

[[解析信令消息失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x635455433}

[[Received an invalid HA message]{lang="PT-BR"}]{#struct_0_x9704_x2783_1379244942}

[[收到一个无效的]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x9704_x2783_x1025439815}[消息]{style="font-family:宋体"}

[[Invalid LSP index]{lang="EN-US"}]{#struct_0_x9704_x2783_x427295840}

[[无效的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x9704_x2783_x1907580191}[索引值]{style="font-family:宋体"}

[[Failed to allocate a NID]{lang="EN-US"}]{#struct_0_x9704_x2783_1913477821}

[[申请]{style="font-family:宋体"}[NID]{lang="EN-US"}]{#struct_0_x9704_x2783_x999720642}[失败]{style="font-family:宋体"}

[[Failed to set the NID]{lang="PT-BR"}]{#struct_0_x9704_x2783_x427361376}

[[设置]{style="font-family:宋体"}[NID]{lang="EN-US"}]{#struct_0_x9704_x2783_486700441}[失败]{style="font-family:宋体"}

[[Failed to free the NID]{lang="PT-BR"}]{#struct_0_x9704_x2783_x2040524490}

[[释放]{style="font-family:宋体"}[NID]{lang="EN-US"}]{#struct_0_x9704_x2783_x83653195}[失败]{style="font-family:宋体"}

[[Failed to update the LSP]{lang="PT-BR"}]{#struct_0_x9704_x2783_x143626786}

[[更新]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x9704_x2783_x427164768}[失败]{style="font-family:宋体"}

[[Failed to add ]{lang="PT-BR"}[an FTN entry]{lang="EN-US"}]{#struct_0_x9704_x2783_x1038406045}

[[添加]{style="font-family:宋体"}[FTN]{lang="EN-US"}]{#struct_0_x9704_x2783_x1067952112}[表项失败]{style="font-family:宋体"}

[[Failed to add a cross-connected entry]{lang="PT-BR"}]{#struct_0_x9704_x2783_x516917053}

[[添加]{style="font-family:宋体"}[XC]{lang="EN-US"}]{#struct_0_x9704_x2783_x427230304}[表项失败]{style="font-family:宋体"}

[[Failed to add all the LSPs]{lang="PT-BR"}]{#struct_0_x9704_x2783_2041446582}

[[添加]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1663335471}[FEC]{lang="PT-BR"}[下的所有等价]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[失败]{style="font-family:宋体"}

[[Failed to send an LSP entry to TNLC when creating the LSP]{lang="PT-BR"}]{#struct_0_x9704_x2783_757701366}

[[向隧道管理通告]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x9704_x2783_x427033696}[隧道表项失败]{style="font-family:宋体"}

[[Failed to send an LSP entry to LFIB when creating the LSP]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1082958276}

[[向]{style="font-family:宋体"}[LFIB]{lang="EN-US"}]{#struct_0_x9704_x2783_833672652}[下发]{style="font-family:宋体"}[LSP]{lang="EN-US"}[表项失败]{style="font-family:宋体"}

[[Failed to send an LSP entry to HA when creating the LSP]{lang="EN-US"}]{#struct_0_x9704_x2783_x1434892951}

[[LSP]{lang="EN-US"}]{#struct_0_x9704_x2783_x427099232}[创建时向]{style="font-family:宋体"}[HA]{lang="EN-US"}[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[表项失败]{style="font-family:宋体"}

[[Failed to release the label]{lang="EN-US"}]{#struct_0_x9704_x2783_x1137305112}

[[释放标签失败]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1517240804}

[[Label *label* is in bad status, and a notification was sent to signaling *signal* ]{lang="EN-US"}]{#struct_0_x9704_x2783_x426902624}

[[标签]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1999629041}[状态错误，发送通知信息给信令协议]{style="font-family:宋体"}*[signal]{lang="PT-BR"}*

*[ ]{lang="EN-US"}*

[[表1-2 ]{lang="EN-US"}[debugging mpls lsm event]{lang="EN-US"}]{#struct_0_x9704_x2783_x1591853324}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x527412388}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x1570049917}

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x476583905}

[[Received and processed an interface event. Interface index: *ifIndex*; event: *event*; result: *result*]{lang="EN-US"}]{#struct_0_x9704_x2783_x351308037}

[[收到并处理接口事件。接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*]{#struct_0_x9704_x2783_x426968160}[；接口事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[；处理结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Notify interface management that the process of the event completed]{lang="EN-US"}]{#struct_0_x9704_x2783_x1905678705}[ ]{lang="EN-US"}

[[通知接口管理事件处理完成]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x318914578}

[[VRF added]{lang="PT-BR"}[ successfully]{lang="EN-US"}]{#struct_0_x9704_x2783_1406182761}

[[添加]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x9704_x2783_x2023343465}[成功]{style="font-family:宋体"}

[[VRF deleted successfully]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1434575885}

[[删除]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x9704_x2783_x426771552}[成功]{style="font-family:宋体"}

[[Application *applicationID* session event: Received an init message]{lang="PT-BR"}]{#struct_0_x9704_x2783_1229485587}

[[应用]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1502095981}*[applicationID]{lang="PT-BR"}*[的]{style="font-family:宋体"}[会话事件：收到初始化消息]{style="font-family:宋体"}

[[Application *applicationID* session event: Recovery completed]{lang="PT-BR"}]{#struct_0_x9704_x2783_650517137}

[[应用]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1059093153}*[applicationID]{lang="PT-BR"}*[的]{style="font-family:宋体"}[会话事件：恢复完成]{style="font-family:宋体"}

[[Application session event: LIPC down]{lang="PT-BR"}]{#struct_0_x9704_x2783_424789827}

[[应用会话事件：进程间通信连接断开]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x426837088}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mpls lsm hsb]{lang="EN-US"}]{#struct_0_x9704_x2783_1250331977}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x527477523}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x1866223464}

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x982667334}

[[Sent an HA messa]{lang="PT-BR"}[ge. Message type: *messageType*, length: *length*]{lang="EN-US"}]{#struct_0_x9704_x2783_580887290}

[[发送备份消息，消息类型为]{style="font-family:宋体"}*[messageType]{lang="EN-US"}*]{#struct_0_x9704_x2783_x246011832}[，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Received an HA message]{lang="PT-BR"}[. Message type: *messageType*, length: *length*]{lang="EN-US"}]{#struct_0_x9704_x2783_747865350}

[[收到备份消息，消息类型为]{style="font-family:宋体"}*[messageType]{lang="EN-US"}*]{#struct_0_x9704_x2783_x427295839}[，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging mpls lsm label]{lang="EN-US"}]{#struct_0_x9704_x2783_x1906990366}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x526375760}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x400634292}

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_1105839127}

[[Label *label* released successfully]{lang="EN-US"}]{#struct_0_x9704_x2783_1308834903}

[[成功释放标签]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1903495858}

[[Label segment is available]{lang="PT-BR"}]{#struct_0_x9704_x2783_x427361375}

[[标签段可用]{style="font-family:宋体"}]{#struct_0_x9704_x2783_486503833}

[[Claim label *label*]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1888970256}

[[申请指定标签]{style="font-family:宋体"}]{#struct_0_x9704_x2783_52705076}

[[Refresh label *label*, signalling *signal*]{lang="PT-BR"}]{#struct_0_x9704_x2783_x882742318}

[[刷新标签]{style="font-family:宋体"}]{#struct_0_x9704_x2783_28138456}*[label]{lang="PT-BR"}*[，信令协议为]{style="font-family:宋体"}*[signal]{lang="PT-BR"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging mpls lsm tunnel]{lang="EN-US"}]{#struct_0_x9704_x2783_1401836240}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x531426840}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x427164767}

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x1037554077}

[[Fetch the tunnels. Destination: *destAddr*, ECMP number: *number*]{lang="EN-US"}]{#struct_0_x9704_x2783_1158236974}

[[获取到目的地址]{style="font-family:宋体"}*[destAddr]{lang="EN-US"}*]{#struct_0_x9704_x2783_1763338674}[的隧道，等价隧道数目为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Notify the status event (*event*) of tunnel with destination *destAddr* to application ]{lang="EN-US"}]{#struct_0_x9704_x2783_x962941161}*[applicationID]{lang="PT-BR"}*

[[向应用]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x72903106}*[applicationID]{lang="PT-BR"}*[通告隧道状态变化事件，隧道目的地址为]{style="font-family:宋体"}*[destAddr]{lang="EN-US"}[，]{style="font-family:宋体"}*[隧道状态变化事件包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x9704_x2783_x856066804}[：隧道增加]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x9704_x2783_x427230303}[：隧道删除]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x9704_x2783_2041643190}[：隧道更新]{lang="EN-US" style="font-family:
  宋体"}

[[Notify the status event (]{lang="PT-BR"}*[event]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1107311883}[) of tunnel policy (*policyName*) to application *applicationID*]{lang="PT-BR"}

[[向应用]{style="font-family:宋体"}]{#struct_0_x9704_x2783_988560057}*[applicationID]{lang="PT-BR"}*[通告隧道策略变化事件。隧道策略名称为]{style="font-family:宋体"}*[policyName]{lang="PT-BR"}*[，]{style="font-family:宋体"}[隧道策略变化事件包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x9704_x2783_x2041998127}[：策略增加]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x9704_x2783_x427033695}[：策略删除]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x9704_x2783_x1082761668}[：策略更新]{lang="EN-US" style="font-family:
  宋体"}

[[Process LSP message. Destination: ]{lang="PT-BR"}*[destAddr]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1449766215}[, Tunnel ifindex:]{lang="PT-BR"}[ ]{lang="PT-BR"}*[interfaceIndex]{lang="PT-BR"}*[, event type: *event*, result: ]{lang="PT-BR"}*[result]{lang="EN-US"}*[.]{lang="PT-BR"}

[[处理]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1175786927}[LSP]{lang="PT-BR"}[隧道消息。隧道目的地址为]{style="font-family:宋体"}*[destAddr]{lang="PT-BR"}*[，]{style="font-family:宋体"}[隧道接口索引为]{style="font-family:宋体"}*[interfaceIndex]{lang="PT-BR"}*[，事件类型为]{style="font-family:宋体"}*[event]{lang="PT-BR"}*[，处理结果为]{style="font-family:宋体"}*[result]{lang="PT-BR"}*

[[TNLC received an LSP message. Destination: ]{lang="PT-BR"}*[destAddr]{lang="EN-US"}*]{#struct_0_x9704_x2783_1012738894}[, event type: *event*, ECMP number: ]{lang="PT-BR"}*[number]{lang="EN-US"}*[.]{lang="PT-BR"}

[[隧道控制模块]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x152917611}[收到]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[隧道消息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[隧道目的地址为]{style="font-family:宋体"}*[destAddr]{lang="PT-BR"}*[，事件类型为]{style="font-family:宋体"}*[event]{lang="PT-BR"}*[，等价隧道数目为]{style="font-family:宋体"}*[number]{lang="PT-BR"}*

[ ]{lang="PT-BR"}

[[表1-6 ]{lang="EN-US"}[debugging mpls lsm process]{lang="EN-US"}]{#struct_0_x9704_x2783_x427099231}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x531797949}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x1137370648}

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x1182500126}

[[Configuration commands applied to drive successfully]{lang="PT-BR"}[ ]{lang="PT-BR"}]{#struct_0_x9704_x2783_x505943319}

[[成功下发配置命令到驱动]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x103187158}

[[Allocate a NID successfully]{lang="EN-US"}]{#struct_0_x9704_x2783_1832799917}

[[成功申请]{style="font-family:宋体"}[NID]{lang="EN-US"}]{#struct_0_x9704_x2783_x300333832}

[[Set the NID ]{lang="PT-BR"}[successfully]{lang="EN-US"}]{#struct_0_x9704_x2783_x426902623}

[[成功设置]{style="font-family:宋体"}[NID]{lang="EN-US"}]{#struct_0_x9704_x2783_1999694577}

[[Release the NID]{lang="PT-BR"}[ successfully]{lang="EN-US"}]{#struct_0_x9704_x2783_730802896}

[[成功释放]{style="font-family:宋体"}[NID]{lang="EN-US"}]{#struct_0_x9704_x2783_425242430}

[[LSP updated successfully. XC index: *XcIndex*, Inseg index: *InSegmentIndex*, Outseg index: *OutSegmentIndex*, FTN index: *FtnIndex*, Serve FLag: *ServeFlag*.]{lang="PT-BR"}]{#struct_0_x9704_x2783_715472422}

[[成功更新]{style="font-family:宋体"}]{#struct_0_x9704_x2783_2107848792}[LSP]{lang="PT-BR"}[信息。]{style="font-family:宋体"}[XC]{lang="PT-BR"}[索引为]{style="font-family:宋体"}*[XcIndex]{lang="PT-BR"}*[，入方向索引为]{style="font-family:宋体"}*[InSegmentIndex]{lang="PT-BR"}*[，出方向索引为]{style="font-family:宋体"}*[OutSegmentIndex]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FTN]{lang="PT-BR"}[索引为]{style="font-family:宋体"}*[FtnIndex]{lang="PT-BR"}*[，统计使能标记为]{style="font-family:宋体"}*[ServeFlag]{lang="PT-BR"}*

[[LSP added successfully. XC index: *XcIndex*, Inseg index: *InSegmentIndex*, Outseg index: *OutSegmentIndex*, FTN index: *FtnIndex*, Serve FLag: *ServeFlag*.]{lang="PT-BR"}]{#struct_0_x9704_x2783_x426968159}

[[成功添加]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1906268526}[LSP]{lang="PT-BR"}[信息。]{style="font-family:宋体"}[XC]{lang="PT-BR"}[索引为]{style="font-family:宋体"}*[XcIndex]{lang="PT-BR"}*[，入方向索引为]{style="font-family:宋体"}*[InSegmentIndex]{lang="PT-BR"}*[，出方向索引为]{style="font-family:宋体"}*[OutSegmentIndex]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FTN]{lang="PT-BR"}[索引为]{style="font-family:宋体"}*[FtnIndex]{lang="PT-BR"}*[，统计使能标记为]{style="font-family:宋体"}*[ServeFlag]{lang="PT-BR"}*

[[LSP deleted successfully. XC index: *XcIndex*, Inseg index: *InSegmentIndex*, Outseg index: *OutSegmentIndex*, FTN index: *FtnIndex*]{lang="PT-BR"}]{#struct_0_x9704_x2783_926572115}

[[成功删除]{style="font-family:宋体"}]{#struct_0_x9704_x2783_175826451}[LSP]{lang="PT-BR"}[信息。]{style="font-family:宋体"}[XC]{lang="PT-BR"}[索引为]{style="font-family:宋体"}*[XcIndex]{lang="PT-BR"}*[，入方向索引为]{style="font-family:宋体"}*[InSegmentIndex]{lang="PT-BR"}*[，出方向索引为]{style="font-family:宋体"}*[OutSegmentIndex]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FTN]{lang="PT-BR"}[索引为]{style="font-family:宋体"}*[FtnIndex]{lang="PT-BR"}*

[[Slave: Fill the LSP table. Version: *EntryVersion*, Flag: *LspFlag*, SigID: *LsmSig*, FEC info: type *type*, ip address *address*, mask length *length*, vrf index *index*, Inseg: in-label *InLabel*, in-ifindex *ifIndex*, ECMP: *OutSegNum*]{lang="PT-BR"}]{#struct_0_x9704_x2783_189551335}

[[备进程填充]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x714933706}[LSP]{lang="PT-BR"}[表项。版本号为]{style="font-family:宋体"}*[EntryVersion]{lang="PT-BR"}*[，]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[操作标记为]{style="font-family:宋体"}*[LspFlag]{lang="PT-BR"}*[，信令协议类型为]{style="font-family:宋体"}*[LsmSig]{lang="PT-BR"}*

[[FEC]{lang="PT-BR"}]{#struct_0_x9704_x2783_x426771551}[信息：]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[类型为]{style="font-family:宋体"}*[type]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[目的地址为]{style="font-family:宋体"}*[address]{lang="PT-BR"}*[，目的地址掩码为]{style="font-family:宋体"}*[length]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[所属]{style="font-family:宋体"}[VPN]{lang="PT-BR"}[的索引为]{style="font-family:宋体"}*[index]{lang="PT-BR"}*

[[入方向信息：入标签为]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1229682195}*[InLabel]{lang="PT-BR"}*[，入接口为]{style="font-family:宋体"}*[ifIndex]{lang="PT-BR"}*

[[等价数目为]{style="font-family:宋体"}]{#struct_0_x9704_x2783_21961947}*[OutSegNum]{lang="PT-BR"}*

[[Master: Fill the LSP table. Version: *EntryVersion*, Flag: *LspFlag*, SigID: *LsmSig*, FEC info: type *type*, ip address *address*, mask length *length*, vrf index *index*, Inseg: in-label *InLabel*, in-ifindex *ifIndex*, ECMP: *OutSegNum*]{lang="PT-BR"}]{#struct_0_x9704_x2783_927996666}

[[主进程填充]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x426837087}[LSP]{lang="PT-BR"}[表项。版本号为]{style="font-family:宋体"}*[EntryVersion]{lang="PT-BR"}*[，]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[操作标记为]{style="font-family:宋体"}*[LspFlag]{lang="PT-BR"}*[，信令协议类型为]{style="font-family:宋体"}*[LsmSig]{lang="PT-BR"}*

[[FEC]{lang="PT-BR"}]{#struct_0_x9704_x2783_1249480009}[信息：]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[类型为]{style="font-family:宋体"}*[type]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[目的地址为]{style="font-family:宋体"}*[address]{lang="PT-BR"}*[，目的地址掩码为]{style="font-family:宋体"}*[length]{lang="PT-BR"}*[，]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[所属]{style="font-family:宋体"}[VPN]{lang="PT-BR"}[的索引为]{style="font-family:宋体"}*[index]{lang="PT-BR"}*

[[入方向信息：入标签为]{style="font-family:宋体"}]{#struct_0_x9704_x2783_915751762}*[InLabel]{lang="PT-BR"}*[，入接口为]{style="font-family:宋体"}*[ifIndex]{lang="PT-BR"}*

[[等价数目为]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x1503194537}*[OutSegNum]{lang="PT-BR"}*

[[Outseg info: type *OutType*, out-ifindex *ifIndex*, next-hop *IpAddr*, out-label *OutLabel*, outgoing NID *OutgoingNid*, TPID *TPID*, backup out-ifindex *ifIndexFrr*]{lang="PT-BR"}]{#struct_0_x9704_x2783_x27928958}

[[处理的]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1138788105}[LSP]{lang="PT-BR"}[表项的出方向信息。类型为]{style="font-family:宋体"}*[OutType]{lang="PT-BR"}[，]{style="font-family:宋体"}*[出接口为]{style="font-family:宋体"}*[ifIndex]{lang="PT-BR"}[，]{style="font-family:宋体"}*[下一跳为]{style="font-family:宋体"}*[IpAddr]{lang="PT-BR"}*[，出标签为]{style="font-family:宋体"}*[OutLabel]{lang="PT-BR"}*[，出方向]{style="font-family:宋体"}[NID]{lang="PT-BR"}[为]{style="font-family:宋体"}*[OutgoingNid]{lang="PT-BR"}*[，策略]{style="font-family:宋体"}[ID]{lang="PT-BR"}[为]{style="font-family:宋体"}*[TPID]{lang="PT-BR"}*[，备份出接口为]{style="font-family:宋体"}*[ifIndexFrr]{lang="PT-BR"}*

[[ILM downloading. Operation: *OperType*, in-label: *InLabel*, length: *length*]{lang="PT-BR"}]{#struct_0_x9704_x2783_50772370}

[[下发]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1855876047}[ILM]{lang="PT-BR"}[表项：操作类型为]{style="font-family:宋体"}*[OperType]{lang="PT-BR"}*[，入标签为]{style="font-family:宋体"}*[InLabel]{lang="PT-BR"}*[，长度为]{style="font-family:宋体"}*[length]{lang="PT-BR"}*

[[NHLFE downloading. Operation: *OperType*, NID: *nid*, length: *length*]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1484363669}

[[下发]{style="font-family:宋体"}]{#struct_0_x9704_x2783_1138722569}[NHLFE]{lang="PT-BR"}[表项：操作类型为]{style="font-family:宋体"}*[OperType]{lang="PT-BR"}*[，]{style="font-family:宋体"}[NID]{lang="PT-BR"}[为]{style="font-family:宋体"}*[nid]{lang="PT-BR"}*[，长度为]{style="font-family:宋体"}*[length]{lang="PT-BR"}*

[ ]{lang="PT-BR"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_113507830}

[[\# ]{lang="PT-BR"}]{#struct_0_x9704_x2783_x23741965}[打开]{style="font-family:宋体"}[MPLS LSM]{lang="PT-BR"}[的事件调试信息开关。断开]{style="font-family:宋体"}[L3VPN]{lang="PT-BR"}[应用与]{style="font-family:宋体"}[LSM]{lang="PT-BR"}[的连接]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并重建该连接时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls lsm event ]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1599860013}

[\*May 12 06:34:53:514 2010 Sy]{lang="PT-BR"}[sname LSM/7/EVENT:]{lang="EN-US"}

[Application session event: LIPC down.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_2072638190}*[应用连接断开]{style="font-family:宋体"}*

[[\*May 12 06:35:00:116 2010 Sysname LSM/7/EVENT:]{lang="EN-US"}]{#struct_0_x9704_x2783_x2139585559}

[Application 2 session event: Received an init message.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_947173163}*[收到]{style="font-family:宋体"}[连接初始化消息]{style="font-family:宋体"}*

[[\*May 12 06:35:00:117 2010 Sysname LSM/7/EVENT:]{lang="EN-US"}]{#struct_0_x9704_x2783_1588518422}

[Application 2 session event: Recover completed.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x9704_x2783_1138919177}*[连接恢复完成]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x9704_x2783_1627800628}[打开]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的错误调试信息开关。当标签]{style="font-family:宋体"}[1024]{lang="EN-US"}[已经被使用的情况下，新创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重复使用]{style="font-family:宋体"}[1024]{lang="EN-US"}[标签时，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls lsm error]{lang="EN-US"}]{#struct_0_x9704_x2783_x815123751}

[\*May 12 09:02:25:795 2010 Sysname LSM/7/ERROR:]{lang="EN-US"}

[Label 1024 is in bad status, and a notification was sent to signaling 3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_1780773958}*[标签冲突，通知信令]{style="font-family:宋体"}[LSP]{lang="EN-US"}[处理失败。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x9704_x2783_x566558096}[打开]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的热备份事件调试信息开关。发送一条实时备份消息时，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls lsm hsb]{lang="EN-US"}]{#struct_0_x9704_x2783_x1437893549}

[\*May 7 17:33:22:796 2010 Sysname LSM/7/HSB:]{lang="EN-US"}

[Sent an HA message. Message type: 1, length: 80.  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_2138878149}*[发送备份消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x9704_x2783_57519214}[打开]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的标签分配管理调试信息开关。申请指定标签时，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls lsm label]{lang="EN-US"}]{#struct_0_x9704_x2783_1138853641}

[\*May 12 09:11:17:560 2010 Sysname LSM/7/LABEL:]{lang="EN-US"}

[Claim label 1025, result 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1060337486}*[成功申请标签]{style="font-family:宋体"}[1025]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x9704_x2783_x318224427}[打开]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的隧道管理调试信息开关。处理并生成一条]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道时，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls lsm tunnel]{lang="EN-US"}]{#struct_0_x9704_x2783_x931290011}

[\*May 7 14:51:51:08 2010 Sysname LSM/7/TUNNEL:]{lang="EN-US"}

[TNLC received an LSP message. Destination: 0xdedee9e9, event type: 1, ECMP number:]{lang="EN-US"}

[1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_1565123056}*[隧道控制模块收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道消息]{style="font-family:宋体"}*

[[\*May 7 14:51:51:13 2010 Sysname LSM/7/TUNNEL:]{lang="EN-US"}]{#struct_0_x9704_x2783_x966676096}

[Notify the status event (1) of tunnel with destination dedee9e9 to application 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1110581969}*[通告隧道状态变化事件]{style="font-family:宋体"}*

[[\*May  7 14:51:51:15 2010 Sysname LSM/7/TUNNEL:]{lang="EN-US"}]{#struct_0_x9704_x2783_1139050249}

[Process LSP message. Destination: 0xdedee9e9, Tunnel ifindex :0, event type: 1,]{lang="EN-US"}

[result: 0.  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1475341025}*[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道消息的结果]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1458130242}[打开]{style="font-family:宋体"}[MPLS LSM]{lang="EN-US"}[的处理过程调试信息开关。处理并生成一条]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[表项时，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls lsm process]{lang="PT-BR"}]{#struct_0_x9704_x2783_1343109403}

[\*May 12 09:20:58:749 2010 ]{lang="PT-BR"}[Sysname ]{lang="EN-US"}[LSM/7/PROCESS:]{lang="PT-BR"}

[Master: Fill the LSP table. Version: 0, Flag: 0x18, SigID: 3, FEC info: type 17, ip address 1.1.1.1, mask length 32, vrf index 0, Inseg: in-label 1028, in-ifindex]{lang="PT-BR"}

[ 136479, ECMP: 1.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x9704_x2783_x855810774}*[处理的]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[消息的]{style="font-family:宋体"}[FEC]{lang="PT-BR"}[和入方向信息]{style="font-family:宋体"}*

[[\*May 12 09:20:58:752 2010 Sysname LSM/7/PROCESS:]{lang="PT-BR"}]{#struct_0_x9704_x2783_823325450}

[Outseg info: type 65, out-ifindex 136479, next-hop 12.12.12.2, out-label 1025, outgoing NID 4294967295, TPID 65535, backup out-ifindex 0.]{lang="PT-BR"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_1771003002}*[处理的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[消息出方向信息]{style="font-family:宋体"}*

[[\*May 12 09:20:58:754 2010 ]{lang="PT-BR"}[Sysname ]{lang="EN-US"}]{#struct_0_x9704_x2783_1138984713}[LSM/7/PROCESS:]{lang="PT-BR"}

[LSP updated successfully. XC index: 2, Inseg index: 3, Outseg index: 2, FTN index: 2, Serve FLag:0x1.]{lang="PT-BR"}

[*[// LSP]{lang="PT-BR"}*]{#struct_0_x9704_x2783_516505993}*[表项更新成功]{style="font-family:宋体"}*

[[\*May 12 09:20:58:765 2010 Sysname LSM/7/PROCESS:]{lang="PT-BR"}]{#struct_0_x9704_x2783_x1791946100}

[NHLFE downloading. Operation: 5, NID: 2049, result: 0.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x9704_x2783_578661594}*[下发]{style="font-family:宋体"}[NHLFE]{lang="PT-BR"}[表项]{style="font-family:宋体"}*

[[\*May 12 09:20:58:765 2010 Sysname LSM/7/PROCESS:]{lang="PT-BR"}]{#struct_0_x9704_x2783_x557339074}

[ILM downloading. Operation: 1, in-label: 1025, result: 0.]{lang="PT-BR"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1089002883}*[下发]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项]{style="font-family:宋体"}*

::: {#1498124939 .myid}
[]{#_Toc404790421}[]{#struct_0_x9704_x2783_1617433499}[]{#_Toc304293983}[]{#_Toc275244325}[]{#_Toc130266256}

**MPLS基础 \-- MPLS基础调试命令 \-- debugging mpls packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_1558095576}

[**[debugging mpls packet]{lang="EN-US"}**[ \[ **acl** *acl-number* \| **acl6** *acl6-number* \] \[ **inlabel** *outer-in-label* \[ *inner-in-label* \] \] ]{lang="EN-US"}]{#struct_0_x9704_x2783_1139181321}

[**[undo debugging mpls packet]{lang="EN-US"}**]{#struct_0_x9704_x2783_2044371039}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_2139925326}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x259801016}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x491946383}

[[1]{lang="EN-US"}]{#struct_0_x9704_x2783_x1268772920}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_778977588}

[**[acl]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_x9704_x2783_1531814949}[：输出符合]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配条件的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的调试信息]{style="font-family:宋体"}[, *acl-number*]{lang="EN-US"}[为高级访问控制列表号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[acl6 ]{lang="EN-US"}***[acl6-number]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1900019660}[：输出符合]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[匹配条件的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的调试信息，]{style="font-family:宋体"}*[acl6-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[高级访问控制列表号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inlabel]{lang="EN-US"}**]{#struct_0_x9704_x2783_1945965817}[：输出具有指定入标签值的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的调试信息。]{style="font-family:宋体"}

[*[outer-in-label]{lang="EN-US"}*]{#struct_0_x9704_x2783_1139115785}[：外层入标签，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[inner-in-label]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1034826259}[：内层入标签，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_1888141020}

[**[debugging mpls packet]{lang="EN-US"}**]{#struct_0_x9704_x2783_x1961956372}[命令用来打开]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文转发调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文转发调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_x853602680}[报文转发调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[[表1-7 ]{lang="EN-US"}]{.TableTextChar}[[debugging mpls packet]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}]{#struct_0_x9704_x2783_960629149}[[命令输出信息描述表]{style="font-size:9.0pt;
font-family:黑体"}]{.TableTextChar}

[]{#table_struct_0_x534955609}[[字段]{style="font-family:黑体"}]{#struct_0_x9704_x2783_x990005673}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9704_x2783_2048033551}

[[MPLS Input]{lang="EN-US"}]{#struct_0_x9704_x2783_1139312393}

[[收到]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_1652031085}[报文]{style="font-family:宋体"}

[[MPLS Forward]{lang="EN-US"}]{#struct_0_x9704_x2783_1602138221}

[[转发]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_35047588}[报文]{style="font-family:宋体"}

[[MPLS Output]{lang="EN-US"}]{#struct_0_x9704_x2783_x1600276282}

[[发送]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_1814735834}[报文]{style="font-family:宋体"}

[[Receiving from interface *interface-name*]{lang="EN-US"}]{#struct_0_x9704_x2783_1139246857}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1485558742}[收到数据包]{style="font-family:宋体"}

[[Sending to interface *interface-name* ]{lang="EN-US"}]{#struct_0_x9704_x2783_x1808146052}

[[发送数据包到接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x9704_x2783_x2040818815}

[[Label(s)]{lang="EN-US"}]{#struct_0_x9704_x2783_50425489}

[[标签（包括私网内层标签和公网外层标签）]{style="font-family:宋体"}]{#struct_0_x9704_x2783_x79505294}

[[EXP]{lang="EN-US"}]{#struct_0_x9704_x2783_1138788106}

[[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_50575762}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_x9704_x2783_1802656051}

[[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_1378356441}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[*[Operation]{lang="EN-US"}*[ Label]{lang="EN-US"}]{#struct_0_x9704_x2783_x608571192}

[[标签操作（如]{style="font-family:宋体"}[POP]{lang="EN-US"}]{#struct_0_x9704_x2783_1211393508}[、]{style="font-family:宋体"}[PUSH]{lang="EN-US"}[、]{style="font-family:宋体"}[SWAP]{lang="EN-US"}[等）]{style="font-family:宋体"}

[[PktLen]{lang="EN-US"}]{#struct_0_x9704_x2783_1138722570}

[[数据包的长度]{style="font-family:宋体"}]{#struct_0_x9704_x2783_113966583}

[[MPLS send result *result*]{lang="EN-US"}]{#struct_0_x9704_x2783_x1080767025}

[[MPLS]{lang="EN-US"}]{#struct_0_x9704_x2783_x1761909090}[报文发送结果，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示发送成功，其它表示失败]{style="font-family:宋体"}

[[AF]{lang="EN-US"}]{#struct_0_x9704_x2783_x288928579}

[[地址族类型]{style="font-family:宋体"}]{#struct_0_x9704_x2783_193962098}

[[ ]{lang="EN-US" style="font-size:
9.0pt"}]{.TableTextChar}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9704_x2783_1903052648}

[[\# ]{lang="EN-US"}]{#struct_0_x9704_x2783_6503096}[在设备上打开]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[的报文调试信息开关，当网络中存在]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流量时，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<PE1\> debugging mpls packet]{lang="EN-US"}]{#struct_0_x9704_x2783_1138919178}

[\*Oct 19 09:13:03:979 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;]{lang="EN-US"}

[MPLS Input: Receiving from interface GE1/0/1, PktLen=70, Label(s)=1025, EXP=4, TTL=3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_1626948660}*[接收到]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文：接收报文的接口为]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[70]{lang="EN-US"}[字节，入标签为]{style="font-family:宋体"}[1025]{lang="EN-US"}[，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}*

[[\*Oct 19 09:13:03:980 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;]{lang="EN-US"}]{#struct_0_x9704_x2783_1059248022}

[POP Label=1025, EXP=4, TTL=3]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1568224727}*[弹出标签，标签为]{style="font-family:宋体"}[1025]{lang="EN-US"}[，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}*

[[\*Oct 19 09:13:03:980 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;]{lang="EN-US"}]{#struct_0_x9704_x2783_x2068418361}

[PUSH Label=2025, EXP=4, TTL=2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_x97464877}*[压入标签，标签为]{style="font-family:宋体"}[2025]{lang="EN-US"}[，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Oct 19 09:13:03:980 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;]{lang="EN-US"}]{#struct_0_x9704_x2783_x1202954774}

[MPLS Output: Sending to interface GE1/0/2, PktLen=70, Label(s)=2025, EXP=4, TTL=2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x9704_x2783_352184579}*[发送]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文：发送报文的接口为]{style="font-family:宋体"}[GE1/0/2]{lang="EN-US"}[，报文的出标签为]{style="font-family:宋体"}[2025]{lang="EN-US"}[，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Oct 19 09:13:03:981 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;]{lang="EN-US"}]{#struct_0_x9704_x2783_1138853642}

[MPLS send result 0.]{lang="EN-US"}

[*[// MPLS]{lang="EN-US"}*]{#struct_0_x9704_x2783_x1060140878}*[报文发送成功]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
