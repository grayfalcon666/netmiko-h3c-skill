::: {#-260358525 .myid}
[]{#_Toc404796720}[]{#struct_0_19838_x1039_1767900310}

**PTP \-- PTP配置命令 \-- display ptp clock**

------------------------------------------------------------------------

[**[display ptp clock]{lang="EN-US"}**]{#struct_0_19838_x1039_1130910371}[命令用来显示设备的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[时钟信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2123266297}

[**[display ptp clock]{lang="EN-US"}**]{#struct_0_19838_x1039_1925441282}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x412964865}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_1541580136}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1110983475}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_170370608}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_1028000966}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_146813926}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_1708532594}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2123725048}

[[如果]{style="font-family:宋体"}]{#struct_0_19838_x1039_1048066991}[PTP profile]{lang="EN-US"}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[没有指定，则显示信息为空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_657885227}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1601503680}[显示设备的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[时钟信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp clock]{lang="EN-US"}]{#struct_0_19838_x1039_x2123790584}

[PTP profile         : IEEE 1588 Version 2]{lang="EN-US"}

[PTP mode            : BC]{lang="EN-US"}

[Slave only          : No]{lang="EN-US"}

[Clock ID            : 000FE2-FFFE-FF0000]{lang="EN-US"}

[Clock type          : ToD1]{lang="EN-US"}

[ ToD direction  : In]{lang="EN-US"}

[ ToD delay time : 0 (ns)]{lang="EN-US"}

[Clock domain        : 0]{lang="EN-US"}

[Number of PTP ports : 2]{lang="EN-US"}

[Priority1     : 128]{lang="EN-US"}

[Priority2     : 128]{lang="EN-US"}

[Clock quality :]{lang="EN-US"}

[ Class                 : 248]{lang="EN-US"}

[ Accuracy              : 254]{lang="EN-US"}

[ Offset (log variance) : 65535]{lang="EN-US"}

[Offset from master : 0 (ns)]{lang="EN-US"}

[Mean path delay    : 0 (ns)]{lang="EN-US"}

[Steps removed      : 1]{lang="EN-US"}

[Local clock time   : Sun Jan 15 20:57:29 2011]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ptp clock]{lang="EN-US"}]{#struct_0_19838_x1039_x456838397}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1007263370}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_x512714772}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_511747372}

[[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x955935018}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1046457320}[协议遵循的标准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IEEE 1588 Version 2]{lang="EN-US"}]{#struct_0_19838_x1039_1644035149}[：]{lang="EN-US" style="font-family:
  宋体"}[PTP]{lang="EN-US"}[协议遵循]{lang="EN-US" style="font-family:
  宋体"}[IEEE1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IEEE 802.1AS]{lang="EN-US"}]{#struct_0_19838_x1039_x2123593976}[：]{lang="EN-US" style="font-family:宋体"}[PTP]{lang="EN-US"}[协议遵循]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[PTP mode]{lang="EN-US"}]{#struct_0_19838_x1039_300162109}

[[时钟节点类型：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1334996932}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BC]{lang="EN-US"}]{#struct_0_19838_x1039_x269931694}[：表示]{lang="EN-US" style="font-family:宋体"}[BC]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2ETC]{lang="EN-US"}]{#struct_0_19838_x1039_x1296132531}[：表示]{lang="EN-US" style="font-family:宋体"}[E2ETC]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2ETC-OC]{lang="EN-US"}]{#struct_0_19838_x1039_x2123659512}[：表示]{lang="EN-US" style="font-family:宋体"}[E2ETC+OC]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OC]{lang="EN-US"}]{#struct_0_19838_x1039_240963257}[：表示]{lang="EN-US" style="font-family:宋体"}[OC]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2PTC]{lang="EN-US"}]{#struct_0_19838_x1039_1378037368}[：表示]{lang="EN-US" style="font-family:宋体"}[P2PTC]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2PTC-OC]{lang="EN-US"}]{#struct_0_19838_x1039_x628851692}[：表示]{lang="EN-US" style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[Slave only]{lang="EN-US"}]{#struct_0_19838_x1039_1733785215}

[[OC]{lang="EN-US"}]{#struct_0_19838_x1039_x234762831}[的工作模式是否为]{style="font-family:宋体"}[Slave only]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_19838_x1039_x2123462904}[：表示是]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_19838_x1039_1780779320}[：表示不是]{lang="EN-US" style="font-family:宋体"}

[[Clock ID]{lang="EN-US"}]{#struct_0_19838_x1039_1387546321}

[[本设备的时钟编号]{style="font-family:宋体"}]{#struct_0_19838_x1039_1694130179}

[[Clock type]{lang="EN-US"}]{#struct_0_19838_x1039_1465604242}

[[本设备的时钟类型：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2123528440}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_19838_x1039_1356437211}[：本地时钟]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ToD0]{lang="EN-US"}]{#struct_0_19838_x1039_x1740529053}[：第一路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ToD1]{lang="EN-US"}]{#struct_0_19838_x1039_x1740332445}[：第二路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟]{style="font-family:宋体"}

[[ToD direction]{lang="EN-US"}]{#struct_0_19838_x1039_228506140}

[[ToD]{lang="FR"}]{#struct_0_19838_x1039_x1918247028}[时钟方向，取值为]{style="font-family:宋体"}[In]{lang="EN-US"}[。本设备的时钟类型为]{style="font-family:宋体"}[Local]{lang="EN-US"}[时，不显示该字段]{style="font-family:宋体"}

 

[[ToD delay time]{lang="EN-US"}]{#struct_0_19838_x1039_1240029118}

[[ToD]{lang="FR"}]{#struct_0_19838_x1039_x1740397981}[时钟时延校正时间，单位为纳秒。本设备的时钟类型为]{style="font-family:宋体"}[Local]{lang="EN-US"}[时，不显示该字段]{style="font-family:宋体"}

 

[[Clock domain]{lang="EN-US"}]{#struct_0_19838_x1039_x2123331832}

[[本设备所在的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1993067630}[域]{style="font-family:宋体"}

[[Number of PTP ports]{lang="EN-US"}]{#struct_0_19838_x1039_x832844471}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1857482584}[接口的数量]{style="font-family:宋体"}

[[Priority1]{lang="EN-US"}]{#struct_0_19838_x1039_x158498894}

[[本设备上时钟优先级一的值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2123397368}

[[Priority2]{lang="EN-US"}]{#struct_0_19838_x1039_1655464085}

[[本设备上时钟优先级二的值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1227206104}

[[Clock quality]{lang="EN-US"}]{#struct_0_19838_x1039_1380506369}

[[时钟品质特性]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2123200760}

[[Class]{lang="EN-US"}]{#struct_0_19838_x1039_18392788}

[[本设备上时钟的时间等级值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x135353800}

[[Accuracy]{lang="EN-US"}]{#struct_0_19838_x1039_x1524476211}

[[本设备上时钟的时间精度值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2123266296}

[[Offset (log variance)]{lang="EN-US"}]{#struct_0_19838_x1039_x803442073}

[[最优时钟的偏差度量]{style="font-family:宋体"}]{#struct_0_19838_x1039_x167770063}

[[Offset from master]{lang="EN-US"}]{#struct_0_19838_x1039_x25747099}

[[与父节点的时钟偏差，单位为纳秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_x2123725051}[表示无意义]{style="font-family:宋体"}

[[Mean path delay]{lang="EN-US"}]{#struct_0_19838_x1039_x874181774}

[[平均路径延时，单位为纳秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_952208732}[表示无意义]{style="font-family:宋体"}

[[Steps removed]{lang="EN-US"}]{#struct_0_19838_x1039_x2123790587}

[[最优时钟到本时钟节点的跳数，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_x2022922338}[表示无意义]{style="font-family:宋体"}

[[Local clock time]{lang="EN-US"}]{#struct_0_19838_x1039_284242640}

[[当前的本地系统时间]{style="font-family:宋体"}]{#struct_0_19838_x1039_x306152393}

[ ]{lang="EN-US"}

::: {#-1263206742 .myid}
[]{#_Toc404796721}[]{#struct_0_19838_x1039_1465649058}

**PTP \-- PTP配置命令 \-- display ptp corrections**

------------------------------------------------------------------------

[**[display ptp corrections]{lang="EN-US"}**]{#struct_0_19838_x1039_x2123593979}[命令用来显示]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口时间校正的历史信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1622152192}

[**[display ptp corrections]{lang="EN-US"}**]{#struct_0_19838_x1039_x707367281}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x400929047}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2045310154}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_564853444}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1071145166}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x2055433541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x2123659515}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x1325120684}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1256495145}

[[当设备每通过]{style="font-family:宋体"}[Slave]{lang="EN-US"}]{#struct_0_19838_x1039_x1880367742}[端口进行过一次时间]{style="font-family:宋体"}[/]{lang="EN-US"}[频率同步，就会记录一条对应信息，从而显示信息不为空，具体为：如果指定]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[，且设备存在]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口时，通过该]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口进行了时间同步，则显示信息不为空。若]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口更换，记录会被清空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_508576532}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_2115415582}[显示]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口时间校正的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp corrections]{lang="EN-US"}]{#struct_0_19838_x1039_x115190031}

[Slave port   Correction time          Corrections(s,ns)     Rate ratio]{lang="EN-US"}

[GE1/0/1      Mar 11 03:14:54 2012     0,74                  0.999999973]{lang="EN-US"}

[GE1/0/1      Mar 11 03:14:55 2012    -1,17                  0.999999980]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ptp corrections]{lang="EN-US"}]{#struct_0_19838_x1039_1844564505}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1018116298}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2123462907}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_1377494793}

[[Slave port]{lang="EN-US"}]{#struct_0_19838_x1039_x35453194}

[[Slave]{lang="EN-US"}]{#struct_0_19838_x1039_x1552319021}[端口名称]{style="font-family:宋体"}

[[Correction time]{lang="EN-US"}]{#struct_0_19838_x1039_x95761421}

[[时间偏差的校正时间]{style="font-family:宋体"}]{#struct_0_19838_x1039_x640081826}

[[Corrections(s,ns)]{lang="EN-US"}]{#struct_0_19838_x1039_x2123528443}

[[时间偏差（秒，纳秒），]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_953152684}[表示本次没有校正]{style="font-family:宋体"}

[[Rate ratio]{lang="EN-US"}]{#struct_0_19838_x1039_x1926018715}

[[本端口与]{style="font-family:宋体"}[Master]{lang="EN-US"}]{#struct_0_19838_x1039_214610007}[端口的频率比，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示本次没有校正]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-790250591 .myid}
[]{#_Toc404796722}[]{#struct_0_19838_x1039_x519686419}

**PTP \-- PTP配置命令 \-- display ptp foreign-masters-record**

------------------------------------------------------------------------

[**[display ptp foreign-masters-record]{lang="EN-US"}**]{#struct_0_19838_x1039_x1472218091}[命令用来显示外部主节点的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_649718296}

[**[display ptp foreign-masters-record ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_19838_x1039_x2123331835}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1542384779}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_138205020}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1985251470}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_834175884}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x1848376784}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_134368761}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x808452980}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x240646092}

[**[interface]{lang="EN-US"}***[ interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_19838_x1039_x2123397371}[：显示指定接口上的外部主节点信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。如未指定本参数，将显示所有接口的外部主节点信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x717123374}

[[在指定]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x613911483}[为]{style="font-family:宋体"}[IEEE 1588 version 2]{lang="EN-US"}[，同时指定]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[，且设备存在]{style="font-family:宋体"}[Slave]{lang="EN-US"}[或]{style="font-family:宋体"}[Uncalibrated]{lang="EN-US"}[端口时，显示信息才不为空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x584229266}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x250866684}[显示所有接口的外部主节点信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp foreign-masters-record]{lang="EN-US"}]{#struct_0_19838_x1039_x293914765}

[P1=Priority1, P2=Priority2, C=Class, A=Accuracy,]{lang="EN-US"}

[OSLV=Offset-scaled-log-variance, SR=Steps-removed]{lang="EN-US"}

[GM=Grandmaster]{lang="EN-US"}

[\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-\-- \-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface    Clock ID             P1   P2   C    A    OSLV   SR   GM]{lang="EN-US"}

[\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-\-- \-\-\-\-\-\-\-\--]{lang="EN-US"}

[GE1/0/1      000FE2-FFFE-FF0000   0    128  248  254  65535  0    Yes]{lang="EN-US"}

[GE1/0/2      000FE2-FFFE-FF0001   0    128  248  254  65535  1    No]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ptp foreign-masters-record]{lang="EN-US"}]{#struct_0_19838_x1039_x2123200763}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1018177450}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_1584476729}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_1643929637}

[[Interface]{lang="EN-US"}]{#struct_0_19838_x1039_x1310172126}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_912251544}[接口的名称]{style="font-family:宋体"}

[[Clock ID]{lang="EN-US"}]{#struct_0_19838_x1039_x1136462960}

[[外部主时钟节点的编号]{style="font-family:宋体"}]{#struct_0_19838_x1039_25737069}

[[P1]{lang="EN-US"}]{#struct_0_19838_x1039_x2123266299}

[[时钟优先级一的值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1919187320}

[[P2]{lang="EN-US"}]{#struct_0_19838_x1039_x302979486}

[[时钟优先级二的值]{style="font-family:宋体"}]{#struct_0_19838_x1039_1688603458}

[[C]{lang="EN-US"}]{#struct_0_19838_x1039_x511049071}

[[时钟的时间等级值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1316683276}

[[A]{lang="EN-US"}]{#struct_0_19838_x1039_x2123725050}

[[时钟的时间精度值]{style="font-family:宋体"}]{#struct_0_19838_x1039_691902167}

[[OSLV]{lang="EN-US"}]{#struct_0_19838_x1039_125858564}

[[最优时钟的偏差度量]{style="font-family:宋体"}]{#struct_0_19838_x1039_x474423965}

[[SR]{lang="EN-US"}]{#struct_0_19838_x1039_x599820512}

[[最优时钟到该时钟节点的跳数]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2123790586}

[[GM]{lang="EN-US"}]{#struct_0_19838_x1039_705961017}

[[最优时钟节点：]{style="font-family:宋体"}]{#struct_0_19838_x1039_39651938}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_19838_x1039_1896325535}[：表示该节点是最优时钟节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_19838_x1039_x1282492764}[：表示该节点不是最优时钟节点]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-709071388 .myid}
[]{#_Toc404796723}[]{#struct_0_19838_x1039_x2123593978}

**PTP \-- PTP配置命令 \-- display ptp interface**

------------------------------------------------------------------------

[**[display ptp interface]{lang="EN-US"}**]{#struct_0_19838_x1039_1106731163}[命令用来显示接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_818452522}

[**[display]{lang="EN-US"}**[ **ptp** **interface** \[ *interface-type* *interface-number* \| **brief** \]]{lang="EN-US"}]{#struct_0_19838_x1039_x1582049345}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1306936888}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x471331839}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_441027974}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x704634715}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_93242384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x2123659514}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_1403762671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x555337126}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_19838_x1039_1049739784}[：详细显示指定接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。如未指定本参数，将显示所有接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_19838_x1039_1433361632}[：简要显示所有接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息。如果未指定本参数，将详细显示指定接口或所有接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1099587418}

[[如果接口使能了]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1919760884}[功能，则详细显示信息不为空。只有接口]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能实际工作时，简要显示信息才不为空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x29450574}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x2123462906}[简要显示所有接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp interface brief]{lang="EN-US"}]{#struct_0_19838_x1039_x1351388562}

[Name         State        Delay mechanism  Clock step  Asymmetry correction]{lang="EN-US"}

[GE1/0/1      Slave        E2E              Two         0]{lang="EN-US"}

[GE1/0/2      Passive      E2E              Two         0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x914223833}[详细显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_19838_x1039_x2123528442}

[Clock ID                    : 000FE2-FFFE-FF0000]{lang="EN-US"}

[Port number                 : 15]{lang="EN-US"}

[PTP version                 : 2]{lang="EN-US"}

[PTP enable                  : Enabled]{lang="EN-US"}

[Transport of PTP            : User Datagram Protocol (IPv4)]{lang="EN-US"}

[Unicast destination address : 10.10.10.2]{lang="EN-US"}

[DSCP priority               : 56]{lang="EN-US"}

[Port state                  : Slave]{lang="EN-US"}

[Force state                 : No]{lang="EN-US"}

[Clock step                  : Two]{lang="EN-US"}

[Asymmetry correction        : 0]{lang="EN-US"}

[Delay mechanism             : End to End]{lang="EN-US"}

[Announce interval (log mean)           : 1]{lang="EN-US"}

[Announce receipt time out              : 3]{lang="EN-US"}

[Sync interval (log mean)               : 2]{lang="EN-US"}

[Delay request interval (log mean)      : 2]{lang="EN-US"}

[Peer delay request interval (log mean) : 0]{lang="EN-US"}

[Mean path delay                        : 0 (ns)]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ptp interface]{lang="EN-US"}]{#struct_0_19838_x1039_x1775730671}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1023126506}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2072057052}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_881489917}

[[Name]{lang="EN-US"}]{#struct_0_19838_x1039_1778143222}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1281971836}[接口的名称]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_19838_x1039_x2123331834}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1186498576}[接口的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Slave]{lang="EN-US"}]{#struct_0_19838_x1039_1031197203}[：接口状态为]{style="font-family:宋体"}[Slave]{lang="EN-US"}[，跟踪外部时间信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Uncalibrated]{lang="EN-US"}]{#struct_0_19838_x1039_2026682155}[：接口状态为]{lang="EN-US" style="font-family:宋体"}[Uncalibrated]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Slave]{lang="EN-US"}[状态前的临时状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_19838_x1039_x835055396}[：接口状态为]{style="font-family:宋体"}[Passive]{lang="EN-US"}[（端口收到对端的]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文后，计算出的状态），不跟踪外部时间信息，也不对外发布时间信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_19838_x1039_x426534241}[：接口状态为]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[，对外发布时间信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Premaster]{lang="EN-US"}]{#struct_0_19838_x1039_2035494609}[：接口状态为]{lang="EN-US" style="font-family:宋体"}[Premaster]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[状态前的临时状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Listening]{lang="EN-US"}]{#struct_0_19838_x1039_x2123397370}[：接口状态为]{lang="EN-US" style="font-family:宋体"}[Listening]{lang="EN-US"}[（端口初始化后，即进入]{style="font-family:宋体"}[Listening]{lang="EN-US"}[状态）]{style="font-family:宋体"}[，不跟踪外部时间信息，也不对外发布时间信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Faulty]{lang="EN-US"}]{#struct_0_19838_x1039_2011759981}[：接口状态为]{style="font-family:宋体"}[Faulty]{lang="EN-US"}[，该状态为]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议的错误状态（即检测到错误），接口不处理]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_19838_x1039_x413783878}[：接口状态为]{lang="EN-US" style="font-family:宋体"}[Disabled]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[接口上]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议未运行]{style="font-family:宋体"}[，接口不处理]{lang="EN-US" style="font-family:宋体"}[协议报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initializing]{lang="EN-US"}]{#struct_0_19838_x1039_374633710}[：接口状态为]{lang="EN-US" style="font-family:宋体"}[Initializing]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[接口位于]{style="font-family:宋体"}[初始化状态，接口不处理]{lang="EN-US" style="font-family:宋体"}[协议报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_624751595}[：表示无意义]{lang="EN-US" style="font-family:宋体"}

[[Delay mechanism]{lang="EN-US"}]{#struct_0_19838_x1039_x2123200762}

[[接口的延时测量机制：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1144406626}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[End to End]{lang="EN-US"}]{#struct_0_19838_x1039_723708818}[：请求应答机制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer to Peer]{lang="EN-US"}]{#struct_0_19838_x1039_x82075531}[：端延时机制]{lang="EN-US" style="font-family:宋体"}

[[Clock step]{lang="EN-US"}]{#struct_0_19838_x1039_2023924651}

[[时间戳的携带模式：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2123266298}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[One]{lang="EN-US"}]{#struct_0_19838_x1039_x353103379}[：表示单步模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Two]{lang="EN-US"}]{#struct_0_19838_x1039_x1425042384}[：表示双步模式]{lang="EN-US" style="font-family:宋体"}

[[Asymmetry correction]{lang="EN-US"}]{#struct_0_19838_x1039_677955975}

[[非对称延迟校正时间，单位为纳秒]{style="font-family:宋体"}]{#struct_0_19838_x1039_x66126522}

[[Clock ID]{lang="EN-US"}]{#struct_0_19838_x1039_x201410746}

[[接口所在设备的时钟编号]{style="font-family:宋体"}]{#struct_0_19838_x1039_1667887462}

[[Port number]{lang="EN-US"}]{#struct_0_19838_x1039_900891398}

[[接口号]{style="font-family:宋体"}]{#struct_0_19838_x1039_1994116664}

[[PTP version]{lang="EN-US"}]{#struct_0_19838_x1039_x201476282}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1634720416}[版本号：取值只能为]{style="font-family:宋体"}[2]{lang="EN-US"}[，表示]{style="font-family:宋体"}[PTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[2]{lang="EN-US"}

[[PTP enable]{lang="EN-US"}]{#struct_0_19838_x1039_1352144056}

[[接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_2087015051}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_19838_x1039_58700285}[：表示接口的]{lang="EN-US" style="font-family:宋体"}[PTP]{lang="EN-US"}[处于激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_19838_x1039_x201279674}[：表示接口的]{lang="EN-US" style="font-family:宋体"}[PTP]{lang="EN-US"}[处于未激活状态]{lang="EN-US" style="font-family:宋体"}

[[Transport of PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1502475732}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1314638238}[报文封装格式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User Datagram Protocol (IPv4)]{lang="EN-US"}]{#struct_0_19838_x1039_905292216}[：]{lang="EN-US" style="font-family:宋体"}[PTP]{lang="EN-US"}[报文采用]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[）封装格式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IEEE 802.3/Ethernet]{lang="EN-US"}]{#struct_0_19838_x1039_x201345210}[：]{lang="EN-US" style="font-family:
  宋体"}[PTP]{lang="EN-US"}[报文采用]{lang="EN-US" style="font-family:
  宋体"}[IEEE 802.3/Ethernet]{lang="EN-US"}[封装格式]{lang="EN-US" style="font-family:宋体"}

[[Unicast destination address]{lang="EN-US"}]{#struct_0_19838_x1039_x1740266907}

[[采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_19838_x1039_774380086}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式的单播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。未配置]{style="font-family:宋体"}**[ptp]{lang="EN-US"}**[ **unicast-destination**]{lang="EN-US"}[命令，不显示该字段]{style="font-family:宋体"}

 

[[DSCP priority]{lang="EN-US"}]{#struct_0_19838_x1039_x1740070299}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_654294514}[报文封装]{style="font-family:宋体"}[格式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[时]{style="font-family:宋体"}[的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。未配置]{style="font-family:宋体"}**[ptp dscp]{lang="EN-US"}**[命令时，不显示该字段]{style="font-family:宋体"}

 

[[VLAN]{lang="EN-US"}]{#struct_0_19838_x1039_1409861930}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1016555650}[报文的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。未配置]{style="font-family:宋体"}**[ptp vlan]{lang="EN-US"}**[命令时，不显示该字段]{style="font-family:宋体"}

 

[[Dot1p priority]{lang="EN-US"}]{#struct_0_19838_x1039_x1740135835}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x713246184}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。未配置]{style="font-family:宋体"}**[ptp vlan]{lang="EN-US"}**[命令时，不显示该字段]{style="font-family:宋体"}

 

[[Force state]{lang="EN-US"}]{#struct_0_19838_x1039_1229010953}

[[是否配置强制状态生效：]{style="font-family:宋体"}]{#struct_0_19838_x1039_403518435}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_19838_x1039_1788357958}[：表示已配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_19838_x1039_x201148602}[：表示未配置]{lang="EN-US" style="font-family:宋体"}

[[Announce interval (log mean)]{lang="EN-US"}]{#struct_0_19838_x1039_61183415}

[[Announce]{lang="EN-US"}]{#struct_0_19838_x1039_595951589}[报文的发送周期＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[（单位为秒），本字段就是]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的值]{style="font-family:宋体"}

[[Announce receipt time out]{lang="EN-US"}]{#struct_0_19838_x1039_x201214138}

[[Announce]{lang="EN-US"}]{#struct_0_19838_x1039_80200489}[报文的接收超时倍数，在倍数的发送周期内，若未收到主节点的]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文，则认为主节点失效]{style="font-family:宋体"}

[[Sync interval (log mean)]{lang="EN-US"}]{#struct_0_19838_x1039_x64960060}

[[Sync]{lang="EN-US"}]{#struct_0_19838_x1039_261624207}[报文的发送周期＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[（单位为秒），本字段就是]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的值]{style="font-family:宋体"}

[[Delay request interval (log mean)]{lang="EN-US"}]{#struct_0_19838_x1039_x201017530}

[[Delay_Req]{lang="EN-US"}]{#struct_0_19838_x1039_882134608}[报文的最小发送间隔＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[（单位为秒），本字段就是]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的值]{style="font-family:宋体"}

[[Peer delay request interval (log mean)]{lang="EN-US"}]{#struct_0_19838_x1039_x716610404}

[[Pdelay_Req]{lang="EN-US"}]{#struct_0_19838_x1039_x201083066}[报文的发送周期＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[（单位为秒），本字段就是]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的值]{style="font-family:宋体"}

[[Mean path delay]{lang="EN-US"}]{#struct_0_19838_x1039_1644985313}

[[接口与对端的平均路径延时，单位为纳秒]{style="font-family:宋体"}]{#struct_0_19838_x1039_1333322972}

[ ]{lang="EN-US"}

::: {#1317133954 .myid}
[]{#_Toc304915245}[]{#_Toc404796724}[]{#struct_0_19838_x1039_x1534198157}

**PTP \-- PTP配置命令 \-- display ptp parent**

------------------------------------------------------------------------

[**[display ptp parent]{lang="EN-US"}**]{#struct_0_19838_x1039_857003741}[命令用来显示当前]{style="font-family:宋体"}[PTP]{lang="EN-US"}[设备父节点信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x200886458}

[**[display ptp parent]{lang="EN-US"}**]{#struct_0_19838_x1039_x306849001}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1295774887}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_753829104}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1369143621}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x129526185}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_1945507851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1793655767}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_2088952170}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x200951994}

[[如果]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1455921557}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[没有指定、]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[指定为]{style="font-family:宋体"}[TC]{lang="EN-US"}[或配置了强制状态生效，则显示信息为空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x489533241}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1555877940}[显示当前]{style="font-family:宋体"}[PTP]{lang="EN-US"}[设备父节点信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp parent]{lang="EN-US"}]{#struct_0_19838_x1039_x470551601}

[Parent clock:]{lang="EN-US"}

[ Parent clock ID                         : 000FE2-FFFE-FF0005]{lang="EN-US"}

[ Parent port number                      : 15]{lang="EN-US"}

[ Observed parent offset (log variance)   : N/A]{lang="EN-US"}

[ Observed parent clock phase change rate : N/A]{lang="EN-US"}

[Grandmaster clock:]{lang="EN-US"}

[ Grandmaster clock ID: 000FE2-FFFE-FF0000]{lang="EN-US"}

[ Grandmaster clock quality:]{lang="EN-US"}

[  Class                 : 248]{lang="EN-US"}

[  Accuracy              : 254]{lang="EN-US"}

[  Offset (log variance) : 65535]{lang="EN-US"}

[  Priority1             : 128]{lang="EN-US"}

[  Priority2             : 128]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ptp parent]{lang="EN-US"}]{#struct_0_19838_x1039_x201410745}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x990245226}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_1668084070}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_1882793534}

[[Parent clock]{lang="EN-US"}]{#struct_0_19838_x1039_1640497785}

[[父时钟信息]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1123615662}

[[Parent clock ID]{lang="EN-US"}]{#struct_0_19838_x1039_203468494}

[[父时钟的编号]{style="font-family:宋体"}]{#struct_0_19838_x1039_x524994956}

[[Parent port number]{lang="EN-US"}]{#struct_0_19838_x1039_x201476281}

[[父时钟节点的输出接口号]{style="font-family:宋体"}]{#struct_0_19838_x1039_1634654880}

[[Observed parent offset (log variance)]{lang="EN-US"}]{#struct_0_19838_x1039_1030177396}

[[父时钟节点的偏差度量，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_x1474578652}[表示无意义]{style="font-family:宋体"}

[[Observed parent clock phase change rate]{lang="EN-US"}]{#struct_0_19838_x1039_1074206895}

[[父时钟节点的相位变化比率，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_19838_x1039_x1888620318}[表示无意义]{style="font-family:宋体"}

[[Grandmaster clock]{lang="EN-US"}]{#struct_0_19838_x1039_x201279673}

[[最优时钟节点信息]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1502541268}

[[Grandmaster clock ID]{lang="EN-US"}]{#struct_0_19838_x1039_x981645086}

[[最优时钟节点编号]{style="font-family:宋体"}]{#struct_0_19838_x1039_x463958981}

[[Grandmaster clock quality]{lang="EN-US"}]{#struct_0_19838_x1039_x548700967}

[[最优时钟节点品质特性]{style="font-family:宋体"}]{#struct_0_19838_x1039_x201345209}

[[Class]{lang="EN-US"}]{#struct_0_19838_x1039_1229469704}

[[最优时钟的时间等级值]{style="font-family:宋体"}]{#struct_0_19838_x1039_1574456527}

[[Accuracy]{lang="EN-US"}]{#struct_0_19838_x1039_x2043744218}

[[最优时钟的时间精度值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1283057336}

[[Offset (log variance)]{lang="EN-US"}]{#struct_0_19838_x1039_x201148601}

[[最优时钟的偏差度量]{style="font-family:宋体"}]{#struct_0_19838_x1039_60986807}

[[Priority1]{lang="EN-US"}]{#struct_0_19838_x1039_1207846917}

[[最优时钟优先级一的值]{style="font-family:宋体"}]{#struct_0_19838_x1039_1243810839}

[[Priority2]{lang="EN-US"}]{#struct_0_19838_x1039_x1732885809}

[[最优时钟优先级二的值]{style="font-family:宋体"}]{#struct_0_19838_x1039_x201214137}

[ ]{lang="EN-US"}

::: {#-1080832621 .myid}
[]{#_Toc404796725}[]{#struct_0_19838_x1039_80921385}

**PTP \-- PTP配置命令 \-- display ptp statistics**

------------------------------------------------------------------------

[**[display ptp statistics]{lang="EN-US"}**]{#struct_0_19838_x1039_100771040}[命令用来显示]{style="font-family:宋体"}[PTP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_276243337}

[**[display ptp statistics ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_19838_x1039_545432992}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1126874001}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_444948880}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1639984081}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x201017529}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_881675857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1218560892}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x752876405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x152029334}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_19838_x1039_604250595}[：显示指定接口上的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。如未指定本参数，将显示所有接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_367118262}

[[如果]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_1027347865}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[没有指定，则显示信息为空。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x448938138}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x1600080246}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ptp statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_19838_x1039_x201083065}

[                     Received packets]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Announce :0          Sync      :0          Signaling          :0]{lang="EN-US"}

[DelayReq :0          DelayResp :0          FollowUp           :0]{lang="EN-US"}

[PdelayReq:0          PdelayResp:0          PdelayRespFollowUp :0]{lang="EN-US"}

[ ]{lang="EN-US"}

[                     Sent packets]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Announce :476        Sync      :2543       Signaling          :0]{lang="EN-US"}

[DelayReq :0          DelayResp :0          FollowUp           :2542]{lang="EN-US"}

[PdelayReq:238        PdelayResp:0          PdelayRespFollowUp :0]{lang="EN-US"}

[ ]{lang="EN-US"}

[                     Discarded packets]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Announce :0          Sync      :0          Signaling          :0]{lang="EN-US"}

[DelayReq :0          DelayResp :0          FollowUp           :0]{lang="EN-US"}

[PdelayReq:0          PdelayResp:0          PdelayRespFollowUp :0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ptp statistics]{lang="EN-US"}]{#struct_0_19838_x1039_1644788705}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x996018346}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_2050549836}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_x200886457}

[[Received packets]{lang="EN-US"}]{#struct_0_19838_x1039_x307045609}

[[收到的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_310065029}[协议报文数量的统计信息]{style="font-family:宋体"}

[[Sent packets]{lang="EN-US"}]{#struct_0_19838_x1039_x1151525983}

[[发出的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1325105124}[协议报文数量的统计信息]{style="font-family:宋体"}

[[Discarded packets]{lang="EN-US"}]{#struct_0_19838_x1039_x1795828242}

[[丢弃的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x200951993}[协议报文数量的统计信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#881671741 .myid}
[]{#_Toc404796726}[]{#struct_0_19838_x1039_x1455724949}

**PTP \-- PTP配置命令 \-- display ptp time-property**

------------------------------------------------------------------------

[**[display ptp time-property]{lang="EN-US"}**]{#struct_0_19838_x1039_x696127407}[命令用来显示]{style="font-family:
宋体"}[PTP]{lang="EN-US"}[时钟节点时间特性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1404659140}

[**[display ptp time-property]{lang="EN-US"}**]{#struct_0_19838_x1039_x1923036467}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1112908957}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_90660732}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1012817208}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1124241022}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x201410748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1667232102}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x1039_x1406714557}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_995379408}

[[如果]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x775983020}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[没有指定、]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[指定为]{style="font-family:宋体"}[TC]{lang="EN-US"}[或配置了强制状态生效，则显示信息为空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x955680896}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_287175378}[显示]{style="font-family:宋体"}[PTP]{lang="EN-US"}[节点时间特性。]{style="font-family:宋体"}

[[\<Sysname\> display ptp time-property]{lang="EN-US"}]{#struct_0_19838_x1039_x201476284}

[PTP clock time property:]{lang="EN-US"}

[ Current UTC offset valid : True]{lang="EN-US"}

[ Current UTC offset       : 33]{lang="EN-US"}

[ Leap59 : Yes]{lang="EN-US"}

[ Leap61 : No]{lang="EN-US"}

[ Time traceable      : True]{lang="EN-US"}

[ Frequency traceable : True]{lang="EN-US"}

[ PTP timescale       : True]{lang="EN-US"}

[ Time source         : 0xA0 (Internal oscillator)]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display ptp time-property]{lang="EN-US"}]{#struct_0_19838_x1039_1634851488}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1000755306}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1374576769}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x1039_1101746886}

[[PTP clock time property]{lang="EN-US"}]{#struct_0_19838_x1039_x346813257}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1282317618}[时钟节点时间特性]{style="font-family:宋体"}

[[Current UTC offset valid]{lang="EN-US"}]{#struct_0_19838_x1039_x201279676}

[[当前偏移量是否有效：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1502344660}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[True]{lang="EN-US"}]{#struct_0_19838_x1039_x655186938}[：有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_19838_x1039_x2000341404}[：无效]{lang="EN-US" style="font-family:宋体"}

[[Current UTC offset]{lang="EN-US"}]{#struct_0_19838_x1039_1315409923}

[[最优时钟的]{style="font-family:宋体"}[UTC]{lang="EN-US"}]{#struct_0_19838_x1039_x219925280}[时间相对于]{style="font-family:宋体"}[TAI]{lang="EN-US"}[时间的累计偏移量（单位为秒）]{style="font-family:宋体"}

[[Leap59]{lang="EN-US"}]{#struct_0_19838_x1039_x201345212}

[[是否对累计偏移量减一：]{style="font-family:宋体"}]{#struct_0_19838_x1039_1229142025}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_19838_x1039_x1926226699}[：表示是]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_19838_x1039_1243276775}[：表示不是]{lang="EN-US" style="font-family:宋体"}

[[Leap61]{lang="EN-US"}]{#struct_0_19838_x1039_x1356822409}

[[是否对累计偏移量加一：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1354292920}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_19838_x1039_x201148604}[：表示是]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_19838_x1039_60790199}[：表示不是]{lang="EN-US" style="font-family:宋体"}

[[Time traceable]{lang="EN-US"}]{#struct_0_19838_x1039_2095123186}

[[时间可跟踪性：]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1601966590}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ture]{lang="EN-US"}]{#struct_0_19838_x1039_1646572593}[：]{style="font-family:宋体"}[PTP]{lang="EN-US"}[时间可跟踪]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_19838_x1039_x201214140}[：]{style="font-family:宋体"}[PTP]{lang="EN-US"}[时间不可跟踪]{style="font-family:宋体"}

[[Frequency traceable]{lang="EN-US"}]{#struct_0_19838_x1039_80724776}

[[频率可跟踪性：]{style="font-family:宋体"}]{#struct_0_19838_x1039_153709846}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ture]{lang="EN-US"}]{#struct_0_19838_x1039_1137228280}[：频率可跟踪]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_19838_x1039_x201017532}[：频率不可跟踪]{lang="EN-US" style="font-family:宋体"}

[[PTP timescale]{lang="EN-US"}]{#struct_0_19838_x1039_882003536}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_2028269466}[时间标识：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[True]{lang="EN-US"}]{#struct_0_19838_x1039_x1413988214}[：]{style="font-family:宋体"}[PTP]{lang="EN-US"}[时间标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_19838_x1039_491358212}[：非]{style="font-family:宋体"}[PTP]{lang="EN-US"}[时间标识]{style="font-family:宋体"}

[[Time source]{lang="EN-US"}]{#struct_0_19838_x1039_x201083068}

[[最优时钟的属性值，代表的时钟类别包括：]{style="font-family:宋体"}]{#struct_0_19838_x1039_1645116385}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Atomic clock]{lang="EN-US"}]{#struct_0_19838_x1039_x1370716148}[：原子时钟]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GPS]{lang="EN-US"}]{#struct_0_19838_x1039_1677239175}[：]{lang="EN-US" style="font-family:宋体"}[Global Positioning System]{lang="EN-US"}[，全球定位系统]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Handset]{lang="EN-US"}]{#struct_0_19838_x1039_x200886460}[：手持设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Internal oscillator]{lang="EN-US"}]{#struct_0_19838_x1039_x307373286}[：内部振荡器]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NTP]{lang="EN-US"}]{#struct_0_19838_x1039_1871477870}[：]{lang="EN-US" style="font-family:宋体"}[Network Time Protocol]{lang="EN-US"}[，网络时间协议]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_19838_x1039_x200951996}[：其他]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1456052629}[：]{lang="EN-US" style="font-family:宋体"}[Precision Time Protocol]{lang="EN-US"}[，精确时间协议]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Terrestrial radio]{lang="EN-US"}]{#struct_0_19838_x1039_2123132906}[：陆基无线电]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_19838_x1039_1602097204}[：未知]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-784425857 .myid}
[]{#_Toc404796727}[]{#struct_0_19838_x1039_x744324678}

**PTP \-- PTP配置命令 \-- ptp active force-state**

------------------------------------------------------------------------

[**[ptp active force-state]{lang="EN-US"}**]{#struct_0_19838_x1039_x201410747}[命令用来配置强制状态生效。]{style="font-family:宋体"}

[**[undo ptp active force-state]{lang="EN-US"}**]{#struct_0_19838_x1039_1667952998}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_126303201}

[**[ptp]{lang="EN-US"}**[ **active** **force-state**]{lang="EN-US"}]{#struct_0_19838_x1039_682769665}

[**[undo]{lang="EN-US"}**[ **ptp** **active** **force-state**]{lang="EN-US"}]{#struct_0_19838_x1039_x1032180740}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1167139390}

[[未配置强制状态生效功能。]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1216927042}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_253404855}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x201476283}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1634785952}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_609865133}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x363018906}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x629179512}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_922294854}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1215690669}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x1231354659}[配置强制状态生效。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x201279675}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp active force-state]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1502410196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_422878814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_x1189624802}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp force-state]{lang="EN-US"}**]{#struct_0_19838_x1039_678723803}
:::

::: {#1143437204 .myid}
[]{#_Toc404796728}[]{#struct_0_19838_x1039_x1702710061}[]{#_Toc304915246}

**PTP \-- PTP配置命令 \-- ptp announce-interval**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **announce-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_2065726680}[命令用来配置]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **announce-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_263258822}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1033874834}

[**[ptp]{lang="EN-US"}**[ **announce-interval** *value*]{lang="EN-US"}]{#struct_0_19838_x1039_x201345211}

[**[undo]{lang="EN-US"}**[ **ptp** **announce-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_1228945417}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_60675305}

[[不同]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_984040229}[的缺省情况不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_2138339259}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的发送周期为]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[（即]{lang="EN-US" style="font-family:宋体"}[2^1^]{lang="EN-US"}[）秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1089783761}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的发送周期为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[（即]{lang="EN-US" style="font-family:宋体"}[2^0^]{lang="EN-US"}[）秒。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x819107280}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x2039331155}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x201148603}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_61117879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x5936873}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x340542459}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x1039_913057790}[：]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的发送周期＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[，单位为秒。当]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 1588 version 2]{lang="EN-US"}[时，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[；当]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1469371599}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_134924419}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_359035299}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x1827641702}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[4]{lang="EN-US"}[（即]{style="font-family:宋体"}[2^2^]{lang="EN-US"}[）秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x201214139}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp announce-interval 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_80266025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_x455733728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_433755357}
:::

::: {#-263787410 .myid}
[]{#_Toc404796729}[]{#struct_0_19838_x1039_1339913435}[]{#_Toc304915247}

**PTP \-- PTP配置命令 \-- ptp announce-timeout**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **announce-timeout**]{lang="EN-US"}]{#struct_0_19838_x1039_x28342130}[命令用来配置]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的接收超时倍数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **announce-timeout**]{lang="EN-US"}]{#struct_0_19838_x1039_x1368082043}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x540501610}

[**[ptp]{lang="EN-US"}**[ **announce-timeout** *multiple-value*]{lang="EN-US"}]{#struct_0_19838_x1039_x201017531}

[**[undo]{lang="EN-US"}**[ **ptp** **announce-timeout**]{lang="EN-US"}]{#struct_0_19838_x1039_882200144}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1902821896}

[[Announce]{lang="EN-US"}]{#struct_0_19838_x1039_1211733892}[报文的接收超时倍数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_276145900}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_1112283025}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1202825108}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1613403671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1035708993}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x201083067}

[*[multiple-value]{lang="EN-US"}*]{#struct_0_19838_x1039_1644919777}[：表示]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的接收超时倍数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_506027046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_2123907844}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主节点会周期性地发送]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}]{#struct_0_19838_x1039_51229047}[报文给从节点，当]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[时，如果从节点在本端配置的]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}[报文发送周期的]{lang="EN-US" style="font-family:宋体"}*[multiple-value]{lang="EN-US"}*[倍时间之内未收到主节点发来的]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}[报文，便认为该主节点失效；当]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，如果从节点在对端配置的]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}[报文发送周期的]{lang="EN-US" style="font-family:宋体"}*[multiple-value]{lang="EN-US"}*[倍时间之内未收到主节点发来的]{lang="EN-US" style="font-family:宋体"}[Announce]{lang="EN-US"}[报文，便认为该主节点失效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了保证]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1338093268}[PTP]{lang="EN-US"}[网络的稳定，请根据网络环境配置合理的值。一般情况下，建议将]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的接收超时倍数配置为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1229811759}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1220323190}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Announce]{lang="EN-US"}[报文的接收超时倍数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x200886459}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp announce-timeout 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x306914537}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp announce-interval]{lang="EN-US"}**]{#struct_0_19838_x1039_1032504370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_1139360263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_x1464920772}
:::

::: {#1290654071 .myid}
[]{#_Toc404796730}[]{#struct_0_19838_x1039_x1238431265}[]{#_Toc304915248}

**PTP \-- PTP配置命令 \-- ptp asymmetry-correction**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **asymmetry-correction**]{lang="EN-US"}]{#struct_0_19838_x1039_x1742785657}[命令用来配置非对称延迟校正时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **asymmetry-correction**]{lang="EN-US"}]{#struct_0_19838_x1039_28253749}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x200951995}

[**[ptp]{lang="EN-US"}**[ **asymmetry-correction** { **minus** \| **plus** } *value*]{lang="EN-US"}]{#struct_0_19838_x1039_x1455856021}

[**[undo]{lang="EN-US"}**[ **ptp** **asymmetry-correction**]{lang="EN-US"}]{#struct_0_19838_x1039_1214040751}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x431356632}

[[接口的非对称延迟校正时间为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19838_x1039_x563676929}[纳秒，即不进行校正。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1209475803}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x452634656}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1756438626}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1852164454}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x201410750}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1667756389}

[**[minus]{lang="EN-US"}**]{#struct_0_19838_x1039_540282644}[：表示进行负的非对称延迟校正。]{style="font-family:宋体"}

[**[plus]{lang="EN-US"}**]{#struct_0_19838_x1039_x172492112}[：表示进行正的非对称延迟校正。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x1039_x847516748}[：表示非对称延迟的校正时间值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2000000]{lang="EN-US"}[，单位为纳秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1699523183}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1158459476}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x779729872}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x101258961}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置非对称延迟的校正时间]{style="font-family:宋体"}[100]{lang="EN-US"}[纳秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x201476286}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp asymmetry-correction plus 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1634982560}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_531103023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_1562702882}
:::

::: {#1715489589 .myid}
[]{#_Toc404796731}[]{#struct_0_19838_x1039_x1986577240}[]{#_Toc304915249}

**PTP \-- PTP配置命令 \-- ptp clock-source**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}[ clock-source]{lang="EN-US"}**]{#struct_0_19838_x1039_x969734319}[命令用来配置外接]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟源的相关参数。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}[ clock-source]{lang="EN-US"}**]{#struct_0_19838_x1039_1454765012}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x201279678}

[**[ptp]{lang="EN-US"}[ clock-source ]{lang="EN-US"}**[{ **tod0** \| **tod1** }]{lang="EN-US"}[ { **accuracy** *acc-value* \| **class** *class-value* \| **time-source** *ts-value* }]{lang="EN-US"}]{#struct_0_19838_x1039_1334821356}

[**[undo ptp]{lang="EN-US"}[ clock-source ]{lang="EN-US"}**[{ **tod0** \| **tod1** } ]{lang="EN-US"}[{ **accuracy** \| **class** \| **time-source** }]{lang="EN-US"}]{#struct_0_19838_x1039_x173986361}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x118055045}

[[外接]{style="font-family:宋体"}[ToD]{lang="EN-US"}]{#struct_0_19838_x1039_1531522950}[时钟源的时间精度值为]{style="font-family:宋体"}[32]{lang="EN-US"}[，时间等级值为]{style="font-family:宋体"}[6]{lang="EN-US"}[，属性值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1935934040}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x271259898}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_223144033}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x201345214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1228748809}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1986668457}

[**[tod0]{lang="EN-US"}**]{#struct_0_19838_x1039_x1251674378}[：表示配置第一路外接]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟源的参数。]{style="font-family:宋体"}

[**[tod1]{lang="EN-US"}**]{#struct_0_19838_x1039_x174051897}[：表示配置第二路外接]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟源的参数。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[accuracy]{lang="EN-US"}**[ *acc-value*]{lang="EN-US"}]{#struct_0_19838_x1039_729998589}[：表示时钟的时间精度。]{style="font-family:宋体"}*[acc-value]{lang="EN-US"}*[为时间精度值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，数值越小精度越高，具体取值及其含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?1715489589#_Ref268612052)[所示。]{style="font-family:宋体"}

[]{#struct_0_19838_x1039_x2128896550}[[表1-8 ]{lang="EN-US"}[时间精度值及其含义]{style="font-family:
黑体"}]{#_Ref268612052}

[]{#table_struct_0_x999408810}[[时间精度值（十六进制）]{style="font-family:黑体"}]{#struct_0_19838_x1039_2126317130}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_19838_x1039_x201148606}

[[00]{lang="EN-US"}]{#struct_0_19838_x1039_60921271}[～]{style="font-family:宋体"}[1F]{lang="EN-US"}

[[Reserved]{lang="EN-US"}]{#struct_0_19838_x1039_x344474459}[（保留）]{style="font-family:宋体"}

[[20]{lang="EN-US"}]{#struct_0_19838_x1039_1804353253}

[[时间精确到]{style="font-family:宋体"}[25]{lang="EN-US"}]{#struct_0_19838_x1039_1667215215}[纳秒（]{style="font-family:宋体"}[1]{lang="EN-US"}[纳秒＝]{style="font-family:宋体"}[10^-9^]{lang="EN-US"}[秒）以内]{style="font-family:宋体"}

[[21]{lang="EN-US"}]{#struct_0_19838_x1039_141662997}

[[时间精确到]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_19838_x1039_x294439655}[纳秒以内]{style="font-family:宋体"}

[[22]{lang="EN-US"}]{#struct_0_19838_x1039_x201214142}

[[时间精确到]{style="font-family:宋体"}[250]{lang="EN-US"}]{#struct_0_19838_x1039_80593704}[纳秒以内]{style="font-family:宋体"}

[[23]{lang="EN-US"}]{#struct_0_19838_x1039_1211831838}

[[时间精确到]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x1039_1438289795}[微秒（]{style="font-family:宋体"}[1]{lang="EN-US"}[微秒＝]{style="font-family:宋体"}[10^-6^]{lang="EN-US"}[秒）以内]{style="font-family:宋体"}

[[24]{lang="EN-US"}]{#struct_0_19838_x1039_387204497}

[[时间精确到]{style="font-family:宋体"}[2.5]{lang="EN-US"}]{#struct_0_19838_x1039_x201017534}[微秒以内]{style="font-family:宋体"}

[[25]{lang="EN-US"}]{#struct_0_19838_x1039_882396752}

[[时间精确到]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_19838_x1039_701749751}[微秒以内]{style="font-family:宋体"}

[[26]{lang="EN-US"}]{#struct_0_19838_x1039_1953128277}

[[时间精确到]{style="font-family:宋体"}[25]{lang="EN-US"}]{#struct_0_19838_x1039_1509476813}[微秒以内]{style="font-family:宋体"}

[[27]{lang="EN-US"}]{#struct_0_19838_x1039_x201083070}

[[时间精确到]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_19838_x1039_1644592096}[微秒以内]{style="font-family:宋体"}

[[28]{lang="EN-US"}]{#struct_0_19838_x1039_2111789571}

[[时间精确到]{style="font-family:宋体"}[250]{lang="EN-US"}]{#struct_0_19838_x1039_134490311}[微秒以内]{style="font-family:宋体"}

[[29]{lang="EN-US"}]{#struct_0_19838_x1039_x1320432107}

[[时间精确到]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x1039_x200886462}[毫秒（]{style="font-family:宋体"}[1]{lang="EN-US"}[毫秒＝]{style="font-family:宋体"}[10^-3^]{lang="EN-US"}[秒）以内]{style="font-family:宋体"}

[[2A]{lang="EN-US"}]{#struct_0_19838_x1039_x307242214}

[[时间精确到]{style="font-family:宋体"}[2.5]{lang="EN-US"}]{#struct_0_19838_x1039_x847378551}[毫秒以内]{style="font-family:宋体"}

[[2B]{lang="EN-US"}]{#struct_0_19838_x1039_x1778862646}

[[时间精确到]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_19838_x1039_1637817253}[毫秒以内]{style="font-family:宋体"}

[[2C]{lang="EN-US"}]{#struct_0_19838_x1039_x200951998}

[[时间精确到]{style="font-family:宋体"}[25]{lang="EN-US"}]{#struct_0_19838_x1039_x1455135125}[毫秒以内]{style="font-family:宋体"}

[[2D]{lang="EN-US"}]{#struct_0_19838_x1039_x624775918}

[[时间精确到]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_19838_x1039_502571944}[毫秒以内]{style="font-family:宋体"}

[[2E]{lang="EN-US"}]{#struct_0_19838_x1039_x201410749}

[[时间精确到]{style="font-family:宋体"}[250]{lang="EN-US"}]{#struct_0_19838_x1039_1667297638}[毫秒以内]{style="font-family:宋体"}

[[2F]{lang="EN-US"}]{#struct_0_19838_x1039_524256329}

[[时间精确到]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x1039_955891349}[秒以内]{style="font-family:宋体"}

[[30]{lang="EN-US"}]{#struct_0_19838_x1039_x201476285}

[[时间精确到]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_19838_x1039_1634917024}[秒以内]{style="font-family:宋体"}

[[31]{lang="EN-US"}]{#struct_0_19838_x1039_984528420}

[[时间精确到大于]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_19838_x1039_x1217884364}[秒]{style="font-family:宋体"}

[[32]{lang="EN-US"}]{#struct_0_19838_x1039_x201279677}[～]{style="font-family:宋体"}[7F]{lang="EN-US"}

[[Reserved]{lang="EN-US"}]{#struct_0_19838_x1039_x1502279124}[（保留）]{style="font-family:宋体"}

[[80]{lang="EN-US"}]{#struct_0_19838_x1039_1056802118}[～]{style="font-family:宋体"}[FD]{lang="EN-US"}

[[For use by alternate PTP profiles]{lang="EN-US"}]{#struct_0_19838_x1039_x201345213}[（为]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}[预留）]{style="font-family:宋体"}

[[FE]{lang="EN-US"}]{#struct_0_19838_x1039_1229076489}

[[Unknown]{lang="EN-US"}]{#struct_0_19838_x1039_x719369566}[（未知）]{style="font-family:宋体"}

[[FF]{lang="EN-US"}]{#struct_0_19838_x1039_1105265298}

[[Reserved]{lang="EN-US"}]{#struct_0_19838_x1039_x201148605}[（保留）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[**[class]{lang="EN-US"}**[ *class-value*]{lang="EN-US"}]{#struct_0_19838_x1039_60724663}[：表示时钟的时间等级。]{style="font-family:宋体"}*[class-value]{lang="EN-US"}*[为时间等级值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，数值越小等级越高，具体取值及其含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1715489589#_Ref268612094)[所示（未列出的取值均被协议所保留）。]{style="font-family:宋体"}

[]{#struct_0_19838_x1039_1690886147}[[表1-9 ]{lang="EN-US"}[时间等级值及其含义]{style="font-family:
黑体"}]{#_Ref268612094}

[]{#table_struct_0_x973198410}[[时间等级值（十进制）]{style="font-family:黑体"}]{#struct_0_19838_x1039_2067218654}

[[含义]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1310612946}

[[6]{lang="EN-US"}]{#struct_0_19838_x1039_x1693509606}

[[表示与主参考时间源保持同步的时钟节点，由]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1048884112}[来分配时间表。时间等级值为]{style="font-family:宋体"}[6]{lang="EN-US"}[的时钟节点不可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[7]{lang="EN-US"}]{#struct_0_19838_x1039_x201214141}

[[表示先前时间等级值为]{style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_19838_x1039_80790312}[、但已无法与特定用途时间源保持同步的时钟节点，已进入续任模式且满足续任条件的时钟节点，由]{style="font-family:宋体"}[PTP]{lang="EN-US"}[来分配时间表。时间等级值为]{style="font-family:宋体"}[7]{lang="EN-US"}[的时钟节点不可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[13]{lang="EN-US"}]{#struct_0_19838_x1039_x652103304}

[[表示与特定用途的时间源保持同步的时钟节点，由]{style="font-family:宋体"}[ARB]{lang="EN-US"}]{#struct_0_19838_x1039_x1137535948}[来分配时间表。时间等级值为]{style="font-family:宋体"}[13]{lang="EN-US"}[的时钟节点不可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[14]{lang="EN-US"}]{#struct_0_19838_x1039_x1033020671}

[[表示先前时间等级值为]{style="font-family:宋体"}[13]{lang="EN-US"}]{#struct_0_19838_x1039_1816861095}[、但已无法与特定用途时间源保持同步的时钟节点，已进入续任模式且满足续任条件的时钟节点，由]{style="font-family:宋体"}[ARB]{lang="EN-US"}[来分配时间表。时间等级值为]{style="font-family:宋体"}[14]{lang="EN-US"}[的时钟节点不可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[52]{lang="EN-US"}]{#struct_0_19838_x1039_x201017533}

[[表示时间等级值为]{style="font-family:宋体"}[7]{lang="EN-US"}]{#struct_0_19838_x1039_882069072}[的时钟节点由于不满足续任条件而降级为备选时钟]{style="font-family:宋体"}[A]{lang="EN-US"}[。时间等级值为]{style="font-family:宋体"}[52]{lang="EN-US"}[的时钟节点不可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[58]{lang="EN-US"}]{#struct_0_19838_x1039_881937705}

[[表示时间等级值为]{style="font-family:宋体"}[14]{lang="EN-US"}]{#struct_0_19838_x1039_1865651117}[的时钟节点由于不满足续任条件而降级为备选时钟]{style="font-family:宋体"}[A]{lang="EN-US"}[。时间等级值为]{style="font-family:宋体"}[58]{lang="EN-US"}[的时钟节点不可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[187]{lang="EN-US"}]{#struct_0_19838_x1039_810993700}

[[表示时间等级值为]{style="font-family:宋体"}[7]{lang="EN-US"}]{#struct_0_19838_x1039_x201083069}[的时钟节点由于不满足续任条件而降级为备选时钟]{style="font-family:宋体"}[B]{lang="EN-US"}[。时间等级值为]{style="font-family:宋体"}[187]{lang="EN-US"}[的时钟节点可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[193]{lang="EN-US"}]{#struct_0_19838_x1039_1645050849}

[[表示时间等级值为]{style="font-family:宋体"}[14]{lang="EN-US"}]{#struct_0_19838_x1039_x1741929511}[的时钟节点由于不满足续任条件而降级为备选时钟]{style="font-family:宋体"}[B]{lang="EN-US"}[。时间等级值为]{style="font-family:宋体"}[193]{lang="EN-US"}[的时钟节点可成为该域中其他时钟的从时钟]{style="font-family:宋体"}

[[248]{lang="EN-US"}]{#struct_0_19838_x1039_1373394779}

[[时间等级值的缺省取值]{style="font-family:宋体"}]{#struct_0_19838_x1039_957941653}

[[255]{lang="EN-US"}]{#struct_0_19838_x1039_x200886461}

[[表示工作模式为]{style="font-family:宋体"}[Slave-only]{lang="EN-US"}]{#struct_0_19838_x1039_x307438822}[的时钟节点]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[**[time-source]{lang="EN-US"}**[ *ts-value*]{lang="EN-US"}]{#struct_0_19838_x1039_x1730570692}[：表示时钟的属性。]{style="font-family:宋体"}*[ts-value]{lang="EN-US"}*[为属性值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，具体取值及其含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-10]{lang="EN-US"}](?1715489589#_Ref268612150)[所示（未列出的取值均被协议所保留）。]{style="font-family:宋体"}

[]{#struct_0_19838_x1039_x263686425}[[表1-10 ]{lang="EN-US"}[属性值及其含义]{style="font-family:
黑体"}]{#_Ref268612150}

[]{#table_struct_0_x977698730}[[属性值（十六进制）]{style="font-family:黑体"}]{#struct_0_19838_x1039_x542384858}

[[含义]{style="font-family:黑体"}]{#struct_0_19838_x1039_x921682277}

[[10]{lang="EN-US"}]{#struct_0_19838_x1039_1804528337}

[[Atomic clock]{lang="EN-US"}]{#struct_0_19838_x1039_x200951997}[（原子时钟）]{style="font-family:宋体"}

[[20]{lang="EN-US"}]{#struct_0_19838_x1039_x1455987093}

[[GPS]{lang="EN-US"}]{#struct_0_19838_x1039_1214297560}[（]{style="font-family:宋体"}[Global Positioning System]{lang="EN-US"}[，全球定位系统）]{style="font-family:宋体"}

[[30]{lang="EN-US"}]{#struct_0_19838_x1039_x1625720316}

[[Terrestrial radio]{lang="EN-US"}]{#struct_0_19838_x1039_524546389}[（陆基无线电）]{style="font-family:宋体"}

[[40]{lang="EN-US"}]{#struct_0_19838_x1039_95993522}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_1364673195}[（]{style="font-family:宋体"}[Precision Time Protocol]{lang="EN-US"}[，精确时间协议）]{style="font-family:宋体"}

[[50]{lang="EN-US"}]{#struct_0_19838_x1039_724152674}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x1039_1912892943}[（]{style="font-family:宋体"}[Network Time Protocol]{lang="EN-US"}[，网络时间协议）]{style="font-family:宋体"}

[[60]{lang="EN-US"}]{#struct_0_19838_x1039_977869547}

[[Handset]{lang="EN-US"}]{#struct_0_19838_x1039_x480989128}[（手持设备）]{style="font-family:宋体"}

[[90]{lang="EN-US"}]{#struct_0_19838_x1039_1364607659}

[[Other]{lang="EN-US"}]{#struct_0_19838_x1039_1094812610}[（其他）]{style="font-family:宋体"}

[[A0]{lang="EN-US"}]{#struct_0_19838_x1039_x1229164946}

[[Internal oscillator]{lang="EN-US"}]{#struct_0_19838_x1039_x1211976565}[（内部振荡器）]{style="font-family:宋体"}

[[F0]{lang="EN-US"}]{#struct_0_19838_x1039_x1661506121}[～]{style="font-family:宋体"}[FE]{lang="EN-US"}

[[For use by alternate PTP profiles]{lang="EN-US"}]{#struct_0_19838_x1039_x1476349079}[（为]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}[预留）]{style="font-family:宋体"}

[[FF]{lang="EN-US"}]{#struct_0_19838_x1039_1364804267}

[[Reserved]{lang="EN-US"}]{#struct_0_19838_x1039_734340406}[（保留）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1555388154}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x988100082}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x599243681}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_737593257}[配置]{style="font-family:宋体"}[第一路外接]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟源的]{style="font-family:宋体"}[时间精度值为]{style="font-family:宋体"}[44]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1364738731}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp clock-source tod0 accuracy 44]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1144630934}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_23217041}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x826191529}

::: {#883623633 .myid}
[]{#_Toc404796732}[]{#struct_0_19838_x1039_2031449454}[]{#_Toc304915250}

**PTP \-- PTP配置命令 \-- ptp clock-step**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **clock-step**]{lang="EN-US"}]{#struct_0_19838_x1039_x1886045864}[命令用来[配置时间戳的携带]{#_Toc260994363}模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **clock-step**]{lang="EN-US"}]{#struct_0_19838_x1039_2023849085}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x994820142}

[**[ptp]{lang="EN-US"}**[ **clock-step** { **one-step** \| **two-step** }]{lang="EN-US"}]{#struct_0_19838_x1039_1364935339}

[**[undo]{lang="EN-US"}**[ **ptp** **clock-step**]{lang="EN-US"}]{#struct_0_19838_x1039_1496226219}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1076904484}

[[时间戳的携带模式为双步模式。]{style="font-family:宋体"}]{#struct_0_19838_x1039_x489552300}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_796220309}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x1239115812}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1590114905}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_468140099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1506581783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364869803}

[**[one-step]{lang="EN-US"}**]{#struct_0_19838_x1039_x361815417}[：表示时间戳的携带模式为单步模式。]{style="font-family:宋体"}

[**[two-step]{lang="EN-US"}**]{#struct_0_19838_x1039_x972920626}[：表示时间戳的携带模式为双步模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_86835938}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1613564962}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1642881643}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，只支持双步模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[mode]{lang="EN-US"}]{#struct_0_19838_x1039_1983733248}[为]{lang="EN-US" style="font-family:宋体"}[E2ETC]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[P2PTC]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[E2ETC+OC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[时，只支持双步模式。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x686085020}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x1175155954}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置时间戳的携带模式为双步模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1365066411}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp clock-step two-step]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x462876819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_550755689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_x1052836745}
:::

::: {#-1656001142 .myid}
[]{#_Toc304915251}[]{#_Toc404796733}[]{#struct_0_19838_x1039_60090947}

**PTP \-- PTP配置命令 \-- ptp delay-mechanism**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **delay-mechanism**]{lang="EN-US"}]{#struct_0_19838_x1039_841672116}[命令用来配置]{style="font-family:宋体"}[BC]{lang="EN-US"}[或]{style="font-family:宋体"}[OC]{lang="EN-US"}[的延时测量机制。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **delay-mechanism**]{lang="EN-US"}]{#struct_0_19838_x1039_878684682}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1795783482}

[**[ptp]{lang="EN-US"}**[ **delay-mechanism** { **e2e** \| **p2p** }]{lang="EN-US"}]{#struct_0_19838_x1039_1365000875}

[**[undo]{lang="EN-US"}**[ **ptp** **delay-mechanism**]{lang="EN-US"}]{#struct_0_19838_x1039_x1954393135}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_82562572}

[[不同]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x949754398}[的缺省情况不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_1368997646}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[时，缺省延时测量机制为请求应答机制。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19838_x1039_409830118}[profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，缺省延时测量机制为端延时机制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_25808632}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x1519521103}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1653140773}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1365197483}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x2055109662}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1243665957}

[**[e2e]{lang="EN-US"}**]{#struct_0_19838_x1039_x601997526}[：表示]{style="font-family:宋体"}[E2ETC]{lang="EN-US"}[所使用的请求应答机制。]{style="font-family:宋体"}

[**[p2p]{lang="EN-US"}**]{#struct_0_19838_x1039_581062553}[：表示]{style="font-family:宋体"}[P2PTC]{lang="EN-US"}[所使用的端延时机制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1871490379}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当设备的时钟节点类型为]{style="font-family:宋体"}]{#struct_0_19838_x1039_1612145394}[BC]{lang="EN-US"}[或]{style="font-family:宋体"}[OC]{lang="EN-US"}[时，才允许配置该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1370266931}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，只支持端延时机制，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_906339585}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1365131947}[配置设备的时钟节点类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置延时测量机制为请求应答机制。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x1575368628}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp delay-mechanism e2e]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1948167694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_x1333592919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x1648166218}
:::

::: {#1506135845 .myid}
[]{#_Toc404796734}[]{#struct_0_19838_x1039_1442077205}[]{#_Toc304915252}[]{#_Toc345342931}[]{#_Toc345342997}[]{#_Toc345342932}[]{#_Toc345342998}[]{#_Toc345342933}[]{#_Toc345342999}[]{#_Toc345342934}[]{#_Toc345343000}[]{#_Toc345342935}[]{#_Toc345343001}[]{#_Toc345342936}[]{#_Toc345343002}[]{#_Toc345342937}[]{#_Toc345343003}[]{#_Toc345342938}[]{#_Toc345343004}[]{#_Toc345342939}[]{#_Toc345343005}[]{#_Toc345342940}[]{#_Toc345343006}[]{#_Toc345342941}[]{#_Toc345343007}[]{#_Toc345342942}[]{#_Toc345343008}[]{#_Toc345342943}[]{#_Toc345343009}[]{#_Toc345342944}[]{#_Toc345343010}[]{#_Toc345342945}[]{#_Toc345343011}[]{#_Toc345342946}[]{#_Toc345343012}[]{#_Toc345342947}[]{#_Toc345343013}[]{#_Toc345342948}[]{#_Toc345343014}[]{#_Toc345342949}[]{#_Toc345343015}[]{#_Toc345342950}[]{#_Toc345343016}[]{#_Toc345342951}[]{#_Toc345343017}[]{#_Toc345342952}[]{#_Toc345343018}[]{#_Toc345342953}[]{#_Toc345343019}[]{#_Toc345342954}[]{#_Toc345343020}[]{#_Toc345342955}[]{#_Toc345343021}[]{#_Toc345342956}[]{#_Toc345343022}[]{#_Toc345342957}[]{#_Toc345343023}[]{#_Toc345342958}[]{#_Toc345343024}[]{#_Toc345342959}[]{#_Toc345343025}[]{#_Toc345342960}[]{#_Toc345343026}

**PTP \-- PTP配置命令 \-- ptp destination-mac**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **destination-mac**]{lang="EN-US"}]{#struct_0_19838_x1039_x1502348081}[命令用来配置非]{style="font-family:宋体"}[Pdelay]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **destination-mac**]{lang="EN-US"}]{#struct_0_19838_x1039_1364673196}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_724349282}

[**[ptp]{lang="EN-US"}**[ **destination-mac** *mac-address*]{lang="EN-US"}]{#struct_0_19838_x1039_1383481396}

[**[undo]{lang="EN-US"}**[ **ptp** **destination-mac**]{lang="EN-US"}]{#struct_0_19838_x1039_x1595937904}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1323040537}

[[非]{style="font-family:宋体"}[Pdelay]{lang="EN-US"}]{#struct_0_19838_x1039_1350770945}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[011B-1900-0000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_648815796}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x1992837281}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_994144742}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1364607660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1095271361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x67836842}

[*[mac-address]{lang="EN-US"}*]{#struct_0_19838_x1039_x226337437}[：表示非]{style="font-family:宋体"}[Pdelay]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，取值为]{style="font-family:宋体"}[0180-C200-000E]{lang="EN-US"}[或]{style="font-family:宋体"}[011B-1900-0000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2129163169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_1700693837}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pdelay]{lang="EN-US"}]{#struct_0_19838_x1039_x1135694069}[报文（包括]{lang="EN-US" style="font-family:宋体"}[Pdelay_Req]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Pdelay_Resp]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Pdelay_Resp_Follow_Up]{lang="EN-US"}[等）默认的目的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}[0180-C200-000E]{lang="EN-US"}[，不可修改。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1713574855}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令在]{style="font-family:宋体"}]{#struct_0_19838_x1039_1364804268}[PTP]{lang="EN-US"}[报文采用]{style="font-family:宋体"}[IEEE 802.3/Ethernet]{lang="EN-US"}[封装格式时才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_733357366}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x9277549}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置非]{style="font-family:宋体"}[Pdelay]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-C200-000E]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1525698610}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp destination-mac 0180-c200-000e]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1478219894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x530048051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_345867907}
:::

::: {#1398621534 .myid}
[]{#_Toc304915253}[]{#_Toc404796735}[]{#struct_0_19838_x1039_x1059500781}

**PTP \-- PTP配置命令 \-- ptp domain**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_19838_x1039_1364738732}[命令用来配置设备所属的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_19838_x1039_1144827542}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1563950027}

[**[ptp]{lang="EN-US"}**[ **domain** *domain-number*]{lang="EN-US"}]{#struct_0_19838_x1039_x833269082}

[**[undo]{lang="EN-US"}**[ **ptp** **domain**]{lang="EN-US"}]{#struct_0_19838_x1039_x359984602}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x698343294}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_20826121}[设备缺省属于域]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1244955104}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x359536213}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364935340}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1495767472}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x745091858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_781419777}

[*[domain-number]{lang="EN-US"}*]{#struct_0_19838_x1039_x1327931366}[：表示设备加入的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[域，]{style="font-family:宋体"}*[domain-number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_965058663}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x595228940}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x82870106}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1364869804}[配置设备所属的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[域为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x361487737}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp domain 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1776463486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_1780620137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x589662418}
:::

::: {#670813199 .myid}
[]{#_Toc404796736}[]{#struct_0_19838_x1039_x174379575}[]{#_Toc385854902}[]{#_Toc383589558}

**PTP \-- PTP配置命令 \-- ptp dscp**

------------------------------------------------------------------------

[**[ptp dscp]{lang="EN-US"}**]{#struct_0_19838_x1039_244508850}[命令用来配置]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）时的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ptp dscp]{lang="EN-US"}**]{#struct_0_19838_x1039_x1314202579}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1184859562}

[**[ptp dscp]{lang="FR"}**[ ]{lang="FR"}*[dscp]{lang="EN-US"}*]{#struct_0_19838_x1039_x794278349}

[**[undo ]{lang="FR"}[ptp dscp]{lang="EN-US"}**]{#struct_0_19838_x1039_x174445111}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2130878385}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1175089665}[报文封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）时的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_445912189}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_886807321}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x288830681}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_2122794358}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x397519657}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x174248503}

[*[dscp]{lang="SV"}*]{#struct_0_19838_x1039_x1319281403}[：]{style="font-family:宋体"}[DSCP]{lang="SV"}[优先级，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1956122126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1832043590}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_1044621600}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[只有当]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1762609105}[PTP]{lang="EN-US"}[报文封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）时，该命令才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1162412097}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x177652603}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文]{style="font-family:宋体"}[封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）时的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x174314039}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp transport-protocol udp]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp dscp 63]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1739008883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x1463733874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x2051399310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp transport-protocol]{lang="EN-US"}**]{#struct_0_19838_x1039_1502773565}
:::

::: {#292474422 .myid}
[]{#_Toc404796737}[]{#struct_0_19838_x1039_1783913462}

**PTP \-- PTP配置命令 \-- ptp enable**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_19838_x1039_451871157}[命令用来使能接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **enable**]{lang="EN-US"}]{#struct_0_19838_x1039_504462318}[命令用来关闭接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365066412}

[**[ptp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_19838_x1039_x463073427}

[**[undo]{lang="EN-US"}**[ **ptp** **enable**]{lang="EN-US"}]{#struct_0_19838_x1039_x262242765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1842743762}

[[接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1126117664}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_740225995}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x956030056}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1289351584}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x628888536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1365000876}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1954327599}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x2080083701}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备时钟节点类型为]{style="font-family:宋体"}]{#struct_0_19838_x1039_x740988695}[OC]{lang="EN-US"}[时，只允许在一个接口上使能]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议在完成]{style="font-family:宋体"}]{#struct_0_19838_x1039_1773188753}[PTP]{lang="EN-US"}[相关参数配置后，再在接口上使能]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1969713134}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_387291568}[配置设备的时钟节点类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1365197484}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x2055175198}[配置设备的时钟节点类型为]{style="font-family:宋体"}[E2ETC]{lang="EN-US"}[，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_381988073}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode e2etc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ptp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_738851640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_x844478849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x1257195990}
:::

::: {#-1739243069 .myid}
[]{#_Toc404796738}[]{#struct_0_19838_x1039_1962999107}[]{#_Toc304915254}

**PTP \-- PTP配置命令 \-- ptp force-state**

------------------------------------------------------------------------

[**[ptp force-state]{lang="EN-US"}**]{#struct_0_19838_x1039_1365131948}[命令用来[配置]{#_Toc260994359}]{style="font-family:宋体"}[PTP]{lang="EN-US"}[接口的]{style="font-family:宋体"}[强制角色。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **force-state**]{lang="EN-US"}]{#struct_0_19838_x1039_x1574647732}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2141769704}

[**[ptp force-state]{lang="EN-US"}**[ { **master** \| **passive** \| **slave** }]{lang="EN-US"}]{#struct_0_19838_x1039_x1060075256}

[**[undo]{lang="EN-US"}**[ **ptp** **force-state**]{lang="EN-US"}]{#struct_0_19838_x1039_x255980385}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x602737930}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x297578670}[接口的角色由]{style="font-family:宋体"}[BMC]{lang="EN-US"}[算法自动生成。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1047232207}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_646858978}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364673193}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_724021602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x447254930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1358446141}

[**[master]{lang="EN-US"}**]{#struct_0_19838_x1039_101738727}[：表示]{style="font-family:宋体"}[PTP]{lang="EN-US"}[接口的角色为]{style="font-family:宋体"}[Master]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[**[passive]{lang="EN-US"}**]{#struct_0_19838_x1039_376994274}[：表示]{style="font-family:宋体"}[PTP]{lang="EN-US"}[接口的角色为]{style="font-family:宋体"}[Passive]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_19838_x1039_x1414974604}[：表示]{style="font-family:宋体"}[PTP]{lang="EN-US"}[接口的角色为]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_19838_x1039_9824370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1265949426}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一台设备上最多只允许配置一个]{style="font-family:宋体"}]{#struct_0_19838_x1039_1364607657}[Slave]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1095730114}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x2007410611}[配置设备的时钟节点类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[，]{style="font-family:宋体"}[并配置]{style="font-family:宋体"}[PTP]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的强制角色为]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_819937802}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp force-state slave]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_627559869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_1860858332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_700952045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp slave-only]{lang="EN-US"}**]{#struct_0_19838_x1039_1364804265}
:::

::: {#351199196 .myid}
[]{#_Toc404796739}[]{#struct_0_19838_x1039_734209334}[]{#_Toc304915255}

**PTP \-- PTP配置命令 \-- ptp min-delayreq-interval**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **min-delayreq-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_x1225345607}[命令用来配置]{style="font-family:宋体"}[Delay_Req]{lang="EN-US"}[报文的最小发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **min-delayreq-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_x1462763045}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1822580155}

[**[ptp]{lang="EN-US"}**[ **min-delayreq-interval** *value*]{lang="EN-US"}]{#struct_0_19838_x1039_x1409968711}

[**[undo]{lang="EN-US"}**[ **ptp** **min-delayreq-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_1625888738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x795945038}

[[不同]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x712080293}[的缺省情况不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_1364738729}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[Delay_Req]{lang="EN-US"}[报文的最小发送间隔为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[（即]{lang="EN-US" style="font-family:宋体"}[2^0^]{lang="EN-US"}[）秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_1145155221}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_770237924}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x1761467527}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1904715266}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_655387286}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1934090401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1594211668}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x1039_124075661}[：]{style="font-family:宋体"}[Delay_Req]{lang="EN-US"}[报文的最小发送间隔＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[，单位为秒，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[-4]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364935337}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_1495570859}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1076752622}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_133986531}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Delay_Req]{lang="EN-US"}[报文的最小发送间隔为]{style="font-family:宋体"}[4]{lang="EN-US"}[（即]{style="font-family:宋体"}[2^2^]{lang="EN-US"}[）秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x405549813}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp min-delayreq-interval 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2052852407}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_1364869801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x361684345}
:::

::: {#1766724365 .myid}
[]{#_Toc404796740}[]{#struct_0_19838_x1039_x608635914}[]{#_Toc304915256}

**PTP \-- PTP配置命令 \-- ptp mode**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_762853547}[命令用来配置设备的时钟节点类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_x212616194}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_88259612}

[**[ptp]{lang="EN-US"}**[ **mode** { **bc** \| **e2etc** \| **e2etc-oc** \| **oc** \| **p2ptc** \| **p2ptc-oc** }]{lang="EN-US"}]{#struct_0_19838_x1039_x1079600754}

[**[undo]{lang="EN-US"}**[ **ptp** **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_861159714}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1486263039}

[[设备上没有配置任何时钟节点类型。]{style="font-family:宋体"}]{#struct_0_19838_x1039_1365066409}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x463401106}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x236284449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x440987775}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x987379033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1959072847}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1264108577}

[**[bc]{lang="EN-US"}**]{#struct_0_19838_x1039_1053970980}[：表示时钟节点类型为]{style="font-family:宋体"}[BC]{lang="EN-US"}[（]{style="font-family:宋体"}[Boundary Clock]{lang="EN-US"}[，边界时钟）。]{style="font-family:宋体"}

[**[e2etc]{lang="EN-US"}**]{#struct_0_19838_x1039_1365000873}[：表示时钟节点类型为]{style="font-family:宋体"}[E2ETC]{lang="EN-US"}[（]{style="font-family:宋体"}[End-to-End Transparent Clock]{lang="EN-US"}[，端到端透明时钟）。]{style="font-family:宋体"}

[**[e2etc-oc]{lang="EN-US"}**]{#struct_0_19838_x1039_x1954524207}[：表示时钟节点类型为]{style="font-family:宋体"}[E2ETC+OC]{lang="EN-US"}[（端到端透明时钟与普通时钟混合）。]{style="font-family:宋体"}

[**[oc]{lang="EN-US"}**]{#struct_0_19838_x1039_1529818284}[：表示时钟节点类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[（]{style="font-family:宋体"}[Ordinary Clock]{lang="EN-US"}[，普通时钟）。]{style="font-family:宋体"}

[**[p2ptc]{lang="EN-US"}**]{#struct_0_19838_x1039_1594349495}[：表示时钟节点类型为]{style="font-family:宋体"}[P2PTC]{lang="EN-US"}[（]{style="font-family:宋体"}[Peer-to-Peer Transparent Clock]{lang="EN-US"}[，点到点透明时钟）。]{style="font-family:宋体"}

[**[p2ptc-oc]{lang="EN-US"}**]{#struct_0_19838_x1039_1041579859}[：表示时钟节点类型为]{style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[（点到点透明时钟与普通时钟混合）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1215257763}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x833127932}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1445493698}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置为]{lang="EN-US" style="font-family:宋体"}[E2ETC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[E2ETC+OC]{lang="EN-US"}[类型。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[改变设备的时钟节点类型，会清空除]{style="font-family:宋体"}]{#struct_0_19838_x1039_x704431123}[profile]{lang="EN-US"}[类型外的所有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365197481}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x2054978590}[配置设备的时钟节点类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x2100211230}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}[]{#_Toc135292481}[]{#_Toc135292482}[]{#_Toc135292483}[]{#_Toc135292484}[]{#_Toc135292485}[]{#_Toc135292486}[]{#_Toc135292487}[]{#_Toc135292488}[]{#_Toc135292489}[]{#_Toc135292490}[]{#_Toc135292491}[]{#_Toc135292492}[]{#_Toc135292493}[]{#_Toc135292494}[]{#_Toc135292495}[]{#_Toc135292562}[]{#_Toc135292563}[]{#_Toc135292577}[]{#_Toc135292578}[]{#_Toc135292579}[]{#_Toc135292580}[]{#_Toc135292583}[]{#_Toc135292584}[]{#_Toc135292585}[]{#_Toc135292586}[]{#_Toc135292587}[]{#_Toc135292588}[]{#_Toc135292589}[]{#_Toc135292590}[]{#_Toc135292591}[]{#_Toc135292592}[]{#_Toc135292593}[]{#_Toc135292594}[]{#_Toc135292595}[]{#_Toc135292596}[]{#_Toc135292597}[]{#_Toc135292598}[]{#_Toc135292599}[]{#_Toc135292600}[]{#_Toc135292601}[]{#_Toc135292602}[]{#_Toc135292603}[]{#_Toc135292604}[]{#_Toc135292605}[]{#_Toc135292606}[]{#_Toc135292633}[]{#_Toc135292634}[]{#_Toc135292635}[]{#_Toc135292639}[]{#_Toc135292641}[]{#_Toc135292642}[]{#_Toc135292643}[]{#_Toc135292644}[]{#_Toc135292645}[]{#_Toc135292646}[]{#_Toc135292647}[]{#_Toc135292648}[]{#_Toc135292649}[]{#_Toc135292650}[]{#_Toc135292651}[]{#_Toc135292652}[]{#_Toc135292653}[]{#_Toc135292654}[]{#_Toc135292655}[]{#_Toc135292656}[]{#_Toc135292657}[]{#_Toc135292658}[]{#_Toc135292659}[]{#_Toc135292660}[]{#_Toc135292670}[]{#_Toc135292671}[]{#_Toc135292672}[]{#_Toc135292673}[]{#_Toc135292678}[]{#_Toc135292680}[]{#_Toc135292683}[]{#_Toc135292684}[]{#_Toc135292685}[]{#_Toc135292686}[]{#_Toc135292687}[]{#_Toc135292688}[]{#_Toc135292689}[]{#_Toc135292690}[]{#_Toc135292691}[]{#_Toc135292692}[]{#_Toc135292693}[]{#_Toc135292694}[]{#_Toc135292695}[]{#_Toc135292696}[]{#_Toc135292697}[]{#_Toc135292698}[]{#_Toc135292699}[]{#_Toc135292719}[]{#_Toc135292720}[]{#_Toc135292727}[]{#_Toc135292728}[]{#_Toc135292729}[]{#_Toc135292735}[]{#_Toc135292736}[]{#_Toc135292737}[]{#_Toc135292747}[]{#_Toc135292748}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1666595567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_169660583}
:::

::: {#-1596367016 .myid}
[]{#_Toc404796741}[]{#struct_0_19838_x1039_1752086074}[]{#_Toc304915257}

**PTP \-- PTP配置命令 \-- ptp pdelay-req-interval**

------------------------------------------------------------------------

[**[ptp pdelay-req-interval]{lang="EN-US"}**]{#struct_0_19838_x1039_647260533}[命令用来配置]{style="font-family:宋体"}[Pdelay_Req]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **pdelay-req-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_x2086570964}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365131945}

[**[ptp]{lang="EN-US"}**[ **pdelay-req-interval** *value*]{lang="EN-US"}]{#struct_0_19838_x1039_x1575499700}

[**[undo]{lang="EN-US"}**[ **ptp** **pdelay-req-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_1309148246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2034550951}

[[Pdelay_Req]{lang="EN-US"}]{#struct_0_19838_x1039_1810434240}[报文的发送周期为]{style="font-family:宋体"}[1]{lang="EN-US"}[（即]{style="font-family:宋体"}[2^0^]{lang="EN-US"}[）秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1095706871}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_546449889}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1248763499}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_946130643}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1364673194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_724218210}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x1039_170344699}[：]{style="font-family:宋体"}[Pdelay_Req]{lang="EN-US"}[报文的发送周期＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[，单位为秒，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[-4]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。当]{style="font-family:宋体"}[profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 1588 version 2]{lang="EN-US"}[时，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1446317220}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x971440908}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1401094783}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x461441458}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Pdelay_Req]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[4]{lang="EN-US"}[（即]{style="font-family:宋体"}[2^2^]{lang="EN-US"}[）秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1364607658}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp pdelay-req-interval 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1094747074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x2021667602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x1382693686}
:::

::: {#1412475333 .myid}
[]{#_Toc404796742}[]{#struct_0_19838_x1039_772888631}[]{#_Toc304915258}

**PTP \-- PTP配置命令 \-- ptp port-mode**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **port-mode**]{lang="EN-US"}]{#struct_0_19838_x1039_743322156}[命令用来配置]{style="font-family:宋体"}[TC+OC]{lang="EN-US"}[（包括]{style="font-family:宋体"}[E2ETC+OC]{lang="EN-US"}[和]{style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[）的接口类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **port-mode**]{lang="EN-US"}]{#struct_0_19838_x1039_1227130558}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1810248646}

[**[ptp]{lang="EN-US"}**[ **port-mode** **oc**]{lang="EN-US"}]{#struct_0_19838_x1039_456239683}

[**[undo]{lang="EN-US"}**[ **ptp** **port-mode**]{lang="EN-US"}]{#struct_0_19838_x1039_1364804266}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_734274870}

[[E2ETC+OC]{lang="EN-US"}]{#struct_0_19838_x1039_1123208803}[和]{style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[上各接口的类型都为]{style="font-family:宋体"}[TC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1158948614}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_1538395811}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2130562613}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_278065650}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x201370520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1281093891}

[**[oc]{lang="EN-US"}**]{#struct_0_19838_x1039_1364738730}[：表示]{style="font-family:宋体"}[TC+OC]{lang="EN-US"}[的接口类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1144696470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_763267051}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当设备的时钟节点类型为]{style="font-family:宋体"}]{#struct_0_19838_x1039_1901722223}[E2ETC+OC]{lang="EN-US"}[或]{style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[时才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x251708843}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x337930368}[配置设备的时钟节点类型为]{style="font-family:宋体"}[P2PTC+OC]{lang="EN-US"}[，并配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x1020140814}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode p2ptc-oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp port-mode oc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364935338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_1496291755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_273409111}
:::

::: {#-539347923 .myid}
[]{#_Toc404796743}[]{#struct_0_19838_x1039_x4484099}[]{#_Toc304915259}[]{#_Toc302131798}

**PTP \-- PTP配置命令 \-- ptp priority**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **priority** **clock-source**]{lang="EN-US"}]{#struct_0_19838_x1039_x1756607484}[命令用来配置时钟参与]{style="font-family:宋体"}[BMC]{lang="EN-US"}[算法的优先级参数。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **priority** **clock-source**]{lang="EN-US"}]{#struct_0_19838_x1039_2139715013}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1686028659}

[**[ptp]{lang="EN-US"}**[ **priority** **clock-source** { **local** \| **tod0** \| **tod1** } { **priority1** *pri1-value* \| **priority2** *pri2-value* }]{lang="EN-US"}]{#struct_0_19838_x1039_534655816}

[**[undo]{lang="EN-US"}**[ **ptp** **priority** **clock-source** { **local** \| **tod0** \| **tod1** } { **priority1** \| **priority2** }]{lang="EN-US"}]{#struct_0_19838_x1039_x174445117}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364869802}

[[不同]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x361880953}[的缺省情况不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x551083581}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[时，时钟优先级一、二的缺省值均为]{lang="EN-US" style="font-family:宋体"}[128]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19838_x1039_2054001611}[profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，时钟优先级一的缺省值均为]{style="font-family:宋体"}[246]{lang="EN-US"}[，时钟优先级二的缺省值均为]{style="font-family:宋体"}[248]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1617189898}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_224669664}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1485798393}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_711184946}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1365066410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x462942355}

[**[local]{lang="EN-US"}**]{#struct_0_19838_x1039_1717354244}[：表示配置本地时钟的优先级参数。]{style="font-family:宋体"}

[**[tod0]{lang="EN-US"}**]{#struct_0_19838_x1039_x174314045}[：表示配置第一路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟的优先级参数。]{style="font-family:宋体"}

[**[tod1]{lang="EN-US"}**]{#struct_0_19838_x1039_x1738222450}[：表示配置第二路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟的优先级参数。]{style="font-family:宋体"}[本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[priority1]{lang="EN-US"}**[ *pri1-value*]{lang="EN-US"}]{#struct_0_19838_x1039_x657008713}[：表示时钟的优先级一。]{style="font-family:宋体"}*[pri1-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[优先级一的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，数值越小优先级越高。]{style="font-family:宋体"}

[**[priority2]{lang="EN-US"}**[ *pri2-value*]{lang="EN-US"}]{#struct_0_19838_x1039_x1776380291}[：表示时钟的优先级二。]{style="font-family:宋体"}*[pri2-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[优先级二的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，数值越小优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x510749768}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x909638914}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365000874}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x1954458671}[配置本地时钟的优先级一值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_487550179}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp priority clock-source local priority1 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2104142723}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_1329802704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x552788978}
:::

::: {#-1144791783 .myid}
[]{#_Toc304915260}[]{#_Toc404796744}[]{#struct_0_19838_x1039_1107793796}

**PTP \-- PTP配置命令 \-- ptp profile**

------------------------------------------------------------------------

[**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_x1110724889}[命令用来配置设备采用的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议标准。]{style="font-family:宋体"}

[**[undo ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_1365197482}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2055044126}

[**[ptp]{lang="EN-US"}**[ **profile** { **1588v2** \| **8021as** }]{lang="EN-US"}]{#struct_0_19838_x1039_x1221256142}

[**[undo]{lang="EN-US"}**[ **ptp** **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x447961908}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2115143246}

[[未配置设备采用的]{style="font-family:宋体"}[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_x1650091410}[协议标准，]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议不运行。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_440544587}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x275687819}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365131946}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1575303092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1054494688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1232645591}

[**[1588v2]{lang="EN-US"}**]{#struct_0_19838_x1039_965744667}[：表示采用的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议标准为]{style="font-family:宋体"}[IEEE 1588 version 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[8021as]{lang="EN-US"}**]{#struct_0_19838_x1039_1018070673}[：表示采用的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议标准为]{style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_997852458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须首先配置设备支持的]{style="font-family:宋体"}]{#struct_0_19838_x1039_1210721520}[PTP]{lang="EN-US"}[协议标准，否则不允许执行其他]{style="font-family:宋体"}[PTP]{lang="EN-US"}[配置命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当改变或取消设备采用的]{style="font-family:宋体"}]{#struct_0_19838_x1039_x534802389}[PTP]{lang="EN-US"}[协议标准时，]{style="font-family:宋体"}[PTP]{lang="EN-US"}[功能不工作，将会清空用户在之前]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议标准下的所有]{style="font-family:宋体"}[PTP]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364673191}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_723890530}[配置设备采用的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议标准为]{style="font-family:宋体"}[IEEE 1588 version 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x1366444681}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}
:::

::: {#-1812690354 .myid}
[]{#_Toc404796745}[]{#struct_0_19838_x1039_x265316804}

**PTP \-- PTP配置命令 \-- ptp slave-only**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **slave-only**]{lang="EN-US"}]{#struct_0_19838_x1039_1741675653}[命令用来配置]{style="font-family:宋体"}[OC]{lang="EN-US"}[的工作模式为]{style="font-family:宋体"}[Slave-only]{lang="EN-US"}[，即]{style="font-family:宋体"}[OC]{lang="EN-US"}[只能作为从时钟。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **slave-only**]{lang="EN-US"}]{#struct_0_19838_x1039_x960305729}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_844982252}

[**[ptp]{lang="EN-US"}**[ **slave-only**]{lang="EN-US"}]{#struct_0_19838_x1039_811234607}

[**[undo]{lang="EN-US"}**[ **ptp** **slave-only**]{lang="EN-US"}]{#struct_0_19838_x1039_1364607655}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1095599042}

[[OC]{lang="EN-US"}]{#struct_0_19838_x1039_1527987859}[的工作模式不是]{style="font-family:宋体"}[Slave-only]{lang="EN-US"}[，即]{style="font-family:宋体"}[OC]{lang="EN-US"}[既可作为主时钟也可作为从时钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x959267296}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_1121042849}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x628155110}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1400986878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1847830045}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_454922450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_1364804263}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当设备的时钟节点类型为]{style="font-family:宋体"}]{#struct_0_19838_x1039_734078262}[OC]{lang="EN-US"}[时，才允许配置该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[OC]{lang="EN-US"}]{#struct_0_19838_x1039_502087763}[的工作模式为]{lang="EN-US" style="font-family:宋体"}[Slave-only]{lang="EN-US"}[时，也允许将其]{lang="EN-US" style="font-family:宋体"}[PTP]{lang="EN-US"}[接口强制配置为]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[端口或]{lang="EN-US" style="font-family:宋体"}[Passive]{lang="EN-US"}[端口，通过]{lang="EN-US" style="font-family:宋体"}**[ptp force-state]{lang="EN-US"}**[命令进行生效配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x422662950}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1130949331}[配置设备的时钟节点类型为]{style="font-family:宋体"}[OC]{lang="EN-US"}[，并配置其工作模式为]{style="font-family:宋体"}[Slave-only]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x158514128}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp slave-only]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1391665148}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp force-state]{lang="EN-US"}**]{#struct_0_19838_x1039_1006089784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_1364738727}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_1144499861}
:::

::: {#-1155245561 .myid}
[]{#_Toc304915261}[]{#_Toc404796746}[]{#struct_0_19838_x1039_747723971}[]{#_Toc345342972}[]{#_Toc345343038}

**PTP \-- PTP配置命令 \-- ptp source**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_19838_x1039_x1067712053}[命令用来配置采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）封装格式的组播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_19838_x1039_1626530875}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1979370695}

[**[ptp]{lang="EN-US"}**[ **source** *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x1039_x2017448014}

[**[undo]{lang="EN-US"}**[ **ptp** **source** *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x1039_x1683123954}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364935335}

[[未配置采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_19838_x1039_1495439787}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）封装格式的组播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_63389374}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_1102882479}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1863334321}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x238475683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x177824876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_853267820}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x1039_994956121}[：表示采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）封装格式的组播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19838_x1039_1364869799}[：指定本端设备和对端设备通信时使用的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示对端设备位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1469159098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1408687255}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_1573065806}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令在]{style="font-family:宋体"}]{#struct_0_19838_x1039_x2132940294}[PTP]{lang="EN-US"}[报文]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式]{style="font-family:宋体"}[时才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1058335279}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_446619180}[配置采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）封装格式的组播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.5.1.5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1365066407}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp source 3.5.1.5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x462745746}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_1314482282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_x620749965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp transport-protocol]{lang="EN-US"}**]{#struct_0_19838_x1039_x1647699217}
:::

::: {#-1725020127 .myid}
[]{#_Toc404796747}[]{#struct_0_19838_x1039_x25672414}

**PTP \-- PTP配置命令 \-- ptp syn-interval**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **syn-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_868687932}[命令用来配置]{style="font-family:宋体"}[Sync]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **syn-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_x1100389945}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365000871}

[**[ptp]{lang="EN-US"}**[ **syn-interval** *value*]{lang="EN-US"}]{#struct_0_19838_x1039_x1954655279}

[**[undo]{lang="EN-US"}**[ **ptp** **syn-interval**]{lang="EN-US"}]{#struct_0_19838_x1039_x623898185}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2090903227}

[[不同]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x961221360}[的缺省情况不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_454137143}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 1588 ]{lang="EN-US"}[v]{lang="EN-US"}[ersion 2]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[Sync]{lang="EN-US"}[报文的发送周期为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[（即]{lang="EN-US" style="font-family:宋体"}[2^0^]{lang="EN-US"}[）秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_1150526285}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[Sync]{lang="EN-US"}[报文的发送周期为]{lang="EN-US" style="font-family:宋体"}[1/8]{lang="EN-US"}[（即]{lang="EN-US" style="font-family:宋体"}[2^-3^]{lang="EN-US"}[）秒。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_412444884}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_x1686911939}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365197479}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x2055502867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1972620304}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1104923451}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x1039_x1473246249}[：]{style="font-family:宋体"}[Sync]{lang="EN-US"}[报文的发送周期＝]{style="font-family:宋体"}[2*^value^*]{lang="EN-US"}[，单位为秒，当]{style="font-family:宋体"}[profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[-4]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[；当]{style="font-family:
宋体"}[profile]{lang="EN-US"}[为]{style="font-family:宋体"}[IEEE 1588 version 2]{lang="EN-US"}[时，]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[-1]{lang="EN-US"}[～]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1899375042}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_1290712733}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1098223847}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1365131943}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Sync]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[2]{lang="EN-US"}[（即]{style="font-family:宋体"}[2^1^]{lang="EN-US"}[）秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x1575106484}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp syn-interval 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_645335942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x640141528}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x1522301593}
:::

::: {#1365054246 .myid}
[]{#_Toc404796748}[]{#struct_0_19838_x1039_x173658684}[]{#_Toc385854914}[]{#_Toc383589570}

**PTP \-- PTP配置命令 \-- ptp tod**

------------------------------------------------------------------------

[**[ptp tod]{lang="FR"}**]{#struct_0_19838_x1039_764370417}[命令用来配置]{style="font-family:宋体"}[ToD]{lang="FR"}[时钟信号的方向和收发时延校正时间。]{style="font-family:宋体"}

[**[undo ]{lang="FR"}**]{#struct_0_19838_x1039_x858958053}**[ptp tod]{lang="FR"}**[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x577401960}

[**[ptp ]{lang="FR"}**]{#struct_0_19838_x1039_1760398825}[{ **tod0** \| **tod1** } { **input** \[ **delay** *input-delay-time* \] \| **output** \[ **delay** *output-delay-time* \] }]{lang="FR"}

[**[undo ptp ]{lang="FR"}**]{#struct_0_19838_x1039_390115092}[{ **tod0** \| **tod1** } { **input** \| **output** }]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_943528779}

[[ToD]{lang="EN-US"}]{#struct_0_19838_x1039_701486363}[时钟信号方向]{style="font-family:宋体"}[为入方向，收发时延校正时间为[0]{lang="EN-US"}]{style="font-family:宋体"}[纳秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2063568595}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x577467496}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1011304846}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1956063312}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_716505212}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1472453766}

[**[tod0]{lang="FR"}**]{#struct_0_19838_x1039_1914733342}[：]{style="font-family:宋体"}[第一路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[tod1]{lang="FR"}**]{#struct_0_19838_x1039_x349395209}[：第二路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟]{style="font-family:宋体"}[。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[input]{lang="SV"}**]{#struct_0_19838_x1039_x577270888}[：时钟信号方向为入方向，即此时设备接收外部时间信号]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[*[input-delay-time]{lang="FR"}*]{#struct_0_19838_x1039_x1755905580}[：]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟信号的接收延迟校正时间，]{style="font-family:宋体"}[单位为纳秒，取值范围]{style="font-family:宋体"}[与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[**[output]{lang="FR"}**]{#struct_0_19838_x1039_419842001}[：]{style="font-family:宋体"}[时钟信号方向为出方向，即此时设备向外提供时间信号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[output-delay-time]{lang="FR"}*]{#struct_0_19838_x1039_210584623}[：]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟信号的发送延迟校正时间，]{style="font-family:宋体"}[单位为纳秒，取值范围]{style="font-family:宋体"}[与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2097676186}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x586140260}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1587133340}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x577336424}[配置]{style="font-family:宋体"}[PTP]{lang="FR"}[第一路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟信号为入方向、接收时延校正时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[纳秒，]{style="font-family:宋体"}[第二路]{style="font-family:宋体"}[ToD]{lang="EN-US"}[时钟信号为出方向、发送时延校正时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[纳秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x569917987}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp tod0 input delay 1000]{lang="EN-US"}

[\[Sysname\] ptp tod1 output delay 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1404195309}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x1893242158}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x508539329}
:::

::: {#554664590 .myid}
[]{#_Toc304915262}[]{#_Toc404796749}[]{#struct_0_19838_x1039_x77115560}

**PTP \-- PTP配置命令 \-- ptp transport-protocol**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **transport-protocol**]{lang="EN-US"}]{#struct_0_19838_x1039_x742039604}[命令用来配置当前接口的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）格式。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **transport-protocol**]{lang="EN-US"}]{#struct_0_19838_x1039_1364673192}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_724087138}

[**[ptp]{lang="EN-US"}**[ **transport-protocol udp**]{lang="EN-US"}]{#struct_0_19838_x1039_x867917845}

[**[undo]{lang="EN-US"}**[ **ptp** **transport-protocol**]{lang="EN-US"}]{#struct_0_19838_x1039_x146779678}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x589550877}

[[PTP]{lang="EN-US"}]{#struct_0_19838_x1039_935937231}[报文的封装格式为]{style="font-family:宋体"}[IEEE 802.3/Ethernet]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1093314041}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19838_x1039_400114056}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1418399364}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1364607656}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1095664578}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1076505296}

[**[udp]{lang="EN-US"}**]{#struct_0_19838_x1039_694063678}[：表示配置接口下]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1179085185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x871722288}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1562645536}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1881514752}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1947407544}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文封装格式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1364804264}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp transport-protocol udp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_734143798}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x1020796323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x1026713688}
:::

::: {#1569373447 .myid}
[]{#_Toc404796750}[]{#struct_0_19838_x1039_x577533032}[]{#_Toc385854916}[]{#_Toc383589572}

**PTP \-- PTP配置命令 \-- ptp unicast-destination**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **unicast-destination**]{lang="EN-US"}]{#struct_0_19838_x1039_x564627717}[命令用来配置]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式的单播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **unicast-destination**]{lang="EN-US"}]{#struct_0_19838_x1039_x999009853}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x66974775}

[**[ptp]{lang="EN-US"}**[ **unicast-destination** *ip-address*]{lang="EN-US"}]{#struct_0_19838_x1039_x577598568}

[**[undo]{lang="EN-US"}**[ **ptp** **unicast-destination** *ip-address*]{lang="EN-US"}]{#struct_0_19838_x1039_1816944013}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_81188459}

[[未配置采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_19838_x1039_920605706}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式的单播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x297754807}

[[三层以太网接口视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_11335860}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x44164059}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x576877672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_2132625928}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_587776467}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x1039_x1131874539}[：表示]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式的单播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x167574112}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x38734958}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1776544684}[为]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1AS]{lang="EN-US"}[时，不允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令在]{style="font-family:宋体"}]{#struct_0_19838_x1039_x576943208}[PTP]{lang="EN-US"}[报文]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式]{style="font-family:宋体"}[时才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x956008578}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_447977082}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）]{style="font-family:宋体"}[封装格式的单播]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.10.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x950787993}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp transport-protocol udp]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp unicast-destination 10.10.10.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x616250760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_330945012}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x1047847958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp transport-protocol]{lang="EN-US"}**]{#struct_0_19838_x1039_x577401959}
:::

::: {#607177758 .myid}
[]{#_Toc404796751}[]{#struct_0_19838_x1039_x1776061846}

**PTP \-- PTP配置命令 \-- ptp utc**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **utc**]{lang="EN-US"}]{#struct_0_19838_x1039_1521228653}[命令用来配置]{style="font-family:宋体"}[UTC]{lang="EN-US"}[的校正日期。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ptp** **utc**]{lang="EN-US"}]{#struct_0_19838_x1039_x560604930}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1364738728}

[**[ptp]{lang="EN-US"}**[ **utc** { **leap59-date** \| **leap61-date** } *date*]{lang="EN-US"}]{#struct_0_19838_x1039_1145220757}

[**[undo]{lang="EN-US"}**[ **ptp** **utc** { **leap59-date** \| **leap61-date** }]{lang="EN-US"}]{#struct_0_19838_x1039_x1187691493}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1140688251}

[[没有配置]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1434559809}[UTC]{lang="EN-US"}[的校正日期。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1768154185}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x272947696}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_404965876}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1299065745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1364935336}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1495636395}

[**[leap59-date]{lang="EN-US"}**]{#struct_0_19838_x1039_x748207704}[：表示在指定日期的最后一分钟（]{style="font-family:宋体"}[23]{lang="EN-US"}[点]{style="font-family:宋体"}[59]{lang="EN-US"}[分）对当前设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[进行校正，使其比]{style="font-family:宋体"}[TAI]{lang="EN-US"}[慢一秒。]{style="font-family:宋体"}

[**[leap61-date]{lang="EN-US"}**]{#struct_0_19838_x1039_85182884}[：表示在指定日期的最后一分钟（]{style="font-family:宋体"}[23]{lang="EN-US"}[点]{style="font-family:宋体"}[59]{lang="EN-US"}[分）对当前设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[进行校正，使其比]{style="font-family:宋体"}[TAI]{lang="EN-US"}[快一秒。]{style="font-family:宋体"}

[*[date]{lang="EN-US"}*]{#struct_0_19838_x1039_1333500683}[：表示指定日期，格式为]{style="font-family:宋体"}[YYYY/MM/DD]{lang="EN-US"}[。]{style="font-family:宋体"}[YYYY]{lang="EN-US"}[表示年，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[；]{style="font-family:宋体"}[MM]{lang="EN-US"}[表示月，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[；]{style="font-family:宋体"}[DD]{lang="EN-US"}[表示日，取值范围取决于所输入的月份。指定日期请不要早于系统的当前日期，否则配置将不会生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1557992576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先配置]{lang="EN-US" style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_1293105848}[和]{lang="EN-US" style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[leap59]{lang="EN-US"}]{#struct_0_19838_x1039_x2006337949}[和]{style="font-family:宋体"}[leap61]{lang="EN-US"}[的配置不能够同时存在，后配置的会覆盖前面的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2138691348}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_1364869800}[假设系统的当前日期为]{style="font-family:宋体"}[2010]{lang="EN-US"}[年]{style="font-family:宋体"}[8]{lang="EN-US"}[月]{style="font-family:
宋体"}[8]{lang="EN-US"}[日，配置设备的时钟节点类型为]{style="font-family:宋体"}[BC]{lang="EN-US"}[，并指定在]{style="font-family:宋体"}[2010]{lang="EN-US"}[年]{style="font-family:宋体"}[12]{lang="EN-US"}[月]{style="font-family:宋体"}[31]{lang="EN-US"}[日的最后一分钟对当前设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[进行校正，使其比]{style="font-family:宋体"}[TAI]{lang="EN-US"}[慢一秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x361749881}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode bc]{lang="EN-US"}

[\[Sysname\] ptp utc leap59-date 2010/12/31]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x108924622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_19838_x1039_1829225521}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x851323313}
:::

::: {#-1734826423 .myid}
[]{#_Toc404796752}[]{#struct_0_19838_x1039_x83979176}[]{#_Toc304915263}

**PTP \-- PTP配置命令 \-- ptp utc offset**

------------------------------------------------------------------------

[**[ptp]{lang="EN-US"}**[ **utc** **offset**]{lang="EN-US"}]{#struct_0_19838_x1039_2024762905}[命令用来配置]{style="font-family:宋体"}[UTC]{lang="EN-US"}[相对于]{style="font-family:宋体"}[TAI]{lang="EN-US"}[的累计偏移量。]{style="font-family:宋体"}

[**[undo ptp]{lang="EN-US"}**[ **utc** **offset**]{lang="EN-US"}]{#struct_0_19838_x1039_1365066408}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x463466642}

[**[ptp]{lang="EN-US"}**[ **utc** **offset** *utc-offset*]{lang="EN-US"}]{#struct_0_19838_x1039_x1045898006}

[**[undo]{lang="EN-US"}**[ **ptp** **utc** **offset**]{lang="EN-US"}]{#struct_0_19838_x1039_x742567579}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x685585876}

[[UTC]{lang="EN-US"}]{#struct_0_19838_x1039_2106559446}[相对于]{style="font-family:宋体"}[TAI]{lang="EN-US"}[的累计偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x412208893}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x432507190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1094548308}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1365000872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_x1954589743}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x177865523}

[*[utc-offset]{lang="EN-US"}*]{#struct_0_19838_x1039_2073321686}[：表示当前设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[相对于]{style="font-family:宋体"}[TAI]{lang="EN-US"}[的累计偏移量，单位为秒，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1387154608}

[[必须先配置]{style="font-family:宋体"}[PTP profile]{lang="EN-US"}]{#struct_0_19838_x1039_x1878304330}[和]{style="font-family:宋体"}[PTP mode]{lang="EN-US"}[后，才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_2093847131}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_451067842}[配置]{style="font-family:宋体"}[UTC]{lang="EN-US"}[相对于]{style="font-family:宋体"}[TAI]{lang="EN-US"}[的累计偏移量为]{style="font-family:宋体"}[33]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_1365197480}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] ptp utc offset 33]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x2054913054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x1053790339}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ptp profile]{lang="EN-US"}**]{#struct_0_19838_x1039_1427335152}
:::

::: {#-2080262825 .myid}
[]{#_Toc404796753}[]{#struct_0_19838_x1039_x577729639}[]{#_Toc385854919}[]{#_Toc383589575}

**PTP \-- PTP配置命令 \-- ptp vlan**

------------------------------------------------------------------------

[**[ptp vlan]{lang="FR"}**]{#struct_0_19838_x1039_1070328107}[命令用来配置]{style="font-family:宋体"}[PTP]{lang="EN-US"}[报文]{style="font-family:宋体"}[的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ]{lang="FR"}**]{#struct_0_19838_x1039_1889964114}**[ptp vlan]{lang="FR"}**[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_370493624}

[**[ptp vlan ]{lang="FR"}**]{#struct_0_19838_x1039_122946450}*[vlan-id]{lang="FR"}***[ ]{lang="FR"}**[\[ **dot1p** *dot1p-value* \]]{lang="FR"}

[**[undo ptp vlan ]{lang="FR"}**]{#struct_0_19838_x1039_73490672}[\[ **dot1p** \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x1039_285142092}

[[PTP]{lang="FR"}]{#struct_0_19838_x1039_1899108630}[报文不带]{style="font-family:宋体"}[VLAN Tag]{lang="FR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_960082869}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x577533031}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x564562181}

[[network-admin]{lang="FR"}]{#struct_0_19838_x1039_x2132604318}

[[mdc-admin]{lang="FR"}]{#struct_0_19838_x1039_x67351711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1045018267}

[**[vlan]{lang="FR"}**]{#struct_0_19838_x1039_x1161918938}*[ vlan-id]{lang="FR"}*[：]{style="font-family:宋体"}[VLAN]{lang="FR"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同]{style="font-family:宋体"}[，]{style="font-family:宋体"}[请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[dot1p ]{lang="FR"}**]{#struct_0_19838_x1039_x1025777956}*[dot1p-value]{lang="FR"}*[：]{style="font-family:
宋体"}[802.1p]{lang="FR"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[7]{lang="FR"}[。如果未指定本参数，表示]{style="font-family:宋体"}[802.1p]{lang="FR"}[优先级为]{style="font-family:宋体"}[7]{lang="FR"}[，即最高优先级。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1608489168}

[[必须先配置]{style="font-family:宋体"}]{#struct_0_19838_x1039_1532443862}[PTP profile]{lang="FR"}[和]{style="font-family:宋体"}[PTP mode]{lang="FR"}[后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[才允许配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x577598567}

[[\# ]{lang="FR"}]{#struct_0_19838_x1039_1817271693}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上配置]{style="font-family:宋体"}[PTP]{lang="FR"}[报文的]{style="font-family:宋体"}[VLAN ID]{lang="FR"}[为]{style="font-family:宋体"}[2]{lang="FR"}[、]{style="font-family:
宋体"}[802.1p]{lang="FR"}[优先级为]{style="font-family:宋体"}[6]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x1039_x1039167293}

[\[Sysname\] ptp profile 1588v2]{lang="EN-US"}

[\[Sysname\] ptp mode oc]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ptp vlan 2 dot1p 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x51621605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_19838_x1039_x2070889683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ptp mode]{lang="EN-US"}**]{#struct_0_19838_x1039_x1554391675}
:::

::: {#-800427886 .myid}
[]{#_Toc404796754}[]{#struct_0_19838_x1039_x1467754961}[]{#_Toc304915264}

**PTP \-- PTP配置命令 \-- reset ptp statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **ptp statistics**]{lang="EN-US"}]{#struct_0_19838_x1039_1632553722}[命令用来清除]{style="font-family:宋体"}[PTP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_712476948}

[**[reset]{lang="EN-US"}**[ **ptp** **statistics** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_19838_x1039_x954649856}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1365131944}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19838_x1039_x1575434164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x646243758}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x1039_29924365}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x1039_1628778953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x1039_85842001}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_19838_x1039_170551424}[：清除指定接口上的统计信息。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。若未指定接口类型和接口编号，将清除所有接口上的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x1039_x1456212562}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x1039_x1522305436}[]{#_Toc139807263}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[PTP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_19838_x1039_x1364210160}[]{#_Toc139807265}[reset ptp statistics interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x1039_1142835523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ptp statistics]{lang="EN-US"}**]{#struct_0_19838_x1039_922936575}

[ ]{lang="EN-US"}
:::
