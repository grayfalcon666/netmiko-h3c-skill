::: {#-1240429183 .myid}
[]{#_Toc363740041}[]{#_Toc174161344}[]{#_Toc404794740}[]{#struct_0_x1608_14494_x421343688}[]{#_Toc366846414}[]{#_Toc366658786}[]{#_Toc366658522}[]{#_Toc366658548}[]{#_Toc366658573}[]{#_Toc366658585}[]{#_Toc366658597}[]{#_Toc366658624}[]{#_Toc366658787}[]{#_Toc366658523}[]{#_Toc366658549}[]{#_Toc366658574}[]{#_Toc366658586}[]{#_Toc366658598}[]{#_Toc366658625}[]{#_Toc366658788}[]{#_Toc366658524}[]{#_Toc366658550}[]{#_Toc366658575}[]{#_Toc366658587}[]{#_Toc366658599}[]{#_Toc366658626}[]{#_Toc366658789}[]{#_Toc366658525}[]{#_Toc366658551}[]{#_Toc366658576}[]{#_Toc366658588}[]{#_Toc366658600}[]{#_Toc366658627}[]{#_Toc366658790}[]{#_Toc366658526}[]{#_Toc366658552}[]{#_Toc366658577}[]{#_Toc366658589}[]{#_Toc366658601}[]{#_Toc366658628}[]{#_Toc366658791}[]{#_Toc366658590}[]{#_Toc366658602}[]{#_Toc366658629}[]{#_Toc366658792}[]{#_Toc366658793}

**AP管理 \-- AP管理调试命令 \-- debugging wlan ap**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1608_14494_x208937494}

[**[debugging wlan ap ]{lang="EN-US"}**[{ **all** \| **name** *ap-name* \| **serial-id** *serial-id* \| **mac-address** *mac-address* } { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1608_14494_x452702303}

[**[undo debugging wlan ap ]{lang="EN-US"}**[{ **all \| name** *ap-name* \| **serial-id** *serial-id* \| **mac-address** *mac-address* \| { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1608_14494_1734150518}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1608_14494_x831318790}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1608_14494_x602765549}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1608_14494_1639987343}

[[network-admin]{lang="EN-US"}]{#struct_0_x1608_14494_656848422}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1608_14494_1436551116}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1608_14494_610312158}

[**[all]{lang="EN-US"}**]{#struct_0_x1608_14494_1452636839}[：表示所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x1660140932}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称。]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[serial-id]{lang="EN-US"}**[ *serial-id*]{lang="EN-US"}]{#struct_0_x1608_14494_1479606693}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的序列号。]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[AP]{lang="EN-US"}[的序列号，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_x1608_14494_622391406}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，输入格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1608_14494_2049655960}[：表示]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1608_14494_x552376022}[：表示]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[错误类型调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1608_14494_779433635}[：表示]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[事件类型调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1608_14494_2024810494}

[**[debugging wlan ap]{lang="EN-US"}**]{#struct_0_x1608_14494_470165088}[命令用来打开]{style="font-family:宋体"}[AP]{lang="EN-US"}[上]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging wlan ap]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[AP]{lang="EN-US"}[上]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1942745180}[上]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan ap all event]{lang="EN-US"}]{#struct_0_x1608_14494_x255991661}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1475675333}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_x230457779}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1918272711}

[[Created AP *ap-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_x1820779472}

[[成功创建名称为]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x78814374}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[[Deleted AP *ap-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_1223151559}

[[成功删除名称为]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_1226090593}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[[Synchronized AP information]{lang="EN-US"}]{#struct_0_x1608_14494_x1660140929}

[[同步数据结束]{style="font-family:宋体"}]{#struct_0_x1608_14494_x892980766}

[[Sent message to the kernel]{lang="EN-US"}]{#struct_0_x1608_14494_1754736260}

[[下发消息至内核]{style="font-family:宋体"}]{#struct_0_x1608_14494_x1660140928}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan ap all error]{lang="EN-US"}]{#struct_0_x1608_14494_x733299445}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1468723337}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_x706866647}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1910102807}

[[Failed to open APDB user script.]{lang="EN-US"}]{#struct_0_x1608_14494_x1647764528}

[[打开]{style="font-family:宋体"}[APDB]{lang="EN-US"}]{#struct_0_x1608_14494_1169906095}[用户脚本失败]{style="font-family:宋体"}

[[Failed to decode APDB user script.]{lang="EN-US"}]{#struct_0_x1608_14494_x223015344}

[[解析]{style="font-family:宋体"}[APDB]{lang="EN-US"}]{#struct_0_x1608_14494_1174100608}[用户脚本失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1608_14494_1267063383}

[[\# ]{lang="EN-US" style="color:black"}]{#struct_0_x1608_14494_1218359701}[打开所有]{style="font-family:宋体;color:black"}[AP]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;color:black"}[WLAN]{lang="EN-US" style="color:black"}[模块的事件调试信息开关，创建手工]{style="font-family:宋体;
color:black"}[AP]{lang="EN-US" style="color:black"}[后，会有如下调试信息。]{style="font-family:宋体;color:black"}

[[\<Sysname\> debugging wlan ap all event]{lang="EN-US"}]{#struct_0_x1608_14494_825570693}

[\<Sysname\> system view]{lang="EN-US"}

[\[Sysname\] wlan ap ap1 model WA2100]{lang="EN-US"}

[\*Jul 25 14:20:35:749 2013 H3C APMGR/7/Event: -MDC=1; Created AP ap1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1608_14494_x1693875470}*[成功创建一个手工]{style="font-family:宋体"}[AP]{lang="EN-US"}[，]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称为]{style="font-family:宋体"}[ap1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1608_14494_x391983333}[打开所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[上]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[模块的事件调试信息开关，删除手工]{style="font-family:宋体"}[AP]{lang="EN-US"}[后，会有如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging wlan ap all event]{lang="EN-US"}]{#struct_0_x1608_14494_x2120890184}

[\<Sysname\> system view]{lang="EN-US"}

[\[Sysname\] undo wlan ap ap1]{lang="EN-US"}

[\*Jul 25 14:20:35:749 2013 H3C APMGR/7/Event: -MDC=1; Deleted AP ap1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1608_14494_x466734470}*[成功删除一个手工]{style="font-family:宋体"}[AP]{lang="EN-US"}[，]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称为]{style="font-family:宋体"}[ap1]{lang="EN-US"}*

[[\# ]{lang="EN-US" style="color:black"}]{#struct_0_x1608_14494_x2085620782}[打开所有]{style="font-family:宋体;color:black"}[AP]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;color:black"}[WLAN]{lang="EN-US" style="color:black"}[模块的所有调试信息开关，删除手工]{style="font-family:宋体;
color:black"}[AP]{lang="EN-US" style="color:black"}[后，会有如下调试信息。]{style="font-family:宋体;color:black"}

[[\<Sysname\> debugging wlan ap all all]{lang="EN-US"}]{#struct_0_x1608_14494_2099029323}

[\<Sysname\> system view]{lang="EN-US"}

[\[Sysname\] undo wlan ap ap1]{lang="EN-US"}

[\*Jul 25 14:20:35:749 2013 H3C APMGR/7/Event: -MDC=1; Deleted AP ap1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1608_14494_452473531}*[成功删除一个手工]{style="font-family:宋体"}[AP]{lang="EN-US"}[，]{style="font-family:宋体"}[AP]{lang="EN-US"}[名称为]{style="font-family:宋体"}[ap1]{lang="EN-US"}*

::: {#1145658578 .myid}
[]{#_Toc404794741}[]{#struct_0_x1608_14494_1571144049}

**AP管理 \-- AP管理调试命令 \-- debugging wlan capwap**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1608_14494_x1760884905}

[**[debugging wlan capwap]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **packet** { **control** { **receive** \| **send** } \[ **verbose** \] \| **data** } \| **timer** }]{lang="EN-US"}]{#struct_0_x1608_14494_805945375}

[**[undo debugging wlan capwap ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **packet** { **control** { **receive** \| **send** } \[ **verbose** \] \| **data** } \| **timer** }]{lang="EN-US"}]{#struct_0_x1608_14494_x1958067274}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1608_14494_1343875577}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1608_14494_x1583225598}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1608_14494_1875382128}

[[network-admin]{lang="EN-US"}]{#struct_0_x1608_14494_567484002}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1608_14494_24388252}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1608_14494_324517358}

[**[all]{lang="EN-US"}**]{#struct_0_x1608_14494_53528210}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[所有类型调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1608_14494_1614454829}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[错误类型调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1608_14494_1668273934}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[事件类型调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x1608_14494_x1238781475}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1608_14494_1770366618}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[control]{lang="EN-US"}**]{#struct_0_x1608_14494_770816081}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[控制报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1608_14494_1731201603}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[报文接收调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1608_14494_1806147777}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[报文发送调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1608_14494_x466255457}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[详细调试信息开关。]{style="font-family:宋体"}

[**[data]{lang="EN-US"}**]{#struct_0_x1608_14494_656172964}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[数据报文调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1608_14494_887817470}[：表示]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1608_14494_1023025435}

[**[debugging wlan capwap]{lang="EN-US"}**]{#struct_0_x1608_14494_1387845136}[命令用来打开]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging wlan capwap]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x1608_14494_1672985970}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap error]{lang="EN-US"}]{#struct_0_x1608_14494_133534133}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1470845341}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_x1151498220}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1654094305}

 

[[Failed to verify CAPWAP header.]{lang="EN-US"}]{#struct_0_x1608_14494_x85503324}

[[校验控制报文]{style="font-family:宋体"}[CAPWAP header]{lang="EN-US"}]{#struct_0_x1608_14494_x1499491376}[失败]{style="font-family:宋体"}

 

[[Failed to verify CAPWAP control header.]{lang="EN-US"}]{#struct_0_x1608_14494_x1287683892}

[[校验控制报文]{style="font-family:宋体"}[CAPWAP control header]{lang="EN-US"}]{#struct_0_x1608_14494_26477590}[失败]{style="font-family:宋体"}

 

[[Failed to send *MsgType* message.]{lang="EN-US"}]{#struct_0_x1608_14494_x1147712212}

[[发送]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_309571406}[类型报文失败。]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[u]{lang="EN-US"}[nknown ]{lang="EN-US"}]{#struct_0_x1608_14494_1577385135}[m]{lang="EN-US"}[essage]{lang="EN-US"}[：未知报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[iscovery ]{lang="EN-US"}]{#struct_0_x1608_14494_x1762094345}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：发现请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[iscovery ]{lang="EN-US"}]{#struct_0_x1608_14494_682346594}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：发现回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin ]{lang="EN-US"}]{#struct_0_x1608_14494_1539880970}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：加入请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin ]{lang="EN-US"}]{#struct_0_x1608_14494_1333466137}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：请求加入回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}]{#struct_0_x1608_14494_1973496674}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：配置请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}]{#struct_0_x1608_14494_844361762}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：配置回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}]{#struct_0_x1608_14494_x721938920}[u]{lang="EN-US"}[pdate ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：配置更新请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}]{#struct_0_x1608_14494_90744470}[u]{lang="EN-US"}[pdate ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：配置更新回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTP ]{lang="EN-US"}]{#struct_0_x1608_14494_803892533}[e]{lang="EN-US"}[vent ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[WTP]{lang="EN-US"}[事件请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTP ]{lang="EN-US"}]{#struct_0_x1608_14494_11301194}[e]{lang="EN-US"}[vent ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[WTP]{lang="EN-US"}[事件回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[hange ]{lang="EN-US"}]{#struct_0_x1608_14494_1224947100}[s]{lang="EN-US"}[tate ]{lang="EN-US"}[e]{lang="EN-US"}[vent ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：状态事件改变请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[hange ]{lang="EN-US"}]{#struct_0_x1608_14494_x833831394}[s]{lang="EN-US"}[tate ]{lang="EN-US"}[e]{lang="EN-US"}[vent ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：状态事件改变回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e]{lang="EN-US"}[cho ]{lang="EN-US"}]{#struct_0_x1608_14494_870805123}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：回声请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e]{lang="EN-US"}[cho ]{lang="EN-US"}]{#struct_0_x1608_14494_x1744391666}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：回声回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[mage ]{lang="EN-US"}]{#struct_0_x1608_14494_x1134322823}[d]{lang="EN-US"}[ata ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：镜像数据请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[mage ]{lang="EN-US"}]{#struct_0_x1608_14494_193983761}[d]{lang="EN-US"}[ata ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：镜像数据回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[r]{lang="EN-US"}[eset ]{lang="EN-US"}]{#struct_0_x1608_14494_x1321421247}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：重启请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[r]{lang="EN-US"}[eset ]{lang="EN-US"}]{#struct_0_x1608_14494_x1554782747}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：重启回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[p]{lang="EN-US"}[rimary ]{lang="EN-US"}]{#struct_0_x1608_14494_x1422874675}[d]{lang="EN-US"}[iscovery ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：优先发现请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[p]{lang="EN-US"}[rimary ]{lang="EN-US"}]{#struct_0_x1608_14494_x1405330337}[d]{lang="EN-US"}[iscovery ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：优先发现回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[ata ]{lang="EN-US"}]{#struct_0_x1608_14494_x1218442527}[t]{lang="EN-US"}[ransfer ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：数据传输请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[ata ]{lang="EN-US"}]{#struct_0_x1608_14494_2011628151}[t]{lang="EN-US"}[ransfer ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：数据传输回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[lear ]{lang="EN-US"}]{#struct_0_x1608_14494_1530330968}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：清除配置请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[lear ]{lang="EN-US"}]{#struct_0_x1608_14494_788731199}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：清除配置回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[tation ]{lang="EN-US"}]{#struct_0_x1608_14494_1721487919}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Station]{lang="EN-US"}[配置请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[tation ]{lang="EN-US"}]{#struct_0_x1608_14494_1328135873}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Station]{lang="EN-US"}[配置回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}]{#struct_0_x1608_14494_2143147507}[LAN]{lang="EN-US"}[ ]{lang="EN-US"}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[W]{lang="EN-US"}[LAN]{lang="EN-US"}[配置请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}]{#struct_0_x1608_14494_1684402157}[LAN]{lang="EN-US"}[ ]{lang="EN-US"}[c]{lang="EN-US"}[onfiguration ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[W]{lang="EN-US"}[LAN]{lang="EN-US"}[配置回复报文]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to match *MsgType* with SeqNum *SeqNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_x35752973}

[[匹配序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_x1608_14494_x142138714}[类型为]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的报文失败]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Received duplicate *MsgType* with SeqNum *SeqNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_1258665380}

[[收到重复的序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_x1608_14494_x1649943088}[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Received old *MsgType* with SeqNum *SeqNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_1417102894}

[[收到序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_x1608_14494_1174035072}[的旧的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x168127779}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Number of packets in the retransmission queue exceeded the limit *MaxNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_x1377939207}

[[重传队列中缓存的报文超过最大数量]{style="font-family:宋体"}*[MaxNum]{lang="EN-US"}*]{#struct_0_x1608_14494_x405424336}

 

[[Failed to retransmit *MsgType* and tore down the tunnel: Number of retransmissions exceeded the limit *RetranCnt.*]{lang="EN-US"}]{#struct_0_x1608_14494_853459919}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x392048869}[类型报文重传次数达到]{style="font-family:宋体"}*[RetranCnt]{lang="EN-US"}*[次数导致重传失败，断开隧道]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_1350598759}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Failed to retransmit *MsgType* *RetranCnt* times.]{lang="EN-US"}]{#struct_0_x1608_14494_1367066947}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1768943758}[类型报文重传次数达到]{style="font-family:宋体"}*[RetranCnt]{lang="EN-US"}*[次数导致重传失败。]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_335267664}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Failed to send fragment *FragNum* of *MsgType* with SeqNum *SeqNum* to AP at address:*port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x1958132810}

[[向地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x1608_14494_x1305781172}[端口号为]{style="font-family:宋体"}*[port ]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文的第]{style="font-family:宋体"}*[FragNum]{lang="EN-US"}*[个分片失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1158440716}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Failed to send all fragments of *MsgType* with SeqNum *SeqNum* to AP at address:*port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x680385172}

[[向地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x1608_14494_360287144}[端口号为]{style="font-family:宋体"}*[port ]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文的分片未全部成功]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_1270320790}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

 

[[Received packet fragments exceeded the upper limit.]{lang="EN-US"}]{#struct_0_x1608_14494_770750545}

[[接收报文的分片个数超过上限]{style="font-family:宋体"}]{#struct_0_x1608_14494_395596002}

 

[[Discarded a duplicate fragment.]{lang="EN-US"}]{#struct_0_x1608_14494_1797921642}

[[丢弃重复的分片]{style="font-family:宋体"}]{#struct_0_x1608_14494_381739758}

 

[[Failed to decode TLV: Invalid packet length.]{lang="EN-US"}]{#struct_0_x1608_14494_x1151563756}

[[报文长度非法，解析]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1608_14494_1786898137}[失败]{style="font-family:宋体"}

 

[[Failed to decode TLV: Type = *TlvType*, Length = *TlvLen*.]{lang="EN-US"}]{#struct_0_x1608_14494_x127413868}

[[解析类型为]{style="font-family:宋体"}*[TlvType]{lang="EN-US"}*]{#struct_0_x1608_14494_1668964143}[，长度为]{style="font-family:宋体"}*[TlvLen]{lang="EN-US"}*[的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to decode Vendor TLV: Invalid packet length.]{lang="EN-US"}]{#struct_0_x1608_14494_x37149420}

[[报文长度非法，解析]{style="font-family:宋体"}[Vendor TLV]{lang="EN-US"}]{#struct_0_x1608_14494_1577319599}[失败]{style="font-family:宋体"}

 

[[Failed to decode Vendor TLV: Element ID=*ElementID*, element Length=*ElementLen*.]{lang="EN-US"}]{#struct_0_x1608_14494_x895738963}

[[解析元素类型标识为]{style="font-family:宋体"}*[ElementID]{lang="EN-US"}*]{#struct_0_x1608_14494_905478510}[，长度为]{style="font-family:宋体"}*[ElementLen]{lang="EN-US"}*[的]{style="font-family:宋体"}[Vendor TLV]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request: WTP Model Number was not included in WTP BoardData.]{lang="EN-US"}]{#struct_0_x1608_14494_x2006844495}

[[WTP BoardData]{lang="EN-US"}]{#struct_0_x1608_14494_x763159402}[中不包含]{style="font-family:宋体"}[WTP Model Number]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Discovery Reqeust]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request: WTP Board Data has no serial ID and MAC address.]{lang="EN-US"}]{#struct_0_x1608_14494_11235658}

[[WTP BoardData]{lang="EN-US"}]{#struct_0_x1608_14494_x1310996913}[中不包含]{style="font-family:宋体"}[SerialID]{lang="EN-US"}[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，处理]{style="font-family:宋体"}[Discovery Reqeust]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: AP reported wrong radio numbers.]{lang="EN-US"}]{#struct_0_x1608_14494_1584772547}

[[序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x298676778}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[上报错误的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[个数，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unsupported hardware version.]{lang="EN-US"}]{#struct_0_x1608_14494_x1670967394}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1554848283}[不支持序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的硬件版本，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unsupported boot version.]{lang="EN-US"}]{#struct_0_x1608_14494_x701252742}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1308795}[不支持序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[上的启动文件版本，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unsupported AP.]{lang="EN-US"}]{#struct_0_x1608_14494_1530265432}

[[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1530147244}[不支持该序列号的]{style="font-family:宋体"}[AP]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unmatched model number.]{lang="EN-US"}]{#struct_0_x1608_14494_989778272}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_767528224}[不支持序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[model]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unmatched model number.]{lang="EN-US"}]{#struct_0_x1608_14494_x35818509}

[[序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_462793464}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的型号名和]{style="font-family:宋体"}[AC]{lang="EN-US"}[上配置的不符，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unsupported tunnel mode.]{lang="EN-US"}]{#struct_0_x1608_14494_1157057315}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_1207760083}[不支持序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的隧道模式，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unsupported MAC type.]{lang="EN-US"}]{#struct_0_x1608_14494_1173969536}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_385489516}[不支持序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[类型，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unsupported discovery type.]{lang="EN-US"}]{#struct_0_x1608_14494_x1468345318}

[[不支持序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x392114405}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的发现类型，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: No WTP Descriptor TLV.]{lang="EN-US"}]{#struct_0_x1608_14494_487258126}

[[序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x1651332206}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文中缺少]{style="font-family:宋体"}[WTP Descriptor TLV]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: No WTP Board Data TLV.]{lang="EN-US"}]{#struct_0_x1608_14494_x1958198346}

[[Discovery Request]{lang="EN-US"}]{#struct_0_x1608_14494_1686991041}[报文中缺少]{style="font-family:宋体"}[WTP Board Data TLV]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process fast recovery: Unmatched model.]{lang="EN-US"}]{#struct_0_x1608_14494_800647913}

[[Model]{lang="EN-US"}]{#struct_0_x1608_14494_770685009}[不匹配，处理快速恢复失败]{style="font-family:宋体"}

 

[[Failed to process fast recovery: Unmatched Serial ID.]{lang="EN-US"}]{#struct_0_x1608_14494_x394065052}

[[Serial ID]{lang="EN-US"}]{#struct_0_x1608_14494_x1198292211}[不匹配，处理快速恢复失败]{style="font-family:宋体"}

 

[[Failed to process fast recovery:Unmatched MAC address.]{lang="EN-US"}]{#struct_0_x1608_14494_x1151629292}

[[MAC Address]{lang="EN-US"}]{#struct_0_x1608_14494_1375401092}[不匹配，处理快速恢复失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id* in Run state: Invalid fast recovery.]{lang="EN-US"}]{#struct_0_x1608_14494_x1850163217}

[[由于快速回复不合法]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x1608_14494_1577254063}[在]{style="font-family:宋体"}[Run]{lang="EN-US"}[状态时处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*.]{lang="EN-US"}]{#struct_0_x1608_14494_x963377226}

[[APMGR]{lang="EN-US"}]{#struct_0_x1608_14494_1484411170}[处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Invalid AP state.]{lang="EN-US"}]{#struct_0_x1608_14494_11170122}

[[当前]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_391842866}[的状态非法，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: MAC address was already in use.]{lang="EN-US"}]{#struct_0_x1608_14494_1662296577}

[[相同的]{style="font-family:宋体"}[Mac]{lang="EN-US"}]{#struct_0_x1608_14494_x1554913819}[地址已经被使用]{style="font-family:宋体"}[,]{lang="EN-US"}[处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: AC has no available IP address.]{lang="EN-US"}]{#struct_0_x1608_14494_x1863345380}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1816291213}[没有可用的]{style="font-family:宋体"}[ip]{lang="EN-US"}[地址，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: No available AP configurations.]{lang="EN-US"}]{#struct_0_x1608_14494_912592142}

[[没有可用的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1459995317}[配置信息，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Number of APs exceeded the limit.]{lang="EN-US"}]{#struct_0_x1608_14494_x346652468}

[[超过了]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x1608_14494_1268888038}[允许上线的]{style="font-family:宋体"}[AP]{lang="EN-US"}[最大个数，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

 

[[Failed to process discovery request from AP with serial ID *serial-id*: Unknown error.]{lang="EN-US"}]{#struct_0_x1608_14494_1672172565}

[[除已知错误码外的其它问题，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_106088624}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

 

[[Failed to decode discovery request.]{lang="EN-US"}]{#struct_0_x1608_14494_x1812453435}

[[解析]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}]{#struct_0_x1608_14494_1530199896}[失败]{style="font-family:宋体"}

 

[[Failed to decode join request.]{lang="EN-US"}]{#struct_0_x1608_14494_352208175}

[[解析]{style="font-family:宋体"}[Join Request]{lang="EN-US"}]{#struct_0_x1608_14494_x685465611}[失败]{style="font-family:宋体"}

 

[[Failed to process join request: No WTP Board Data TLV in the request.]{lang="EN-US"}]{#struct_0_x1608_14494_524585969}

[[Join Request]{lang="EN-US"}]{#struct_0_x1608_14494_x35884045}[报文中缺少]{style="font-family:宋体"}[WTP Board Data TLV]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process join request from AP with serial ID *serial-id*: No WTP Descriptor TLV.]{lang="EN-US"}]{#struct_0_x1608_14494_483586824}

[[序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x1275026556}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文中缺少]{style="font-family:宋体"}[WTP Descriptor TLV]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process join request from AP with serial ID *serial-id*: No Session ID TLV.]{lang="EN-US"}]{#struct_0_x1608_14494_1173904000}

[[序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x1215822260}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文中缺少]{style="font-family:宋体"}[SessionID TLV]{lang="EN-US"}[，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process join request: WTP Board Data TLV lacks necessary sub element.]{lang="EN-US"}]{#struct_0_x1608_14494_x1572618978}

[[WTP BoardData]{lang="EN-US"}]{#struct_0_x1608_14494_x392179941}[中缺少必要子元素，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to process join request from AP with serial ID *serial-id*: Number of APs exceeded the limit.]{lang="EN-US"}]{#struct_0_x1608_14494_950078507}

[[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x301627216}[个数超过限制，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Unsupported transport protocol.]{lang="EN-US"}]{#struct_0_x1608_14494_x1958263882}

[[Transport Protocol]{lang="EN-US"}]{#struct_0_x1608_14494_720240841}[不支持，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: APMGR has no available license.]{lang="EN-US"}]{#struct_0_x1608_14494_x297195903}

[[Apmgr]{lang="EN-US"}]{#struct_0_x1608_14494_x1863279844}[进程没有可用的证书，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Not enough memory.]{lang="EN-US"}]{#struct_0_x1608_14494_x1816225677}

[[内存达到上限，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_912657678}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to process join request]{lang="EN-US"}[ from AP with serial ID *serial-id*: Invalid AP online info.]{lang="EN-US"}]{#struct_0_x1608_14494_x1459929781}

[[由于]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x1608_14494_1268953574}[检查到]{style="font-family:宋体"}[AP]{lang="EN-US"}[上线信息不合法，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to add AP running info.]{lang="EN-US"}]{#struct_0_x1608_14494_1672238101}

[[由于添加]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_106154160}[运行数据失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to apply AP group configurations.]{lang="EN-US"}]{#struct_0_x1608_14494_1726334916}

[[由于应用]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x700414894}[组配置失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to create an auto AP.]{lang="EN-US"}]{#struct_0_x1608_14494_x297130367}

[[创建自动]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_2038572444}[失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to create a CTLAP.]{lang="EN-US"}]{#struct_0_x1608_14494_x1863214308}

[[创建]{style="font-family:宋体"}[CTLAP]{lang="EN-US"}]{#struct_0_x1608_14494_x1816160141}[失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to add the AP to an AP group.]{lang="EN-US"}]{#struct_0_x1608_14494_912723214}

[[加入]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1058587317}[组失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to create AP private data.]{lang="EN-US"}]{#struct_0_x1608_14494_1670296038}

[[创建]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1341001495}[私有数据失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: MAC authentication failed.]{lang="EN-US"}]{#struct_0_x1608_14494_2073580565}

[[请求]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1608_14494_507496624}[地址认证失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Failed to create private data for CTLAP.]{lang="EN-US"}]{#struct_0_x1608_14494_1267011511}

[[创建]{style="font-family:宋体"}[CTLAP]{lang="EN-US"}]{#struct_0_x1608_14494_x299072430}[私有数据失败，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Unknown error.]{lang="EN-US"}]{#struct_0_x1608_14494_104212097}

[[除已知错误码外的其他问题，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x1461871844}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to process process join request from AP with serial ID *serial-id*: Unsupported MAC type.]{lang="EN-US"}]{#struct_0_x1608_14494_x832000425}

[[Mac Type]{lang="EN-US"}]{#struct_0_x1608_14494_770619473}[不支持，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process process join request from AP with serial ID *serial-id*: Unsupported tunnel mode.]{lang="EN-US"}]{#struct_0_x1608_14494_1148181677}

[[Tunnel mode]{lang="EN-US"}]{#struct_0_x1608_14494_1646311509}[不匹配，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process process join request from AP with serial ID *serial-id*: Session ID was already in use.]{lang="EN-US"}]{#struct_0_x1608_14494_x1151694828}

[[Session ID]{lang="EN-US"}]{#struct_0_x1608_14494_x304229117}[已被使用，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process process join request from AP with serial ID *serial-id*: Unmatched model number.]{lang="EN-US"}]{#struct_0_x1608_14494_761727538}

[[序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_1577188527}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的型号名和]{style="font-family:宋体"}[AC]{lang="EN-US"}[上配置的不符，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process process join request from AP with serial ID *serial-id*: Unmatched number of radios.]{lang="EN-US"}]{#struct_0_x1608_14494_1815121937}

[[Radio]{lang="EN-US"}]{#struct_0_x1608_14494_267620458}[个数错误，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Unsupported boot version.]{lang="EN-US"}]{#struct_0_x1608_14494_11104586}

[[启动文件错误，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x441411012}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process the second half of join request: Invalid AP ID.]{lang="EN-US"}]{#struct_0_x1608_14494_x1554979355}

[[AP ID]{lang="EN-US"}]{#struct_0_x1608_14494_x1595684280}[无效，处理]{style="font-family:宋体"}[Join request]{lang="EN-US"}[后半部分失败]{style="font-family:宋体"}

[[Failed to add an AP according to join request from AP with serial ID *serial-id*.]{lang="EN-US"}]{#struct_0_x1608_14494_1530134360}

[[根据序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*]{#struct_0_x1608_14494_x390380907}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[报文信息来添加]{style="font-family:宋体"}[AP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id* in Run state: Invalid fast recovery.]{lang="EN-US"}]{#struct_0_x1608_14494_x542300732}

[[由于快速恢复不合法，在]{style="font-family:宋体"}[Run]{lang="EN-US"}]{#struct_0_x1608_14494_x35949581}[状态下处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: Invalid AP state.]{lang="EN-US"}]{#struct_0_x1608_14494_x1520981119}

[[当前]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_271308576}[的状态非法，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: MAC address was already in use.]{lang="EN-US"}]{#struct_0_x1608_14494_1173838464}

[[相同的]{style="font-family:宋体"}[Mac]{lang="EN-US"}]{#struct_0_x1608_14494_1160220461}[地址已经被使用，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Received configuration update response with wrong error code *ResultCode* from AP *ap-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_1932481552}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x392245477}[接收到]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[回复的错误的配置更新结果码为]{style="font-family:宋体"}*[ResultCode]{lang="EN-US"}*[的]{style="font-family:宋体"}[Configuration Update Response]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Failed to decode configuration update response.]{lang="EN-US"}]{#struct_0_x1608_14494_2068611917}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1986151383}[解析]{style="font-family:宋体"}[Configuration Update Response]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to process configuration status request.]{lang="EN-US"}]{#struct_0_x1608_14494_x1958329418}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1771182557}[处理]{style="font-family:宋体"}[Configuration Status Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to decode configuration status request.]{lang="EN-US"}]{#struct_0_x1608_14494_x1409308228}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_770553937}[解析]{style="font-family:宋体"}[Configuration Status Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to decode reset response.]{lang="EN-US"}]{#struct_0_x1608_14494_1255285580}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x980099516}[解析]{style="font-family:宋体"}[Reset Response]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to create image file keep-alive timer.]{lang="EN-US"}]{#struct_0_x1608_14494_x1151760364}

[[创建]{style="font-family:宋体"}[image]{lang="EN-US"}]{#struct_0_x1608_14494_762248615}[文件保活定时器失败]{style="font-family:宋体"}

[[Failed to write message with type *type* and sub type *sub-type* to AP entity thread queue*.*]{lang="EN-US"}]{#struct_0_x1608_14494_167194684}

[[子线程写主类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x1608_14494_1577122991}[子类型为]{style="font-family:宋体"}*[sub-type]{lang="EN-US"}*[的消息到]{style="font-family:宋体"}[AP]{lang="EN-US"}[实体线程的消息队列失败]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[取值为以下两种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1608_14494_1361518100}[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[端]{lang="EN-US" style="font-family:宋体"}[Image]{lang="EN-US"}[模块消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1608_14494_632794705}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[端]{lang="EN-US" style="font-family:宋体"}[Image]{lang="EN-US"}[模块消息]{lang="EN-US" style="font-family:宋体"}

[*[sub-type]{lang="EN-US"}*]{#struct_0_x1608_14494_11039050}[取值为以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1608_14494_857037613}[：]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[读镜像文件请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1608_14494_956041873}[：]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[写镜像文件请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1608_14494_x1555044891}[：]{style="font-family:宋体"}[LWAPP]{lang="EN-US"}[读镜像文件请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1608_14494_x1128815465}[：]{style="font-family:宋体"}[LWAPP]{lang="EN-US"}[读镜像文件请求]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x1608_14494_1530068824}[：]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[读镜像文件回复]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x1608_14494_x1179469324}[：]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[读镜像文件回复]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1608_14494_74120847}[：]{style="font-family:宋体"}[LWAPP]{lang="EN-US"}[读镜像文件回复]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1608_14494_x36015117}[：]{style="font-family:宋体"}[LWAPP]{lang="EN-US"}[读镜像文件回复]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x1608_14494_x969042601}[：文件线程退出]{lang="EN-US" style="font-family:宋体"}

[[Failed to write message with type *type* and sub type *sub-type to* file thread queue.]{lang="EN-US"}]{#struct_0_x1608_14494_1173772928}

[[AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1961812514}[实体线程写主类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[子类型为]{style="font-family:宋体"}*[sub-type]{lang="EN-US"}*[的消息到文件线程的消息队列失败]{style="font-family:宋体"}

[*[type]{lang="EN-US"}*]{#struct_0_x1608_14494_514824388}[、]{style="font-family:宋体"}*[sub-type]{lang="EN-US"}*[的取值请参见]{style="font-family:宋体"}[Failed to write entity-thread queue type *type* by sub-type *sub-type*]{lang="EN-US"}[中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[、]{style="font-family:宋体"}*[sub-type]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[[Failed to get current directory.]{lang="EN-US"}]{#struct_0_x1608_14494_x392311013}

[[获取当前工作路径失败]{style="font-family:宋体"}]{#struct_0_x1608_14494_492548394}

[[Failed to allocate memory for image file *file-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_821591350}

[[为文件名为的]{style="font-family:宋体"}*[file-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x1958394954}[的]{style="font-family:宋体"}[Image]{lang="EN-US"}[文件内存分配失败]{style="font-family:宋体"}

[[Failed to read image file *file-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_1247369725}

[[读取文件名为]{style="font-family:宋体"}*[file-name]{lang="EN-US"}*]{#struct_0_x1608_14494_770488401}[的]{style="font-family:宋体"}[Image]{lang="EN-US"}[文件失败]{style="font-family:宋体"}

[[Failed to open image file *file-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_1691868632}

[[打开文件名为]{style="font-family:宋体"}*[file-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x1352158513}[的]{style="font-family:宋体"}[Image]{lang="EN-US"}[文件打开失败]{style="font-family:宋体"}

[[Failed to exit file thread.]{lang="EN-US"}]{#struct_0_x1608_14494_x1151825900}

[[文件线程退出失败]{style="font-family:宋体"}]{#struct_0_x1608_14494_x1406596279}

[[Failed to create file thread.]{lang="EN-US"}]{#struct_0_x1608_14494_x2101825307}

[[文件线程创建失败]{style="font-family:宋体"}]{#struct_0_x1608_14494_1577057455}

[[Failed to initiate file thread.]{lang="EN-US"}]{#struct_0_x1608_14494_1000963090}

[[文件线程初始化失败]{style="font-family:宋体"}]{#struct_0_x1608_14494_10973514}

[[Failed to download image file *file-name* for AP *ap-name*.]{lang="EN-US"}]{#struct_0_x1608_14494_1003869272}

[[Image]{lang="EN-US"}]{#struct_0_x1608_14494_x1098695590}[文件下载失败]{style="font-family:宋体"}

[[Failed to decode image data request.]{lang="EN-US"}]{#struct_0_x1608_14494_x1555110427}

[[Image Data Request]{lang="EN-US"}]{#struct_0_x1608_14494_x142035536}[解析失败]{style="font-family:宋体"}

[[Received invalid image data request.]{lang="EN-US"}]{#struct_0_x1608_14494_923251354}

[[收到无效的]{style="font-family:宋体"}[Image Data Request]{lang="EN-US"}]{#struct_0_x1608_14494_1530003288}[报文]{style="font-family:宋体"}

[[Number of images downloaded at the same time exceeded the limit.]{lang="EN-US"}]{#struct_0_x1608_14494_x1966962259}

[[超出]{style="font-family:宋体"}[Image]{lang="EN-US"}]{#struct_0_x1608_14494_x36080653}[下载上限]{style="font-family:宋体"}

[[Failed to process image data request.]{lang="EN-US"}]{#struct_0_x1608_14494_x980689557}

[[Image Data Request]{lang="EN-US"}]{#struct_0_x1608_14494_1963594994}[处理失败]{style="font-family:宋体"}

[[Failed to decode image data response.]{lang="EN-US"}]{#struct_0_x1608_14494_1307990656}

[[Image Data Response]{lang="EN-US"}]{#struct_0_x1608_14494_x479583544}[解析失败]{style="font-family:宋体"}

[[Received invalid image data response.]{lang="EN-US"}]{#struct_0_x1608_14494_x258093285}

[[收到无效的]{style="font-family:宋体"}[Image Data Response]{lang="EN-US"}]{#struct_0_x1608_14494_1454478284}[报文]{style="font-family:宋体"}

[[Failed to process image data response.]{lang="EN-US"}]{#struct_0_x1608_14494_x1824177226}

[[Image Data Response]{lang="EN-US"}]{#struct_0_x1608_14494_1448359600}[处理失败]{style="font-family:宋体"}

[[Failed to send data channel keep-alive message.]{lang="EN-US"}]{#struct_0_x1608_14494_904706129}

[[发送数据隧道保活报文失败]{style="font-family:宋体"}]{#struct_0_x1608_14494_x1487284736}

[[Failed to process data channel keep-alive message: Session ID TLV didn\'t exist.]{lang="EN-US"}]{#struct_0_x1608_14494_x1017608172}

[[处理数据隧道保活报文失败，]{style="font-family:宋体"}[Session ID TLV]{lang="EN-US"}]{#struct_0_x1608_14494_1711275183}[不存在]{style="font-family:宋体"}

[[Failed to process data channel keep-alive message: Invalid session ID.]{lang="EN-US"}]{#struct_0_x1608_14494_x1854577873}

[[处理数据隧道保活报文失败，]{style="font-family:宋体"}[Session ID TLV]{lang="EN-US"}]{#struct_0_x1608_14494_x1340316598}[无效]{style="font-family:宋体"}

[[LWAPP: Failed to verify LWAPP transport header.]{lang="EN-US"}]{#struct_0_x1608_14494_145191242}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1236059470}[：校验控制报文]{style="font-family:宋体"}[LWAPP transport header]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to verify LWAPP control header.]{lang="EN-US"}]{#struct_0_x1608_14494_x1420892699}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1367322559}[：校验控制报文]{style="font-family:宋体"}[LWAPP control header]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to send *MsgType*.]{lang="EN-US"}]{#struct_0_x1608_14494_1664221016}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1447741609}[：发送]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_1781708816}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[u]{lang="EN-US"}[nknown ]{lang="EN-US"}]{#struct_0_x1608_14494_98137075}[m]{lang="EN-US"}[essage]{lang="EN-US"}[：未知报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[iscovery ]{lang="EN-US"}]{#struct_0_x1608_14494_x1717015830}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：发现请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[iscovery ]{lang="EN-US"}]{#struct_0_x1608_14494_1307925120}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：发现回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin ]{lang="EN-US"}]{#struct_0_x1608_14494_x894080568}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：加入请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin ]{lang="EN-US"}]{#struct_0_x1608_14494_x258158821}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：加入回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin ACK]{lang="EN-US"}]{#struct_0_x1608_14494_x967469348}[：加入确认报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin ]{lang="EN-US"}]{#struct_0_x1608_14494_128446731}[c]{lang="EN-US"}[onfirm]{lang="EN-US"}[：加入确认回复报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[mage ]{lang="EN-US"}]{#struct_0_x1608_14494_x1824242762}[d]{lang="EN-US"}[ata ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：镜像数据请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[im]{lang="EN-US"}[age ]{lang="EN-US"}]{#struct_0_x1608_14494_1440191234}[d]{lang="EN-US"}[ata ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：镜像数据回复报文]{lang="EN-US" style="font-family:宋体"}

[[LWAPP: Failed to match *MsgType* with SeqNum *SeqNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_904640593}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_902693674}[：匹配序列号为]{style="font-family:宋体"}[SeqNum]{lang="EN-US"}[类型为]{style="font-family:宋体"}[MsgType]{lang="EN-US"}[的报文失败]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[[LWAPP: Received duplicate *MsgType* with SeqNum *SeqNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_x1017673708}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1653356686}[：接收到序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*[的重复请求报文，即序列号等于上次接受的请求报文序列号。]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_1711209647}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[[LWAPP: Received old *MsgType* with SeqNum *SeqNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_x1850526297}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_145125706}[：接收到序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*[的旧的请求报文，即序列号小于上次接收的请求报文序列号]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1222249192}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[[LWAPP: Number of packets in the retransmission queue exceeded the limit *MaxNum*.]{lang="EN-US"}]{#struct_0_x1608_14494_x1420958235}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1158583269}[：重传队列中缓存的报文超过最大数量]{style="font-family:宋体"}*[MaxNum]{lang="EN-US"}*

[[LWAPP: Failed to retransmit *MsgType* and tore down the tunnel: Number of retransmissions exceeded the limit *RetranCnt*.]{lang="EN-US"}]{#struct_0_x1608_14494_x1338424652}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1664155480}[：报文重传]{style="font-family:宋体"}*[RetranCnt]{lang="EN-US"}*[次后失败，断开隧道]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_245734059}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[[LWAPP: Failed to retransmit *MsgType* *RetranCnt* times.]{lang="EN-US"}]{#struct_0_x1608_14494_98071539}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1411227771}[：报文重传]{style="font-family:宋体"}*[RetranCnt]{lang="EN-US"}*[次后失败]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_1307859584}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request because WTP Descriptor TLV didn\'t exist.]{lang="EN-US"}]{#struct_0_x1608_14494_673725533}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x258224357}[：]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[没有携带]{style="font-family:宋体"}[Descriptor TLV]{lang="EN-US"}

[[LWAPP: Failed to process discovery request because WTP Name TLV didn\'t exist.]{lang="EN-US"}]{#struct_0_x1608_14494_1087643510}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1824308298}[：]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[没有携带]{style="font-family:宋体"}[WTP Name TLV]{lang="EN-US"}

[[LWAPP: Failed to process discovery request because WTP Radio Information TLV didn\'t exist.]{lang="EN-US"}]{#struct_0_x1608_14494_x1052149659}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_904575057}[：]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[没有携带]{style="font-family:宋体"}[Radio Information TLV]{lang="EN-US"}

[[LWAPP: Failed to process discovery request: Unsupported discovery type.]{lang="EN-US"}]{#struct_0_x1608_14494_x1374133884}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1017739244}[：发现类型不支持]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: Unmatched number of radios.]{lang="EN-US"}]{#struct_0_x1608_14494_1580919569}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1711144111}[：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[数量不匹配，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: Unsupported hardware version.]{lang="EN-US"}]{#struct_0_x1608_14494_145060170}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1631997900}[：硬件版本不支持，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: Unsupported boot version.]{lang="EN-US"}]{#struct_0_x1608_14494_x1421023771}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x140822810}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[不支持]{style="font-family:宋体"}[AP]{lang="EN-US"}[的启动版本，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: Unsupported AP software version.]{lang="EN-US"}]{#struct_0_x1608_14494_1664089944}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1873027986}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[不支持]{style="font-family:宋体"}[AP]{lang="EN-US"}[的软件版本，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process Discovery Request because WTP name carried default serial-ID.]{lang="EN-US"}]{#struct_0_x1608_14494_98006003}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1023612179}[：]{style="font-family:宋体"}[WTP Name]{lang="EN-US"}[中携带默认的序列号，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process Discovery Request because WTP name carried auto serial-ID.]{lang="EN-US"}]{#struct_0_x1608_14494_1307794048}

[[LWAPP:]{lang="EN-US"}[ WTP Name]{lang="EN-US"}]{#struct_0_x1608_14494_x1302071815}[中携带自动序列号，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: Serial-ID didn't match the AP name.]{lang="EN-US"}]{#struct_0_x1608_14494_x258289893}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_591995419}[：]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[中的]{style="font-family:宋体"}[serial-id]{lang="EN-US"}[和]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Name]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: WTP Board Data carried default model number.]{lang="EN-US"}]{#struct_0_x1608_14494_x1824373834}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x246002304}[：]{style="font-family:宋体"}[WTP Board Data]{lang="EN-US"}[中携带默认的型号，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Received discovery request when AP was in non-idle state.]{lang="EN-US"}]{#struct_0_x1608_14494_904509521}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1017804780}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[在]{style="font-family:宋体"}[AP]{lang="EN-US"}[处于非]{style="font-family:宋体"}[Idle]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[LWAPP: Failed to process discovery request: Unmatched model number.]{lang="EN-US"}]{#struct_0_x1608_14494_240230069}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1711078575}[：型号不匹配，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: APMGR Failed to process discovery request.]{lang="EN-US"}]{#struct_0_x1608_14494_x1860130301}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_144994634}[：]{style="font-family:宋体"}[APMGR]{lang="EN-US"}[处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP:Failed to process discovery request: MAC address was already in use.]{lang="EN-US"}]{#struct_0_x1608_14494_x354384111}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1421089307}[：]{style="font-family:宋体"}[WTP MAC]{lang="EN-US"}[地址重复，处理]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to decode discovery request.]{lang="EN-US"}]{#struct_0_x1608_14494_x1040515974}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1664024408}[：解析]{style="font-family:宋体"}[Discovery Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to decode join request.]{lang="EN-US"}]{#struct_0_x1608_14494_1810048567}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_97940467}[：解析]{style="font-family:宋体"}[Join  Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to decode join ACK.]{lang="EN-US"}]{#struct_0_x1608_14494_1307728512}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x2062170014}[：解析]{style="font-family:宋体"}[Join Ack]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request: WTP Name TLV didn't exist.]{lang="EN-US"}]{#struct_0_x1608_14494_x258355429}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x81745117}[：]{style="font-family:宋体"}[WTP Name TLV]{lang="EN-US"}[不存在，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request: WTP Descriptor TLV didn't exist.]{lang="EN-US"}]{#struct_0_x1608_14494_x1824439370}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_750120577}[：]{style="font-family:宋体"}[WTP Descriptor TLV]{lang="EN-US"}[不存在，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request: Session ID TLV didn't exist.]{lang="EN-US"}]{#struct_0_x1608_14494_904443985}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_975927912}[：]{style="font-family:宋体"}[Session ID TLV]{lang="EN-US"}[不存在，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request: WTP ADDR TLV didn't exist.]{lang="EN-US"}]{#struct_0_x1608_14494_x1017870316}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1323997452}[：]{style="font-family:宋体"}[WTP ADDR TLV]{lang="EN-US"}[不存在，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request: WTP Radio Information TLV didn't exist.]{lang="EN-US"}]{#struct_0_x1608_14494_1711013039}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_144929098}[：]{style="font-family:宋体"}[WTP Radio Information TLV]{lang="EN-US"}[不存在，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request: XNONCE TLV didn't exist.]{lang="EN-US"}]{#struct_0_x1608_14494_x37731312}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1421154843}[：]{style="font-family:宋体"}[XNONCE TLV]{lang="EN-US"}[不存在，处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request from AP with serial ID *serial-id*: Number of APs exceeded the limit.]{lang="EN-US"}]{#struct_0_x1608_14494_1663958872}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1647029713}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[个数超过限制，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request from AP with serial ID *serial-id*: Unmatched number of radios.]{lang="EN-US"}]{#struct_0_x1608_14494_97874931}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1892748290}[：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[个数错误，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request from AP with serial ID *serial-id*:Unsupported hardware version.]{lang="EN-US"}]{#struct_0_x1608_14494_1307662976}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1278264725}[：硬件版本错误，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request from AP with serial ID *serial-id*: Unsupported boot version.]{lang="EN-US"}]{#struct_0_x1608_14494_x258420965}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1824504906}[：启动版本错误，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request from AP with serial ID *serial-id*: Session ID was already in use.]{lang="EN-US"}]{#struct_0_x1608_14494_904378449}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1639674086}[：]{style="font-family:宋体"}[SessionID]{lang="EN-US"}[已被使用，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join request from AP with serial ID *serial-id*: Invalid AP state.]{lang="EN-US"}]{#struct_0_x1608_14494_x1017935852}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_226272953}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[当前的状态不合法，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process join request from AP with serial ID *serial-id*: MAC address was already in use.]{lang="EN-US"}]{#struct_0_x1608_14494_1710947503}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_119961752}[：相同的]{style="font-family:宋体"}[Mac]{lang="EN-US"}[地址已经被使用，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to add AP according to join request from AP with serial ID *serial-id*.]{lang="EN-US"}]{#struct_0_x1608_14494_144863562}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1421220379}[：根据序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join request]{lang="EN-US"}[报文信息来添加]{style="font-family:宋体"}[AP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to process the second half of join request: Invalid AP ID.]{lang="EN-US"}]{#struct_0_x1608_14494_621140930}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1663893336}[：]{style="font-family:宋体"}[AP ID]{lang="EN-US"}[无效，处理]{style="font-family:宋体"}[Join request]{lang="EN-US"}[后半部分失败]{style="font-family:宋体"}

[[LWAPP: Failed to process join ACK from AP with serial ID *serial-id*: Wrong session ID.]{lang="EN-US"}]{#struct_0_x1608_14494_384217239}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_97809395}[：]{style="font-family:宋体"}[SessionID]{lang="EN-US"}[错误，处理序列号为]{style="font-family:宋体"}*[serial-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Join Ack]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[LWAPP: Failed to decode image data request message.]{lang="EN-US"}]{#struct_0_x1608_14494_1238448233}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1441880704}[：解析]{style="font-family:宋体"}[Image Data Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Failed to process image data request message.]{lang="EN-US"}]{#struct_0_x1608_14494_x124203237}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1287430524}[：处理]{style="font-family:宋体"}[Image Data Request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[LWAPP: Number of images downloaded at the same time exceeded the limit.]{lang="EN-US"}]{#struct_0_x1608_14494_x1690287178}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1038596177}[：超出]{style="font-family:宋体"}[Image]{lang="EN-US"}[下载上限]{style="font-family:宋体"}

[[LWAPP: Received invalid Image Data Request message.]{lang="EN-US"}]{#struct_0_x1608_14494_x1260901571}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x883718124}[：收到无效的]{style="font-family:宋体"}[Image Data Request]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap event]{lang="EN-US"}]{#struct_0_x1608_14494_867213367}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1764040217}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_2101003088}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1594335942}

[[Received join request from AP with serial ID *serial-id* in Run state and tore down the tunnel.]{lang="EN-US"}]{#struct_0_x1608_14494_x538069340}

[[Run]{lang="EN-US"}]{#struct_0_x1608_14494_978981351}[状态下收到序列号为]{style="font-family:宋体"}*[serial-Id]{lang="EN-US"}*[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文，]{style="font-family:宋体"} [断开隧道]{style="font-family:宋体"}

[[Cannot process join request from AP with serial ID *serial-id*: AP down event was being processed.]{lang="EN-US"}]{#struct_0_x1608_14494_x1461609700}

[[Apmgr]{lang="EN-US"}]{#struct_0_x1608_14494_x1414555533}[正在处理]{style="font-family:宋体"}[down]{lang="EN-US"}[事件，接收到序列号为]{style="font-family:宋体"}*[serial-Id]{lang="EN-US"}*[的]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文，丢弃报文]{style="font-family:宋体"}

[[CAPWAP tunnel to AP *ap-name* went down:*.* R*eason*.]{lang="EN-US"}]{#struct_0_x1608_14494_2013667687}

[[由于原因]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x1608_14494_613379449}[，]{style="font-family:宋体"}[AC]{lang="EN-US"}[端断开和]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[间的隧道]{style="font-family:宋体"}

[*[reason]{lang="EN-US"}*]{#struct_0_x1608_14494_1845165231}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Neighbor ]{lang="EN-US"}]{#struct_0_x1608_14494_1479599589}[d]{lang="EN-US"}[ead timer expired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Neighbor Dead]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait ]{lang="EN-US"}]{#struct_0_x1608_14494_x100721927}[r]{lang="EN-US"}[equest timer expired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Wait Request]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Data ]{lang="EN-US"}]{#struct_0_x1608_14494_x1507760606}[c]{lang="EN-US"}[heck timer expired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Data Check]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to process data channel keep-alive]{lang="EN-US"}]{#struct_0_x1608_14494_x2080003165}[ message]{lang="EN-US"}[：处理数据隧道保活报文失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to process]{lang="EN-US"}]{#struct_0_x1608_14494_x1936894297}[ request]{lang="EN-US"}[：处理]{lang="EN-US" style="font-family:宋体"}[请求]{style="font-family:宋体"}[报文失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP was reset]{lang="EN-US"}]{#struct_0_x1608_14494_985684402}[：重启]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP was deleted]{lang="EN-US"}]{#struct_0_x1608_14494_x838438601}[：删除]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to go up]{lang="EN-US"}]{#struct_0_x1608_14494_1584367467}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[UP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Serial number changed]{lang="EN-US"}]{#struct_0_x1608_14494_x1871587993}[：修改序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Number of APs exceeded the limit]{lang="EN-US"}]{#struct_0_x1608_14494_279081290}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[个数超过上限]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Process]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_x1608_14494_x1979031155}[j]{lang="EN-US"}[oin ]{lang="EN-US"}[r]{lang="EN-US"}[equest in Run state]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Run]{lang="EN-US"}[状态下收到]{lang="EN-US" style="font-family:宋体"}[并处理]{style="font-family:宋体"}[Join Request]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to create AP context]{lang="EN-US"}]{#struct_0_x1608_14494_x247267755}[：创建]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}[ailure]{lang="EN-US"}]{#struct_0_x1608_14494_379636128}[ r]{lang="EN-US"}[esult ]{lang="EN-US"}[c]{lang="EN-US"}[ode]{lang="EN-US"}[：失败的错误码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to retransmit message ]{lang="EN-US"}]{#struct_0_x1608_14494_1115413302}[：重传失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to download image file]{lang="EN-US"}]{#struct_0_x1608_14494_309044944}[：下载]{lang="EN-US" style="font-family:宋体"}[image]{lang="EN-US"}[文件失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Image file downloaded successfully]{lang="EN-US"}]{#struct_0_x1608_14494_x548849856}[：下载]{lang="EN-US" style="font-family:宋体"}[image]{lang="EN-US"}[文件成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[File operation timer expired]{lang="EN-US"}]{#struct_0_x1608_14494_124332865}[：]{lang="EN-US" style="font-family:宋体"}[File operation]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[LWAPP: LWAPP tunnel to AP *ap-name* went down: R*eason*.]{lang="EN-US"}]{#struct_0_x1608_14494_538699982}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1287002651}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[端断开和]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[间的]{style="font-family:宋体"}[LWAPP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[*[reason]{lang="EN-US"}*]{#struct_0_x1608_14494_x271304497}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait ]{lang="EN-US"}]{#struct_0_x1608_14494_2114049171}[r]{lang="EN-US"}[equest timer expired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Wait Request]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Number of APs exceeded the limit]{lang="EN-US"}]{#struct_0_x1608_14494_1041705192}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[个数超过上限]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to process]{lang="EN-US"}]{#struct_0_x1608_14494_2033378717}[ request]{lang="EN-US"}[：处理]{lang="EN-US" style="font-family:宋体"}[请求]{style="font-family:宋体"}[报文失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to create AP context]{lang="EN-US"}]{#struct_0_x1608_14494_x87446322}[：创建]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP was reset]{lang="EN-US"}]{#struct_0_x1608_14494_x1015711972}[：重启]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP was deleted]{lang="EN-US"}]{#struct_0_x1608_14494_1390076930}[：删除]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to go up]{lang="EN-US"}]{#struct_0_x1608_14494_1798111064}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[UP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Serial number changed]{lang="EN-US"}]{#struct_0_x1608_14494_1341187064}[：修改序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to retransmit message]{lang="EN-US"}]{#struct_0_x1608_14494_x1455162190}[：重传失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to download image file]{lang="EN-US"}]{#struct_0_x1608_14494_2062614682}[：]{lang="EN-US" style="font-family:宋体"}[Image]{lang="EN-US"}[文件下载失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Image file downloaded successfully]{lang="EN-US"}]{#struct_0_x1608_14494_816716273}[：]{lang="EN-US" style="font-family:宋体"}[Image]{lang="EN-US"}[文件下载成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[File operation timer expired]{lang="EN-US"}]{#struct_0_x1608_14494_1949783723}[：]{lang="EN-US" style="font-family:宋体"}[File operation]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap fsm]{lang="EN-US"}]{#struct_0_x1608_14494_223334108}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1791491885}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_x1355443356}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1557340477}

[[Enter Join state.]{lang="EN-US"}]{#struct_0_x1608_14494_232027123}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_1165269943}[进入]{style="font-family:宋体"}[Join ]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Enter Config state.]{lang="EN-US"}]{#struct_0_x1608_14494_x1782111275}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1030205630}[进入]{style="font-family:宋体"}[Config]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Enter Image Download state]{lang="EN-US"}]{#struct_0_x1608_14494_x428892755}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1671369971}[进入]{style="font-family:宋体"}[Image Download]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Enter Data Check state.]{lang="EN-US"}]{#struct_0_x1608_14494_1932893539}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_1056278703}[进入]{style="font-family:宋体"}[Data Check]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Enter Run state.]{lang="EN-US"}]{#struct_0_x1608_14494_529058347}

[[AC]{lang="EN-US"}]{#struct_0_x1608_14494_x1506809280}[进入]{style="font-family:宋体"}[Run]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[LWAPP: Enter Join state.]{lang="EN-US"}]{#struct_0_x1608_14494_x833043238}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_67917387}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[进入]{style="font-family:宋体"}[Join]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[LWAPP: Enter Join Confirm state.]{lang="EN-US"}]{#struct_0_x1608_14494_1441815168}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1745478915}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[进入]{style="font-family:宋体"}[Join Confirm]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[LWAPP: Enter Image Download state.]{lang="EN-US"}]{#struct_0_x1608_14494_337111082}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1191629720}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[进入]{style="font-family:宋体"}[Image Download]{lang="EN-US"}[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap packet control receive]{lang="EN-US"}]{#struct_0_x1608_14494_x1854302544}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1788447823}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_x1281441939}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_238861584}

[[Received *MsgType* with SeqNum *SeqNum* from AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_1046262334}

[[从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_1238194911}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*[的]{style="font-family:宋体"} *[MsgType]{lang="EN-US"}*[类型报文]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1036959087}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[Received a fragment from AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x1404089523}

[[从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_681912981}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收到一个控制报文分片]{style="font-family:宋体"}

[[Assembled *MsgType* with SeqNum *SeqNum* from AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x124268773}

[[从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_x1723882105}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收到完整的一组分片并成功重组为序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*[的]{style="font-family:宋体"} *[MsgType]{lang="EN-US"}*[类型报文]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x985975481}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[LWAPP: Received *MsgType* with SeqNum *SeqNum* from AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_842959966}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x538286443}[：从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x568788810}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap packet control receive verbose]{lang="EN-US"}]{#struct_0_x1608_14494_663256205}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1790822533}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_1488379907}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_777930584}

[[Received *MsgType* from AP at *address:port.* Length=*length*. *content*]{lang="EN-US"}]{#struct_0_x1608_14494_x1713080076}

[[从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_1883810273}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}*[ MsgType]{lang="EN-US"}*[类型报文，其详细信息为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1114737041}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[Received fragment from AP at *address:port.*, Length= *length*. *content*]{lang="EN-US"}]{#struct_0_x1608_14494_737689954}

[[从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_x1690352714}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收到一个控制报文分片，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，详细信息为]{style="font-family:宋体"}[content]{lang="EN-US"}[。]{style="font-family:宋体"}

[[LWAPP: Received *MsgType* from AP at *address:port.* Length= *length*. *content*]{lang="EN-US"}]{#struct_0_x1608_14494_x681814143}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x1945561131}[：从地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[接收长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文，其详细信息为]{style="font-family:宋体"}*[content]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x563734807}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap packet control send]{lang="EN-US"}]{#struct_0_x1608_14494_x42142766}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1783894785}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_847023299}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1592866833}

[[Sent *MsgType* with SeqNum *SeqNum* to AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x1563082531}

[[发送序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_x1608_14494_1864547894}[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文到地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_24740719}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[Sent fragment *FragNum* of *MsgType* with SeqNum *SeqNum* to AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x1883393970}

[[发送序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_x1608_14494_x443761082}[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文的第]{style="font-family:宋体"}*[FragNum]{lang="EN-US"}*[个分片到地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1905424876}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[Sent all fragments of *MsgType* with SeqNum *SeqNum* to AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_1038530641}

[[发送序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_x1608_14494_724309108}[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文的所有]{style="font-family:宋体"}[分片到地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1785422093}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[LWAPP: Sent *MsgType* with SeqNum *SeqNum* to AP at *address:port.*]{lang="EN-US"}]{#struct_0_x1608_14494_x1934528884}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1727415164}[：发送序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*[的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[类型报文到地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x1819880056}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap packet control send verbose]{lang="EN-US"}]{#struct_0_x1608_14494_x1959267182}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1785837385}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_184680611}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_x957905109}

[[Sent *MsgType* sent to AP at *address*:*port*: Length=*length*. *content*]{lang="EN-US"}]{#struct_0_x1608_14494_x1030706201}

[[向地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_1255876886}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}*[ MsgType]{lang="EN-US"}*[类型报文，其详细信息为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_641951855}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[Sent fragment *FragNum* of *MsgType* sent to AP at *address:port: Length=length. content*]{lang="EN-US"}]{#struct_0_x1608_14494_x883783660}

[[向地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x1608_14494_1226756208}[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送到第]{style="font-family:宋体"}*[FragNum]{lang="EN-US"}*[个控制报文分片，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，详细信息为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x957789623}[取值请参见]{style="font-family:宋体"}[Failed to send *MsgType* message]{lang="EN-US"}[中的]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[取值]{style="font-family:宋体"}

[[LWAPP: Sent *MsgType* sent to AP at *address:port: Length=length. content*]{lang="EN-US"}]{#struct_0_x1608_14494_x1435557141}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_72761163}[：向地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}*[ MsgType]{lang="EN-US"}*[类型报文，其详细信息为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[*[MsgType]{lang="EN-US"}*]{#struct_0_x1608_14494_x2072387545}[取值请参见]{style="font-family:宋体"}[LWAPP: Failed to send *MsgType* message]{lang="EN-US"}[中]{style="font-family:宋体"}*[MsgType]{lang="EN-US"}*[的取值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap data]{lang="EN-US"}]{#struct_0_x1608_14494_x823921522}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1785078179}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_1870165590}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_1566806706}

[[Sent data channel keep-alive message to AP.]{lang="EN-US"}]{#struct_0_x1608_14494_1594363493}

[[向]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_239205109}[发送数据隧道保活报文成功]{style="font-family:宋体"}

[[Received data channel keep-alive message from AP.]{lang="EN-US"}]{#struct_0_x1608_14494_502454154}

[[成功收到来自]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1608_14494_1845099695}[的数据隧道保活报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US" style="font-size:9.0pt"}[debugging wlan capwap timer]{lang="EN-US"}]{#struct_0_x1608_14494_665541952}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1779913001}[[字段]{style="font-family:黑体"}]{#struct_0_x1608_14494_1432565474}

[[描述]{style="font-family:黑体"}]{#struct_0_x1608_14494_x1061106324}

[[Wait Request timer expired.]{lang="EN-US"}]{#struct_0_x1608_14494_x46841794}

[[Wait Request]{lang="EN-US"}]{#struct_0_x1608_14494_1217876357}[定时器超时]{style="font-family:宋体"}

[[File *file-name* operation timer expired.]{lang="EN-US"}]{#struct_0_x1608_14494_639036758}

[*[file-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x1325682904}[文件的操作定时器超时]{style="font-family:宋体"}

[[Image file keep-alive timer expired. Freed the file *file-name* buffer.]{lang="EN-US"}]{#struct_0_x1608_14494_124092978}

[*[file-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x1269867478}[文件的文件保活定时器超时，释放文件缓存]{style="font-family:宋体"}

[[Debug Wait timer of AP *ap-name* expired.]{lang="EN-US"}]{#struct_0_x1608_14494_2045753127}

[*[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x573324643}[上的]{style="font-family:宋体"}[DataTransfer]{lang="EN-US"}[等待分片定时器超时]{style="font-family:宋体"}

[[Debug Refresh timer of AP *ap-name* expired.]{lang="EN-US"}]{#struct_0_x1608_14494_x1114450779}

[*[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_279015754}[上的]{style="font-family:宋体"}[DataTransfer]{lang="EN-US"}[重启调试信息的刷新定时器]{style="font-family:宋体"}

[[Retransmission timer of AP *ap-name* expired.]{lang="EN-US"}]{#struct_0_x1608_14494_x1626292127}

[*[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_x1468775106}[上的报文收发的重传定时器超时]{style="font-family:宋体"}

[[Fragment timer of AP *ap-name* expired.]{lang="EN-US"}]{#struct_0_x1608_14494_x947501376}

[*[ap-name]{lang="EN-US"}*]{#struct_0_x1608_14494_770934221}[上的报文收发的分片定时器超时]{style="font-family:宋体"}

[[Data Check timer expired.]{lang="EN-US"}]{#struct_0_x1608_14494_209723595}

[[Data Check]{lang="EN-US"}]{#struct_0_x1608_14494_x612783688}[定时器超时]{style="font-family:宋体"}

[[LWAPP: Retransmission timer of AP *ap-name* expired.]{lang="EN-US"}]{#struct_0_x1608_14494_594900214}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_x2137306728}[：]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[上的报文收发的重传定时器超时]{style="font-family:宋体"}

[[LWAPP: File *file-name* operation timer expired.]{lang="EN-US"}]{#struct_0_x1608_14494_x1287068187}

[[LWAPP]{lang="EN-US"}]{#struct_0_x1608_14494_1803435942}[：]{style="font-family:宋体"}*[file-name]{lang="EN-US"}*[文件操作定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1608_14494_x2104792471}

[[\# AP]{lang="EN-US"}]{#struct_0_x1608_14494_x1460553613}[发现]{style="font-family:宋体"}[AC]{lang="EN-US"}[的过程中，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[端打开]{style="font-family:宋体"}[capwap fsm]{lang="EN-US"}[调试开关，会有如下调试信息：]{style="font-family:宋体"}

[[\<AC\> debugging wlan capwap fsm]{lang="EN-US"}]{#struct_0_x1608_14494_599646386}

[\*Sep 10 10:59]{lang="EN-US"}[：]{style="font-family:宋体"}[17:404 2013 H3C.com CWS/7/FSM]{lang="EN-US"}[：]{style="font-family:宋体"}[ -MDC = 1; Enter Join state.]{lang="EN-US"}

[*[// AC]{lang="EN-US"}*]{#struct_0_x1608_14494_x1903052387}*[进入]{style="font-family:宋体"}[Join]{lang="EN-US"}[状态]{style="font-family:宋体"}*
