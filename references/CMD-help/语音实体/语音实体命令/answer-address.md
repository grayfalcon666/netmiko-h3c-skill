::::: {#-1209837796 .myid}
[]{#_Toc404794345}[]{#struct_0_16135_x6401_x626056996}

**语音实体 \-- 语音实体命令 \-- answer-address**

------------------------------------------------------------------------

[**[answer-address]{lang="EN-US"}**]{#struct_0_16135_x6401_940026945}[命令用来在实体下配置一个号码串，若此号码串与呼叫中的主叫号码相匹配，则将该实体作为入实体。该主叫号码是呼叫]{style="font-family:宋体"}[INVITE]{lang="EN-US"}[报文中的主叫号码。]{style="font-family:宋体"}

[**[undo answer-address]{lang="EN-US"}**]{#struct_0_16135_x6401_1490705194}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_667399702}

[**[answer-address ]{lang="EN-US"}***[calling-number-string]{lang="EN-US"}*]{#struct_0_16135_x6401_1276337965}

[**[undo answer-address]{lang="EN-US"}**]{#struct_0_16135_x6401_2143058991}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_500030502}

[[没有配置任何可将该实体作为入实体的主叫号码匹配信息。]{style="font-family:宋体"}]{#struct_0_16135_x6401_210917906}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_210710645}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1227096121}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1391086252}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_977224166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1432626050}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1474778265}

[*[calling-number-string]{lang="EN-US"}*]{#struct_0_16135_x6401_x843847570}[：指定的主叫号码串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，格式为]{style="font-family:宋体"}[\[ + \] { *regular-expression* \[ T \] \[ \$ \] \| T }]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1902916920}[+]{lang="EN-US"}["：号码模板如果以"]{style="font-family:宋体"}[+]{lang="EN-US"}["号开头，表示整个号码是一个]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准号码，如]{style="font-family:宋体"}[+110022]{lang="EN-US"}[表示]{style="font-family:宋体"}[110022]{lang="EN-US"}[是符合]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准的号码。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音实体命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_16135_x6401_435943024}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[如果配置的号码首位带有]{style="font-family:KaiTi_GB2312"}]{#struct_0_16135_x6401_x1895493482}["+"]{lang="EN-US"}[号，则在中继环境中需要注意：]{style="font-family:KaiTi_GB2312"}[E&M/R2/LGS]{lang="EN-US"}[信令采用的是]{style="font-family:KaiTi_GB2312"}[DTMF]{lang="EN-US"}[传输，由于]{style="font-family:KaiTi_GB2312"}["+"]{lang="EN-US"}[号本身没有对应的音频，所以无法将号码成功的传输到被叫侧。而]{style="font-family:KaiTi_GB2312"}[DSS1]{lang="EN-US"}[信令采用]{style="font-family:KaiTi_GB2312"}[ISDN]{lang="EN-US"}[传输，不存在上述问题。在实际应用中，用户应该避免配置传输信令无法识别的字符，否则将会导致呼叫失败。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1778068147}[\$]{lang="EN-US"}["：只能放在结尾，表示号码结束，号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的]{style="font-family:宋体"}*[regular-expression]{lang="EN-US"}*[部分。如果号码模板后没有]{style="font-family:宋体"}[\$]{lang="EN-US"}[字符，则表示可以匹配以此号码开头的号码。]{style="font-family:宋体"}[例如，配置]{lang="EN-US" style="font-family:宋体"}[answer-address 20]{lang="EN-US"}[，表示将匹配呼叫中的以]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[开头的主叫号码的实体作为入实体。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[符号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_1882302219}[T]{lang="EN-US"}["：]{style="font-family:宋体"}[T]{lang="EN-US"}[表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[regular-expression]{lang="EN-US"}*]{#struct_0_16135_x6401_1992003168}[：由"]{lang="EN-US" style="font-family:宋体"}[0-9#\*.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{lang="EN-US" style="font-family:宋体"}[[表]{lang="EN-US" style="font-family:宋体"}[1-1]{lang="EN-US"}](?-1209837796#_Ref398306821)[所示。]{lang="EN-US" style="font-family:宋体"}

[]{#struct_0_16135_x6401_133457891}[[表1-1 ]{lang="EN-US"}[符号含义描述表]{style="font-family:
黑体"}]{#_Ref398306821}

[]{#table_struct_0_x159339344}[[符号]{style="font-family:黑体"}]{#struct_0_16135_x6401_1823783249}
:::::

[[含义]{style="font-family:黑体"}]{#struct_0_16135_x6401_x49442476}

[[0-9]{lang="EN-US"}]{#struct_0_16135_x6401_11991191}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16135_x6401_x334483586}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_16135_x6401_x2115414218}[和]{style="font-family:宋体"}[\*]{lang="EN-US"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_1699541832}

[[.]{lang="EN-US"}]{#struct_0_16135_x6401_x415767697}

[[通配符，可以与任何一个有效号码匹配。如：]{style="font-family:宋体"}[555....]{lang="EN-US"}]{#struct_0_16135_x6401_1378174820}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_16135_x6401_518391634}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_16135_x6401_1287278233}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1029341523}

[[+]{lang="EN-US"}]{#struct_0_16135_x6401_1894003580}

[[指明符号前的字符串重复一次或多次。如：]{style="font-family:宋体"}[9876(54)+]{lang="EN-US"}]{#struct_0_16135_x6401_x739575084}[可以匹配]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[%]{lang="EN-US"}]{#struct_0_16135_x6401_1246600052}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[9876(54)%]{lang="EN-US"}]{#struct_0_16135_x6401_x449363057}[可以匹配]{style="font-family:宋体"}[9876]{lang="EN-US"}[、]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[-]{lang="EN-US"}]{#struct_0_16135_x6401_180512058}

[[连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如：]{style="font-family:宋体"}[\[1-9\]]{lang="EN-US"}]{#struct_0_16135_x6401_x305585213}[表示从]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[9]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_16135_x6401_1546336331}["只能出现在"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["中，且连接两端只能为数字]{style="font-family:宋体"}

[[\[ \]]{lang="EN-US"}]{#struct_0_16135_x6401_x1571518381}

[[表示字符选择范围，如：]{style="font-family:宋体"}[\[1-36\]]{lang="EN-US"}]{#struct_0_16135_x6401_1746595999}[表示只可匹配单个字符]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[中的某一个]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_16135_x6401_278193512}["和"]{style="font-family:宋体"}[( )]{lang="EN-US"}["如果嵌套使用，则必须以"]{style="font-family:宋体"}[( \[ \] )]{lang="EN-US"}["形式出现，不允许其它形式，如"]{style="font-family:宋体"}[\[ \[ \] \]]{lang="EN-US"}["、"]{style="font-family:宋体"}[\[ ( ) \]]{lang="EN-US"}["等]{style="font-family:宋体"}

[[( )]{lang="EN-US"}]{#struct_0_16135_x6401_566014124}

[[表示一组字符，如：]{style="font-family:宋体"}[(123)]{lang="EN-US"}]{#struct_0_16135_x6401_531412799}[表示字符串]{style="font-family:宋体"}[123]{lang="EN-US"}[，它一般与符号"]{style="font-family:宋体"}[!]{lang="EN-US"}["、"]{style="font-family:宋体"}[%]{lang="EN-US"}["、"]{style="font-family:宋体"}[+]{lang="EN-US"}["一起使用，如：]{style="font-family:宋体"}[408(12)+]{lang="EN-US"}[，可以匹配]{style="font-family:宋体"}[40812]{lang="EN-US"}[或]{style="font-family:宋体"}[408121212]{lang="EN-US"}[等字符串]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_177301670}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1852108968}[配置]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体]{style="font-family:宋体"}[1]{lang="EN-US"}[，收到的呼叫中主叫号码以]{style="font-family:宋体"}[456]{lang="EN-US"}[开头时，可以使用该实体作为入实体。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_536283666}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 1 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity1\] answer-address 456]{lang="EN-US"}

::::: {#795477320 .myid}
[]{#_Toc404794346}[]{#struct_0_16135_x6401_x859116490}[]{#_Toc355262294}[]{#_Ref353368027}

**语音实体 \-- 语音实体命令 \-- codec**

------------------------------------------------------------------------

[**[codec]{lang="EN-US"}**]{#struct_0_16135_x6401_x1371982243}[命令用来配置语音编解码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **codec**]{lang="EN-US"}]{#struct_0_16135_x6401_73832589}[命令用来删除配置的语音编解码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1576615403}

[]{#struct_0_16135_x6401_x1549474907}[]{#_Hlt20797640}**[codec]{lang="EN-US"}**[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g723r63** \| **g726r16** \| **g726r24** \| **g726r32** \| **g726r40** \| **g729a** \| **g729br8** \| **g729r8** } \[ **bytes** *payload-size* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **codec** ]{lang="EN-US"}]{#struct_0_16135_x6401_467806342}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_731011442}

[[没有配置语音编解码。]{style="font-family:宋体"}]{#struct_0_16135_x6401_1961606638}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1511125207}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1216668764}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_961456565}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_854753397}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_737798269}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1141704089}

[**[g711alaw]{lang="EN-US"}**]{#struct_0_16135_x6401_1433039105}[：表示]{style="font-family:宋体"}[G.711]{lang="EN-US"}[的]{style="font-family:宋体"}[A]{lang="EN-US"}[律编解码方式，带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，通常被欧洲采用。]{style="font-family:宋体"}

[**[g711ulaw]{lang="EN-US"}**]{#struct_0_16135_x6401_819610968}[：表示]{style="font-family:宋体"}[G.711]{lang="EN-US"}[的]{style="font-family:宋体"}[m]{lang="EN-US" style="font-family:Symbol"}[律编解码方式，带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，通常被北美和日本等国家采用。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_16135_x6401_730945906}[：表示]{style="font-family:宋体"}[G.723.1 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[5.3kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g723r63]{lang="EN-US"}**]{#struct_0_16135_x6401_80945901}[：表示]{style="font-family:宋体"}[G.723.1 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[6.3kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g726r16]{lang="EN-US"}**]{#struct_0_16135_x6401_1489062324}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[16kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r24]{lang="EN-US"}**]{#struct_0_16135_x6401_794201662}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[24kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r32]{lang="EN-US"}**]{#struct_0_16135_x6401_x131436884}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码，带宽为]{style="font-family:宋体"}[32kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r40]{lang="EN-US"}**]{#struct_0_16135_x6401_x1643513499}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[40kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g729a]{lang="EN-US"}**]{#struct_0_16135_x6401_x1162032938}[：表示]{style="font-family:宋体"}[G.729 Annex A]{lang="EN-US"}[编解码方式，对]{style="font-family:宋体"}[G.729]{lang="EN-US"}[编解码进行了一系列简化，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g729br8]{lang="EN-US"}**]{#struct_0_16135_x6401_x2058826043}[：表示]{style="font-family:宋体"}[G.729 Annex B]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g729r8]{lang="EN-US"}**]{#struct_0_16135_x6401_2069651853}[：表示]{style="font-family:宋体"}[G.729]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bytes]{lang="EN-US"}**[ *payload-size*]{lang="EN-US"}]{#struct_0_16135_x6401_730880370}[：每秒发送的编码字节数，取值范围和选择的编解码有关，单位为字节：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g711alaw]{lang="EN-US"}**]{#struct_0_16135_x6401_x1036937519}[和]{style="font-family:宋体"}**[g711ulaw]{lang="EN-US"}**[的取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[8]{lang="EN-US"}[的倍数），]{style="font-family:宋体"}[80]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[80]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g723r53]{lang="EN-US"}**]{#struct_0_16135_x6401_1591793424}[的取值范围为]{style="font-family:
宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g723r63]{lang="EN-US"}**]{#struct_0_16135_x6401_x1076692360}[的取值范围为]{style="font-family:
宋体"}[24]{lang="EN-US"}[～]{style="font-family:宋体"}[144]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[24]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r16]{lang="EN-US"}**]{#struct_0_16135_x6401_739017216}[的取值范围为]{style="font-family:
宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[220]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r24]{lang="EN-US"}**]{#struct_0_16135_x6401_x159885872}[的取值范围为]{style="font-family:
宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[210]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[30]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r32]{lang="EN-US"}**]{#struct_0_16135_x6401_x1373066237}[的取值范围为]{style="font-family:
宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[40]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r40]{lang="EN-US"}**]{#struct_0_16135_x6401_1708321261}[的取值范围为]{style="font-family:
宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[50]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g729a]{lang="EN-US"}**]{#struct_0_16135_x6401_730814834}[、]{style="font-family:
宋体"}**[g729br8]{lang="EN-US"}**[和]{style="font-family:
宋体"}**[729r8]{lang="EN-US"}**[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[10]{lang="EN-US"}[的倍数）。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}**[g711]{lang="EN-US"}**]{#struct_0_16135_x6401_x1473466599}[为]{style="font-family:宋体"}[160]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g723r63]{lang="EN-US"}**[为]{style="font-family:宋体"}[24]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g723r53]{lang="EN-US"}**[为]{style="font-family:宋体"}[20]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r16]{lang="EN-US"}**[为]{style="font-family:宋体"}[60]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r24]{lang="EN-US"}**[为]{style="font-family:宋体"}[90]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r32]{lang="EN-US"}**[为]{style="font-family:宋体"}[120]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r40]{lang="EN-US"}**[为]{style="font-family:宋体"}[150]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g729]{lang="EN-US"}**[为]{style="font-family:宋体"}[30]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x2125391409}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音实体命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_16135_x6401_x1341068227}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[只有当通讯双方拥有的语音编解码存在交集时，双方才能正常建立呼叫。]{style="font-family:KaiTi_GB2312"}]{#struct_0_16135_x6401_60710498}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:KaiTi_GB2312"}]{#struct_0_16135_x6401_x26670350}
:::

[ ]{lang="EN-US"}

[**[g711alaw]{lang="EN-US"}**]{#struct_0_16135_x6401_1965063992}[和]{style="font-family:宋体"}**[g711ulaw]{lang="EN-US"}**[编解码可以提供高质量的语音传输，但要占用较高的带宽。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_16135_x6401_232305044}[和]{style="font-family:宋体"}**[g723r63]{lang="EN-US"}**[编解码提供了静音压缩技术和舒适噪音，较高速率的输出基于多脉冲多量级技术并提供某种程度上较高质量的音质，较低速率的输出基于码激励线性预测技术并为应用提供了更大的灵活性。]{style="font-family:宋体"}

[**[g729r8]{lang="EN-US"}**]{#struct_0_16135_x6401_639510371}[和]{style="font-family:宋体"}**[g729a]{lang="EN-US"}**[编解码提供的话音质量与]{style="font-family:宋体"}[32kbps]{lang="EN-US"}[的]{style="font-family:宋体"}[ADPCM]{lang="EN-US"}[（]{style="font-family:宋体"}[Adaptive Differential Pulse Code Modulation]{lang="EN-US"}[，自适应差分脉冲编码调制）相似，具有长话的质量，同时具有低带宽、较小时间延迟和适中处理复杂度，因此应用广泛。]{style="font-family:宋体"}

[[为了更清晰地了解各种语音编解码算法对语音带宽、话音质量等的影响，]{style="font-family:宋体"}]{#struct_0_16135_x6401_730749298}[[表]{style="font-family:宋体"}[1-2]{lang="EN-US"}](?795477320#_Ref404268010)[介绍相关算法和带宽的关系。]{style="font-family:宋体"}

[]{#_Ref404268010}[]{#struct_0_16135_x6401_x1305337790}[]{#_Ref148446106}[]{#_Toc121809742}[[表1-2 ]{lang="EN-US"}[相关算法和带宽的关系]{style="font-family:黑体"}]{#_Toc112125376}

[]{#table_struct_0_x643981765}[[语音编解码]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1946164093}
:::::

[[带宽]{style="font-family:黑体"}]{#struct_0_16135_x6401_205389951}

[[语音质量]{style="font-family:黑体"}]{#struct_0_16135_x6401_1575700422}

[[G.711]{lang="EN-US"}]{#struct_0_16135_x6401_1500394659}[（]{style="font-family:宋体"}[A]{lang="EN-US"}[律、]{style="font-family:宋体"}[m]{lang="EN-US" style="font-family:Symbol"}[律）]{style="font-family:宋体"}

[[64Kbps]{lang="EN-US"}]{#struct_0_16135_x6401_115734139}[（没有压缩）]{style="font-family:宋体"}

[[语音质量最好]{style="font-family:宋体"}]{#struct_0_16135_x6401_730683762}

[[G.726]{lang="EN-US"}]{#struct_0_16135_x6401_639461691}

[[16]{lang="EN-US"}]{#struct_0_16135_x6401_1167598393}[、]{style="font-family:宋体"}[24]{lang="EN-US"}[、]{style="font-family:宋体"}[32]{lang="EN-US"}[、]{style="font-family:宋体"}[40 Kbps]{lang="EN-US"}

[[语音质量较好]{style="font-family:宋体"}]{#struct_0_16135_x6401_1179299418}

[[G.729]{lang="EN-US"}]{#struct_0_16135_x6401_x1985733675}

[[8Kbps]{lang="EN-US"}]{#struct_0_16135_x6401_x1339800359}

[[语音质量较好]{style="font-family:宋体"}]{#struct_0_16135_x6401_1678214667}

[[G.723 r63]{lang="EN-US"}]{#struct_0_16135_x6401_730618226}

[[6.3Kbps]{lang="EN-US"}]{#struct_0_16135_x6401_x895540979}

[[语音质量一般]{style="font-family:宋体"}]{#struct_0_16135_x6401_1252599305}

[[G.723 r53]{lang="EN-US"}]{#struct_0_16135_x6401_648238251}

[[5.3Kbps]{lang="EN-US"}]{#struct_0_16135_x6401_x1913163757}

[[语音质量一般]{style="font-family:宋体"}]{#struct_0_16135_x6401_731601266}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1188233835}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1999045398}[配置语音编解码为]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x877808011}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] codec g711alaw]{lang="EN-US"}

::: {#-561127002 .myid}
[]{#_Toc404794347}[]{#struct_0_16135_x6401_1638030890}[]{#_Toc355262295}

**语音实体 \-- 语音实体命令 \-- codec preference**

------------------------------------------------------------------------

[**[codec preference]{lang="EN-US"}**]{#struct_0_16135_x6401_x1313925869}[命令用来配置编解码优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **codec preference**]{lang="EN-US"}]{#struct_0_16135_x6401_1812239684}[命令用来删除已配置的编解码优先级。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_731535730}

[**[codec preference ]{lang="EN-US"}***[priority]{lang="EN-US"}*[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g723r63** \| **g726r16** \| **g726r24** \| **g726r32** \| **g726r40** \| **g729a** \| **g729br8** \| **g729r8** } \[ **bytes** *payload-size* \]]{lang="EN-US"}]{#struct_0_16135_x6401_x1793499175}

[**[undo codec preference ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_16135_x6401_x604762194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_750979157}

[[编解码模板中不存在编解码设置。]{style="font-family:宋体"}]{#struct_0_16135_x6401_747666998}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1845231392}

[[编解码模板视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_1101453206}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1962061515}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x835073946}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1641576014}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_411789275}

[*[priority]{lang="EN-US"}*]{#struct_0_16135_x6401_1759970689}[：表示编解码的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[，数值越小表示优先级越高。]{style="font-family:宋体"}

[**[g711alaw]{lang="EN-US"}**]{#struct_0_16135_x6401_1341137905}[：表示]{style="font-family:宋体"}[G.711]{lang="EN-US"}[的]{style="font-family:宋体"}[A]{lang="EN-US"}[律编解码方式，带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，通常被欧洲采用。]{style="font-family:宋体"}

[**[g711ulaw]{lang="EN-US"}**]{#struct_0_16135_x6401_x1022165840}[：表示]{style="font-family:宋体"}[G.711]{lang="EN-US"}[的]{style="font-family:宋体"}[m]{lang="EN-US" style="font-family:Symbol"}[律编解码方式，带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，通常被北美和日本等国家采用。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_16135_x6401_x20927009}[：表示]{style="font-family:宋体"}[G.723.1 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[5.3kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g723r63]{lang="EN-US"}**]{#struct_0_16135_x6401_1491923127}[：表示]{style="font-family:宋体"}[G.723.1 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[6.3kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g726r16]{lang="EN-US"}**]{#struct_0_16135_x6401_1871378867}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[16kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r24]{lang="EN-US"}**]{#struct_0_16135_x6401_x699428784}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[24kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r32]{lang="EN-US"}**]{#struct_0_16135_x6401_x1641641550}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码，带宽为]{style="font-family:宋体"}[32kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r40]{lang="EN-US"}**]{#struct_0_16135_x6401_1524689435}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[40kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g729a]{lang="EN-US"}**]{#struct_0_16135_x6401_x1256436465}[：表示]{style="font-family:宋体"}[G.729 Annex A]{lang="EN-US"}[编解码方式，对]{style="font-family:宋体"}[G.729]{lang="EN-US"}[编解码进行了一系列简化，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g729br8]{lang="EN-US"}**]{#struct_0_16135_x6401_x867123540}[：表示]{style="font-family:宋体"}[G.729 Annex B]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g729r8]{lang="EN-US"}**]{#struct_0_16135_x6401_1474395790}[：表示]{style="font-family:宋体"}[G.729]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bytes]{lang="EN-US"}**[ *payload-size*]{lang="EN-US"}]{#struct_0_16135_x6401_x1834970380}[：每秒发送的编码字节数，取值范围和选择的编解码有关：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g711alaw]{lang="EN-US"}**]{#struct_0_16135_x6401_x2088404211}[和]{style="font-family:宋体"}**[g711ulaw]{lang="EN-US"}**[的取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[8]{lang="EN-US"}[的倍数），]{style="font-family:宋体"}[80]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[80]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g723r53]{lang="EN-US"}**]{#struct_0_16135_x6401_781265534}[的取值范围为]{style="font-family:
宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g723r63]{lang="EN-US"}**]{#struct_0_16135_x6401_x458864570}[的取值范围为]{style="font-family:
宋体"}[24]{lang="EN-US"}[～]{style="font-family:宋体"}[144]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[24]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r16]{lang="EN-US"}**]{#struct_0_16135_x6401_x1641707086}[的取值范围为]{style="font-family:
宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[220]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r24]{lang="EN-US"}**]{#struct_0_16135_x6401_x1316768920}[的取值范围为]{style="font-family:
宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[210]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[30]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r32]{lang="EN-US"}**]{#struct_0_16135_x6401_418358839}[的取值范围为]{style="font-family:
宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[40]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r40]{lang="EN-US"}**]{#struct_0_16135_x6401_x246891087}[的取值范围为]{style="font-family:
宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[50]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g729a]{lang="EN-US"}**]{#struct_0_16135_x6401_x2034727307}[、]{style="font-family:
宋体"}**[g729br8]{lang="EN-US"}**[和]{style="font-family:
宋体"}**[729r8]{lang="EN-US"}**[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[10]{lang="EN-US"}[的倍数）。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}**[g711]{lang="EN-US"}**]{#struct_0_16135_x6401_x1388707015}[为]{style="font-family:宋体"}[160]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g723r63]{lang="EN-US"}**[为]{style="font-family:宋体"}[24]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g723r53]{lang="EN-US"}**[为]{style="font-family:宋体"}[20]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r16]{lang="EN-US"}**[为]{style="font-family:宋体"}[60]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r24]{lang="EN-US"}**[为]{style="font-family:宋体"}[90]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r32]{lang="EN-US"}**[为]{style="font-family:宋体"}[120]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r40]{lang="EN-US"}**[为]{style="font-family:宋体"}[150]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g729]{lang="EN-US"}**[为]{style="font-family:宋体"}[30]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x606208657}

[[关于各编解码的介绍请参见]{style="font-family:宋体"}**[codec]{lang="EN-US"}**]{#struct_0_16135_x6401_1332712852}[命令中的使用指导。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_18415093}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x1641772622}[配置编解码模版]{style="font-family:宋体"}[1]{lang="EN-US"}[的第一优先级编解码为]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_1758178355}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice class codec 1]{lang="EN-US"}

[\[Sysname-voice-class-codec1\] codec preference 1 g711alaw]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404794348}[]{#struct_0_16135_x6401_x1042691636}[]{#_Toc355262296}

**语音实体 \-- 语音实体命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_16135_x6401_x1934405412}[命令用来配置语音实体的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_16135_x6401_1140997284}[命令用来删除已配置的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1809841072}

[**[description]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_16135_x6401_562665346}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_16135_x6401_x83590796}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641838158}

[[没有配置语音实体的描述信息。]{style="font-family:宋体"}]{#struct_0_16135_x6401_1056531468}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x973885491}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1627742427}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_738466994}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1079979141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_953227889}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x916727867}

[*[string]{lang="EN-US"}*]{#struct_0_16135_x6401_x1243658407}[：语音实体的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641903694}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_368549016}[配置语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[room10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_543190901}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] description room10]{lang="EN-US"}
:::

::: {#1417918335 .myid}
[]{#_Toc404794349}[]{#struct_0_16135_x6401_x1741174290}

**语音实体 \-- 语音实体命令 \-- display voice call**

------------------------------------------------------------------------

[**[display voice call]{lang="EN-US"}**]{#struct_0_16135_x6401_x1810067950}[命令用来显示正在呼叫的语音控制信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1789121468}

[**[display voice call]{lang="EN-US"}**]{#struct_0_16135_x6401_38551247}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1903772327}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_1202534997}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1578240580}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1908270648}

[[network-operator]{lang="EN-US"}]{#struct_0_16135_x6401_x1741108754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1047658588}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16135_x6401_2013915252}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1022776615}

[[一路基本的语音呼叫由两个]{style="font-family:宋体"}[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x2120332726}[组成，一个入呼叫]{style="font-family:宋体"}[Leg]{lang="EN-US"}[和一个出呼叫]{style="font-family:宋体"}[Leg]{lang="EN-US"}[。]{style="font-family:宋体"}[Leg]{lang="EN-US"}[的作用是标识一路呼叫段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x110256564}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x1024738517}[如]{style="font-family:宋体"}[[[[图]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1417918335#_Ref371944607)[所示的组网图，号码]{style="font-family:宋体"}[2222]{lang="EN-US"}[呼叫号码]{style="font-family:宋体"}[11111]{lang="EN-US"}[，并建立通话。在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上使用]{style="font-family:宋体"}**[display voice call]{lang="EN-US"}**[命令显示正在呼叫的语音控制信息。]{style="font-family:宋体"}

[]{#struct_0_16135_x6401_1188317376}[[图1-1 ]{lang="EN-US"}[呼叫组网图]{style="font-family:黑体"}]{#_Ref371944607}

[[![](语音实体命令.files/image002.png){#图片 3 border="0" width="459" height="162"}]{lang="EN-US"}]{#struct_0_16135_x6401_452515173}

[ ]{lang="EN-US"}

[[\<RouterB\> display voice call]{lang="EN-US"}]{#struct_0_16135_x6401_x1741043218}

[Voice call information]{lang="EN-US"}[：]{style="font-family:宋体"}

[Call1]{lang="EN-US"}

[   CallID                   : 6]{lang="EN-US"}

[   Calling number           : 2222]{lang="EN-US"}

[   Called number            : 1111]{lang="EN-US"}

[   Call info-table index    : 0]{lang="EN-US"}

[   Total call-legs          : 2]{lang="EN-US"}

[   Leg 1]{lang="EN-US"}

[      LegID                 : 10]{lang="EN-US"}

[      Leg type              : Call-Leg]{lang="EN-US"}

[      Status                : Connected]{lang="EN-US"}

[      Call reference ID     : 3]{lang="EN-US"}

[      Signal protocol       : LGS]{lang="EN-US"}

[      Voice line            : 2/1/2]{lang="EN-US"}

[   Leg 2]{lang="EN-US"}

[      LegID                 : 11]{lang="EN-US"}

[      Leg type              : Call-Leg]{lang="EN-US"}

[      Status                : Connected]{lang="EN-US"}

[      Call reference ID     : 4]{lang="EN-US"}

[      Signal protocol       : SIP]{lang="EN-US"}

[      Target SIP address    : 192.168.2.1:5060]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x2081336913}[如]{style="font-family:宋体"}[[[[图]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1417918335#_Ref371944607)[所示的组网图，号码]{style="font-family:宋体"}[1111]{lang="EN-US"}[呼叫号码]{style="font-family:宋体"}[2222]{lang="EN-US"}[，并建立通话，]{style="font-family:宋体"}[2222]{lang="EN-US"}[作为呼叫保持发起方进行拍叉操作。在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上使用]{style="font-family:宋体"}**[display voice call]{lang="EN-US"}**[命令显示正在呼叫的语音控制信息。]{style="font-family:宋体"}

[[\<RouterB\> display voice call]{lang="EN-US"}]{#struct_0_16135_x6401_x1740977682}

[Voice call information]{lang="EN-US"}[：]{style="font-family:宋体"}

[Call1]{lang="EN-US"}

[   CallID                   : 7]{lang="EN-US"}

[   Calling number           : 1111]{lang="EN-US"}

[   Called number            : 2222]{lang="EN-US"}

[   Call info-table index    : 0]{lang="EN-US"}

[   Total call-legs          : 2]{lang="EN-US"}

[   Leg 1]{lang="EN-US"}

[      LegID                 : 17]{lang="EN-US"}

[      Leg type              : Call-Leg]{lang="EN-US"}

[      Status                : Connected]{lang="EN-US"}

[      Call reference ID     : 7]{lang="EN-US"}

[      Signal protocol       : SIP]{lang="EN-US"}

[      Target SIP address    : 192.168.2.1:5060]{lang="EN-US"}

[   Leg 2]{lang="EN-US"}

[      LegID                 : 18]{lang="EN-US"}

[      Leg type              : Call-Leg]{lang="EN-US"}

[      Status                : Connected]{lang="EN-US"}

[      Call reference ID     : 14]{lang="EN-US"}

[      Signal protocol       : LGS]{lang="EN-US"}

[      Voice line            : 2/1/2]{lang="EN-US"}

[      Number of services    : 1]{lang="EN-US"}

[      Service name          : CH]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display voice call]{lang="EN-US"}]{#struct_0_16135_x6401_x529565977}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x691623153}[[字段]{style="font-family:黑体"}]{#struct_0_16135_x6401_469279596}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16135_x6401_x754933279}

[[CallID]{lang="EN-US"}]{#struct_0_16135_x6401_102143257}

[[标识一路呼叫，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16135_x6401_x1989600113}[～]{style="font-family:宋体"}[999]{lang="EN-US"}

[[Calling number]{lang="EN-US"}]{#struct_0_16135_x6401_x1366052447}

[[主叫号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1293110013}

[[Called number]{lang="EN-US"}]{#struct_0_16135_x6401_x1740912146}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1883448730}

[[Call info-table index]{lang="EN-US"}]{#struct_0_16135_x6401_x1783387795}

[[呼叫信息表索引]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1278593715}

[[Total call-legs]{lang="EN-US"}]{#struct_0_16135_x6401_x1693230231}

[[呼叫]{style="font-family:宋体"}[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_1703116194}[的数量，取值范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}

[[LegID]{lang="EN-US"}]{#struct_0_16135_x6401_x1313600265}

[[唯一的标示一路呼叫]{style="font-family:宋体"}[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x168690548}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}

[[Leg type]{lang="EN-US"}]{#struct_0_16135_x6401_x1740846610}

[[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_1438428278}[的类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Call_Leg]{lang="EN-US"}]{#struct_0_16135_x6401_1562229100}[：呼叫相关的]{lang="EN-US" style="font-family:宋体"}[Leg]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Temp_Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x1199234096}[：临时]{style="font-family:宋体"}[Leg]{lang="EN-US"}[，在设备作为]{style="font-family:宋体"}[SIP trunk]{lang="EN-US"}[时，会出现该类型的]{style="font-family:宋体"}[Leg]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MOH_Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x514613352}[：音乐保持业务]{lang="EN-US" style="font-family:宋体"}[Leg]{lang="EN-US"}

[[Status]{lang="EN-US"}]{#struct_0_16135_x6401_x1142786798}

[[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x1569832571}[的状态，]{style="font-family:宋体"}[Leg]{lang="EN-US"}[的类型不同，状态也不相同]{style="font-family:宋体"}

[[呼叫相关的]{style="font-family:宋体"}[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x1740781074}[（]{style="font-family:宋体"}[Call_Leg]{lang="EN-US"}[）的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finding-route]{lang="EN-US"}]{#struct_0_16135_x6401_966967336}[：等待路由查询响应]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming_ACK]{lang="EN-US"}]{#struct_0_16135_x6401_x1982804228}[：入呼叫应答状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Outgoing_ACK]{lang="EN-US"}]{#struct_0_16135_x6401_1528987738}[：出呼叫应答状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connected]{lang="EN-US"}]{#struct_0_16135_x6401_x1482965474}[：呼叫已连接状态]{lang="EN-US" style="font-family:宋体"}

[[音乐保持业务]{style="font-family:宋体"}[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_718626275}[（]{style="font-family:宋体"}[MOH_Leg]{lang="EN-US"}[）的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Waiting-music-response]{lang="EN-US"}]{#struct_0_16135_x6401_622752887}[：等待音乐服务器响应状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MOH_connected]{lang="EN-US"}]{#struct_0_16135_x6401_x1741764114}[：已经和音乐服务器建立连接]{lang="EN-US" style="font-family:宋体"}

[[Temp_Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x1074557124}[没有状态，该]{style="font-family:宋体"}[Leg]{lang="EN-US"}[的]{style="font-family:宋体"}[Status]{lang="EN-US"}[字段显示为]{style="font-family:宋体"}[-NA-]{lang="EN-US"}

[[Call reference ID]{lang="EN-US"}]{#struct_0_16135_x6401_x7195584}

[[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_2113378489}[对应的呼叫协议控制块]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Signal protocol ]{lang="EN-US"}]{#struct_0_16135_x6401_x1583768351}

[[该]{style="font-family:宋体"}[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x257488651}[的信令类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[SIP]{lang="EN-US"}]{#struct_0_16135_x6401_830314340}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[LGS]{lang="EN-US"}]{#struct_0_16135_x6401_x1741698578}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2]{lang="EN-US"}]{#struct_0_16135_x6401_x737847665}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[E&M]{lang="EN-US"}]{#struct_0_16135_x6401_673482051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVA]{lang="EN-US"}]{#struct_0_16135_x6401_x825362276}

[[Voice line]{lang="EN-US"}]{#struct_0_16135_x6401_x1773606348}

[[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_1534501557}[使用的语音用户线]{style="font-family:宋体"}

[[Number of services]{lang="EN-US"}]{#struct_0_16135_x6401_x1741239827}

[[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_2066981807}[上的语音业务的数量]{style="font-family:宋体"}

[[Service name]{lang="EN-US"}]{#struct_0_16135_x6401_593214109}

[[Leg]{lang="EN-US"}]{#struct_0_16135_x6401_x1704751258}[上语音业务的名称：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CH]{lang="EN-US"}]{#struct_0_16135_x6401_x555061973}[：呼叫保持业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CW]{lang="EN-US"}]{#struct_0_16135_x6401_x1270579960}[：呼叫等待业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCH]{lang="EN-US"}]{#struct_0_16135_x6401_207634364}[：多方保持业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MOH]{lang="EN-US"}]{#struct_0_16135_x6401_x1741174291}[：音乐保持业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CT]{lang="EN-US"}]{#struct_0_16135_x6401_x243984009}[：]{lang="EN-US" style="font-family:宋体"}[SIP to SIP]{lang="EN-US"}[的呼叫转接业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CF]{lang="EN-US"}]{#struct_0_16135_x6401_1751465799}[：]{lang="EN-US" style="font-family:宋体"}[SIP to SIP]{lang="EN-US"}[的呼叫前转业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CB]{lang="EN-US"}]{#struct_0_16135_x6401_1134615950}[：呼叫备份业务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CFO]{lang="EN-US"}]{#struct_0_16135_x6401_845401549}[：呼叫前转业务发起方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CTO]{lang="EN-US"}]{#struct_0_16135_x6401_448133020}[：呼叫转接业务发起方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CTR]{lang="EN-US"}]{#struct_0_16135_x6401_x1410637232}[：呼叫转接业务接收方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CTT]{lang="EN-US"}]{#struct_0_16135_x6401_x1741108755}[：呼叫转接业务目的方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Conference]{lang="EN-US"}]{#struct_0_16135_x6401_x518425353}[：三方会议业务]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#2065974533 .myid}
[]{#_Toc404794350}[]{#struct_0_16135_x6401_x1401081010}[]{#_Toc355262292}[]{#_Toc299461496}[]{#_Toc94588230}[]{#_Toc80176777}

**语音实体 \-- 语音实体命令 \-- display voice call-info**

------------------------------------------------------------------------

[**[display voice call-info]{lang="EN-US"}**]{#struct_0_16135_x6401_1177073012}[命令用来显示正在呼叫的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x287790687}

[**[display voice call-info ]{lang="EN-US"}**[{ *tag* **\| all** }]{lang="EN-US"}]{#struct_0_16135_x6401_x2007743211}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641969230}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_x2021280718}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1548404469}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_568169693}

[[network-operator]{lang="EN-US"}]{#struct_0_16135_x6401_x358920088}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1238954742}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16135_x6401_590102924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x295818155}

[*[tag]{lang="EN-US"}*]{#struct_0_16135_x6401_1792967116}[：呼叫的标签号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[511]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_16135_x6401_x599536609}[：显示所有呼叫信息的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1642034766}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_629755163}[显示所有正在呼叫的信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice call-info all]{lang="EN-US"}]{#struct_0_16135_x6401_871810501}

[Call tag 0]{lang="EN-US"}

[   Caller number : 5000]{lang="EN-US"}

[   Called number : 1000]{lang="EN-US"}

[   Call direction : From packet switch]{lang="EN-US"}

[   Voice interface index : 0x00000000]{lang="EN-US"}

[   Voice entity currently used : 1]{lang="EN-US"}

[   Voice entities offered : 1]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display voice call-info]{lang="EN-US"}]{#struct_0_16135_x6401_1115520158}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x643736933}[[字段]{style="font-family:黑体"}]{#struct_0_16135_x6401_x466549633}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641418521}

[[Call tag]{lang="EN-US"}]{#struct_0_16135_x6401_x1641051726}

[[呼叫信息的标签号]{style="font-family:宋体"}]{#struct_0_16135_x6401_2005745942}

[[Caller number]{lang="EN-US"}]{#struct_0_16135_x6401_1951817301}

[[主叫号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_1681847244}

[[Called number]{lang="EN-US"}]{#struct_0_16135_x6401_x1942432706}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_1854001074}

[[Call direction]{lang="EN-US"}]{#struct_0_16135_x6401_x1641117262}

[[该次呼叫的呼叫方向：]{style="font-family:宋体"}]{#struct_0_16135_x6401_1396105761}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[From packet switch]{lang="EN-US"}]{#struct_0_16135_x6401_x1743931807}[：由]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[网络发起的呼叫]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[From circuit switch]{lang="EN-US"}]{#struct_0_16135_x6401_967746529}[：由]{lang="EN-US" style="font-family:
  宋体"}[PSTN]{lang="EN-US"}[网络发起的呼叫]{lang="EN-US" style="font-family:
  宋体"}

[[Voice interface index]{lang="EN-US"}]{#struct_0_16135_x6401_294891508}

[[发起当前呼叫的语音接口索引]{style="font-family:宋体"}]{#struct_0_16135_x6401_981260339}

[[Voice entity currently used]{lang="EN-US"}]{#struct_0_16135_x6401_x1641576013}

[[当前呼叫使用的语音实体]{style="font-family:宋体"}]{#struct_0_16135_x6401_x347725612}

[[Voice entities offered]{lang="EN-US"}]{#struct_0_16135_x6401_x623463519}

[[可以提供进行该呼叫的所有语音实体]{style="font-family:宋体"}]{#struct_0_16135_x6401_2125881129}

[]{#_Toc296158434}[]{#_Toc296159749}[]{#_Toc296158436}[]{#_Toc296159751}[]{#_Toc296158437}[]{#_Toc296159752}[]{#_Toc296158438}[]{#_Toc296159753}[]{#_Toc296158439}[]{#_Toc296159754}[]{#_Toc296158440}[]{#_Toc296159755}[]{#_Toc296158441}[]{#_Toc296159756}[]{#_Toc296158442}[]{#_Toc296159757}[]{#_Toc296158443}[]{#_Toc296159758}[]{#_Toc296158444}[]{#_Toc296159759}[]{#_Toc296158445}[]{#_Toc296159760}[]{#_Toc296158446}[]{#_Toc296159761}[]{#_Toc296158447}[]{#_Toc296159762}[]{#_Toc296158448}[]{#_Toc296159763}[]{#_Toc296158449}[]{#_Toc296159764}[]{#_Toc296158450}[]{#_Toc296159765}[]{#_Toc296158451}[]{#_Toc296159766}[]{#_Toc296158452}[]{#_Toc296159767}[]{#_Toc296158453}[]{#_Toc296159768}[]{#_Toc296158454}[]{#_Toc296159769}[]{#_Toc296158455}[]{#_Toc296159770}[]{#_Toc296158456}[]{#_Toc296159771}[]{#_Toc296158457}[]{#_Toc296159772}[]{#_Toc296158458}[]{#_Toc296159773}[]{#_Toc296158459}[]{#_Toc296159774}[]{#_Toc296158460}[]{#_Toc296159775}[]{#_Toc296158461}[]{#_Toc296159776}[]{#_Toc296158462}[]{#_Toc296159777}[]{#_Toc296158463}[]{#_Toc296159778}[]{#_Toc296158464}[]{#_Toc296159779}[]{#_Toc296158465}[]{#_Toc296159780}[]{#_Toc296158469}[]{#_Toc296159784}[]{#_Toc296158476}[]{#_Toc296159791}[]{#_Toc296158477}[]{#_Toc296159792}[]{#_Toc296158478}[]{#_Toc296159793}[]{#_Toc296158487}[]{#_Toc296159802}[]{#_Toc296158488}[]{#_Toc296159803}[]{#_Toc296158534}[]{#_Toc296159849}[]{#_Toc296158536}[]{#_Toc296159851}[]{#_Toc296158537}[]{#_Toc296159852}[]{#_Toc296158538}[]{#_Toc296159853}[]{#_Toc296158539}[]{#_Toc296159854}[]{#_Toc296158540}[]{#_Toc296159855}[]{#_Toc296158541}[]{#_Toc296159856}[]{#_Toc296158542}[]{#_Toc296159857}[]{#_Toc296158543}[]{#_Toc296159858}[]{#_Toc296158544}[]{#_Toc296159859}[]{#_Toc296158545}[]{#_Toc296159860}[]{#_Toc296158546}[]{#_Toc296159861}[]{#_Toc296158547}[]{#_Toc296159862}[]{#_Toc296158548}[]{#_Toc296159863}[]{#_Toc296158549}[]{#_Toc296159864}[]{#_Toc296158550}[]{#_Toc296159865}[]{#_Toc296158551}[]{#_Toc296159866}[]{#_Toc296158552}[]{#_Toc296159867}[]{#_Toc296158553}[]{#_Toc296159868}[]{#_Toc296158554}[]{#_Toc296159869}[]{#_Toc296158556}[]{#_Toc296159871}[]{#_Toc296158557}[]{#_Toc296159872}[]{#_Toc296158562}[]{#_Toc296159877}[]{#_Toc296158584}[]{#_Toc296159899}[]{#_Toc296158586}[]{#_Toc296159901}[]{#_Toc296158587}[]{#_Toc296159902}[]{#_Toc296158588}[]{#_Toc296159903}[]{#_Toc296158589}[]{#_Toc296159904}[]{#_Toc296158590}[]{#_Toc296159905}[]{#_Toc296158591}[]{#_Toc296159906}[]{#_Toc296158592}[]{#_Toc296159907}[]{#_Toc296158593}[]{#_Toc296159908}[]{#_Toc296158594}[]{#_Toc296159909}[]{#_Toc296158595}[]{#_Toc296159910}[]{#_Toc296158596}[]{#_Toc296159911}[]{#_Toc296158597}[]{#_Toc296159912}[]{#_Toc296158598}[]{#_Toc296159913}[]{#_Toc296158599}[]{#_Toc296159914}[]{#_Toc296158600}[]{#_Toc296159915}[]{#_Toc296158601}[]{#_Toc296159916}[]{#_Toc296158602}[]{#_Toc296159917}[]{#_Toc296158603}[]{#_Toc296159918}[]{#_Toc296158604}[]{#_Toc296159919}[]{#_Toc296158605}[]{#_Toc296159920}[]{#_Toc296158606}[]{#_Toc296159921}[]{#_Toc296158607}[]{#_Toc296159922}[]{#_Toc296158608}[]{#_Toc296159923}[]{#_Toc296158609}[]{#_Toc296159924}[]{#_Toc296158610}[]{#_Toc296159925}[]{#_Toc296158611}[]{#_Toc296159926}[]{#_Toc296158612}[]{#_Toc296159927}[]{#_Toc296158613}[]{#_Toc296159928}[]{#_Toc296158614}[]{#_Toc296159929}[]{#_Toc296158615}[]{#_Toc296159930}[]{#_Toc296158625}[]{#_Toc296159940}[]{#_Toc296158626}[]{#_Toc296159941}[]{#_Toc296158648}[]{#_Toc296159963}[ ]{lang="EN-US"}

::: {#-970573354 .myid}
[]{#_Toc404794351}[]{#struct_0_16135_x6401_655530740}[]{#_Toc355262293}

**语音实体 \-- 语音实体命令 \-- display voice entity**

------------------------------------------------------------------------

[**[display voice entity]{lang="EN-US"}**]{#struct_0_16135_x6401_x142616917}[命令用来显示语音实体的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641641549}

[**[display]{lang="EN-US"}**[ **voice** **entity** { *entity-tag* **\|** **all** \| **ivr** \| **pots** \| **voip** }]{lang="EN-US"}]{#struct_0_16135_x6401_x1560489816}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1637213321}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_x663392719}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1580070345}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_683741291}

[[network-operator]{lang="EN-US"}]{#struct_0_16135_x6401_x1377181623}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x42886861}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16135_x6401_x501438797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641707085}

[*[entity-tag]{lang="EN-US"}*]{#struct_0_16135_x6401_1412114435}[：显示指定语音实体的配置信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_16135_x6401_x1994926223}[：表示显示所有语音实体的配置信息。]{style="font-family:宋体"}

[**[ivr]{lang="EN-US"}**]{#struct_0_16135_x6401_1525387894}[：表示显示所有]{style="font-family:宋体"}[IVR]{lang="EN-US"}[语音实体的配置信息。]{style="font-family:宋体"}

[**[pots]{lang="EN-US"}**]{#struct_0_16135_x6401_1592816563}[：表示显示所有]{style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体的配置信息。]{style="font-family:宋体"}

[**[voip]{lang="EN-US"}**]{#struct_0_16135_x6401_1520779488}[：表示显示所有]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1003506937}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_2096172156}[显示所有语音实体的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice entity all]{lang="EN-US"}]{#struct_0_16135_x6401_x1641903693}

[POTS 9999]{lang="EN-US"}

[   Current state: Up]{lang="EN-US"}

[   Description: entity9999]{lang="EN-US"}

[   Priority level: 0]{lang="EN-US"}

[   Match template: 9999]{lang="EN-US"}

[   Voice line: 2/2/1]{lang="EN-US"}

[   Dial prefix: Not configured]{lang="EN-US"}

[   Send number: All]{lang="EN-US"}

[   Max connections: 50]{lang="EN-US"}

[   Codec: g723r53; bytes: 80; vad: Disabled]{lang="EN-US"}

[   Caller permit: 1]{lang="EN-US"}

[   Caller group: permit group 1]{lang="EN-US"}

[   Substitute called: 9999]{lang="EN-US"}

[   Substitute calling: 9999]{lang="EN-US"}

[   DTMF relay: Outband-NTE]{lang="EN-US"}

[   RTP payload-type for NTE: 113]{lang="EN-US"}

[   Playout mode: adaptive]{lang="EN-US"}

[   Playout initial delay: 30 ms]{lang="EN-US"}

[   Playout minimum delay: 10 ms]{lang="EN-US"}

[   Playout maximum delay: 160 ms]{lang="EN-US"}

[   IP media DSCP: ef]{lang="EN-US"}

[   IP signaling DSCP: ef]{lang="EN-US"}

[   Register number: Enabled]{lang="EN-US"}

[   Call-forwarding no-reply number: 5555]{lang="EN-US"}

[   Call-forwarding on-busy number: 6666]{lang="EN-US"}

[   Call-forwarding unavailable number: 7777]{lang="EN-US"}

[   Call-forwarding unconditional number: 8888]{lang="EN-US"}

[   Authentication info: ]{lang="EN-US"}

[     Username: 1000]{lang="EN-US"}

[     Password: \*\*\*\*\*\*]{lang="EN-US"}

[     Realm: abc.com]{lang="EN-US"}

[ ]{lang="EN-US"}

[VoIP 8888]{lang="EN-US"}

[   Current state: Up]{lang="EN-US"}

[   Description: Not configured]{lang="EN-US"}

[   Priority level: 0]{lang="EN-US"}

[   Match template: 8888]{lang="EN-US"}

[   Target SIP address: 1.1.1.1]{lang="EN-US"}

[   Max connections: 10]{lang="EN-US"}

[   Caller permit: 1]{lang="EN-US"}

[   Caller group: permit group 1]{lang="EN-US"}

[   Substitute called: 9999]{lang="EN-US"}

[   Substitute calling: 9999]{lang="EN-US"}

[   DTMF relay: Outband-SIP]{lang="EN-US"}

[   Playout mode: adaptive]{lang="EN-US"}

[   Playout initial delay: 30 ms]{lang="EN-US"}

[   Playout minimum delay: 10 ms]{lang="EN-US"}

[   Playout maximum delay: 160 ms]{lang="EN-US"}

[   IP media DSCP: ef]{lang="EN-US"}

[   Codec transparent: Disabled]{lang="EN-US"}

[   Media flow-around: Enabled]{lang="EN-US"}

[   Voice class SIP early-offer forced: Disabled]{lang="EN-US"}

[   Voice class SIP URI scheme: Global]{lang="EN-US"}

[   Voice class SIP bind media source-interface: GigabitEthernet2/1/1]{lang="EN-US"}

[   Voice class SIP bind control source-interface: GigabitEthernet2/1/1]{lang="EN-US"}

[   Voice class SIP keepalive up-interval: 60 s ]{lang="EN-US"}

[   Voice class SIP keepalive down-interval: 30 s]{lang="EN-US"}

[   Voice class SIP keepalive retry: 5]{lang="EN-US"}

[   Fax protocol: standard-t38; ls-redundancy: 0; hs-redundancy: 0]{lang="EN-US"}

[   Fax cng-switch: Disabled]{lang="EN-US"}

[   Fax level: -15]{lang="EN-US"}

[   Fax local-train threshold: 10]{lang="EN-US"}

[   Fax nsf: 0x000000 ]{lang="EN-US"}

[   Fax rate: Voice]{lang="EN-US"}

[   Fax train-mode: PPP]{lang="EN-US"}

[   Fax ecm: Disabled]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display voice entity]{lang="EN-US"}]{#struct_0_16135_x6401_x1553765285}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x649922213}[[字段]{style="font-family:黑体"}]{#struct_0_16135_x6401_1247068653}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16135_x6401_x460789583}

[[VoIP *entity-number*]{lang="EN-US"}]{#struct_0_16135_x6401_x2050035406}

[[语音实体类型和语音实体号]{style="font-family:宋体"}]{#struct_0_16135_x6401_142559189}

[[目前支持的语音实体类型包括：]{style="font-family:宋体"}[VoIP]{lang="EN-US"}]{#struct_0_16135_x6401_1387571169}[、]{style="font-family:宋体"}[POTS]{lang="EN-US"}[、]{style="font-family:宋体"}[IVR]{lang="EN-US"}

[[Current state]{lang="EN-US"}]{#struct_0_16135_x6401_x1641969229}

[[语音实体状态：]{style="font-family:宋体"}]{#struct_0_16135_x6401_x98900881}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_16135_x6401_1361157933}[：语音实体处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_16135_x6401_1390445545}[：语音实体处于关闭状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_16135_x6401_x155601418}

[[语音实体的描述信息。]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_16135_x6401_x661094865}[表示没有配置语音实体的描述信息]{style="font-family:宋体"}

[[Priority level]{lang="EN-US"}]{#struct_0_16135_x6401_x1642034765}

[[语音实体的优先级]{style="font-family:宋体"}]{#struct_0_16135_x6401_226470636}

[[Match template]{lang="EN-US"}]{#struct_0_16135_x6401_146997972}

[[语音实体的号码模板]{style="font-family:宋体"}]{#struct_0_16135_x6401_162538086}

[[Target SIP address]{lang="EN-US"}]{#struct_0_16135_x6401_x1486212092}

[[语音实体的呼叫目的地址]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1641051725}

[[Voice line]{lang="EN-US"}]{#struct_0_16135_x6401_x723137413}

[[绑定到语音实体的语音用户线]{style="font-family:宋体"}]{#struct_0_16135_x6401_1906150456}

[[Dial prefix]{lang="EN-US"}]{#struct_0_16135_x6401_1303585744}

[[配置的拨号前缀]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1060017590}

[[Send number]{lang="EN-US"}]{#struct_0_16135_x6401_x1641117261}

[[号码发送类型：]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1332777594}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[All]{lang="EN-US"}]{#struct_0_16135_x6401_126153120}[：发送全部被叫号码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Truncate]{lang="EN-US"}]{#struct_0_16135_x6401_x1641576016}[：按号码截断方式发送被叫号码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[number]{lang="EN-US"}]{#struct_0_16135_x6401_x751010139}[：号码发送的长度]{style="font-family:宋体"}

[[Max connections]{lang="EN-US"}]{#struct_0_16135_x6401_x2004684377}

[[最大连接呼叫数]{style="font-family:宋体"}]{#struct_0_16135_x6401_x509181797}

[[Codec: *codec* ; bytes: *bytes* ; vad:]{lang="EN-US"}]{#struct_0_16135_x6401_x1641641552}

[[语音编解码，]{style="font-family:宋体"}]{#struct_0_16135_x6401_361890021}

[[每秒发送的编码字节数，]{style="font-family:宋体"}]{#struct_0_16135_x6401_1346239386}

[[静音抑制功能的状态：]{style="font-family:宋体"}]{#struct_0_16135_x6401_841047427}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_x1641707088}[：静音抑制功能处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_1459168602}[：静音抑制功能处于关闭状态]{lang="EN-US" style="font-family:宋体"}

[[Caller permit]{lang="EN-US"}]{#struct_0_16135_x6401_x1641772624}

[[允许呼出]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16135_x6401_951609301}[呼入的主叫号码模板]{style="font-family:宋体"}

[[Caller group]{lang="EN-US"}]{#struct_0_16135_x6401_1447281884}

[[绑定到语音实体的用户组]{style="font-family:宋体"}]{#struct_0_16135_x6401_131184811}

[[Substitute called]{lang="EN-US"}]{#struct_0_16135_x6401_x1641838160}

[[绑定到语音实体的号码变换规则表，对被叫号码应用号码变换]{style="font-family:宋体"}]{#struct_0_16135_x6401_1412565220}

[[Substitute calling]{lang="EN-US"}]{#struct_0_16135_x6401_724197969}

[[绑定到语音实体的号码变换规则表，对主叫号码应用号码变换]{style="font-family:宋体"}]{#struct_0_16135_x6401_x2066332507}

[[DTMF relay]{lang="EN-US"}]{#struct_0_16135_x6401_x1641903696}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Outband-SIP]{lang="EN-US"}]{#struct_0_16135_x6401_x794250398}[：将]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号封装为]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Outband-NTE]{lang="EN-US"}]{#struct_0_16135_x6401_858203515}[：将]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号封装为符合]{lang="EN-US" style="font-family:宋体"}[RFC 2833]{lang="EN-US"}[建议的]{lang="EN-US" style="font-family:宋体"}[RTP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inband-voice]{lang="EN-US"}]{#struct_0_16135_x6401_583522308}[：将]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号封装为]{lang="EN-US" style="font-family:宋体"}[RTP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[RTP payload-type for NTE]{lang="EN-US"}]{#struct_0_16135_x6401_x1641969232}

[[使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}]{#struct_0_16135_x6401_x858481304}[方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号时，]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[payload]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Playout mode]{lang="EN-US"}]{#struct_0_16135_x6401_1335721454}

[[缓存语音包的工作模式]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1642034768}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[adaptive]{lang="EN-US"}]{#struct_0_16135_x6401_x1741698579}[：自适应模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fixed]{lang="EN-US"}]{#struct_0_16135_x6401_828236276}[：静态模式]{lang="EN-US" style="font-family:宋体"}

[[Playout initial delay]{lang="EN-US"}]{#struct_0_16135_x6401_x533044251}

[[语音包的初始缓冲时间]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1666511041}

[[Playout minimum delay]{lang="EN-US"}]{#struct_0_16135_x6401_x1641051728}

[[语音包的最小缓冲时间]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1126421940}

[[Playout maximum delay]{lang="EN-US"}]{#struct_0_16135_x6401_86415233}

[[语音包的最大缓冲时间]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1131626430}

[[IP media DSCP]{lang="EN-US"}]{#struct_0_16135_x6401_x1641117264}

[[承载媒体流的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16135_x6401_x2092292481}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Register number]{lang="EN-US"}]{#struct_0_16135_x6401_x1154294666}

[[语音实体会是否向]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_16135_x6401_866959050}[服务器发起注册：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_x1641641551}[：语音实体会向]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器发起注册]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_x1204193920}[：语音实体不会向]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器发起注册]{lang="EN-US" style="font-family:宋体"}

[[Codec transparent]{lang="EN-US"}]{#struct_0_16135_x6401_x1641707087}

[[编解码透传功能的状态：]{style="font-family:宋体"}]{#struct_0_16135_x6401_249315021}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_x590591030}[：编解码透传功能处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_x1641772623}[：编解码透传功能处于关闭状态]{style="font-family:宋体"}

[[Media flow-around]{lang="EN-US"}]{#struct_0_16135_x6401_192094414}

[[媒体旁路功能的状态：]{style="font-family:宋体"}]{#struct_0_16135_x6401_x534552495}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_x1641838159}[：媒体旁路功能处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_x509552473}[：媒体旁路功能处于关闭状态]{lang="EN-US" style="font-family:宋体"}

[[Voice class SIP early-offer forced]{lang="EN-US"}]{#struct_0_16135_x6401_x780400623}

[[DO-EO]{lang="EN-US"}]{#struct_0_16135_x6401_x1641903695}[转换功能的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_1934632957}[：]{style="font-family:宋体"}[DO-EO]{lang="EN-US"}[转换功能处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_x1641969231}[：]{lang="EN-US" style="font-family:宋体"}[DO-EO]{lang="EN-US"}[转换功能处于关闭状态]{lang="EN-US" style="font-family:宋体"}

[[Voice class SIP URI scheme]{lang="EN-US"}]{#struct_0_16135_x6401_1850757765}

[[SIP]{lang="EN-US"}]{#struct_0_16135_x6401_x800211034}[呼叫时使用的]{style="font-family:宋体"}[URL]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global]{lang="EN-US"}]{#struct_0_16135_x6401_x1963010448}[：]{style="font-family:宋体"}[全局使用]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[格式的]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIP]{lang="EN-US"}]{#struct_0_16135_x6401_x40696147}[：指定在]{style="font-family:宋体"}[SIP]{lang="EN-US"}[呼叫时使用]{style="font-family:宋体"}[SIP]{lang="EN-US"}[格式的]{style="font-family:宋体"}[URL]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIPS]{lang="EN-US"}]{#struct_0_16135_x6401_x396926508}[：指定在]{style="font-family:宋体"}[SIP]{lang="EN-US"}[呼叫时使用]{style="font-family:宋体"}[SIPS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[URL]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Voice class SIP bind media]{lang="EN-US"}]{#struct_0_16135_x6401_x455196777}

[[发送的媒体流的源接口]{style="font-family:宋体"}]{#struct_0_16135_x6401_823998047}

[[Voice class SIP bind control]{lang="EN-US"}]{#struct_0_16135_x6401_x1642034767}

[[发送的]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_16135_x6401_x936328778}[信令流的源接口]{style="font-family:宋体"}

[[Voice class codec]{lang="EN-US"}]{#struct_0_16135_x6401_1116964625}

[[绑定到语音实体的编解码模板]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1641051727}

[[Call-forwarding no-reply number]{lang="EN-US"}]{#struct_0_16135_x6401_439662001}

[[无应答呼叫前转的目的号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1641117263}

[[Call-forwarding on-busy number]{lang="EN-US"}]{#struct_0_16135_x6401_x169978180}

[[遇忙呼叫前转的目的号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_x2122351399}

[[Call-forwarding unavailable number]{lang="EN-US"}]{#struct_0_16135_x6401_x1641576018}

[[不可用呼叫前转的目的号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1557579193}

[[Call-forwarding unconditional number]{lang="EN-US"}]{#struct_0_16135_x6401_x1641641554}

[[无条件呼叫前转的目的号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_x800909393}

[[Authentication info: ]{lang="EN-US"}]{#struct_0_16135_x6401_696257347}

[[     Username: *name*]{lang="EN-US"}]{#struct_0_16135_x6401_x1641707090}

[[     Password: \*\*\*\*\*\*]{lang="EN-US"}]{#struct_0_16135_x6401_1815333426}

[[     Realm: *realm*]{lang="EN-US"}]{#struct_0_16135_x6401_x1641772626}

[[注册鉴权信息，包括鉴权用户名、鉴权密码、域名]{style="font-family:宋体"}]{#struct_0_16135_x6401_x211190113}

[[Voice class SIP keepalive up-interval]{lang="EN-US"}]{#struct_0_16135_x6401_x1641838162}

[[在标记语音实体为不可用前，本端发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}]{#struct_0_16135_x6401_249765806}[报文的时间间隔]{style="font-family:宋体"}

[[Voice class SIP keepalive down-interval]{lang="EN-US"}]{#struct_0_16135_x6401_x1641903698}

[[在标记语音实体为可用前，本端发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}]{#struct_0_16135_x6401_1981687124}[报文的时间间隔]{style="font-family:宋体"}

[[Voice class SIP keepalive retry]{lang="EN-US"}]{#struct_0_16135_x6401_354079999}

[[在改变语音实体状态前，重复探测的次数]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1641969234}

[[Fax protocol]{lang="EN-US"}]{#struct_0_16135_x6401_284608288}

[[传真协议]{style="font-family:宋体"}]{#struct_0_16135_x6401_x118676239}

[[Fax cng-switch]{lang="EN-US"}]{#struct_0_16135_x6401_x1574585326}

[[CNG]{lang="EN-US"}]{#struct_0_16135_x6401_1447407702}[传真切换功能的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_241433675}[：]{style="font-family:宋体"}[CNG]{lang="EN-US"}[传真切换功能处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_687892815}[：]{style="font-family:宋体"}[CNG]{lang="EN-US"}[传真切换功能处于关闭状态]{style="font-family:宋体"}

[[Fax level]{lang="EN-US"}]{#struct_0_16135_x6401_x505318572}

[[发送载波能量值]{style="font-family:宋体"}]{#struct_0_16135_x6401_x2040990540}

[[Fax local-train threshold]{lang="EN-US"}]{#struct_0_16135_x6401_1739983933}

[[本地训练阈值百分比]{style="font-family:宋体"}]{#struct_0_16135_x6401_1850692229}

[[Fax nsf]{lang="EN-US"}]{#struct_0_16135_x6401_x878191126}

[[非标准能力协商的国家码和厂商码]{style="font-family:宋体"}]{#struct_0_16135_x6401_1441697119}

[[Fax rate]{lang="EN-US"}]{#struct_0_16135_x6401_x925245293}

[[最高传真速率]{style="font-family:宋体"}]{#struct_0_16135_x6401_640838648}

[[Fax train-mode]{lang="EN-US"}]{#struct_0_16135_x6401_x1281541189}

[[传真的训练方式：]{style="font-family:宋体"}]{#struct_0_16135_x6401_233094424}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_16135_x6401_284542752}[：表示使用本地训练方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_16135_x6401_x118741775}[：表示使用端对端训练方式]{style="font-family:宋体"}

[[Fax ecm]{lang="EN-US"}]{#struct_0_16135_x6401_1447342166}

[[ECM]{lang="EN-US"}]{#struct_0_16135_x6401_994073281}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_16135_x6401_687827279}[：]{style="font-family:
  宋体"}[ECM]{lang="EN-US"}[处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_16135_x6401_x2041056076}[：]{style="font-family:宋体"}[ECM]{lang="EN-US"}[处于关闭状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-985825129 .myid}
[]{#_Toc404794352}[]{#struct_0_16135_x6401_x1741043220}

**语音实体 \-- 语音实体命令 \-- dsp-image**

------------------------------------------------------------------------

[**[dsp-image]{lang="PT-BR"}**]{#struct_0_16135_x6401_x1740977684}[命令用来配置]{style="font-family:宋体"}[DSP]{lang="EN-US"}[（]{style="font-family:宋体"}[Digital Signal Processor]{lang="EN-US"}[，数字信号处理器）镜像文件类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_633233437}

[**[dsp-image]{lang="EN-US"}**[ { **ms** \| **general** }]{lang="EN-US"}]{#struct_0_16135_x6401_777200780}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1231658361}

[[缺省情况下，使用通用]{style="font-family:宋体"}[DSP]{lang="EN-US"}]{#struct_0_16135_x6401_2015899695}[镜像文件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_832907234}

[[语音视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_210646691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_2012741924}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x902200340}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1565986628}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_95672296}

[**[ms]{lang="EN-US"}**]{#struct_0_16135_x6401_1003230396}[：配置]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件为微软认证版本。该类型的]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件可以满足微软认证要求的语音通信质量，但不支持]{style="font-family:宋体"}[G.723]{lang="EN-US"}[编解码。]{style="font-family:宋体"}

[**[general]{lang="EN-US"}**]{#struct_0_16135_x6401_2074092579}[：配置]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件为通用版本。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_399512003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1740912148}[DSP]{lang="EN-US"}[镜像文件后，必须重启设备，配置的]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在和微软]{style="font-family:宋体"}]{#struct_0_16135_x6401_892488792}[Lync Server]{lang="EN-US"}[配合时，请使用微软认证版本的]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件。其他情况，建议使用通用]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1905665580}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1054384722}[配置]{style="font-family:宋体"}[DSP]{lang="EN-US"}[镜像文件为微软认证版本。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_1107382986}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dsp-image ms]{lang="EN-US"}
:::

::: {#-1907836213 .myid}
[]{#_Toc404794353}[]{#struct_0_16135_x6401_304318110}[]{#_Toc355262313}[]{#_Toc345245916}[]{#_Toc346096024}[]{#_Toc345245917}[]{#_Toc346096025}[]{#_Toc345245918}[]{#_Toc346096026}[]{#_Toc345245919}[]{#_Toc346096027}[]{#_Toc345245920}[]{#_Toc346096028}[]{#_Toc345245921}[]{#_Toc346096029}[]{#_Toc345245922}[]{#_Toc346096030}[]{#_Toc345245923}[]{#_Toc346096031}[]{#_Toc345245924}[]{#_Toc346096032}[]{#_Toc345245925}[]{#_Toc346096033}[]{#_Toc345245926}[]{#_Toc346096034}[]{#_Toc345245927}[]{#_Toc346096035}[]{#_Toc345245928}[]{#_Toc346096036}[]{#_Toc345245929}[]{#_Toc346096037}[]{#_Toc345245930}[]{#_Toc346096038}[]{#_Toc345245931}[]{#_Toc346096039}[]{#_Toc345245932}[]{#_Toc346096040}[]{#_Toc345245933}[]{#_Toc346096041}[]{#_Toc345245934}[]{#_Toc346096042}[]{#_Toc345245935}[]{#_Toc346096043}[]{#_Toc345245936}[]{#_Toc346096044}[]{#_Toc345245937}[]{#_Toc346096045}[]{#_Toc345245938}[]{#_Toc346096046}[]{#_Toc345245939}[]{#_Toc346096047}[]{#_Toc345245940}[]{#_Toc346096048}[]{#_Toc345245941}[]{#_Toc346096049}[]{#_Toc345245942}[]{#_Toc346096050}[]{#_Toc345245943}[]{#_Toc346096051}[]{#_Toc345245944}[]{#_Toc346096052}[]{#_Toc345245945}[]{#_Toc346096053}[]{#_Toc345245946}[]{#_Toc346096054}[]{#_Toc345245947}[]{#_Toc346096055}[]{#_Toc345245948}[]{#_Toc346096056}[]{#_Toc345245949}[]{#_Toc346096057}[]{#_Toc345245950}[]{#_Toc346096058}[]{#_Toc345245951}[]{#_Toc346096059}[]{#_Toc345245952}[]{#_Toc346096060}[]{#_Toc345245953}[]{#_Toc346096061}[]{#_Toc345245954}[]{#_Toc346096062}[]{#_Toc345245955}[]{#_Toc346096063}[]{#_Toc345245956}[]{#_Toc346096064}[]{#_Toc345245957}[]{#_Toc346096065}[]{#_Toc345245958}[]{#_Toc346096066}[]{#_Toc345245959}[]{#_Toc346096067}[]{#_Toc345245960}[]{#_Toc346096068}[]{#_Toc345245961}[]{#_Toc346096069}[]{#_Toc345245962}[]{#_Toc346096070}[]{#_Toc345245963}[]{#_Toc346096071}[]{#_Toc345245964}[]{#_Toc346096072}[]{#_Toc345245965}[]{#_Toc346096073}[]{#_Toc345245966}[]{#_Toc346096074}[]{#_Toc345245967}[]{#_Toc346096075}[]{#_Toc345245968}[]{#_Toc346096076}[]{#_Toc345245969}[]{#_Toc346096077}[]{#_Toc296158651}[]{#_Toc296159966}[]{#_Toc296158652}[]{#_Toc296159967}[]{#_Toc296158653}[]{#_Toc296159968}[]{#_Toc296158654}[]{#_Toc296159969}[]{#_Toc296158655}[]{#_Toc296159970}[]{#_Toc296158656}[]{#_Toc296159971}[]{#_Toc296158657}[]{#_Toc296159972}[]{#_Toc296158658}[]{#_Toc296159973}[]{#_Toc296158659}[]{#_Toc296159974}[]{#_Toc296158660}[]{#_Toc296159975}[]{#_Toc296158661}[]{#_Toc296159976}[]{#_Toc296158662}[]{#_Toc296159977}[]{#_Toc296158663}[]{#_Toc296159978}[]{#_Toc296158664}[]{#_Toc296159979}[]{#_Toc296158665}[]{#_Toc296159980}[]{#_Toc296158666}[]{#_Toc296159981}[]{#_Toc296158667}[]{#_Toc296159982}[]{#_Toc296158668}[]{#_Toc296159983}[]{#_Toc296158669}[]{#_Toc296159984}[]{#_Toc296158670}[]{#_Toc296159985}[]{#_Toc296158671}[]{#_Toc296159986}[]{#_Toc296158672}[]{#_Toc296159987}[]{#_Toc296158677}[]{#_Toc296159992}[]{#_Toc296158685}[]{#_Toc296160000}[]{#_Toc296158686}[]{#_Toc296160001}[]{#_Toc296158687}[]{#_Toc296160002}[]{#_Toc296158716}[]{#_Toc296160031}[]{#_Toc296158718}[]{#_Toc296160033}[]{#_Toc296158719}[]{#_Toc296160034}[]{#_Toc296158720}[]{#_Toc296160035}[]{#_Toc296158721}[]{#_Toc296160036}[]{#_Toc296158722}[]{#_Toc296160037}[]{#_Toc296158723}[]{#_Toc296160038}[]{#_Toc296158724}[]{#_Toc296160039}[]{#_Toc296158725}[]{#_Toc296160040}[]{#_Toc296158726}[]{#_Toc296160041}[]{#_Toc296158727}[]{#_Toc296160042}[]{#_Toc296158728}[]{#_Toc296160043}[]{#_Toc296158729}[]{#_Toc296160044}[]{#_Toc296158730}[]{#_Toc296160045}[]{#_Toc296158731}[]{#_Toc296160046}[]{#_Toc296158732}[]{#_Toc296160047}[]{#_Toc296158733}[]{#_Toc296160048}[]{#_Toc296158734}[]{#_Toc296160049}[]{#_Toc296158735}[]{#_Toc296160050}[]{#_Toc296158736}[]{#_Toc296160051}[]{#_Toc296158737}[]{#_Toc296160052}[]{#_Toc296158738}[]{#_Toc296160053}[]{#_Toc296158739}[]{#_Toc296160054}[]{#_Toc296158740}[]{#_Toc296160055}[]{#_Toc296158741}[]{#_Toc296160056}[]{#_Toc296158742}[]{#_Toc296160057}[]{#_Toc296158743}[]{#_Toc296160058}[]{#_Toc296158745}[]{#_Toc296160060}[]{#_Toc296158747}[]{#_Toc296160062}[]{#_Toc296158750}[]{#_Toc296160065}[]{#_Toc296158752}[]{#_Toc296160067}[]{#_Toc296158753}[]{#_Toc296160068}[]{#_Toc296158754}[]{#_Toc296160069}[]{#_Toc296158755}[]{#_Toc296160070}[]{#_Toc296158756}[]{#_Toc296160071}[]{#_Toc296158757}[]{#_Toc296160072}[]{#_Toc296158760}[]{#_Toc296160075}[]{#_Toc296158761}[]{#_Toc296160076}[]{#_Toc296158762}[]{#_Toc296160077}[]{#_Toc296158795}[]{#_Toc296160110}[]{#_Toc137035624}[]{#_Toc137036654}[]{#_Toc137041713}[]{#_Toc137042384}[]{#_Toc87442398}[]{#_Toc87787038}[]{#_Toc87851901}[]{#_Toc87852680}[]{#_Toc87853461}[]{#_Toc87867500}[]{#_Toc87442408}[]{#_Toc87787048}[]{#_Toc87851911}[]{#_Toc87852690}[]{#_Toc87853471}[]{#_Toc87867510}[]{#_Toc87442409}[]{#_Toc87787049}[]{#_Toc87851912}[]{#_Toc87852691}[]{#_Toc87853472}[]{#_Toc87867511}[]{#_Toc87442410}[]{#_Toc87787050}[]{#_Toc87851913}[]{#_Toc87852692}[]{#_Toc87853473}[]{#_Toc87867512}[]{#_Toc87442411}[]{#_Toc87787051}[]{#_Toc87851914}[]{#_Toc87852693}[]{#_Toc87853474}[]{#_Toc87867513}[]{#_Toc87442412}[]{#_Toc87787052}[]{#_Toc87851915}[]{#_Toc87852694}[]{#_Toc87853475}[]{#_Toc87867514}[]{#_Toc87442413}[]{#_Toc87787053}[]{#_Toc87851916}[]{#_Toc87852695}[]{#_Toc87853476}[]{#_Toc87867515}[]{#_Toc87442414}[]{#_Toc87787054}[]{#_Toc87851917}[]{#_Toc87852696}[]{#_Toc87853477}[]{#_Toc87867516}[]{#_Toc87442415}[]{#_Toc87787055}[]{#_Toc87851918}[]{#_Toc87852697}[]{#_Toc87853478}[]{#_Toc87867517}[]{#_Toc87442416}[]{#_Toc87787056}[]{#_Toc87851919}[]{#_Toc87852698}[]{#_Toc87853479}[]{#_Toc87867518}[]{#_Toc87442417}[]{#_Toc87787057}[]{#_Toc87851920}[]{#_Toc87852699}[]{#_Toc87853480}[]{#_Toc87867519}[]{#_Toc87442418}[]{#_Toc87787058}[]{#_Toc87851921}[]{#_Toc87852700}[]{#_Toc87853481}[]{#_Toc87867520}[]{#_Toc87442419}[]{#_Toc87787059}[]{#_Toc87851922}[]{#_Toc87852701}[]{#_Toc87853482}[]{#_Toc87867521}[]{#_Toc87442420}[]{#_Toc87787060}[]{#_Toc87851923}[]{#_Toc87852702}[]{#_Toc87853483}[]{#_Toc87867522}[]{#_Toc87442426}[]{#_Toc87787066}[]{#_Toc87851929}[]{#_Toc87852708}[]{#_Toc87853489}[]{#_Toc87867528}[]{#_Toc35952990}[]{#_Toc35953393}[]{#_Toc35954277}[]{#_Toc35955154}[]{#_Toc296158797}[]{#_Toc296160112}[]{#_Toc296158798}[]{#_Toc296160113}[]{#_Toc296158799}[]{#_Toc296160114}[]{#_Toc296158800}[]{#_Toc296160115}[]{#_Toc296158801}[]{#_Toc296160116}[]{#_Toc296158802}[]{#_Toc296160117}[]{#_Toc296158803}[]{#_Toc296160118}[]{#_Toc296158804}[]{#_Toc296160119}[]{#_Toc296158805}[]{#_Toc296160120}[]{#_Toc296158806}[]{#_Toc296160121}[]{#_Toc296158807}[]{#_Toc296160122}[]{#_Toc296158808}[]{#_Toc296160123}[]{#_Toc296158809}[]{#_Toc296160124}[]{#_Toc296158810}[]{#_Toc296160125}[]{#_Toc296158811}[]{#_Toc296160126}[]{#_Toc296158812}[]{#_Toc296160127}[]{#_Toc296158813}[]{#_Toc296160128}[]{#_Toc296158814}[]{#_Toc296160129}[]{#_Toc296158815}[]{#_Toc296160130}[]{#_Toc296158816}[]{#_Toc296160131}[]{#_Toc296158817}[]{#_Toc296160132}[]{#_Toc296158821}[]{#_Toc296160136}[]{#_Toc296158826}[]{#_Toc296160141}[]{#_Toc296158839}[]{#_Toc296160154}[]{#_Toc296158840}[]{#_Toc296160155}[]{#_Toc296158841}[]{#_Toc296160156}[]{#_Toc296158842}[]{#_Toc296160157}[]{#_Toc296158843}[]{#_Toc296160158}[]{#_Toc296158844}[]{#_Toc296160159}[]{#_Toc296158845}[]{#_Toc296160160}[]{#_Toc296158846}[]{#_Toc296160161}[]{#_Toc296158847}[]{#_Toc296160162}[]{#_Toc296158848}[]{#_Toc296160163}[]{#_Toc296158849}[]{#_Toc296160164}[]{#_Toc296158850}[]{#_Toc296160165}[]{#_Toc296158851}[]{#_Toc296160166}[]{#_Toc296158852}[]{#_Toc296160167}[]{#_Toc296158853}[]{#_Toc296160168}[]{#_Toc296158854}[]{#_Toc296160169}[]{#_Toc296158855}[]{#_Toc296160170}[]{#_Toc296158856}[]{#_Toc296160171}[]{#_Toc296158857}[]{#_Toc296160172}[]{#_Toc296158858}[]{#_Toc296160173}[]{#_Toc296158859}[]{#_Toc296160174}[]{#_Toc296158860}[]{#_Toc296160175}[]{#_Toc296158861}[]{#_Toc296160176}[]{#_Toc296158862}[]{#_Toc296160177}[]{#_Toc296158877}[]{#_Toc296160192}[]{#_Toc296158878}[]{#_Toc296160193}[]{#_Toc296158915}[]{#_Toc296160230}[]{#_Toc296158917}[]{#_Toc296160232}[]{#_Toc296158918}[]{#_Toc296160233}[]{#_Toc296158919}[]{#_Toc296160234}[]{#_Toc296158920}[]{#_Toc296160235}[]{#_Toc296158921}[]{#_Toc296160236}[]{#_Toc296158922}[]{#_Toc296160237}[]{#_Toc296158923}[]{#_Toc296160238}[]{#_Toc296158924}[]{#_Toc296160239}[]{#_Toc296158925}[]{#_Toc296160240}[]{#_Toc296158926}[]{#_Toc296160241}[]{#_Toc296158927}[]{#_Toc296160242}[]{#_Toc296158928}[]{#_Toc296160243}[]{#_Toc296158929}[]{#_Toc296160244}[]{#_Toc296158930}[]{#_Toc296160245}[]{#_Toc296158931}[]{#_Toc296160246}[]{#_Toc296158932}[]{#_Toc296160247}[]{#_Toc296158933}[]{#_Toc296160248}[]{#_Toc296158934}[]{#_Toc296160249}[]{#_Toc296158935}[]{#_Toc296160250}[]{#_Toc296158937}[]{#_Toc296160252}[]{#_Toc296158938}[]{#_Toc296160253}[]{#_Toc296158939}[]{#_Toc296160254}[]{#_Toc296158943}[]{#_Toc296160258}[]{#_Toc296158965}[]{#_Toc296160280}[]{#_Toc296158966}[]{#_Toc296160281}[]{#_Toc296158967}[]{#_Toc296160282}[]{#_Toc296158969}[]{#_Toc296160284}[]{#_Toc296158970}[]{#_Toc296160285}[]{#_Toc296158971}[]{#_Toc296160286}[]{#_Toc296158972}[]{#_Toc296160287}[]{#_Toc296158973}[]{#_Toc296160288}[]{#_Toc296158974}[]{#_Toc296160289}[]{#_Toc296158975}[]{#_Toc296160290}[]{#_Toc296158976}[]{#_Toc296160291}[]{#_Toc296158977}[]{#_Toc296160292}[]{#_Toc296158978}[]{#_Toc296160293}[]{#_Toc296158979}[]{#_Toc296160294}[]{#_Toc296158980}[]{#_Toc296160295}[]{#_Toc296158981}[]{#_Toc296160296}[]{#_Toc296158982}[]{#_Toc296160297}[]{#_Toc296158983}[]{#_Toc296160298}[]{#_Toc296158984}[]{#_Toc296160299}[]{#_Toc296158987}[]{#_Toc296160302}[]{#_Toc296158988}[]{#_Toc296160303}[]{#_Toc296158991}[]{#_Toc296160306}[]{#_Toc296158992}[]{#_Toc296160307}[]{#_Toc296158993}[]{#_Toc296160308}[]{#_Toc296158994}[]{#_Toc296160309}[]{#_Toc296158995}[]{#_Toc296160310}[]{#_Toc296158996}[]{#_Toc296160311}[]{#_Toc296158997}[]{#_Toc296160312}[]{#_Toc296158998}[]{#_Toc296160313}[]{#_Toc296158999}[]{#_Toc296160314}[]{#_Toc296159000}[]{#_Toc296160315}[]{#_Toc296159001}[]{#_Toc296160316}[]{#_Toc296159002}[]{#_Toc296160317}[]{#_Toc296159003}[]{#_Toc296160318}[]{#_Toc296159004}[]{#_Toc296160319}[]{#_Toc296159005}[]{#_Toc296160320}[]{#_Toc296159006}[]{#_Toc296160321}[]{#_Toc296159007}[]{#_Toc296160322}[]{#_Toc296159010}[]{#_Toc296160325}[]{#_Toc296159011}[]{#_Toc296160326}[]{#_Toc296159014}[]{#_Toc296160329}[]{#_Toc296159015}[]{#_Toc296160330}[]{#_Toc296159016}[]{#_Toc296160331}[]{#_Toc296159017}[]{#_Toc296160332}[]{#_Toc296159018}[]{#_Toc296160333}[]{#_Toc296159019}[]{#_Toc296160334}[]{#_Toc296159020}[]{#_Toc296160335}[]{#_Toc296159021}[]{#_Toc296160336}[]{#_Toc296159022}[]{#_Toc296160337}[]{#_Toc296159023}[]{#_Toc296160338}[]{#_Toc296159024}[]{#_Toc296160339}[]{#_Toc296159025}[]{#_Toc296160340}[]{#_Toc296159026}[]{#_Toc296160341}[]{#_Toc296159027}[]{#_Toc296160342}[]{#_Toc296159028}[]{#_Toc296160343}[]{#_Toc296159029}[]{#_Toc296160344}[]{#_Toc296159030}[]{#_Toc296160345}[]{#_Toc296159034}[]{#_Toc296160349}[]{#_Toc296159035}[]{#_Toc296160350}[]{#_Toc296159042}[]{#_Toc296160357}[]{#_Toc354744830}[]{#_Toc354817950}[]{#_Toc354935986}[]{#_Toc355261822}[]{#_Toc355262297}[]{#_Toc355262382}[]{#_Toc354744831}[]{#_Toc354817951}[]{#_Toc354935987}[]{#_Toc355261823}[]{#_Toc355262298}[]{#_Toc355262383}[]{#_Toc354744832}[]{#_Toc354817952}[]{#_Toc354935988}[]{#_Toc355261824}[]{#_Toc355262299}[]{#_Toc355262384}[]{#_Toc354744833}[]{#_Toc354817953}[]{#_Toc354935989}[]{#_Toc355261825}[]{#_Toc355262300}[]{#_Toc355262385}[]{#_Toc354744834}[]{#_Toc354817954}[]{#_Toc354935990}[]{#_Toc355261826}[]{#_Toc355262301}[]{#_Toc355262386}[]{#_Toc354744835}[]{#_Toc354817955}[]{#_Toc354935991}[]{#_Toc355261827}[]{#_Toc355262302}[]{#_Toc355262387}[]{#_Toc354744836}[]{#_Toc354817956}[]{#_Toc354935992}[]{#_Toc355261828}[]{#_Toc355262303}[]{#_Toc355262388}[]{#_Toc354744837}[]{#_Toc354817957}[]{#_Toc354935993}[]{#_Toc355261829}[]{#_Toc355262304}[]{#_Toc355262389}[]{#_Toc354744838}[]{#_Toc354817958}[]{#_Toc354935994}[]{#_Toc355261830}[]{#_Toc355262305}[]{#_Toc355262390}[]{#_Toc354744839}[]{#_Toc354817959}[]{#_Toc354935995}[]{#_Toc355261831}[]{#_Toc355262306}[]{#_Toc355262391}[]{#_Toc354744840}[]{#_Toc354817960}[]{#_Toc354935996}[]{#_Toc355261832}[]{#_Toc355262307}[]{#_Toc355262392}[]{#_Toc354744841}[]{#_Toc354817961}[]{#_Toc354935997}[]{#_Toc355261833}[]{#_Toc355262308}[]{#_Toc355262393}[]{#_Toc354744842}[]{#_Toc354817962}[]{#_Toc354935998}[]{#_Toc355261834}[]{#_Toc355262309}[]{#_Toc355262394}[]{#_Toc354744843}[]{#_Toc354817963}[]{#_Toc354935999}[]{#_Toc355261835}[]{#_Toc355262310}[]{#_Toc355262395}[]{#_Toc354744844}[]{#_Toc354817964}[]{#_Toc354936000}[]{#_Toc355261836}[]{#_Toc355262311}[]{#_Toc355262396}[]{#_Toc354744845}[]{#_Toc354817965}[]{#_Toc354936001}[]{#_Toc355261837}[]{#_Toc355262312}[]{#_Toc355262397}

**语音实体 \-- 语音实体命令 \-- entity**

------------------------------------------------------------------------

[**[entity]{lang="EN-US"}**]{#struct_0_16135_x6401_311472080}[命令用来创建语音实体，并进入语音实体视图。]{style="font-family:宋体"}

[**[undo entity]{lang="EN-US"}**]{#struct_0_16135_x6401_x443876154}[命令用来删除已创建的语音实体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1873324501}

[**[entity]{lang="EN-US"}**[ *entity-number* \[ **ivr** \| **pots** \| **voip** \]]{lang="EN-US"}]{#struct_0_16135_x6401_810284575}

[**[undo]{lang="EN-US"}**[ **entity** { *entity-number* \| **all** \| **ivr** \| **pots** \| **voip** }]{lang="EN-US"}]{#struct_0_16135_x6401_x2078374521}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1642034770}

[[不存在语音实体。]{style="font-family:宋体"}]{#struct_0_16135_x6401_x176748355}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1433969209}

[[语音拨号策略视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1829651461}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_141033470}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x309995596}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1078314793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1754274663}

[*[entity-number]{lang="EN-US"}*]{#struct_0_16135_x6401_x1696493923}[：语音实体号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_16135_x6401_x1641051730}[：所有语音实体。]{style="font-family:宋体"}

[**[ivr]{lang="EN-US"}**]{#struct_0_16135_x6401_1525387796}[：用于接入可定制交互式语音应答系统的语音实体。]{style="font-family:宋体"}

[**[pots]{lang="EN-US"}**]{#struct_0_16135_x6401_x1482586764}[：用于本地电话或是]{style="font-family:宋体"}[PSTN]{lang="EN-US"}[侧的语音实体。]{style="font-family:宋体"}

[**[voip]{lang="EN-US"}**]{#struct_0_16135_x6401_x867989574}[：用于]{style="font-family:宋体"}[IP]{lang="EN-US"}[侧的语音实体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x22744729}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建新语音实体时需指明语音实体类型。]{style="font-family:宋体"}]{#struct_0_16135_x6401_1788775620}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备最多支持]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1927496171}[1000]{lang="EN-US"}[个语音实体。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1437842740}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x669934539}[创建并进入]{style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x1641117266}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ]{lang="FR"}[dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] ]{lang="FR"}[entity 10 pots]{lang="EN-US"}
:::

::::: {#-981241550 .myid}
[]{#_Toc404794354}[]{#struct_0_16135_x6401_2124703329}

**语音实体 \-- 语音实体命令 \-- incoming called-number**

------------------------------------------------------------------------

[**[incoming called-number]{lang="EN-US"}**]{#struct_0_16135_x6401_1050576147}[命令用来在实体下配置一个号码串，若此号码串与呼叫中的被叫号码相匹配，则将该实体作为入实体。该被叫号码是呼叫]{style="font-family:宋体"}[INVITE]{lang="EN-US"}[报文中的被叫号码。]{style="font-family:宋体"}

[**[undo incoming called-number]{lang="EN-US"}**]{#struct_0_16135_x6401_558619388}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1963986501}

[**[incoming called-number]{lang="EN-US"}**[ *called-number-string*]{lang="EN-US"}]{#struct_0_16135_x6401_x887429726}

[**[undo incoming called-number]{lang="EN-US"}**]{#struct_0_16135_x6401_x1320348497}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1875632011}

[[没有配置任何可将该实体作为入实体的被叫号码匹配信息。]{style="font-family:宋体"}]{#struct_0_16135_x6401_681438817}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_209882074}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1603357480}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_446136789}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x499749138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x202961704}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1007464553}

[*[called-number-string]{lang="EN-US"}*]{#struct_0_16135_x6401_266686680}[：指定的被叫号码串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，格式为]{style="font-family:宋体"}[\[ + \] { *regular-expression* \[ T \] \[ \$ \] \| T }]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_951583108}[+]{lang="EN-US"}["：号码模板如果以"]{style="font-family:宋体"}[+]{lang="EN-US"}["号开头，表示整个号码是一个]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准号码，如]{style="font-family:宋体"}[+110022]{lang="EN-US"}[表示]{style="font-family:宋体"}[110022]{lang="EN-US"}[是符合]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准的号码。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音实体命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_16135_x6401_x1147031791}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[如果配置的号码首位带有]{style="font-family:KaiTi_GB2312"}]{#struct_0_16135_x6401_603799940}["+"]{lang="EN-US"}[号，则在中继环境中需要注意：]{style="font-family:KaiTi_GB2312"}[E&M/R2/LGS]{lang="EN-US"}[信令采用的是]{style="font-family:KaiTi_GB2312"}[DTMF]{lang="EN-US"}[传输，由于]{style="font-family:KaiTi_GB2312"}["+"]{lang="EN-US"}[号本身没有对应的音频，所以无法将号码成功的传输到被叫侧。而]{style="font-family:KaiTi_GB2312"}[DSS1]{lang="EN-US"}[信令采用]{style="font-family:KaiTi_GB2312"}[ISDN]{lang="EN-US"}[传输，不存在上述问题。在实际应用中，用户应该避免配置传输信令无法识别的字符，否则将会导致呼叫失败。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1092081542}[\$]{lang="EN-US"}["：只能放在结尾，表示号码结束，号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的]{style="font-family:宋体"}*[regular-expression]{lang="EN-US"}*[部分。如果号码模板后没有]{style="font-family:宋体"}[\$]{lang="EN-US"}[字符，则表示可以匹配以此号码开头的号码。]{style="font-family:宋体"}[例如，配置]{lang="EN-US" style="font-family:宋体"}**[incoming called-number ]{lang="EN-US"}**[20]{lang="EN-US"}[，表示将匹配呼叫中的以]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[开头的被叫号码的实体作为入实体。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[符号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1108621574}[T]{lang="EN-US"}["：]{style="font-family:宋体"}[T]{lang="EN-US"}[表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[regular-expression]{lang="EN-US"}*]{#struct_0_16135_x6401_1721418802}[：由"]{lang="EN-US" style="font-family:宋体"}[0-9#\*.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{lang="EN-US" style="font-family:宋体"}[[表]{lang="EN-US" style="font-family:宋体"}[1-6]{lang="EN-US"}](?-981241550#_Ref398304882)[所示。]{lang="EN-US" style="font-family:宋体"}

[]{#struct_0_16135_x6401_x1861363661}[[表1-6 ]{lang="EN-US"}[符号含义描述表]{style="font-family:
黑体"}]{#_Ref398304882}

[]{#table_struct_0_160222655}[[符号]{style="font-family:黑体"}]{#struct_0_16135_x6401_2076148350}
:::::

[[含义]{style="font-family:黑体"}]{#struct_0_16135_x6401_x200895499}

[[0-9]{lang="EN-US"}]{#struct_0_16135_x6401_x712099596}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16135_x6401_x1766979440}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_16135_x6401_x1673002120}[和]{style="font-family:宋体"}[\*]{lang="EN-US"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_155400397}

[[.]{lang="EN-US"}]{#struct_0_16135_x6401_1443612486}

[[通配符，可以与任何一个有效号码匹配。如：]{style="font-family:宋体"}[555....]{lang="EN-US"}]{#struct_0_16135_x6401_x1410683544}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_16135_x6401_x693991558}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_16135_x6401_1318199811}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}]{#struct_0_16135_x6401_942486852}

[[+]{lang="EN-US"}]{#struct_0_16135_x6401_x247884130}

[[指明符号前的字符串重复一次或多次。如：]{style="font-family:宋体"}[9876(54)+]{lang="EN-US"}]{#struct_0_16135_x6401_x52084889}[可以匹配]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[%]{lang="EN-US"}]{#struct_0_16135_x6401_2124768865}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[9876(54)%]{lang="EN-US"}]{#struct_0_16135_x6401_558684924}[可以匹配]{style="font-family:宋体"}[9876]{lang="EN-US"}[、]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[-]{lang="EN-US"}]{#struct_0_16135_x6401_782382276}

[[连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如：]{style="font-family:宋体"}[\[1-9\]]{lang="EN-US"}]{#struct_0_16135_x6401_x1007399017}[表示从]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[9]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_16135_x6401_1374012994}["只能出现在"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["中，且连接两端只能为数字]{style="font-family:宋体"}

[[\[ \]]{lang="EN-US"}]{#struct_0_16135_x6401_1721484338}

[[表示字符选择范围，如：]{style="font-family:宋体"}[\[1-36\]]{lang="EN-US"}]{#struct_0_16135_x6401_x651927310}[表示只可匹配单个字符]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[中的某一个]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_16135_x6401_x200829963}["和"]{style="font-family:宋体"}[( )]{lang="EN-US"}["如果嵌套使用，则必须以"]{style="font-family:宋体"}[( \[ \] )]{lang="EN-US"}["形式出现，不允许其它形式，如"]{style="font-family:宋体"}[\[ \[ \] \]]{lang="EN-US"}["、"]{style="font-family:宋体"}[\[ ( ) \]]{lang="EN-US"}["等]{style="font-family:宋体"}

[[( )]{lang="EN-US"}]{#struct_0_16135_x6401_x1766913904}

[[表示一组字符，如：]{style="font-family:宋体"}[(123)]{lang="EN-US"}]{#struct_0_16135_x6401_1229100173}[表示字符串]{style="font-family:宋体"}[123]{lang="EN-US"}[，它一般与符号"]{style="font-family:宋体"}[!]{lang="EN-US"}["、"]{style="font-family:宋体"}[%]{lang="EN-US"}["、"]{style="font-family:宋体"}[+]{lang="EN-US"}["一起使用，如：]{style="font-family:宋体"}[408(12)+]{lang="EN-US"}[，可以匹配]{style="font-family:宋体"}[40812]{lang="EN-US"}[或]{style="font-family:宋体"}[408121212]{lang="EN-US"}[等字符串]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1123667004}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_2119731503}[配置]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体]{style="font-family:宋体"}[1]{lang="EN-US"}[，收到的呼叫中被叫号码以]{style="font-family:宋体"}[456]{lang="EN-US"}[开头时，可以使用该实体作为入实体。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_155465933}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 1 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity1\] incoming called-number 456]{lang="EN-US"}

::: {#1677150225 .myid}
[]{#_Toc404794355}[]{#struct_0_16135_x6401_x929493067}[]{#_Toc355262314}

**语音实体 \-- 语音实体命令 \-- ip qos dscp**

------------------------------------------------------------------------

[**[ip qos dscp]{lang="EN-US"}**]{#struct_0_16135_x6401_1259691823}[命令用来配置承载媒体流]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo ip qos dscp]{lang="EN-US"}**]{#struct_0_16135_x6401_1017622578}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1925112922}

[**[ip qos dscp ]{lang="EN-US"}**[{ *dscp-value \| dscp-value-set* } **media** ]{lang="EN-US"}]{#struct_0_16135_x6401_791732283}

[**[und]{lang="PT-BR"}[o ip qos ]{lang="EN-US"}**]{#struct_0_16135_x6401_x1289420281}**[dscp]{lang="PT-BR"}[ ]{lang="PT-BR"}**[{ *dscp-value \| dscp-value-set* }]{lang="EN-US"}[ ]{lang="EN-US"}**[media]{lang="PT-BR"}**[ ]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x829863673}

[[全局承载媒体流]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16135_x6401_1056661418}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}**[ef]{lang="EN-US"}**[（]{style="font-family:宋体"}[101110]{lang="EN-US"}[）。语音实体下没有缺省的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。如果该语音实体下没有]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，那么该语音实体的缺省情况与全局的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1641576017}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1977873216}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x164452199}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1874720127}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x896856764}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_668012509}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_16135_x6401_x1953718117}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[dscp-value-set]{lang="EN-US"}*]{#struct_0_16135_x6401_x1013046193}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值如下：]{style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs7]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[media]{lang="EN-US"}**]{#struct_0_16135_x6401_x2141965638}[：承载媒体流的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[]{#struct_0_16135_x6401_1927973962}[[表1-7 ]{lang="EN-US"}[DSCP]{lang="EN-US"}]{#_Ref163816081}[关键字与值的对应表]{style="font-family:黑体"}

[]{#table_struct_0_x625074469}[[关键字]{style="font-family:黑体"}]{#struct_0_16135_x6401_x167669620}
:::

[[DSCP]{lang="EN-US"}]{#struct_0_16135_x6401_1206448455}[值（二进制）]{style="font-family:黑体"}

[[DSCP]{lang="EN-US"}]{#struct_0_16135_x6401_1227081785}[值（十进制）]{style="font-family:黑体"}

[[af11]{lang="EN-US"}]{#struct_0_16135_x6401_x157046669}

[[001010]{lang="EN-US"}]{#struct_0_16135_x6401_1222915585}

[[10]{lang="EN-US"}]{#struct_0_16135_x6401_x1641707089}

[[af12]{lang="EN-US"}]{#struct_0_16135_x6401_x1269714753}

[[001100]{lang="EN-US"}]{#struct_0_16135_x6401_x1337408102}

[[12]{lang="EN-US"}]{#struct_0_16135_x6401_1547804478}

[[af13]{lang="EN-US"}]{#struct_0_16135_x6401_1187213416}

[[001110]{lang="EN-US"}]{#struct_0_16135_x6401_x113179880}

[[14]{lang="EN-US"}]{#struct_0_16135_x6401_x1641772625}

[[af21]{lang="EN-US"}]{#struct_0_16135_x6401_x614474640}

[[010010]{lang="EN-US"}]{#struct_0_16135_x6401_x710236916}

[[18]{lang="EN-US"}]{#struct_0_16135_x6401_2082323249}

[[af22]{lang="EN-US"}]{#struct_0_16135_x6401_x74910289}

[[010100]{lang="EN-US"}]{#struct_0_16135_x6401_800728971}

[[20]{lang="EN-US"}]{#struct_0_16135_x6401_x1641838161}

[[af23]{lang="EN-US"}]{#struct_0_16135_x6401_x153518721}

[[010110]{lang="EN-US"}]{#struct_0_16135_x6401_x570648768}

[[22]{lang="EN-US"}]{#struct_0_16135_x6401_259808746}

[[af31]{lang="EN-US"}]{#struct_0_16135_x6401_1867694272}

[[011010]{lang="EN-US"}]{#struct_0_16135_x6401_x1641903697}

[[26]{lang="EN-US"}]{#struct_0_16135_x6401_771833543}

[[af32]{lang="EN-US"}]{#struct_0_16135_x6401_344344847}

[[011100]{lang="EN-US"}]{#struct_0_16135_x6401_782622897}

[[28]{lang="EN-US"}]{#struct_0_16135_x6401_1635368693}

[[af33]{lang="EN-US"}]{#struct_0_16135_x6401_x1641969233}

[[011110]{lang="EN-US"}]{#struct_0_16135_x6401_707602637}

[[30]{lang="EN-US"}]{#struct_0_16135_x6401_x1673144540}

[[af41]{lang="EN-US"}]{#struct_0_16135_x6401_954996992}

[[100010]{lang="EN-US"}]{#struct_0_16135_x6401_x1429242821}

[[34]{lang="EN-US"}]{#struct_0_16135_x6401_x1642034769}

[[af42]{lang="EN-US"}]{#struct_0_16135_x6401_x2099128192}

[[100100]{lang="EN-US"}]{#struct_0_16135_x6401_1131652557}

[[36]{lang="EN-US"}]{#struct_0_16135_x6401_x905314806}

[[af43]{lang="EN-US"}]{#struct_0_16135_x6401_x1641051729}

[[100110]{lang="EN-US"}]{#struct_0_16135_x6401_1602461415}

[[38]{lang="EN-US"}]{#struct_0_16135_x6401_1271502849}

[[cs1]{lang="EN-US"}]{#struct_0_16135_x6401_185671062}

[[001000]{lang="EN-US"}]{#struct_0_16135_x6401_x1641117265}

[[8]{lang="EN-US"}]{#struct_0_16135_x6401_636590874}

[[cs2]{lang="EN-US"}]{#struct_0_16135_x6401_x1976397286}

[[010000]{lang="EN-US"}]{#struct_0_16135_x6401_1803448444}

[[16]{lang="EN-US"}]{#struct_0_16135_x6401_x75492073}

[[cs3]{lang="EN-US"}]{#struct_0_16135_x6401_x1490029842}

[[011000]{lang="EN-US"}]{#struct_0_16135_x6401_x252329497}

[[24]{lang="EN-US"}]{#struct_0_16135_x6401_x75557609}

[[cs4]{lang="EN-US"}]{#struct_0_16135_x6401_1663710926}

[[100000]{lang="EN-US"}]{#struct_0_16135_x6401_x344304792}

[[32]{lang="EN-US"}]{#struct_0_16135_x6401_x531546486}

[[cs5]{lang="EN-US"}]{#struct_0_16135_x6401_x75623145}

[[101000]{lang="EN-US"}]{#struct_0_16135_x6401_x1614643896}

[[40]{lang="EN-US"}]{#struct_0_16135_x6401_1939287815}

[[cs6]{lang="EN-US"}]{#struct_0_16135_x6401_x75688681}

[[110000]{lang="EN-US"}]{#struct_0_16135_x6401_x349423765}

[[48]{lang="EN-US"}]{#struct_0_16135_x6401_x436626247}

[[cs7]{lang="EN-US"}]{#struct_0_16135_x6401_209058211}

[[111000]{lang="EN-US"}]{#struct_0_16135_x6401_x75754217}

[[56]{lang="EN-US"}]{#struct_0_16135_x6401_1924925752}

[[ef]{lang="EN-US"}]{#struct_0_16135_x6401_x1172777747}

[[101110]{lang="EN-US"}]{#struct_0_16135_x6401_x75819753}

[[46]{lang="EN-US"}]{#struct_0_16135_x6401_620937673}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_472937602}

[[载媒体流的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16135_x6401_472872066}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值可以在]{style="font-family:宋体"}[SIP]{lang="EN-US"}[视图或语音实体视图下配置。]{style="font-family:宋体"}[SIP]{lang="EN-US"}[视图下的]{style="font-family:宋体"}**[ip qos dscp]{lang="EN-US"}**[命令为全局命令，当语音实体下配置媒体流的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值时，则使用语音实体配置，否则使用全局命令配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，即语音实体配置优先于全局配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x66261255}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1182927552}[配置承载语音媒体流的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}**[af41]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x75885289}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] ]{lang="FR"}[dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] ]{lang="FR"}[entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial]{lang="FR"}[-entity10]{lang="EN-US"}[\] ]{lang="FR"}[ip qos dscp af41 media]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_472806530}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip qos dscp]{lang="EN-US"}**]{#struct_0_16135_x6401_x2015837941}[（]{lang="EN-US" style="font-family:宋体"}[语音]{style="font-family:宋体"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[SIP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

::: {#-1502834408 .myid}
[]{#_Toc404794356}[]{#struct_0_16135_x6401_1309870559}[]{#_Toc355262316}

**语音实体 \-- 语音实体命令 \-- line**

------------------------------------------------------------------------

[**[line]{lang="EN-US"}**]{#struct_0_16135_x6401_x1818483995}[命令用来将指定的语音用户线绑定到语音实体。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **line**]{lang="EN-US"}]{#struct_0_16135_x6401_x1680959769}[命令用来取消已有的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x983130488}

[**[line]{lang="EN-US"}**[ *line-number*]{lang="EN-US"}]{#struct_0_16135_x6401_x177191841}

[**[undo]{lang="EN-US"}**[ **line**]{lang="EN-US"}]{#struct_0_16135_x6401_65834333}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1488253489}

[[语音实体与语音用户线没有绑定关系。]{style="font-family:宋体"}]{#struct_0_16135_x6401_x362675439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1484953462}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_x75950825}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1818257596}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1026067273}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_120869112}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1467521089}

[*[line-number]{lang="EN-US"}*]{#struct_0_16135_x6401_x1660500020}[：语音用户线号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_893075052}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x1966788961}[语音用户线]{style="font-family:宋体"}[line1/0]{lang="EN-US"}[绑定到指定的语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x74967785}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] line 1/0]{lang="EN-US"}
:::

::::: {#-1681238638 .myid}
[]{#_Toc404794357}[]{#struct_0_16135_x6401_1188874893}[]{#_Toc355262315}

**语音实体 \-- 语音实体命令 \-- match-template**

------------------------------------------------------------------------

[**[match-template]{lang="EN-US"}**]{#struct_0_16135_x6401_x1545451299}[命令用来配置语音实体的号码模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match-template**]{lang="EN-US"}]{#struct_0_16135_x6401_x218827889}[命令用来删除已配置的号码模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1984186308}

[**[match-template ]{lang="EN-US"}***[match-string]{lang="EN-US"}*]{#struct_0_16135_x6401_1670930569}

[**[undo match-template]{lang="EN-US"}**]{#struct_0_16135_x6401_1059140581}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x732748566}

[[语音实体下不存在号码模板。]{style="font-family:宋体"}]{#struct_0_16135_x6401_x75033321}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x432827275}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1239450947}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1698567315}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_394382499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1663801481}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x808799346}

[*[match-string]{lang="EN-US"}*]{#struct_0_16135_x6401_2121403124}[：号码模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，格式为]{style="font-family:宋体"}[\[ **+** \] { *string* \[ **T** \] \[ **\$** \] \| **T** }]{lang="EN-US"}[。符号说明如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_1299744182}[+]{lang="EN-US"}["：号码模板如果以"]{style="font-family:宋体"}[+]{lang="EN-US"}["号开头，"]{style="font-family:宋体"}[+]{lang="EN-US"}["号表示整个号码是一个]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准号码，如]{style="font-family:宋体"}[+110022]{lang="EN-US"}[表示]{style="font-family:宋体"}[110022]{lang="EN-US"}[是符合]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准的号码。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音实体命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_16135_x6401_x75492072}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[如果配置的号码首位带有"]{style="font-family:KaiTi_GB2312"}]{#struct_0_16135_x6401_x1490029841}[+]{lang="EN-US"}["号，则在中继环境中需要注意：]{style="font-family:KaiTi_GB2312"}[E&M/R2/LGS]{lang="EN-US"}[信令采用的是]{style="font-family:KaiTi_GB2312"}[DTMF]{lang="EN-US"}[传输，由于"]{style="font-family:KaiTi_GB2312"}[+]{lang="EN-US"}["号本身没有对应的音频，所以无法将号码成功的传输到被叫侧。而]{style="font-family:KaiTi_GB2312"}[DSS1]{lang="EN-US"}[信令采用]{style="font-family:KaiTi_GB2312"}[ISDN]{lang="EN-US"}[传输，不存在上述问题。在实际应用中，用户应该避免配置传输信令无法识别的字符，否则将会导致呼叫失败。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1818413438}[\$]{lang="EN-US"}["：只能放在结尾，表示号码结束，号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[部分。如果号码模板后没有]{style="font-family:宋体"}[\$]{lang="EN-US"}[字符，则表示可以匹配以此号码开头的号码，例如配置]{style="font-family:宋体"}**[match-template ]{lang="EN-US"}**[20]{lang="EN-US"}[，表示可以匹配以]{style="font-family:宋体"}[20]{lang="EN-US"}[号码开头的号码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[符号"]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1103668706}[T]{lang="EN-US"}["：]{style="font-family:宋体"}[T]{lang="EN-US"}[表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[string]{lang="EN-US"}*]{#struct_0_16135_x6401_x322014612}[：由"]{lang="EN-US" style="font-family:宋体"}[0-9#]{lang="EN-US"}[＊]{lang="EN-US" style="font-family:宋体"}[.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{lang="EN-US" style="font-family:宋体"}[[表]{lang="EN-US" style="font-family:宋体"}[1-8]{lang="EN-US"}](#_0_16135_x6401_668020231)[所示。]{lang="EN-US" style="font-family:宋体"}

[]{#struct_0_16135_x6401_668020231}[]{#_Ref148492379}[]{#_Toc121809759}[[表1-8 ]{lang="EN-US"}[符号含义]{style="font-family:黑体"}]{#_Toc112125389}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_x637232965}[[符号]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1924042637}
:::::

[[含义]{style="font-family:黑体"}]{#struct_0_16135_x6401_x49082311}

[[0-9]{lang="EN-US"}]{#struct_0_16135_x6401_x75557608}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16135_x6401_1663710927}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_16135_x6401_x344239256}[和＊]{style="font-family:宋体"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_16135_x6401_1764895258}

[[.]{lang="EN-US"}]{#struct_0_16135_x6401_x1107256881}

[[通配符，可以与任何一位有效号码匹配。如：]{style="font-family:宋体"}[555. . . . ]{lang="EN-US"}]{#struct_0_16135_x6401_204697967}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_16135_x6401_x75623144}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_16135_x6401_x1614643897}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[符号"]{style="font-family:宋体"}[!%+]{lang="EN-US"}]{#struct_0_16135_x6401_x789595540}["前的字符串（一位号码或号码串），作为非精确匹配的号码，处理类似"]{style="font-family:宋体"}[.]{lang="EN-US"}["通配符；这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}

[[+]{lang="EN-US"}]{#struct_0_16135_x6401_1223330773}

[[指明符号前的字符串重复一次或多次。如：]{style="font-family:宋体"}[9876(54)+]{lang="EN-US"}]{#struct_0_16135_x6401_x1872546814}[可以匹配]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[%]{lang="EN-US"}]{#struct_0_16135_x6401_x75688680}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[9876(54)%]{lang="EN-US"}]{#struct_0_16135_x6401_x349423766}[可以匹配]{style="font-family:宋体"}[9876]{lang="EN-US"}[、]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[-]{lang="EN-US"}]{#struct_0_16135_x6401_x436822855}

[[连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如：]{style="font-family:宋体"}[\[1-9\]]{lang="EN-US"}]{#struct_0_16135_x6401_622840904}[表示从]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[9]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_16135_x6401_x782094514}["只能出现在"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["中，且连接两端只能为数字，如]{style="font-family:宋体"}[0-9]{lang="EN-US"}

[[\[ \]]{lang="EN-US"}]{#struct_0_16135_x6401_x75754216}

[[表示字符选择范围，如：]{style="font-family:宋体"}[\[1-36\]]{lang="EN-US"}]{#struct_0_16135_x6401_1924925753}[表示只可匹配单个字符]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[中的某一个]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_16135_x6401_x1172712211}["和"]{style="font-family:宋体"}[( )]{lang="EN-US"}["如果嵌套使用，则必须以"]{style="font-family:宋体"}[( \[ \] )]{lang="EN-US"}["形式出现，不允许其它形式，如"]{style="font-family:宋体"}[\[ \[ \] \]]{lang="EN-US"}["、"]{style="font-family:宋体"}[\[ ( ) \]]{lang="EN-US"}["等]{style="font-family:宋体"}

[[( )]{lang="EN-US"}]{#struct_0_16135_x6401_658812549}

[[表示一组字符，如：]{style="font-family:宋体"}[(123)]{lang="EN-US"}]{#struct_0_16135_x6401_x1384013669}[表示字符串]{style="font-family:宋体"}[123]{lang="EN-US"}[，它一般与符号"]{style="font-family:宋体"}[!]{lang="EN-US"}["、"]{style="font-family:宋体"}[%]{lang="EN-US"}["、"]{style="font-family:宋体"}[+]{lang="EN-US"}["一起使用，如：]{style="font-family:宋体"}[408(12)+]{lang="EN-US"}[，可以匹配]{style="font-family:宋体"}[40812]{lang="EN-US"}[或]{style="font-family:宋体"}[408121212]{lang="EN-US"}[等字符串，但不能匹配]{style="font-family:宋体"}[408]{lang="EN-US"}[，即]{style="font-family:宋体"}[12]{lang="EN-US"}[可连续出现且至少出现一次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](语音实体命令.files/image001.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_16135_x6401_x1272052500}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[每一个符号占用一个字符，符号]{style="font-family:KaiTi_GB2312"}]{#struct_0_16135_x6401_x75819752}[\[ \]]{lang="EN-US"}[和]{style="font-family:KaiTi_GB2312"}[( )]{lang="EN-US"}[占用两个字符。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_620937674}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16135_x6401_x66261252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本地]{lang="EN-US" style="font-family:宋体"}[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1182927545}[语音实体时，使用]{lang="EN-US" style="font-family:宋体"}**[match-template]{lang="EN-US"}**[指定的是与本地语音用户线绑定的号码模板。配置中继]{lang="EN-US" style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体时，使用]{lang="EN-US" style="font-family:宋体"}**[match-template]{lang="EN-US"}**[指定的是被叫方的号码模板。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[VoIP]{lang="EN-US"}]{#struct_0_16135_x6401_x1053371360}[语音实体时，使用]{lang="EN-US" style="font-family:宋体"}**[match-template]{lang="EN-US"}**[指定的是被叫方的号码模板。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1207325057}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1663068945}[配置]{style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体]{style="font-family:宋体"}[1000]{lang="EN-US"}[的号码模板为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x75885288}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 1000 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity1000\] match-template 1000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1309870558}[配置]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体]{style="font-family:宋体"}[2000]{lang="EN-US"}[的号码模板为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x1818418459}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 2000 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity2000\] match-template 2000]{lang="EN-US"}

::: {#880057182 .myid}
[]{#_Toc404794358}[]{#struct_0_16135_x6401_x1464873287}[]{#_Toc355262317}[]{#_Toc295911311}[]{#_Toc262031004}[]{#_Toc135295492}[]{#_Toc130097141}[]{#_Toc129160861}[]{#_Toc47776203}

**语音实体 \-- 语音实体命令 \-- outband nte**

------------------------------------------------------------------------

[**[outband ]{lang="EN-US"}**]{#struct_0_16135_x6401_880267684}**[nte]{lang="PT-BR"}**[命令用来配置使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}[（]{style="font-family:宋体"}[Named Telephone Event]{lang="EN-US"}[，命名的电话事件）带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **outband**]{lang="EN-US"}]{#struct_0_16135_x6401_x156424597}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1569398820}

[**[outband]{lang="PT-BR"}**]{#struct_0_16135_x6401_1449307924}[ **nte**]{lang="PT-BR"}

[**[undo]{lang="EN-US"}**[ **outband**]{lang="EN-US"}]{#struct_0_16135_x6401_x75950824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1818257595}

[[使用带内方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_16135_x6401_x1429351800}[信号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1549650747}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_x2138291313}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_550140651}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_2094595232}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1251497443}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_127168811}

[[建议配置该方式时，在主被叫设备上同时开启]{style="font-family:宋体"}**[outband]{lang="EN-US"}**[ **nte**]{lang="EN-US"}]{#struct_0_16135_x6401_x74967784}[命令，并设置相同的]{style="font-family:宋体"}**[rtp]{lang="EN-US"}**[ **payload-type**]{lang="EN-US"}[值，否则可能导致]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号传输失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1188874892}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x1545385763}[配置使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}[带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x1514649125}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] outband nte]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_517687004}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rtp]{lang="EN-US"}**[ **payload-type** **nte**]{lang="EN-US"}]{#struct_0_16135_x6401_495461015}
:::

::: {#-341921842 .myid}
[]{#_Toc404794359}[]{#struct_0_16135_x6401_x174828202}

**语音实体 \-- 语音实体命令 \-- playout-delay**

------------------------------------------------------------------------

[**[playout-delay]{lang="EN-US"}**]{#struct_0_16135_x6401_x496804309}[命令用来配置缓存语音包的工作参数。]{style="font-family:宋体"}

[**[undo playout-delay]{lang="EN-US"}**]{#struct_0_16135_x6401_287701269}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_2015433141}

[**[playout-delay ]{lang="EN-US"}**[{ **initial** *milliseconds* \| **maximum** *milliseconds* \| **minimum** *milliseconds* }]{lang="EN-US"}]{#struct_0_16135_x6401_136420179}

[**[undo playout-delay ]{lang="EN-US"}**[{ **initial** \| **maximum** \| **minimum** }]{lang="EN-US"}]{#struct_0_16135_x6401_x57620320}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x967281033}

[[语音包的初始缓冲时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_16135_x6401_x1068264134}[毫秒，最大缓冲时间为]{style="font-family:宋体"}[160]{lang="EN-US"}[毫秒，最小缓冲时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_305591827}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_x2043953081}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x174762666}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1778510806}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x2096876445}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x2067585903}

[**[initial ]{lang="EN-US"}***[milliseconds]{lang="EN-US"}*]{#struct_0_16135_x6401_x1382949225}[：在自适应模式下，]{style="font-family:宋体"}**[initial]{lang="EN-US"}**[是建立通话后语音包初始缓冲时间。在静态模式下，]{style="font-family:宋体"}**[initial]{lang="EN-US"}**[是语音包固定缓冲时间。取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[maximum ]{lang="EN-US"}***[milliseconds]{lang="EN-US"}*]{#struct_0_16135_x6401_2009937795}[：设置语音包的最大缓冲时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为毫秒。该参数只在自适应模式下生效。]{style="font-family:宋体"}

[**[minimum ]{lang="EN-US"}***[milliseconds]{lang="EN-US"}*]{#struct_0_16135_x6401_x1490324504}[：设置语音包的最小缓冲时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[，单位为毫秒。该参数只在自适应模式下生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_55367860}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x301261909}[配置缓存语音包的工作模式为自适应模式，语音包的最小缓冲时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x1249221285}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] playout-delay mode adaptive]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] playout-delay minimum 30]{lang="EN-US"}
:::

::: {#455053370 .myid}
[]{#_Toc404794360}[]{#struct_0_16135_x6401_x1429857421}

**语音实体 \-- 语音实体命令 \-- playout-delay mode**

------------------------------------------------------------------------

[**[playout-delay mode]{lang="EN-US"}**]{#struct_0_16135_x6401_235945930}[命令用来配置缓存语音包的工作模式。]{style="font-family:宋体"}

[**[undo playout-delay mode]{lang="EN-US"}**]{#struct_0_16135_x6401_1996114257}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1477891329}

[**[playout-delay mode ]{lang="EN-US"}**[{ **adaptive \| fixed** }]{lang="EN-US"}]{#struct_0_16135_x6401_x364561360}

[**[undo playout-delay mode]{lang="EN-US"}**]{#struct_0_16135_x6401_x174697130}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x983152187}

[[缓存语音包的工作模式为静态模式。]{style="font-family:宋体"}]{#struct_0_16135_x6401_x159950039}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x2140015891}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_x147173268}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1441045546}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_992142857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1797256665}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x30326234}

[**[adaptive]{lang="EN-US"}**]{#struct_0_16135_x6401_566167430}[：配置缓存语音包的工作模式为自适应模式。在自适应模式下，语音包缓冲区大小可以根据网络抖动情况自动调整。]{style="font-family:宋体"}

[**[fixed]{lang="EN-US"}**]{#struct_0_16135_x6401_x655354375}[：配置缓存语音包的工作模式为静态模式。在静态模式下，语音包缓冲区大小是固定的。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1105207252}

[[在]{style="font-family:宋体"}]{#struct_0_16135_x6401_543261184}[VoIP]{lang="EN-US"}[语音通信质量不理想的情况下，可以使用该命令]{style="font-family:宋体"}[调整缓存语音包的工作模式]{style="font-family:
宋体"}[。在理想的语音网络环境中，语音包从发送方到接收方所经历的传播时间是恒定的，即网络抖动为零。而在实际的网络环境中，语音包从发送方到接收方所经历的传播时间是不断变化的，即存在网络时延抖动。为了消除网络抖动对话音质量造成的影响，语音数据的接收方需要做防抖动处理。接收方通过将接收到的语音包缓存一段时间后再播放，使得以不同时延到达接收方的语音包能够按照发送方的固定时间间隔均匀地被传递给编解码器，从而有效消除网络抖动对通话质量带来的影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_494243910}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_577456330}[配置缓存语音包的工作模式为自适应模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x175680170}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] playout-delay mode adaptive]{lang="EN-US"}
:::

::: {#1229030173 .myid}
[]{#_Toc94588245}[]{#_Toc80176791}[]{#_Toc30075877}[]{#_Toc404794361}[]{#struct_0_16135_x6401_x940240687}[]{#_Toc355262368}[]{#_Toc321750637}[]{#_Toc354936007}[]{#_Toc355261843}[]{#_Toc355262318}[]{#_Toc355262403}[]{#_Toc354936008}[]{#_Toc355261844}[]{#_Toc355262319}[]{#_Toc355262404}[]{#_Toc354936009}[]{#_Toc355261845}[]{#_Toc355262320}[]{#_Toc355262405}[]{#_Toc354936010}[]{#_Toc355261846}[]{#_Toc355262321}[]{#_Toc355262406}[]{#_Toc354936011}[]{#_Toc355261847}[]{#_Toc355262322}[]{#_Toc355262407}[]{#_Toc354936012}[]{#_Toc355261848}[]{#_Toc355262323}[]{#_Toc355262408}[]{#_Toc354936013}[]{#_Toc355261849}[]{#_Toc355262324}[]{#_Toc355262409}[]{#_Toc354936014}[]{#_Toc355261850}[]{#_Toc355262325}[]{#_Toc355262410}[]{#_Toc354936015}[]{#_Toc355261851}[]{#_Toc355262326}[]{#_Toc355262411}[]{#_Toc354936016}[]{#_Toc355261852}[]{#_Toc355262327}[]{#_Toc355262412}[]{#_Toc354936017}[]{#_Toc355261853}[]{#_Toc355262328}[]{#_Toc355262413}[]{#_Toc354936018}[]{#_Toc355261854}[]{#_Toc355262329}[]{#_Toc355262414}[]{#_Toc354936019}[]{#_Toc355261855}[]{#_Toc355262330}[]{#_Toc355262415}[]{#_Toc354936020}[]{#_Toc355261856}[]{#_Toc355262331}[]{#_Toc355262416}[]{#_Toc354936021}[]{#_Toc355261857}[]{#_Toc355262332}[]{#_Toc355262417}[]{#_Toc354936022}[]{#_Toc355261858}[]{#_Toc355262333}[]{#_Toc355262418}[]{#_Toc354936023}[]{#_Toc355261859}[]{#_Toc355262334}[]{#_Toc355262419}[]{#_Toc354936024}[]{#_Toc355261860}[]{#_Toc355262335}[]{#_Toc355262420}[]{#_Toc354936025}[]{#_Toc355261861}[]{#_Toc355262336}[]{#_Toc355262421}[]{#_Toc354936026}[]{#_Toc355261862}[]{#_Toc355262337}[]{#_Toc355262422}[]{#_Toc354936027}[]{#_Toc355261863}[]{#_Toc355262338}[]{#_Toc355262423}[]{#_Toc354936028}[]{#_Toc355261864}[]{#_Toc355262339}[]{#_Toc355262424}[]{#_Toc354936029}[]{#_Toc355261865}[]{#_Toc355262340}[]{#_Toc355262425}[]{#_Toc354936030}[]{#_Toc355261866}[]{#_Toc355262341}[]{#_Toc355262426}[]{#_Toc354936031}[]{#_Toc355261867}[]{#_Toc355262342}[]{#_Toc355262427}[]{#_Toc354936032}[]{#_Toc355261868}[]{#_Toc355262343}[]{#_Toc355262428}[]{#_Toc354936033}[]{#_Toc355261869}[]{#_Toc355262344}[]{#_Toc355262429}[]{#_Toc354936034}[]{#_Toc355261870}[]{#_Toc355262345}[]{#_Toc355262430}[]{#_Toc136487931}[]{#_Toc136504493}[]{#_Toc87442432}[]{#_Toc87787072}[]{#_Toc87851935}[]{#_Toc87852714}[]{#_Toc87853495}[]{#_Toc87867534}[]{#_Toc87442434}[]{#_Toc87787074}[]{#_Toc87851937}[]{#_Toc87852716}[]{#_Toc87853497}[]{#_Toc87867536}[]{#_Toc87442435}[]{#_Toc87787075}[]{#_Toc87851938}[]{#_Toc87852717}[]{#_Toc87853498}[]{#_Toc87867537}[]{#_Toc87442436}[]{#_Toc87787076}[]{#_Toc87851939}[]{#_Toc87852718}[]{#_Toc87853499}[]{#_Toc87867538}[]{#_Toc87442437}[]{#_Toc87787077}[]{#_Toc87851940}[]{#_Toc87852719}[]{#_Toc87853500}[]{#_Toc87867539}[]{#_Toc87442438}[]{#_Toc87787078}[]{#_Toc87851941}[]{#_Toc87852720}[]{#_Toc87853501}[]{#_Toc87867540}[]{#_Toc87442439}[]{#_Toc87787079}[]{#_Toc87851942}[]{#_Toc87852721}[]{#_Toc87853502}[]{#_Toc87867541}[]{#_Toc87442440}[]{#_Toc87787080}[]{#_Toc87851943}[]{#_Toc87852722}[]{#_Toc87853503}[]{#_Toc87867542}[]{#_Toc87442441}[]{#_Toc87787081}[]{#_Toc87851944}[]{#_Toc87852723}[]{#_Toc87853504}[]{#_Toc87867543}[]{#_Toc87442442}[]{#_Toc87787082}[]{#_Toc87851945}[]{#_Toc87852724}[]{#_Toc87853505}[]{#_Toc87867544}[]{#_Toc87442443}[]{#_Toc87787083}[]{#_Toc87851946}[]{#_Toc87852725}[]{#_Toc87853506}[]{#_Toc87867545}[]{#_Toc87442444}[]{#_Toc87787084}[]{#_Toc87851947}[]{#_Toc87852726}[]{#_Toc87853507}[]{#_Toc87867546}[]{#_Toc87442445}[]{#_Toc87787085}[]{#_Toc87851948}[]{#_Toc87852727}[]{#_Toc87853508}[]{#_Toc87867547}[]{#_Toc87442446}[]{#_Toc87787086}[]{#_Toc87851949}[]{#_Toc87852728}[]{#_Toc87853509}[]{#_Toc87867548}[]{#_Toc354817972}[]{#_Toc354936035}[]{#_Toc355261871}[]{#_Toc355262346}[]{#_Toc355262431}[]{#_Toc354817973}[]{#_Toc354936036}[]{#_Toc355261872}[]{#_Toc355262347}[]{#_Toc355262432}[]{#_Toc354817974}[]{#_Toc354936037}[]{#_Toc355261873}[]{#_Toc355262348}[]{#_Toc355262433}[]{#_Toc354817975}[]{#_Toc354936038}[]{#_Toc355261874}[]{#_Toc355262349}[]{#_Toc355262434}[]{#_Toc354817976}[]{#_Toc354936039}[]{#_Toc355261875}[]{#_Toc355262350}[]{#_Toc355262435}[]{#_Toc354817977}[]{#_Toc354936040}[]{#_Toc355261876}[]{#_Toc355262351}[]{#_Toc355262436}[]{#_Toc354817978}[]{#_Toc354936041}[]{#_Toc355261877}[]{#_Toc355262352}[]{#_Toc355262437}[]{#_Toc354817979}[]{#_Toc354936042}[]{#_Toc355261878}[]{#_Toc355262353}[]{#_Toc355262438}[]{#_Toc354817980}[]{#_Toc354936043}[]{#_Toc355261879}[]{#_Toc355262354}[]{#_Toc355262439}[]{#_Toc354817981}[]{#_Toc354936044}[]{#_Toc355261880}[]{#_Toc355262355}[]{#_Toc355262440}[]{#_Toc354817982}[]{#_Toc354936045}[]{#_Toc355261881}[]{#_Toc355262356}[]{#_Toc355262441}[]{#_Toc354817983}[]{#_Toc354936046}[]{#_Toc355261882}[]{#_Toc355262357}[]{#_Toc355262442}[]{#_Toc354817984}[]{#_Toc354936047}[]{#_Toc355261883}[]{#_Toc355262358}[]{#_Toc355262443}[]{#_Toc354817985}[]{#_Toc354936048}[]{#_Toc355261884}[]{#_Toc355262359}[]{#_Toc355262444}[]{#_Toc354817986}[]{#_Toc354936049}[]{#_Toc355261885}[]{#_Toc355262360}[]{#_Toc355262445}[]{#_Toc354817987}[]{#_Toc354936050}[]{#_Toc355261886}[]{#_Toc355262361}[]{#_Toc355262446}[]{#_Toc354817988}[]{#_Toc354936051}[]{#_Toc355261887}[]{#_Toc355262362}[]{#_Toc355262447}[]{#_Toc354817989}[]{#_Toc354936052}[]{#_Toc355261888}[]{#_Toc355262363}[]{#_Toc355262448}[]{#_Toc354817990}[]{#_Toc354936053}[]{#_Toc355261889}[]{#_Toc355262364}[]{#_Toc355262449}[]{#_Toc354817991}[]{#_Toc354936054}[]{#_Toc355261890}[]{#_Toc355262365}[]{#_Toc355262450}[]{#_Toc354817992}[]{#_Toc354936055}[]{#_Toc355261891}[]{#_Toc355262366}[]{#_Toc355262451}[]{#_Toc354817993}[]{#_Toc354936056}[]{#_Toc355261892}[]{#_Toc355262367}[]{#_Toc355262452}

**语音实体 \-- 语音实体命令 \-- rtp payload-type nte**

------------------------------------------------------------------------

[**[rtp]{lang="EN-US"}**[ **payload-type** **nte**]{lang="EN-US"}]{#struct_0_16135_x6401_x1978330972}[命令用来配置使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}[方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号时，]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[payload]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rtp** **payload-type** **nte**]{lang="EN-US"}]{#struct_0_16135_x6401_x75033320}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x432827274}

[**[rtp]{lang="EN-US"}**[ **payload-type** **nte** *value*]{lang="EN-US"}]{#struct_0_16135_x6401_1239516483}

[**[undo]{lang="EN-US"}**[ **rtp** **payload-type** **nte**]{lang="EN-US"}]{#struct_0_16135_x6401_589310794}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x570967007}

[[使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}]{#struct_0_16135_x6401_188697066}[方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号时，]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[payload]{lang="EN-US"}[值为]{style="font-family:宋体"}[101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_151942733}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_x1072531138}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1932995032}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x75492075}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1490029848}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1266700277}

[*[value]{lang="EN-US"}*]{#struct_0_16135_x6401_x349154446}[：]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[payload]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[96]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[。其中]{style="font-family:宋体"}[98]{lang="EN-US"}[用于标识非标准]{style="font-family:宋体"}[T38]{lang="EN-US"}[传真报文，为保留值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1929920091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议配置该方式时，在主被叫设备上同时开启]{style="font-family:宋体"}]{#struct_0_16135_x6401_1647719106}**[outband]{lang="EN-US"}**[ **nte**]{lang="EN-US"}[命令**，**并设置相同的]{style="font-family:宋体"}**[rtp]{lang="EN-US"}**[ **payload-type**]{lang="EN-US"}[值，否则可能导致]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号传输失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[与其它厂商的设备互通时，不能配置其它厂商设备禁用]{style="font-family:宋体"}]{#struct_0_16135_x6401_793074919}[payload]{lang="EN-US"}[值，否则可能导致]{style="font-family:宋体"}[NTE]{lang="EN-US"}[协商失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_722348806}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_417054280}[配置使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}[带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号，其中]{style="font-family:宋体"}[payload]{lang="EN-US"}[值为]{style="font-family:宋体"}[102]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x75557611}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] outband nte]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] rtp payload-type nte 102]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x674941242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[outband nte]{lang="EN-US"}**]{#struct_0_16135_x6401_1211403844}
:::

::: {#1170655049 .myid}
[]{#_Toc404794362}[]{#struct_0_16135_x6401_273983180}[]{#_Toc355262369}[]{#_Toc296159433}[]{#_Toc296160724}[]{#_Toc296159434}[]{#_Toc296160725}[]{#_Toc296159436}[]{#_Toc296160727}[]{#_Toc296159437}[]{#_Toc296160728}[]{#_Toc296159438}[]{#_Toc296160729}[]{#_Toc296159439}[]{#_Toc296160730}[]{#_Toc296159440}[]{#_Toc296160731}[]{#_Toc296159441}[]{#_Toc296160732}[]{#_Toc296159442}[]{#_Toc296160733}[]{#_Toc296159443}[]{#_Toc296160734}[]{#_Toc296159444}[]{#_Toc296160735}[]{#_Toc296159445}[]{#_Toc296160736}[]{#_Toc296159446}[]{#_Toc296160737}[]{#_Toc296159447}[]{#_Toc296160738}[]{#_Toc296159448}[]{#_Toc296160739}[]{#_Toc296159452}[]{#_Toc296160743}[]{#_Toc296159456}[]{#_Toc296160747}[]{#_Toc296159457}[]{#_Toc296160748}[]{#_Toc296159459}[]{#_Toc296160750}[]{#_Toc296159460}[]{#_Toc296160751}[]{#_Toc296159461}[]{#_Toc296160752}[]{#_Toc296159462}[]{#_Toc296160753}[]{#_Toc296159463}[]{#_Toc296160754}[]{#_Toc296159464}[]{#_Toc296160755}[]{#_Toc296159465}[]{#_Toc296160756}[]{#_Toc296159466}[]{#_Toc296160757}[]{#_Toc296159467}[]{#_Toc296160758}[]{#_Toc296159468}[]{#_Toc296160759}[]{#_Toc296159469}[]{#_Toc296160760}[]{#_Toc296159470}[]{#_Toc296160761}[]{#_Toc296159471}[]{#_Toc296160762}[]{#_Toc296159475}[]{#_Toc296160766}[]{#_Toc296159478}[]{#_Toc296160769}[]{#_Toc296159479}[]{#_Toc296160770}[]{#_Toc296159480}[]{#_Toc296160771}[]{#_Toc296159483}[]{#_Toc296160774}[]{#_Toc296159484}[]{#_Toc296160775}[]{#_Toc296159485}[]{#_Toc296160776}[]{#_Toc296159486}[]{#_Toc296160777}[]{#_Toc296159487}[]{#_Toc296160778}[]{#_Toc296159488}[]{#_Toc296160779}[]{#_Toc296159489}[]{#_Toc296160780}[]{#_Toc296159490}[]{#_Toc296160781}[]{#_Toc296159491}[]{#_Toc296160782}[]{#_Toc296159492}[]{#_Toc296160783}[]{#_Toc296159493}[]{#_Toc296160784}[]{#_Toc296159494}[]{#_Toc296160785}[]{#_Toc296159497}[]{#_Toc296160788}[]{#_Toc296159498}[]{#_Toc296160789}[]{#_Toc296159500}[]{#_Toc296160791}[]{#_Toc296159501}[]{#_Toc296160792}[]{#_Toc345245980}[]{#_Toc346096088}[]{#_Toc345245981}[]{#_Toc346096089}[]{#_Toc345245982}[]{#_Toc346096090}[]{#_Toc345245983}[]{#_Toc346096091}[]{#_Toc345245984}[]{#_Toc346096092}[]{#_Toc345245985}[]{#_Toc346096093}[]{#_Toc345245986}[]{#_Toc346096094}[]{#_Toc345245987}[]{#_Toc346096095}[]{#_Toc345245988}[]{#_Toc346096096}[]{#_Toc345245989}[]{#_Toc346096097}[]{#_Toc345245990}[]{#_Toc346096098}[]{#_Toc345245991}[]{#_Toc346096099}[]{#_Toc345245992}[]{#_Toc346096100}[]{#_Toc345245993}[]{#_Toc346096101}[]{#_Toc345245994}[]{#_Toc346096102}[]{#_Toc345245995}[]{#_Toc346096103}[]{#_Toc345245996}[]{#_Toc346096104}[]{#_Toc345245997}[]{#_Toc346096105}[]{#_Toc345245998}[]{#_Toc346096106}[]{#_Toc345245999}[]{#_Toc346096107}[]{#_Toc345246000}[]{#_Toc346096108}[]{#_Toc345246001}[]{#_Toc346096109}

**语音实体 \-- 语音实体命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_16135_x6401_814453398}[命令用来关闭语音实体。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[shutdown]{lang="EN-US"}**]{#struct_0_16135_x6401_1590093943}[命令用来开启语音实体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x286393633}

[**[shutdown]{lang="EN-US"}**]{#struct_0_16135_x6401_1068093425}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_16135_x6401_x75623147}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1614643898}

[[语音实体处于开启状态。]{style="font-family:宋体"}]{#struct_0_16135_x6401_776488401}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_844893626}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_424780522}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_352309144}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1095262220}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1821921688}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1995347996}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x75688683}[关闭语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x349423763}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] shutdown]{lang="EN-US"}
:::

::: {#-1318713737 .myid}
[]{#_Toc404794363}[]{#struct_0_16135_x6401_x436495175}[]{#_Toc355262370}[]{#_Toc295911322}[]{#_Toc262031014}[]{#_Toc135295519}[]{#_Toc130097167}[]{#_Toc129160888}[]{#_Toc47776231}

**语音实体 \-- 语音实体命令 \-- vad-on**

------------------------------------------------------------------------

[**[vad-on]{lang="EN-US"}**]{#struct_0_16135_x6401_x1740792943}[命令用来使能静音抑制功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vad-on**]{lang="EN-US"}]{#struct_0_16135_x6401_x1501211777}[命令用来关闭静音抑制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1867393502}

[**[vad-on]{lang="PT-BR"}**]{#struct_0_16135_x6401_1502523840}[ \[ **g711** \| **g723r53** \| **g723r63** \| **g729a** \| **g729r8** \] \*]{lang="PT-BR"}

[**[undo]{lang="PT-BR"}**]{#struct_0_16135_x6401_x731861337}[ **vad-on** \[ **g711** \| **g723r53** \| **g723r63** \| **g729a** \| **g729r8** \] \*]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x75754219}

[[静音抑制功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16135_x6401_1924925754}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1173170963}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_1276291069}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_2119483568}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_17341269}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_236330025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1078638941}

[**[g711]{lang="PT-BR"}**]{#struct_0_16135_x6401_x175155883}[：]{style="font-family:宋体"}[g711]{lang="EN-US"}[编解码方式的静音抑制功能。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_16135_x6401_x1917272605}[：]{style="font-family:宋体"}[g723r53]{lang="EN-US"}[编解码方式的静音抑制功能。]{style="font-family:宋体"}

[**[g723r63]{lang="EN-US"}**]{#struct_0_16135_x6401_x75819755}[：]{style="font-family:宋体"}[g723r63]{lang="EN-US"}[编解码方式的静音抑制功能。]{style="font-family:宋体"}

[**[g729a]{lang="EN-US"}**]{#struct_0_16135_x6401_620937667}[：]{style="font-family:宋体"}[g729a]{lang="EN-US"}[编解码方式的静音抑制功能。]{style="font-family:宋体"}

[**[g729r8]{lang="PT-BR"}**]{#struct_0_16135_x6401_x2022576387}[：]{style="font-family:宋体"}[g729r8]{lang="EN-US"}[编解码方式的静音抑制功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_244190428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不选择编解码方式，表示打开或关闭所有编解码方式的静音抑制功能。]{style="font-family:宋体"}]{#struct_0_16135_x6401_1736991640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.726]{lang="EN-US"}]{#struct_0_16135_x6401_x929390756}[编解码方式不支持静音抑制。]{style="font-family:宋体"}[G.729br8]{lang="EN-US"}[编解码始终支持静音抑制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1057947396}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x1445520266}[开启]{style="font-family:宋体"}[g723r53]{lang="EN-US"}[编解码方式的静音抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_x75885291}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] ]{lang="FR"}[vad-on g723r53]{lang="EN-US"}
:::

::: {#1077951464 .myid}
[]{#_Toc404794364}[]{#struct_0_16135_x6401_x646444585}[]{#_Toc355262371}

**语音实体 \-- 语音实体命令 \-- voice class codec**

------------------------------------------------------------------------

[**[voice class codec]{lang="EN-US"}**]{#struct_0_16135_x6401_51592937}[命令用来创建编解码模板。]{style="font-family:宋体"}

[**[undo voice class code]{lang="EN-US"}**]{#struct_0_16135_x6401_x347818239}[命令用来删除已配置的编解码模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_92714667}

[**[voice class codec ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_16135_x6401_1056039376}

[**[undo voice class codec ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_16135_x6401_1339315539}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1559638470}

[[不存在编解码模板。]{style="font-family:宋体"}]{#struct_0_16135_x6401_1617053797}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1157912756}

[[语音视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_x75950827}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1818257594}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_136732141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1799145611}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x229001635}

[*[tag]{lang="EN-US"}*]{#struct_0_16135_x6401_x733317872}[：编解码模]{style="font-family:宋体"}[板号，取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[2147483647]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x242580359}

[[设备最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_16135_x6401_1719079220}[个编解码模板。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_298399075}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x74967787}[配置编解码模板]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_1188874891}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice class codec 1]{lang="EN-US"}

[\[sysname-voice-class-codec1\]]{lang="EN-US"}
:::

::: {#1334524894 .myid}
[]{#_Toc404794365}[]{#struct_0_16135_x6401_x1545320227}[]{#_Toc355262372}

**语音实体 \-- 语音实体命令 \-- voice-class codec**

------------------------------------------------------------------------

[**[voice-class codec]{lang="EN-US"}**]{#struct_0_16135_x6401_942597312}[命令用来配置将指定的编解码模板绑定到语音实体。]{style="font-family:宋体"}

[**[undo voice-class codec]{lang="EN-US"}**]{#struct_0_16135_x6401_1762701472}[用来取消已有的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_201705470}

[**[voice-class codec]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_16135_x6401_1176161040}

[**[undo voice-class codec]{lang="EN-US"}**]{#struct_0_16135_x6401_2066858065}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x75033323}

[[编解码模板和语音实体没有绑定关系。]{style="font-family:宋体"}]{#struct_0_16135_x6401_x432827277}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1239582019}

[[POTS]{lang="EN-US"}]{#struct_0_16135_x6401_x630129233}[语音实体视图]{style="font-family:宋体"}[/VoIP]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}[/IVR]{lang="EN-US"}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1592070733}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_753031343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_1939828687}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1369523981}

[*[tag]{lang="EN-US"}*]{#struct_0_16135_x6401_x75492074}[：绑定的编解码模板号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1490029847}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户可以将一个不存在的编解码模板绑定到语音实体，但只有在使用]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1011844384}**[codec preference]{lang="EN-US"}**[命令完成编解码优先级的设置后，该编解码模板才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在语音实体下只能绑定一个编解码模板，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_16135_x6401_2001178727}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x2141537314}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_1152419813}[将编解码模板]{style="font-family:宋体"}[1]{lang="EN-US"}[绑定到语音实体。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_638538953}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] voice-class codec 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x540923634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[codec preference]{lang="EN-US"}**]{#struct_0_16135_x6401_x75557610}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice class codec]{lang="EN-US"}**]{#struct_0_16135_x6401_x674941241}
:::

::: {#654793759 .myid}
[]{#_Toc404794366}[]{#struct_0_16135_x6401_1211207236}[]{#_Toc355262374}[]{#_Toc295911323}[]{#_Toc262031015}[]{#_Toc135295523}[]{#_Toc130097171}[]{#_Toc129160892}[]{#_Toc47776235}[]{#_Toc353354246}[]{#_Toc354744858}[]{#_Toc354817999}[]{#_Toc354936062}[]{#_Toc355261898}[]{#_Toc355262373}[]{#_Toc355262458}[]{#_Toc345246004}[]{#_Toc346096112}

**语音实体 \-- 语音实体命令 \-- voice-setup**

------------------------------------------------------------------------

[**[voice-setup]{lang="EN-US"}**]{#struct_0_16135_x6401_216431103}[命令用来进入语音视图，并启用语音服务。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **voice-setup**]{lang="EN-US"}]{#struct_0_16135_x6401_1656929092}[命令用来关闭语音服务，并退出语音视图，删除所有语音配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1799465939}

[**[voice-setup]{lang="EN-US"}**]{#struct_0_16135_x6401_x496904397}

[**[undo]{lang="EN-US"}**[ **voice-setup**]{lang="EN-US"}]{#struct_0_16135_x6401_286783743}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1848997507}

[[语音服务处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16135_x6401_x75623146}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x1614643899}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16135_x6401_x1952394954}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16135_x6401_1247369415}

[[network-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1644667539}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16135_x6401_x1418402569}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16135_x6401_x799104245}

[[\# ]{lang="EN-US"}]{#struct_0_16135_x6401_x1022035959}[进入语音视图，并启用语音服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16135_x6401_2048972320}

[\[Sysname\] voice-setup]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
