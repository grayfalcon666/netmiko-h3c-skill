::: {#-988472740 .myid}
[]{#_Toc121110292}[]{#_Toc109289999}[]{#_Toc52102254}[]{#_Toc123030573}[]{#_Toc121110309}[]{#_Toc114641929}[]{#_Toc404794700}[]{#struct_0_x1687_15426_593545242}[]{#_Toc214157324}[]{#_Toc209948114}

**可定制IVR \-- 可定制IVR配置命令 \-- call-normal**

------------------------------------------------------------------------

[**[call-normal]{lang="DA"}**]{#struct_0_x1687_15426_x293737005}[命令用来配置普通二次呼叫的号码匹配策略。]{style="font-family:宋体"}

[**[undo]{lang="DA"}**]{#struct_0_x1687_15426_x1637180701}[ **call-normal**]{lang="DA"}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_476911204}

[**[call-normal]{lang="EN-US"}**[ { **length** *number-length* \| **matching** \| **terminator** *character* }]{lang="EN-US"}]{#struct_0_x1687_15426_1312499609}

[**[undo]{lang="EN-US"}**[ **call-normal**]{lang="EN-US"}]{#struct_0_x1687_15426_x2103364386}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x784436632}

[[没有配置普通二次呼叫的号码匹配策略。]{style="font-family:宋体"}]{#struct_0_x1687_15426_x854053342}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x712666160}

[[Call]{lang="EN-US"}]{#struct_0_x1687_15426_x424494058}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522347499}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1822666517}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_589429837}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1671471884}

[**[length]{lang="EN-US"}**[ *number-length*]{lang="EN-US"}]{#struct_0_x1687_15426_314753007}[：匹配输入号码的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[matching]{lang="EN-US"}**]{#struct_0_x1687_15426_266484664}[：随时匹配号码，即只要匹配到用户输入的号码，就立即进行二次呼叫。]{style="font-family:宋体"}

[**[terminator]{lang="EN-US"}**[ *character*]{lang="EN-US"}]{#struct_0_x1687_15426_x1703804544}[：结束符，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[、]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x1687_15426_7602312}

[[请避免将被叫号码中包含的字符或号码配置为终结符。]{style="font-family:宋体"}]{#struct_0_x1687_15426_1852975664}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x189539099}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_2059474071}[配置普通二次呼叫，匹配]{style="font-family:宋体"}[7]{lang="EN-US"}[位长度的用户输入号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_522281963}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 call]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] call-normal length 7]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404794701}[]{#struct_0_x1687_15426_1999059688}[]{#_Toc214157325}[]{#_Toc209948115}[]{#_Toc381113963}[]{#_Toc381713719}[]{#_Toc383792223}[]{#_Toc381113964}[]{#_Toc381713720}[]{#_Toc383792224}[]{#_Toc381113965}[]{#_Toc381713721}[]{#_Toc383792225}[]{#_Toc381113966}[]{#_Toc381713722}[]{#_Toc383792226}[]{#_Toc381113967}[]{#_Toc381713723}[]{#_Toc383792227}[]{#_Toc381113968}[]{#_Toc381713724}[]{#_Toc383792228}

**可定制IVR \-- 可定制IVR配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1687_15426_x1983627470}[命令用来配置节点的描述信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x1687_15426_x1979968125}[命令用来删除节点的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1563593410}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1687_15426_1735853077}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x1687_15426_x421689164}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522478571}

[[没有配置节点的描述信息。]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1626094157}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x669563586}

[[Call/Jump/Service]{lang="EN-US"}]{#struct_0_x1687_15426_1166245629}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1099602707}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1614442293}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x670557325}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x2088875672}

[*[text]{lang="EN-US"}*]{#struct_0_x1687_15426_x1632778500}[：节点的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522413035}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_1524703930}[配置]{style="font-family:宋体"}[Jump]{lang="EN-US"}[节点的描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_x381447860}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 jump]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] description first-node]{lang="EN-US"}
:::

::: {#-1356103434 .myid}
[]{#_Toc404794702}[]{#struct_0_x1687_15426_516268737}[]{#_Toc291661609}[]{#_Toc205711288}[]{#_Toc144027388}[]{#_Toc135295467}[]{#_Toc130097117}[]{#_Toc129160837}[]{#_Toc47776175}

**可定制IVR \-- 可定制IVR配置命令 \-- dial-prefix**

------------------------------------------------------------------------

[**[dial-prefix]{lang="EN-US"}**]{#struct_0_x1687_15426_x1006537780}[命令用来配置号码前缀。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dial-prefix**]{lang="EN-US"}]{#struct_0_x1687_15426_x1029980773}[命令用来删除已配置的前缀号码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1442075494}

[**[dial-prefix]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_x1687_15426_x1486625284}

[**[undo]{lang="EN-US"}**[ **dial-prefix**]{lang="EN-US"}]{#struct_0_x1687_15426_522609643}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x583583321}

[[没有配置号码前缀。]{style="font-family:宋体"}]{#struct_0_x1687_15426_1386860593}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1272215153}

[[Call]{lang="EN-US"}]{#struct_0_x1687_15426_1969853213}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1053274260}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1477291287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_463241357}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_322663739}

[*[string]{lang="EN-US"}*]{#struct_0_x1687_15426_x171723012}[：号码前缀，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[、]{style="font-family:宋体"}[\#]{lang="EN-US"}[。各符号的含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-1]{lang="EN-US"}](?-1356103434#_Ref169498719)[所示。]{style="font-family:
宋体"}

[]{#struct_0_x1687_15426_522544107}[]{#_Ref169498719}[]{#_Toc121809753}[[表1-1 ]{lang="EN-US"}[参数]{style="font-family:黑体"}[string]{lang="EN-US"}]{#_Toc112125387}[中的符号含义]{style="font-family:黑体"}

[]{#table_struct_0_1537377422}[[符号]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1228826624}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_x1687_15426_1432653869}

[[0-9]{lang="EN-US"}]{#struct_0_x1687_15426_1664190830}

[[表示一位号码，可以是]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1687_15426_1463309229}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_x1687_15426_1364665268}[或]{style="font-family:宋体"}[\*]{lang="EN-US"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_x1687_15426_x828401013}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522085354}

[[配置号码前缀后，设备会以"号码前缀＋拨入号码"作为被叫号码。添加号码前缀后，如果号码总长度超过]{style="font-family:宋体"}[31]{lang="EN-US"}]{#struct_0_x1687_15426_190545729}[位时，设备只发送前]{style="font-family:宋体"}[31]{lang="EN-US"}[位号码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1031176510}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_1274031047}[配置号码前缀]{style="font-family:宋体"}[021]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_1872674928}

[\[Sysname\] voice-setup]{lang="EN-US"}

[[\[Sysname-voice\] ivr-system]{lang="EN-US"}]{#struct_0_x1687_15426_x490338513}

[[\[Sysname-voice-ivr\] node 1 call]{lang="EN-US"}]{#struct_0_x1687_15426_x56393491}

[[\[Sysname-voice-dial-node1\] dial-prefix 021]{lang="EN-US"}]{#struct_0_x1687_15426_522019818}

::: {#1447091858 .myid}
[]{#_Toc404794703}[]{#struct_0_x1687_15426_1706084253}[]{#_Toc214157326}[]{#_Toc209948116}

**可定制IVR \-- 可定制IVR配置命令 \-- display voice ivr call-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **voice** **ivr** **call-info**]{lang="EN-US"}]{#struct_0_x1687_15426_x1949632934}[命令用来查看]{style="font-family:宋体"}[IVR]{lang="EN-US"}[呼叫信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1273644545}

[**[display]{lang="EN-US"}**[ **voice** **ivr** **call-info**]{lang="EN-US"}]{#struct_0_x1687_15426_x331570229}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1287381618}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1687_15426_723512369}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1235120154}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x681044735}

[[network-operator]{lang="EN-US"}]{#struct_0_x1687_15426_1978013300}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_522216426}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1687_15426_1641500747}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_819479342}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_488903776}[查看]{style="font-family:宋体"}[IVR]{lang="EN-US"}[呼叫信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice ivr call-info]{lang="EN-US"}]{#struct_0_x1687_15426_1566359610}

[Index  Called-Number    Caller-Number    Entity   Node-Id  Status]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[1      101              100              101      1        PLAY MEDIA]{lang="EN-US"}

[2      406              200              201      3        WAIT INPUT]{lang="EN-US"}

[3      606              300              301      6        CALL]{lang="EN-US"}

[4      806              400              401      9        IDLE]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display voice ivr call-info]{lang="EN-US"}]{#struct_0_x1687_15426_x1857346640}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1532410960}[[字段]{style="font-family:黑体"}]{#struct_0_x1687_15426_522150890}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1687_15426_593545241}

[[Index]{lang="EN-US"}]{#struct_0_x1687_15426_x293737008}

[[呼叫信息索引]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1637508381}

[[Called-Number]{lang="EN-US"}]{#struct_0_x1687_15426_410605120}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1149598846}

[[Caller-Number]{lang="EN-US"}]{#struct_0_x1687_15426_1948458242}

[[主叫号码]{style="font-family:宋体"}]{#struct_0_x1687_15426_522347498}

[[Entity]{lang="EN-US"}]{#struct_0_x1687_15426_x1822666516}

[[被叫号码对应的]{style="font-family:宋体"}[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_x976654104}[语音实体号]{style="font-family:宋体"}

[[Node-Id]{lang="EN-US"}]{#struct_0_x1687_15426_1365038381}

[[正在执行的节点号]{style="font-family:宋体"}]{#struct_0_x1687_15426_1546301164}

[[Status]{lang="EN-US"}]{#struct_0_x1687_15426_x29706091}

[[当前执行所处的状态：]{style="font-family:宋体"}]{#struct_0_x1687_15426_x354409152}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_x1687_15426_522281962}[：空闲状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PLAY MEDIA]{lang="EN-US"}]{#struct_0_x1687_15426_1999059689}[：播放媒体状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAIT INPUT]{lang="EN-US"}]{#struct_0_x1687_15426_x1983693006}[：等待按键状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CALL]{lang="EN-US"}]{#struct_0_x1687_15426_x1245524564}[：呼叫状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1762901073 .myid}
[]{#_Toc404794704}[]{#struct_0_x1687_15426_878415761}[]{#_Toc214157327}[]{#_Toc209948117}

**可定制IVR \-- 可定制IVR配置命令 \-- display voice media-play**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1871441643}

[**[display]{lang="EN-US"}**[ **voice** **media-play**]{lang="EN-US"}]{#struct_0_x1687_15426_522478570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1626094158}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1879417167}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1870349114}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x346285128}

[[network-operator]{lang="EN-US"}]{#struct_0_x1687_15426_2065871577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1066711781}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1687_15426_1328531454}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x2120570923}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_522413034}[查看放音信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice media-play]{lang="EN-US"}]{#struct_0_x1687_15426_1524703929}

[Index    Codec       Media-Id    Play-Times       Status        Type]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[1        g729r8       1001           3             play          PSTN:1/0]{lang="EN-US"}

[2        g711alaw     1002           2             stop          IP:100.1.1.1]{lang="EN-US"}

[3        g711ulaw     1003           2             stop          IP:100.1.1.1]{lang="EN-US"}

[4        g723r53      1004           2             stop          IP:100.1.1.1]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display voice media-play]{lang="EN-US"}]{#struct_0_x1687_15426_x380858035}[命令显示信息描述表]{style="font-family:黑体"}

[]{#_Toc123030574}[]{#_Toc121110274}[]{#table_struct_0_1534317100}[[字段]{style="font-family:黑体"}]{#struct_0_x1687_15426_1302503575}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1784762713}

[[Index]{lang="EN-US"}]{#struct_0_x1687_15426_522609642}

[[放音信息索引]{style="font-family:宋体"}]{#struct_0_x1687_15426_x583583320}

[[Codec]{lang="EN-US"}]{#struct_0_x1687_15426_1386795057}

[[放音编解码类型，包括]{style="font-family:宋体"}[g729r8]{lang="EN-US"}]{#struct_0_x1687_15426_x1097875939}[、]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[、]{style="font-family:宋体"}[g711ulaw]{lang="EN-US"}[和]{style="font-family:宋体"}[g723r53]{lang="EN-US"}[四种编解码类型]{style="font-family:宋体"}

[[Media-Id]{lang="EN-US"}]{#struct_0_x1687_15426_x120148685}

[[媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1687_15426_522544106}

[[Play-Times]{lang="EN-US"}]{#struct_0_x1687_15426_x1228826623}

[[媒体文件总共要播放的次数]{style="font-family:宋体"}]{#struct_0_x1687_15426_1835938396}

[[Status]{lang="EN-US"}]{#struct_0_x1687_15426_693287125}

[[当前的放音状态：]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1320254464}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[play]{lang="EN-US"}]{#struct_0_x1687_15426_1346143809}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop]{lang="EN-US"}]{#struct_0_x1687_15426_522085357}

[[Type]{lang="EN-US"}]{#struct_0_x1687_15426_190545730}

[[当前的呼叫类型：]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1307475657}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSTN]{lang="EN-US"}]{#struct_0_x1687_15426_x1252235517}[：从]{style="font-family:宋体"}[PSTN]{lang="EN-US"}[接入，此例中的]{style="font-family:宋体"}[1/0]{lang="EN-US"}[表示呼叫从语音用户线]{style="font-family:宋体"}[1/0]{lang="EN-US"}[接入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_x1687_15426_x1614818167}[：呼叫从对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址接入]{style="font-family:宋体"}

[ ]{lang="FR"}

::: {#-1492540226 .myid}
[]{#_Toc404794705}[]{#struct_0_x1687_15426_x1425177388}[]{#_Toc214157328}[]{#_Toc209948118}

**可定制IVR \-- 可定制IVR配置命令 \-- display voice media-source**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1843830896}

[**[display]{lang="EN-US"}**[ **voice** **media-source** ]{lang="EN-US"}]{#struct_0_x1687_15426_x1110833935}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522019821}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1014904938}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_589644658}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_282210651}

[[network-operator]{lang="EN-US"}]{#struct_0_x1687_15426_349781447}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1879580968}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1687_15426_1799894110}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_563096081}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x1471544562}[查看媒体文件的读取信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice media-source]{lang="EN-US"}]{#struct_0_x1687_15426_522216429}

[Codec    Media-Id   source        Size (Bytes)   Read-Num  Cache-Num]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="PT-BR"}

[g729r8   1000       cfa0:/wav/g7  69304          1         1]{lang="PT-BR"}

[                    29r8/0.wav]{lang="PT-BR"}

[[表1-4 ]{lang="EN-US"}[display voice media-source]{lang="EN-US"}]{#struct_0_x1687_15426_1641500762}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1533721793}[[字段]{style="font-family:黑体"}]{#struct_0_x1687_15426_819807024}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1687_15426_x182554054}

[[Codec]{lang="EN-US"}]{#struct_0_x1687_15426_82122556}

[[文件使用的编解码类型]{style="font-family:宋体"}]{#struct_0_x1687_15426_x166308860}

[[Media-Id]{lang="EN-US"}]{#struct_0_x1687_15426_1610513425}

[[媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1687_15426_x33315150}

[[Source]{lang="EN-US"}]{#struct_0_x1687_15426_522150893}

[[媒体文件名及存放路径]{style="font-family:宋体"}]{#struct_0_x1687_15426_593545240}

[[Size (Bytes)]{lang="EN-US"}]{#struct_0_x1687_15426_x293737007}

[[媒体文件的大小，以字节为单位]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1637049629}

[[Read-Num]{lang="EN-US"}]{#struct_0_x1687_15426_x362032817}

[[此文件对应的读控制块编号]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1854600811}

[[Cache-Num]{lang="EN-US"}]{#struct_0_x1687_15426_x256637319}

[[此文件对应的缓冲区编号]{style="font-family:宋体"}]{#struct_0_x1687_15426_522347501}

[ ]{lang="EN-US"}

::: {#-900180729 .myid}
[]{#_Toc109290001}[]{#_Toc404794706}[]{#struct_0_x1687_15426_479249806}[]{#_Toc214157332}[]{#_Toc209948122}[]{#_Toc381113974}[]{#_Toc381713730}[]{#_Toc383792234}[]{#_Toc381113975}[]{#_Toc381713731}[]{#_Toc383792235}[]{#_Toc381113976}[]{#_Toc381713732}[]{#_Toc383792236}[]{#_Toc381113977}[]{#_Toc381713733}[]{#_Toc383792237}[]{#_Toc381113978}[]{#_Toc381713734}[]{#_Toc383792238}[]{#_Toc381113979}[]{#_Toc381713735}[]{#_Toc383792239}[]{#_Toc381113980}[]{#_Toc381713736}[]{#_Toc383792240}[]{#_Toc381113981}[]{#_Toc381713737}[]{#_Toc383792241}[]{#_Toc381113982}[]{#_Toc381713738}[]{#_Toc383792242}[]{#_Toc381113983}[]{#_Toc381713739}[]{#_Toc383792243}[]{#_Toc381113984}[]{#_Toc381713740}[]{#_Toc383792244}[]{#_Toc381113985}[]{#_Toc381713741}[]{#_Toc383792245}[]{#_Toc381113986}[]{#_Toc381713742}[]{#_Toc383792246}[]{#_Toc381113987}[]{#_Toc381713743}[]{#_Toc383792247}[]{#_Toc381113988}[]{#_Toc381713744}[]{#_Toc383792248}[]{#_Toc381113989}[]{#_Toc381713745}[]{#_Toc383792249}[]{#_Toc381113990}[]{#_Toc381713746}[]{#_Toc383792250}[]{#_Toc381113991}[]{#_Toc381713747}[]{#_Toc383792251}[]{#_Toc381113992}[]{#_Toc381713748}[]{#_Toc383792252}[]{#_Toc381113993}[]{#_Toc381713749}[]{#_Toc383792253}[]{#_Toc381113994}[]{#_Toc381713750}[]{#_Toc383792254}[]{#_Toc381113995}[]{#_Toc381713751}[]{#_Toc383792255}

**可定制IVR \-- 可定制IVR配置命令 \-- global-input-error**

------------------------------------------------------------------------

[**[global-input-error]{lang="EN-US"}**]{#struct_0_x1687_15426_x1696686245}[命令用来配置全局]{style="font-family:宋体"}[IVR]{lang="EN-US"}[用户输入错误的处理策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **global-input-error**]{lang="EN-US"}]{#struct_0_x1687_15426_1828055278}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1088280084}

[**[global-input-error]{lang="EN-US"}**[ { **media-play** *media-id* \[ *play-times* \] \| **repeat** *repeat-times* } \*]{lang="EN-US"}]{#struct_0_x1687_15426_x901810260}

[**[undo]{lang="EN-US"}**[ **global-input-error**]{lang="EN-US"}]{#struct_0_x1687_15426_908587492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1771989104}

[[输入错误后不播放提示音，输入超过错误]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_x1687_15426_x1054205332}[次后结束呼叫。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1383999993}

[[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_522281965}[管理视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1999059682}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1982972110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1379858834}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1608362151}

[**[media-play]{lang="EN-US"}***[ media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_x1596505953}[：用户输入错误后，设备播放提示音的媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[play-times]{lang="EN-US"}*]{#struct_0_x1687_15426_x428584888}[：播放提示音的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[repeat]{lang="EN-US"}***[ repeat-times]{lang="EN-US"}*]{#struct_0_x1687_15426_x532205867}[：允许用户输入错误的次数，每次用户输入错误后，设备将重新执行该节点，输入错误次数超过设定的值后将结束呼叫。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x2040489245}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x780822910}[配置全局]{style="font-family:宋体"}[IVR]{lang="EN-US"}[用户输入错误的处理策略：播放媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10002]{lang="EN-US"}[的提示音]{style="font-family:宋体"}[2]{lang="EN-US"}[次，输入错误超过]{style="font-family:宋体"}[5]{lang="EN-US"}[次后结束呼叫。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_522478573}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] global-input-error media-play 10002 2 repeat 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1626094155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[input-error]{lang="EN-US"}**]{#struct_0_x1687_15426_x1832363000}
:::

::: {#-1546460677 .myid}
[]{#_Toc404794707}[]{#struct_0_x1687_15426_x1544672113}

**可定制IVR \-- 可定制IVR配置命令 \-- global-timeout**

------------------------------------------------------------------------

[**[global]{lang="EN-US"}**]{#struct_0_x1687_15426_x1050061397}**[-timeout]{lang="DA"}**[命令用来配置全局]{style="font-family:宋体"}[IVR]{lang="DA"}[用户]{style="font-family:宋体"}[输入超时的处理策略。]{style="font-family:宋体"}

[**[undo]{lang="DA"}**]{#struct_0_x1687_15426_422400638}[ ]{lang="DA"}**[global]{lang="EN-US"}[-timeout]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_355415471}

[**[global-timeout]{lang="EN-US"}**[ { **expires** *seconds* \| **media-play** *media-id* \[ *play-times* \] \| **repeat** *repeat-times* } \*]{lang="EN-US"}]{#struct_0_x1687_15426_632900098}

[**[undo global-timeout]{lang="EN-US"}**]{#struct_0_x1687_15426_192681571}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x143796986}

[[超时时间为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x1687_15426_522413037}[秒，超时次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次，输入超时后不播放提示音，超过超时次数后结束呼叫。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1524703928}

[[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_x380923571}[管理视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_497078447}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1778578134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1655074932}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x498065087}

[**[expires]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1687_15426_x264928502}[：超时时间，超时后将重新执行该节点，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[media-play]{lang="EN-US"}***[ media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_1751678161}[：用户输入超时后，设备播放提示音的媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[play-times]{lang="EN-US"}*]{#struct_0_x1687_15426_x1659844192}[：播放提示音的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[repeat]{lang="EN-US"}***[ repeat-times]{lang="EN-US"}*]{#struct_0_x1687_15426_522609645}[：允许用户输入超时的次数，每次用户输入超时后，设备将重新执行该节点。超时次数超过设定的值后将结束呼叫。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x583583327}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_1386467377}[配置全局]{style="font-family:宋体"}[IVR]{lang="EN-US"}[用户输入超时的处理策略：超时时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100001]{lang="EN-US"}[，播放提示音]{style="font-family:宋体"}[1]{lang="EN-US"}[次，超时次数超过]{style="font-family:宋体"}[2]{lang="EN-US"}[次后结束呼叫。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_486855868}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] global-timeout expires 20 media-play 100001 1 repeat 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1002137076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timeout]{lang="EN-US"}**]{#struct_0_x1687_15426_2110641024}
:::

::: {#147252359 .myid}
[]{#_Toc404794708}[]{#struct_0_x1687_15426_2105902153}

**可定制IVR \-- 可定制IVR配置命令 \-- input extension**

------------------------------------------------------------------------

[**[input]{lang="EN-US"}**]{#struct_0_x1687_15426_1357786341}[命令用来配置扩展二次呼叫。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **input**]{lang="EN-US"}]{#struct_0_x1687_15426_x502961902}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1516607903}

[**[input ]{lang="EN-US"}***[number ]{lang="EN-US"}***[extension]{lang="EN-US"}***[ extension-number]{lang="EN-US"}*]{#struct_0_x1687_15426_522544109}

[**[undo]{lang="EN-US"}**[ **input** *number*]{lang="EN-US"}]{#struct_0_x1687_15426_x1228826638}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1249109783}

[[没有配置扩展二次呼叫。]{style="font-family:宋体"}]{#struct_0_x1687_15426_719474648}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1259218832}

[[Call]{lang="EN-US"}]{#struct_0_x1687_15426_x174994904}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x946154160}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x12566951}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1785666316}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1877172326}

[*[number]{lang="EN-US"}*]{#struct_0_x1687_15426_431234588}[：用户输入的号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[、]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[extension-number]{lang="EN-US"}*]{#struct_0_x1687_15426_522085356}[：扩展二次呼叫的号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[、]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1687_15426_190545731}

[[一个]{style="font-family:宋体"}[Call]{lang="EN-US"}]{#struct_0_x1687_15426_x1307475658}[节点下最多可以配置]{style="font-family:宋体"}[10]{lang="EN-US"}[条扩展二次呼叫命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1299289684}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x2096424172}[配置扩展二次呼叫，按]{style="font-family:宋体"}[0]{lang="EN-US"}[表示呼叫号码]{style="font-family:宋体"}[5000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_x1562991192}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 call]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] input 0 extension 5000]{lang="EN-US"}
:::

::: {#2102642499 .myid}
[]{#_Toc404794709}[]{#struct_0_x1687_15426_832707225}

**可定制IVR \-- 可定制IVR配置命令 \-- input-error**

------------------------------------------------------------------------

[**[input-error]{lang="EN-US"}**]{#struct_0_x1687_15426_1186543268}[命令用来配置节点下用户输入错误的处理策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **input-error**]{lang="EN-US"}]{#struct_0_x1687_15426_247661102}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522019820}

[**[input-error]{lang="EN-US"}**[ { **end-call** \| **goto-pre-node** \| **goto-node** *node-id* } \[ **media-play** *media-id* \[ *play-times* \] \| **repeat** *repeat-times* \] \*]{lang="EN-US"}]{#struct_0_x1687_15426_x1014904939}

[**[undo]{lang="EN-US"}**[ **input-error**]{lang="EN-US"}]{#struct_0_x1687_15426_x2139238697}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1396495625}

[[没有配置节点下用户输入错误的处理策略。]{style="font-family:宋体"}]{#struct_0_x1687_15426_x159134274}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_224468885}

[[Jump/Call]{lang="EN-US"}]{#struct_0_x1687_15426_x1910842252}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x969881526}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_721655397}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1672901326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522216428}

[**[end-call]{lang="EN-US"}**]{#struct_0_x1687_15426_1641500761}[：输入错误次数超过设定值后结束呼叫。]{style="font-family:宋体"}

[**[goto-pre-node]{lang="EN-US"}**]{#struct_0_x1687_15426_819610416}[：输入错误次数超过设定值后返回上一级节点。]{style="font-family:宋体"}

[**[goto-node]{lang="EN-US"}**[ *node-id*]{lang="EN-US"}]{#struct_0_x1687_15426_x22526777}[：输入错误次数超过设定值后跳到指定的节点，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[media-play]{lang="EN-US"}***[ media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_716016660}[：用户输入错误后，设备播放提示音的媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[play-times]{lang="EN-US"}*]{#struct_0_x1687_15426_731706825}[：播放提示音的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[repeat]{lang="EN-US"}***[ repeat-times]{lang="EN-US"}*]{#struct_0_x1687_15426_1968410746}[：允许用户输入错误的次数，每次用户输入错误后，设备将重新执行该节点。当输入错误次数超过设定值后，按配置的处理方式进行处理，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1488737092}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x1580018469}[配置节点下用户输入错误的处理策略：播放媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10002]{lang="EN-US"}[的提示音]{style="font-family:宋体"}[2]{lang="EN-US"}[次，输入错误次数超过]{style="font-family:宋体"}[5]{lang="EN-US"}[次就结束呼叫。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_522150892}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 jump]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] input-error end-call media-play 1000 6 repeat 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_593545239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[global-input-error]{lang="EN-US"}**]{#struct_0_x1687_15426_1280241096}
:::

::: {#42913162 .myid}
[]{#_Toc404794710}[]{#struct_0_x1687_15426_291171398}[]{#_Toc214157333}[]{#_Toc209948123}

**可定制IVR \-- 可定制IVR配置命令 \-- ivr-root**

------------------------------------------------------------------------

[**[ivr-root]{lang="EN-US"}**]{#struct_0_x1687_15426_x1635542356}[命令用来配置]{style="font-family:宋体"}[IVR]{lang="EN-US"}[语音实体的根节点，即]{style="font-family:宋体"}[IVR]{lang="EN-US"}[执行的第一个节点。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ivr-root**]{lang="EN-US"}]{#struct_0_x1687_15426_x1717752097}[命令用来取消]{style="font-family:宋体"}[IVR]{lang="EN-US"}[语音实体的根节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_2143150567}

[**[ivr-root]{lang="NL"}**]{#struct_0_x1687_15426_x1857276178}[ *node-id*]{lang="NL"}

[**[undo]{lang="NL"}**]{#struct_0_x1687_15426_467571875}[ **ivr-root**]{lang="NL"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x745964651}

[[不存在]{style="font-family:宋体"}[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_x1626325183}[语音实体的根节点。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522347500}

[[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_479249807}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1696686246}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x900828077}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_100701883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1368471357}

[*[node-id]{lang="EN-US"}*]{#struct_0_x1687_15426_518714060}[：根节点号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x2067438001}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_184991099}[配置]{style="font-family:宋体"}[IVR]{lang="EN-US"}[语音实体的根节点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_522281964}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 100 ivr]{lang="EN-US"}

[\[Sysname-voice-dial-entity100\] ivr-root 1]{lang="EN-US"}
:::

::: {#1543811064 .myid}
[]{#_Toc404794711}[]{#struct_0_x1687_15426_1999059683}[]{#_Toc214157334}[]{#_Toc209948124}

**可定制IVR \-- 可定制IVR配置命令 \-- ivr-system**

------------------------------------------------------------------------

[**[ivr-system]{lang="ES"}**]{#struct_0_x1687_15426_x1983037646}[命令]{style="font-family:宋体"}[用来进入]{style="font-family:宋体"}[IVR]{lang="EN-US"}[管理视图]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1687_15426_773246976}**[ivr-system]{lang="ES"}**[命令用来删除所有]{style="font-family:宋体"}[IVR]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x326489369}

[**[ivr-system]{lang="ES"}**]{#struct_0_x1687_15426_1117461201}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1687_15426_x979398650}**[ivr-system]{lang="ES"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1663393099}

[[没有]{style="font-family:宋体"}[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_x1189826122}[管理视图]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_933396692}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x1687_15426_522478572}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1626094156}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_896520355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1761293467}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1982968246}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x1710567049}[进入]{style="font-family:宋体"}[IVR]{lang="EN-US"}[管理视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_226481633}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\]]{lang="EN-US"}
:::

::: {#1861609725 .myid}
[]{#_Toc404794712}[]{#struct_0_x1687_15426_149160424}[]{#_Toc214157336}[]{#_Toc209948126}

**可定制IVR \-- 可定制IVR配置命令 \-- media-file**

------------------------------------------------------------------------

[**[media-file]{lang="EN-US"}**]{#struct_0_x1687_15426_x2073875757}[命令用来进入语音媒体资源管理视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1493919604}

[**[media-file]{lang="PT-BR"}**]{#struct_0_x1687_15426_522413036}[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g729r8** }]{lang="PT-BR"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1524703927}

[[语音视图]{style="font-family:宋体"}]{#struct_0_x1687_15426_x381775539}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_93817879}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1892170131}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x587206908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x840094339}

[**[g711alaw]{lang="EN-US"}**]{#struct_0_x1687_15426_x960741889}[：进入]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[编码类型视图。]{style="font-family:宋体"}

[**[g711ulaw]{lang="EN-US"}**]{#struct_0_x1687_15426_85759498}[：进入]{style="font-family:宋体"}[g711ulaw]{lang="EN-US"}[编码类型视图。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_x1687_15426_494406823}[：进入]{style="font-family:宋体"}[g723r53]{lang="EN-US"}[编码类型视图。]{style="font-family:宋体"}

[**[g729r8]{lang="EN-US"}**]{#struct_0_x1687_15426_522609644}[：进入]{style="font-family:宋体"}[g729r8]{lang="EN-US"}[编码类型视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x583583326}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_1386401841}[进入编码类型为]{style="font-family:宋体"}[g729r8]{lang="EN-US"}[的媒体资源管理视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_x635769979}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] media-file g729r8]{lang="EN-US"}

[\[Sysname-voice-media-g729r8\]]{lang="EN-US"}
:::

::: {#-952177060 .myid}
[]{#_Toc404794713}[]{#struct_0_x1687_15426_x565767437}[]{#_Toc214157337}[]{#_Toc209948127}

**可定制IVR \-- 可定制IVR配置命令 \-- media-play**

------------------------------------------------------------------------

[**[media-play]{lang="DA"}**]{#struct_0_x1687_15426_2131775904}[命令用来配置等待用户按键播放的提示音。]{style="font-family:宋体"}

[**[undo]{lang="DA"}**]{#struct_0_x1687_15426_706920820}[ **media-play**]{lang="DA"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_815961388}

[**[media-play]{lang="EN-US"}**[ *media-id* \[ *play-times* \] \[ **force** \]]{lang="EN-US"}]{#struct_0_x1687_15426_x198123377}

[**[undo]{lang="EN-US"}**[ **media-play**]{lang="EN-US"}]{#struct_0_x1687_15426_x1721710644}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522544108}

[[没有配置等待用户按键播放的提示音。]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1228826637}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x133364536}

[[Jump/Call]{lang="EN-US"}]{#struct_0_x1687_15426_1709641673}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x954886083}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1838888819}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x19613462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1212024820}

[*[media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_x752239467}[：表示媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[play-times]{lang="EN-US"}*]{#struct_0_x1687_15426_970924573}[：重复播放次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[force]{lang="EN-US"}**]{#struct_0_x1687_15426_x971274055}[：表示进入节点后，播放提示音结束后用户按键才有效。缺省情况为不强制，即表示在提示音播放过程中用户按键有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522085359}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_190545724}[配置等待用户按键提示音，且播放提示音结束后用户按键才有效。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_1031176499}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 jump]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] media-play 10000 3 force]{lang="EN-US"}
:::

::: {#1985170616 .myid}
[]{#_Toc404794714}[]{#struct_0_x1687_15426_x681694273}[]{#_Toc214157338}[]{#_Toc209948128}

**可定制IVR \-- 可定制IVR配置命令 \-- node**

------------------------------------------------------------------------

[**[node]{lang="EN-US"}**]{#struct_0_x1687_15426_760223642}[命令用来创建一个]{style="font-family:宋体"}[IVR]{lang="EN-US"}[节点并进入]{style="font-family:宋体"}[IVR]{lang="EN-US"}[节点视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **node**]{lang="EN-US"}]{#struct_0_x1687_15426_x304417959}[命令用来删除]{style="font-family:宋体"}[IVR]{lang="EN-US"}[节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_37703478}

[**[node]{lang="EN-US"}**[ *node-id* \[ **call** \| **jump** \| **service** \]]{lang="EN-US"}]{#struct_0_x1687_15426_x1280349170}

[**[undo]{lang="EN-US"}**[ **node** { *node-id* \| **all** }]{lang="EN-US"}]{#struct_0_x1687_15426_1547144312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522019823}

[[不存在]{style="font-family:宋体"}[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_x1014904940}[节点。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_233610906}

[[IVR]{lang="EN-US"}]{#struct_0_x1687_15426_x1448789904}[管理视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_761694446}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x65552651}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_318977734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1615187176}

[*[node-id]{lang="EN-US"}*]{#struct_0_x1687_15426_2016377253}[：表示一个节点号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[call]{lang="EN-US"}**]{#struct_0_x1687_15426_363031703}[：表示配置二次呼叫的节点。]{style="font-family:宋体"}

[**[jump]{lang="EN-US"}**]{#struct_0_x1687_15426_450276967}[：表示配置按键选择跳转的节点。]{style="font-family:宋体"}

[**[service]{lang="EN-US"}**]{#struct_0_x1687_15426_522216431}[：表示配置立即二次呼叫、跳转、结束呼叫或放音的节点。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1687_15426_x314814382}[：所有类型的节点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_922002837}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_1343223365}[创建]{style="font-family:宋体"}[Jump]{lang="EN-US"}[节点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_x1570254977}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 jump]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\]]{lang="EN-US"}
:::

::: {#-451395624 .myid}
[]{#_Toc404794715}[]{#struct_0_x1687_15426_859238426}[]{#_Toc214157339}[]{#_Toc209948129}

**可定制IVR \-- 可定制IVR配置命令 \-- operation**

------------------------------------------------------------------------

[**[operation]{lang="EN-US"}**]{#struct_0_x1687_15426_1477788932}[命令用来配置节点操作功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **operation**]{lang="EN-US"}]{#struct_0_x1687_15426_24154065}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522150895}

[**[operation]{lang="EN-US"}**[ *number* { **call-immediate** *call-number* \| **end-call** \| **goto-node** *node-id* \| **goto-pre-node** \| **media-play** *media-id* \[ *play-times* \] }]{lang="EN-US"}]{#struct_0_x1687_15426_593545246}

[**[undo]{lang="EN-US"}**[ **operation** *number*]{lang="EN-US"}]{#struct_0_x1687_15426_x293737001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1636918557}

[[没有配置节点操作功能。]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1184660198}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1940975029}

[[Service]{lang="EN-US"}]{#struct_0_x1687_15426_384298170}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_63811272}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x1936407392}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1409301727}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1361942698}

[*[number]{lang="EN-US"}*]{#struct_0_x1687_15426_522347503}[：执行]{style="font-family:宋体"}[ID]{lang="EN-US"}[标识，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[call-immediate]{lang="EN-US"}**[ *call-number*]{lang="EN-US"}]{#struct_0_x1687_15426_479249808}[：立即二次呼叫的号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[、]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[end-call]{lang="EN-US"}**]{#struct_0_x1687_15426_x1696686259}[：结束呼叫。]{style="font-family:宋体"}

[**[goto-node]{lang="EN-US"}**[ *node-id*]{lang="EN-US"}]{#struct_0_x1687_15426_x141247654}[：跳到指定节点，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[goto-pre-node]{lang="EN-US"}**]{#struct_0_x1687_15426_x1686648416}[：]{style="font-family:宋体"}[返回上级节点]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[media-play]{lang="EN-US"}***[ media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_x97571003}[：配置播放提示音的媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[play-times]{lang="EN-US"}*]{#struct_0_x1687_15426_1517748901}[：播放提示音的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1406249371}

[[当某项执行功能为跳转到其他节点或挂机操作时，将不再执行剩下未执行的功能项。]{style="font-family:宋体"}]{#struct_0_x1687_15426_1492139424}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x561365223}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_522281967}[在]{style="font-family:宋体"}[Service]{lang="EN-US"}[节点配置执行结束呼叫。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_1999059684}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 service]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] operation 1 end-call]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1983365326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[select-rule]{lang="EN-US"}**]{#struct_0_x1687_15426_x747217488}
:::

::: {#986528911 .myid}
[]{#_Toc404794716}[]{#struct_0_x1687_15426_x1690777188}[]{#_Toc214157340}[]{#_Toc209948130}

**可定制IVR \-- 可定制IVR配置命令 \-- select-rule**

------------------------------------------------------------------------

[**[select-rule]{lang="EN-US"}**]{#struct_0_x1687_15426_2022848997}[命令用来配置功能执行顺序。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **select-rule**]{lang="EN-US"}]{#struct_0_x1687_15426_596429624}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1741816152}

[**[select-rule]{lang="EN-US"}**[ *1st-operation 2nd-operation 3rd-operation*]{lang="EN-US"}]{#struct_0_x1687_15426_522478575}

[**[undo]{lang="EN-US"}**[ **select-rule** ]{lang="EN-US"}]{#struct_0_x1687_15426_x1626094161}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_493039220}

[[功能执行顺序为]{style="font-family:宋体"}**[select-rule]{lang="EN-US"}**[ **1** **2** **3**]{lang="EN-US"}]{#struct_0_x1687_15426_1560602927}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_84098237}

[[Service]{lang="EN-US"}]{#struct_0_x1687_15426_73834595}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x848677202}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x359740791}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x685509963}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1404834963}

[*[1st-operation]{lang="EN-US"}*]{#struct_0_x1687_15426_x1461848748}[：第一个执行的操作功能号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[2nd-operation]{lang="EN-US"}*]{#struct_0_x1687_15426_522413039}[：第二个执行的操作功能号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，此参数不能同]{style="font-family:宋体"}*[1st-operation]{lang="EN-US"}*[重复。]{style="font-family:宋体"}

[*[3rd-operation]{lang="EN-US"}*]{#struct_0_x1687_15426_1524703942}[：第三个执行的操作功能号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，此参数不能同]{style="font-family:宋体"}*[1st-operation]{lang="EN-US"}*[，]{style="font-family:宋体"}*[2nd-operation]{lang="EN-US"}*[重复。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x381578933}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x1785946126}[配置]{style="font-family:宋体"}[Service]{lang="EN-US"}[节点下功能执行顺序为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_205351136}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 service]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] select-rule 1 3 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_89760794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[operation]{lang="EN-US"}**]{#struct_0_x1687_15426_x1999369056}
:::

::: {#1515229910 .myid}
[]{#_Toc404794717}[]{#struct_0_x1687_15426_x1983357325}[]{#_Toc214157341}[]{#_Toc209948131}

**可定制IVR \-- 可定制IVR配置命令 \-- set-media**

------------------------------------------------------------------------

[**[set-media]{lang="DA"}**]{#struct_0_x1687_15426_1227809050}[命令用来配置媒体资源]{style="font-family:宋体"}[ID]{lang="DA"}[与媒体文件的对应关系。]{style="font-family:宋体"}

[**[undo]{lang="DA"}**]{#struct_0_x1687_15426_x593015730}[ **set-media**]{lang="DA"}[命令用来删除已配置的对应关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522609647}

[**[set-media]{lang="EN-US"}***[ media-id ]{lang="EN-US"}***[file]{lang="EN-US"}**[ *filename*]{lang="EN-US"}]{#struct_0_x1687_15426_x583583325}

[**[undo]{lang="ES"}**]{#struct_0_x1687_15426_1386598449}[ **set-media** { *media-id* \| **all** }]{lang="ES"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1449078285}

[[没有定义媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1687_15426_x606380694}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_952824087}

[[语音媒体资源管理视图]{style="font-family:宋体"}]{#struct_0_x1687_15426_1613255084}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_985686831}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_265087096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_586946337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522544111}

[*[media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_727488506}[：媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[file]{lang="EN-US"}***[ filename]{lang="EN-US"}*]{#struct_0_x1687_15426_x119375268}[：媒体文件名。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1687_15426_x1591922669}[：所有媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x284851234}

[[\# ]{lang="DA"}]{#struct_0_x1687_15426_442219018}[配置资源]{style="font-family:宋体"}[ID 10001]{lang="DA"}[对应的媒体文件为]{style="font-family:宋体"}[cfa0:/g729/ring.wav]{lang="DA"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x1687_15426_1474895492}

[\[Sysname\] voice-setup]{lang="DA"}

[\[Sysname-voice\] media-file g729r8]{lang="DA"}

[\[Sysname-voice-media-g729r8\] set-media 10001 file cfa0:/g729/ring.wav]{lang="EN-US"}
:::

::: {#591226122 .myid}
[]{#_Toc404794718}[]{#struct_0_x1687_15426_503812567}[]{#_Toc214157342}[]{#_Toc209948132}[]{#_Toc381114008}[]{#_Toc381713764}[]{#_Toc383792268}

**可定制IVR \-- 可定制IVR配置命令 \-- timeout**

------------------------------------------------------------------------

[**[timeout]{lang="EN-US"}**]{#struct_0_x1687_15426_x36389652}[命令用来配置节点下用户输入超时的处理策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timeout**]{lang="EN-US"}]{#struct_0_x1687_15426_1198644588}[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522085358}

[**[timeout]{lang="EN-US"}**[ { **end-call** \| **goto-pre-node** \| **goto-node** *node-id* } \[ **expires** *seconds* \| **media-play** *media-id* \[ *play-times* \] \| **repeat** *repeat-times* \] \*]{lang="EN-US"}]{#struct_0_x1687_15426_190545725}

[**[undo]{lang="EN-US"}**[ **timeout**]{lang="EN-US"}]{#struct_0_x1687_15426_1031176498}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x681759809}

[[没有配置节点下用户输入超时的处理策略。]{style="font-family:宋体"}]{#struct_0_x1687_15426_x1080945457}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x805632866}

[[Jump/Call]{lang="EN-US"}]{#struct_0_x1687_15426_x1420425104}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_1056954552}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1764381059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1250871436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522019822}

[**[end-call]{lang="EN-US"}**]{#struct_0_x1687_15426_x1014904941}[：结束呼叫。]{style="font-family:宋体"}

[**[goto-pre-node]{lang="EN-US"}**]{#struct_0_x1687_15426_1799694847}[：返回上级节点。]{style="font-family:宋体"}

[**[goto-node]{lang="EN-US"}**[ *node-id*]{lang="EN-US"}]{#struct_0_x1687_15426_136194770}[：跳到指定的节点，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[expires]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1687_15426_x1754103070}[：超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[media-play]{lang="EN-US"}***[ media-id]{lang="EN-US"}*]{#struct_0_x1687_15426_704727019}[：用户输入超时后，设备播放提示音的媒体资源]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[play-times]{lang="EN-US"}*]{#struct_0_x1687_15426_x1875367403}[：配置播放提示音的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[repeat]{lang="EN-US"}***[ repeat-times]{lang="EN-US"}*]{#struct_0_x1687_15426_385182754}[：允许用户输入超时的次数，每次用户输入错误后，设备将重新执行该节点。当输入超时次数超过设定值后，按配置的处理方式进行处理，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_741468902}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x1384506696}[配置节点下用户输入超时的处理策略为输入超时次数超过]{style="font-family:宋体"}[3]{lang="EN-US"}[次，结束呼叫。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_522216430}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 jump]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] timeout end-call repeat 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x314814383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[global-]{lang="EN-US"}[timeout]{lang="EN-US"}**]{#struct_0_x1687_15426_921937301}
:::

::: {#1020011220 .myid}
[]{#_Toc404794719}[]{#struct_0_x1687_15426_x1095776896}[]{#_Toc214157343}[]{#_Toc209948133}

**可定制IVR \-- 可定制IVR配置命令 \-- user-input**

------------------------------------------------------------------------

[**[user-input]{lang="DA"}**]{#struct_0_x1687_15426_601069775}[命令用来配置根据具体输入执行跳转操作。]{style="font-family:宋体"}

[**[undo]{lang="DA"}**]{#struct_0_x1687_15426_365779730}[ **user-input**]{lang="DA"}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1687_15426_986377332}

[**[user-input]{lang="EN-US"}**[ *character* { **end-call** \| **goto-node** *node-id* \| **goto-pre-node** }]{lang="EN-US"}]{#struct_0_x1687_15426_1317850950}

[**[undo]{lang="EN-US"}**[ **user-input** *character*]{lang="EN-US"}]{#struct_0_x1687_15426_1186333728}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x938409220}

[[没有配置跳转操作。]{style="font-family:宋体"}]{#struct_0_x1687_15426_522150894}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1687_15426_593545245}

[[Jump]{lang="EN-US"}]{#struct_0_x1687_15426_x293737004}[节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1637246237}

[[network-admin]{lang="EN-US"}]{#struct_0_x1687_15426_x667370871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1687_15426_1307058427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1687_15426_283297988}

[*[character]{lang="EN-US"}*]{#struct_0_x1687_15426_1624717190}[：用户输入的按键信息，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:宋体"}[\*]{lang="EN-US"}[、]{style="font-family:
宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[end-call]{lang="EN-US"}**]{#struct_0_x1687_15426_x1112686870}[：表示结束呼叫。]{style="font-family:宋体"}

[**[goto-node]{lang="EN-US"}***[ node-id]{lang="EN-US"}*]{#struct_0_x1687_15426_x1062869412}[：表示跳到指定的节点，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[goto-pre-node]{lang="EN-US"}**]{#struct_0_x1687_15426_593824692}[：表示返回上级节点。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1687_15426_522347502}

[[在一个]{style="font-family:宋体"}[Jump]{lang="EN-US"}]{#struct_0_x1687_15426_479249809}[节点下最多可以配置]{style="font-family:宋体"}[12]{lang="EN-US"}[个跳转操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1687_15426_x1696686260}

[[\# ]{lang="EN-US"}]{#struct_0_x1687_15426_x2063496419}[配置用户按]{style="font-family:宋体"}[0]{lang="EN-US"}[结束呼叫。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1687_15426_837576689}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ivr-system]{lang="EN-US"}

[\[Sysname-voice-ivr\] node 1 jump]{lang="EN-US"}

[\[Sysname-voice-ivr-node1\] user-input 0 end-call]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
