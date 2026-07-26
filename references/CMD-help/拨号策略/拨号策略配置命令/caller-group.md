::: {#-2043589798 .myid}
[]{#_Toc136850854}[]{#_Toc129160901}[]{#_Toc47776180}[]{#_Toc144027373}[]{#_Toc135295452}[]{#_Toc132701216}[]{#_Toc130097095}[]{#_Toc129160817}[]{#_Toc47776155}[]{#_Toc404794391}[]{#struct_0_59978_43282_x622782746}[]{#_Toc205711285}[]{#_Toc176074718}

**拨号策略 \-- 拨号策略配置命令 \-- caller-group**

------------------------------------------------------------------------

[**[caller-group]{lang="EN-US"}**]{#struct_0_59978_43282_2107173556}[命令用来将用户组绑定到指定的语音实体。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **caller-group**]{lang="EN-US"}]{#struct_0_59978_43282_x716201368}[命令用来取消语音实体和用户组的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_916479321}

[**[caller-group]{lang="EN-US"}**[ { **deny** \| **permit** } *group-id*]{lang="EN-US"}]{#struct_0_59978_43282_x1874866363}

[**[undo]{lang="EN-US"}**[ **caller-group** { { **deny** \| **permit** } *group-id* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_236153918}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x74967786}

[[语音实体下没有绑定用户组，即允许任意主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_59978_43282_1188874890}[呼入。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1545254691}

[[POTS/VoIP/IVR]{lang="EN-US"}]{#struct_0_59978_43282_x964800837}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2100354615}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1966849334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1499924056}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1128861492}

[**[deny]{lang="EN-US"}**]{#struct_0_59978_43282_676765914}[：拒绝用户组中的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_59978_43282_x423033633}[：允许用户组中的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[*[group-id]{lang="EN-US"}*]{#struct_0_59978_43282_x75033322}[：绑定用户组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_x432827276}[：绑定的所有用户组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_1239647555}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x190138621}[将用户组绑定到指定的语音实体，允许用户组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的主叫号码呼出。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1597604040}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 1 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity1\] caller-group permit 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1859507502}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[subscriber-group]{lang="EN-US"}**]{#struct_0_59978_43282_x533550846}
:::

::: {#-294130838 .myid}
[]{#_Toc404794392}[]{#struct_0_59978_43282_x493952393}[]{#_Toc205711286}

**拨号策略 \-- 拨号策略配置命令 \-- caller-permit**

------------------------------------------------------------------------

[**[caller-permit]{lang="EN-US"}**]{#struct_0_59978_43282_x75492077}[命令用来配置允许呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入的主叫号码模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **caller-permit**]{lang="EN-US"}]{#struct_0_59978_43282_x1490029846}[命令用来删除允许呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入的主叫号码模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1717038971}

[**[caller-permit]{lang="EN-US"}**[ *caller-string*]{lang="EN-US"}]{#struct_0_59978_43282_1244047875}

[**[undo]{lang="EN-US"}**[ **caller-permit** { *caller-string* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_1279851732}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_788512613}

[[没有配置允许呼出]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_59978_43282_x1648212218}[呼入的主叫号码模板，即对呼叫不做任何限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_556881182}

[[POTS/VoIP/IVR]{lang="EN-US"}]{#struct_0_59978_43282_x528304644}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x75557613}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x674941240}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_1211272772}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_1804737586}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_x1107197614}[：所有主叫号码模板。]{style="font-family:宋体"}

[*[caller-string]{lang="EN-US"}*]{#struct_0_59978_43282_x100781184}[：主叫号码模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，号码格式为]{style="font-family:宋体"}[{ \[ + \] *string* \[ \$ \] }\| \$]{lang="EN-US"}[，符号说明如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加号"]{style="font-family:宋体"}]{#struct_0_59978_43282_288296}[+]{lang="EN-US"}["：主叫号码模板如果以"]{style="font-family:宋体"}[+]{lang="EN-US"}["号开头，"]{style="font-family:宋体"}[+]{lang="EN-US"}["号表示整个号码是一个]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准号码，如]{style="font-family:宋体"}[+110022]{lang="EN-US"}[表示]{style="font-family:宋体"}[110022]{lang="EN-US"}[是符合]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准的号码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_59978_43282_x1997118259}[\$]{lang="EN-US"}["：只能放在结尾，表示主叫号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[部分。如果配置]{style="font-family:宋体"}**[caller-permit]{lang="EN-US"}**[ \$]{lang="EN-US"}[，表示主叫号码为空。如果主叫号码模板后没有]{style="font-family:宋体"}[\$]{lang="EN-US"}[字符，则表示允许以此号码开头的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入，例如配置]{style="font-family:宋体"}**[caller-permit ]{lang="EN-US"}**[20]{lang="EN-US"}[，表示允许以]{style="font-family:宋体"}[20]{lang="EN-US"}[开头的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[string]{lang="EN-US"}*]{#struct_0_59978_43282_x75623149}[：由"]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[-]{lang="EN-US"}[9#]{lang="EN-US"}[＊]{lang="EN-US" style="font-family:宋体"}[.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{lang="EN-US" style="font-family:宋体"}[[[表]{style="font-family:宋体"}1-1]{lang="EN-US"}](?-294130838#_Ref148082585)[所示]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[]{#_Ref156018416}[]{#_Ref148082585}[]{#_Toc121809741}[]{#_Toc112125375}[[表1-1 ]{lang="EN-US"}[符号含义描述表]{style="font-family:黑体"}]{#struct_0_59978_43282_x1614643900}

[]{#table_struct_0_428642042}[[符号]{style="font-family:黑体"}]{#struct_0_59978_43282_1133177512}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_59978_43282_136689452}

[[0-9]{lang="EN-US"}]{#struct_0_59978_43282_169747762}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_59978_43282_1770769605}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_59978_43282_x683074766}[和＊]{style="font-family:宋体"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1282533777}

[[.]{lang="EN-US"}]{#struct_0_59978_43282_x75688685}

[[通配符，可以与任何一位有效号码匹配。如：]{style="font-family:宋体"}[555. . . . ]{lang="EN-US"}]{#struct_0_59978_43282_x349423769}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_59978_43282_x435839815}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_59978_43282_1896682323}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}]{#struct_0_59978_43282_1891856179}

[[+]{lang="EN-US"}]{#struct_0_59978_43282_x880328480}

[[指明符号前的字符串重复一次或多次。如：]{style="font-family:宋体"}[ 9876(54)+]{lang="EN-US"}]{#struct_0_59978_43282_x75754221}[可以匹配]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[%]{lang="EN-US"}]{#struct_0_59978_43282_x413726414}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[9876(54)%]{lang="EN-US"}]{#struct_0_59978_43282_x847266825}[可以匹配]{style="font-family:宋体"}[9876]{lang="EN-US"}[、]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[-]{lang="EN-US"}]{#struct_0_59978_43282_x997567224}

[[连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如：]{style="font-family:宋体"}[\[1-9\]]{lang="EN-US"}]{#struct_0_59978_43282_x75819757}[表示从]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[9]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_59978_43282_620937669}["只能出现在"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["中，且连接两端只能为数字，如]{style="font-family:宋体"}[0-9 ]{lang="EN-US"}

[[\[ \]]{lang="EN-US"}]{#struct_0_59978_43282_x2022576385}

[[表示字符选择范围，如：]{style="font-family:宋体"}[\[1-36\]]{lang="EN-US"}]{#struct_0_59978_43282_x918608986}[表示只可匹配单个字符]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[中的某一个]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_59978_43282_x1919977537}["和"]{style="font-family:宋体"}[( )]{lang="EN-US"}["如果嵌套使用，则必须以"]{style="font-family:宋体"}[( \[ \] )]{lang="EN-US"}["形式出现，不允许其它形式，如"]{style="font-family:宋体"}[\[ \[ \] \]]{lang="EN-US"}["、"]{style="font-family:宋体"}[\[ ( ) \]]{lang="EN-US"}["等]{style="font-family:宋体"}

[[( )]{lang="EN-US"}]{#struct_0_59978_43282_x75885293}

[[表示一组字符，如：]{style="font-family:宋体"}[(123)]{lang="EN-US"}]{#struct_0_59978_43282_x646444583}[表示字符串]{style="font-family:宋体"}[123]{lang="EN-US"}[，它一般与符号"]{style="font-family:宋体"}[!]{lang="EN-US"}["、"]{style="font-family:宋体"}[%]{lang="EN-US"}["、"]{style="font-family:宋体"}[+]{lang="EN-US"}["一起使用，如：]{style="font-family:宋体"}[408(12)+]{lang="EN-US"}[，可以匹配]{style="font-family:宋体"}[40812]{lang="EN-US"}[或]{style="font-family:宋体"}[408121212]{lang="EN-US"}[等字符串，但不能匹配]{style="font-family:宋体"}[408]{lang="EN-US"}[，即]{style="font-family:宋体"}[12]{lang="EN-US"}[可连续出现且至少出现一次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](拨号策略命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_59978_43282_51461865}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[每一个符号占用一个字符，符号]{style="font-family:KaiTi_GB2312"}]{#struct_0_59978_43282_x1101170700}[\[ \]]{lang="EN-US"}[和]{style="font-family:KaiTi_GB2312"}[( )]{lang="EN-US"}[占用两个字符。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1892559519}

[[使用该命令最多可以配置]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_59978_43282_x1459313714}[个允许呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入的主叫号码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_2093691425}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x75950829}[配置语音实体]{style="font-family:宋体"}[2]{lang="EN-US"}[允许主叫号码为]{style="font-family:宋体"}[1000]{lang="EN-US"}[和以]{style="font-family:宋体"}[20]{lang="EN-US"}[开头的主叫号码呼出。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1818257592}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 2 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity2\] caller-permit 1000\$]{lang="EN-US"}

[\[Sysname-voice-dial-entity2\] caller-permit 20]{lang="EN-US"}

::: {#-1461383778 .myid}
[]{#_Toc404794393}[]{#struct_0_59978_43282_943301195}[]{#_Toc315859777}[]{#_Toc345522840}[]{#_Toc345522841}[]{#_Toc345522842}[]{#_Toc345522843}[]{#_Toc345522844}[]{#_Toc345522845}[]{#_Toc345522846}[]{#_Toc345522847}[]{#_Toc345522848}[]{#_Toc345522849}[]{#_Toc345522850}[]{#_Toc345522851}[]{#_Toc345522852}[]{#_Toc345522853}[]{#_Toc345522854}[]{#_Toc345522855}[]{#_Toc345522856}[]{#_Toc345522857}[]{#_Toc345522858}[]{#_Toc345522859}[]{#_Toc345522860}[]{#_Toc345522861}[]{#_Toc345522862}

**拨号策略 \-- 拨号策略配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_59978_43282_x1060389365}[命令用来配置用户组的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_59978_43282_x997329838}[命令用来删除已配置的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x660140972}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_59978_43282_x1002561347}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_59978_43282_x74967789}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_1188874897}

[[没有配置用户组的描述信息。]{style="font-family:宋体"}]{#struct_0_59978_43282_x1545713443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_287987679}

[[用户组视图]{style="font-family:宋体"}]{#struct_0_59978_43282_x942808279}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_182498983}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_1779452971}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_1799495095}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_173061634}

[*[text]{lang="EN-US"}*]{#struct_0_59978_43282_x75033325}[：用户组描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x432827279}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_1240237379}[配置用户组]{style="font-family:宋体"}[10]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[international]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x54199022}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] subscriber-group 10]{lang="EN-US"}

[\[Sysname-voice-dial-group10\] description international]{lang="EN-US"}
:::

::: {#-1356103434 .myid}
[]{#_Toc404794394}[]{#struct_0_59978_43282_x461631052}[]{#_Toc205711288}[]{#_Toc144027388}[]{#_Toc135295467}[]{#_Toc130097117}[]{#_Toc129160837}[]{#_Toc47776175}

**拨号策略 \-- 拨号策略配置命令 \-- dial-prefix**

------------------------------------------------------------------------

[**[dial-prefix]{lang="EN-US"}**]{#struct_0_59978_43282_1828492836}[命令用来配置号码前缀。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dial-prefix**]{lang="EN-US"}]{#struct_0_59978_43282_x510190445}[命令用来删除已配置的号码前缀。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x523316715}

[**[dial-prefix]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_59978_43282_x75492076}

[**[undo]{lang="EN-US"}**[ **dial-prefix**]{lang="EN-US"}]{#struct_0_59978_43282_x1490029845}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_150955030}

[[没有配置号码前缀。]{style="font-family:宋体"}]{#struct_0_59978_43282_x808246458}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_1742461425}

[[POTS]{lang="EN-US"}]{#struct_0_59978_43282_464435182}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_204448588}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1721050624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x2132852980}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x75557612}

[*[string]{lang="EN-US"}*]{#struct_0_59978_43282_x674941239}[：号码前缀，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由"]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}["、"]{style="font-family:
宋体"}[,]{lang="EN-US"}["、"]{style="font-family:宋体"}[\#]{lang="EN-US"}["或"]{style="font-family:宋体"}[\*]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?-1356103434#_Ref169498719)[所示。]{style="font-family:宋体"}

[]{#struct_0_59978_43282_1210682953}[]{#_Ref169498719}[]{#_Toc121809753}[[表1-2 ]{lang="EN-US"}[参数]{style="font-family:黑体"}[string]{lang="EN-US"}]{#_Toc112125387}[中的符号含义]{style="font-family:黑体"}

[]{#table_struct_0_426659226}[[符号]{style="font-family:黑体"}]{#struct_0_59978_43282_245046184}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_59978_43282_x53697419}

[[0-9]{lang="EN-US"}]{#struct_0_59978_43282_804982930}

[[表示一位号码，可以是]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_59978_43282_x2098300966}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[,]{lang="EN-US"}]{#struct_0_59978_43282_1925101032}

[[一个逗号表示停顿]{style="font-family:宋体"}[500]{lang="EN-US"}]{#struct_0_59978_43282_x75623148}[毫秒再发送下一个号码，可以出现在号码的任意位置]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_59978_43282_x1614643901}[或]{style="font-family:宋体"}[\*]{lang="EN-US"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1595705843}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_x424194072}

[[配置号码前缀后，设备以"号码前缀＋拨入号码"作为被叫号码。添加号码前缀后，如果号码总长度超过]{style="font-family:宋体"}[31]{lang="EN-US"}]{#struct_0_59978_43282_1372466788}[位时，设备只发送前]{style="font-family:宋体"}[31]{lang="EN-US"}[位号码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_980348973}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x2143921534}[配置号码前缀为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x75688684}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 3 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity3\] dial-prefix 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x349423770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[match-template]{lang="EN-US"}**]{#struct_0_59978_43282_x436429640}

::: {#-1129576696 .myid}
[]{#_Toc404794395}[]{#struct_0_59978_43282_x235924780}[]{#_Toc353354233}[]{#_Toc313519999}

**拨号策略 \-- 拨号策略配置命令 \-- dial-program**

------------------------------------------------------------------------

[**[dial-program]{lang="EN-US"}**]{#struct_0_59978_43282_x1859907436}[命令用来进入语音拨号策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dial-program**]{lang="EN-US"}]{#struct_0_59978_43282_1427232405}[命令用来删除语音拨号策略视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_865672536}

[**[dial-program]{lang="EN-US"}**]{#struct_0_59978_43282_x75754220}

[**[undo dial-program]{lang="EN-US"}**]{#struct_0_59978_43282_x413726413}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x846939145}

[[语音视图]{style="font-family:宋体"}]{#struct_0_59978_43282_1319840546}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x503380959}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_413987099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_1632894633}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_1885487529}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x75819756}[进入语音拨号策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_620937670}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}
:::

::::: {#-201518822 .myid}
[]{#_Toc404794396}[]{#struct_0_59978_43282_x66261256}[]{#_Toc205711291}[]{#_Toc136850855}[]{#_Toc129160902}[]{#_Toc47776186}[]{#_Toc345522865}[]{#_Toc345522866}[]{#_Toc345522867}[]{#_Toc345522868}[]{#_Toc345522869}[]{#_Toc345522870}[]{#_Toc345522871}[]{#_Toc345522872}[]{#_Toc345522873}[]{#_Toc345522874}[]{#_Toc345522875}[]{#_Toc345522876}[]{#_Toc345522877}[]{#_Toc345522878}[]{#_Toc345522879}[]{#_Toc345522880}[]{#_Toc345522881}[]{#_Toc345522882}[]{#_Toc345522883}[]{#_Toc345522884}[]{#_Toc345522885}[]{#_Toc345522886}[]{#_Toc345522887}[]{#_Toc345522888}[]{#_Toc345522889}[]{#_Toc345522890}[]{#_Toc345522891}[]{#_Toc345522892}[]{#_Toc345522893}[]{#_Toc345522894}[]{#_Toc345522895}[]{#_Toc345522896}[]{#_Toc345522897}[]{#_Toc345522898}[]{#_Toc345522899}[]{#_Toc345522900}[]{#_Toc345522901}[]{#_Toc345522902}[]{#_Toc345522903}[]{#_Toc345522904}[]{#_Toc345522905}[]{#_Toc345522927}[]{#_Toc345522928}[]{#_Toc345522929}[]{#_Toc345522930}[]{#_Toc345522931}[]{#_Toc345522932}[]{#_Toc345522933}[]{#_Toc345522934}[]{#_Toc345522935}[]{#_Toc345522936}[]{#_Toc345522937}[]{#_Toc345522938}[]{#_Toc345522939}[]{#_Toc345522940}[]{#_Toc345522941}[]{#_Toc345522942}[]{#_Toc345522943}[]{#_Toc345522944}[]{#_Toc345522945}[]{#_Toc345522946}[]{#_Toc345522947}[]{#_Toc345522948}[]{#_Toc345522949}[]{#_Toc345522950}[]{#_Toc345522951}[]{#_Toc345522952}[]{#_Toc345522953}[]{#_Toc345522954}[]{#_Toc345522955}[]{#_Toc345522956}[]{#_Toc345522957}[]{#_Toc345522958}

**拨号策略 \-- 拨号策略配置命令 \-- dot-match**

------------------------------------------------------------------------

[**[dot-match]{lang="EN-US"}**]{#struct_0_59978_43282_1182927549}[命令用来配置点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dot-match**]{lang="EN-US"}]{#struct_0_59978_43282_x1053633504}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x823828693}

[**[dot-match]{lang="EN-US"}**[ { **end-only** \| **left-right** \| **right-left** }]{lang="EN-US"}]{#struct_0_59978_43282_1453762235}

[**[undo]{lang="EN-US"}**[ **dot-match**]{lang="EN-US"}]{#struct_0_59978_43282_x580437123}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x848321860}

[[点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**]{#struct_0_59978_43282_x75885292}["的匹配规则为]{style="font-family:宋体"}**[end-only]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x646444584}

[[语音号码变换视图]{style="font-family:宋体"}]{#struct_0_59978_43282_51658473}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x515935296}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_1559441625}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1218203661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_431044912}

[**[end-only]{lang="EN-US"}**]{#struct_0_59978_43282_x75950828}[：表示只保留]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中末尾所有点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["对应的号码。即无论]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[的末尾是否有点"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["，将]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中末尾所有点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["对应的号码填充到]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[末尾。]{style="font-family:宋体"}

[**[left-right]{lang="EN-US"}**]{#struct_0_59978_43282_x1818257591}[：表示以]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[格式中点的个数，从左至右提取]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["对应的号码。]{style="font-family:宋体"}

[**[right-left]{lang="EN-US"}**]{#struct_0_59978_43282_540016668}[：表示以]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[格式中点的个数，从右至左提取]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["对应的号码。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](拨号策略命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_59978_43282_x813958139}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[上述描述中的]{style="font-family:KaiTi_GB2312"}*[input-template]{lang="EN-US"}*]{#struct_0_59978_43282_321615833}[和]{style="font-family:KaiTi_GB2312"}*[output-template]{lang="EN-US"}*[指的是]{style="font-family:KaiTi_GB2312"}**[rule]{lang="EN-US"}**[命令中的参数。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_191734111}

[[此处的"点号"匹配指的是虚号码匹配。虚号码匹配是指与正则表达式中的可变部分（如]{style="font-family:宋体"}[.+%\![\]]{lang="EN-US"}]{#struct_0_59978_43282_1853460654}[）进行匹配。例如号码]{style="font-family:宋体"}[1255]{lang="EN-US"}[与正则表达式进行虚号码匹配，与正则表达式]{style="font-family:宋体"}[1\[234\]55]{lang="EN-US"}[匹配的号码为]{style="font-family:宋体"}[2]{lang="EN-US"}[，与正则表达式]{style="font-family:宋体"}[125+]{lang="EN-US"}[匹配的号码为]{style="font-family:宋体"}[5]{lang="EN-US"}[，与正则表达式]{style="font-family:宋体"}[1..5]{lang="EN-US"}[匹配的号码为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，号码始终按照从左到右的顺序进行填充，与]{style="font-family:宋体"}**[dot-match]{lang="EN-US"}**]{#struct_0_59978_43282_2112300168}[设置的参数无关。具体例子可参考命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[中的举例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1140328449}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x74967788}[设置号码变换表]{style="font-family:宋体"}[20]{lang="EN-US"}[的点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["匹配规则为]{style="font-family:宋体"}**[right-left]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1188874896}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 20]{lang="EN-US"}

[\[Sysname-voice-dial-substitute20\] dot-match right-left]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1545647907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_59978_43282_x1860739695}
:::::

::: {#-341072778 .myid}
[]{#_Toc404794397}[]{#struct_0_59978_43282_x1353842721}

**拨号策略 \-- 拨号策略配置命令 \-- entity hunt**

------------------------------------------------------------------------

[**[entity hunt]{lang="EN-US"}**]{#struct_0_59978_43282_x151218786}[命令用来配置语音实体的选取规则顺序。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **entity hunt**]{lang="EN-US"}]{#struct_0_59978_43282_x1602644297}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x222578240}

[**[entity hunt ]{lang="EN-US"}***[hunt-number]{lang="EN-US"}*]{#struct_0_59978_43282_29468181}

[**[undo entity hunt]{lang="EN-US"}**]{#struct_0_59978_43282_1994446984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_1804288359}

[[语音实体的选取规则顺序为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_59978_43282_x1354039329}[，即首先采用精确匹配，其次是语音实体优先级，最后是随机选择。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x5494530}

[[语音拨号视图]{style="font-family:宋体"}]{#struct_0_59978_43282_x2070823434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_1598959588}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1585431014}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1945960226}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_321084909}

[*[hunt-number]{lang="EN-US"}*]{#struct_0_59978_43282_x1768674449}[：语音实体的选取规则顺序，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_59978_43282_x1353973793}[：语音实体的选取规则依次为精确匹配，语音实体的优先级，随机选择。]{style="font-family:宋体"}

[[1]{lang="EN-US"}]{#struct_0_59978_43282_x1609382823}[：语音实体的选取规则依次为精确匹配，语音实体的优先级，最久不使用。]{style="font-family:宋体"}

[[2]{lang="EN-US"}]{#struct_0_59978_43282_x763155079}[：语音实体的选取规则依次为语音实体的优先级，精确匹配，随机选择。]{style="font-family:宋体"}

[[3]{lang="EN-US"}]{#struct_0_59978_43282_x232626236}[：语音实体的选取规则依次为语音实体的优先级，精确匹配，最久不使用。]{style="font-family:宋体"}

[[4]{lang="EN-US"}]{#struct_0_59978_43282_x174786148}[：语音实体的选取规则依次为最久不使用，精确匹配语，语音实体的优先级。]{style="font-family:宋体"}

[[5]{lang="EN-US"}]{#struct_0_59978_43282_1752612416}[：语音实体的选取规则依次为最久不使用，语音实体的优先级，精确匹配。]{style="font-family:宋体"}

[[6]{lang="EN-US"}]{#struct_0_59978_43282_x2110047335}[：语音实体的选取规则为随机选择。]{style="font-family:宋体"}

[[7]{lang="EN-US"}]{#struct_0_59978_43282_x1353646113}[：语音实体的选取规则为最久不使用。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[规则描述]{style="font-family:黑体"}]{#struct_0_59978_43282_489193166}

[]{#table_struct_0_1050540096}[[规则]{style="font-family:黑体"}]{#struct_0_59978_43282_1481952708}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_59978_43282_x1370387179}

[[精确匹配]{style="font-family:宋体"}]{#struct_0_59978_43282_x41856049}

[[号码串从左至右，匹配的号码位越多，精确度越高，一旦遇到不能唯一匹配的号码，该规则停止]{style="font-family:宋体"}]{#struct_0_59978_43282_x1353580577}

[[语音实体的优先级]{style="font-family:宋体"}]{#struct_0_59978_43282_1893034786}

[[通过]{style="font-family:宋体"}**[priority]{lang="EN-US"}**]{#struct_0_59978_43282_936454929}[命令可以将语音实体的优先级共分为]{style="font-family:宋体"}[11]{lang="EN-US"}[级，优先级高的语音实体会被优先匹配]{style="font-family:宋体"}

[[随机选择]{style="font-family:宋体"}]{#struct_0_59978_43282_786448653}

[[随机从符合条件的语音实体中选取一个]{style="font-family:宋体"}]{#struct_0_59978_43282_1955788033}

[[最久不使用]{style="font-family:宋体"}]{#struct_0_59978_43282_x1353777185}

[[选择最长时间没有使用的语音实体]{style="font-family:宋体"}]{#struct_0_59978_43282_1000266525}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2116940448}

[[当号码能匹配多个语音实体时，设备会根据配置的选取规则顺序来选择语音实体。如果应用第一个规则后仍无法区别语音实体的优先级顺序，就应用第二个选取规则，依此类推。]{style="font-family:宋体"}]{#struct_0_59978_43282_x1070390648}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_117169155}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x1074085851}[配置语音实体的选取规则顺序为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1353711649}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity hunt 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x805103444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[priority]{lang="EN-US"}**]{#struct_0_59978_43282_x694387648}

::: {#-1049956519 .myid}
[]{#_Toc404794398}[]{#struct_0_59978_43282_x1083106514}[]{#_Toc205711292}[]{#_Toc136850856}[]{#_Toc129160903}[]{#_Toc47776194}

**拨号策略 \-- 拨号策略配置命令 \-- first-rule**

------------------------------------------------------------------------

[**[first-rule]{lang="EN-US"}**]{#struct_0_59978_43282_1387580363}[命令用来配置号码变换表首先使用的号码变换规则]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **first-rule**]{lang="EN-US"}]{#struct_0_59978_43282_505509577}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x456012541}

[**[first-rule]{lang="EN-US"}**[ *id*]{lang="EN-US"}]{#struct_0_59978_43282_x75033324}

[**[undo]{lang="EN-US"}**[ **first-rule**]{lang="EN-US"}]{#struct_0_59978_43282_x432827278}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_1240302915}

[[没有配置首先使用的号码变换规则]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_59978_43282_x1606133052}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1170071438}

[[语音号码变换视图]{style="font-family:宋体"}]{#struct_0_59978_43282_1463133380}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_538227062}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_1540712110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x435856835}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991449382}

[*[id]{lang="EN-US"}*]{#struct_0_59978_43282_1666762920}[：首先使用的号码变换规则]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_967785630}

[[在匹配号码变换规则时，首先使用]{style="font-family:宋体"}**[first-rule]{lang="EN-US"}**]{#struct_0_59978_43282_1845759800}[命令设置的号码变换规则。如果未配置或匹配首选变换规则失败，则顺序匹配其他号码变换规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2036572952}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x413612349}[设置号码变换表]{style="font-family:宋体"}[20]{lang="EN-US"}[首先使用号码变换规则]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1933502893}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 20]{lang="EN-US"}

[\[Sysname-voice-dial-substitute20\] rule 4 663 3]{lang="EN-US"}

[\[Sysname-voice-dial-substitute20\] first-rule 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1447034295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_59978_43282_x1991383846}
:::

::: {#-1681238638 .myid}
[]{#_Toc404794399}[]{#struct_0_59978_43282_x1025234479}[]{#_Toc205711293}[]{#_Toc176074726}

**拨号策略 \-- 拨号策略配置命令 \-- match-template**

------------------------------------------------------------------------

[**[match-template]{lang="EN-US"}**]{#struct_0_59978_43282_x2108172624}[命令用来配置用户组的主叫号码模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match-template**]{lang="EN-US"}]{#struct_0_59978_43282_415826943}[命令用来删除已配置的主叫号码模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1759297392}

[**[match-template]{lang="EN-US"}**[ *match-string*]{lang="EN-US"}]{#struct_0_59978_43282_1167200370}

[**[undo]{lang="EN-US"}**[ **match-template** { *match-string* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_1559122959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x84198466}

[[用户组下没有配置主叫号码模板。]{style="font-family:宋体"}]{#struct_0_59978_43282_1776828225}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991318310}

[[用户组视图]{style="font-family:宋体"}]{#struct_0_59978_43282_1982592663}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_1036488083}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_1618262391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1756816343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1682979648}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_300497442}[：所有主叫号码模板。]{style="font-family:宋体"}

[*[caller-string]{lang="EN-US"}*]{#struct_0_59978_43282_x1228542801}[：主叫号码模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，号码格式为]{style="font-family:宋体"}[{ \[ + \] *string* \[ \$ \] }\| \$]{lang="EN-US"}[，符号说明如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加号"]{style="font-family:宋体"}]{#struct_0_59978_43282_986978638}[+]{lang="EN-US"}["：主叫号码模板如果以"]{style="font-family:宋体"}[+]{lang="EN-US"}["号开头，"]{style="font-family:宋体"}[+]{lang="EN-US"}["号表示整个号码是一个]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准号码，如]{style="font-family:宋体"}[+110022]{lang="EN-US"}[表示]{style="font-family:宋体"}[110022]{lang="EN-US"}[是符合]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准的号码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991252774}[\$]{lang="EN-US"}["：只能放在结尾，表示主叫号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[部分。如果配置]{style="font-family:宋体"}**[match-template]{lang="EN-US"}**[ \$]{lang="EN-US"}[，表示主叫号码为空。如果主叫号码模板后没有]{style="font-family:宋体"}[\$]{lang="EN-US"}[字符，则表示允许以此号码开头的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入，例如配置]{style="font-family:宋体"}**[match-template]{lang="EN-US"}**[ 20]{lang="EN-US"}[，表示允许以]{style="font-family:宋体"}[20]{lang="EN-US"}[开头的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[string]{lang="EN-US"}*]{#struct_0_59978_43282_x1166649973}[：由"]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[-]{lang="EN-US"}[9#]{lang="EN-US"}[＊]{lang="EN-US" style="font-family:宋体"}[.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{lang="EN-US" style="font-family:宋体"}[[[表]{style="font-family:宋体"}1-4]{lang="EN-US"}](?-1681238638#_Ref341709313)[所示]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[]{#struct_0_59978_43282_x353575379}[[表1-4 ]{lang="EN-US"}[符号含义描述表]{style="font-family:
黑体"}]{#_Ref341709313}

[]{#table_struct_0_419682362}[[符号]{style="font-family:黑体"}]{#struct_0_59978_43282_1704962918}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_59978_43282_x1021167221}

[[0-9]{lang="EN-US"}]{#struct_0_59978_43282_1277245801}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_59978_43282_x1821469926}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_59978_43282_x1991187238}[和＊]{style="font-family:宋体"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x944534959}

[[.]{lang="EN-US"}]{#struct_0_59978_43282_x1798357304}

[[通配符，可以与任何一位有效号码匹配。如：]{style="font-family:宋体"}[555. . . . ]{lang="EN-US"}]{#struct_0_59978_43282_1419788314}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_59978_43282_1034529181}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_59978_43282_973358269}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[符号"]{style="font-family:宋体"}[!%+]{lang="EN-US"}]{#struct_0_59978_43282_x1991121702}["前的字符串（一位号码或号码串），作为非精确匹配的号码，处理类似"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["通配符；这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}

[[+]{lang="EN-US"}]{#struct_0_59978_43282_x1252786546}

[[指明符号前的字符串重复一次或多次。如：]{style="font-family:宋体"}[ 9876(54)+]{lang="EN-US"}]{#struct_0_59978_43282_x553199913}[可以匹配]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[%]{lang="EN-US"}]{#struct_0_59978_43282_x1216798143}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[9876(54)%]{lang="EN-US"}]{#struct_0_59978_43282_x193993074}[可以匹配]{style="font-family:宋体"}[9876]{lang="EN-US"}[、]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[-]{lang="EN-US"}]{#struct_0_59978_43282_239650996}

[[连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如：]{style="font-family:宋体"}[\[1-9\]]{lang="EN-US"}]{#struct_0_59978_43282_x1991056166}[表示从]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[9]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_59978_43282_527580871}["只能出现在"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["中，且连接两端只能为数字，如]{style="font-family:宋体"}[0-9 ]{lang="EN-US"}

[[\[ \]]{lang="EN-US"}]{#struct_0_59978_43282_x462651966}

[[表示字符选择范围，如：]{style="font-family:宋体"}[\[1-36\]]{lang="EN-US"}]{#struct_0_59978_43282_2134545955}[表示只可匹配单个字符]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[中的某一个]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_59978_43282_x1990990630}["和"]{style="font-family:宋体"}[( )]{lang="EN-US"}["如果嵌套使用，则必须以"]{style="font-family:宋体"}[( \[ \] )]{lang="EN-US"}["形式出现，不允许其它形式，如"]{style="font-family:宋体"}[\[ \[ \] \]]{lang="EN-US"}["、"]{style="font-family:宋体"}[\[ ( ) \]]{lang="EN-US"}["等]{style="font-family:宋体"}

[[( )]{lang="EN-US"}]{#struct_0_59978_43282_x133450147}

[[表示一组字符，如：]{style="font-family:宋体"}[(123)]{lang="EN-US"}]{#struct_0_59978_43282_x1035672937}[表示字符串]{style="font-family:宋体"}[123]{lang="EN-US"}[，它一般与符号"]{style="font-family:宋体"}[!]{lang="EN-US"}["、"]{style="font-family:宋体"}[%]{lang="EN-US"}["、"]{style="font-family:宋体"}[+]{lang="EN-US"}["一起使用，如：]{style="font-family:宋体"}[408(12)+]{lang="EN-US"}[，可以匹配]{style="font-family:宋体"}[40812]{lang="EN-US"}[或]{style="font-family:宋体"}[408121212]{lang="EN-US"}[等字符串，但不能匹配]{style="font-family:宋体"}[408]{lang="EN-US"}[，即]{style="font-family:宋体"}[12]{lang="EN-US"}[可连续出现且至少出现一次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](拨号策略命令.files/image001.png){#图片 16 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_59978_43282_285609323}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[每一个符号占用一个字符，符号]{style="font-family:KaiTi_GB2312"}]{#struct_0_59978_43282_x1994081598}[\[ \]]{lang="EN-US"}[和]{style="font-family:KaiTi_GB2312"}[( )]{lang="EN-US"}[占用两个字符。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1206482215}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x1991973670}[配置用户组]{style="font-family:宋体"}[2]{lang="EN-US"}[的主叫号码模板为]{style="font-family:宋体"}[1...]{lang="EN-US"}[，表示允许以]{style="font-family:宋体"}[1]{lang="EN-US"}[开头的四位主叫号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1991908134}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] subscriber-group 2]{lang="EN-US"}

[\[Sysname-voice-dial-group2\] match-template 1...]{lang="EN-US"}

::: {#2057585610 .myid}
[]{#_Toc404794400}[]{#struct_0_59978_43282_x1899780927}

**拨号策略 \-- 拨号策略配置命令 \-- max-conn**

------------------------------------------------------------------------

[**[max-conn]{lang="EN-US"}**]{#struct_0_59978_43282_x1384742912}[命令用来配置最大呼叫连接数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **max-conn**]{lang="EN-US"}]{#struct_0_59978_43282_x39944395}[命令用来删除最大呼叫连接数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_450152535}

[**[max-conn]{lang="EN-US"}**[ *max-number*]{lang="EN-US"}]{#struct_0_59978_43282_x1452321259}

[**[undo max-conn]{lang="EN-US"}**]{#struct_0_59978_43282_x17567805}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_655449580}

[[没有配置最大呼叫连接数，即不对呼叫连接数进行限制。]{style="font-family:宋体"}]{#struct_0_59978_43282_x2077311072}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_644831446}

[[POTS/VoIP/IVR]{lang="EN-US"}]{#struct_0_59978_43282_1209553736}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1899846463}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1916592445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x154701694}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1826652646}

[*[max-number]{lang="EN-US"}*]{#struct_0_59978_43282_x1559071620}[：最大呼叫连接数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不允许呼叫。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_1248209015}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x1061069430}[设置语音实体的最大呼叫连接数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x551804259}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 voip]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] max-conn 5]{lang="EN-US"}
:::

::: {#1305093734 .myid}
[]{#_Toc404794401}[]{#struct_0_59978_43282_x1950788888}[]{#_Toc205711296}[]{#_Toc136850859}[]{#_Toc129160906}[]{#_Toc47776201}[]{#_Toc182049293}[]{#_Toc347148817}[]{#_Toc347148818}[]{#_Toc347148819}[]{#_Toc347148820}[]{#_Toc347148821}[]{#_Toc347148822}[]{#_Toc347148823}[]{#_Toc347148824}[]{#_Toc347148825}[]{#_Toc347148826}[]{#_Toc347148827}[]{#_Toc347148828}[]{#_Toc347148829}[]{#_Toc347148830}[]{#_Toc347148831}[]{#_Toc347148832}[]{#_Toc347148833}[]{#_Toc347148834}[]{#_Toc347148835}[]{#_Toc347148836}[]{#_Toc347148837}[]{#_Toc347148838}[]{#_Toc347148839}[]{#_Toc347148840}[]{#_Toc347148841}[]{#_Toc347148842}[]{#_Toc347148843}[]{#_Toc347148844}[]{#_Toc347148845}[]{#_Toc347148846}[]{#_Toc347148847}[]{#_Toc347148848}[]{#_Toc347148849}[]{#_Toc347148850}[]{#_Toc347148851}[]{#_Toc347148852}[]{#_Toc347148853}[]{#_Toc347148854}[]{#_Toc347148855}[]{#_Toc347148856}[]{#_Toc347148857}[]{#_Toc347148858}[]{#_Toc347148859}[]{#_Toc347148860}[]{#_Toc347148861}[]{#_Toc347148862}[]{#_Toc347148863}[]{#_Toc347148864}[]{#_Toc347148865}[]{#_Toc347148866}[]{#_Toc347148867}[]{#_Toc347148868}[]{#_Toc347148869}

**拨号策略 \-- 拨号策略配置命令 \-- number-match**

------------------------------------------------------------------------

[**[number-match]{lang="EN-US"}**]{#struct_0_59978_43282_x353698171}[命令用来配置号码匹配策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **number-match**]{lang="EN-US"}]{#struct_0_59978_43282_x1110927452}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1625849734}

[**[number-match]{lang="EN-US"}**[ { **longest** \| **shortest** }]{lang="EN-US"}]{#struct_0_59978_43282_1965968461}

[**[undo]{lang="EN-US"}**[ **number-match**]{lang="EN-US"}]{#struct_0_59978_43282_617000399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1058173914}

[[使用最短号码匹配策略。]{style="font-family:宋体"}]{#struct_0_59978_43282_x1034345258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1356129879}

[[语音拨号策略视图]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991449381}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_1263478393}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_728215159}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_2132071025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_2089260033}

[**[longest]{lang="EN-US"}**]{#struct_0_59978_43282_x113677650}[：使用最长号码匹配策略。]{style="font-family:宋体"}

[**[shortest]{lang="EN-US"}**]{#struct_0_59978_43282_406079357}[：使用最短号码匹配策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x240018176}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_1440134463}[配置使用最长号码匹配策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1991383845}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-match longest]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1428519006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminator]{lang="EN-US"}**]{#struct_0_59978_43282_x1089022860}
:::

::: {#-546136499 .myid}
[]{#_Toc404794402}[]{#struct_0_59978_43282_x828469494}[]{#_Toc205711298}[]{#_Toc136850860}[]{#_Toc129160907}[]{#_Toc47776202}[]{#_Toc345522965}[]{#_Toc345522966}[]{#_Toc345522967}[]{#_Toc345522968}[]{#_Toc345522969}[]{#_Toc345522970}[]{#_Toc345522971}[]{#_Toc345522972}[]{#_Toc345522973}[]{#_Toc345522974}[]{#_Toc345522975}[]{#_Toc345522976}[]{#_Toc345522977}[]{#_Toc345522978}[]{#_Toc345522979}[]{#_Toc345522980}[]{#_Toc345522981}[]{#_Toc345522982}[]{#_Toc345522983}[]{#_Toc163276493}

**拨号策略 \-- 拨号策略配置命令 \-- number-substitute**

------------------------------------------------------------------------

[**[number-substitute]{lang="EN-US"}**]{#struct_0_59978_43282_x916579630}[命令用来创建号码变换规则表，并进入语音号码变换视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **number-substitute**]{lang="EN-US"}]{#struct_0_59978_43282_621675194}[命令用来删除已配置的号码变换规则表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x510103046}

[**[number-substitute]{lang="EN-US"}**[ *list-number*]{lang="EN-US"}]{#struct_0_59978_43282_666137668}

[**[undo]{lang="EN-US"}**[ **number-substitute** { *list-number* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_x1991318309}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1102455516}

[[不存在号码变换规则表。]{style="font-family:宋体"}]{#struct_0_59978_43282_1712955610}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x410230323}

[[语音拨号策略视图]{style="font-family:宋体"}]{#struct_0_59978_43282_x1872047623}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_2074126623}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_18604997}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_1785205710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2036744517}

[*[list-number]{lang="EN-US"}*]{#struct_0_59978_43282_x1991252773}[：号码变换规则表的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_x763365446}[：所有号码变换规则表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_525887493}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x1305329606}[创建号码变换规则表，并进入语音号码变换视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_788967155}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 1]{lang="FR"}

[\[Sysname-voice-dial-substitute1\]]{lang="FR"}
:::

::: {#567732879 .myid}
[]{#_Toc404794403}[]{#struct_0_59978_43282_12570972}[]{#_Toc205711299}[]{#_Toc136850861}[]{#_Toc129160908}[]{#_Toc47776205}

**拨号策略 \-- 拨号策略配置命令 \-- priority**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_59978_43282_x930683625}[命令用来配置语音实体的优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_59978_43282_x1933617298}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991187237}

[**[priority]{lang="EN-US"}***[ priority-order]{lang="EN-US"}*]{#struct_0_59978_43282_x2060280206}

[**[undo]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_59978_43282_x1458006398}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_330337351}

[[优先级别为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_59978_43282_144942701}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_22871114}

[[POTS/VoIP/IVR]{lang="EN-US"}]{#struct_0_59978_43282_858643438}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1227463942}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_173573813}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x834291314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991121701}

[*[priority-order]{lang="EN-US"}*]{#struct_0_59978_43282_313297395}[：语音实体的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，数值越小表示优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_x232226798}

[[当存在多个相同的号码模板时，优先级高的语音实体会被优先匹配。]{style="font-family:宋体"}]{#struct_0_59978_43282_1398536370}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1119862469}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_1607894856}[配置语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_156038482}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] priority 5]{lang="EN-US"}
:::

::: {#664336251 .myid}
[]{#_Toc404794404}[]{#struct_0_59978_43282_x1991056165}[]{#_Toc205711300}[]{#_Toc135295496}[]{#_Toc130097145}[]{#_Toc129160865}[]{#_Toc47776206}[]{#_Toc345522986}[]{#_Toc345522987}

**拨号策略 \-- 拨号策略配置命令 \-- private-line**

------------------------------------------------------------------------

[**[private-line]{lang="EN-US"}**]{#struct_0_59978_43282_930865398}[命令用来配置专线自动振铃功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **private-line**]{lang="EN-US"}]{#struct_0_59978_43282_1645923501}[命令用来关闭专线自动振铃功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x222376429}

[**[private-line]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_59978_43282_1657935811}

[**[undo]{lang="EN-US"}**[ **private-line**]{lang="EN-US"}]{#struct_0_59978_43282_2125192417}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2108813261}

[[没有配置专线自动振铃功能。]{style="font-family:宋体"}]{#struct_0_59978_43282_146231774}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1990990629}

[[FXS/FXO/E&M/]{lang="EN-US"}]{#struct_0_59978_43282_1788929690}[数字语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_x301447660}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x890941639}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x74862098}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x781119081}

[*[string]{lang="EN-US"}*]{#struct_0_59978_43282_226038817}[：被叫号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，可包含]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、"＊"和"]{style="font-family:
宋体"}**[\#]{lang="EN-US"}**["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_426811853}

[[配置专线自动振铃功能后，用户摘机后不需要做任何拨号操作，设备会将]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_59978_43282_1083021713}[作为被叫号码自动拨出。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991973669}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x468783851}[配置专线自动振铃功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_825917237}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] private-line 1000]{lang="EN-US"}
:::

::: {#1629595628 .myid}
[]{#_Toc404794405}[]{#struct_0_59978_43282_x887859832}[]{#_Toc205711301}[]{#_Toc136850862}[]{#_Toc129160909}[]{#_Toc150260199}[]{#_Toc150670698}

**拨号策略 \-- 拨号策略配置命令 \-- rule**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**]{#struct_0_59978_43282_x598534862}[命令用来配置号码变换规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_59978_43282_x518260617}[命令用来删除号码变换规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_530567675}

[**[rule]{lang="EN-US"}**[ *id* *input-template output-template* \[ **number-type** *input-number-type output-number-type* \| **numbering-plan** *input-numbering-plan output-numbering-plan* \] \*]{lang="EN-US"}]{#struct_0_59978_43282_391773413}

[**[undo]{lang="EN-US"}**[ **rule** { *id* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_x1671180495}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991908133}

[[没有配置号码变换规则。]{style="font-family:宋体"}]{#struct_0_59978_43282_1940893881}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x768422341}

[[语音号码变换视图]{style="font-family:宋体"}]{#struct_0_59978_43282_x1809118595}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_760193287}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_1416503831}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_150251184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_421304285}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_x1991449384}[：所有号码变换规则。]{style="font-family:宋体"}

[*[id]{lang="EN-US"}*]{#struct_0_59978_43282_860193866}[：号码变换规则]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[input-template]{lang="EN-US"}*]{#struct_0_59978_43282_x212409481}[：号码变换的输入匹配模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，号码格式为]{style="font-family:宋体"}[\[ **\^** \] \[ + \] *string* \[ \$ \]]{lang="EN-US"}[，符号说明如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[脱字符"]{style="font-family:宋体"}]{#struct_0_59978_43282_2041119458}[\^]{lang="EN-US"}["：表示必须从字符串的第一个字符开始匹配。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[加号"]{style="font-family:宋体"}]{.ItemStepChar}]{#struct_0_59978_43282_1991790690}[[+]{lang="EN-US"}]{.ItemStepChar}[["："]{style="font-family:宋体"}]{.ItemStepChar}[[+]{lang="EN-US"}]{.ItemStepChar}[["号本身不具备特殊含义，仅表示一位有效号码，以"]{style="font-family:
宋体"}]{.ItemStepChar}[[+]{lang="EN-US"}]{.ItemStepChar}[["号开头的号码是一个]{style="font-family:
宋体"}]{.ItemStepChar}[[E.164]{lang="EN-US"}]{.ItemStepChar}[[标准号码。]{style="font-family:宋体"}]{.ItemStepChar}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_59978_43282_x275556283}[\$]{lang="EN-US"}["：]{style="font-family:宋体"}[[表示必须与号码串的最后一个字符匹配，即用户号码和匹配串进行匹配时，用户号码的最后一个号码必须与匹配串的最后一个字符相匹配。]{style="font-family:宋体"}]{.ItemStepChar}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[string]{lang="EN-US"}*]{#struct_0_59978_43282_653377034}[：由"]{style="font-family:
宋体"}[0-9#]{lang="EN-US"}[＊]{style="font-family:宋体"}[.!%]{lang="EN-US"}["中的字符组合形成的字符串。各符号的含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-5]{lang="EN-US"}](?1629595628#_Ref354745785)[所示。]{style="font-family:
宋体"}

[]{#struct_0_59978_43282_x1680607606}[[表1-5 ]{lang="EN-US"}[参数]{style="font-family:
黑体"}*[string]{lang="EN-US"}*]{#_Ref354745785}[中的符号含义]{style="font-family:
黑体"}

[]{#table_struct_0_449389402}[[符号]{style="font-family:黑体"}]{#struct_0_59978_43282_x1731153147}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991383848}

[[0-9]{lang="EN-US"}]{#struct_0_59978_43282_x1475573173}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_59978_43282_x181754896}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_59978_43282_x930867326}[和＊]{style="font-family:宋体"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1177451192}

[[.]{lang="EN-US"}]{#struct_0_59978_43282_366244200}

[[通配符，可以与任何一位有效号码匹配。如：]{style="font-family:宋体"}[555. . . . ]{lang="EN-US"}]{#struct_0_59978_43282_x384551677}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_59978_43282_x1991318312}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_59978_43282_x1149575219}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}]{#struct_0_59978_43282_x154794359}

[[%]{lang="EN-US"}]{#struct_0_59978_43282_127148093}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[54%]{lang="EN-US"}]{#struct_0_59978_43282_959329412}[可以匹配]{style="font-family:宋体"}[54]{lang="EN-US"}[、]{style="font-family:宋体"}[5454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[*[output-template]{lang="EN-US"}*]{#struct_0_59978_43282_x1991252776}[：号码变换的输出匹配模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由"]{style="font-family:宋体"}[0-9#]{lang="EN-US"}[＊]{style="font-family:宋体"}[.]{lang="EN-US"}["中的字符组合形成的字符串，首位支持]{style="font-family:
宋体"}[[加号"]{style="font-family:
宋体"}]{.ItemStepChar}[[+]{lang="EN-US"}]{.ItemStepChar}[["]{style="font-family:宋体"}]{.ItemStepChar}[。各符号的含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?1629595628#_Ref354745785)[所示。]{style="font-family:宋体"}

[**[number-type]{lang="EN-US"}**]{#struct_0_59978_43282_x3850559}[：号码类型。]{style="font-family:宋体"}

[*[input-number-type]{lang="EN-US"}*]{#struct_0_59978_43282_x193090256}[：输入号码的号码类型。取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-6]{lang="EN-US"}](?1629595628#_Ref154835875)[。]{style="font-family:
宋体"}

[]{#struct_0_59978_43282_x545839812}[[表1-6 ]{lang="EN-US"}[输入号码的号码类型]{style="font-family:
黑体"}]{#_Ref154835875}

[]{#table_struct_0_451115322}[[号码类型]{style="font-family:黑体"}]{#struct_0_59978_43282_1267804997}

[[描述]{style="font-family:黑体"}]{#struct_0_59978_43282_1568810295}

[[abbreviated]{lang="EN-US"}]{#struct_0_59978_43282_x875277620}

[[缩位号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991187240}

[[any]{lang="EN-US"}]{#struct_0_59978_43282_x1300568711}

[[任意]{style="font-family:宋体"}]{#struct_0_59978_43282_x1254418014}

[[international]{lang="EN-US"}]{#struct_0_59978_43282_x275963125}

[[国际号码]{style="font-family:宋体"}]{#struct_0_59978_43282_1473935229}

[[national]{lang="EN-US"}]{#struct_0_59978_43282_x113536593}

[[同一国家但不在本地网络的号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991121704}

[[network]{lang="EN-US"}]{#struct_0_59978_43282_x446217492}

[[特定服务网络的号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x588985956}

[[reserved]{lang="EN-US"}]{#struct_0_59978_43282_x1071477680}

[[扩展保留号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x2043719338}

[[subscriber]{lang="EN-US"}]{#struct_0_59978_43282_x119311928}

[[同一个本地网络的号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991056168}

[[unknown]{lang="EN-US"}]{#struct_0_59978_43282_1690380285}

[[未知号码类型]{style="font-family:宋体"}]{#struct_0_59978_43282_x1816700729}

[ ]{lang="EN-US"}

[*[output-number-type]{lang="EN-US"}*]{#struct_0_59978_43282_x709753845}[：输出号码的号码类型。取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-7]{lang="EN-US"}](?1629595628#_Ref154892305)[。]{style="font-family:
宋体"}

[]{#struct_0_59978_43282_x210797331}[[表1-7 ]{lang="EN-US"}[输出号码的号码类型]{style="font-family:
黑体"}]{#_Ref154892305}

[]{#table_struct_0_445374682}[[号码类型]{style="font-family:黑体"}]{#struct_0_59978_43282_986728286}

[[描述]{style="font-family:黑体"}]{#struct_0_59978_43282_x1990990632}

[[abbreviated]{lang="EN-US"}]{#struct_0_59978_43282_1029349267}

[[缩位号码]{style="font-family:宋体"}]{#struct_0_59978_43282_521031028}

[[international]{lang="EN-US"}]{#struct_0_59978_43282_232453180}

[[国际号码]{style="font-family:宋体"}]{#struct_0_59978_43282_545168413}

[[national]{lang="EN-US"}]{#struct_0_59978_43282_302662244}

[[同一国家但不在本地网络的号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991973672}

[[network]{lang="EN-US"}]{#struct_0_59978_43282_1453464914}

[[特定服务网络的号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x933866976}

[[reserved]{lang="EN-US"}]{#struct_0_59978_43282_1073871326}

[[扩展保留号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x206979226}

[[subscriber]{lang="EN-US"}]{#struct_0_59978_43282_x718337224}

[[同一个本地网络的号码]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991908136}

[[unknown]{lang="EN-US"}]{#struct_0_59978_43282_1181378994}

[[未知号码类型]{style="font-family:宋体"}]{#struct_0_59978_43282_x1652174154}

[ ]{lang="EN-US"}

[**[numbering-plan]{lang="EN-US"}**]{#struct_0_59978_43282_x1310729130}[：编码方案。]{style="font-family:宋体"}

[*[input-numbering-plan]{lang="EN-US"}*]{#struct_0_59978_43282_x12466955}[：输入号码的编码方案。取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-8]{lang="EN-US"}](?1629595628#_Ref154892345)[。]{style="font-family:
宋体"}

[]{#struct_0_59978_43282_1383996176}[[表1-8 ]{lang="EN-US"}[输入号码的编码方案]{style="font-family:
黑体"}]{#_Ref154892345}

[]{#table_struct_0_441567962}[[编码方案]{style="font-family:黑体"}]{#struct_0_59978_43282_1510236036}

[[描述]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991449383}

[[any]{lang="EN-US"}]{#struct_0_59978_43282_100678979}

[[任意]{style="font-family:宋体"}]{#struct_0_59978_43282_x1781711627}

[[data]{lang="EN-US"}]{#struct_0_59978_43282_2097178151}

[[数据编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_x2104711442}

[[isdn]{lang="EN-US"}]{#struct_0_59978_43282_x514019539}

[[ISDN]{lang="EN-US"}]{#struct_0_59978_43282_x1991383847}[电话编码方案]{style="font-family:宋体"}

[[national]{lang="EN-US"}]{#struct_0_59978_43282_1703648876}

[[国内编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_x1313027974}

[[private]{lang="EN-US"}]{#struct_0_59978_43282_1520867310}

[[专用编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_x2082619843}

[[reserved]{lang="EN-US"}]{#struct_0_59978_43282_1753503753}

[[扩展保留]{style="font-family:宋体"}]{#struct_0_59978_43282_x1991318311}

[[telex]{lang="EN-US"}]{#struct_0_59978_43282_x746290692}

[[用户电报编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_213061796}

[[unknown]{lang="EN-US"}]{#struct_0_59978_43282_1473686285}

[[未知编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_x534974353}

[ ]{lang="EN-US"}

[*[output-numbering-plan]{lang="EN-US"}*]{#struct_0_59978_43282_x1991252775}[：输出号码的编码方案。取值范围参见请]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-9]{lang="EN-US"}](?1629595628#_Ref154892367)[。]{style="font-family:
宋体"}

[]{#struct_0_59978_43282_399433968}[[表1-9 ]{lang="EN-US"}[输出号码的编码方案]{style="font-family:
黑体"}]{#_Ref154892367}

[]{#table_struct_0_443938618}[[编码方案]{style="font-family:黑体"}]{#struct_0_59978_43282_1436497503}

[[描述]{style="font-family:黑体"}]{#struct_0_59978_43282_186562246}

[[data]{lang="EN-US"}]{#struct_0_59978_43282_x1946075974}

[[数据编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_1167537390}

[[isdn]{lang="EN-US"}]{#struct_0_59978_43282_x815561873}

[[ISDN]{lang="EN-US"}]{#struct_0_59978_43282_x1991187239}[电话编码方案]{style="font-family:宋体"}

[[national]{lang="EN-US"}]{#struct_0_59978_43282_1784348396}

[[国内编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_x796798285}

[[private]{lang="EN-US"}]{#struct_0_59978_43282_x779648649}

[[专用编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_712334828}

[[reserved]{lang="EN-US"}]{#struct_0_59978_43282_x23675175}

[[扩展保留]{style="font-family:宋体"}]{#struct_0_59978_43282_1883926040}

[[telex]{lang="EN-US"}]{#struct_0_59978_43282_x1991121703}

[[用户电报编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_1476096809}

[[unknown]{lang="EN-US"}]{#struct_0_59978_43282_x1925254999}

[[未知编码方案]{style="font-family:宋体"}]{#struct_0_59978_43282_375108558}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_786158991}

[[对于参数]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*]{#struct_0_59978_43282_x1587869337}[和]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["分]{style="font-family:宋体"}[3]{lang="EN-US"}[种情况进行处理：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}*[output-]{lang="EN-US"}*]{#struct_0_59978_43282_x1991056167}*[template]{lang="EN-US"}*[点号无效]{lang="EN-US" style="font-family:宋体"}

[**[dot-match]{lang="EN-US"}**]{#struct_0_59978_43282_2093664812}[命令配置点号的匹配规则为]{style="font-family:宋体"}**[end-only]{lang="EN-US"}**[时，]{style="font-family:宋体"}*[output]{lang="EN-US"}*[-*template*]{lang="EN-US"}[中点号无效，只需要将]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[参数中末尾所有点号所对应的号码保留至]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中号码的末尾。]{style="font-family:宋体"}

[[例如配置如下规则：]{style="font-family:宋体"}]{#struct_0_59978_43282_852958939}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1970759311}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 1]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] dot-match end-only]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] rule 0 \^..10\...\$ \...267410.]{lang="EN-US"}

[[假设在主叫设备上进行如上配置，并对被叫号码进行变换。主叫拨打电话]{style="font-family:宋体"}[9810765]{lang="EN-US"}]{#struct_0_59978_43282_x936174796}[，匹配输入号码模板后的号码是]{style="font-family:宋体"}[765]{lang="EN-US"}[，经过号码变换后的号码为]{style="font-family:宋体"}[267410765]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[丢弃]{lang="EN-US" style="font-family:宋体"}*[output-]{lang="EN-US"}*]{#struct_0_59978_43282_x1570304099}*[template]{lang="EN-US"}*[中多余的点号]{lang="EN-US" style="font-family:宋体"}

[**[dot-match]{lang="EN-US"}**]{#struct_0_59978_43282_x733929762}[命令配置点号的匹配规则]{style="font-family:宋体"}**[right-left]{lang="EN-US"}**[或]{style="font-family:宋体"}**[left-right]{lang="EN-US"}**[，并且]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中点号位数大于]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中点号的位数时，取]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中点号对应的全部号码，按从左至右的顺序依次替换]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中的点号，]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中多余的点号会被丢弃。]{style="font-family:宋体"}

[[例如配置如下规则：]{style="font-family:宋体"}]{#struct_0_59978_43282_x1990990631}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1432633794}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 1]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] dot-match right-left]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] rule 0 \^..10..\$ ..267410\...]{lang="EN-US"}

[[假设在主叫设备上进行如上配置，并对被叫号码进行变换。主叫拨打电话]{style="font-family:宋体"}[981074]{lang="EN-US"}]{#struct_0_59978_43282_842107259}[，匹配输入号码模板后的号码是]{style="font-family:宋体"}[9874]{lang="EN-US"}[，所以经过号码变换后的号码为]{style="font-family:宋体"}[9826741074]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[丢弃]{lang="EN-US" style="font-family:宋体"}*[input-]{lang="EN-US"}*]{#struct_0_59978_43282_2028549800}*[template]{lang="EN-US"}*[中多余点号所对应的号码]{lang="EN-US" style="font-family:宋体"}

[**[dot-match]{lang="EN-US"}**]{#struct_0_59978_43282_884490485}[命令配置点号的匹配规则为]{style="font-family:宋体"}**[right-left]{lang="EN-US"}**[或]{style="font-family:宋体"}**[left-right]{lang="EN-US"}**[，并且]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中点号位数大于或等于]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中点号位数时，根据]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["的位数，从]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中点号所对应的号码中按照从右至左]{style="font-family:宋体"}[/]{lang="EN-US"}[从左至右顺序提取相应位数的号码，依次替换]{style="font-family:宋体"}*[output-template]{lang="EN-US"}*[中的点号，]{style="font-family:宋体"}*[input-template]{lang="EN-US"}*[中没有被提取的点号所对应的号码会被丢弃。]{style="font-family:宋体"}

[[例如配置如下规则：]{style="font-family:宋体"}]{#struct_0_59978_43282_364088349}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1991973671}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 1]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] dot-match right-left]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] rule 0 \^..10\...\$ ..267410..]{lang="EN-US"}

[[假设在主叫设备上进行如上配置，并对被叫号码进行变换。主叫拨打电话]{style="font-family:宋体"}[9810765]{lang="EN-US"}]{#struct_0_59978_43282_x112619027}[，匹配输入号码模板后的号码是]{style="font-family:宋体"}[8765]{lang="EN-US"}[，所以经过号码变换后的号码为]{style="font-family:宋体"}[8726741065]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1562180838}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_916248411}[创建号码变换规则表]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置号码变换规则]{style="font-family:宋体"}[0]{lang="EN-US"}[，号码变换的输入匹配模板为]{style="font-family:宋体"}[\^..01\...\$]{lang="EN-US"}[，号码变换的输出匹配模板为]{style="font-family:宋体"}[\...1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1991908135}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] number-substitute 1]{lang="EN-US"}

[\[Sysname-voice-dial-substitute1\] rule 0 \^..01\...\$ \...1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_778094467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot-match]{lang="EN-US"}**]{#struct_0_59978_43282_x1757400767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[first-rule]{lang="EN-US"}**]{#struct_0_59978_43282_1238886972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[substitute]{lang="EN-US"}**[ (Voice dial-program view)]{lang="EN-US"}]{#struct_0_59978_43282_127937250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[substitute ]{lang="EN-US"}**[(Voice entity view/Voice subscriber-line view)]{lang="EN-US"}]{#struct_0_59978_43282_8396384}

::: {#-139110481 .myid}
[]{#_Toc404794406}[]{#struct_0_59978_43282_1146887206}[]{#_Toc205711306}[]{#_Toc136850867}[]{#_Toc129160914}[]{#_Toc47776215}[]{#_Toc345522990}[]{#_Toc345522991}[]{#_Toc345522992}[]{#_Toc345522993}[]{#_Toc345522994}[]{#_Toc345522995}[]{#_Toc345522996}[]{#_Toc345522997}[]{#_Toc345522998}[]{#_Toc345522999}[]{#_Toc345523000}[]{#_Toc345523001}[]{#_Toc345523002}[]{#_Toc345523003}[]{#_Toc345523024}[]{#_Toc345523025}[]{#_Toc345523026}[]{#_Toc345523027}[]{#_Toc345523028}[]{#_Toc345523029}[]{#_Toc345523030}[]{#_Toc345523031}[]{#_Toc345523032}[]{#_Toc345523033}[]{#_Toc345523034}[]{#_Toc345523035}[]{#_Toc345523036}[]{#_Toc345523037}[]{#_Toc345523038}[]{#_Toc345523039}[]{#_Toc345523040}[]{#_Toc345523041}[]{#_Toc345523042}[]{#_Toc345523043}[]{#_Toc345523044}[]{#_Toc345523045}[]{#_Toc345523046}[]{#_Toc345523047}[]{#_Toc345523048}[]{#_Toc345523049}[]{#_Toc345523050}[]{#_Toc345523051}[]{#_Toc345523052}[]{#_Toc345523053}[]{#_Toc345523054}[]{#_Toc345523055}[]{#_Toc345523056}[]{#_Toc345523057}[]{#_Toc345523058}[]{#_Toc345523059}[]{#_Toc345523060}[]{#_Toc345523061}[]{#_Toc345523062}[]{#_Toc345523063}[]{#_Toc345523064}[]{#_Toc345523065}[]{#_Toc345523066}[]{#_Toc345523067}[]{#_Toc345523068}[]{#_Toc345523069}[]{#_Toc345523070}[]{#_Toc345523071}[]{#_Toc345523072}[]{#_Toc345523073}[]{#_Toc345523074}[]{#_Toc345523075}[]{#_Toc345523091}[]{#_Toc345523092}[]{#_Toc345523093}[]{#_Toc345523094}[]{#_Toc345523095}[]{#_Toc345523096}[]{#_Toc345523097}[]{#_Toc345523098}[]{#_Toc345523099}[]{#_Toc345523100}[]{#_Toc345523101}[]{#_Toc345523102}[]{#_Toc345523103}[]{#_Toc345523104}[]{#_Toc345523105}[]{#_Toc345523106}[]{#_Toc345523107}[]{#_Toc345523108}[]{#_Toc345523109}[]{#_Toc345523110}[]{#_Toc345523111}[]{#_Toc345523112}[]{#_Toc345523113}[]{#_Toc345523114}[]{#_Toc345523115}[]{#_Toc345523116}[]{#_Toc345523117}[]{#_Toc345523118}[]{#_Toc345523119}[]{#_Toc345523120}[]{#_Toc345523121}[]{#_Toc345523122}[]{#_Toc345523123}

**拨号策略 \-- 拨号策略配置命令 \-- send-number**

------------------------------------------------------------------------

[**[send-number]{lang="EN-US"}**]{#struct_0_59978_43282_x910885945}[命令用来配置发送号码的控制方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **send-number**]{lang="EN-US"}]{#struct_0_59978_43282_1467822318}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991449386}

[**[send-number]{lang="EN-US"}**[ { *digit-number* \| **all** \| **truncate** }]{lang="EN-US"}]{#struct_0_59978_43282_x302605548}

[**[undo]{lang="EN-US"}**[ **send-number**]{lang="EN-US"}]{#struct_0_59978_43282_1702770863}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_1832788866}

[[采用]{style="font-family:宋体"}**[truncate]{lang="EN-US"}**]{#struct_0_59978_43282_83736984}[方式发送号码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_958038329}

[[POTS]{lang="EN-US"}]{#struct_0_59978_43282_x1618140920}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_1265167148}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x635730962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_1796924087}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991383850}

[*[digit-number]{lang="EN-US"}*]{#struct_0_59978_43282_x1831869069}[：号码发送的长度（从号码末尾依次向前提取），取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。数值不大于被叫号码的位数。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_453382971}[：发送全部被叫号码。]{style="font-family:宋体"}

[**[truncate]{lang="EN-US"}**]{#struct_0_59978_43282_999894763}[：按号码截断方式发送被叫号码，即当]{style="font-family:宋体"}**[match-template]{lang="EN-US"}**[命令配置的号码中包含点号"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["时，仅发送与号码模板末尾的点号匹配的号码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2013729736}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x1991318314}[配置发送全部被叫号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x343006165}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] send-number all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1942596410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[match-template]{lang="EN-US"}**]{#struct_0_59978_43282_996193949}
:::

::: {#1865013785 .myid}
[]{#_Toc404794407}[]{#struct_0_59978_43282_1290551929}[]{#_Toc205711307}[]{#_Toc176074740}

**拨号策略 \-- 拨号策略配置命令 \-- subscriber-group**

------------------------------------------------------------------------

[**[subscriber-group]{lang="EN-US"}**]{#struct_0_59978_43282_1240327021}[命令用来创建一个用户组，并进入用户组视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **subscriber-group**]{lang="EN-US"}]{#struct_0_59978_43282_x2008089356}[命令用来删除用户组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1668614726}

[**[subscriber-group]{lang="EN-US"}**[ *group-id*]{lang="EN-US"}]{#struct_0_59978_43282_x1991252778}

[**[undo]{lang="EN-US"}**[ **subscriber-group** { *group-id* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_1158948855}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1032730425}

[[没有创建任何用户组。]{style="font-family:宋体"}]{#struct_0_59978_43282_x943235359}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2083540266}

[[语音拨号视图]{style="font-family:宋体"}]{#struct_0_59978_43282_1601010114}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_1764369386}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1480514647}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x6600795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991187242}

[*[group-id]{lang="EN-US"}*]{#struct_0_59978_43282_1831599171}[：用户组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_1363035312}[：所有用户组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_1629788882}

[[在设备上最多可以创建]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_59978_43282_x1503405986}[个用户组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x197153416}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_18794450}[创建一个用户组，并进入用户组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1306166039}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] subscriber-group 1]{lang="EN-US"}

[\[Sysname-voice-dial-group1\]]{lang="EN-US"}
:::

::: {#-250864321 .myid}
[]{#_Toc404794408}[]{#struct_0_59978_43282_x1991121706}[]{#_Toc205711308}[]{#_Toc136850868}[]{#_Toc129160915}[]{#_Toc47776221}

**拨号策略 \-- 拨号策略配置命令 \-- substitute (Voice entity view/Voice subscriber-line view)**

------------------------------------------------------------------------

[**[substitute]{lang="EN-US"}**]{#struct_0_59978_43282_716581922}[命令用来将号码变换规则表绑定到指定语音实体或语音用户线。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **substitute**]{lang="EN-US"}]{#struct_0_59978_43282_x1827927281}[命令用来取消绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_194746575}

[**[substitute]{lang="EN-US"}**[ { **called** \| **calling** } *list-number*]{lang="EN-US"}]{#struct_0_59978_43282_1974330748}

[**[undo]{lang="EN-US"}**[ **substitute** { **called** \| **calling** }]{lang="EN-US"}]{#struct_0_59978_43282_x834325210}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_361012012}

[[没有绑定号码变换规则表，即不进行号码变换。]{style="font-family:宋体"}]{#struct_0_59978_43282_x1624834943}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x2098555694}

[[POTS/VoIP/IVR]{lang="EN-US"}]{#struct_0_59978_43282_x1991056170}[语音实体视图]{style="font-family:宋体"}[/]{lang="EN-US"}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_1334215461}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_657968728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1571857062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_836193877}

[**[called]{lang="EN-US"}**]{#struct_0_59978_43282_247187881}[：对被叫号码应用号码变换。]{style="font-family:宋体"}

[**[calling]{lang="EN-US"}**]{#struct_0_59978_43282_x1472167257}[：对主叫号码应用号码变换。]{style="font-family:宋体"}

[*[list-number]{lang="EN-US"}*]{#struct_0_59978_43282_786336633}[：绑定的号码变换规则表的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_912389510}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x1943735137}[配置将号码变换规则表]{style="font-family:宋体"}[6]{lang="EN-US"}[绑定到语音实体]{style="font-family:宋体"}[10]{lang="EN-US"}[，表示对被叫号码应用号码变换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x1990990634}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] substitute called 6]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_1374975099}[配置将号码变换规则表]{style="font-family:宋体"}[6]{lang="EN-US"}[绑定到语音用户线]{style="font-family:宋体"}[2/1/1]{lang="EN-US"}[，表示对被叫号码应用号码变换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_1374844027}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] subscriber-line2/1/1]{lang="EN-US"}

[\[Sysname-voice-line2/1/1\] substitute called 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1835918321}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[number-substitute]{lang="EN-US"}**]{#struct_0_59978_43282_697546954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_59978_43282_1151466895}
:::

::: {#800566533 .myid}
[]{#_Toc404794409}[]{#struct_0_59978_43282_41314546}[]{#_Toc205711309}[]{#_Toc136850869}[]{#_Toc129160916}[]{#_Toc47776222}

**拨号策略 \-- 拨号策略配置命令 \-- substitute (Voice dial-program view)**

------------------------------------------------------------------------

[**[substitute]{lang="EN-US"}**]{#struct_0_59978_43282_x1856884141}[命令用来将号码变换规则表绑定到入局]{style="font-family:宋体"}[/]{lang="EN-US"}[出局呼叫的主]{style="font-family:宋体"}[/]{lang="EN-US"}[被叫号码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **substitute**]{lang="EN-US"}]{#struct_0_59978_43282_324323034}[命令用来取消绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1376271118}

[**[substitute]{lang="EN-US"}**[ { **incoming-call** \| **outgoing-call** } { **called** \| **calling** } *list-number*]{lang="EN-US"}]{#struct_0_59978_43282_x1991973674}

[**[undo]{lang="EN-US"}**[ **substitute** { **incoming-call** \| **outgoing-call** } { **called** \| **calling** } { *list-number* \| **all** }]{lang="EN-US"}]{#struct_0_59978_43282_290665500}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_1295408818}

[[没有绑定号码变换规则表，即不进行号码变换。]{style="font-family:宋体"}]{#struct_0_59978_43282_x1691503792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x472915721}

[[语音拨号策略视图]{style="font-family:宋体"}]{#struct_0_59978_43282_1444896947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_736986928}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x1098314999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_755492684}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991908138}

[**[incoming-call]{lang="EN-US"}**]{#struct_0_59978_43282_18579580}[：将号码变换规则表绑定到入局呼叫。]{style="font-family:宋体"}

[**[outgoing-call]{lang="EN-US"}**]{#struct_0_59978_43282_1749989925}[：将号码变换规则表绑定到出局呼叫。]{style="font-family:宋体"}

[**[called]{lang="EN-US"}**]{#struct_0_59978_43282_x1564713949}[：对被叫号码应用号码变换。]{style="font-family:宋体"}

[**[calling]{lang="EN-US"}**]{#struct_0_59978_43282_x1923078204}[：对主叫号码应用号码变换。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_59978_43282_x1633864634}[：所有的号码变换规则表。]{style="font-family:宋体"}

[*[list-number]{lang="EN-US"}*]{#struct_0_59978_43282_x1306622264}[：绑定的号码变换规则表的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_1280415878}

[[最多可以绑定]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_59978_43282_1093647858}[个号码变换规则表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991449385}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x705890075}[配置将号码变换规则表]{style="font-family:宋体"}[5]{lang="EN-US"}[绑定到入局呼叫的被叫号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_147255780}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\]]{lang="EN-US"}[ substitute incoming-call called 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_x868320405}[配置将号码变换规则表]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[、]{style="font-family:
宋体"}[8]{lang="EN-US"}[绑定到出局呼叫的被叫号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_x264363805}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\]]{lang="EN-US"}[ substitute outgoing-call called 5]{lang="EN-US"}

[\[Sysname-voice-dial\]]{lang="EN-US"}[ substitute outgoing-call called 6]{lang="EN-US"}

[\[Sysname-voice-dial\]]{lang="EN-US"}[ substitute outgoing-call called 8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1358069428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[number-substitute]{lang="EN-US"}**]{#struct_0_59978_43282_x1890757296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_59978_43282_x1991383849}
:::

::: {#-1290659308 .myid}
[]{#_Toc404794410}[]{#struct_0_59978_43282_1253310182}[]{#_Toc205711310}[]{#_Toc135295510}[]{#_Toc132701235}[]{#_Toc130097158}[]{#_Toc129160879}[]{#_Toc47776224}

**拨号策略 \-- 拨号策略配置命令 \-- terminator**

------------------------------------------------------------------------

[**[terminator]{lang="EN-US"}**]{#struct_0_59978_43282_x1237899988}[命令用来配置拨号终结符。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **terminator**]{lang="EN-US"}]{#struct_0_59978_43282_940387712}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_59978_43282_1777246285}

[**[terminator]{lang="EN-US"}**[ *character*]{lang="EN-US"}]{#struct_0_59978_43282_x336334622}

[**[undo]{lang="EN-US"}**[ **terminator**]{lang="EN-US"}]{#struct_0_59978_43282_x262139960}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_59978_43282_1916858494}

[[没有配置拨号终结符。]{style="font-family:宋体"}]{#struct_0_59978_43282_x1331320580}

[[【视图】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1991318313}

[[语音拨号策略视图]{style="font-family:宋体"}]{#struct_0_59978_43282_416508722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_59978_43282_2001563396}

[[network-admin]{lang="EN-US"}]{#struct_0_59978_43282_x164781336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_59978_43282_x693594619}

[[【参数】]{style="font-family:黑体"}]{#struct_0_59978_43282_x1963394960}

[*[character]{lang="EN-US"}*]{#struct_0_59978_43282_x577688698}[：拨号终结符，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、"]{style="font-family:宋体"}[\#]{lang="EN-US"}["、"＊"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_59978_43282_x523739663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[拨号终结符用来表示拨号已经结束，设备接收到这个符号就会根据所拨的号码发起呼叫，即使配置使用最长号码匹配策略，也不会再等待。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_59978_43282_x1991252777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请避免将被叫号码中包含的字符或号码配置为终结符。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_59978_43282_x396926643}

[[【举例】]{style="font-family:黑体"}]{#struct_0_59978_43282_1562233382}

[[\# ]{lang="EN-US"}]{#struct_0_59978_43282_695644630}[配置拨号终结符为"]{style="font-family:宋体"}[\#]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_59978_43282_509954918}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] terminator \#]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
