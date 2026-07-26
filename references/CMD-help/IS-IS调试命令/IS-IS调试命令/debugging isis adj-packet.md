::: {#-2041907362 .myid}
[]{#_Toc216606632}[]{#_Toc404788099}[]{#struct_0_16293_x2703_x1743248447}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis adj-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_425975100}

[**[debugging]{lang="EN-US"}**[ **isis** **adj-packet** \[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x501965864}

[**[undo]{lang="EN-US"}**[ **debugging** **adj-packet** \[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x1013827381}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1954748836}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_x164968053}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1588627891}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x249572087}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x236115967}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1184733955}

[**[receive]{lang="EN-US"}**]{#struct_0_16293_x2703_413139579}[：打开]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文接收调试功能。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_16293_x2703_1842264313}[：打开]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送调试功能。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16293_x2703_37712299}[：打开]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文详细信息调试功能。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1910442899}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1654973582}

[**[debugging isis adj-packet]{lang="EN-US"}**]{#struct_0_16293_x2703_1588562355}[命令用来打开]{style="font-family:
宋体"}[IS-IS Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:
宋体"}**[undo debugging isis adj-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x573731437}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x1498640893}[进程的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[]{#struct_0_16293_x2703_558895418}[[表1-1 ]{lang="EN-US"}[debugging isis adj-packet]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x521761788}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1007405110}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_12099255}

[[ISIS-*process-id*-ADJ: System is under disable state, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x1110484179}

[[收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_1588758963}[报文时，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程处于]{style="font-family:宋体"}[disable]{lang="EN-US"}[状态，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_2134102578}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS*-process-id*-ADJ: Circuit (*circuitName*)\'s state is not up, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_772600168}

[[收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x1084649732}[报文时，接口处于非]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1989695558}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_541613181}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*process-id*-ADJ: Circuit (*circuitName*) is under disable state, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1588693427}

[[收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x600374638}[报文时，接口处于]{style="font-family:宋体"}[silence]{lang="EN-US"}[状态，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_215335817}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x960512830}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*process-id*-ADJ: Receive a packet from self, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x1471280550}

[[收到了自己发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_591800844}[报文，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1588890035}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: Receive a invalid packet, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x1401915796}

[[收到了被截断或报文长度与实际长度不一致的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x1879583896}[报文，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x411461943}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: Receive a invalid packet, has the same SystemId, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x1040491002}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_1588824499}[报文携带的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[和本系统的相同，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_184764638}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: Receive a *helloType* packet from (*systemId*) on circuit (*circuitName*).]{lang="EN-US"}]{#struct_0_16293_x2703_x947222534}

[[接收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_795813747}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1589021107}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[helloType]{lang="EN-US"}*]{#struct_0_16293_x2703_x201004020}[：取值为]{lang="EN-US" style="font-family:宋体"}[LAN L1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LAN L2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[P2P]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1873558804}[：报文携带的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_2114376112}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*process-id*-ADJ: IIH PDU type (*type*) with circuit (*circuitName*) mismatch.]{lang="EN-US"}]{#struct_0_16293_x2703_1588955571}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_955694422}[报文]{style="font-family:宋体"}[Level]{lang="EN-US"}[类型与接口配置不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1435799145}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_16293_x2703_622714395}[：取值为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1589152179}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*process-id*-ADJ: IIH protocol support with circuit (*circuitName*) mismatch.]{lang="EN-US"}]{#struct_0_16293_x2703_199200289}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_1177186158}[报文携带的协议支持信息与本系统不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1872891761}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1589086643}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*process-id*-ADJ: IIH IP address with circuit (*circuitName*) mismatch.]{lang="EN-US"}]{#struct_0_16293_x2703_160784555}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x1724618259}[报文携带的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与本系统不在同一网段或与本系统]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相同]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1260463964}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1588627888}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*process-id*-ADJ: IIH area address with the local system mismatch.]{lang="EN-US"}]{#struct_0_16293_x2703_x250161912}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x1872921236}[报文携带的区域地址与本系统不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1588562352}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: IIH has the same SNPA with a NBR, but different SystemId. The NBR will be down.]{lang="EN-US"}]{#struct_0_16293_x2703_x573403757}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_1240299294}[报文，携带的]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[与本系统已维护的邻居相同，但]{style="font-family:宋体"}[System ID]{lang="EN-US"}[不同，本系统维护的邻居]{style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1430871426}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: IIH has the same SystemId with a NBR, but different SNPA. The IIH will be discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1588758960}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_2134037042}[报文，携带的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[与本系统已维护的邻居相同，但]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[不同，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1203088077}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS- *process-id* -ADJ: IIH has the same LinkLocal address with circuit(*circuitName*).]{lang="EN-US"}]{#struct_0_16293_x2703_1588693424}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x600440174}[报文携带的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址与接收接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址相同。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1373892968}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1588890032}[：]{lang="EN-US" style="font-family:
  宋体"}[接口名称]{lang="EN-US" style="font-family:宋体"}

[[ISIS- *process-id* -ADJ: IIH circuit(*circuitName*) contains No usable Ip addresses at all. IIH Ignored.]{lang="EN-US"}]{#struct_0_16293_x2703_x1401457044}

[[设备之间即不能建立]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16293_x2703_x226297889}[邻居也不能建立]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x149189613}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1588824496}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS- *process-id* -ADJ: Rxed *type* can not pass authentication on circuit(*circuitName*). IIH Ignored]{lang="EN-US"}]{#struct_0_16293_x2703_185616606}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x2005571246}[报文没有通过认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1589021104}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_16293_x2703_x201200628}[：]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[AN]{lang="EN-US"}[ L1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[AN]{lang="EN-US"}[ L2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[P2P]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1588955568}[：]{lang="EN-US" style="font-family:
  宋体"}[接口名称]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: *type* NBR (*systemId*) two way pass.]{lang="EN-US"}]{#struct_0_16293_x2703_955235671}

[[邻居]{style="font-family:宋体"}[2-way]{lang="EN-US"}]{#struct_0_16293_x2703_x1562343528}[检查成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1589152176}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_16293_x2703_200183329}[：取值为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x2113297969}[：邻居的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[ISIS-*process-id*-ADJ: *type* NBR (*systemId*) two way fail.]{lang="EN-US"}]{#struct_0_16293_x2703_1589086640}

[[邻居]{style="font-family:宋体"}[2-way]{lang="EN-US"}]{#struct_0_16293_x2703_160850091}[检查失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2350267}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_16293_x2703_1588627889}[：取值为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x250096376}[：邻居的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[ISIS-*process-id*-ADJ:DIS type *type*, on *circuitName*, old DIS: *sourceId1*, new DIS: *sourceId2*.]{lang="EN-US"}]{#struct_0_16293_x2703_x1500170752}

[[DIS]{lang="EN-US"}]{#struct_0_16293_x2703_1588562353}[选举结果]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x573338221}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_16293_x2703_1588758961}[：]{lang="EN-US" style="font-family:宋体"}[取值为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_2133971506}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId1]{lang="EN-US"}*]{#struct_0_16293_x2703_1299223222}[：原]{lang="EN-US" style="font-family:宋体"}[DIS-ID]{lang="EN-US"}[，为空，则原]{lang="EN-US" style="font-family:宋体"}[DIS]{lang="EN-US"}[不存在]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId2]{lang="EN-US"}*]{#struct_0_16293_x2703_1588693425}[：新]{lang="EN-US" style="font-family:宋体"}[DIS-ID]{lang="EN-US"}[，为空，则新]{lang="EN-US" style="font-family:宋体"}[DIS]{lang="EN-US"}[不存在]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*process-id*-ADJ: Send a *helloType* packet on circuit (*circuitName*)]{lang="EN-US"}]{#struct_0_16293_x2703_x600505710}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_977483848}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1588890033}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[helloType]{lang="EN-US"}*]{#struct_0_16293_x2703_x1401522580}[：]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[LAN L1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LAN L2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[P2P]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1588824497}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS- *process-id* -ADJ: Small-Hello is enabled on circuit(*circuitName*)]{lang="EN-US"}]{#struct_0_16293_x2703_185682142}

[[接口使能]{style="font-family:宋体"}[Small-Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x472731792}[功能。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1589021105}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x201135092}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS- *process-id* -ADJ: The circuit(*circuitName*) is silent.IIH not sent.]{lang="EN-US"}]{#struct_0_16293_x2703_1588955569}

[[接口状态为]{style="font-family:宋体"}[silent]{lang="EN-US"}]{#struct_0_16293_x2703_955170135}[，接口不发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_89247287}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1589152177}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS- *process-id* -ADJ: The Extended circuit ID of IIH mismatch. IIH ignored.]{lang="EN-US"}]{#struct_0_16293_x2703_866949804}

[[扩展接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16293_x2703_866622124}[不匹配，忽略此]{style="font-family:宋体"}[IIH]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_2095112757}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS- *process-id* -ADJ: Circuit(*circuitName*) is MPLS TE Tunnel interface, IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x2019204464}

[[接收接口是]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}]{#struct_0_16293_x2703_866556588}[隧道接口，忽略此]{style="font-family:宋体"}[IIH]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1261063154}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x83083520}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_200117793}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_248280278}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[3333.3333. 3333]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.3.3.166/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[FFFF.FFFF.FFFF]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.3.3.89/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在同一个区域]{style="font-family:宋体"}[49]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis adj-packet]{lang="EN-US"}]{#struct_0_16293_x2703_x1513520965}

[\*Apr  4 18:47:08:383 2011 RouterA ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US"}

[ISIS-1-ADJ: Send a Lan L2 Hello packet on circuit(GigabitEthernet1/0/2)]{lang="EN-US"}

[\*Apr  4 18:47:08:384 2011 RouterA ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US"}

[ISIS-1-ADJ: Send a Lan L1 Hello packet on circuit(GigabitEthernet1/0/2)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x624362669}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上发送]{style="font-family:宋体"}[L1]{lang="EN-US"}[和]{style="font-family:宋体"}[L2]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_1589086641}

[ISIS-1-ADJ: Receive a Lan L2 Hello packet from(ffff.ffff.ffff) on circuit(GigabitEthernet1/0/2)]{lang="EN-US"}

[\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US"}

[ISIS-1-ADJ: Level-2 NBR(ffff.ffff.ffff) two way pass.]{lang="EN-US"}

[\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ADJ: Receive a Lan L1 Hello packet from(ffff.ffff.ffff) on circuit(GigabitEthernet1/0/2)]{lang="EN-US"}

[\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ADJ: Level-1 NBR(ffff.ffff.ffff) two way pass.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_160915627}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上接收]{style="font-family:宋体"}[L1]{lang="EN-US"}[和]{style="font-family:宋体"}[L2]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，对端]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为：]{style="font-family:宋体"}[FFFF.FFFF.FFFF]{lang="EN-US"}[，]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查通过，建立了邻居关系]{style="font-family:宋体"}*

[[\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1530393339}

[ISIS-1-ADJ: Send a Lan L1 Hello packet on circuit(GigabitEthernet1/0/2)]{lang="EN-US"}

[\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ADJ: Send a Lan L2 Hello packet on circuit(GigabitEthernet1/0/2)]{lang="EN-US"}

[\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ADJ: DIS type Level-1, on GigabitEthernet1/0/2, old DIS:, new DIS:3333.3333.3333.01.]{lang="EN-US"}

[\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ADJ: DIS type Level-2, on GigabitEthernet1/0/2, old DIS:, new DIS:3333.3333.3333.01.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1354284849}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上进行了]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举，在]{style="font-family:宋体"}[L1]{lang="EN-US"}[、]{style="font-family:宋体"}[L2]{lang="EN-US"}[上分别选出了]{style="font-family:宋体"}[DIS]{lang="EN-US"}*

::: {#-842803313 .myid}
[]{#_Toc404788100}[]{#struct_0_16293_x2703_1588627886}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x249244408}

[**[debuging isis all]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_2129149504}

[**[undo debuging isis all]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_1120747633}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x627196185}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_1107433366}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x324686135}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_514136161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1803200401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1588562350}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x573534829}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1262736589}

[**[debuging isis all]{lang="EN-US"}**]{#struct_0_16293_x2703_x498135291}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}**[undo debugging isis all]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x658209940}[所有的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x1632558561}[进程的调试信息开关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x2003109392}

[[\# ]{lang="EN-US"}]{#struct_0_16293_x2703_1783596907}[打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis all 1]{lang="EN-US"}]{#struct_0_16293_x2703_1588758958}
:::

::: {#-811830289 .myid}
[]{#_Toc404788101}[]{#struct_0_16293_x2703_2133512755}[]{#_Toc263865604}[]{#_Toc216606633}[]{#_Toc205281029}[]{#_Toc161626627}[]{#_Toc161569530}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis bfd-event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_518517238}

[**[debugging isis bfd-event ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x10191583}

[**[undo debugging isis bfd-event]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x746374963}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1816739482}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_451228921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1479728993}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_534871779}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1588693422}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x600046958}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1006557616}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体;color:#0000CC"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_991330585}

[**[debugging isis bfd-event]{lang="EN-US"}**]{#struct_0_16293_x2703_166494494}[命令用来打开]{style="font-family:
宋体"}[IS-IS BFD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:
宋体"}**[undo debugging isis bfd-event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS BFD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS BFD]{lang="EN-US"}]{#struct_0_16293_x2703_1855333652}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x733886624}[进程的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging isis bfd-event]{lang="EN-US"}]{#struct_0_16293_x2703_126548450}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x532271964}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_515581364}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_1588890030}

[[ISIS- process-id -BFD: Success to send Sessiontype session Msg. DstIPAddr: XX.XX.XX.XX SrcIPAddr:]{lang="EN-US"}]{#struct_0_16293_x2703_x1401588116}

[[ YY.YY.YY.YY, NeighborType: leveltype]{lang="EN-US"}]{#struct_0_16293_x2703_1560375575}

[[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_452631286}[协议通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模块的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x891549715}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Sessiontype]{lang="EN-US"}*]{#struct_0_16293_x2703_x1220801388}[：消息类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Sessiontype]{lang="EN-US"}*]{#struct_0_16293_x2703_1588824494}[：消息类型]{lang="EN-US" style="font-family:
  宋体"}[。值可以为：]{style="font-family:宋体"}[create]{lang="EN-US"}[，]{style="font-family:宋体"}[创建会话]{lang="EN-US" style="font-family:宋体"}[；]{style="font-family:宋体"}[delete]{lang="EN-US"}[，]{style="font-family:宋体"}[删除会话]{lang="EN-US" style="font-family:宋体"}[；]{style="font-family:宋体"}[disable]{lang="EN-US"}[，]{style="font-family:宋体"}[去使能会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstIPAddr]{lang="EN-US"}]{#struct_0_16293_x2703_185485534}[：会话目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcIPAddr]{lang="EN-US"}]{#struct_0_16293_x2703_x1876632314}[：会话源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NeighborType]{lang="EN-US"}]{#struct_0_16293_x2703_1084723438}[：邻居类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[leveltype]{lang="EN-US"}*]{#struct_0_16293_x2703_575275641}[：]{lang="EN-US" style="font-family:宋体"}[级别]{style="font-family:宋体"}[类型]{lang="EN-US" style="font-family:宋体"}[。值可以为：]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[，广播网]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[邻居；]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，广播网]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[邻居；]{style="font-family:宋体"}[P2P]{lang="EN-US"}[，]{style="font-family:宋体"}[P2P]{lang="EN-US"}[邻居]{style="font-family:宋体"}

[ ]{lang="EN-US" style="color:#0000CC"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x148416240}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_499406256}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，分别在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS BFD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging isis bfd-event]{lang="EN-US"}]{#struct_0_16293_x2703_1589021102}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] isis bfd enable]{lang="EN-US"}

[\*Jan  2 02:16:46:688 2000 Sysname ISIS/7/ISISDBG:]{lang="EN-US"}

[ISIS-1-BFD: Success to send create session Msg. DstIPAddr: 12.12.12.1, SrcIPAddr: 12.12.12.2, NeighborType: Level-1]{lang="EN-US"}

[*[// IS-IS]{lang="EN-US"}*]{#struct_0_16293_x2703_x201331700}*[协议通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模块创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，会话目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[12.12.12.1]{lang="EN-US"}[，会话源地址为]{style="font-family:宋体"}[12.12.12.2]{lang="EN-US"}[，邻居类型为广播网]{style="font-family:宋体"}[Level-1]{lang="EN-US"}*

[[\[Sysname-Vlan-interface100\] undo isis bfd enable]{lang="EN-US"}]{#struct_0_16293_x2703_105997724}

[\*Jan  2 02:17:14:968 2000 Sysname ISIS/7/ISISDBG:]{lang="EN-US"}

[ISIS-1-BFD: Success to send disable session Msg. DstIPAddr: 12.12.12.1, SrcIPAddr: 12.12.12.2, NeighborType: Level-1]{lang="EN-US"}

[*[// IS-IS]{lang="EN-US"}*]{#struct_0_16293_x2703_825357233}*[协议通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模块去使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，会话目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[12.12.12.1]{lang="EN-US"}[，会话源地址为]{style="font-family:宋体"}[12.12.12.2]{lang="EN-US"}[，邻居类型为广播网]{style="font-family:宋体"}[Level-1]{lang="EN-US"}*

::: {#1632425944 .myid}
[]{#_Toc404788102}[]{#struct_0_16293_x2703_1508791584}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_346789931}

[**[debuging isis error]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_1588955566}

[**[undo debuging isis error]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_956153175}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1096751642}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_x172096440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1625375431}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1250560626}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1100602260}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x36067764}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1589152174}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_200052257}

[**[debuging isis error]{lang="EN-US"}**]{#struct_0_16293_x2703_x141742505}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}**[undo debugging isis error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x515889093}[错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x813497498}[进程的错误调试信息开关。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging isis error]{lang="EN-US"}]{#struct_0_16293_x2703_1527465791}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x529244660}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_1489950099}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_1589086638}

[[ISIS-*procId*-ERR: LAN ADJ number has arrived max.]{lang="EN-US"}]{#struct_0_16293_x2703_160325802}

[[接口邻居数目达到最大值]{style="font-family:宋体"}]{#struct_0_16293_x2703_442026241}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x713947050}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid protocol descriminator. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x402438249}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_169645630}[报文协议鉴别字段错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1588627887}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid version. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x249178872}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_x1483033186}[报文协议版本错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x514484730}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid protocol ID. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1526834443}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_1588562351}[报文协议]{style="font-family:宋体"}[ID]{lang="EN-US"}[错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x573469293}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid system ID length. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1308748052}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_868468838}[报文]{style="font-family:宋体"}[system ID]{lang="EN-US"}[错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x599200776}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid max area address number. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1588758959}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_2133447219}[报文区域地址最大数错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1331080014}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid packet Type. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_890639642}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_x1805637880}[报文类型错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1588693423}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH contains invalid head length. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x600112494}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_1391527839}[报文头长度错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_645057700}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR:  Receive a LAN IIH contains invalid circuit Type. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1588890031}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_x1401653652}[报文接口类型错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_405856527}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR:  Receive a LAN IIH contains invalid priority. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_437307695}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_1588824495}[报文]{style="font-family:宋体"}[dis]{lang="EN-US"}[优先级错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_185551070}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH neighbor TLV decode error. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_822551662}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_332293104}[报文邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解码错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1589021103}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR:  Receive a LAN IIH area address TLV decode error. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_x201266164}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_x1084630544}[报文区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解码错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x717362449}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH IP address TLV decode error. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1588955567}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_956087639}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解码错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730255882}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Receive a LAN IIH protocol support TLV decode error. IIH discarded.]{lang="EN-US"}]{#struct_0_16293_x2703_1589152175}

[[接收到的]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_199986721}[报文协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}[解码错误，不处理接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_303942719}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR:  System\'s state is disable.]{lang="EN-US"}]{#struct_0_16293_x2703_718778179}

[[进程处于]{style="font-family:宋体"}[disable]{lang="EN-US"}]{#struct_0_16293_x2703_1589086639}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_160391338}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR:  Socket ID leave muti-cast group failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x1077760465}

[[将接口从组播组中删除失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1140255465}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1551516360}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: *adjLevel* Hello timer start failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x673486647}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_87080484}[定时器创建失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140321001}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adjLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1225979153}[：]{lang="EN-US" style="font-family:宋体"}[hello]{lang="EN-US"}[定时器的类型]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Socket ID join mutiple broadcast group failed.]{lang="EN-US"}]{#struct_0_16293_x2703_314922837}

[[将接口加入到组播组中失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1140124393}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x469765082}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: UPDT Module NBR TLV Modify Failed.]{lang="EN-US"}]{#struct_0_16293_x2703_1271490678}

[[邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_16293_x2703_x1140189929}[更新失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1926908452}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Notify UPDT Module LSP Change Failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x1798488858}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1139993321}[重新生成失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x439709292}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: DEC Module ISPF Link Update Failed.]{lang="EN-US"}]{#struct_0_16293_x2703_385684220}

[[邻接链路更新失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1140058857}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_156052474}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Hold timer start failed.]{lang="EN-US"}]{#struct_0_16293_x2703_1630741904}

[[邻居维持定时器创建失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1139862249}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1904572598}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Get SNPA address failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x729193924}

[[获取]{style="font-family:宋体"}[snpa]{lang="EN-US"}]{#struct_0_16293_x2703_x1139927785}[地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_577911239}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Get circuit(*circuitName*)\'s priority failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x1139731177}

[[获取接口]{style="font-family:宋体"}[DIS]{lang="EN-US"}]{#struct_0_16293_x2703_1879321342}[优先级失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x2096971637}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139796713}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Get system\'s area address failed.]{lang="EN-US"}]{#struct_0_16293_x2703_66419398}

[[获取接口系统区域地址失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_814435502}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140255464}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: The circuit\'s MTU is too less.]{lang="EN-US"}]{#struct_0_16293_x2703_x14567581}

[[接口]{style="font-family:宋体"}[mtu]{lang="EN-US"}]{#struct_0_16293_x2703_x1140321000}[大小放不下当前]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_340104788}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Get circuit(*circuitName*)\'s IP address failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x1974044351}

[[获取接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_x1140124392}[地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1096318859}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140189928}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: The circuit\'s MTU is too less to encode LAN IIH.]{lang="EN-US"}]{#struct_0_16293_x2703_x360824511}

[[接口]{style="font-family:宋体"}[mtu]{lang="EN-US"}]{#struct_0_16293_x2703_x2144603085}[大小放不下]{style="font-family:宋体"}[IIH]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139993320}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Get circuit(*circuitName*)\'s MTU failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x2005793233}

[[获取接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_16293_x2703_x1140058856}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1410031467}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139862248}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Hello packet send failed on circuit(*circuitName*).]{lang="EN-US"}]{#struct_0_16293_x2703_x338488657}

[[接口]{style="font-family:宋体"}[IIH]{lang="EN-US"}]{#struct_0_16293_x2703_x1139927784}[报文发送失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_2143995180}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139731176}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Hello timer create failed on circuit(*circuitName*).]{lang="EN-US"}]{#struct_0_16293_x2703_313237401}

[[接口上的]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_16293_x2703_x1801045555}[定时器创建失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139796712}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1499664543}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error modifying the attributes of the route entry in RM.]{lang="EN-US"}]{#struct_0_16293_x2703_x1140255467}

[[更新路由属性失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1580651522}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140321003}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x63179739}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140124395}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Error adding a new route entry in RM.]{lang="EN-US"}]{#struct_0_16293_x2703_336803972}

[[添加新路由失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1140189931}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1570743628}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139993323}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_723090122}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Error deleting a route entry in RM.]{lang="EN-US"}]{#struct_0_16293_x2703_x1140058859}

[[删除路由失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_606391168}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139862251}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1548276702}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139927787}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*) Error getting *level* nexthop information for *systemId* from ISPF module.]{lang="EN-US"}]{#struct_0_16293_x2703_1740710653}

[[获取路由发布源的下一条失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1139731179}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1072752288}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139796715}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140255466}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1148231833}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*procId*-ERR: Error building nexthop list for route *ipAddr*/*mask*.]{lang="EN-US"}]{#struct_0_16293_x2703_x1140321002}

[[创建下一条链表失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1502904202}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140124394}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddr]{lang="EN-US"}*]{#struct_0_16293_x2703_1902887913}[：接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140189930}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error processing ipv4 route entry.]{lang="EN-US"}]{#struct_0_16293_x2703_x4659687}

[[路由计算出错]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1139993322}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140058858}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x959692773}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error adding the route source entry from the source list.]{lang="EN-US"}]{#struct_0_16293_x2703_x1139862250}

[[添加路由发布源失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_17807239}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139927786}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x988172702}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error finding the routeEntry structure for address *ipAddr*/*mask*.]{lang="EN-US"}]{#struct_0_16293_x2703_x1139731178}

[[查找路由信息失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1139796714}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x693095489}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140255469}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddr]{lang="EN-US"}*]{#struct_0_16293_x2703_x1130312828}[：接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140321005}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Error deleting the route source entry from the source list.]{lang="EN-US"}]{#struct_0_16293_x2703_x1140124397}

[[删除路由发布源失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1499603386}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140189933}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1561424254}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error modifying the route source entry in the source list.]{lang="EN-US"}]{#struct_0_16293_x2703_x1139993325}

[[更新路由发布源失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1140058861}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_962424920}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139862253}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Add route to URT fails.]{lang="EN-US"}]{#struct_0_16293_x2703_x385477288}

[[路由已满，添加路由失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1139927789}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139731181}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_717504968}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*) Modify route in URT failure.]{lang="EN-US"}]{#struct_0_16293_x2703_x1139796717}

[[更新路由失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_2035787866}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140255468}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140321004}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Del route form URT fails.]{lang="EN-US"}]{#struct_0_16293_x2703_x1985494040}

[[删除路由失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1140124396}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1140189932}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1167459101}[：系统类型]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[可为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-ERR: Resetting the system]{lang="EN-US"}]{#struct_0_16293_x2703_x1139993324}

[[进程正在]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_16293_x2703_x1140058860}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x603659021}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: MTU Size Exceeds Max PDU Size *mtuSize*, Setting it to Max PDU Size.]{lang="EN-US"}]{#struct_0_16293_x2703_x1139862252}

[[接口]{style="font-family:宋体"}[mtu]{lang="EN-US"}]{#struct_0_16293_x2703_1180606653}[超过最大值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139927788}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtuSize]{lang="EN-US"}*]{#struct_0_16293_x2703_x1139731180}[：接口]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Processing the circuit MTU change event fails]{lang="EN-US"}]{#struct_0_16293_x2703_x848578973}

[[接口]{style="font-family:宋体"}[mtu]{lang="EN-US"}]{#struct_0_16293_x2703_x1139796716}[变化处理失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238754522}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtuSize]{lang="EN-US"}*]{#struct_0_16293_x2703_972440144}[：接口]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Processing the physical circuit board insert error]{lang="EN-US"}]{#struct_0_16293_x2703_1238820058}

[[接口板插入处理出错]{style="font-family:宋体"}]{#struct_0_16293_x2703_1238623450}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x591558289}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Processing the physical circuit delete error on circuit :*circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1238688986}

[[处理物理接口删除出错]{style="font-family:宋体"}]{#struct_0_16293_x2703_1239016666}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_971844587}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1239082202}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Processing the physical circuit UP \--\> Down error on circuit : *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1238885594}

[[物理接口]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_16293_x2703_1238951130}[到]{style="font-family:宋体"}[down]{lang="EN-US"}[的处理出错]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1333960536}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1239278810}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Processing the physical circuit config error on circuit :  *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1239344346}

[[物理接口配置的处理出错]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1771814194}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238754523}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1238820059}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Processing board remove failed on circuit : *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1238623451}

[[物理接口板拔出的处理出错]{style="font-family:宋体"}]{#struct_0_16293_x2703_x591623825}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238688987}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1239016667}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Invalid phase *enDisablePhase*, ignore event.]{lang="EN-US"}]{#struct_0_16293_x2703_1239082203}

[[进程不在]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_16293_x2703_x248185263}[的阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238885595}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[enDisablePhase]{lang="EN-US"}*]{#struct_0_16293_x2703_1238951131}[：进程所处的状态阶段]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: The event type and disable phase mismatch.]{lang="EN-US"}]{#struct_0_16293_x2703_1334026072}

[[进程的]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_16293_x2703_1239278811}[状态和阶段不一致]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239344347}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Failed to add neighbor into *lspLevel* LSPs]{lang="EN-US"}]{#struct_0_16293_x2703_1238754520}

[[向]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_972571216}[中添加邻居信息失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238820056}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1238623448}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型。可为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[ISIS-*procId*-ERR: Failed to add address *ipAddr*/*mask* into *lspleve* LSPs]{lang="EN-US"}]{#struct_0_16293_x2703_1238688984}

[[向]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_1647098297}[中添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddr]{lang="EN-US"}*]{#struct_0_16293_x2703_1239016664}[：接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_1239082200}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1238885592}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型。可为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[ISIS-*procId*-ERR: Failed to start csnp timer on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1762800365}

[[接口]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_16293_x2703_1238951128}[定时器创建失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239278808}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1239344344}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Failed to start psnp timer on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1238754521}

[[接口]{style="font-family:宋体"}[PSNP]{lang="EN-US"}]{#struct_0_16293_x2703_972636752}[定时器创建失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238820057}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1238623449}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Failed to start flood timer on the circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1238688985}

[[接口]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_1239016665}[泛洪定时器创建失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_972041195}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1239082201}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Failed to stop lsp flood timer on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1238885593}

[[关闭接口]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_1238951129}[泛洪定时器失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239278809}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1239344345}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Failed to stop *lspLevel* timer on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1772010802}

[[关闭接口]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_1238754518}[生成定时器失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238820054}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1238623446}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型。可为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1238688982}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-ERR: Parsed neighbor\'s metric(*systemId*) more than max metric value]{lang="EN-US"}]{#struct_0_16293_x2703_1239016662}

[[接口邻居]{style="font-family:宋体"}[metric]{lang="EN-US"}]{#struct_0_16293_x2703_971582443}[值大于允许的最大值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239082198}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1238885590}[：系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*procId*-ERR: Skip ip address prefix for mismatching with mask]{lang="EN-US"}]{#struct_0_16293_x2703_1238951126}

[[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_1239278806}[地址前缀和掩码不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239344342}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Skip the prefix for invalid ip prefix]{lang="EN-US"}]{#struct_0_16293_x2703_1238754519}

[[IP]{lang="EN-US"}]{#struct_0_16293_x2703_1238820055}[地址前缀不正确]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1739396118}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1238623447}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型。可为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[ISIS-*procId*-ERR: Internal ip reach Tlv with external bit set encountered]{lang="EN-US"}]{#struct_0_16293_x2703_1238688983}

[[内部可达]{style="font-family:宋体"}[IP TLV]{lang="EN-US"}]{#struct_0_16293_x2703_1239016663}[包含]{style="font-family:宋体"}[metric]{lang="EN-US"}[类型为外部的位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239082199}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Area addr tlv in non-zero fragment, skip this area addr tlv ]{lang="EN-US"}]{#struct_0_16293_x2703_1238885591}

[[非零分片中存在区域地址]{style="font-family:宋体"}]{#struct_0_16293_x2703_1238951127}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1239278807}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Area addr tlv in pseudo node lsp, skip this area addr tlv]{lang="EN-US"}]{#struct_0_16293_x2703_1239344343}

[[伪节点]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1771617586}[中存在区域地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490128833}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Lsp info update failed]{lang="EN-US"}]{#struct_0_16293_x2703_x1490063297}

[[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_x1490259905}[中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息更新失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490194369}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-ERR: Lsp insert failed]{lang="EN-US"}]{#struct_0_16293_x2703_x1489866689}

[[向]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1489801153}[中添加邻居信息失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489997761}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489932225}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型。可为]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[ISIS-*processId*-ERR: Lsp\'s seq number is 0]{lang="EN-US"}]{#struct_0_16293_x2703_x1489604545}

[[接收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489539009}[报文的序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490128832}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Illegal is-type in level-1 lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1490063296}

[[Level-1 LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1490259904}[报文的]{style="font-family:宋体"}[IS-TYPE]{lang="EN-US"}[字段非法，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490194368}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Check sum is zero]{lang="EN-US"}]{#struct_0_16293_x2703_x1489866688}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489801152}[报文的校验和为]{style="font-family:宋体"}[0]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489997760}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Check sum error]{lang="EN-US"}]{#struct_0_16293_x2703_x1489932224}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489604544}[报文的校验和错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489539008}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Support protocol mismatch]{lang="EN-US"}]{#struct_0_16293_x2703_x1490128835}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1490063299}[报文携带的协议支持和本地的不匹配，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490259907}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Lsp with too long area addr]{lang="EN-US"}]{#struct_0_16293_x2703_x1490194371}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_683018986}[报文中携带的区域地址长度超过最大区域地址长度，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489801155}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Lsp with wrong area addr length]{lang="EN-US"}]{#struct_0_16293_x2703_x1489997763}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489932227}[报文中携带的区域地址长度错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489604547}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Lsp with invalid area addr]{lang="EN-US"}]{#struct_0_16293_x2703_x1489539011}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1490128834}[报文中携带的区域地址长度不合法，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490063298}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Wrongly formatted interface ip address tlv in lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1490259906}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1490194370}[报文中携带的接口地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}[格式错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489866690}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Wrongly formatted nbr tlv in lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1489801154}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489997762}[报文中携带的邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}[格式错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489932226}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: IP Reachablity tlv occur in pseudonode lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1489604546}

[[伪节点]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489539010}[报文中携带的]{style="font-family:宋体"}[IP]{lang="EN-US"}[可达]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490128837}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Badly formatted ip reachablity tlv in lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1490063301}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1490259909}[报文中携带的]{style="font-family:宋体"}[IP]{lang="EN-US"}[可达]{style="font-family:宋体"}[TLV]{lang="EN-US"}[格式错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490194373}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Bad tlv len in the received lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x1489866693}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489801157}[报文中携带的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489932229}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Pdu size(*pduSize*) which is greater than receive buf size(*reveiveBufSize*)]{lang="EN-US"}]{#struct_0_16293_x2703_x1489604549}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489539013}[报文长度大于接收缓冲区大小，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1490128836}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pduSize]{lang="EN-US"}]{#struct_0_16293_x2703_x1490063300}[：]{lang="EN-US" style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reveiveBufSize]{lang="EN-US"}]{#struct_0_16293_x2703_x1490259908}[：]{lang="EN-US" style="font-family:宋体"}[接收缓冲区大小]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Pdu size(*pduSize*) which is less than common pdu header size(*pduCommonHeaderSize*)]{lang="EN-US"}]{#struct_0_16293_x2703_x1490194372}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1489866692}[报文长度小于公共报文头大小，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489801156}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pduSize]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489997764}[：]{lang="EN-US" style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pduCommonHeaderSize]{lang="EN-US"}*]{#struct_0_16293_x2703_x1489932228}[：]{lang="EN-US" style="font-family:宋体"}[公共报文头大小]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Pdu size(*pduSize*) which is less than fixed pdu header size(*pduFixedHeaderSize*)]{lang="EN-US"}]{#struct_0_16293_x2703_x1489539012}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_75955108}[报文长度小于固定报文头大小，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76020644}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pduSize]{lang="EN-US"}]{#struct_0_16293_x2703_75824036}[：]{lang="EN-US" style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pduFixedHeaderSize]{lang="EN-US"}]{#struct_0_16293_x2703_75889572}[：]{lang="EN-US" style="font-family:
  宋体"}[固定报文头大小]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Pdu length mismatch: recvLen = *recvLen*, encodeLen = *encodeLen*]{lang="EN-US"}]{#struct_0_16293_x2703_76217252}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_76282788}[报文长度和报文中的长度字段不相等，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76086180}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[recvLen]{lang="EN-US"}*]{#struct_0_16293_x2703_76151716}[：]{lang="EN-US" style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[encodeLen]{lang="EN-US"}*]{#struct_0_16293_x2703_76479396}[：]{lang="EN-US" style="font-family:宋体"}[报文中的长度字段]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Lsp or snp pdu common header error]{lang="EN-US"}]{#struct_0_16293_x2703_75955109}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_76020645}[公共报文头错误，丢弃报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_75824037}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Try to send pdu on loopback circuit]{lang="EN-US"}]{#struct_0_16293_x2703_75889573}

[[企图在环回接口上发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_76217253}[，不发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76282789}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Send pdu error, SENDTO return is *SentDataLen*, usBufLen is *bufDataLen*]{lang="EN-US"}]{#struct_0_16293_x2703_76086181}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_76479397}[发送失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76544933}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SentDataLen]{lang="EN-US"}*]{#struct_0_16293_x2703_75955106}[：发送出去的数据长度]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bufDataLen]{lang="EN-US"}*]{#struct_0_16293_x2703_76020642}[：需要发送的数据长度]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Lsp size(*lspSize*) is larger than circuit mtu(*circuitMtu*)]{lang="EN-US"}]{#struct_0_16293_x2703_75824034}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_75889570}[报文大小大于发送接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76217250}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspSize]{lang="EN-US"}*]{#struct_0_16293_x2703_76086178}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitMtu]{lang="EN-US"}*]{#struct_0_16293_x2703_76151714}[：]{lang="EN-US" style="font-family:宋体"}[发送接口的]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}

[[ISIS-*processId*-ERR: Wrong lsp entry tlv length(*lspEntryTlvLen*) in snp]{lang="EN-US"}]{#struct_0_16293_x2703_76479394}

[[SNP]{lang="EN-US"}]{#struct_0_16293_x2703_76544930}[报文中的]{style="font-family:宋体"}[LSP ENTRY TLV]{lang="EN-US"}[长度错误]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_75955107}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspEntryTlvLen]{lang="EN-US"}*]{#struct_0_16293_x2703_76020643}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP ENTRY TLV]{lang="EN-US"}[长度]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Snp contain too much lsp entry]{lang="EN-US"}]{#struct_0_16293_x2703_75889571}

[[SNP]{lang="EN-US"}]{#struct_0_16293_x2703_76217251}[报文中的]{style="font-family:宋体"}[LSP ENTRY]{lang="EN-US"}[个数多过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76282787}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Invalid lsp id reported in snp]{lang="EN-US"}]{#struct_0_16293_x2703_76086179}

[[SNP]{lang="EN-US"}]{#struct_0_16293_x2703_76151715}[报文中的]{style="font-family:宋体"}[LSP ENTRY]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP-ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76544931}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to install lsp with seq number zero]{lang="EN-US"}]{#struct_0_16293_x2703_75955104}

[[安装序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16293_x2703_76020640}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_75824032}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to add level-*Level* area address *areaAdress*]{lang="EN-US"}]{#struct_0_16293_x2703_75889568}

[[添加区域地址失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_76282784}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76086176}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_76151712}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAdress]{lang="EN-US"}*]{#struct_0_16293_x2703_76479392}[：区域地址]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Failed to delete level-*Level* area address *areaAdress*]{lang="EN-US"}]{#struct_0_16293_x2703_75955105}

[[删除区域地址失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_76020641}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_75824033}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_75889569}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAdress]{lang="EN-US"}*]{#struct_0_16293_x2703_76282785}[：区域地址]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Failed to add level- *Level* protocol support *protocolSupport*]{lang="EN-US"}]{#struct_0_16293_x2703_76086177}

[[添加协议支持失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_76151713}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_76479393}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1642039049}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocolSupport]{lang="EN-US"}*]{#struct_0_16293_x2703_1642104585}[：协议支持]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-ERR: Failed to delete level- *Level* protocol support *protocolSupport*]{lang="EN-US"}]{#struct_0_16293_x2703_1641907977}

[[删除协议支持失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1642301193}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642366729}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1642170121}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocolSupport]{lang="EN-US"}*]{#struct_0_16293_x2703_1642235657}[：协议支持]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-ERR: Failed to add level-*Level* neighbour: System *SystemId* =\> Neighbour *nbrSourceId*]{lang="EN-US"}]{#struct_0_16293_x2703_1642628873}

[[添加邻居失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1642039050}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642104586}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1641907978}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642301194}[：]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642366730}[：邻居的]{lang="EN-US" style="font-family:
  宋体"}[SourceID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to delete level-*Level* neighbour: System *SystemId* =\> Neighbour *nbrSourceId*]{lang="EN-US"}]{#struct_0_16293_x2703_1642170122}

[[删除邻居失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1642563338}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642628874}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1642039047}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1641907975}[：]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1641973511}[：邻居的]{lang="EN-US" style="font-family:
  宋体"}[SourceID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to modify level-*Level* neighbour: System *SystemId* =\> Neighbour *nbrSourceId*]{lang="EN-US"}]{#struct_0_16293_x2703_1642301191}

[[修改邻居失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1642170119}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642235655}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1642563335}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642039048}[：]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642104584}[：邻居的]{lang="EN-US" style="font-family:
  宋体"}[SourceID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to add level-*Level* Interface IP address: *ipAddress*/*mask*]{lang="EN-US"}]{#struct_0_16293_x2703_1641907976}

[[添加接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_1642301192}[地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642366728}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1642170120}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_1642563336}[：接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_1642628872}[：地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Failed to delete level-*Level* Interface IP address: *ipAddress*/*mask*]{lang="EN-US"}]{#struct_0_16293_x2703_1642104581}

[[删除接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_1641907973}[地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1641973509}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1642366725}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_1642170117}[：接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_1642235653}[：地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Failed to add level-*Level* pseudo neighbour: Pseudo *pseudoNodeSourceId* =\> Neighbour *nbrSystemId*]{lang="EN-US"}]{#struct_0_16293_x2703_1642628869}

[[添加伪节点邻居失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1642039046}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1641907974}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1641973510}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudoNodeSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642301190}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrSystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1642170118}[：邻居]{lang="EN-US" style="font-family:
  宋体"}[System ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to delete level-*Level* pseudo neighbour: Pseudo *pseudoNodeSourceId* =\> Neighbour *nbrSystemId*]{lang="EN-US"}]{#struct_0_16293_x2703_1642235654}

[[删除伪节点邻居失败]{style="font-family:宋体"}]{#struct_0_16293_x2703_1642563334}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730613946}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x730548410}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudoNodeSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730679482}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrSystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730351802}[：邻居]{lang="EN-US" style="font-family:
  宋体"}[System ID]{lang="EN-US"}

[[ISIS-*processId*-ERR: Failed to add level-*Level* IP prefix: *ipPrefix*/*mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x730286266}

[[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_x730417338}[前缀失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730089658}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x730024122}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_x730548409}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x730745017}[：前缀掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Failed to delete level-*Level* IP prefix: *ipPrefix* / *mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x730351801}

[[删除]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_x730286265}[前缀失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730417337}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x730089657}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_x730024121}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x730548412}[：前缀掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Failed to modify level-*Level* IP prefix: *ipPrefix* / *mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x730745020}

[[修改]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_x730351804}[前缀失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730286268}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x730417340}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_x730089660}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x730613947}[：前缀掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-ERR: Level-*Level*, receive wrong extended nerghbor SubTlv, Type=*type*, Length=*len*]{lang="EN-US"}]{#struct_0_16293_x2703_866753199}

[[接收到错误的扩展邻居]{style="font-family:宋体"}[sub-tlv]{lang="EN-US"}]{#struct_0_16293_x2703_1689641379}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_866687663}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x664851969}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_16293_x2703_867408559}[：]{lang="EN-US" style="font-family:宋体"}[sub-tlv]{lang="EN-US"}[类型值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[len]{lang="EN-US"}*]{#struct_0_16293_x2703_867343023}[：]{lang="EN-US" style="font-family:宋体"}[sub-tlv]{lang="EN-US"}[长度]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x924887181}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_x379417271}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，路由器类型为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.166/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[FFFF.FFFF.FFFF]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在同一个区域]{style="font-family:宋体"}[49]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis error]{lang="EN-US"}]{#struct_0_16293_x2703_x1415100021}

[\*Apr  8 21:47:12:360 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ERR: Receive a LAN IIH contains invalid protocol discriminator. IIH discarded.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x172275899}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上收到协议鉴别号不是]{style="font-family:宋体"}[0x83]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#-1081914249 .myid}
[]{#_Toc404788103}[]{#struct_0_16293_x2703_x1973330011}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1942015994}

[**[debuging isis event]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_658236924}

[**[undo debuging isis event]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x730548411}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x578844854}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_386585963}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x356050526}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x544542297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1688872959}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1402703160}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x953372940}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x730745019}

[**[debuging isis event]{lang="EN-US"}**]{#struct_0_16293_x2703_x929391699}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}**[undo debugging isis event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x286362213}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1884379988}[进程的事件调试信息开关。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging isis event]{lang="EN-US"}]{#struct_0_16293_x2703_1921730384}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x493511704}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1707789449}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1634554614}

[[ISIS-*procId*-EVT: Rib smooth start. ]{lang="EN-US"}]{#struct_0_16293_x2703_x730679483}

[[数据平滑开始]{style="font-family:宋体"}]{#struct_0_16293_x2703_978653977}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x567122762}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Rt smooth end.]{lang="EN-US"}]{#struct_0_16293_x2703_1676216820}

[[数据平滑结束]{style="font-family:宋体"}]{#struct_0_16293_x2703_x2051280664}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x439451631}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: LSP MTU change from *oldLspBuf* to *newLspBuf*, notify UPDT MTU change.]{lang="EN-US"}]{#struct_0_16293_x2703_x730351803}

[[进程]{style="font-family:宋体"}[lsp]{lang="EN-US"}]{#struct_0_16293_x2703_x138187338}[缓冲区的大小改变]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x284326850}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[oldLspBuf]{lang="EN-US"}*]{#struct_0_16293_x2703_2039360964}[：]{lang="EN-US" style="font-family:宋体"}[lsp]{lang="EN-US"}[缓冲区之前的大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[newLspBuf]{lang="EN-US"}*]{#struct_0_16293_x2703_1839073269}[：新的]{lang="EN-US" style="font-family:宋体"}[lsp]{lang="EN-US"}[缓冲区的大小]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Processing the physical circuit board Insert event]{lang="EN-US"}]{#struct_0_16293_x2703_x730286267}

[[处理接口板插入事件]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1689716556}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1220865892}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Processing the physical circuit add event on circuit : *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_969115037}

[[物理接口添加事件]{style="font-family:宋体"}]{#struct_0_16293_x2703_1719891610}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730482875}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x511259697}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-EVT: Processing the physical circuit delete event on circuit : *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1705115088}

[[物理接口]{style="font-family:宋体"}]{#struct_0_16293_x2703_549276958} [删除事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730417339}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x2103081788}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-EVT: Processing Down \--\> Up event on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1852816940}

[[接口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_16293_x2703_1797288550}[到]{style="font-family:宋体"}[Up]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_819835931}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x730089659}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-EVT: Processing Up \--\> Down event on circuit  *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_630329832}

[[接口]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_16293_x2703_2061413113}[到]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_942777761}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x730024123}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-EVT: Processing the physical circuit Param change event on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x153153724}

[[接口配置改变处理事件]{style="font-family:宋体"}]{#struct_0_16293_x2703_x532442061}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1420217294}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x730613950}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-EVT: Processing board remove event on circuit  *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x924952716}

[[接口板拔出事件]{style="font-family:宋体"}]{#struct_0_16293_x2703_x422384908}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730548414}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x578648246}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-EVT: Processing the logical address add event  : *ipAddr*]{lang="EN-US"}]{#struct_0_16293_x2703_87907820}

[[逻辑接口添加处理事件]{style="font-family:宋体"}]{#struct_0_16293_x2703_1728667776}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730745022}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[ipAddr]{lang="EN-US"}*]{#struct_0_16293_x2703_x929850452}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Processing the logical address delete event  : *ipAddr* ]{lang="EN-US"}]{#struct_0_16293_x2703_874250711}

[[逻辑接口删除处理事件]{style="font-family:宋体"}]{#struct_0_16293_x2703_x730679486}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_978457369}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddr]{lang="EN-US"}*]{#struct_0_16293_x2703_x458481582}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Reset processing with backinfo: module *moudleId*, event *eventId*, phase *phaseId*.]{lang="EN-US"}]{#struct_0_16293_x2703_x730351806}

[[进程]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_16293_x2703_x138383946}[的阶段信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x342403375}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[moudleId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1202414408}[：模块]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventid]{lang="EN-US"}*]{#struct_0_16293_x2703_x730286270}[：触发]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[phaseId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1689651019}[：]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[所处的阶段]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Reset change into phase *phaseId*]{lang="EN-US"}]{#struct_0_16293_x2703_106995668}

[[进程]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_16293_x2703_x730482878}[进入下一个阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x511587377}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[moudleId]{lang="EN-US"}*]{#struct_0_16293_x2703_1795901213}[：模块]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventid]{lang="EN-US"}*]{#struct_0_16293_x2703_x730417342}[：触发]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[phaseId]{lang="EN-US"}*]{#struct_0_16293_x2703_x2103671611}[：]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[所处的阶段]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Reset processing receive event *eventId.*]{lang="EN-US"}]{#struct_0_16293_x2703_x391356173}

[[进程收到]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_16293_x2703_x730089662}[触发事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_630919657}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventid]{lang="EN-US"}*]{#struct_0_16293_x2703_x675680453}[：触发]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*procId*-EVT: Reset begin]{lang="EN-US"}]{#struct_0_16293_x2703_x730024126}

[[进程]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_16293_x2703_x152957116}[开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_653050546}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Reset finished, process with reset reason *eventId*]{lang="EN-US"}]{#struct_0_16293_x2703_x730613949}

[[进程]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_16293_x2703_x924493965}[结束事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_418996015}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventid]{lang="EN-US"}*]{#struct_0_16293_x2703_x730548413}[：触发]{lang="EN-US" style="font-family:宋体"}[reset]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[]{#table_struct_0_x497526536}[[ISIS-*procId*-EVT: Updt receive lsp change event.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x578713782}

[[UPDT]{lang="EN-US"}]{#struct_0_16293_x2703_437024580}[模块收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文改变事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1926856215}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT:]{lang="EN-US" style="font-size:
  9.0pt"}[ ]{lang="EN-US"}]{#struct_0_16293_x2703_x524072543}[Updt receive interface : *circuitName* state change to state(*eventType*).]{lang="EN-US" style="font-size:9.0pt"}

[[UPDT]{lang="EN-US"}]{#struct_0_16293_x2703_x809899611}[模块收到接口状态改变事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730745021}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x929915988}[：]{lang="EN-US" style="font-family:
  宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[eventType]{lang="EN-US"}*]{#struct_0_16293_x2703_1239852020}[：事件类型]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT:]{lang="EN-US" style="font-size:
  9.0pt"}[ ]{lang="EN-US"}]{#struct_0_16293_x2703_x623968949}[IS-IS ipv6 state change, inform DEC update ipv6 prefix.]{lang="EN-US" style="font-size:9.0pt"}

[[UPDT]{lang="EN-US"}]{#struct_0_16293_x2703_591373968}[模块通知路由模块更新]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_110961917}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT:]{lang="EN-US" style="font-size:
  9.0pt"}[ ]{lang="EN-US"}]{#struct_0_16293_x2703_x730679485}[Updt receive authen change event.]{lang="EN-US" style="font-size:9.0pt"}

[[UPDT]{lang="EN-US"}]{#struct_0_16293_x2703_978260761}[模块收到认证改变事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_849801897}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-EVT: Updt receive *lsplevel* fast flood event]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x650457759}

[[UPDT]{lang="EN-US"}]{#struct_0_16293_x2703_x958873008}[模块收到]{style="font-family:宋体"}[fast-flood]{lang="EN-US"}[快速扩散事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x730351805}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsplevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x138318410}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-EVT: Receive BGP convergence message, quit the overload state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x949644389}

[[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x949578853}[进程收到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[收敛消息，退出]{style="font-family:宋体"}[overload]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1048791540}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{style="font-family:宋体"}

[[ISIS-*procId*-EVT: Receive IPv6 BGP convergence message, quit the overload state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x949120102}

[[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x973205301}[进程收到]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[收敛消息，退出]{style="font-family:宋体"}[overload]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x949054566}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1253017355}

[[\# ]{lang="EN-US"}]{#struct_0_16293_x2703_752874711}[在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[消息事件调试信息开关。在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis event]{lang="EN-US"}]{#struct_0_16293_x2703_x306338568}

[\*Apr  8 05:58:11:217 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-EVT: Processing the logical address delete event : 1.1.1.2/24]{lang="EN-US"}

[\*Apr  8 05:58:11:218 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-EVT: Processing the logical address add event : 2.2.2.2/24]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x940206625}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上删除主逻辑接口地址和]{style="font-family:宋体"}[添加新的主逻辑接口的事件]{style="font-family:宋体"}*

::: {#-1182630541 .myid}
[]{#_Toc404788104}[]{#struct_0_16293_x2703_x730286269}[]{#_Toc303704544}[]{#_Toc303149289}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis graceful-restart**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1690109772}

[**[debuging isis graceful-restart]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x1267736424}

[**[undo debuging graceful-restart]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_2004366112}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x816250885}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_525980147}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1260151289}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1173528562}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x730482877}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x511128625}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1025799923}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x310227724}

[**[debuging isis graceful-restart]{lang="EN-US"}**]{#struct_0_16293_x2703_26953364}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[ GR]{lang="EN-US"}[调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}**[undo debugging isis graceful-restart]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[ GR]{lang="EN-US"}[调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1849569730}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关处于]{style="font-family:宋体"}[关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1924029605}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging isis graceful-restart]{lang="EN-US"}]{#struct_0_16293_x2703_x829928109}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x495804748}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x730417341}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x2103606075}

[[ISIS-*procId*-GR: Temporary DIS type Level-*Level*, on  *CircName*, DIS: *DisStr*.]{lang="EN-US"}]{#struct_0_16293_x2703_968968444}

[[GR Helper]{lang="EN-US"}]{#struct_0_16293_x2703_1011509055}[端进行临时]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x829934404}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1234882735}[：进行]{lang="EN-US" style="font-family:宋体"}[DIS]{lang="EN-US"}[选举的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_x730089661}[：]{lang="EN-US" style="font-family:宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DisStr]{lang="EN-US"}]{#struct_0_16293_x2703_630854121}[：选举出来的临时]{style="font-family:宋体"}[DIS]{lang="EN-US"}

[[ISIS-*procId*-GR: All Level-*Level* T1 timers have stopped.]{lang="EN-US"}]{#struct_0_16293_x2703_x1439466950}

[[T1]{lang="DA"}]{#struct_0_16293_x2703_x914977653}[定时器停止]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_395593626}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x730024125}[：]{lang="EN-US" style="font-family:宋体"}[T1]{lang="EN-US"}[定时器所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR: Adjacency(*SystemIdr*) on *CircName*(Level-*level*) comes out RestartMode.]{lang="EN-US"}]{#struct_0_16293_x2703_x152760508}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16293_x2703_1820979884}[状态发生变化，由]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态变为非]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1218661428}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1480159162}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_835469995}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1209045350}[：邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR: Adjacency(*SystemId*) on *CircName* (Level-*level*) comes in RestartMode.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x141128255}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16293_x2703_206812576}[状态发生变化，由非]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1952681451}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_835535531}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1551566861}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1128950739}[：邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x735458067}[Level-*Level* NBR(*SystemId*) SA bit set, adjacency not advertised.]{lang="EN-US" style="font-size:
  9.0pt"}

[[邻居报文]{style="font-family:宋体"}[GR TLV]{lang="EN-US"}]{#struct_0_16293_x2703_835338923}[中的]{style="font-family:宋体"}[SA]{lang="EN-US"}[比特位被设置上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1882296523}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1798195548}[：邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_962311778}[：]{style="font-family:宋体"}[邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835404459}[Level-*Level* NBR(*SystemId*) SA bit clear, adjacency advertised.]{lang="EN-US" style="font-size:9.0pt"}

[[邻居报文]{style="font-family:宋体"}[GR TLV]{lang="EN-US"}]{#struct_0_16293_x2703_1160145975}[中的]{style="font-family:宋体"}[SA]{lang="EN-US"}[比特位被清除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x42231113}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x73894507}[：邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="EN-US"}*]{#struct_0_16293_x2703_835732139}[：]{style="font-family:宋体"}[邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_266324583}[Receive restart request hello from *SystemId*, on *CircName* (Level-*Level*)]{lang="EN-US" style="font-size:9.0pt"}

[[收到邻居的]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1533178352}[GR]{lang="DA"}[请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="DA"}*]{#struct_0_16293_x2703_x1959081495}[：]{style="font-family:宋体"}[IS-IS]{lang="DA"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="DA"}*]{#struct_0_16293_x2703_835797675}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="DA"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1251376094}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_2076601786}[：邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835601067}[Receive *helloType* hello with RR bit set from nbr *SystemId*, on *CircName*]{lang="EN-US" style="font-size:9.0pt"}

[[收到]{style="font-family:宋体"}]{#struct_0_16293_x2703_1786396317}[RR]{lang="DA"}[置位的]{style="font-family:宋体"}[Hello]{lang="DA"}[报文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="DA"}*]{#struct_0_16293_x2703_1773953225}[：]{style="font-family:宋体"}[IS-IS]{lang="DA"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[helloType]{lang="EN-US"}*]{#struct_0_16293_x2703_x1636325252}[：取值为]{lang="EN-US" style="font-family:宋体"}[LAN L1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LAN L2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[P2P]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[SystemId]{lang="DA"}*]{#struct_0_16293_x2703_835666603}[：邻居的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="DA"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_1452442297}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x595575970}[RA received on circuit: Circ*Name* Level-*Level*]{lang="EN-US" style="font-size:
  9.0pt"}

[[收到邻居的]{style="font-family:宋体"}]{#struct_0_16293_x2703_835994283}[GR]{lang="DA"}[应答]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="DA"}*]{#struct_0_16293_x2703_x1896130932}[：]{style="font-family:宋体"}[IS-IS]{lang="DA"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_x163719169}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_836059819}[：]{style="font-family:
  宋体"}[邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_214878255}[Interface(*CircName*) Level-*Level* T1 timer expired count: *T1TimerExpCnt*.]{lang="EN-US" style="font-size:9.0pt"}

[[T1]{lang="DA"}]{#struct_0_16293_x2703_472272387}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="DA"}*]{#struct_0_16293_x2703_835469996}[：]{style="font-family:宋体"}[IS-IS]{lang="DA"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1209045349}[：]{style="font-family:宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1781120510}[：]{style="font-family:宋体"}[邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[T1TimerExpCnt]{lang="EN-US"}*]{#struct_0_16293_x2703_835535532}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时的次数，超时]{lang="EN-US" style="font-family:宋体"}[10]{lang="EN-US"}[次之后取消]{lang="EN-US" style="font-family:宋体"}[T1]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x1551566862}[Interface(*CircName*) Level-*Level* T1 timer expired count has arrived max.]{lang="EN-US" style="font-size:
  9.0pt"}

[[T1]{lang="DA"}]{#struct_0_16293_x2703_x1532235266}[定时器超时次数达到最大次数]{style="font-family:宋体"}[10]{lang="DA"}[次]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="DA"}*]{#struct_0_16293_x2703_835338924}[：]{style="font-family:宋体"}[IS-IS]{lang="DA"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1882296516}[：]{style="font-family:宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1038615125}[：]{style="font-family:宋体"}[邻居所属的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835404460}[Graceful-restart complete.]{lang="EN-US" style="font-size:9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_x1560843218}[完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x2077180609}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835732140}[Enter phase(*GrPhase*)]{lang="EN-US" style="font-size:9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_x2072327584}[进入下一阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x2141442011}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[GrPhase]{lang="EN-US"}*]{#struct_0_16293_x2703_835797676}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[阶段，包括]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步阶段、第一次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算阶段、引入计算阶段、第二次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算阶段、]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成阶段、]{style="font-family:宋体"}[GR]{lang="EN-US"}[完成阶段]{style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x1251376091}[T3 timer stoped owe to all T2 timer stopped.]{lang="EN-US" style="font-size:
  9.0pt"}

[[由于]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_16293_x2703_1673317259}[定时器停止，导致停止]{style="font-family:宋体"}[T3]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_835601068}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_1786396322}[Received Level-*Level* T2 timer cancel event(*T2StopEvent*).]{lang="EN-US" style="font-size:
  9.0pt"}

[[收到触发]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_16293_x2703_835666604}[停止的事件，事件类型包括"所有]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止"和"]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成"。两个事件都发生时才真正停止]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1452442298}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x596165794}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[T2StopEvent]{lang="EN-US"}*]{#struct_0_16293_x2703_835994284}[：]{style="font-family:宋体"}[触发停止]{lang="EN-US" style="font-family:宋体"}[T2]{lang="EN-US"}[定时器的事件，包括"所有]{lang="EN-US" style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止"和"]{lang="EN-US" style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成"]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x1896130929}[Level-*Level* T2 timer stopped]{lang="EN-US" style="font-size:
  9.0pt"}

[[停止]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_16293_x2703_836059820}[定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1788856376}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1583046566}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835469993}[Level-*Level* T2 timer expired]{lang="EN-US" style="font-size:9.0pt"}

[[T2]{lang="EN-US"}]{#struct_0_16293_x2703_x1209045352}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_835535529}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_787085307}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_x1162440411}[T3 timer expired before T2 timer.]{lang="EN-US" style="font-size:
  9.0pt"}

[[T3]{lang="EN-US"}]{#struct_0_16293_x2703_835338921}[定时器先于]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1882296521}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835404457}[Graceful-restart enter *GrTypeStr* phase(*LSDB synchronization*).]{lang="EN-US" style="font-size:9.0pt"}

[[开始]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16293_x2703_1160145969}[，分为]{style="font-family:宋体"}[restarting ]{lang="EN-US"}[方式和]{style="font-family:宋体"}[starting]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x41444682}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[GrTypeStr]{lang="EN-US"}*]{#struct_0_16293_x2703_835732137}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式，分为]{lang="EN-US" style="font-family:宋体"}[restarting]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[starting]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_266324577}[Begin to purge local Level-]{lang="EN-US" style="font-size:9.0pt"}*[Level]{lang="EN-US" style="font-size:9.0pt"}*[ ]{lang="EN-US" style="font-size:9.0pt"}[lsp]{lang="EN-US" style="font-size:9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_835797673}[完成，将本地原来生成、现在失效的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[清除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1251376096}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_835601065}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16293_x2703_1786396319}[:Purge Level-]{lang="EN-US" style="font-size:
  9.0pt"}*[Level]{lang="EN-US" style="font-size:9.0pt"}*[ lsp L*spid*-*LspNum*]{lang="EN-US" style="font-size:9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_1773297865}[完成，将本地原来生成、现在失效的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[清除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_835666601}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_1452442295}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Lspid]{lang="EN-US"}*]{#struct_0_16293_x2703_835994281}[：]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LspNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x1896130934}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-GR: End to purge local Level-]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_836059817}*[Level]{lang="EN-US" style="font-size:
  9.0pt"}*[ lsp]{lang="EN-US" style="font-size:9.0pt"}

[[清除失效]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_214878261}[结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_835469994}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1209045351}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR: Synchronized Level-]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16293_x2703_835535530}*[Level]{lang="EN-US" style="font-size:9.0pt"}*[ csnp from *SourceId* on circuit *CircName* range from *StartLspid* -*LspNum* to *EndLspidSysId* -*LspNum*]{lang="EN-US" style="font-size:9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_x1551566860}[过程中收到]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端发送的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_835338922}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1882296522}[：]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[SourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_835404458}[：]{style="font-family:宋体"}[Helper]{lang="EN-US"}[的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_1160145974}[：]{style="font-family:宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[StartLspId]{lang="EN-US"}*]{#struct_0_16293_x2703_835732138}[：]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文中开始的]{lang="EN-US" style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[LspNum]{lang="EN-US"}*]{#struct_0_16293_x2703_266324584}[：]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文中]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的序号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[EndLspId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1533178357}[：]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文中结束的]{lang="EN-US" style="font-family:宋体"}[LSPID]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:9.0pt"}[ ]{lang="EN-US"}]{#struct_0_16293_x2703_835797674}[Level-]{lang="EN-US" style="font-size:9.0pt"}*[Level]{lang="EN-US" style="font-size:9.0pt"}*[ lsdb synchronization is complete]{lang="EN-US" style="font-size:9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_x1251376093}[过程中]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_835601066}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_835666602}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-*procId*-GR:]{lang="EN-US" style="font-size:
  9.0pt"}[ ]{lang="EN-US"}]{#struct_0_16293_x2703_1452442296}[Level-]{lang="EN-US" style="font-size:9.0pt"}*[Level]{lang="EN-US" style="font-size:9.0pt"}*[ csnp set synchronization is complete on circuit *CircName*]{lang="EN-US" style="font-size:
  9.0pt"}

[[GR]{lang="EN-US"}]{#struct_0_16293_x2703_835994282}[过程中]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[接收完全]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1896130931}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_836059818}[：]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[CircName]{lang="EN-US"}*]{#struct_0_16293_x2703_214878256}[：]{style="font-family:宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_472272390}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_x799441646}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[0000.0000.0001]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[12.0.0.1/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[0000.0000.0002]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[12.0.0.2/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在不同区域，建立]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[类型的邻居。在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<RouterB\> debugging isis graceful-restart]{lang="EN-US"}]{#struct_0_16293_x2703_835469991}

[\<RouterB\> reset isis all graceful-restart]{lang="EN-US"}

[%Sep  5 16:09:47:646 2011 RouterB ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 100, Level-2 adjacency 0000.0000.0001 (GigabitEthernet1/0/2), state change to: DOWN.]{lang="EN-US"}

[\*Sep  5 16:09:47:735 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Graceful-restart enter restarting phase(LSDB synchronization).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1209045354}*[进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[，方式为]{style="font-family:宋体"}[restarting]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步阶段]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:751 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x2110496723}

[ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-2 T1 timer expired count: 1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 16:09:47:751 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_424442239}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}[1]{lang="EN-US"}[次]{style="font-family:宋体"}*

[[%Sep  5 16:09:47:752 2011 RouterB ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 100, Level-2 adjacency 0000.0000.0001 (GigabitEthernet1/0/2), state change to: UP.]{lang="EN-US"}]{#struct_0_16293_x2703_77415962}

[\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: RA received on circuit: GigabitEthernet1/0/2 Level-2]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Synchronized Level-2 csnp from 0000.0000.0001.00 on circuit GigabitEthernet1/0/2 range from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_441481134}*[收到]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端发送的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_835535527}

[ISIS-100-GR: RA received on circuit: GigabitEthernet1/0/2 Level-1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_787085301}*[收到]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1162440413}

[ISIS-100-GR: Level-2 csnp set synchronization is complete on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[*[// Level-2]{lang="EN-US"}*]{#struct_0_16293_x2703_x1295524546}*[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[接收完全]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_1723300039}

[ISIS-100-GR: All Level-2 T1 timers have stopped.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x413387777}*[关闭]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_835338919}

[ISIS-100-GR: Received Level-2 T2 timer cancel event(All T1 stopped).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_456355647}*[触发关闭]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器，事件为所有]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:786 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x874448236}

[ISIS-100-GR: Level-2 lsdb synchronization is complete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 16:09:47:786 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Received Level-2 T2 timer cancel event(LSDB sync).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_197025192}*[触发关闭]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器，事件为]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}*

[[\*Sep  5 16:09:47:786 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1730035540}

[ISIS-100-GR: Level-2 T2 timer stopped]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_176226594}*[停止]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\<RouterB\>]{lang="EN-US"}]{#struct_0_16293_x2703_835404455}

[\*Sep  5 16:09:50:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 2.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 16:09:50:754 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: RA received on circuit: GigabitEthernet1/0/2 Level-1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 10.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count has arrived max.]{lang="EN-US"}

[*[// Level-1]{lang="EN-US"}*]{#struct_0_16293_x2703_1160145971}*[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时次数达到]{style="font-family:宋体"}[10]{lang="EN-US"}[次]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x41968969}

[ISIS-100-GR: All Level-1 T1 timers have stopped.]{lang="EN-US"}

[*[// Level1]{lang="EN-US"}*]{#struct_0_16293_x2703_x116980957}*[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_2144260863}

[ISIS-100-GR: Received Level-1 T2 timer cancel event(All T1 stopped).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1977169677}*[触发关闭]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器，事件为]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_835732135}

[ISIS-100-GR: Level-1 T2 timer stopped]{lang="EN-US"}

[*[// Level-2]{lang="EN-US"}*]{#struct_0_16293_x2703_266324579}*[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1960145386}

[ISIS-100-GR: T3 timer stoped owe to all T2 timer stopped.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_36048720}*[两个]{style="font-family:宋体"}[Level]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器都已停止，此时停止]{style="font-family:宋体"}[T3]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1587664211}

[ISIS-100-GR: Enter phase(First SPF computation)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1355942264}*[进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[的第一次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算阶段]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:825 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_388840118}

[ISIS-100-GR: Enter phase(Redistribution)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_386393095}*[第一次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算结束，进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[的引入路由阶段]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:825 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_835797671}

[ISIS-100-GR: Enter phase(Second SPF computation)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1251376098}*[路由引入结束，进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[的第二次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算阶段]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_463463678}

[ISIS-100-GR: Enter phase(LSP generation)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_2145064863}*[第二次]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算结束，进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成阶段]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_435578095}

[ISIS-100-GR: Begin to purge local Level-1 lsp]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1567428726}*[开始清除本地生成的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的失效]{style="font-family:宋体"}[LSP]{lang="EN-US"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_157462129}

[ISIS-100-GR: End to purge local Level-1 lsp]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1136771122}*[本地生成的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的失效]{style="font-family:宋体"}[LSP]{lang="EN-US"}[清除完成]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_835601063}

[ISIS-100-GR: Begin to purge local Level-2 lsp]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1786396313}*[开始清除本地生成的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的失效]{style="font-family:宋体"}[LSP]{lang="EN-US"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_1773691081}

[ISIS-100-GR: End to purge local Level-2 lsp]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1902297137}*[本地生成的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的失效]{style="font-family:宋体"}[LSP]{lang="EN-US"}[清除完成]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_1963033082}

[ISIS-100-GR: Enter phase(Finish)]{lang="EN-US"}

[*[// LSP]{lang="EN-US"}*]{#struct_0_16293_x2703_x452021867}*[生成完成，进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[结束阶段]{style="font-family:宋体"}*

[[\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_835666599}

[ISIS-100-GR: Graceful-restart complete.]{lang="EN-US"}

[*[// GR]{lang="EN-US"}*]{#struct_0_16293_x2703_695662426}*[完成]{style="font-family:宋体"}*

::: {#1828341190 .myid}
[]{#_Toc404788105}[]{#struct_0_16293_x2703_x652921868}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis ha-event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_75005520}

[**[debuging isis ha-event]{lang="EN-US"}**]{#struct_0_16293_x2703_x2125518290}

[**[undo debuging isis ha-event]{lang="EN-US"}**]{#struct_0_16293_x2703_x228997678}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_831163677}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_x377813079}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x425625701}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_835994279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1851500926}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_2105398698}

[**[debuging isis ha-event]{lang="EN-US"}**]{#struct_0_16293_x2703_2044443557}[命令用来打开]{style="font-family:宋体"}[IS-IS HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging isis ha-event]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[IS-IS HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS HA]{lang="EN-US"}]{#struct_0_16293_x2703_x209206469}[调试信息开关[处于关闭状态]{#OLE_LINK1}。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1894767088}[进程的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging isis ha-event]{lang="EN-US"}]{#struct_0_16293_x2703_x1528705825}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x472450548}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_836059815}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_214878259}

[[ISIS-HA: RtBackup ISIS ]{lang="EN-US"}]{#struct_0_16293_x2703_472272375}*[datatype.]{lang="EN-US"}*

[[实时备份]{style="font-family:宋体"}[ISIS ]{lang="EN-US"}]{#struct_0_16293_x2703_347569431}[数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[datatype]{lang="EN-US"}*]{#struct_0_16293_x2703_1296629554}[：数据类型]{lang="EN-US" style="font-family:宋体"}

[[ISIS-HA: Receive RIB reconnet event]{lang="EN-US"}]{#struct_0_16293_x2703_x298828045}

[[收到重连]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_835469992}[消息]{style="font-family:宋体"}

[[ISIS-HA: Receive RIB pull-route event]{lang="EN-US"}]{#struct_0_16293_x2703_x1209045353}

[[收到更新路由消息]{style="font-family:宋体"}]{#struct_0_16293_x2703_262156272}

[[ISIS-HA: Receive ISIS RtData.]{lang="EN-US"}]{#struct_0_16293_x2703_x2020339531}

[[收到实时备份数据]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1997459190}

[[ISIS-HA: Batch backup ISIS data.]{lang="EN-US"}]{#struct_0_16293_x2703_835535528}

[[批量备份]{style="font-family:宋体"}]{#struct_0_16293_x2703_787085308}

[[ISIS-HA: Stop ISIS data.]{lang="EN-US"}]{#struct_0_16293_x2703_x1162440420}

[[停止备份处理]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1699005681}

[[ISIS-HA: Degrade (master to standby), delete ISIS data.]{lang="EN-US"}]{#struct_0_16293_x2703_x1221634439}

[[主板变为备板，删除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_835338920}[相关数据]{style="font-family:宋体"}

[[ISIS-HA: Upgrade (standby to master), smooth ISIS data.]{lang="EN-US"}]{#struct_0_16293_x2703_x1882296520}

[[备板升级为主板，平滑]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_232111607}[相关数据]{style="font-family:宋体"}

[[ISIS-HA: Notify NBR smooth start]{lang="EN-US"}]{#struct_0_16293_x2703_x1564394047}

[[通知]{style="font-family:宋体"}[NBR]{lang="EN-US"}]{#struct_0_16293_x2703_1211982403}[平滑数据开始]{style="font-family:宋体"}

[[ISIS-HA: Notify NBR smooth end]{lang="EN-US"}]{#struct_0_16293_x2703_835404456}

[[通知]{style="font-family:宋体"}[NBR]{lang="EN-US"}]{#struct_0_16293_x2703_1160145968}[平滑数据结束]{style="font-family:宋体"}

[[ISIS-HA: Notify RIB disconnect start]{lang="EN-US"}]{#struct_0_16293_x2703_x41510218}

[[通知与]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1712002852}[连接断开处理开始]{style="font-family:宋体"}

[[ISIS-HA: Notify RIB disconnect end]{lang="EN-US"}]{#struct_0_16293_x2703_835732136}

[[通知与]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_266324578}[连接断开处理结束]{style="font-family:宋体"}

[[ISIS-HA: Notify RIB smooth start]{lang="EN-US"}]{#struct_0_16293_x2703_x1960145385}

[[通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1530035221}[平滑数据开始]{style="font-family:宋体"}

[[ISIS-HA: Notify RIB smooth end]{lang="EN-US"}]{#struct_0_16293_x2703_835797672}

[[通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1251376095}[平滑数据结束]{style="font-family:宋体"}

[[ISIS-HA: Connect to RIB successfully.]{lang="EN-US"}]{#struct_0_16293_x2703_x652281569}

[[跟]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1145668283}[建立连接成功]{style="font-family:宋体"}

[[ISIS-HA: Connect to RIB failed, try to reconnect later.]{lang="EN-US"}]{#struct_0_16293_x2703_835601064}

[[跟]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_1786396318}[建立连接失败，稍后重连]{style="font-family:宋体"}

[[ISIS-HA: Receive SIGKILL Signal from SCM.]{lang="EN-US"}]{#struct_0_16293_x2703_1773363401}

[[从]{style="font-family:宋体"}[SCM]{lang="EN-US"}]{#struct_0_16293_x2703_x495277628}[收到资源回退的消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_835666600}

[[\# ]{lang="EN-US"}]{#struct_0_16293_x2703_1452442294}[在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，路由器类型为]{style="font-family:宋体"}[level-1-2]{lang="EN-US"}[，]{style="font-family:宋体"}[network-entity]{lang="EN-US"}[为]{style="font-family:宋体"}[10.7798.1111.1111.00]{lang="EN-US"}[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS HA]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis ha-event]{lang="NO-BOK"}]{#struct_0_16293_x2703_x595379362}

[\*Apr  8 22:01:25:812 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-HA: RtBackup ISIS systemID.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr  8 22:01:25:813 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-HA: RtBackup ISIS Process Area Data.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x897905558}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上删除]{style="font-family:宋体"}[network-entity]{lang="EN-US"}*

::: {#-818448459 .myid}
[]{#_Toc404788106}[]{#struct_0_16293_x2703_1889436760}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis miscellaneous-errors**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1161469918}

[**[debuging isis ]{lang="EN-US"}[miscellaneous-errors]{lang="EN-US"}**]{#struct_0_16293_x2703_x835484067}

[**[undo debuging ]{lang="EN-US"}[miscellaneous-errors]{lang="EN-US"}**]{#struct_0_16293_x2703_835994280}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1896130933}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1729803110}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1642582966}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1647748614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_397350998}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1406004369}

[**[debuging isis ]{lang="EN-US"}[miscellaneous-errors]{lang="EN-US"}**]{#struct_0_16293_x2703_x89021749}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程无关调试信息开关。]{style="font-family:宋体"}**[undo debugging isis ]{lang="EN-US"}[miscellaneous-errors]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程无关调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1482725909}[进程无关调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_836059816}[进程的进程无关调试信息开关。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging isis miscellaneous-errors]{lang="EN-US"}]{#struct_0_16293_x2703_214878262}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x476330768}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_2046250498}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_446707484}

[[ISIS-ERR: Create all hello socket failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x527232719}

[[创建]{style="font-family:宋体"}[hello socket]{lang="EN-US"}]{#struct_0_16293_x2703_x2060129812}[失败]{style="font-family:宋体"}

[[ISIS-ERR: Destroy all hello socket failed.]{lang="EN-US"}]{#struct_0_16293_x2703_x1893413360}

[[删除]{style="font-family:宋体"}[hello socket]{lang="EN-US"}]{#struct_0_16293_x2703_x1745486312}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_29064334}

[[\# ]{lang="EN-US"}]{#struct_0_16293_x2703_x2099863755}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程。打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程无关调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis miscellaneous-errors]{lang="EN-US"}]{#struct_0_16293_x2703_1892902882}

[\*Apr  8 22:04:12:389 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-ERR: Create all hello socket failed ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1383689816}*[收发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的]{style="font-family:宋体"}[socket]{lang="EN-US"}[创建失败]{style="font-family:宋体"}*

::: {#-528753002 .myid}
[]{#_Toc404788107}[]{#struct_0_16293_x2703_x760527118}[]{#_Toc341341558}[]{#_Toc341285950}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis redistribute**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x2068229792}

[**[debugging isis redistribute]{lang="EN-US"}**[ { **ipv4** \[ **topology** *topo-name* \] \| **ipv6** } { **event** \| **prefix** \[ *prefix* \[ *mask-length* \] \] }]{lang="EN-US"}]{#struct_0_16293_x2703_x1893347824}

[**[undo debugging isis redistribute]{lang="EN-US"}**[ { **ipv4** \[ **topology** *topo-name* \] \| **ipv6** } { **event** \| **prefix** }]{lang="EN-US"}]{#struct_0_16293_x2703_2123987930}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1989980536}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_1393981002}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1265951467}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1028012222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1143792798}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_884628024}

[**[ipv4]{lang="EN-US"}**]{#struct_0_16293_x2703_x1893544432}[：打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由引入开关。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_16293_x2703_866687665}[：打开指定拓扑的引入开关。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则表示打开公网的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由引入开关。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_16293_x2703_1082299040}[：打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由引入开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_16293_x2703_334907259}[：打开路由引入事件开关。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**]{#struct_0_16293_x2703_750670373}[：打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由引入前缀开关。]{style="font-family:宋体"}

[*[prefix]{lang="EN-US"}*[ \[ *mask-length* \]]{lang="EN-US"}]{#struct_0_16293_x2703_516265220}[：表示打开特定前缀开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_196750532}

[**[debuging isis ]{lang="EN-US"}[redistribute ipv4 event]{lang="EN-US"}**]{#struct_0_16293_x2703_x1477731794}[命令用来打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入事件调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debuging isis** **redistribute ipv4 event**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入事件调试信息开关。]{style="font-family:宋体"}

[**[debuging isis ]{lang="EN-US"}[redistribute ipv4 prefix]{lang="EN-US"}**]{#struct_0_16293_x2703_x1412488723}[命令用来打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入前缀调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debuging isis** **redistribute ipv4 prefix**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入前缀调试信息开关。]{style="font-family:宋体"}

[**[debuging isis ]{lang="EN-US"}[redistribute ipv6 event]{lang="EN-US"}**]{#struct_0_16293_x2703_x1893478896}[命令用来打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[引入事件调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debuging isis** **redistribute ipv6 event**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[引入事件调试信息开关。]{style="font-family:宋体"}

[**[debuging isis ]{lang="EN-US"}[redistribute ipv6 prefix]{lang="EN-US"}**]{#struct_0_16293_x2703_x900581803}[命令用来打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[引入前缀调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debuging isis** **redistribute ipv6 prefix**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[引入前缀调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_956982750}[的引入事件和前缀调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定前缀，则打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x882072936}[的所有前缀调试信息开关。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging isis redistribute ipv4 event]{lang="EN-US"}]{#struct_0_16293_x2703_x1881384239}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x477326276}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_575999259}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_1782131142}

[[ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* request rib to stop *rpaname* batch notify]{lang="EN-US"}]{#struct_0_16293_x2703_x1893151216}

[[通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_1993110489}[停止路由引入批量上报]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_867408561}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_1122392198}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x1586422478}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* deregister *rpaname* notify to rib]{lang="EN-US"}]{#struct_0_16293_x2703_1728647186}

[[通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x462831862}[去注册路由引入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_867343025}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893085680}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x1108288248}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* request rib for *rpaname* query]{lang="EN-US"}]{#struct_0_16293_x2703_x710262092}

[[向]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1061689155}[查询路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861999087}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_x999426893}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893282288}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* register *rpaname* notify to rib]{lang="EN-US"}]{#struct_0_16293_x2703_x1684962852}

[[通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_1275829749}[注册路由引入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862064623}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_1110317712}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_168065508}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid*  is added to *rpaname* *batchtype* batch list]{lang="EN-US"}]{#struct_0_16293_x2703_x1893216752}

[[添加]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1801524454}[进程到引入路由批量链表中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861868015}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_x2004093520}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_1399459113}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[batchtype]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892889072}[：批量类型，]{lang="EN-US" style="font-family:宋体"}[register]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[query]{lang="EN-US"}

[[ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* is deleted from *rpaname* *batchtype* batch list]{lang="EN-US"}]{#struct_0_16293_x2703_x1568750089}

[[从引入路由批量链表中删除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x243510779}[进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861933551}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_2135101746}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_1960547226}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[batchtype]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892823536}[：批量类型，]{lang="EN-US" style="font-family:宋体"}[register]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[query]{lang="EN-US"}

[[ISIS-RDM(TopoIndex *mtindex*): Reregister *rpaname* attr to rib]{lang="EN-US"}]{#struct_0_16293_x2703_x1612646956}

[[向]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1953223084}[重新注册路由属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862261231}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x778586194}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Register *rpaname* attr to rib]{lang="EN-US"}]{#struct_0_16293_x2703_x1893413359}

[[向]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_627363291}[注册路由属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862326767}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x1881276525}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Deregister *rpaname* attr to rib]{lang="EN-US"}]{#struct_0_16293_x2703_x1893347823}

[[向]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_x1767694839}[去注册路由属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862130159}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x935182218}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): IS-IS instance *intsid* receive *batchmsgtype* message]{lang="EN-US"}]{#struct_0_16293_x2703_x651637945}

[[接收到批量开始]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16293_x2703_x1893544431}[结束消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862195695}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[intsid]{lang="EN-US"}*]{#struct_0_16293_x2703_1485583567}[：实例号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[batchmsgtype]{lang="EN-US"}*]{#struct_0_16293_x2703_x1284046290}[：批量消息类型，批量开始]{lang="EN-US" style="font-family:
  宋体"}[/]{lang="EN-US"}[批量结束]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Process protocol *rpaname* attr msg]{lang="EN-US"}]{#struct_0_16293_x2703_x737964705}

[[处理路由属性消息]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1893478895}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861474799}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_665502138}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Process protocol *rpaname* smooth attr msg]{lang="EN-US"}]{#struct_0_16293_x2703_696161016}

[[处理路由属性平滑消息]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1893151215}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861540335}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_1589825962}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Route redist process, schedule type: *schedtype*]{lang="EN-US"}]{#struct_0_16293_x2703_x641352330}

[[处理引入调度消息]{style="font-family:宋体"}]{#struct_0_16293_x2703_428156883}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862064622}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[schedtype]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893085679}[：调度类型]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging isis redistribute ipv4 prefix]{lang="EN-US"}]{#struct_0_16293_x2703_814746949}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x482267228}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1714522521}

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x213952540}

[[ISIS-RDM(TopoIndex *mtindex*): Process common refresh message for redist prefix *prefix/masklen*, old protocol: *rpaname*, new protocol: *rpaname*,  flag: *flag*]{lang="EN-US"}]{#struct_0_16293_x2703_x1079907896}

[[处理引入路由刷新消息]{style="font-family:宋体"}]{#struct_0_16293_x2703_616388601}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861868014}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[prefix/masklen]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893282287}[：路由前缀和掩码长度]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x1637908685}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_16293_x2703_x1567414105}[：路由标记]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Process common delete message for redist prefix *prefix/masklen*, old protocol:  *rpaname*]{lang="EN-US"}]{#struct_0_16293_x2703_627154725}

[[处理引入路由删除消息]{style="font-family:宋体"}]{#struct_0_16293_x2703_1682857407}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1861933550}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[prefix/masklen]{lang="EN-US"}*]{#struct_0_16293_x2703_687199290}[：路由前缀和掩码长度]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rpaname]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893216751}[：路由协议名]{lang="EN-US" style="font-family:宋体"}

[[ISIS-RDM(TopoIndex *mtindex*): Process *procid* Adding redist prefix for *prefix/masklen*]{lang="EN-US"}]{#struct_0_16293_x2703_1398239927}

[[添加上报的路由到本地路由表]{style="font-family:宋体"}]{#struct_0_16293_x2703_838680442}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TopoIndex *mtindex*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862261230}[：]{lang="EN-US" style="font-family:宋体"}[指定拓扑的路由管理拓扑索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procid]{lang="EN-US"}*]{#struct_0_16293_x2703_1251763309}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[prefix/masklen]{lang="EN-US"}*]{#struct_0_16293_x2703_x721762593}[：路由前缀和掩码长度]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1892889071}

[[\# ]{lang="EN-US"}]{#struct_0_16293_x2703_x1165465562}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程。打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入事件开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis redistribute ipv4 event]{lang="NO-BOK"}]{#struct_0_16293_x2703_x923593509}

[\*Nov  1 12:51:08:773 2012 ]{lang="EN-US"}[RouterA]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-RDM(TopoIndex 0): ISIS process 1 is added to static register batch list]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1448845558}*[添加]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[到静态路由引入注册链表中]{style="font-family:宋体"}*

[[\*Nov  1 12:51:08:774 2012 ]{lang="EN-US"}]{#struct_0_16293_x2703_x1106493078}[RouterA]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-RDM(TopoIndex 0): ISIS process 1 register static notify to rib]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1330471221}*[向]{style="font-family:宋体"}[RIB]{lang="EN-US"}[注册静态路由引入]{style="font-family:宋体"}*

[[\*Nov  1 12:51:08:774 2012 ]{lang="EN-US"}]{#struct_0_16293_x2703_1305321470}[RouterA]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-RDM(TopoIndex 0): IS-IS instance 0 receive BatchStart message]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892823535}*[公网实例接收到]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由批量上报开始消息]{style="font-family:宋体"}*

[[\*Nov  1 12:51:08:775 2012 ]{lang="EN-US"}]{#struct_0_16293_x2703_1116236399}[RouterA]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-RDM(TopoIndex 0): IS-IS instance 0 receive BatchEnd message]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_938274452}*[公网实例接收到]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由批量上报结束消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_16293_x2703_1534158727}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程。打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入前缀开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis redistribute ipv4 prefix]{lang="NO-BOK"}]{#struct_0_16293_x2703_x698631723}

[\*Nov  1 13:17:07:637 2012 ]{lang="EN-US"}[RouterA]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-RDM(TopoIndex 0): Process common refresh message for redist prefix 200.0.0.0/24, old pro]{lang="EN-US"}

[tocol: static, new protocol: static, flag: 3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1543786039}*[接收到]{style="font-family:宋体"}[RIB]{lang="EN-US"}[上报的静态路由]{style="font-family:宋体"}[200.0.0.0/24]{lang="EN-US"}[刷新消息]{style="font-family:宋体"}*

[[\*Nov  1 13:17:07:637 2012 ]{lang="EN-US"}]{#struct_0_16293_x2703_x1893413362}[RouterA]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-RDM(TopoIndex 0): (ProID 1): Adding redist prefix for 200.0.0.0/24.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1386681570}*[添加引入路由]{style="font-family:宋体"}[200.0.0.0/2[]{#_Toc341341559}4]{lang="EN-US"}*

::: {#-1327360492 .myid}
[]{#_Toc404788108}[]{#struct_0_16293_x2703_x315429948}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis self-originate-update**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x223935778}

[**[debugging]{lang="EN-US"}**[ **isis** **self-originate-update** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x1469996057}

[**[undo]{lang="EN-US"}**[ **debugging** **isis** **self-originate-update** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x603684659}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1533098988}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_459355223}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1967498599}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1893347826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1008179952}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x155728123}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x674261114}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x358118078}

[**[debugging isis self-originate-update]{lang="EN-US"}**]{#struct_0_16293_x2703_1593153241}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[本地更新的调试信息开关。]{style="font-family:宋体"}**[undo debugging isis self-originate-update]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[本地更新的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x402523456}[本地更新的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_233798829}[进程的本地更新的调试信息开关。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging isis self-originate-update]{lang="EN-US"}]{#struct_0_16293_x2703_x1893544434}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x478929852}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x2049868842}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x211368512}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Purging level-*level* LSP \[*lsp-id*\]]{lang="EN-US"}]{#struct_0_16293_x2703_x1351780587}

[[清除]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_1898081016}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1796807663}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893478898}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_262217611}[：被清除]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: *tlv-name ip-address* into level-*level* LSPs, TLV: *tlv-type*]{lang="EN-US"}]{#struct_0_16293_x2703_199638472}

[[添加]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_16293_x2703_1643522878}[到]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1121147385}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tlv-name]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893151218}[：]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[名称，取值为]{lang="EN-US" style="font-family:宋体"}[Adding neighbor]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Adding address]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_1186541435}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，取值为空或]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1792076649}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tlv-type]{lang="EN-US"}*]{#struct_0_16293_x2703_x589807130}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型，取值为协议规定的值]{style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleting address *ip-address* from level-*level* LSPs, TLV: *tlv-type*]{lang="EN-US"}]{#struct_0_16293_x2703_956998465}

[[从]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1893085682}[中删除]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_54511166}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_991058223}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，取值为]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x480495245}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tlv-type]{lang="EN-US"}*]{#struct_0_16293_x2703_2081459189}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型，取值为协议规定的值]{style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: The remaining space of level-*level* fragment 0 LSP is shortage]{lang="EN-US"}]{#struct_0_16293_x2703_x1893282290}

[[往]{style="font-family:宋体"}[LSP 0]{lang="EN-US"}]{#struct_0_16293_x2703_x2041127676}[分片中添加]{style="font-family:宋体"}[TLV]{lang="EN-US"}[时，剩余空间不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1221293898}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x2137943574}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: ISIS(*process-id*) level-*level* LSP over flow]{lang="EN-US"}]{#struct_0_16293_x2703_x1893216754}

[[往]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_638725040}[分片中添加]{style="font-family:宋体"}[TLV]{lang="EN-US"}[时，所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分片空间已满]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1812702805}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1348195722}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: The remaining space of level-*level* fragment 0 LSP is shortage while adding area or protocol support]{lang="EN-US"}]{#struct_0_16293_x2703_1512039908}

[[往]{style="font-family:宋体"}[LSP 0]{lang="EN-US"}]{#struct_0_16293_x2703_x1892889074}[分片中添加区域地址或协议支持]{style="font-family:宋体"}[TLV]{lang="EN-US"}[时，剩余空间不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x762181035}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_983340380}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Rebuilding all level-*level* LSPs Start]{lang="EN-US"}]{#struct_0_16293_x2703_x1068849446}

[[开始]{style="font-family:宋体"}[rebuild]{lang="EN-US"}]{#struct_0_16293_x2703_x1892823538}[所有的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1163290566}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_2147308560}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Rebuilding all level-*level* LSPs End]{lang="EN-US"}]{#struct_0_16293_x2703_x1893413361}

[[结束]{style="font-family:宋体"}[rebuild]{lang="EN-US"}]{#struct_0_16293_x2703_983397043}[所有的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1514523637}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_404743399}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: MTU Change triggers rebuild]{lang="EN-US"}]{#struct_0_16293_x2703_x1893347825}

[[MTU]{lang="EN-US"}]{#struct_0_16293_x2703_x604895425}[变化触发]{style="font-family:宋体"}[rebuild]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1068644590}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Attempting to exceed Max Seq Num]{lang="EN-US"}]{#struct_0_16293_x2703_x1893544433}

[[生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1646584315}[时，序列号达到最大]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892357907}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Generating Level-*level* LSP \[*lsp-id*\], Seq *sequence-number*, Length *lsp-length*]{lang="EN-US"}]{#struct_0_16293_x2703_699197480}

[[生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1893478897}[结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1828301552}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1076865179}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893151217}[：生成]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sequence-number]{lang="EN-US"}*]{#struct_0_16293_x2703_427026548}[：生成]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[的序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-length]{lang="EN-US"}*]{#struct_0_16293_x2703_x1406632433}[：生成]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的长度]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: TLV Handle triggers rebuild]{lang="EN-US"}]{#struct_0_16293_x2703_x1893085681}

[[TLV]{lang="EN-US"}]{#struct_0_16293_x2703_457795693}[变化触发]{style="font-family:宋体"}[rebuild]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x608904609}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Added level-*level* area address *area-address*]{lang="EN-US"}]{#struct_0_16293_x2703_x1893282289}

[[往]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x118878911}[中添加区域地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1868658680}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893216753}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-address]{lang="EN-US"}*]{#struct_0_16293_x2703_235440513}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleted level-*level* area address *area-address*]{lang="EN-US"}]{#struct_0_16293_x2703_1952895504}

[[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1892889073}[中删除区域地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2666148}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x199551755}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-address]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892823537}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Added level-*level* protocol support *protocol-support*]{lang="EN-US"}]{#struct_0_16293_x2703_x46563015}

[[往]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1893413364}[中添加协议支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_223882156}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_581145341}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-support]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893347828}[：协议支持]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleted level-*level* protocol support *protocol-support*]{lang="EN-US"}]{#struct_0_16293_x2703_154619462}

[[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1893544436}[中删除协议支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x887069428}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1393169355}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-support]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893478900}[：协议支持]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Added level-*level* interface IP address: *ip-address/mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x94602572}

[[往]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1893151220}[中添加接口地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_830507683}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_54077096}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893085684}[：接口地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_861080220}[：接口地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleted level-*level* interface IP address: *ip-address/mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x1893282292}

[[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x878328262}[中删除接口地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1065639244}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893216756}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_x524074374}[：接口地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892889076}[：接口地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Added level-*level* neighbour: System *system-id* =\> Neighbour *source-id*]{lang="EN-US"}]{#struct_0_16293_x2703_400618379}

[[往]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1892823540}[中添加非伪节点到伪节点的邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1519848606}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893413363}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x179402371}[：非伪节点]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1093725114}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleted level-*level* neighbour: System *system-id* =\> Neighbour *source-id*]{lang="EN-US"}]{#struct_0_16293_x2703_x1893347827}

[[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_557903989}[中删除非伪节点到伪节点的邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893544435}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x483784901}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893478899}[：非伪节点]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1303866330}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Modified level-*level* neighbour: System *system-id* =\> Neighbour *source-id*]{lang="EN-US"}]{#struct_0_16293_x2703_x1893151219}

[[在]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x379542506}[中修改非伪节点到伪节点的邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893085683}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1620595107}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1893282291}[：非伪节点]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x475043735}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Added level-*level* pseudo neighbour: Pseudo *source-id* =\> Neighbour *system-id*]{lang="EN-US"}]{#struct_0_16293_x2703_x1893216755}

[[往]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x927358901}[中添加伪节点到非伪节点的邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892889075}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_803902906}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1892823539}[：非伪节点]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1565592789}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleted level-*level* pseudo neighbour: Pseudo *source-id* =\> Neighbour *system-id*]{lang="EN-US"}]{#struct_0_16293_x2703_x327329419}

[[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1571218837}[中删除伪节点到非伪节点的邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327263883}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1537367679}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327460491}[：非伪节点]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x353238689}[：伪节点]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Added level-*level* IP prefix: *ip-address/mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x327394955}

[[往]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_1545219728}[中添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327067275}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1595444182}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_x327001739}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x350194416}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Deleted level-*level* IP prefix: *ip-address/mask*]{lang="EN-US"}]{#struct_0_16293_x2703_x327198347}

[[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1979734615}[中删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327132811}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1206523380}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_x326805131}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x326739595}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: Modified level-*level* IP prefix: *ip-address/mask*]{lang="EN-US"}]{#struct_0_16293_x2703_1505499895}

[[在]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x327329418}[中修改]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1571284373}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x327263882}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_16293_x2703_1537302143}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_16293_x2703_x327460490}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[前缀地址掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: ]{lang="EN-US"}[Added level-*Level* router ID *router-id.*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862064620}

[[在]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_x1861868012}[中添加]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1861933548}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1862261228}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[router]{lang="EN-US"}[-]{lang="EN-US"}*]{#struct_0_16293_x2703_x1862326764}*[id]{lang="EN-US"}*[：]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[，点分十进制格式]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-ORG: ]{lang="EN-US"}[Deleted level-*Level* router ID*.*]{lang="EN-US"}]{#struct_0_16293_x2703_x1862130156}

[[在]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}]{#struct_0_16293_x2703_1875409218}[中添加]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1862195692}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1861474796}[：]{lang="EN-US" style="font-family:宋体"}[TLV DB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x353304225}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_x1814487106}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[7777.8888.1111]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/02]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8.8.8.8/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[5555.1111.1111]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8.8.8.5/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在同一个区域]{style="font-family:宋体"}[18]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[本地更新的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis self-originate-update]{lang="EN-US"}]{#struct_0_16293_x2703_x327394954}

[\<RouterA\> system-view]{lang="EN-US"}

[\[RouterA\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[RouterA-GigabitEthernet1/0/2\] ip address 8.8.8.7 24]{lang="EN-US"}

[\[RouterA-GigabitEthernet1/0/2\]]{lang="EN-US"}

[\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Deleted level-1 interface IP address: 8.8.8.8/255.255.255.0]{lang="EN-US"}

[\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Deleted level-2 interface IP address: 8.8.8.8/255.255.255.0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1545285264}*[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}[中删除接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*

[[\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_475981384}

[ISIS-1-ORG: Deleted level-1 IP prefix: 8.8.8.0/255.255.255.0]{lang="EN-US"}

[\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Deleted level-2 IP prefix: 8.8.8.0/255.255.255.0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x626347824}*[从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}[中删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}*

[[\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x407008135}

[ISIS-1-ORG: Added level-1 interface IP address: 8.8.8.7/255.255.255.0]{lang="EN-US"}

[\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Added level-2 interface IP address: 8.8.8.7/255.255.255.0]{lang="EN-US"}

[\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1226336937}*[在]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}[中添加接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*

[[ISIS-1-ORG: Deleting address 8.8.8.0/24 from level-1 LSPs, TLV: 128]{lang="EN-US"}]{#struct_0_16293_x2703_x327067274}

[\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Deleting address 8.8.8.0/24 from level-2 LSPs, TLV: 128]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1595378646}*[从]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}*

[[%Apr  8 16:26:27:283 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-1 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: DOWN.]{lang="EN-US"}]{#struct_0_16293_x2703_639611899}

[\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Deleted level-1 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111]{lang="EN-US"}

[%Apr  8 16:26:27:283 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-2 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: DOWN.]{lang="EN-US"}

[\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Deleted level-2 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x83651082}*[邻居]{style="font-family:宋体"}[down]{lang="EN-US"}[，从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}[中删除伪节点到非伪节点邻居]{style="font-family:宋体"}*

[[%Apr  8 16:26:27:392 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-2 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: UP.]{lang="EN-US"}]{#struct_0_16293_x2703_250929778}

[\*Apr  8 16:26:27:392 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Added level-2 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111]{lang="EN-US"}

[%Apr  8 16:26:27:392 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-1 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: UP.]{lang="EN-US"}

[\*Apr  8 16:26:27:392 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Added level-1 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x327001738}*[邻居]{style="font-family:宋体"}[up]{lang="EN-US"}[，从]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}[中添加伪节点到非伪节点邻居]{style="font-family:宋体"}*

[[\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x350259952}

[ISIS-1-ORG: Generating Level-2 LSP \[7777.8888.1111.01-00\], Seq 0x0000000a, Length 55]{lang="EN-US"}

[\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Generating Level-1 LSP \[7777.8888.1111.01-00\], Seq 0x0000000a, Length 55]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1719852513}*[生成伪节点]{style="font-family:宋体"}[LSP]{lang="EN-US"}*

[[\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_166769810}

[ISIS-1-ORG: Generating Level-2 LSP \[7777.8888.1111.00-00\], Seq 0x00000013, Length 54]{lang="EN-US"}

[\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Generating Level-1 LSP \[7777.8888.1111.00-00\], Seq 0x00000014, Length 54]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1348513457}*[生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}*

[[\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x327198346}

[ISIS-1-ORG: Added level-1 IP prefix: 8.8.8.0/255.255.255.0]{lang="EN-US"}

[\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Adding address 8.8.8.0/24 into level-1 LSPs, TLV: 128]{lang="EN-US"}

[\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Added level-2 IP prefix: 8.8.8.0/255.255.255.0]{lang="EN-US"}

[\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Adding address 8.8.8.0/24 into level-2 LSPs, TLV: 128]{lang="EN-US"}

[\*Apr  8 16:26:39:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1979669079}*[在]{style="font-family:宋体"}[TLV DB]{lang="EN-US"}[中添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀，在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}*

[[ISIS-1-ORG: Generating Level-2 LSP \[7777.8888.1111.00-00\], Seq 0x00000014, Length 68]{lang="EN-US"}]{#struct_0_16293_x2703_915556265}

[\*Apr  8 16:26:39:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-ORG: Generating Level-1 LSP \[7777.8888.1111.00-00\], Seq 0x00000015, Length 68]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1280399709}*[生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}*

::: {#-706552492 .myid}
[]{#_Toc404788109}[]{#struct_0_16293_x2703_1116620632}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis snp-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1791425312}

[**[debugging]{lang="EN-US"}**[ **isis** **snp-packet** \[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_135133580}

[**[undo]{lang="EN-US"}**[ **debugging** **isis** **snp-packet** \[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x327132810}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1206457844}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_500492790}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_388657072}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1804374185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1121992174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x808111395}

[**[receive]{lang="EN-US"}**]{#struct_0_16293_x2703_1747805555}[：表示接收]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_16293_x2703_x326805130}[：表示发送]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16293_x2703_x1929993204}[：表示]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文详细调试信息开关。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1718688454}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1787937164}

[**[debugging isis snp-packet]{lang="EN-US"}**]{#struct_0_16293_x2703_205771809}[命令用来打开]{style="font-family:
宋体"}[IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:
宋体"}**[undo debugging isis snp-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS SNP]{lang="EN-US"}]{#struct_0_16293_x2703_2136456512}[报文的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x1299570711}[进程的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging isis snp-packet]{lang="EN-US"}]{#struct_0_16293_x2703_x593215223}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x455269612}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x326739594}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_1505565431}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Receive *psnp-type* from *system-id* on circuit *circuit-name*]{lang="EN-US"}]{#struct_0_16293_x2703_1816095310}

[[收到]{style="font-family:宋体"}[PSNP]{lang="EN-US"}]{#struct_0_16293_x2703_103703285}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_455409236}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[psnp-type]{lang="EN-US"}*]{#struct_0_16293_x2703_1005070037}[：]{lang="EN-US" style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1 PSNP]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2 PSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327329421}[：发送]{lang="EN-US" style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_x1571743124}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Receive *csnp-type* from *source-id* on circuit *circuit-name* range from *start-lsp-id* to *end-lsp-id*]{lang="EN-US"}]{#struct_0_16293_x2703_448153179}

[[收到]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1785080028}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1992607695}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[csnp-type]{lang="EN-US"}*]{#struct_0_16293_x2703_x327263885}[：]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1 CSNP]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2 CSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1537760895}[：发送]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{lang="EN-US" style="font-family:宋体"}[SOURCE ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_x1184557888}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[start-lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1427456271}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[摘要的起始]{lang="EN-US" style="font-family:
  宋体"}[LSP ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[end-lsp-id]{lang="DA"}*]{#struct_0_16293_x2703_x1064351197}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="DA"}[摘要的结束]{lang="EN-US" style="font-family:宋体"}[LSP ID]{lang="DA"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Not find current lsp entry to build csnp]{lang="EN-US"}]{#struct_0_16293_x2703_x327460493}

[[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_16293_x2703_x353369761}[报文时，在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中没有找到起始]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[或第一个比起始]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[大的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_863511147}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Circuit(*circuit-name*) silence, csnp NOT sent]{lang="EN-US"}]{#struct_0_16293_x2703_x597640658}

[[接口配置]{style="font-family:宋体"}[silent]{lang="EN-US"}]{#struct_0_16293_x2703_x1029036437}[，不发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327394957}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_1545088656}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Level-*level* csnp timer expired on a NOT dis circuit(*circuit-name*)]{lang="EN-US"}]{#struct_0_16293_x2703_1193470130}

[[CSNP]{lang="EN-US"}]{#struct_0_16293_x2703_1805408298}[定时器在非]{style="font-family:宋体"}[DIS]{lang="EN-US"}[接口上超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327067277}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_1595313110}[：接口的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_x2099643651}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Send *snp-type* on circuit *circuit-name*]{lang="EN-US"}]{#struct_0_16293_x2703_x346338749}

[[发送]{style="font-family:宋体"}[CSNP/PSNP]{lang="EN-US"}]{#struct_0_16293_x2703_x327001741}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x349670133}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[snp-type]{lang="EN-US"}*]{#struct_0_16293_x2703_x1617817203}[：]{lang="EN-US" style="font-family:宋体"}[SNP]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1 CSNP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L2 CSNP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L1 PSNP]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2 PSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_230840166}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:]{lang="EN-US"}[Circuit(*circuit-name*) silence, psnp NOT sent]{lang="EN-US"}]{#struct_0_16293_x2703_x327198349}

[[接口配置]{style="font-family:宋体"}[silent]{lang="EN-US"}]{#struct_0_16293_x2703_x1979865687}[，不发送]{style="font-family:宋体"}[PSNP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1346526829}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_x1385789553}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Level- *level* psnp timer expired on a dis circuit(*circuit-name*)]{lang="EN-US"}]{#struct_0_16293_x2703_x327132813}

[[PSNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1206392308}[定时器在]{style="font-family:宋体"}[DIS]{lang="EN-US"}[接口上超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x331338349}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[level]{lang="EN-US"}*]{#struct_0_16293_x2703_x702642418}[：接口的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}[，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuit-name]{lang="EN-US"}*]{#struct_0_16293_x2703_x326805133}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Lsp entry *lsp-id* processed, newer than lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x1929796596}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_126996079}[摘要比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的新]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x326739597}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1505630967}[：收到的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Lsp entry *lsp-id* processed, older than lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_703341473}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x327329420}[摘要比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的旧]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1571808660}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_729954476}[：收到的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Lsp entry *lsp-id* processed, same as lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x327263884}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_1537695359}[摘要和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的新旧程度一样]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1934373426}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_929123187}[：收到的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Lsp entry *lsp-id* processed, NO exist in lsdb]{lang="EN-US"}]{#struct_0_16293_x2703_x327460492}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x353435297}[摘要在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中不存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x259609719}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327394956}[：收到的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Psnp not processed before DIS election]{lang="EN-US"}]{#struct_0_16293_x2703_1545154192}

[[在]{style="font-family:宋体"}[DIS]{lang="EN-US"}]{#struct_0_16293_x2703_x652644031}[选举完成之前不处理收到的]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process-id]{lang="EN-US"}]{#struct_0_16293_x2703_x327067276}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Psnp not processed, current IS is NOT DIS]{lang="EN-US"}]{#struct_0_16293_x2703_1595247574}

[[当前的]{style="font-family:宋体"}[IS]{lang="EN-US"}]{#struct_0_16293_x2703_x327001740}[不是]{style="font-family:宋体"}[DIS]{lang="EN-US"}[时不处理收到的]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process-id]{lang="EN-US"}]{#struct_0_16293_x2703_x349735669}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Csnp not processed before DIS election]{lang="EN-US"}]{#struct_0_16293_x2703_733524894}

[[在]{style="font-family:宋体"}[DIS]{lang="EN-US"}]{#struct_0_16293_x2703_x327198348}[选举完成之前不处理收到的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process-id]{lang="EN-US"}]{#struct_0_16293_x2703_x1979800151}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Csnp not processed on DIS]{lang="EN-US"}]{#struct_0_16293_x2703_x1104271812}

[[DIS]{lang="EN-US"}]{#struct_0_16293_x2703_x327132812}[不处理收到的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process-id]{lang="EN-US"}]{#struct_0_16293_x2703_x1206326772}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP:Lsp entry *lsp-id* in csnp is not found in lsdb]{lang="EN-US"}]{#struct_0_16293_x2703_x326805132}

[[收到]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1929862132}[报文中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中不存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1782025224}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsp-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x326739596}[：收到的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[process-id]{lang="EN-US"}*[-SNP: *snp-content*]{lang="EN-US"}]{#struct_0_16293_x2703_1505696503}

[[SNP]{lang="EN-US"}]{#struct_0_16293_x2703_x153809699}[报文的内容]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327329423}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[snp-content]{lang="EN-US"}*]{#struct_0_16293_x2703_x1571874196}[：]{lang="EN-US" style="font-family:
  宋体"}[SNP]{lang="EN-US"}[报文内容]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_717307488}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_x327263887}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[7777.8888.1111]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8.8.8.8/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[5555.1111.1111]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8.8.8.5/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在同一个区域]{style="font-family:宋体"}[18]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis snp-packet]{lang="EN-US"}]{#struct_0_16293_x2703_1537629823}

[\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-SNP:]{lang="EN-US"}

[0000: 83 21 01 06  18 01 00 00  00 63 55 55  11 11 11 11]{lang="EN-US"}

[0010: 00 00 00 00  00 00 00 00  00 ff ff ff  ff ff ff ff]{lang="EN-US"}

[0020: ff 09 40 04  a8 55 55 11  11 11 11 00  00 00 00 00]{lang="EN-US"}

[0030: 05 ff 6e 04  6b 55 55 11  11 11 11 00  01 00 00 00]{lang="EN-US"}

[0040: 01 49 95 04  a6 55 55 11  11 11 11 01  00 00 00 00]{lang="EN-US"}

[0050: 03 d8 b4 04  a7 77 77 88  88 11 11 00  00 00 00 00]{lang="EN-US"}

[0060: 05 f0 47]{lang="EN-US"}

[*[// SNP]{lang="EN-US"}*]{#struct_0_16293_x2703_729498899}*[报文内容]{style="font-family:宋体"}*

[[\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x156787919}

[ISIS-1-SNP: Receive L1 CSNP from 5555.1111.1111.00 on circuit GigabitEthernet1/0/2 range from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x342310288}*[收到]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x327460495}

[ISIS-1-SNP: Lsp entry 5555.1111.1111.00-00 processed, same as lsdb copy]{lang="EN-US"}

[\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[*[// CSNP]{lang="EN-US"}*]{#struct_0_16293_x2703_x352976545}*[报文上的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的新旧程度一样]{style="font-family:宋体"}*

[[ISIS-1-SNP: Lsp entry 5555.1111.1111.00-01 processed, NO exist in lsdb]{lang="EN-US"}]{#struct_0_16293_x2703_x1807141048}

[\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[*[// CSNP]{lang="EN-US"}*]{#struct_0_16293_x2703_510414530}*[报文上的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中不存在]{style="font-family:宋体"}*

[[ISIS-1-SNP: Lsp entry 5555.1111.1111.01-00 processed, same as lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x1810605618}

[\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-SNP: Lsp entry 7777.8888.1111.00-00 processed, same as lsdb copy]{lang="EN-US"}

[\*Apr  8 16:51:24:151 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-SNP: Send L1 PSNP on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1599834243}*[发送]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#-1697392765 .myid}
[]{#_Toc404788110}[]{#struct_0_16293_x2703_1546352123}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis spf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x327394959}

[**[debugging]{lang="EN-US"}**[ **isis** **spf** \[ **pic** \| **verbose** \] \[ *process-id* \[ **ipv4** \[ **topology** *topo-name* \] \| **ipv6** \] \]]{lang="EN-US"}]{#struct_0_16293_x2703_1544957584}

[**[undo]{lang="EN-US"}**[ **debugging** **spf** \[ **pic** \| **verbose**\] \[ *process-id* \[ **ipv4** \[ **topology** *topo-name* \] \| **ipv6** \] \]]{lang="EN-US"}]{#struct_0_16293_x2703_1276574639}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x257030449}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_875622817}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1248336972}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_379650895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x327067279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1594657750}

[**[pic]{lang="EN-US"}**]{#struct_0_16293_x2703_x1862261226}[：表]{style="font-family:宋体"}[示]{style="font-family:宋体"}[前缀无关收敛]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16293_x2703_215272706}[：表示路由计算详细调试信息开关。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1669273542}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_16293_x2703_x1862326762}[：打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_16293_x2703_2097965677}[：打开指定拓扑的路由计算调试信息开关。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则表示打开公网的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_16293_x2703_x958355283}[：打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x215670343}

[**[debugging isis]{lang="EN-US"}**[ **spf**]{lang="EN-US"}]{#struct_0_16293_x2703_x27143453}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}**[undo debugging isis]{lang="EN-US"}**[ **spf**]{lang="EN-US"}[命令用来关闭]{style="font-family:
宋体"}[IS-IS]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x221588244}[路由计算调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_535012885}[进程的路由计算调试信息开关。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging isis spf]{lang="EN-US"}]{#struct_0_16293_x2703_x327001743}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x461238792}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x349539061}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x497800540}

[[ISIS- ]{lang="EN-US"}*[process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Trigger SPF at  Sec =]{lang="EN-US"}*[ xxx]{lang="EN-US"}*[, MSec =]{lang="EN-US"}[ *yyy*]{lang="EN-US"}]{#struct_0_16293_x2703_1511270053}

[[触发路由计算时间]{style="font-family:宋体"}]{#struct_0_16293_x2703_1053689195}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_812209427}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x327198351}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_16293_x2703_x1979341398}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_16293_x2703_139512889}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) SPF old scheduled event: ]{lang="EN-US"}*[triggerType]{lang="EN-US"}*[, new trigger event: ]{lang="EN-US"}*[triggerType]{lang="EN-US"}*]{#struct_0_16293_x2703_x1908231249}

[[开始新的触发，显示旧的和新的触发类型]{style="font-family:宋体"}]{#struct_0_16293_x2703_1018482232}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327132815}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[topoId]{lang="EN-US"}]{#struct_0_16293_x2703_x1206785524}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[triggerType]{lang="EN-US"}*]{#struct_0_16293_x2703_123149050}[，触发类型，包括：全部路由计算、]{style="font-family:宋体"}[ISPF]{lang="EN-US"}[拓扑变化、区域地址变化、增量]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀计算、全部]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀计算、停止计算]{style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Total IPv4 route number less then maximum, SPF will be resche]{lang="EN-US"}]{#struct_0_16293_x2703_x2004151145}

[[dule.  ]{lang="EN-US"}]{#struct_0_16293_x2703_x326805135}

[[需要进行路由前缀超规格恢复计算]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1929665524}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x667519686}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_989917423}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) SPF node Create root node ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[ Dist:]{lang="EN-US"}*[ distanceValue]{lang="EN-US"}*[ Nextho]{lang="EN-US"}]{#struct_0_16293_x2703_103958785}

[[ps: ]{lang="EN-US"}*[nexthopNum]{lang="EN-US"}*[ Nbrs:]{lang="EN-US"}*[ nbrNum]{lang="EN-US"}*[ Parents:]{lang="EN-US"}*[ parentNum]{lang="EN-US"}*[ Tree]{lang="EN-US"}]{#struct_0_16293_x2703_x326739599}

[[创建根节点]{style="font-family:宋体"}[SPFNODE]{lang="EN-US"}]{#struct_0_16293_x2703_1506286327}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x672461473}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_565284330}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x327329422}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1571939732}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[distanceValue]{lang="EN-US"}*]{#struct_0_16293_x2703_998584498}[：到达根结点的]{lang="EN-US" style="font-family:
  宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum]{lang="EN-US"}*]{#struct_0_16293_x2703_2066114662}[：节点的下一跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x327263886}[：节点的邻居数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1537564287}[：父节点数]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: SPF node (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Adding system ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1126743533}

[[创建]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_535777988}[节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x327460494}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x353042081}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x260962201}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x327394958}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="DA"}]{#struct_0_16293_x2703_1545023120}*[ process-id]{lang="DA"}*[ -SPF: SPF node (MT ]{lang="DA"}*[topoId]{lang="DA"}*[)(L ]{lang="DA"}*[sysLevel]{lang="DA"}*[) Deleting system ]{lang="DA"}*[sourceId]{lang="EN-US"}*[  ]{lang="DA"}

[[删除]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1054027972}[SPF]{lang="DA"}[节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="DA"}*]{#struct_0_16293_x2703_x575148939}*[：]{lang="EN-US" style="font-family:宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="DA"}*]{#struct_0_16293_x2703_x327067278}[：]{lang="EN-US" style="font-family:宋体"}[拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="DA"}*]{#struct_0_16293_x2703_1594592214}[：]{lang="EN-US" style="font-family:宋体"}[系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="DA"}*]{#struct_0_16293_x2703_1786080978}[：]{lang="EN-US" style="font-family:宋体"}[源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="DA"}

[[ISIS-]{lang="DA"}]{#struct_0_16293_x2703_x327001742}*[ process-id]{lang="DA"}*[ -SPF: SPF node (MT ]{lang="DA"}*[topoId]{lang="DA"}*[)(L ]{lang="DA"}*[sysLevel]{lang="DA"}*[) Updating system ]{lang="DA"}*[sourceId]{lang="EN-US"}*[  ]{lang="EN-US"}[Overload]{lang="DA"}

[[更新]{style="font-family:宋体"}]{#struct_0_16293_x2703_x349604597}[SPF]{lang="DA"}[节点状态为]{style="font-family:宋体"}[Overload]{lang="DA"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x410697941}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x327198350}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1979275862}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x937897489}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="DA"}]{#struct_0_16293_x2703_x327132814}*[ process-id]{lang="DA"}*[ -SPF: SPF node (MT ]{lang="DA"}*[topoId]{lang="DA"}*[)(L ]{lang="DA"}*[sysLevel]{lang="DA"}*[) Updating system ]{lang="DA"}*[sourceId]{lang="EN-US"}*

[[更新]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1206719988}[SPF]{lang="DA"}[节点状态从]{style="font-family:宋体"}[Overload]{lang="DA"}[中恢复]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2123221131}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x326805134}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1929731060}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_40298378}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) SPF node Set DIRECT flag on node. ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[  Dist:]{lang="EN-US"}]{#struct_0_16293_x2703_x326739598}

[*[distanceValue]{lang="EN-US"}*[ Nexthops:]{lang="EN-US"}*[ nexthopNum]{lang="EN-US"}*[ Nbrs:]{lang="EN-US"}*[ nbrNum]{lang="EN-US"}*[ Parents:]{lang="EN-US"}*[ parentNum]{lang="EN-US"}*[ Direct]{lang="EN-US"}]{#struct_0_16293_x2703_1506351863}

[[设置节点]{style="font-family:宋体"}[Direct]{lang="EN-US"}]{#struct_0_16293_x2703_964532393}[标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1594984882}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x169399815}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_166785191}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595050418}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[distanceValue]{lang="EN-US"}*]{#struct_0_16293_x2703_608524461}[：到达根结点的]{lang="EN-US" style="font-family:
  宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x1800786920}[：节点的下一跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1594853810}[：节点的邻居数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x2065696300}[：父节点数]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: SPF link (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Adding link ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[ \--\> ]{lang="EN-US"}*[destId]{lang="EN-US"}*[  Cost:*Cost*   ]{lang="EN-US"}]{#struct_0_16293_x2703_x367885919}

[[创建广播网]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16293_x2703_1594919346}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2077213162}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595247026}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1715221113}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x955814259}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[destId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595312562}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Cost]{lang="EN-US"}*]{#struct_0_16293_x2703_1394044827}[：]{style="font-family:宋体"}[路径开销值]{style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: SPF link (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Deleting link ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[ \--\> ]{lang="EN-US"}*[destId]{lang="EN-US"}*[  Cost:*Cost*]{lang="EN-US"}]{#struct_0_16293_x2703_1595115954}

[[删除广播网]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16293_x2703_x140855711}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_259961856}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595181490}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x2145721367}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595509170}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[destId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1286717805}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Cost]{lang="EN-US"}*]{#struct_0_16293_x2703_1595574706}[：]{style="font-family:宋体"}[路径开销值]{style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: SPF link (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Updating link ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[ \--\> ]{lang="EN-US"}*[destId]{lang="EN-US"}*[  Cost:*Cost*]{lang="EN-US"}]{#struct_0_16293_x2703_982788725}

[[更新广播网]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16293_x2703_x1835737640}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1594984883}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x169334279}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1595050419}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_608458925}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[destId]{lang="EN-US"}*]{#struct_0_16293_x2703_219228390}[：目的系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Cost]{lang="EN-US"}*]{#struct_0_16293_x2703_1594853811}[：]{style="font-family:宋体"}[路径开销值]{style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) I-SPF run started at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_x2065761836}

[[ISPF]{lang="EN-US"}]{#struct_0_16293_x2703_1594919347}[路由计算开始时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2077278698}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595247027}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1715155577}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_16293_x2703_1595312563}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_16293_x2703_1393979291}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: Checking changed links.]{lang="EN-US"}]{#struct_0_16293_x2703_1595115955}

[[处理变化]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16293_x2703_x140921247}[，决定是否需要重构]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1030915658}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: Need rebuild SPT.  ]{lang="EN-US"}]{#struct_0_16293_x2703_1595181491}

[[需要重构]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_x2145655831}[树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1595509171}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: Processing links with change flags.]{lang="EN-US"}]{#struct_0_16293_x2703_x1286652269}

[[无需重构]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_1595574707}[树，仅处理协议使用、下一跳变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_982723189}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Running full SPF.]{lang="EN-US"}]{#struct_0_16293_x2703_1594984880}

[[开始全部]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_x169268743}[计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1595050416}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_609441965}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1594853808}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Begin Level-]{lang="EN-US"}*[ sysLevel]{lang="EN-US"}*[ SPF from root node.]{lang="EN-US"}]{#struct_0_16293_x2703_x2066220589}

[[从根节点开始进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_1594919344}[计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2077344234}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595247024}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1715090041}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) SPF node Node is added into SPT. ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[ Dist:]{lang="EN-US"}*[ distanceValue]{lang="EN-US"}*[ Nexthops:]{lang="EN-US"}*[ nexthopNum]{lang="EN-US"}*[ Nbrs:]{lang="EN-US"}*[ nbrNum]{lang="EN-US"}*[ Parents:]{lang="EN-US"}*[ parentNum]{lang="EN-US"}*[ Tree  ]{lang="EN-US"}]{#struct_0_16293_x2703_1595312560}

[[把]{style="font-family:宋体"}[TentList]{lang="EN-US"}]{#struct_0_16293_x2703_1393913755}[中的节点加入到]{style="font-family:宋体"}[SPT]{lang="EN-US"}[树中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1595115952}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x140462495}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1595181488}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x2146245654}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[distanceValue]{lang="EN-US"}*]{#struct_0_16293_x2703_1595509168}[：到达根结点的]{lang="EN-US" style="font-family:
  宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x1286193516}[：节点的下一跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1595574704}[：节点的邻居数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1594984881}[：父节点数]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF:  New distance is ]{lang="EN-US"}*[distanceValue]{lang="EN-US"}*[.  ]{lang="EN-US"}]{#struct_0_16293_x2703_x169203207}

[[到根结点的新]{style="font-family:宋体"}[Distance]{lang="EN-US"}]{#struct_0_16293_x2703_1595050417}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_609376429}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[distanceValue]{lang="EN-US"}*]{#struct_0_16293_x2703_1594853809}[：到达根结点的]{lang="EN-US" style="font-family:
  宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF:  Less cost, add node to TENT HEAP.]{lang="EN-US"}]{#struct_0_16293_x2703_x2066286125}

[[子结点到根结点的]{style="font-family:宋体"}[Distance]{lang="EN-US"}]{#struct_0_16293_x2703_1594919345}[小]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2077409770}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF:  Equal cost, add node to TENT HEAP.]{lang="EN-US"}]{#struct_0_16293_x2703_1595247025}

[[子结点到根结点的]{style="font-family:宋体"}[Distance]{lang="EN-US"}]{#struct_0_16293_x2703_1595312561}[相同]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1393848219}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) SPF node Son node update to TENT list ]{lang="EN-US"}*[sourceId]{lang="EN-US"}*[ D]{lang="EN-US"}]{#struct_0_16293_x2703_1595115953}

[[ist:]{lang="EN-US"}*[ distanceValue]{lang="EN-US"}*[ Nexthops:]{lang="EN-US"}*[ nexthopNum]{lang="EN-US"}*[ Nbrs:]{lang="EN-US"}*[ nbrNum]{lang="EN-US"}*[ Parents:]{lang="EN-US"}*[ parentNum]{lang="EN-US"}*[ Tent Direct]{lang="EN-US"}]{#struct_0_16293_x2703_x140528031}

[[把节点加入到]{style="font-family:宋体"}[TentList]{lang="EN-US"}]{#struct_0_16293_x2703_1595181489}[中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1595509169}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1286127980}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1595574705}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_982854261}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[distanceValue]{lang="EN-US"}*]{#struct_0_16293_x2703_1594984878}[：到达根结点的]{lang="EN-US" style="font-family:
  宋体"}[cost]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x169793034}[：节点的下一跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbrNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1595050414}[：节点的邻居数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parentNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1594853806}[：父节点数]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: Link is backard link, ignore.]{lang="EN-US"}]{#struct_0_16293_x2703_x2065303085}

[[忽略回指]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16293_x2703_1594919342}[的处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2076951018}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: Node is Overload. Ignore its nbrs.]{lang="EN-US"}]{#struct_0_16293_x2703_1595247022}

[[当前节点]{style="font-family:宋体"}[Overload]{lang="EN-US"}]{#struct_0_16293_x2703_1595312558}[，则忽略其邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1394438044}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Merge nexthop from root node IPV4:]{lang="EN-US"}*[ nexthopNum1 ]{lang="EN-US"}*[/]{lang="EN-US"}*[ nexthopNum2]{lang="EN-US"}*]{#struct_0_16293_x2703_1595115950}

[[从根节点上继承下一跳]{style="font-family:宋体"}]{#struct_0_16293_x2703_1595181486}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x2146114582}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595509166}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum1]{lang="EN-US"}*]{#struct_0_16293_x2703_x1287111020}[：根节点下]{lang="EN-US" style="font-family:
  宋体"}[Link]{lang="EN-US"}[上的下一跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum2]{lang="EN-US"}*]{#struct_0_16293_x2703_1595574702}[：子节点上的下一跳数]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Merge nexthop from parent node IPV4:]{lang="EN-US"}*[ nexthopNum]{lang="EN-US"}*]{#struct_0_16293_x2703_1594984879}

[[从父节点上继承下一跳]{style="font-family:宋体"}]{#struct_0_16293_x2703_x169727498}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1595050415}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1594853807}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthopNum]{lang="EN-US"}*]{#struct_0_16293_x2703_x2065368621}[：父节点上的下一跳数]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: Inform SPF nodes change to PAC&PRC.]{lang="EN-US"}]{#struct_0_16293_x2703_1594919343}

[[处理]{style="font-family:宋体"}[SpfNode]{lang="EN-US"}]{#struct_0_16293_x2703_1595247023}[节点变化提交]{style="font-family:宋体"}[PAC]{lang="EN-US"}[和]{style="font-family:宋体"}[PRC]{lang="EN-US"}[处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1715417721}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) I-SPF run ended at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_1595312559}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISPF]{lang="EN-US"}]{#struct_0_16293_x2703_1595115951}[路由计算结束时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x140659103}*[：]{lang="EN-US" style="font-family:
  宋体"}*[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1595181487}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1595509167}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_16293_x2703_x1287045484}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_16293_x2703_1595574703}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: AREA: Updating (L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) areas:                                         ]{lang="EN-US"}]{#struct_0_16293_x2703_x1133898473}

[[          New areas: \[]{lang="EN-US"}*[newareaAddress]{lang="EN-US"}*[\]\[ ]{lang="EN-US"}*[newareaAddress]{lang="EN-US"}*[\] \[]{lang="EN-US"}*[newareaAddress]{lang="EN-US"}*[\].                                                           ]{lang="EN-US"}]{#struct_0_16293_x2703_x1133832937}

[[          Old areas:\[ ]{lang="EN-US"}*[oldareaAddress]{lang="EN-US"}*[\]\[ ]{lang="EN-US"}*[oldareaAddress]{lang="EN-US"}*[\] \[]{lang="EN-US"}*[oldareaAddress]{lang="EN-US"}*[\].]{lang="EN-US"}]{#struct_0_16293_x2703_2006985280}

[[更新区域地址，显示旧的和新的区域地址信息]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1134029545}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133964009}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1580435078}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[newareaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133636329}[：新区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[oldareaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133570793}[：旧区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Install one area: ]{lang="EN-US"}*[areaAddress]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133767401}

[[加入一个新的区域地址]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1943655582}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133701865}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133374185}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133308649}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Remove one area: ]{lang="EN-US"}*[areaAddress]{lang="EN-US"}*[.  ]{lang="EN-US"}]{#struct_0_16293_x2703_x91176890}

[[删除一个区域地址]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1133898472}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133832936}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1134029544}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x788675377}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) AREA run started at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133964008}

[[区域地址计算开始时间]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1133636328}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process-id]{lang="EN-US"}]{#struct_0_16293_x2703_x1133570792}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[topoId]{lang="EN-US"}]{#struct_0_16293_x2703_1580657753}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sysLevel]{lang="EN-US"}]{#struct_0_16293_x2703_x1133767400}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[xxx]{lang="EN-US"}]{#struct_0_16293_x2703_x1133701864}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[yyy]{lang="EN-US"}]{#struct_0_16293_x2703_x1133374184}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Processing increment area address calculating.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133308648}

[[处理区域地址变化]{style="font-family:宋体"}]{#struct_0_16293_x2703_1474907051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133898475}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133832939}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1134029547}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Area Addr: ]{lang="EN-US"}*[areaAddress]{lang="EN-US"}*[ is available.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133964011}

[[区域地址有效]{style="font-family:宋体"}]{#struct_0_16293_x2703_1936599902}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133636331}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133570795}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133767403}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133701867}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Area Addr: ]{lang="EN-US"}*[areaAddress]{lang="EN-US"}*[ is available.]{lang="EN-US"}]{#struct_0_16293_x2703_x587374642}

[[区域地址无效]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1133374187}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133308651}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133898474}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133832938}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1134029546}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Updating computed areas into L2 LSDB.]{lang="EN-US"}]{#struct_0_16293_x2703_374124037}

[[往]{style="font-family:宋体"}[L2]{lang="EN-US"}]{#struct_0_16293_x2703_x1133964010}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中更新区域地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133636330}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133570794}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Attach bit is set in running SPF.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133767402}

[[区域地址计算中设置]{style="font-family:宋体"}[ATT]{lang="EN-US"}]{#struct_0_16293_x2703_x1133701866}[位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133374186}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1268508185}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Attach bit is cleared in running SPF.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133308650}

[[区域地址计算中清除]{style="font-family:宋体"}[ATT]{lang="EN-US"}]{#struct_0_16293_x2703_x1133898477}[位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133832941}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1134029549}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Area Addr: ]{lang="EN-US"}*[areaAddress]{lang="EN-US"}*[ is adevertised to L2.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133964013}

[[区域地址在]{style="font-family:宋体"}[L2LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1133636333}[中的发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133570797}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_821142866}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133767405}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) Area Addr: ]{lang="EN-US"}*[areaAddress]{lang="EN-US"}*[ is not adevertised to L2.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133701869}

[[区域地址撤销在]{style="font-family:宋体"}[L2LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1133374189}[中的发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133308653}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133898476}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133832940}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) AREA run ended at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_x1134029548}

[[区域地址计算结束时间]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1133964012}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1133636332}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[topoId]{lang="EN-US"}]{#struct_0_16293_x2703_1887947881}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sysLevel]{lang="EN-US"}]{#struct_0_16293_x2703_x1133570796}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[xxx]{lang="EN-US"}]{#struct_0_16293_x2703_x1133767404}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[yyy]{lang="EN-US"}]{#struct_0_16293_x2703_x1133701868}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Adding prefix for ]{lang="EN-US"}*[ipPrefix]{lang="EN-US"}*[ / *subMask* from *sourceId*, into forwarding table.]{lang="EN-US"}]{#struct_0_16293_x2703_x1133374188}

[[往]{style="font-family:宋体"}[ISIS L1/L2]{lang="EN-US"}]{#struct_0_16293_x2703_x1133308652}[路由表中加入当前节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245373658}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245308122}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245242586}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_1245177050}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subMask]{lang="EN-US"}*]{#struct_0_16293_x2703_1245111514}[：子网掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245045978}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Deleting prefix for ]{lang="EN-US"}*[ipPrefix]{lang="EN-US"}*[ / *subMask*, from forw]{lang="EN-US"}]{#struct_0_16293_x2703_1244980442}

[[arding table.  ]{lang="EN-US"}]{#struct_0_16293_x2703_1244914906}

[[从]{style="font-family:宋体"}[ISIS L1/L2]{lang="EN-US"}]{#struct_0_16293_x2703_1245897946}[路由表中删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245832410}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x329098857}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245373659}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_1245308123}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subMask]{lang="EN-US"}*]{#struct_0_16293_x2703_1245242587}[：子网掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Modifying prefix for ]{lang="EN-US"}*[ipPrefix]{lang="EN-US"}*[ / *subMask*, in forw]{lang="EN-US"}]{#struct_0_16293_x2703_1245177051}

[[arding table.]{lang="EN-US"}]{#struct_0_16293_x2703_1245111515}

[[往]{style="font-family:宋体"}[ISIS]{lang="EN-US"}]{#struct_0_16293_x2703_1245045979}[路由表中更改]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1244980443}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1244914907}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245897947}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_1245832411}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subMask]{lang="EN-US"}*]{#struct_0_16293_x2703_1245373656}[：子网掩码]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) PRC run started at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_1245308120}

[[PRC]{lang="EN-US"}]{#struct_0_16293_x2703_1245242584}[计算开始时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245177048}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245111512}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245045976}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_16293_x2703_1244980440}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_16293_x2703_1244914904}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Processing increment IPV4 prefix calculating.]{lang="EN-US"}]{#struct_0_16293_x2703_1245897944}

[[计算变化的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16293_x2703_1245832408}[路由前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245373657}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245308121}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245242585}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Processing full ipv4 prefix calculating.]{lang="EN-US"}]{#struct_0_16293_x2703_1245111513}

[[处理]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16293_x2703_1245045977}[路由前缀变化链表，计算全部]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1244980441}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1244914905}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245897945}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) PRC run ended at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_1245832409}

[[PRC]{lang="EN-US"}]{#struct_0_16293_x2703_1245373654}[计算结束时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245308118}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245242582}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1245177046}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_16293_x2703_1245111510}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_16293_x2703_1245045974}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[) All phases of SPF work completed at  Sec = ]{lang="EN-US"}*[xxx]{lang="EN-US"}*[, MSec = ]{lang="EN-US"}*[yyy]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_16293_x2703_1244980438}

[[路由计算所有阶段全部完成时间]{style="font-family:宋体"}]{#struct_0_16293_x2703_1244914902}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245897942}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245832406}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[xxx]{lang="EN-US"}*]{#struct_0_16293_x2703_1245373655}[：秒值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[yyy]{lang="EN-US"}*]{#struct_0_16293_x2703_1245308119}[：毫秒值]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Exceeded SPF slice time while processing IPV4 PRC.]{lang="EN-US"}]{#struct_0_16293_x2703_1245242583}

[[处理]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16293_x2703_1245177047}[前缀路由计算时超过了]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算分片时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1245111511}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_1245045975}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1244914903}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Number of IPV4 routes exceed limit!]{lang="EN-US"}]{#struct_0_16293_x2703_1245897943}

[[路由条数超过规格限制]{style="font-family:宋体"}]{#struct_0_16293_x2703_1245832407}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483509697}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483575233}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483640769}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Processing full prefix calculating.]{lang="EN-US"}]{#struct_0_16293_x2703_x1483706305}

[[处理全部前缀计算]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1483771841}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483902913}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483968449}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1482985409}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="EN-US"}*[ process-id]{lang="EN-US"}*[ -SPF: (MT ]{lang="EN-US"}*[topoId]{lang="EN-US"}*[)(L ]{lang="EN-US"}*[sysLevel]{lang="EN-US"}*[) Exceeded SPF slice time when full processing prefix calculating]{lang="EN-US"}]{#struct_0_16293_x2703_x1483050945}

[[处理全部前缀计算时间到达限制]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1483509696}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483575232}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483640768}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483771840}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[ISIS- *process-id* -SPF: (MT *topoId*) Sync route\[*acction*\] *ipPrefix* / *subMask*  to rib]{lang="EN-US"}]{#struct_0_16293_x2703_x1483837376}

[[同步路由到路由表]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1483902912}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483968448}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[action]{lang="EN-US"}*]{#struct_0_16293_x2703_x1482985408}[：添加，删除或修改路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483050944}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subMask]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483575235}[：子网掩码]{lang="EN-US" style="font-family:宋体"}

[[(MT *topoId*)(L *sysLevel*) Deleted route *ipPrefix* / *subMask*  PIC backup flag in source *sourceId*.]{lang="EN-US"}]{#struct_0_16293_x2703_2029356004}

[[删除]{style="font-family:宋体"}[PIC]{lang="EN-US"}]{#struct_0_16293_x2703_2029552612}[备份标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029487076}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_2030207972}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_2030142436}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subMask]{lang="EN-US"}*]{#struct_0_16293_x2703_2029683685}[：子网掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029814757}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[(MT *topoId*)(L *sysLevel*) Deleted PIC backup flag in source *sourceId* while route *ipPrefix* / *subMask* was deactivated.]{lang="EN-US"}]{#struct_0_16293_x2703_2029749221}

[[当原路由无效时，删除]{style="font-family:宋体"}[PIC]{lang="EN-US"}]{#struct_0_16293_x2703_2029421541}[备份标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029356005}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_2029552613}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_2030207973}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subMask]{lang="EN-US"}*]{#struct_0_16293_x2703_2030142437}[：子网掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029683686}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[(MT *topoId*)(L *sysLevel*) Added route to RIB with relay NIB ID *nibId*, destination: *ipPrefix*.]{lang="EN-US"}]{#struct_0_16293_x2703_2029618150}

[[添加路由信息至]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_2029814758}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029421542}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_2029356006}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nibId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029552614}[：]{lang="EN-US" style="font-family:宋体"}[NIB ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_2029487078}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[(MT *topoId*)(L *sysLevel*) Modified route to RIB with relay NIB ID *nibId*, destination: *ipPrefix*.]{lang="EN-US"}]{#struct_0_16293_x2703_2030207974}

[[修改路由信息至]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_2029683687}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029618151}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_2029814759}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nibId]{lang="EN-US"}*]{#struct_0_16293_x2703_2029749223}[：]{lang="EN-US" style="font-family:宋体"}[NIB ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_2029421543}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[(MT *topoId*)(L *sysLevel*) Deleted route to RIB with relay NIB ID *nibId*, destination: *ipPrefix*.]{lang="EN-US"}]{#struct_0_16293_x2703_2029552615}

[[删除路由信息至]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_16293_x2703_2029487079}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_2030207975}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_2030142439}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nibId]{lang="EN-US"}*]{#struct_0_16293_x2703_x699265209}[：]{lang="EN-US" style="font-family:宋体"}[NIB ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipPrefix]{lang="EN-US"}*]{#struct_0_16293_x2703_x699068601}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀]{lang="EN-US" style="font-family:宋体"}

[[(MT *topoId*)(L *sysLevel*) Deleted relay NIB ID *nibId*, spfnode: *sourceId*, *ipFamily*.]{lang="EN-US"}]{#struct_0_16293_x2703_x699134137}

[[删除]{style="font-family:宋体"}[NIB ID]{lang="EN-US"}]{#struct_0_16293_x2703_x699461817}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x699330745}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x699396281}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nibId]{lang="EN-US"}*]{#struct_0_16293_x2703_x698675385}[：]{lang="EN-US" style="font-family:宋体"}[NIB ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x699199672}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipF]{lang="EN-US"}[amily]{lang="EN-US"}*]{#struct_0_16293_x2703_x699265208}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[(MT *topoId*)(L *sysLevel*) Added relay NIB ID *nibId*, spfnode: *sourceId*, *ipFamily*.]{lang="EN-US"}]{#struct_0_16293_x2703_x699068600}

[[添加]{style="font-family:宋体"}[NIB ID]{lang="EN-US"}]{#struct_0_16293_x2703_x699461816}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x699527352}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x699330744}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nibId]{lang="EN-US"}*]{#struct_0_16293_x2703_x698675384}[：]{lang="EN-US" style="font-family:宋体"}[NIB ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x698740920}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipF]{lang="EN-US"}[amily]{lang="EN-US"}*]{#struct_0_16293_x2703_x699199671}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[(MT *topoId*)(L *sysLevel*) Modified relay NIB ID *nibId*, spfnode: *sourceId*, *ipFamily*.]{lang="EN-US"}]{#struct_0_16293_x2703_x699068599}

[[修改]{style="font-family:宋体"}[NIB ID]{lang="EN-US"}]{#struct_0_16293_x2703_x699134135}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topoId]{lang="EN-US"}*]{#struct_0_16293_x2703_x699461815}[：拓扑号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sysLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x699330743}[：系统级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nibId]{lang="EN-US"}*]{#struct_0_16293_x2703_x699396279}[：]{lang="EN-US" style="font-family:宋体"}[NIB ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_x698740919}[：源系统]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipF]{lang="EN-US"}[amily]{lang="EN-US"}*]{#struct_0_16293_x2703_x699199670}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1513381032}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_x1437560663}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，分别在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，建立]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[邻居。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开路由计算调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis spf verbose]{lang="EN-US"}]{#struct_0_16293_x2703_x250204563}

[\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L1) Deleting link 0000.0000.0004.05 \--\> 0000.0000.0004.00 Cost:0]{lang="EN-US"}

[\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF node (MT0)(L1) Deleting system 0000.0000.0004.05]{lang="DA"}

[\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Trigger SPF at  Sec = 23961, MSec = 527]{lang="EN-US"}

[\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) SPF old scheduled event: 0x00000000, new trigger event: 0x00000002.]{lang="EN-US"}

[\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) SPF event 0x00000002 is scheduled.]{lang="EN-US"}

[\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x700440715}*[删除]{style="font-family:宋体"}[Level1]{lang="EN-US"}[的]{style="font-family:宋体"}[Link]{lang="EN-US"}[和]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点，触发路由计算]{style="font-family:宋体"}*

[[ISIS-13-SPF: SPF link (MT0)(L2) Deleting link 0000.0000.0004.05 \--\> 0000.0000.0004.00 Cost:0]{lang="EN-US"}]{#struct_0_16293_x2703_x1483640771}

[\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF node (MT0)(L2) Deleting system 0000.0000.0004.05]{lang="DA"}

[\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Trigger SPF at  Sec = 23961, MSec = 528]{lang="EN-US"}

[\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) SPF old scheduled event: 0x00000002, new trigger event: 0x00000002.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x705419490}*[删除]{style="font-family:宋体"}[Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[Link]{lang="EN-US"}[和]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点，触发路由计算]{style="font-family:宋体"}*

[[\*Apr  8 13:25:27:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1483706307}

[ISIS-13-SPF: (MT0)(L1) Deleting prefix for 10.152.1.0/255.255.255.0, from forwarding table.]{lang="EN-US"}

[\*Apr  8 13:25:27:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) Deleting prefix for 10.152.1.0/255.255.255.0, from forwarding table.]{lang="EN-US"}

[\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) Adding prefix for 10.152.1.0/255.255.255.0 from 0000.0000.0004.00, into forwarding table.]{lang="EN-US"}

[\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Trigger SPF at  Sec = 23967, MSec = 892]{lang="EN-US"}

[\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) SPF old scheduled event: 0x00000002, new trigger event: 0x00000008.]{lang="EN-US"}

[\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) SPF event 0x0000000A is scheduled.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) SPF Event:0xa, running Flag, old: 0, current: 0x16.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1280114008}*[删除]{style="font-family:宋体"}[Level1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由前缀，触发路由计算]{style="font-family:宋体"}*

[[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1483902915}

[ISIS-13-SPF: (MT0)(L1) I-SPF run started at  Sec = 23971, MSec = 529 .]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Checking changed links.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L1) Destroy LINK 0000.0000.0004.05 \--\> 0000.0000.0004.00 Del]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Need rebuild SPT.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) Running full SPF.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Begin Level-1 SPF from root node.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) SPF node Node is added into SPT. 1000.0001.0003.00 Dist:0 Nexthops:0 Nbrs:1 Parents:0 Tree]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L1) Check the link to one nbr. 1000.0001.0003.00 \--\> 0000.0000.0004.07 AttAdjs:1]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF:  New distance is 10.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF:  Less cost, add node to TENT HEAP.]{lang="EN-US"}

[\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) SPF node Son node update to TENT list 0000.0000.0004.07 Dist:10 Nexthops:0 Nbrs:2 Parents:0 Tent Direct     ;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L1) Check the link to one nbr. 0000.0000.0004.07 \--\> 1000.0001.0003.00 AttAdjs:1 Back]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Link is backard link, ignore.]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) SPF node Node is added into SPT. 0000.0000.0004.00 Dist:10 Nexthops:0 Nbrs:1 Parents:1 Tree]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Merge nexthop from root node IPV4:1/1]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Merge nexthop from parent node IPV4:0]{lang="EN-US"}

[ISIS-13-SPF: Inform SPF nodes change to PAC&PRC.]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) SPF node Destroy node 0000.0000.0004.05 Dist:4294967295 Nexthops:0 Nbrs:0 Parents:0 Direct Del]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) I-SPF run ended at  Sec = 23971, MSec = 530 .]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) I-SPF run started at  Sec = 23971, MSec = 530 .]{lang="EN-US"}

[\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Checking changed links.]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L2) Destroy LINK 0000.0000.0004.05 \--\> 0000.0000.0004.00 Del]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Need rebuild SPT.]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) Running full SPF.]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Begin Level-2 SPF from root node.]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) SPF node Node is added into SPT. 1000.0001.0003.00 Dist:0 Nexthops:0 Nbrs:1 Parents:0 Tree]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L2) Check the link to one nbr. 1000.0001.0003.00 \--\> 0000.0000.0004.07 AttAdjs:1]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) SPF node  NBR node found. 0000.0000.0004.07 Dist:4294967295 Nexthops:0 Nbrs:2 Parents:0 Direct]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF:  New distance is 10.]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF:  Less cost, add node to TENT HEAP.]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) SPF node Son node update to TENT list 0000.0000.0004.07 Dist:10 Nexthops:0 Nbrs:2 Parents:0 Tent Direct]{lang="EN-US"}

[\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: SPF link (MT0)(L2) Check the link to one nbr. 0000.0000.0004.07 \--\> 1000.0001.0003.00 AttAdjs:1 Back]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Link is backard link, ignore.]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) SPF node Node is added into SPT. 0000.0000.0004.00 Dist:10 Nexthops:0 Nbrs:1 Parents:1 Tree]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Merge nexthop from root node IPV4:1/1]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Merge nexthop from parent node IPV4:0]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: Inform SPF nodes change to PAC&PRC.]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) SPF node Destroy node 0000.0000.0004.05 Dist:4294967295 N]{lang="EN-US"}

[exthops:0 Nbrs:0 Parents:0 Direct Del]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) I-SPF run ended at  Sec = 23971, MSec = 532 .]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[进行]{style="font-size:10.5pt;
font-family:宋体"}[Level1]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[和]{style="font-size:
10.5pt;font-family:宋体"}[Level2]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[的]{style="font-size:
10.5pt;font-family:宋体"}[ISPF]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[计算]{style="font-size:
10.5pt;font-family:宋体"}*

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) AREA run started at  Sec = 23971, MSec = 532 .]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) Processing increment area address calculating.]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) Area Addr: 32 is available.]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) AREA run ended at  Sec = 23971, MSec = 532 .]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) AREA run started at  Sec = 23971, MSec = 532 .]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) Processing increment area address calculating.]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) Area Addr: 32 is available.]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) AREA run ended at  Sec = 23971, MSec = 532 .]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0) Updating computed areas into L2 LSDB.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1303452024}*[进行]{style="font-family:宋体"}[Level1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level2]{lang="EN-US"}[的区域地址计算]{style="font-family:宋体"}*

[[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1483968451}

[ISIS-13-SPF: (MT0)(L1) PRC run started at  Sec = 23971, MSec = 532 .]{lang="EN-US"}

[\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) Processing increment IPV4 prefix calculating.]{lang="EN-US"}

[\*Apr  8 13:25:37:533 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L1) PRC run ended at  Sec = 23971, MSec = 533 .]{lang="EN-US"}

[\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) PRC run started at  Sec = 23971, MSec = 544 .]{lang="EN-US"}

[\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) Processing increment IPV4 prefix calculating.]{lang="EN-US"}

[\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-13-SPF: (MT0)(L2) PRC run ended at  Sec = 23971, MSec = 544 .]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1513810139}*[进行]{style="font-family:宋体"}[Level1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[Prc]{lang="EN-US"}[计算]{style="font-family:宋体"}*

[[\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_x1762539124}

[ISIS-13-SPF: (MT0) All phases of SPF work completed at  Sec = 23971, MSec = 544]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x2000510057}*[路由计算所有阶段完成]{style="font-family:宋体"}*

::: {#1487674431 .myid}
[]{#_Toc404788111}[]{#struct_0_16293_x2703_x1482985411}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x2037759818}

[**[debuging isis timer]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_x1273149299}

[**[undo debuging isis timer]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_874584844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_680592194}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_129268651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1859142048}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1704868800}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x1483050947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x318209169}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_1772945970}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x61304395}

[**[debuging isis timer]{lang="EN-US"}**]{#struct_0_16293_x2703_x2077133852}[命令用来打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging isis timer]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x778364076}[定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_x1314073438}[进程的定时器调试信息开关。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging isis timer]{lang="EN-US"}]{#struct_0_16293_x2703_x1723635313}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x437150268}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1483509698}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x113109300}

[[ISIS-*procId*-TMR: *adjLevel* adjacency *systemId* hold timer expired on the circuit *circuitName.*]{lang="EN-US"}]{#struct_0_16293_x2703_801833559}

[[hold time]{lang="EN-US"}]{#struct_0_16293_x2703_x969638681}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_346389686}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adjLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483575234}[：邻居类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1215502323}[：邻居]{lang="EN-US" style="font-family:宋体"}[system id]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x884715688}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-TMR: *adjLevel* hello timer expired on the circuit *circuitName*.]{lang="EN-US"}]{#struct_0_16293_x2703_x106460132}

[[Hello]{lang="EN-US"}]{#struct_0_16293_x2703_x1912409757}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483640770}[：进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adjLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_2023463865}[：邻居类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1721924174}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-TMR: Starting waiting timer for max seq num exceed, time value is *timer* ms.]{lang="EN-US"}]{#struct_0_16293_x2703_x34205608}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x384936768}[序列号反转处理的定时器启动]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483706306}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timer]{lang="EN-US"}*]{#struct_0_16293_x2703_1448769347}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号反转需要等待的处理时间秒数（]{style="font-family:宋体"}[LSP]{lang="EN-US"}[老化时间]{style="font-family:宋体"}[+LSP]{lang="EN-US"}[删除时间）]{style="font-family:宋体"}

[[ISIS-]{lang="DA"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_756964588}[-TMR: ]{lang="DA"}*[lspLevel]{lang="EN-US"}*[ LSP ]{lang="DA"}*[lspId]{lang="EN-US"}*[ ]{lang="EN-US"}[gen timer expired]{lang="DA"}

[[LSP]{lang="DA"}]{#struct_0_16293_x2703_x1702854626}[生成定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="DA"}*]{#struct_0_16293_x2703_x1483771842}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="DA"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="DA"}*]{#struct_0_16293_x2703_1741333429}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="DA"}[类型]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="DA"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="DA"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[lspId]{lang="DA"}*]{#struct_0_16293_x2703_x172896421}[ ]{lang="DA"}[：]{lang="EN-US" style="font-family:宋体"}[LSPID]{lang="DA"}

[[ISIS-*procId*-TMR: Start *lspLevel* LSP *lspid* gen timer, time vlaue is *Second*(ms)]{lang="EN-US"}]{#struct_0_16293_x2703_x1625440601}

[[启动]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1483837378}[生成时间间隔定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_454833550}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1772343522}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspid]{lang="EN-US"}*]{#struct_0_16293_x2703_x459298366}[：]{lang="EN-US" style="font-family:宋体"}[LSPID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Second]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483902914}[：]{lang="EN-US" style="font-family:宋体"}[Lsp]{lang="EN-US"}[生成定时器的当前时间间隔]{lang="EN-US" style="font-family:宋体"}

[[ISIS-]{lang="DA"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x262631917}[-TMR: Stop ]{lang="DA"}*[lspLevel]{lang="EN-US"}*[ LSP ]{lang="DA"}*[lspid ]{lang="EN-US"}*[ gen timer]{lang="DA"}

[[关闭]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x2021943776}[生成时间间隔定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1859159655}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483968450}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspid]{lang="EN-US"}*]{#struct_0_16293_x2703_1215073216}[：]{lang="EN-US" style="font-family:宋体"}[LSPID]{lang="EN-US"}

[[ISIS-*procId*-TMR: *lspLevel* flood timer expired on the circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1579964589}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_804993522}[报文发送定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1482985410}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_691123537}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x526105294}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-TMR: *lspLevel* fast flood timer expired]{lang="EN-US"}]{#struct_0_16293_x2703_x1483050946}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_1247874772}[快速扩散定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1188007833}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_937833247}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[ISIS-*procId*-TMR: *lspLevel* csnp timer expired on the circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1483509701}

[[CSNP]{lang="EN-US"}]{#struct_0_16293_x2703_1808746250}[报文发送定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_2125335748}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483575237}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1618786850}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-TMR: *lspLevel* psnp timer expired on the circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x1072854167}

[[PSNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1483640773}[报文发送定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_457379924}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_1272973049}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值为]{lang="EN-US" style="font-family:宋体"}[L1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[L2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483706309}[：接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*procId*-TMR: ]{lang="EN-US"}]{#struct_0_16293_x2703_x829775314}[(MT]{lang="DA"}*[mtIId]{lang="EN-US"}*[) Stop SPF timer.]{lang="DA"}

[[关闭]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_295281579}[定时器停止]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算调度]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_1945096330}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[mtIId]{lang="DA"}*]{#struct_0_16293_x2703_x1483771845}[：]{lang="EN-US" style="font-family:宋体"}[拓扑号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*procId*-TMR: ]{lang="EN-US"}]{#struct_0_16293_x2703_981818542}[(MT]{lang="DA"}*[mtIId]{lang="EN-US"}*[) SPF timer expired.]{lang="DA"}

[[关闭]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_x1483837381}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[procId]{lang="EN-US"}*]{#struct_0_16293_x2703_x754692351}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}*[mtIId]{lang="DA"}*]{#struct_0_16293_x2703_895814041}[：]{lang="EN-US" style="font-family:宋体"}[拓扑号]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1110785720}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_1319789207}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，路由器类型为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.166/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[FFFF.FFFF.FFFF]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在同一个区域]{style="font-family:宋体"}[49]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis timer]{lang="EN-US"}]{#struct_0_16293_x2703_x1483902917}

[\*Apr  8 22:04:12:389 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-TMR: Level-1 hello timer expired on the circuit GigabitEthernet1/0/2.]{lang="EN-US"}

[\*Apr  8 22:04:15:039 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-TMR: Level-2 hello timer expired on the circuit GigabitEthernet1/0/2.]{lang="EN-US"}

[*[// Level-1]{lang="EN-US"}*]{#struct_0_16293_x2703_x1828715858}*[的邻居邻接超时，]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的邻居邻接超时]{style="font-family:宋体"}*

::: {#-147246634 .myid}
[]{#_Toc404788112}[]{#struct_0_16293_x2703_x426026454}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis update-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x712632519}

[**[debugging]{lang="EN-US"}**[ **isis** **update-packet** \[ **receive** \| **send** \] \[ **verbose**\] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_789244329}

[**[undo]{lang="EN-US"}**[ **debugging** **isis** **update-packet** \[ **receive** \| **send** \] \[ **verbose**\] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_16293_x2703_561111145}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1483968453}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_1618357743}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1363835366}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1629526481}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x993768946}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_422019436}

[**[receive]{lang="EN-US"}**]{#struct_0_16293_x2703_x1358083058}[：表示接收]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_16293_x2703_1371392467}[：表示发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_16293_x2703_x1482985413}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文详细调试信息开关。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_16293_x2703_x874960404}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1696072420}

[**[debugging isis]{lang="EN-US"}**]{#struct_0_16293_x2703_x994283656}[命令用来打开]{style="font-family:宋体"}[IS-IS LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}**[undo debugging isis]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS LSP]{lang="EN-US"}]{#struct_0_16293_x2703_642041773}[报文的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_16293_x2703_1643487551}[进程的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging isis update-packet]{lang="EN-US"}]{#struct_0_16293_x2703_1451293767}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x444363896}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1644181628}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_x1483050949}

[[ISIS-*processId*-UPDT: PDU level(*pduLevel*) mismatch with circuit level(*circuitLevel*) ]{lang="EN-US"}]{#struct_0_16293_x2703_x768547863}

[[接收到的]{style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1480765081}[报文的]{style="font-family:宋体"}[Level]{lang="EN-US"}[和接口]{style="font-family:宋体"}[Level]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x27715938}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pduLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x164632447}[：]{lang="EN-US" style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitLevel]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483509700}[：]{lang="EN-US" style="font-family:
  宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[Level]{lang="EN-US"}

[[ISIS-*processId*-UPDT: Lsp with more than three area addr(es)]{lang="EN-US"}]{#struct_0_16293_x2703_242662309}

[[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x720665237}[报文中携带的区域地址个数多于]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1464425529}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Receive *pduName* lspid=*systemId*. *pseudonodeNumber*-*lspNumber* seq=*lspSequenceNumber* ht=*holdTime* from snpa *mac-address* on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x683478934}

[[接收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1483575236}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x52702909}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pduName]{lang="EN-US"}*]{#struct_0_16293_x2703_x944367137}[：]{lang="EN-US" style="font-family:宋体"}[L1 LSP/L2 LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_1286392297}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483640772}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_x1108704017}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspSequenceNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_x534617941}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文的序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[holdTime]{lang="EN-US"}*]{#struct_0_16293_x2703_1722647815}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的存活时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mac-address]{lang="EN-US"}*]{#struct_0_16293_x2703_x1169572093}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文接收接口的]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483706308}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文接收接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Snpa address of pdu is the same as the local circuit(*circuitName*)]{lang="EN-US"}]{#struct_0_16293_x2703_1899108041}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_1342354362}[报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和接收接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[一样]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x797281909}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483771844}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP/SNP]{lang="EN-US"}[报文接收接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ ISIS process is under disable, ignoring pdu]{lang="EN-US"}]{#struct_0_16293_x2703_x1747064813}

[[ISIS]{lang="EN-US"}]{#struct_0_16293_x2703_x1823258398}[进程处于]{style="font-family:宋体"}[disable]{lang="EN-US"}[状态]{style="font-family:宋体"}[, ]{lang="EN-US"}[丢弃]{style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483837380}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Circuit(*circuitName*) is not operationally on, ignoring pdu]{lang="EN-US"}]{#struct_0_16293_x2703_811391590}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_1618902438}[报文接收接口处于非工作状态]{style="font-family:宋体"}[, ]{lang="EN-US"}[丢弃]{style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x195224888}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483902916}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP/SNP]{lang="EN-US"}[报文接收接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT: Circuit(*circuitName*) is silence, ignoring pdu]{lang="EN-US"}]{#struct_0_16293_x2703_900167497}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_x1317792843}[报文接收接口处于]{style="font-family:宋体"}[silence]{lang="EN-US"}[状态]{style="font-family:宋体"}[, ]{lang="EN-US"}[丢弃]{style="font-family:宋体"}[LSP/SNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1061992155}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_x1483968452}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP/SNP]{lang="EN-US"}[报文接收接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT: No active adjacency entry with such snpa(*mac-address*) on the cicuit(*circuitName*)]{lang="EN-US"}]{#struct_0_16293_x2703_52273802}

[[LSP/SNP]{lang="EN-US"}]{#struct_0_16293_x2703_x30071902}[报文发送端不是接收接口上的活动邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1482985412}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mac-address]{lang="EN-US"}*]{#struct_0_16293_x2703_1853922951}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP/SNP]{lang="EN-US"}[报文发送端]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_1000880825}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP/SNP]{lang="EN-US"}[报文接收接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT: Parsed area address *areaAddress*]{lang="EN-US"}]{#struct_0_16293_x2703_x1483050948}

[[从]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_797536078}[报文中解析区域地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_323951400}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaAddress]{lang="EN-US"}*]{#struct_0_16293_x2703_192297618}[：区域地址]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Parsed neighbor *neighborSourceId*]{lang="EN-US"}]{#struct_0_16293_x2703_82574244}

[[从]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_x1715715155}[报文中解析邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_868306888}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[neighborSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_82508708}[：邻居的]{lang="EN-US" style="font-family:
  宋体"}[Source ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT: Parsed ip prefix *ipAddressPair*]{lang="EN-US"}]{#struct_0_16293_x2703_x1742334427}

[[从]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_587572116}[报文中解析]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_82443172}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddressPair]{lang="EN-US"}*]{#struct_0_16293_x2703_x2123108900}[：]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址地址和掩码长度]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT: (MT]{lang="EN-US"}[ *topologyId*) *updateType* *Level* spf node(*nodeSourceId*)]{lang="EN-US"}]{#struct_0_16293_x2703_82377636}

[[向路由计算模块更新]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_16293_x2703_x1056474433}[节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1035024704}[：]{lang="EN-US" style="font-family:宋体"}[ IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topologyId]{lang="EN-US"}*]{#struct_0_16293_x2703_82312100}[：]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updateType]{lang="EN-US"}*]{#struct_0_16293_x2703_853476905}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[修改）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x1846321446}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nodeSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_82246564}[：]{lang="EN-US" style="font-family:
  宋体"}[SPF]{lang="EN-US"}[节点的]{lang="EN-US" style="font-family:
  宋体"}[Source ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level* att route advertised by *advertisednodeSourceId*]{lang="EN-US"}]{#struct_0_16293_x2703_x1097319500}

[[向路由计算模块更新默认路由]{style="font-family:宋体"}]{#struct_0_16293_x2703_493145454}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_82181028}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topologyId]{lang="EN-US"}*]{#struct_0_16293_x2703_2119699706}[：发布默认路由的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updateType]{lang="EN-US"}*]{#struct_0_16293_x2703_82115492}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x854841751}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[advertisednodeSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_1210351213}[：发布默认路由的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT: (MT *topologyId*) Update *Level*  area address advertised by *advertisednodeSourceId*]{lang="EN-US"}]{#struct_0_16293_x2703_83098532}

[[向路由计算模块更新区域地址]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1119510429}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_405993105}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topologyId]{lang="EN-US"}*]{#struct_0_16293_x2703_83032996}[：发布默认路由的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_x734908821}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[advertisednodeSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_82574245}[：发布默认路由的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level* spf link(*sourceId*-\>*destId*)]{lang="EN-US"}]{#struct_0_16293_x2703_240599981}

[[向路由计算模块更新]{style="font-family:宋体"}[SPF Link]{lang="EN-US"}]{#struct_0_16293_x2703_82508709}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_596317733}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topologyId]{lang="EN-US"}*]{#struct_0_16293_x2703_x856984859}[：发布默认路由的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updateType]{lang="EN-US"}*]{#struct_0_16293_x2703_82443173}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_215543260}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sourceId]{lang="FR"}*]{#struct_0_16293_x2703_82377637}[：]{lang="EN-US" style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[destId]{lang="FR"}*]{#struct_0_16293_x2703_899840703}[：]{lang="EN-US" style="font-family:宋体"}[目的]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="FR"}

[[ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level*  ip prefix(*ipAddressPair*) advertised by *advertisednodeSourceId*  in tlv type *tlvType*]{lang="EN-US"}]{#struct_0_16293_x2703_x858069396}

[[向路由计算模块更新路由前缀]{style="font-family:宋体"}]{#struct_0_16293_x2703_82312101}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1485175255}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[topologyId]{lang="EN-US"}*]{#struct_0_16293_x2703_82246565}[：发布默认路由的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点所在的拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[updateType]{lang="EN-US"}*]{#struct_0_16293_x2703_1241332660}[：更新类型（添加]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[删除）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Level]{lang="EN-US"}*]{#struct_0_16293_x2703_82181029}[：]{lang="EN-US" style="font-family:宋体"}[Level-1/Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipAddressPair]{lang="EN-US"}*]{#struct_0_16293_x2703_163384570}[：]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[路由前缀]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[advertisednodeSourceId]{lang="EN-US"}*]{#struct_0_16293_x2703_82115493}[：发布路由前缀的]{lang="EN-US" style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{lang="EN-US" style="font-family:宋体"}[Source ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tlvType]{lang="EN-US"}*]{#struct_0_16293_x2703_1101473385}[：发布路由前缀的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[ISIS-*processId*-UPDT: Own lsp *systemId*.]{lang="EN-US"}[ *pseudonodeNumber*-*lspNumber* processed, newer than lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x372461869}

[[处理比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_83098533}[中新的本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_836804707}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_83032997}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_1221406315}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82574242}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-UPDT: Other lsp *systemId*.]{lang="EN-US"}[ *pseudonodeNumber*-*lspNumber* processed, newer than lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x1333378131}

[[处理比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_82508706}[中新的非本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1359997403}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_82443170}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_x1740771876}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82377634}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, older than lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x674137409}

[[处理比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_82312098}[中旧的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_1246377574}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_82246562}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_2050636724}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82181026}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-UPDT: Lsp *systemId*.]{lang="EN-US"}[ *pseudonodeNumber*-*lspNumber* processed, same as lsdb copy]{lang="EN-US"}]{#struct_0_16293_x2703_x556659462}

[[处理和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_82115490}[中新旧一样的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1237178775}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_83098530}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_x1501847453}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_83032994}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Own lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, no exist in lsdb]{lang="EN-US"}]{#struct_0_16293_x2703_x352571797}

[[处理]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_82574243}[中不存在的本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_622937005}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_82508707}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82443171}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_597880284}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-UPDT: Other lsp *systemId*.]{lang="EN-US"}[ *pseudonodeNumber*-*lspNumber* processed, no exist in lsdb]{lang="EN-US"}]{#struct_0_16293_x2703_82377635}

[[处理]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_16293_x2703_1282177727}[中不存在的非本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_82312099}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1092274586}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82246563}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_94321588}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[ISIS-*processId*-UPDT: *lspContent*]{lang="EN-US"}]{#struct_0_16293_x2703_82181027}

[[接收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_82115491}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_719136361}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT: Lsp seq number is ZERO]{lang="EN-US"}]{#struct_0_16293_x2703_83098531}

[[发送序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16293_x2703_454467683}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_83032995}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[ISIS-*processId*-UPDT: Flooding *pduName* *systemId*.]{lang="EN-US"}[ *pseudonodeNumber*-*lspNumber* on the circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_1603743339}

[[扩散]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_82574240}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_82508704}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pduName]{lang="EN-US"}*]{#struct_0_16293_x2703_x977660379}[：]{lang="EN-US" style="font-family:宋体"}[L1 LSP/L2 LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_82443168}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_x1704036031}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82377632}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_82312096}[：扩散接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT: Circuit(*circuitName*) is silence, lsp not sent]{lang="EN-US"}]{#struct_0_16293_x2703_x1901578650}

[[接口处于]{style="font-family:宋体"}[silence]{lang="EN-US"}]{#struct_0_16293_x2703_82246560}[状态]{style="font-family:宋体"}[, LSP]{lang="EN-US"}[不在这个接口上进行扩散]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_x1861993548}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_82181024}[：扩散接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT:]{lang="EN-US"}[ Send *pduName* lspid=*systemId*. *pseudonodeNumber*-*lspNumber* seq=*lspSequenceNumber* ht=*holdTime* from snpa *mac-address* on circuit *circuitName*]{lang="EN-US"}]{#struct_0_16293_x2703_x174322438}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_82115488}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_83098528}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pduName]{lang="EN-US"}*]{#struct_0_16293_x2703_1593584584}[：]{lang="EN-US" style="font-family:宋体"}[L1 LSP/L2 LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[systemId]{lang="EN-US"}*]{#struct_0_16293_x2703_83032992}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[发送设备的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pseudonodeNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82574241}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[发送设备的伪节点]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_1005274029}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的分片号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lspSequenceNumber]{lang="EN-US"}*]{#struct_0_16293_x2703_82508705}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文的序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[holdTime]{lang="EN-US"}*]{#struct_0_16293_x2703_1360991781}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的存活时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mac-address]{lang="EN-US"}*]{#struct_0_16293_x2703_82443169}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文发送接口的]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[circuitName]{lang="EN-US"}*]{#struct_0_16293_x2703_82377633}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[报文发送接口名]{lang="EN-US" style="font-family:
  宋体"}

[[ISIS-*processId*-UPDT: *lspContent*]{lang="EN-US"}]{#struct_0_16293_x2703_1664514751}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_16293_x2703_82312097}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[processId]{lang="EN-US"}*]{#struct_0_16293_x2703_82246561}[：]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_476658612}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_319158927}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[3333.3333.3333]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.3.3.166/24]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[为]{style="font-family:宋体"}[FFFF.FFFF.FFFF]{lang="EN-US"}[、路由器类型为]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[，并在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.3.3.89/24]{lang="EN-US"}[；]{style="font-family:宋体"}[Router A]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[在同一个区域]{style="font-family:宋体"}[49]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[IS-IS LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging isis update-packet]{lang="EN-US"}]{#struct_0_16293_x2703_1163736860}

[\*Apr  8 03:39:05:325 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-UPDT: Receive L1 LSP lspid=ffff.ffff.ffff.00-01 seq=0x00000002 ht=1061 from snpa 0000-5e14-0200 on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[\*Apr  8 03:39:06:051 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-UPDT: Receive L2 LSP lspid=ffff.ffff.ffff.00-01 seq=0x00000002 ht=1059 from snpa 0000-5e14-0200 on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_1406603027}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上接收到]{style="font-family:宋体"}[Level-1 lspid=ffff.ffff.ffff.00-01]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文和]{style="font-family:宋体"}[Level-2 lspid=ffff.ffff.ffff.00-01]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr  8 03:39:10:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}]{#struct_0_16293_x2703_82181025}

[ISIS-1-UPDT: Flooding L2 LSP 3333.3333.3333.00-00 on the circuit GigabitEthernet1/0/2]{lang="EN-US"}

[\*Apr  8 03:39:10:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-UPDT: Flooding L1 LSP 3333.3333.3333.00-00 on the circuit GigabitEthernet1/0/2]{lang="EN-US"}

[\*Apr  8 03:39:10:601 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-UPDT: Send L1 LSP lspid=3333.3333.3333.00-00 seq=0x00000004 ht=1199 from snpa 0000-0e16-0200 on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[\*Apr  8 03:39:10:601 2011 RouterA ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US"}

[ISIS-1-UPDT: Send L2 LSP lspid=3333.3333.3333.00-00 seq=0x00000004 ht=1199 from snpa 0000-0e16-0200 on circuit GigabitEthernet1/0/2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x2130637574}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上发送]{style="font-family:宋体"}[Level-1 lspid=3333.3333.3333.00-00]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文和]{style="font-family:宋体"}[Level-2 lspid=3333.3333.3333.00-00]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#143436581 .myid}
[]{#_Toc404788113}[]{#struct_0_16293_x2703_1937511197}

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging osi**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1578999782}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_16293_x2703_x1097196940}

[**[debugging osi]{lang="EN-US"}**]{#struct_0_16293_x2703_564792658}

[**[undo debugging osi]{lang="EN-US"}**]{#struct_0_16293_x2703_2048423456}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16293_x2703_1088799547}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging osi ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}]{#struct_0_16293_x2703_x1252505896}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[ \]]{lang="EN-US"}

[**[undo debugging osi]{lang="EN-US"}**[ \[ **slot** ]{lang="EN-US"}]{#struct_0_16293_x2703_994368732}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[\]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16293_x2703_1937052446}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging osi]{lang="EN-US"}**[ \[ **chassis** ]{lang="EN-US"}]{#struct_0_16293_x2703_x1552286123}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ **slot** *slot-number* \]]{lang="EN-US"}

[**[undo debugging osi]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_16293_x2703_26334393}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16293_x2703_314062142}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16293_x2703_645509171}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1584108274}

[[network-admin]{lang="EN-US"}]{#struct_0_16293_x2703_1310249599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16293_x2703_x384485989}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x551056391}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_16293_x2703_x664914437}[：单板所在的槽位号。如果未指定本参数，将打开所有单板]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_16293_x2703_1936986910}[：设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将打开所有成员设备]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_16293_x2703_1492457964}[：设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果未指定本参数，将打开所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16293_x2703_1229007551}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将打开所有成员设备上所有单板]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16293_x2703_x1750348606}[：指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将打开所有单板]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16293_x2703_x322388152}

[**[debugging osi]{lang="EN-US"}**]{#struct_0_16293_x2703_1765189076}[命令用来]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}**[undo debugging osi]{lang="EN-US"}**[命令用来]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSI]{lang="EN-US"}]{#struct_0_16293_x2703_1678975860}[连接的]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[debugging osi]{lang="EN-US"}]{#struct_0_16293_x2703_2021757366}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x651309903}[[字段]{style="font-family:黑体"}]{#struct_0_16293_x2703_x444288341}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16293_x2703_1937183518}

[[OSI Input]{lang="EN-US"}]{#struct_0_16293_x2703_1991543192}

[[接收报文]{style="font-family:宋体"}]{#struct_0_16293_x2703_1937117982}

[[OSI Output]{lang="EN-US"}]{#struct_0_16293_x2703_1945351971}

[[发送报文]{style="font-family:宋体"}]{#struct_0_16293_x2703_x648562541}

[[IN IF]{lang="EN-US"}]{#struct_0_16293_x2703_1937314590}

[[接收报文的入接口]{style="font-family:宋体"}]{#struct_0_16293_x2703_1217282763}

[[OUT IF]{lang="EN-US"}]{#struct_0_16293_x2703_1832393779}

[[发送报文的出接口]{style="font-family:宋体"}]{#struct_0_16293_x2703_1937249054}

[[Packet Length]{lang="EN-US"}]{#struct_0_16293_x2703_x30259811}

[[报文的长度]{style="font-family:宋体"}]{#struct_0_16293_x2703_1937445662}

[[DstMac]{lang="EN-US"}]{#struct_0_16293_x2703_435998094}

[[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16293_x2703_1197018817}[地址]{style="font-family:宋体"}

[[First 32 bytes]{lang="EN-US"}]{#struct_0_16293_x2703_1937380126}

[[报文的前]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_16293_x2703_27989312}[字节内容]{style="font-family:宋体"}

[[The packet is dropped(Service slot is invalid)]{lang="EN-US"}]{#struct_0_16293_x2703_1937576734}

[[没有]{style="font-family:宋体"}[OSI]{lang="EN-US"}]{#struct_0_16293_x2703_1995254593}[连接时，接收到的报文因为没有业务板处理而被丢弃]{style="font-family:宋体"}

[[The packet is dropped(No match mac found)]{lang="EN-US"}]{#struct_0_16293_x2703_1370172242}

[[接收到的报文因为]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16293_x2703_1937511198}[地址匹配失败而被丢弃]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16293_x2703_1579196390}

[[\# Router A]{lang="EN-US"}]{#struct_0_16293_x2703_x1182732160}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，分别在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接报文调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging osi]{lang="EN-US"}]{#struct_0_16293_x2703_1937052443}

[\*Nov  7 14:34:14:913 2012 RouterA SOCKET/7/OSI: -MDC=1-Slot=2; ]{lang="EN-US"}

[OSI Input:]{lang="EN-US"}

[ IN IF = GigabitEthernet1/0/1, Packet Length = 1497]{lang="EN-US"}

[ DstMac = 0180-c200-0014]{lang="EN-US"}

[ First 32 bytes:]{lang="EN-US"}

[ 831b0106 0f010000 01000000 00000200]{lang="EN-US"}

[ 1e05d940 00000000 00010101 02011084]{lang="EN-US"}

[\*Nov  7 14:34:14:913 2012 RouterA SOCKET/7/OSI: -MDC=1;]{lang="EN-US"}

[OSI Input:]{lang="EN-US"}

[ IN IF = GigabitEthernet1/0/1, Packet Length = 1497]{lang="EN-US"}

[ DstMac = 0180-c200-0014]{lang="EN-US"}

[ First 32 bytes:]{lang="EN-US"}

[ 831b0106 0f010000 01000000 00000200]{lang="EN-US"}

[ 1e05d940 00000000 00010101 02011084]{lang="EN-US"}

[\*Nov  7 14:34:16:854 2012 RouterA SOCKET/7/OSI: -MDC=1;]{lang="EN-US"}

[OSI Output:]{lang="EN-US"}

[ OUT IF = GigabitEthernet1/0/1, Packet Length = 1497]{lang="EN-US"}

[ DstMac = 0180-c200-0014]{lang="EN-US"}

[ First 32 bytes:]{lang="EN-US"}

[ 831b0106 0f010000 01000000 00000100]{lang="EN-US"}

[ 1e05d940 00000000 00010101 02011084]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16293_x2703_x1552089515}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上接收和发送报文，报文长度为]{style="font-family:宋体"}[1497]{lang="EN-US"}[，目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-c200-0014]{lang="EN-US"}*

[ ]{lang="EN-US"}
