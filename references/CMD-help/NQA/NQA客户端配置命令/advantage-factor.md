::: {#-884418889 .myid}
[]{#_Toc404796635}[]{#struct_0_13730_22192_1521448751}[]{#_Toc199826234}

**NQA \-- NQA客户端配置命令 \-- advantage-factor**

------------------------------------------------------------------------

[**[advantage-factor]{lang="EN-US"}**]{#struct_0_13730_22192_1778836695}[命]{style="font-family:宋体"}[令用来配置用于计算]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值和]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值的补偿因子。]{style="font-family:宋体"}

[**[undo advantage-factor]{lang="EN-US"}**]{#struct_0_13730_22192_x1289097303}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1684871503}

[**[advantage-factor ]{lang="EN-US"}***[factor ]{lang="EN-US"}*]{#struct_0_13730_22192_x1707400870}

[**[undo advantage-factor]{lang="EN-US"}**]{#struct_0_13730_22192_1805702011}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_106707540}

[[补偿因子取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13730_22192_175807187}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x260525956}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_38103089}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1778377943}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_990346292}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_55007194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1357458723}

[*[factor]{lang="EN-US"}*]{#struct_0_13730_22192_x1698641561}[：用于计算]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值和]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值的补偿因子，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1969714821}

[[用户对语音质量的评价具有一定的主观性，不同用户对语音质量的容忍程度不同，因此，衡量语音质量时，需要考虑用户的主观因素。对语音质量容忍程度较强的用户，可以通过]{style="font-family:宋体"}**[advantage-factor]{lang="EN-US"}**]{#struct_0_13730_22192_640624089}[命令配置补偿因子，在计算]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值时将减去该补偿因子，修正]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[和]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值，以便在比较语音质量时综合考虑客观和主观因素。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1551432148}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x83123542}[配置语音测试的补偿因子为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1778443479}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type voice]{lang="EN-US"}

[\[Sysname-nqa-admin-test-voice\] advantage-factor 10]{lang="EN-US"}
:::

::: {#-1013057033 .myid}
[]{#_Toc404796636}[]{#struct_0_13730_22192_x1663850212}[]{#_Toc199826235}

**NQA \-- NQA客户端配置命令 \-- codec-type**

------------------------------------------------------------------------

[**[codec-type]{lang="EN-US"}**]{#struct_0_13730_22192_x1522343058}[命令用来配置语音测试的编码格式。]{style="font-family:宋体"}

[**[undo codec-type]{lang="EN-US"}**]{#struct_0_13730_22192_x989312796}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_598498140}

[**[codec-type]{lang="EN-US"}**[ { **g711a** \| **g711u** \| **g729a** }]{lang="EN-US"}]{#struct_0_13730_22192_2049038850}

[**[undo codec-type]{lang="EN-US"}**]{#struct_0_13730_22192_x1340416974}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x144441008}

[[语音编码格式为]{style="font-family:宋体"}[G.711 ]{lang="EN-US"}[A]{lang="EN-US"}]{#struct_0_13730_22192_1778509015}[律。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1884625647}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_x117326285}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1374307462}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_348197817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x184235784}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1518308167}

[**[g711a]{lang="EN-US"}**]{#struct_0_13730_22192_64268833}[：]{style="font-family:宋体"}[G.711 ]{lang="EN-US"}[A]{lang="EN-US"}[律语音编码格式。]{style="font-family:宋体"}

[**[g711u]{lang="EN-US"}**]{#struct_0_13730_22192_1881637143}[：]{style="font-family:宋体"}[G.711 µ]{lang="EN-US"}[律语音编码格式。]{style="font-family:宋体"}

[**[g729a]{lang="EN-US"}**]{#struct_0_13730_22192_1778574551}[：]{style="font-family:宋体"}[G.729 ]{lang="EN-US"}[A]{lang="EN-US"}[律语音编码格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_262276810}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1716505623}[配置]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的语音编码格式为]{style="font-family:宋体"}[G.729 A]{lang="EN-US"}[律。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1667785300}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type voice]{lang="EN-US"}

[\[Sysname-nqa-admin-test-voice\] codec-type g729a]{lang="EN-US"}
:::

::: {#27082221 .myid}
[]{#_Toc404796637}[]{#struct_0_13730_22192_2076613233}

**NQA \-- NQA客户端配置命令 \-- data-fill**

------------------------------------------------------------------------

[**[data-fill]{lang="EN-US"}**]{#struct_0_13730_22192_x470704798}[命令用来配置发送的探测报文的填充字符串。]{style="font-family:宋体"}

[**[undo data-fill]{lang="EN-US"}**]{#struct_0_13730_22192_x1151150825}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1909694710}

[**[data-fill]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_13730_22192_1779164375}

[**[undo]{lang="EN-US"}**[ **data-fill**]{lang="EN-US"}]{#struct_0_13730_22192_1808795480}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1369926280}

[[探测报文的填充内容为十六进制数值]{style="font-family:宋体"}[00010203040506070809]{lang="EN-US"}]{#struct_0_13730_22192_11931215}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x347024298}

[[ICMP-echo/Path-jitter/UDP-echo/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_1707949557}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_153514885}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_132889046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1779229911}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1855265750}

[*[string]{lang="EN-US"}*]{#struct_0_13730_22192_46849615}[：探测报文的填充内容，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x628434012}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果探测报文的数据段长度比配置的填充数据长度小，系统在报文封装时以报文的数据段长度为界截取该字符串的前一部分；]{style="font-family:宋体"}]{#struct_0_13730_22192_2117218028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果探测报文的数据段长度比配置的填充数据长度大，系统在报文封装时用该字符串进行循环填充，直到填满。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1809539784}

[[例如，配置填充数据为"]{style="font-family:宋体"}[abcd]{lang="EN-US"}]{#struct_0_13730_22192_x1827791756}["，当探测报文数据段长度为]{style="font-family:宋体"}[3]{lang="EN-US"}[字节时，则取"]{style="font-family:宋体"}[abc]{lang="EN-US"}["作为填充数据；当探测报文大小为]{style="font-family:宋体"}[6]{lang="EN-US"}[字节时，则使用"]{style="font-family:宋体"}[adcdab]{lang="EN-US"}["作为填充数据。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}]{#struct_0_13730_22192_1330512670}[测试中，配置的字符串用来填充]{lang="EN-US" style="font-family:宋体"}[ICMP Echo]{lang="EN-US"}[消息的数据字段。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_13730_22192_133103017}[UDP-echo]{lang="EN-US"}[测试中，由于]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数据字段的前]{style="font-family:宋体"}[5]{lang="EN-US"}[个字节具有特定用途，所以只用所配置的字符串填充报文中剩余的字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_13730_22192_x950243265}[UDP-jitter]{lang="EN-US"}[测试中，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数据字段的前]{style="font-family:宋体"}[68]{lang="EN-US"}[个字节具有特定用途，所以只用所配置的字符串填充报文中剩余的字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_13730_22192_493720592}[Voice]{lang="EN-US"}[测试中，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数据字段的前]{style="font-family:宋体"}[16]{lang="EN-US"}[个字节具有特定用途，所以只用所配置的字符串填充报文中剩余的字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_13730_22192_783530325}[Path-jitter]{lang="EN-US"}[测试中，由于]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[探测阶段]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数据字段的前]{style="font-family:宋体"}[4]{lang="EN-US"}[个字节具有特定用途，所以只用所配置的字符串填充]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文中剩余的字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1110601684}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_968069200}[配置]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文的填充字符串为]{style="font-family:宋体"}[abcd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_399485857}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] data-fill abcd]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1716540956}[在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测报文的填充字符串为]{style="font-family:宋体"}[abcd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x950177729}

[\[Sysname\] nqa template tcp tcptplt]{lang="EN-US"}

[\[Sysname-nqatplt-tcp-tcptplt\] data-fill abcd]{lang="EN-US"}
:::

::: {#-1912717852 .myid}
[]{#_Toc404796638}[]{#struct_0_13730_22192_x251936313}

**NQA \-- NQA客户端配置命令 \-- data-size**

------------------------------------------------------------------------

[**[data-size]{lang="EN-US"}**]{#struct_0_13730_22192_x312133811}[命令用来配置发送的探测报文中的填充内容的大小。]{style="font-family:宋体"}

[**[undo data-size]{lang="EN-US"}**]{#struct_0_13730_22192_x463047606}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1687310493}

[**[data-size]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_13730_22192_x1893828725}

[**[undo]{lang="EN-US"}**[ **data-size**]{lang="EN-US"}]{#struct_0_13730_22192_178940604}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_420896799}

[[缺省情况如]{style="font-family:宋体"}]{#struct_0_13730_22192_x950112193}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-1912717852#_Ref337469088)[所示。]{style="font-family:宋体"}

[]{#struct_0_13730_22192_1657473225}[[表1-1 ]{lang="EN-US"}[探测报文中的填充内容大小的缺省值]{style="font-family:
黑体"}]{#_Ref337469088}

[]{#table_struct_0_240780895}[[测试类型]{style="font-family:黑体"}]{#struct_0_13730_22192_1384695485}
:::

[[编码类型]{style="font-family:黑体"}]{#struct_0_13730_22192_x600850881}

[[缺省值（字节）]{style="font-family:黑体"}]{#struct_0_13730_22192_1798631917}

[[ICMP-echo]{lang="EN-US"}]{#struct_0_13730_22192_909960144}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_2001469812}

[[100]{lang="EN-US"}]{#struct_0_13730_22192_1781477729}

[[UDP-echo]{lang="EN-US"}]{#struct_0_13730_22192_x950046657}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_132199934}

[[100]{lang="EN-US"}]{#struct_0_13730_22192_709905456}

[[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_415830421}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1325580926}

[[100]{lang="EN-US"}]{#struct_0_13730_22192_1544121192}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_802476136}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_81904123}

[[100]{lang="EN-US"}]{#struct_0_13730_22192_x597598081}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x950505409}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1044075677}

[[100]{lang="EN-US"}]{#struct_0_13730_22192_x502919801}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_776407865}

[[G.711 A]{lang="EN-US"}]{#struct_0_13730_22192_x1487039118}[律]{style="font-family:宋体"}

[[172]{lang="EN-US"}]{#struct_0_13730_22192_x950439873}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_878650059}

[[G.711 µ]{lang="EN-US"}]{#struct_0_13730_22192_979341486}[律]{style="font-family:宋体"}

[[172]{lang="EN-US"}]{#struct_0_13730_22192_222513210}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_x823455692}

[[G.729 A]{lang="EN-US"}]{#struct_0_13730_22192_x950374337}[律]{style="font-family:宋体"}

[[32]{lang="EN-US"}]{#struct_0_13730_22192_109584319}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1609827877}

[[ICMP-echo/Path-jitter/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1788052153}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_2074285063}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_26314255}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1277017594}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950308801}

[*[size]{lang="EN-US"}*]{#struct_0_13730_22192_x693528832}[：探测报文中的填充内容的大小，单位为字节，]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-echo]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试类型取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[和]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试类型取值范围为]{style="font-family:宋体"}[68]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试类型取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_2054914350}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_358106326}[ICMP-echo]{lang="EN-US"}[和]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试，探测报文中填充内容的大小为]{style="font-family:宋体"}[ICMP Echo]{lang="EN-US"}[消息中数据字段的长度。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_x39191986}[UDP-echo]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试，探测报文中填充内容的大小为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文中数据字段的长度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x875557615}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x663860888}[配置发送的]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文中的填充内容的大小为]{style="font-family:宋体"}[80]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_2009211343}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] data-size 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x949718977}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置发送的]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文中的填充内容的大小为]{style="font-family:宋体"}[80]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_910276168}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] data-size 80]{lang="EN-US"}

::: {#-1419093612 .myid}
[]{#_Toc404796639}[]{#struct_0_13730_22192_1851635252}

**NQA \-- NQA客户端配置命令 \-- description (any NQA test type view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_13730_22192_1098046915}[命令用来对测试组进行简要描述，通常用于描述一个测试组的测试类型或测试目的。]{style="font-family:宋体"}**[undo description]{lang="EN-US"}**[命令用来删除已配置的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1146044898}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_13730_22192_x84643487}

[**[undo description]{lang="EN-US"}**]{#struct_0_13730_22192_629685991}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1687888574}

[[未配置描述字符串。]{style="font-family:宋体"}]{#struct_0_13730_22192_x949653441}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2137154311}

[[任意测试类型视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x723685014}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x881476241}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_533933604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1136663304}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2074375820}

[*[text]{lang="EN-US"}*]{#struct_0_13730_22192_2061062631}[：测试组的描述，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950243264}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_493655056}[配置测试组的描述字符串为]{style="font-family:宋体"}[icmp-probe]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_365887553}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] description icmp-probe]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1993528350}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置描述字符串为]{style="font-family:宋体"}[icmp-probe]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1577300783}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] description icmp-probe]{lang="EN-US"}
:::

::: {#-1281268123 .myid}
[]{#_Toc404796640}[]{#struct_0_13730_22192_1812870433}

**NQA \-- NQA客户端配置命令 \-- destination ip**

------------------------------------------------------------------------

[**[destination ip]{lang="EN-US"}**]{#struct_0_13730_22192_752485406}[命令用来配置测试操作中探测报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo destination ip]{lang="EN-US"}**]{#struct_0_13730_22192_x950177728}[命令用来删除已配置的探测报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x251870777}

[**[destination]{lang="EN-US"}**[ **ip** *ip-address*]{lang="EN-US"}]{#struct_0_13730_22192_x1891765494}

[**[undo]{lang="EN-US"}**[ **destination** **ip**]{lang="EN-US"}]{#struct_0_13730_22192_x560244162}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1509887225}

[[未配置测试操作中探测报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_x1491466756}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x461146933}

[[DHCP/DLSw/DNS/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1265050526}[测试类型视图]{style="font-family:宋体"}

[[DNS/ICMP/RADIUS/TCP/UDP]{lang="EN-US"}]{#struct_0_13730_22192_176965475}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950112192}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1657538761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1774073533}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x516714854}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13730_22192_1856218414}[：测试操作中探测报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1675310550}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x577737231}[配置]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[测试操作中探测报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x950046656}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] destination ip 10.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_132134398}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试操作中探测报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x367095348}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] destination ip 10.1.1.1]{lang="EN-US"}
:::

::: {#1944169410 .myid}
[]{#_Toc404796641}[]{#struct_0_13730_22192_x2141165725}[]{#_Toc330975603}

**NQA \-- NQA客户端配置命令 \-- destination ipv6**

------------------------------------------------------------------------

[**[destination ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_66321827}[命令用来配置测试操作中探测报文的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo destination ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_x847843922}[命令用来删除已配置的探测报文的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1722785081}

[**[destination]{lang="EN-US"}**[ **ipv6** *ipv6-address*]{lang="EN-US"}]{#struct_0_13730_22192_x777333323}

[**[undo]{lang="EN-US"}**[ **destination** **ipv6**]{lang="EN-US"}]{#struct_0_13730_22192_858158806}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950505408}

[[未配置测试操作中探测报文的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13730_22192_x1044141213}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_2136552220}

[[DNS/ICMP/RADIUS/TCP/UDP]{lang="EN-US"}]{#struct_0_13730_22192_x1695092239}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1096363286}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x888474841}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x833808550}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_805668842}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13730_22192_2097668914}[：测试操作中探测报文的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950439872}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_878715595}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试操作中探测报文的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1400580059}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] destination ipv6 1::1]{lang="EN-US"}
:::

::: {#-647308977 .myid}
[]{#_Toc404796642}[]{#struct_0_13730_22192_x1077090992}[]{#_Toc338259659}

**NQA \-- NQA客户端配置命令 \-- destination port**

------------------------------------------------------------------------

[**[destination port]{lang="EN-US"}**]{#struct_0_13730_22192_x688088905}[命令用来配置测试操作的目的端口号。]{style="font-family:宋体"}

[**[undo destination port]{lang="EN-US"}**]{#struct_0_13730_22192_x2120114387}[命令用来删除已配置的目的端口号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x353736897}

[**[destination]{lang="FR"}**]{#struct_0_13730_22192_159463187}[ **port** *port-number*]{lang="FR"}

[**[undo]{lang="FR"}**]{#struct_0_13730_22192_x950374336}[ **destination** **port**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_109649855}

[[对于]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_x1745046708}[测试，目的端口号缺省为]{style="font-family:宋体"}[33434]{lang="EN-US"}[；对于其他类型测试，未配置测试操作的目的端口号。]{style="font-family:宋体"}

[[对于各类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1454599391}[模板，各种操作类型的端口号缺省为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[（]{style="font-family:宋体"}[80]{lang="EN-US"}[）、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[（]{style="font-family:宋体"}[21]{lang="EN-US"}[）、]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[（]{style="font-family:宋体"}[1812]{lang="EN-US"}[）；对于其他模板类型，未配置测试操作的目的端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1811894808}

[[TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="FR"}]{#struct_0_13730_22192_x1437608311}[测试类型视图]{style="font-family:宋体"}

[[DNS/RADIUS/TCP/UDP]{lang="FR"}]{#struct_0_13730_22192_1147619210}[类型的]{style="font-family:宋体"}[NQA]{lang="FR"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1331077882}

[[network-admin]{lang="FR"}]{#struct_0_13730_22192_x670716578}

[[mdc-admin]{lang="FR"}]{#struct_0_13730_22192_249216580}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950308800}

[*[port-number]{lang="FR"}*]{#struct_0_13730_22192_x693594368}[：]{style="font-family:宋体"}[测试操作的目的端口号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x771819401}

[[\# ]{lang="FR"}]{#struct_0_13730_22192_496298383}[配置测试操作的目的端口号为]{style="font-family:宋体"}[9000]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1543805778}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-echo\] destination port 9000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x2106071805}[在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试操作的目的端口号为]{style="font-family:宋体"}[9000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x949718976}

[\[Sysname\] nqa template tcp tcptplt]{lang="EN-US"}

[\[Sysname-nqatplt-tcp-tcptplt\] destination port 9000]{lang="EN-US"}
:::

::: {#1346694052 .myid}
[]{#_Toc404796643}[]{#struct_0_13730_22192_910341704}[]{#_Toc199826240}[]{#_Toc200180402}[]{#_Toc201634222}[]{#_Toc202085296}[]{#_Toc202085601}[]{#_Toc200180403}[]{#_Toc201634223}[]{#_Toc202085297}[]{#_Toc202085602}[]{#_Toc200180405}[]{#_Toc201634225}[]{#_Toc202085299}[]{#_Toc202085604}[]{#_Toc200180406}[]{#_Toc201634226}[]{#_Toc202085300}[]{#_Toc202085605}[]{#_Toc200180407}[]{#_Toc201634227}[]{#_Toc202085301}[]{#_Toc202085606}[]{#_Toc200180408}[]{#_Toc201634228}[]{#_Toc202085302}[]{#_Toc202085607}[]{#_Toc200180409}[]{#_Toc201634229}[]{#_Toc202085303}[]{#_Toc202085608}[]{#_Toc200180410}[]{#_Toc201634230}[]{#_Toc202085304}[]{#_Toc202085609}[]{#_Toc200180411}[]{#_Toc201634231}[]{#_Toc202085305}[]{#_Toc202085610}[]{#_Toc200180412}[]{#_Toc201634232}[]{#_Toc202085306}[]{#_Toc202085611}[]{#_Toc200180413}[]{#_Toc201634233}[]{#_Toc202085307}[]{#_Toc202085612}[]{#_Toc200180414}[]{#_Toc201634234}[]{#_Toc202085308}[]{#_Toc202085613}[]{#_Toc200180415}[]{#_Toc201634235}[]{#_Toc202085309}[]{#_Toc202085614}[]{#_Toc200180416}[]{#_Toc201634236}[]{#_Toc202085310}[]{#_Toc202085615}[]{#_Toc200180417}[]{#_Toc201634237}[]{#_Toc202085311}[]{#_Toc202085616}[]{#_Toc200180418}[]{#_Toc201634238}[]{#_Toc202085312}[]{#_Toc202085617}[]{#_Toc200180419}[]{#_Toc201634239}[]{#_Toc202085313}[]{#_Toc202085618}[]{#_Toc200180451}[]{#_Toc201634271}[]{#_Toc202085345}[]{#_Toc202085650}[]{#_Toc200180587}[]{#_Toc201634407}[]{#_Toc202085481}[]{#_Toc202085786}[]{#_Toc200180588}[]{#_Toc201634408}[]{#_Toc202085482}[]{#_Toc202085787}[]{#_Toc200180590}[]{#_Toc201634410}[]{#_Toc202085484}[]{#_Toc202085789}[]{#_Toc200180601}[]{#_Toc201634421}[]{#_Toc202085495}[]{#_Toc202085800}[]{#_Toc200180602}[]{#_Toc201634422}[]{#_Toc202085496}[]{#_Toc202085801}

**NQA \-- NQA客户端配置命令 \-- display nqa history**

------------------------------------------------------------------------

[**[display nqa history]{lang="EN-US"}**]{#struct_0_13730_22192_x112025893}[命令用来显示]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1111609471}

[**[display nqa history]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *admin-name* *operation-tag* \]]{lang="EN-US"}]{#struct_0_13730_22192_x562422974}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_356780672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x300743295}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_294223091}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_257963796}

[[network-operator]{lang="EN-US"}]{#struct_0_13730_22192_1550938068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x949653440}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13730_22192_x2137088775}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_461801815}

[*[admin-name operation-tag]{lang="EN-US"}*]{#struct_0_13730_22192_130651380}[：显示指定测试组的历史记录。如果不指定这两个参数，将显示所有测试组的历史记录。其中，]{style="font-family:
宋体"}*[admin-name]{lang="EN-US"}*[为创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写；]{style="font-family:宋体"}*[operation-tag]{lang="EN-US"}*[为测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x63197524}

[**[display nqa history]{lang="EN-US"}**]{#struct_0_13730_22192_466787308}[命令的显示信息无法反映]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[，]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的结果，如果想了解]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[，]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的结果，建议通过]{style="font-family:宋体"}**[display nqa result]{lang="EN-US"}**[命令查看最近一次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试的结果，或通过]{style="font-family:宋体"}**[display nqa statistics]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试的统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x624583895}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_802541671}[显示管理员名字为]{style="font-family:宋体"}[administrator]{lang="EN-US"}[，测试类型标签为]{style="font-family:宋体"}[tracert]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试项的历史记录。]{style="font-family:宋体"}

[[\<Sysname\> display nqa history administrator tracert]{lang="EN-US"}]{#struct_0_13730_22192_802476135}

[NQA entry (admin administrator, tag tracert) history records:]{lang="EN-US"}

[Index      TTL  Response  Hop IP          Status          Time ]{lang="EN-US"}

[1          2    328       4.1.1.1         Succeeded       2013-09-09 14:46:06.2  ]{lang="EN-US"}

[1          2    328       4.1.1.1         Succeeded       2013-09-09 14:46:05.2  ]{lang="EN-US"}

[1          2    328       4.1.1.1         Succeeded       2013-09-09 14:46:04.2  ]{lang="EN-US"}

[1          1    328       3.1.1.2         Succeeded       2013-09-09 14:46:03.2  ]{lang="EN-US"}

[1          1    328       3.1.1.1         Succeeded       2013-09-09 14:46:02.2 ]{lang="EN-US"}

[1          1    328       3.1.1.1         Succeeded       2013-09-09 14:46:01.2  ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1617977104}[查看管理员名字为]{style="font-family:宋体"}[administrator]{lang="EN-US"}[，测试操作标签为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史记录。]{style="font-family:宋体"}

[[\<Sysname\> display nqa history administrator test]{lang="EN-US"}]{#struct_0_13730_22192_x950243267}

[NQA entry (admin administrator, tag test) history records:]{lang="EN-US"}

[  Index      Response     Status           Time]{lang="EN-US"}

[  10         329          Succeeded        2011-04-29 20:54:26.5]{lang="EN-US"}

[  9          344          Succeeded        2011-04-29 20:54:26.2]{lang="EN-US"}

[  8          328          Succeeded        2011-04-29 20:54:25.8]{lang="EN-US"}

[  7          328          Succeeded        2011-04-29 20:54:25.5]{lang="EN-US"}

[  6          328          Succeeded        2011-04-29 20:54:25.1]{lang="EN-US"}

[  5          328          Succeeded        2011-04-29 20:54:24.8]{lang="EN-US"}

[  4          328          Succeeded        2011-04-29 20:54:24.5]{lang="EN-US"}

[  3          328          Succeeded        2011-04-29 20:54:24.1]{lang="EN-US"}

[  2          328          Succeeded        2011-04-29 20:54:23.8]{lang="EN-US"}

[  1          328          Succeeded        2011-04-29 20:54:23.4]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display nqa history]{lang="EN-US"}]{#struct_0_13730_22192_493589520}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_236460209}[[字段]{style="font-family:黑体"}]{#struct_0_13730_22192_1722529705}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13730_22192_x455521105}

[[Index]{lang="EN-US"}]{#struct_0_13730_22192_450723279}

[[历史记录的编号，一次]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_x950177731}[测试中的所有记录此编号一致]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_13730_22192_802410599}

[[本次探测的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_13730_22192_917237694}[值]{style="font-family:宋体"}

[[Response]{lang="EN-US"}]{#struct_0_13730_22192_x251412024}

[[测试成功时，为测试报文的往返时延；如果测试超时，则为超时时间；不能完成测试时，则为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13730_22192_x329447083}[。单位为毫秒]{style="font-family:宋体"}

[[Hop IP]{lang="EN-US"}]{#struct_0_13730_22192_802345063}

[[回复应答的节点]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_596724996}[地址]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_13730_22192_x1714910011}

[[测试结果的状态值，具体如下：]{style="font-family:宋体"}]{#struct_0_13730_22192_x2139456134}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Succeeded]{lang="EN-US"}]{#struct_0_13730_22192_296990897}[：测试成功，接收到响应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown error]{lang="EN-US"}]{#struct_0_13730_22192_x950112195}[：未知错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Internal error]{lang="EN-US"}]{#struct_0_13730_22192_1657604297}[：内部错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Timeout]{lang="EN-US"}]{#struct_0_13730_22192_x1355132309}[：请求超时]{lang="EN-US" style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_13730_22192_x1484511011}

[[测试完成时间]{style="font-family:宋体"}]{#struct_0_13730_22192_x1838653611}

[ ]{lang="EN-US"}

::: {#-625527015 .myid}
[]{#_Toc199826506}[]{#_Toc404796644}[]{#struct_0_13730_22192_778698783}[]{#_Toc250551325}[]{#_Toc199824828}[]{#_Toc199825432}[]{#_Toc199825761}[]{#_Toc199826090}[]{#_Toc199826418}[]{#_Toc199824846}[]{#_Toc199825450}[]{#_Toc199825779}[]{#_Toc199826108}[]{#_Toc199826436}[]{#_Toc199824869}[]{#_Toc199825473}[]{#_Toc199825802}[]{#_Toc199826131}[]{#_Toc199826459}[]{#_Toc199824870}[]{#_Toc199825474}[]{#_Toc199825803}[]{#_Toc199826132}[]{#_Toc199826460}[]{#_Toc199824871}[]{#_Toc199825475}[]{#_Toc199825804}[]{#_Toc199826133}[]{#_Toc199826461}[]{#_Toc199824873}[]{#_Toc199825477}[]{#_Toc199825806}[]{#_Toc199826135}[]{#_Toc199826463}[]{#_Toc199824889}[]{#_Toc199825493}[]{#_Toc199825822}[]{#_Toc199826151}[]{#_Toc199826479}[]{#_Toc199824915}[]{#_Toc199825519}[]{#_Toc199825848}[]{#_Toc199826177}[]{#_Toc199826505}

**NQA \-- NQA客户端配置命令 \-- display nqa reaction counters**

------------------------------------------------------------------------

[**[display nqa reaction counters]{lang="EN-US"}**]{#struct_0_13730_22192_x950046659}[命令用来显示阈值告警组的当前监测结果。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_132068862}

[**[display nqa reaction counters]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[admin-name]{lang="EN-US"}*[ *operation-tag* \[ *item-number* \] \]]{lang="EN-US"}]{#struct_0_13730_22192_x1991518092}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1162027058}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x1423921143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1059435048}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1585633072}

[[network-operator]{lang="EN-US"}]{#struct_0_13730_22192_102040207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_331881615}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13730_22192_x950505411}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1044599964}

[*[admin-name operation-tag]{lang="EN-US"}*]{#struct_0_13730_22192_288504513}[：显示指定测试组中阈值告警组的当前监测结果。如果不指定这两个参数，将显示所有测试组中所有阈值告警组的当前监测结果。其中，]{style="font-family:
宋体"}*[admin-name]{lang="EN-US"}*[为创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写；]{style="font-family:宋体"}*[operation-tag]{lang="EN-US"}*[为测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x2055818757}[：显示指定阈值告警组的当前监测结果。如果不指定该参数，将显示所有阈值告警组的当前监测结果。]{style="font-family:宋体"}*[item-number]{lang="EN-US"}*[为阈值告警组的编号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_556405136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_13730_22192_x958548128}[NQA]{lang="EN-US"}[阈值告警组的阈值类型为平均值，或监测对象为]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[或]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值，则显示的监测结果为无效值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[测试结束后，不会清除监测结果，即测试组启动后，监测结果会不断累加。]{style="font-family:宋体"}]{#struct_0_13730_22192_273782592}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x150749144}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x950439875}[显示]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[测试组]{style="font-family:宋体"}[admin test]{lang="EN-US"}[的所有阈值告警组的当前监测结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa reaction counters admin test]{lang="EN-US"}]{#struct_0_13730_22192_879043275}

[NQA entry (admin admin, tag test) reaction counters:]{lang="EN-US"}

[  Index  Checked Element  Threshold Type  Checked Num  Over-threshold Num]{lang="EN-US"}

[  ]{lang="EN-US"}[1      probe-duration   accumulate      12           4]{lang="FR"}

[  2      probe-duration   average         -            -]{lang="FR"}

[  ]{lang="FR"}[3      probe-duration   consecutive     160          56]{lang="EN-US"}

[  4      probe-fail       accumulate      12           0]{lang="EN-US"}

[  5      probe-fail       consecutive     162          2]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display nqa reaction counters]{lang="EN-US"}]{#struct_0_13730_22192_x1601009514}[命令显示信息描述]{style="font-family:黑体"}

[]{#table_struct_0_238492132}[[字段]{style="font-family:黑体"}]{#struct_0_13730_22192_701537435}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13730_22192_x1861567057}

[[Index]{lang="EN-US"}]{#struct_0_13730_22192_720584230}

[[阈值告警组的编号]{style="font-family:宋体"}]{#struct_0_13730_22192_x950374339}

[[Checked Element]{lang="EN-US"}]{#struct_0_13730_22192_109453247}

[[监测的对象]{style="font-family:宋体"}]{#struct_0_13730_22192_x850104625}

[[Threshold Type]{lang="EN-US"}]{#struct_0_13730_22192_1511858072}

[[阈值类型]{style="font-family:宋体"}]{#struct_0_13730_22192_1405921531}

[[Checked Num]{lang="EN-US"}]{#struct_0_13730_22192_1639159645}

[[已监测的样本个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x950308803}

[[Over-threshold Num]{lang="EN-US"}]{#struct_0_13730_22192_x693659904}

[[超出阈值的样本个数]{style="font-family:宋体"}]{#struct_0_13730_22192_1285033203}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display nqa reaction counters]{lang="EN-US"}]{#struct_0_13730_22192_841548503}[命令显示字段取值描述]{style="font-family:黑体"}

[]{#table_struct_0_265861290}[[监测对象]{style="font-family:黑体"}]{#struct_0_13730_22192_1368882202}

[[阈值类型]{style="font-family:黑体"}]{#struct_0_13730_22192_419773434}

[[监测的样本范围]{style="font-family:黑体"}]{#struct_0_13730_22192_x949718979}

[[Checked Num]{lang="EN-US"}]{#struct_0_13730_22192_910407240}[取值]{style="font-family:黑体"}

[[Over-threshold Num]{lang="EN-US"}]{#struct_0_13730_22192_x627419076}[取值]{style="font-family:黑体"}

[[probe-duration]{lang="EN-US"}]{#struct_0_13730_22192_x880928047}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_2143985779}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1837836236}[测试组后进行的探测]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x949653443}[测试组后已完成的探测次数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x2137023239}[测试组后探测持续时间不在阈值范围内的探测次数]{style="font-family:宋体"}

[[average]{lang="EN-US"}]{#struct_0_13730_22192_x409423664}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1761313587}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_846918031}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1469223565}

[[consecutive]{lang="EN-US"}]{#struct_0_13730_22192_x950243266}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_493523984}[测试组后进行的探测]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1815269221}[测试组后已完成的探测次数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_584431733}[测试组后探测持续时间不在阈值范围内的探测次数]{style="font-family:宋体"}

[[probe-fail]{lang="EN-US"}]{#struct_0_13730_22192_1123019761}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_x950177730}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x251346488}[测试组后进行的探测]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_868890254}[测试组后已完成的探测次数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x904943377}[测试组后失败的探测次数]{style="font-family:宋体"}

[[consecutive]{lang="EN-US"}]{#struct_0_13730_22192_x503677657}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x950112194}[测试组后进行的探测]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1657669833}[测试组后已完成的探测次数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_522474762}[测试组后失败的探测次数]{style="font-family:宋体"}

[[RTT]{lang="EN-US"}]{#struct_0_13730_22192_1501671146}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_140286014}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x950046658}[测试组后发送的报文]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_132003326}[测试组后已发送的报文个数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1975545417}[测试组后往返时间不在阈值范围内的报文个数]{style="font-family:宋体"}

[[average]{lang="EN-US"}]{#struct_0_13730_22192_x1259693187}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x950505410}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1044665500}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x843469172}

[[jitter-DS/jitter-SD]{lang="EN-US"}]{#struct_0_13730_22192_1172843206}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_x950439874}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_879108811}[测试组后发送的报文]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_778030428}[测试组后已发送的报文个数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x984076290}[测试组后单向时延抖动不在阈值范围内的报文个数]{style="font-family:宋体"}

[[average]{lang="EN-US"}]{#struct_0_13730_22192_x950374338}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_109518783}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1516424488}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x134293740}

[[OWD-DS/OWD-SD]{lang="EN-US"}]{#struct_0_13730_22192_x950308802}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x693725440}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_7046172}[测试组后发送的报文]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x949718978}[测试组后已发送的报文个数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_910472776}[测试组后单向时延不在阈值范围内的报文个数]{style="font-family:宋体"}

[[packet-loss]{lang="EN-US"}]{#struct_0_13730_22192_2099224424}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_x949653442}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x2136957703}[测试组后发送的报文]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_823417533}[测试组后已发送的报文个数]{style="font-family:宋体"}

[[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_2060511165}[测试组后的丢包数]{style="font-family:宋体"}

[[ICPIF]{lang="EN-US"}]{#struct_0_13730_22192_x950243269}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_493458448}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x243061305}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x950177733}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x251543096}

[[MOS]{lang="EN-US"}]{#struct_0_13730_22192_1229624482}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x950112197}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1657735369}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x2125668958}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x950046661}

[ ]{lang="EN-US"}

::: {#-1690229506 .myid}
[]{#_Toc404796645}[]{#struct_0_13730_22192_132593153}

**NQA \-- NQA客户端配置命令 \-- display nqa result**

------------------------------------------------------------------------

[**[display nqa result]{lang="EN-US"}**]{#struct_0_13730_22192_1284548435}[命令用来显示最近一次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试的当前结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1493904906}

[**[display nqa result ]{lang="EN-US"}**[\[ *admin-name* *operation-tag* \]]{lang="EN-US"}]{#struct_0_13730_22192_1270445897}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_2122289755}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x40288115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x950505413}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1044731036}

[[network-operator]{lang="EN-US"}]{#struct_0_13730_22192_1796068386}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1528214476}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13730_22192_1276600760}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x237161281}

[*[admin-name operation-tag]{lang="EN-US"}*]{#struct_0_13730_22192_x1194824339}[：显示指定测试组的最近一次测试的当前结果。如果不指定这两个参数，将显示所有测试组的最近一次测试的结果。其中，]{style="font-family:
宋体"}*[admin-name]{lang="EN-US"}*[为创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写；]{style="font-family:宋体"}*[operation-tag]{lang="EN-US"}*[为测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1604538196}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x950439877}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[测试的最近一次测试的当前结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_878912203}

[NQA entry (admin admin, tag test) test results:]{lang="EN-US"}

[    Send operation times: 1              Receive response times: 1 ]{lang="EN-US"}

[    Min/Max/Average round trip time: 35/35/35 ]{lang="EN-US"}

[    Square-Sum of round trip time: 1225 ]{lang="EN-US"}

[    Last succeeded probe time: 2011-05-29 10:50:33.2 ]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 0% ]{lang="EN-US"}

[    Failures due to timeout: 0]{lang="EN-US"}

[    Failures due to disconnect: 0]{lang="EN-US"}

[    Failures due to no connection: 0]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1909020698}[显示]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试的最近一次测试的当前结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_x950308805}

[NQA entry (admin admin, tag test) test results:]{lang="EN-US"}

[    Send operation times: 10             Receive response times: 10]{lang="EN-US"}

[    Min/Max/Average round trip time: 15/46/26]{lang="EN-US"}

[    Square-Sum of round trip time: 8103]{lang="EN-US"}

[    Last packet received time: 2011-05-29 10:56:38.7]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 0%]{lang="EN-US"}

[    Failures due to timeout: 0]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[    Packets out of sequence: 0]{lang="EN-US"}

[    Packets arrived late: 0]{lang="EN-US"}

[  UDP-jitter results:]{lang="EN-US"}

[   ]{lang="EN-US"}[RTT number: 10]{lang="DA"}

[    Min positive SD: 8                     Min positive DS: 8]{lang="DA"}

[    ]{lang="DA"}[Max positive SD: 18                    Max positive DS: 8]{lang="EN-US"}

[    Positive SD number: 5                  Positive DS number: 2]{lang="EN-US"}

[    Positive SD sum: 75                    Positive DS sum: 32]{lang="EN-US"}

[    Positive SD average: 15                Positive DS average: 16]{lang="EN-US"}

[    Positive SD square-sum: 1189           Positive DS square-sum: 640]{lang="EN-US"}

[    ]{lang="EN-US"}[Min negative SD: 8                     Min negative DS: 1]{lang="DA"}

[    Max negative SD: 24                    Max negative DS: 30]{lang="DA"}

[    Negative SD number: 4                  Negative DS number: 7]{lang="DA"}

[    Negative SD sum: 56                    Negative DS sum: 99]{lang="DA"}

[    Negative SD average: 14                Negative DS average: 14]{lang="DA"}

[    ]{lang="DA"}[Negative SD square-sum: 946            Negative DS square-sum: 1495]{lang="EN-US"}

[  One way results:]{lang="EN-US"}

[    Max SD delay: 22                       Max DS delay: 23]{lang="EN-US"}

[    ]{lang="EN-US"}[Min SD delay: 7                        Min DS delay: 7]{lang="DA"}

[    ]{lang="DA"}[Number of SD delay: 10                 Number of DS delay: 10]{lang="EN-US"}

[    Sum of SD delay: 125                   Sum of DS delay: 132]{lang="EN-US"}

[    Square-Sum of SD delay: 1805           Square-Sum of DS delay: 1988]{lang="EN-US"}

[    SD lost packets: 0                     DS lost packets: 0]{lang="EN-US"}

[    Lost packets for unknown reason: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x693266688}[显示]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试最近一次测试的当前结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_x949718981}

[NQA entry (admin admin, tag test) test results:]{lang="EN-US"}

[    Send operation times: 1000           Receive response times: 0]{lang="EN-US"}

[    Min/Max/Average round trip time: 0/0/0]{lang="EN-US"}

[    Square-Sum of round trip time: 0]{lang="EN-US"}

[    Last packet received time: 0-00-00 00:00:00.0]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 100%]{lang="EN-US"}

[    Failures due to timeout: 1000]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[    Packets out of sequence: 0]{lang="EN-US"}

[    Packets arrived late: 0]{lang="EN-US"}

[  Voice results:]{lang="EN-US"}

[   ]{lang="EN-US"}[RTT number: 0]{lang="DA"}

[    Min positive SD: 0                     Min positive DS: 0]{lang="DA"}

[    ]{lang="DA"}[Max positive SD: 0                     Max positive DS: 0]{lang="EN-US"}

[    Positive SD number: 0                  Positive DS number: 0]{lang="EN-US"}

[    Positive SD sum: 0                     Positive DS sum: 0]{lang="EN-US"}

[    Positive SD average: 0                 Positive DS average: 0]{lang="EN-US"}

[    Positive SD square-sum: 0              Positive DS square-sum: 0]{lang="EN-US"}

[    ]{lang="EN-US"}[Min negative SD: 0                     Min negative DS: 0]{lang="DA"}

[    Max negative SD: 0                     Max negative DS: 0]{lang="DA"}

[    Negative SD number: 0                  Negative DS number: 0]{lang="DA"}

[    Negative SD sum: 0                     Negative DS sum: 0]{lang="DA"}

[    Negative SD average: 0                 Negative DS average: 0]{lang="DA"}

[    ]{lang="DA"}[Negative SD square-sum: 0              Negative DS square-sum: 0]{lang="EN-US"}

[  One way results:]{lang="EN-US"}

[    Max SD delay: 0                        Max DS delay: 0]{lang="EN-US"}

[    ]{lang="EN-US"}[Min SD delay: 0                        Min DS delay: 0]{lang="DA"}

[    ]{lang="DA"}[Number of SD delay: 0                  Number of DS delay: 0]{lang="EN-US"}

[    Sum of SD delay: 0                     Sum of DS delay: 0]{lang="EN-US"}

[    Square-Sum of SD delay: 0              Square-Sum of DS delay: 0]{lang="EN-US"}

[    SD lost packets: 0                     DS lost packets: 0]{lang="EN-US"}

[    Lost packets for unknown reason: 1000]{lang="EN-US"}

[  Voice scores:]{lang="EN-US"}

[    MOS value: 0.99                        ICPIF value: 87]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_909882961}[显示]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试正在进行中。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_474570185}

[Data collecting in progress\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x949653445}[显示]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试没有生成结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_x2137416455}

[  Path jitter result is not available.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_2071101195}[显示]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试的最近一次测试的当前结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_x950177732}

[NQA entry (admin admin, tag test) test results:]{lang="EN-US"}

[  Hop IP 192.168.40.210]{lang="EN-US"}

[    Basic Results:]{lang="EN-US"}

[      Send operation times: 10]{lang="EN-US"}

[      Receive response times: 10]{lang="EN-US"}

[      Min/Max/Average round trip time: 1/1/1]{lang="EN-US"}

[      Square-Sum of round trip time: 10]{lang="EN-US"}

[    Extended Results:]{lang="EN-US"}

[      Packet loss ratio: 0%]{lang="EN-US"}

[      Failures due to timeout: 0]{lang="EN-US"}

[      Failures due to internal error: 0]{lang="EN-US"}

[      Failures due to other errors: 0]{lang="EN-US"}

[      Packets out of sequence: 0]{lang="EN-US"}

[      Packets arrived late: 0]{lang="EN-US"}

[    Path-Jitter Results:]{lang="EN-US"}

[      Jitter number: 9]{lang="EN-US"}

[        Min/Max/Average jitter: 0/0/0]{lang="EN-US"}

[      Positive jitter number: 0]{lang="EN-US"}

[        Min/Max/Average positive jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum positive jitter: 0/0]{lang="EN-US"}

[      Negative jitter number: 0]{lang="EN-US"}

[        Min/Max/Average negative jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum negative jitter: 0/0]{lang="EN-US"}

[  Hop IP 192.168.50.209]{lang="EN-US"}

[    Basic Results:]{lang="EN-US"}

[      Send operation times: 10]{lang="EN-US"}

[      Receive response times: 10]{lang="EN-US"}

[      Min/Max/Average round trip time: 1/1/1]{lang="EN-US"}

[      Square-Sum of round trip time: 10]{lang="EN-US"}

[    Extended Results:]{lang="EN-US"}

[      Packet loss ratio: 0%]{lang="EN-US"}

[      Failures due to timeout: 0]{lang="EN-US"}

[      Failures due to internal error: 0]{lang="EN-US"}

[      Failures due to other errors: 0]{lang="EN-US"}

[      Packets out of sequence: 0]{lang="EN-US"}

[      Packets arrived late: 0]{lang="EN-US"}

[    Path-Jitter Results:]{lang="EN-US"}

[      Jitter number: 9]{lang="EN-US"}

[        Min/Max/Average jitter: 0/0/0]{lang="EN-US"}

[      Positive jitter number: 0]{lang="EN-US"}

[        Min/Max/Average positive jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum positive jitter: 0/0]{lang="EN-US"}

[      Negative jitter number: 0]{lang="EN-US"}

[        Min/Max/Average negative jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum negative jitter: 0/0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_802738277}[显示]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试的最近一次测试的当前结果。]{style="font-family:宋体"}

[[\<Sysname\> display nqa result admin test]{lang="EN-US"}]{#struct_0_13730_22192_802672741}

[NQA entry (admin admin, tag test) test results:]{lang="EN-US"}

[    Send operation times: 6              Receive response times: 6 ]{lang="EN-US"}

[    Min/Max/Average round trip time: 35/35/35 ]{lang="EN-US"}

[    Square-Sum of round trip time: 1225 ]{lang="EN-US"}

[    Last succeeded probe time: 2013-09-09 14:23:24.5 ]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 0% ]{lang="EN-US"}

[    Failures due to timeout: 0]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[  UDP-tracert results:  ]{lang="EN-US"}

[    TTL    Hop IP             Time]{lang="EN-US"}

[    1      3.1.1.1            2013-09-09 14:23:24.5]{lang="EN-US"}

[    2      4.1.1.1            2013-09-09 14:23:24.5]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display nqa result]{lang="EN-US"}]{#struct_0_13730_22192_x251477560}[命令显示信息描述]{style="font-family:黑体"}

[]{#table_struct_0_259068138}[[字段]{style="font-family:黑体"}]{#struct_0_13730_22192_98091602}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13730_22192_1634669846}

[[Send operation times]{lang="EN-US"}]{#struct_0_13730_22192_989611281}

[[发送的探测报文数]{style="font-family:宋体"}]{#struct_0_13730_22192_1924697441}

[[Receive response times]{lang="EN-US"}]{#struct_0_13730_22192_x950112196}

[[收到的响应报文数]{style="font-family:宋体"}]{#struct_0_13730_22192_1657800905}

[[Min/Max/Average round trip time]{lang="EN-US"}]{#struct_0_13730_22192_543368200}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_x1910116845}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均往返时间，单位为毫秒]{style="font-family:宋体"}

[[Square-Sum of round trip time]{lang="EN-US"}]{#struct_0_13730_22192_x739266776}

[[往返时间平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x1879836491}

[[Last succeeded probe time]{lang="EN-US"}]{#struct_0_13730_22192_x950046660}

[[一次测试中最后一次成功探测的完成时间，如果一次测试中的探测均失败，则该时间显示为全]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13730_22192_132527617}[，]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[、]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试中无此信息]{style="font-family:宋体"}

[[Last packet received time]{lang="EN-US"}]{#struct_0_13730_22192_931810029}

[[一次探测中最后一次成功收到正确响应报文的时间，如果一次探测中没有收到过正确的响应报文，则该时间显示为全]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13730_22192_1421943575}[，]{style="font-family:宋体"}[只在]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Packet loss ratio]{lang="EN-US"}]{#struct_0_13730_22192_467964045}

[[平均丢包率]{style="font-family:宋体"}]{#struct_0_13730_22192_x950505412}

[[Failures due to timeout]{lang="EN-US"}]{#struct_0_13730_22192_x1044796572}

[[测试过程中超时的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_250291187}

[[Failures due to disconnect]{lang="EN-US"}]{#struct_0_13730_22192_421300917}

[[对方强制断开连接的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_1248075866}

[[Failures due to no connection]{lang="EN-US"}]{#struct_0_13730_22192_x950439876}

[[和对方建立连接失败的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_878977739}

[[Failures due to internal error]{lang="EN-US"}]{#struct_0_13730_22192_1178332865}

[[因内部错误失败的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x501473698}

[[Failures due to other errors]{lang="EN-US"}]{#struct_0_13730_22192_933133519}

[[因其它错误失败的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x950374340}

[[Packets out of sequence]{lang="EN-US"}]{#struct_0_13730_22192_110043072}

[[报文失序的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_435430248}

[[Packets arrived late]{lang="EN-US"}]{#struct_0_13730_22192_x24369471}

[[探测超时后，收到的响应报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x950308804}

[[UDP-jitter results]{lang="EN-US"}]{#struct_0_13730_22192_x693332224}

[[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1901249365}[测试的结果，只在]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Voice results]{lang="EN-US"}]{#struct_0_13730_22192_2076178661}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_x949718980}[测试的结果，只在]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[RTT number]{lang="EN-US"}]{#struct_0_13730_22192_909948497}

[[收到的响应报文数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1595914182}

[[Min positive SD]{lang="EN-US"}]{#struct_0_13730_22192_2017447031}

[[源到目的方向正抖动时延的最小值]{style="font-family:宋体"}]{#struct_0_13730_22192_x949653444}

[[Min positive DS]{lang="EN-US"}]{#struct_0_13730_22192_x2137350919}

[[目的到源方向正抖动时延的最小值]{style="font-family:宋体"}]{#struct_0_13730_22192_x540029800}

[[Max positive SD]{lang="EN-US"}]{#struct_0_13730_22192_x45274660}

[[源到目的方向正抖动时延的最大值]{style="font-family:宋体"}]{#struct_0_13730_22192_615840676}

[[Max positive DS]{lang="EN-US"}]{#struct_0_13730_22192_x914404500}

[[目的到源方向正抖动时延的最大值]{style="font-family:宋体"}]{#struct_0_13730_22192_x1581275895}

[[Positive SD number]{lang="EN-US"}]{#struct_0_13730_22192_1089016003}

[[源到目的方向正抖动时延的数目]{style="font-family:宋体"}]{#struct_0_13730_22192_615906212}

[[Positive DS number]{lang="EN-US"}]{#struct_0_13730_22192_x1339417000}

[[目的到源方向正抖动时延的数目]{style="font-family:宋体"}]{#struct_0_13730_22192_x2123967218}

[[Positive SD sum]{lang="EN-US"}]{#struct_0_13730_22192_615971748}

[[源到目的方向正抖动时延之和]{style="font-family:宋体"}]{#struct_0_13730_22192_x522791360}

[[Positive DS sum]{lang="EN-US"}]{#struct_0_13730_22192_78083607}

[[目的到源方向正抖动时延之和]{style="font-family:宋体"}]{#struct_0_13730_22192_616037284}

[[Positive SD average]{lang="EN-US"}]{#struct_0_13730_22192_x1978392866}

[[源到目的方向正抖动时延的平均值]{style="font-family:宋体"}]{#struct_0_13730_22192_1134653640}

[[Positive DS average]{lang="EN-US"}]{#struct_0_13730_22192_x396785296}

[[目的到源方向正抖动时延的平均值]{style="font-family:宋体"}]{#struct_0_13730_22192_615578532}

[[Positive SD square-sum]{lang="EN-US"}]{#struct_0_13730_22192_x1432633472}

[[源到目的方向正抖动时延的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x1228684460}

[[Positive DS square-sum]{lang="EN-US"}]{#struct_0_13730_22192_615644068}

[[目的到源方向正抖动时延的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_1922631440}

[[Min negative SD]{lang="EN-US"}]{#struct_0_13730_22192_1696245813}

[[源到目的方向负抖动时延的绝对值的最小值]{style="font-family:宋体"}]{#struct_0_13730_22192_615709604}

[[Min negative DS]{lang="EN-US"}]{#struct_0_13730_22192_x1939584026}

[[目的到源方向负抖动时延的绝对值的最小值]{style="font-family:宋体"}]{#struct_0_13730_22192_x195482943}

[[Max negative SD]{lang="EN-US"}]{#struct_0_13730_22192_615775140}

[[源到目的方向负抖动时延的绝对值的最大值]{style="font-family:宋体"}]{#struct_0_13730_22192_x1936092694}

[[Max negative DS]{lang="EN-US"}]{#struct_0_13730_22192_x923605733}

[[目的到源方向负抖动时延的绝对值的最大值]{style="font-family:宋体"}]{#struct_0_13730_22192_616364964}

[[Negative SD number]{lang="EN-US"}]{#struct_0_13730_22192_x2102197024}

[[源到目的方向]{style="font-family:宋体"}]{#struct_0_13730_22192_x29478211}[负抖动时延]{style="font-family:宋体"}[的数目]{style="font-family:宋体"}

[[Negative DS number]{lang="EN-US"}]{#struct_0_13730_22192_616430500}

[[目的到源方向]{style="font-family:宋体"}]{#struct_0_13730_22192_x310281045}[负抖动时延]{style="font-family:宋体"}[的数目]{style="font-family:宋体"}

[[Negative SD sum]{lang="EN-US"}]{#struct_0_13730_22192_1955093852}

[[源到目的方向]{style="font-family:宋体"}]{#struct_0_13730_22192_615840677}[负抖动时延]{style="font-family:宋体"}[的绝对值之和]{style="font-family:宋体"}

[[Negative DS sum]{lang="EN-US"}]{#struct_0_13730_22192_x914404499}

[[目的到源方向]{style="font-family:宋体"}]{#struct_0_13730_22192_615906213}[负抖动时延]{style="font-family:宋体"}[的绝对值之和]{style="font-family:宋体"}

[[Negative SD average]{lang="EN-US"}]{#struct_0_13730_22192_x1339416999}

[[源到目的方向]{style="font-family:宋体"}]{#struct_0_13730_22192_x334953132}[负抖动时延]{style="font-family:宋体"}[的绝对值的平均值]{style="font-family:宋体"}

[[Negative DS average]{lang="EN-US"}]{#struct_0_13730_22192_615971749}

[[目的到源方向]{style="font-family:宋体"}]{#struct_0_13730_22192_x522791361}[负抖动时延]{style="font-family:宋体"}[的绝对值的平均值]{style="font-family:宋体"}

[[Negative SD square-sum]{lang="EN-US"}]{#struct_0_13730_22192_616037285}

[[源到目的方向]{style="font-family:宋体"}]{#struct_0_13730_22192_x1978392867}[负抖动时延]{style="font-family:宋体"}[的平方和]{style="font-family:宋体"}

[[Negative DS square-sum]{lang="EN-US"}]{#struct_0_13730_22192_x431430301}

[[目的到源方向]{style="font-family:宋体"}]{#struct_0_13730_22192_615578533}[负抖动时延]{style="font-family:宋体"}[的平方和]{style="font-family:宋体"}

[[One way results]{lang="EN-US"}]{#struct_0_13730_22192_x1432633473}

[[单向延迟测试结果，只有]{style="font-family:宋体"}[UDP-Jitter]{lang="EN-US"}]{#struct_0_13730_22192_1500198895}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[类型测试有单向延迟测试结果]{style="font-family:宋体"}

[[Max SD delay]{lang="EN-US"}]{#struct_0_13730_22192_615644069}

[[源到目的的最大时延]{style="font-family:宋体"}]{#struct_0_13730_22192_1922631441}

[[Max DS delay]{lang="EN-US"}]{#struct_0_13730_22192_615709605}

[[目的到源的最大时延]{style="font-family:宋体"}]{#struct_0_13730_22192_x1939584025}

[[Min SD delay]{lang="EN-US"}]{#struct_0_13730_22192_615775141}

[[源到目的的最小时延]{style="font-family:宋体"}]{#struct_0_13730_22192_x1936092695}

[[Min DS delay]{lang="EN-US"}]{#struct_0_13730_22192_642478208}

[[目的到源的最小时延]{style="font-family:宋体"}]{#struct_0_13730_22192_616364965}

[[Number of SD delay]{lang="EN-US"}]{#struct_0_13730_22192_x2102197023}

[[源到目的计算的时延数]{style="font-family:宋体"}]{#struct_0_13730_22192_616430501}

[[Number of DS delay]{lang="EN-US"}]{#struct_0_13730_22192_x310281046}

[[目的到源计算的时延数]{style="font-family:宋体"}]{#struct_0_13730_22192_615840674}

[[Sum of SD delay]{lang="EN-US"}]{#struct_0_13730_22192_x914404502}

[[源到目的的时延和]{style="font-family:宋体"}]{#struct_0_13730_22192_x1581406967}

[[Sum of DS delay]{lang="EN-US"}]{#struct_0_13730_22192_615906210}

[[目的到源的时延和]{style="font-family:宋体"}]{#struct_0_13730_22192_x1339417002}

[[Square-Sum of SD delay]{lang="EN-US"}]{#struct_0_13730_22192_615971746}

[[源到目的的时延的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x522791354}

[[Square-Sum of DS delay]{lang="EN-US"}]{#struct_0_13730_22192_616037282}

[[目的到源的时延的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x1978392868}

[[SD lost packets]{lang="EN-US"}]{#struct_0_13730_22192_615578530}

[[源到目的方向丢失的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1432633474}

[[DS lost packets]{lang="EN-US"}]{#struct_0_13730_22192_615644066}

[[目的到源方向丢失的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_1922631438}

[[Lost packets for unknown reason]{lang="EN-US"}]{#struct_0_13730_22192_615709602}

[[不能确定原因丢失的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1939584020}

[[Voice scores]{lang="EN-US"}]{#struct_0_13730_22192_615775138}

[[语音参数，只在]{style="font-family:宋体"}[Voice]{lang="EN-US"}]{#struct_0_13730_22192_402559458}[类型测试有此信息]{style="font-family:宋体"}

[[MOS value]{lang="EN-US"}]{#struct_0_13730_22192_616364962}

[[为语音计算的]{style="font-family:宋体"}[MOS]{lang="EN-US"}]{#struct_0_13730_22192_x2102197022}[值]{style="font-family:宋体"}

[[ICPIF value]{lang="EN-US"}]{#struct_0_13730_22192_616430498}

[[为语音计算的]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}]{#struct_0_13730_22192_2065106968}[值]{style="font-family:宋体"}

[[Hop IP]{lang="EN-US"}]{#struct_0_13730_22192_615840675}

[[本跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_x914404501}[地址，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Path-jitter results]{lang="EN-US"}]{#struct_0_13730_22192_615906211}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1339417001}[测试的结果，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Jitter number]{lang="EN-US"}]{#struct_0_13730_22192_615971747}

[[计算抖动次数，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x522791355}[测试中存在此信息]{style="font-family:宋体"}

[[Min/Max/Average jitter]{lang="EN-US"}]{#struct_0_13730_22192_616037283}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_x1978392869}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均抖动时延，单位为毫秒，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Positive jitter number]{lang="EN-US"}]{#struct_0_13730_22192_615578531}

[[正抖动时延的数目，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1432633475}[测试中存在此信息]{style="font-family:宋体"}

[[Min/Max/Average positive jitter]{lang="EN-US"}]{#struct_0_13730_22192_615644067}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_1922631439}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均正抖动时延，单位为毫秒，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Sum/Square-Sum positive jitter]{lang="EN-US"}]{#struct_0_13730_22192_615709603}

[[正抖动时延之和]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_x1939584019}[平方和，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Negative jitter number]{lang="EN-US"}]{#struct_0_13730_22192_615775139}

[[负抖动时延的数目，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_616364963}[测试中存在此信息]{style="font-family:宋体"}

[[Min/Max/Average negative jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2102197021}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_616430499}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均负抖动时延，单位为毫秒，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Sum/Square-Sum negative jitter]{lang="EN-US"}]{#struct_0_13730_22192_2065106967}

[[负抖动时延之和]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_615840672}[平方和，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_13730_22192_802738284}

[[本次收到的应答报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_13730_22192_802672748}[值]{style="font-family:宋体"}

[[Hop IP]{lang="EN-US"}]{#struct_0_13730_22192_x1996105533}

[[回复应答的节点]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_802607212}[地址]{style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_13730_22192_802541676}

[[收到应答报文的时间]{style="font-family:宋体"}]{#struct_0_13730_22192_802476140}

[ ]{lang="EN-US"}

::: {#-868847228 .myid}
[]{#_Toc404796646}[]{#struct_0_13730_22192_x914404504}[]{#_Toc199826507}

**NQA \-- NQA客户端配置命令 \-- display nqa statistics**

------------------------------------------------------------------------

[**[display nqa ]{lang="EN-US"}[statistics]{lang="EN-US"}**]{#struct_0_13730_22192_x1581013751}[命令用来显示]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1940090428}

[**[display nqa statistics]{lang="EN-US"}**[ \[ *admin-name* *operation-tag* \]]{lang="EN-US"}]{#struct_0_13730_22192_x1570290728}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1679251357}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x1667939838}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_615906208}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_999235166}

[[network-operator]{lang="EN-US"}]{#struct_0_13730_22192_747307579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1678411431}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13730_22192_1115355632}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1697815780}

[*[admin-name operation-tag]{lang="EN-US"}*]{#struct_0_13730_22192_x95290990}[：显示指定测试组的统计信息。如果不指定这两个参数，将显示所有测试组的统计信息。其中，]{style="font-family:
宋体"}*[admin-name]{lang="EN-US"}*[为创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写；]{style="font-family:宋体"}*[operation-tag]{lang="EN-US"}*[为测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x812899541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[测试开始后，如果第一次测试中的所有探测尚未完成，则无法生成统计信息。若此时通过该命令查看统计信息，则显示信息为全]{style="font-family:宋体"}]{#struct_0_13730_22192_746783578}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了阈值告警组，将显示在]{style="font-family:宋体"}]{#struct_0_13730_22192_615971744}**[statistics interval]{lang="EN-US"}**[命令指定的统计周期内的监测结果。若阈值告警组的阈值类型为平均值，或监测对象为]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[或]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值，则显示的监测结果为无效值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_802410604}[测试类型不支持用该命令显示统计信息。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x522791356}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_77952536}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[测试的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display nqa statistics admin test]{lang="EN-US"}]{#struct_0_13730_22192_616037280}

[NQA entry (admin admin, tag test) test statistics:]{lang="EN-US"}

[  NO. : 1]{lang="EN-US"}

[    Start time: 2007-01-01 09:30:20.0 ]{lang="EN-US"}

[    Life time: 2 seconds]{lang="EN-US"}

[    Send operation times: 1              Receive response times: 1 ]{lang="EN-US"}

[    Min/Max/Average round trip time: 13/13/13 ]{lang="EN-US"}

[    Square-Sum of round trip time: 169 ]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 0% ]{lang="EN-US"}

[    Failures due to timeout: 0]{lang="EN-US"}

[    Failures due to disconnect: 0]{lang="EN-US"}

[    Failures due to no connection: 0]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1978392870}[显示]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display nqa statistics admin test]{lang="EN-US"}]{#struct_0_13730_22192_615578528}

[NQA entry (admin admin, tag test) test statistics:]{lang="EN-US"}

[  NO. : 1]{lang="EN-US"}

[    Start time: 2007-01-01 09:33:22.3]{lang="EN-US"}

[    Life time: 23 seconds]{lang="EN-US"}

[    Send operation times: 100            Receive response times: 100]{lang="EN-US"}

[    Min/Max/Average round trip time: 1/11/5]{lang="EN-US"}

[    Square-Sum of round trip time: 24360]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 0%]{lang="EN-US"}

[    Failures due to timeout: 0]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[    Packets out of sequence: 0]{lang="EN-US"}

[    Packets arrived late: 0]{lang="EN-US"}

[  UDP-jitter results:]{lang="EN-US"}

[   ]{lang="EN-US"}[RTT number: 550]{lang="DA"}

[    Min positive SD: 1                     Min positive DS: 1]{lang="DA"}

[    ]{lang="DA"}[Max positive SD: 7                     Max positive DS: 1]{lang="EN-US"}

[    Positive SD number: 220                Positive DS number: 97]{lang="EN-US"}

[    Positive SD sum: 283                   Positive DS sum: 287]{lang="EN-US"}

[    Positive SD average: 1                 Positive DS average: 2]{lang="EN-US"}

[    Positive SD square-sum: 709            Positive DS square-sum: 1937]{lang="EN-US"}

[    ]{lang="EN-US"}[Min negative SD: 2                     Min negative DS: 1]{lang="DA"}

[    Max negative SD: 10                    Max negative DS: 1]{lang="DA"}

[    Negative SD number: 81                 Negative DS number: 94]{lang="DA"}

[    Negative SD sum: 556                   Negative DS sum: 191]{lang="DA"}

[    Negative SD average: 6                 Negative DS average: 2]{lang="DA"}

[    ]{lang="DA"}[Negative SD square-sum: 4292           Negative DS square-sum: 967]{lang="EN-US"}

[  One way results:]{lang="EN-US"}

[    Max SD delay: 5                        Max DS delay: 5]{lang="EN-US"}

[    ]{lang="EN-US"}[Min SD delay: 1                        Min DS delay: 1]{lang="DA"}

[    ]{lang="DA"}[Number of SD delay: 550                Number of DS delay: 550]{lang="EN-US"}

[    Sum of SD delay: 1475                  Sum of DS delay: 1201]{lang="EN-US"}

[    Square-Sum of SD delay: 5407           Square-Sum of DS delay: 3959]{lang="EN-US"}

[    SD lost packets: 0                     DS lost packets: 0]{lang="EN-US"}

[    Lost packets for unknown reason: 0]{lang="EN-US"}

[  Reaction statistics:]{lang="EN-US"}

[    Index  Checked Element  Threshold Type  Checked Num  Over-threshold Num]{lang="EN-US"}

[    1      jitter-DS        accumulate      90           25]{lang="EN-US"}

[    2      jitter-SD        average         -            -]{lang="EN-US"}

[    3      OWD-DS           -               100          24]{lang="EN-US"}

[    4      OWD-SD           -               100          13]{lang="EN-US"}

[    5      packet-loss      accumulate      0            0]{lang="EN-US"}

[    6      RTT              accumulate      100          52]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_906018678}[显示]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display nqa statistics admin test]{lang="EN-US"}]{#struct_0_13730_22192_615709600}

[NQA entry (admin admin, tag test) test statistics:]{lang="EN-US"}

[  NO. : 1]{lang="EN-US"}

[    Start time: 2007-01-01 09:33:45.3]{lang="EN-US"}

[    Life time: 120 seconds]{lang="EN-US"}

[    Send operation times: 10             Receive response times: 10]{lang="EN-US"}

[    Min/Max/Average round trip time: 1/12/7]{lang="EN-US"}

[    Square-Sum of round trip time: 620]{lang="EN-US"}

[  Extended results:]{lang="EN-US"}

[    Packet loss ratio: 0%]{lang="EN-US"}

[    Failures due to timeout: 0]{lang="EN-US"}

[    Failures due to internal error: 0]{lang="EN-US"}

[    Failures due to other errors: 0]{lang="EN-US"}

[    Packets out of sequence: 0]{lang="EN-US"}

[    Packets arrived late: 0]{lang="EN-US"}

[  Voice results:]{lang="EN-US"}

[   ]{lang="EN-US"}[RTT number: 10]{lang="DA"}

[    Min positive SD: 3                     Min positive DS: 1]{lang="DA"}

[    ]{lang="DA"}[Max positive SD: 10                    Max positive DS: 1]{lang="EN-US"}

[    Positive SD number: 3                  Positive DS number: 2]{lang="EN-US"}

[    Positive SD sum: 18                    Positive DS sum: 2]{lang="EN-US"}

[    Positive SD average: 6                 Positive DS average: 1]{lang="EN-US"}

[    Positive SD square-sum: 134            Positive DS square-sum: 2]{lang="EN-US"}

[    ]{lang="EN-US"}[Min negative SD: 3                     Min negative DS: 1]{lang="DA"}

[    Max negative SD: 9                     Max negative DS: 1]{lang="DA"}

[    Negative SD number: 4                  Negative DS number: 2]{lang="DA"}

[    Negative SD sum: 25                    Negative DS sum: 2]{lang="DA"}

[    Negative SD average: 6                 Negative DS average: 1]{lang="DA"}

[    ]{lang="DA"}[Negative SD square-sum: 187            Negative DS square-sum: 2]{lang="EN-US"}

[  One way results:]{lang="EN-US"}

[    Max SD delay: 0                        Max DS delay: 0]{lang="EN-US"}

[    ]{lang="EN-US"}[Min SD delay: 0                        Min DS delay: 0]{lang="DA"}

[    ]{lang="DA"}[Number of SD delay: 0                  Number of DS delay: 0]{lang="EN-US"}

[    Sum of SD delay: 0                     Sum of DS delay: 0]{lang="EN-US"}

[    Square-Sum of SD delay: 0              Square-Sum of DS delay: 0]{lang="EN-US"}

[    SD lost packets: 0                     DS lost packets: 0]{lang="EN-US"}

[    Lost packets for unknown reason: 0]{lang="EN-US"}

[  Voice scores:]{lang="EN-US"}

[    Max MOS value: 4.40                    Min MOS value: 4.40]{lang="EN-US"}

[    Max ICPIF value: 0                     Min ICPIF value: 0]{lang="EN-US"}

[  Reaction statistics:]{lang="EN-US"}

[    Index  Checked Element  Threshold Type  Checked Num  Over-threshold Num]{lang="EN-US"}

[    1      ICPIF            -               -            -]{lang="EN-US"}

[    2      MOS              -               -            -]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1939584022}[显示]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display nqa statistics admin test]{lang="EN-US"}]{#struct_0_13730_22192_616364960}

[NQA entry (admin admin, tag test) test statistics:]{lang="EN-US"}

[  NO. : 1]{lang="EN-US"}

[  Path 1:]{lang="EN-US"}

[  Hop IP 192.168.40.210]{lang="EN-US"}

[    Basic Results:]{lang="EN-US"}

[      Send operation times: 10]{lang="EN-US"}

[      Receive response times: 10]{lang="EN-US"}

[      Min/Max/Average round trip time: 1/1/1]{lang="EN-US"}

[      Square-Sum of round trip time: 10]{lang="EN-US"}

[    Extended Results:]{lang="EN-US"}

[      Packet loss ratio: 0%]{lang="EN-US"}

[      Failures due to timeout: 0]{lang="EN-US"}

[      Failures due to internal error: 0]{lang="EN-US"}

[      Failures due to other errors: 0]{lang="EN-US"}

[      Packets out of sequence: 0]{lang="EN-US"}

[      Packets arrived late: 0]{lang="EN-US"}

[    Path-Jitter Results:]{lang="EN-US"}

[      Jitter number: 9]{lang="EN-US"}

[        Min/Max/Average jitter: 0/0/0]{lang="EN-US"}

[      Positive jitter number: 0]{lang="EN-US"}

[        Min/Max/Average positive jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum positive jitter: 0/0]{lang="EN-US"}

[      Negative jitter number: 0]{lang="EN-US"}

[        Min/Max/Average negative jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum negative jitter: 0/0]{lang="EN-US"}

[  Hop IP 192.168.50.209]{lang="EN-US"}

[    Basic Results:]{lang="EN-US"}

[      Send operation times: 10]{lang="EN-US"}

[      Receive response times: 10]{lang="EN-US"}

[      Min/Max/Average round trip time: 1/1/1]{lang="EN-US"}

[      Square-Sum of round trip time: 10]{lang="EN-US"}

[    Extended Results:]{lang="EN-US"}

[      Packet loss ratio: 0%]{lang="EN-US"}

[      Failures due to timeout: 0]{lang="EN-US"}

[      Failures due to internal error: 0]{lang="EN-US"}

[      Failures due to other errors: 0]{lang="EN-US"}

[      Packets out of sequence: 0]{lang="EN-US"}

[      Packets arrived late: 0]{lang="EN-US"}

[    Path-Jitter Results:]{lang="EN-US"}

[      Jitter number: 9]{lang="EN-US"}

[        Min/Max/Average jitter: 0/0/0]{lang="EN-US"}

[      Positive jitter number: 0]{lang="EN-US"}

[        Min/Max/Average positive jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum positive jitter: 0/0]{lang="EN-US"}

[      Negative jitter number: 0]{lang="EN-US"}

[        Min/Max/Average negative jitter: 0/0/0]{lang="EN-US"}

[        Sum/Square-Sum negative jitter: 0/0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display nqa statistics]{lang="EN-US"}]{#struct_0_13730_22192_x2102197020}[命令显示信息描述]{style="font-family:黑体"}

[]{#table_struct_0_3497586}[[字段]{style="font-family:黑体"}]{#struct_0_13730_22192_616430496}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13730_22192_2065106966}

[[No.]{lang="EN-US"}]{#struct_0_13730_22192_x452328826}

[[统计组的组号]{style="font-family:宋体"}]{#struct_0_13730_22192_x1001416958}

[[Start time]{lang="EN-US"}]{#struct_0_13730_22192_x816549476}

[[测试组启动时间]{style="font-family:宋体"}]{#struct_0_13730_22192_442368702}

[[Life time]{lang="EN-US"}]{#struct_0_13730_22192_615840673}

[[测试的持续时间，单位为秒]{style="font-family:宋体"}]{#struct_0_13730_22192_x914404503}

[[Send operation times]{lang="EN-US"}]{#struct_0_13730_22192_x1581341431}

[[发送的探测报文数]{style="font-family:宋体"}]{#struct_0_13730_22192_406198466}

[[Receive response times]{lang="EN-US"}]{#struct_0_13730_22192_1314394090}

[[收到的响应报文数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1049372755}

[[Min/Max/Average round trip time]{lang="EN-US"}]{#struct_0_13730_22192_615906209}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_999235167}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均往返时间，单位为毫秒]{style="font-family:宋体"}

[[Square-Sum of round trip time]{lang="EN-US"}]{#struct_0_13730_22192_747307580}

[[往返时间平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x1251444398}

[[Packet loss ratio]{lang="EN-US"}]{#struct_0_13730_22192_x1700551092}

[[平均丢包率]{style="font-family:宋体"}]{#struct_0_13730_22192_615971745}

[[Failures due to timeout]{lang="EN-US"}]{#struct_0_13730_22192_x522791357}

[[测试过程中超时的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_77887000}

[[Failures due to disconnect]{lang="EN-US"}]{#struct_0_13730_22192_x1306564886}

[[对方强制断开连接的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_583264918}

[[Failures due to no connection]{lang="EN-US"}]{#struct_0_13730_22192_616037281}

[[和对方建立连接失败的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1978392871}

[[Failures due to internal error]{lang="EN-US"}]{#struct_0_13730_22192_x1238064891}

[[因内部错误失败的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_553855300}

[[Failures due to other errors]{lang="EN-US"}]{#struct_0_13730_22192_615578529}

[[因其它错误失败的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_906018677}

[[Packets out of sequence]{lang="EN-US"}]{#struct_0_13730_22192_x1027789478}

[[报文失序的次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x693618254}

[[Packets arrived late]{lang="EN-US"}]{#struct_0_13730_22192_615644065}

[[迟到报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_1922631437}

[[UDP-jitter results]{lang="EN-US"}]{#struct_0_13730_22192_1696311350}

[[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x617028553}[测试的结果，只在]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Voice results]{lang="EN-US"}]{#struct_0_13730_22192_615709601}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1939584021}[测试的结果，只在]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[RTT number]{lang="EN-US"}]{#struct_0_13730_22192_1726831358}

[[收到的响应报文数]{style="font-family:宋体"}]{#struct_0_13730_22192_482322295}

[[Min positive SD]{lang="EN-US"}]{#struct_0_13730_22192_615775137}

[[源到目的方向抖动时延为正值的最小值]{style="font-family:宋体"}]{#struct_0_13730_22192_402559463}

[[Min positive DS]{lang="EN-US"}]{#struct_0_13730_22192_x705082219}

[[目的到源方向抖动时延为正值的最小值]{style="font-family:宋体"}]{#struct_0_13730_22192_616364961}

[[Max positive SD]{lang="EN-US"}]{#struct_0_13730_22192_x2102197019}

[[源到目的方向抖动时延为正值的最大值]{style="font-family:宋体"}]{#struct_0_13730_22192_x788796490}

[[Max positive DS]{lang="EN-US"}]{#struct_0_13730_22192_x1113706935}

[[目的到源方向抖动时延为正值的最大值]{style="font-family:宋体"}]{#struct_0_13730_22192_616430497}

[[Positive SD number]{lang="EN-US"}]{#struct_0_13730_22192_2065106965}

[[源到目的方向抖动时延为正值的数目]{style="font-family:宋体"}]{#struct_0_13730_22192_x452263290}

[[Positive DS number]{lang="EN-US"}]{#struct_0_13730_22192_x2113042679}

[[目的到源方向抖动时延为正值的数目]{style="font-family:宋体"}]{#struct_0_13730_22192_1410111106}

[[Positive SD sum]{lang="EN-US"}]{#struct_0_13730_22192_81170539}

[[源到目的方向抖动时延为正值的和]{style="font-family:宋体"}]{#struct_0_13730_22192_1530697824}

[[Positive DS sum]{lang="EN-US"}]{#struct_0_13730_22192_x2112977143}

[[目的到源方向抖动时延为正值的和]{style="font-family:宋体"}]{#struct_0_13730_22192_x930842763}

[[Positive SD average]{lang="EN-US"}]{#struct_0_13730_22192_x1185297333}

[[源到目的方向抖动时延为正值的平均值]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112911607}

[[Positive DS average]{lang="EN-US"}]{#struct_0_13730_22192_x916560006}

[[目的到源方向抖动时延为正值的平均值]{style="font-family:宋体"}]{#struct_0_13730_22192_1843581566}

[[Positive SD square-sum]{lang="EN-US"}]{#struct_0_13730_22192_x2112846071}

[[源到目的方向抖动时延为正值的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2010367213}

[[Positive DS square-sum]{lang="EN-US"}]{#struct_0_13730_22192_313479126}

[[目的到源方向抖动时延为正值的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113304823}

[[Min negative SD]{lang="EN-US"}]{#struct_0_13730_22192_1973629498}

[[源到目的方向抖动时延为负值的最小绝对值]{style="font-family:宋体"}]{#struct_0_13730_22192_x1066591399}

[[Min negative DS]{lang="EN-US"}]{#struct_0_13730_22192_x2113239287}

[[目的到源方向抖动时延为负值的最小绝对值]{style="font-family:宋体"}]{#struct_0_13730_22192_x1509348807}

[[Max negative SD]{lang="EN-US"}]{#struct_0_13730_22192_x879272428}

[[源到目的方向抖动时延为负值的最大绝对值]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113173751}

[[Max negative DS]{lang="EN-US"}]{#struct_0_13730_22192_x286236428}

[[目的到源方向抖动时延为负值的最大绝对值]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113108215}

[[Negative SD number]{lang="EN-US"}]{#struct_0_13730_22192_1341999358}

[[源到目的方向抖动时延为负值的数目]{style="font-family:宋体"}]{#struct_0_13730_22192_428104743}

[[Negative DS number]{lang="EN-US"}]{#struct_0_13730_22192_x2112518391}

[[目的到源方向抖动时延为负值的数目]{style="font-family:宋体"}]{#struct_0_13730_22192_1192710323}

[[Negative SD sum]{lang="EN-US"}]{#struct_0_13730_22192_1790466126}

[[源到目的方向抖动时延为负值的绝对值和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112452855}

[[Negative DS sum]{lang="EN-US"}]{#struct_0_13730_22192_1615872774}

[[目的到源方向抖动时延为负值的绝对值和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113042678}

[[Negative SD average]{lang="EN-US"}]{#struct_0_13730_22192_x1318772249}

[[源到目的方向抖动时延为负值的绝对值的平均值]{style="font-family:宋体"}]{#struct_0_13730_22192_x302320266}

[[Negative DS average]{lang="EN-US"}]{#struct_0_13730_22192_x2112977142}

[[目的到源方向抖动时延为负值的绝对值的平均值]{style="font-family:宋体"}]{#struct_0_13730_22192_1798040592}

[[Negative SD square-sum]{lang="EN-US"}]{#struct_0_13730_22192_1346656421}

[[源到目的方向抖动时延为负值的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112911606}

[[Negative DS square-sum]{lang="EN-US"}]{#struct_0_13730_22192_1812323349}

[[目的到源方向抖动时延为负值的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112846070}

[[One way results]{lang="EN-US"}]{#struct_0_13730_22192_x444283272}

[[单向延迟测试结果，只有]{style="font-family:宋体"}[UDP-Jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2113304822}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[类型测试有单向延迟测试结果]{style="font-family:宋体"}

[[Max SD delay]{lang="EN-US"}]{#struct_0_13730_22192_x755253857}

[[源到目的的最大时延]{style="font-family:宋体"}]{#struct_0_13730_22192_x264006638}

[[Max DS delay]{lang="EN-US"}]{#struct_0_13730_22192_x2113239286}

[[目的到源的最大时延]{style="font-family:宋体"}]{#struct_0_13730_22192_1219534548}

[[Min SD delay]{lang="EN-US"}]{#struct_0_13730_22192_x2113173750}

[[源到目的的最小时延]{style="font-family:宋体"}]{#struct_0_13730_22192_x1852320369}

[[Min DS delay]{lang="EN-US"}]{#struct_0_13730_22192_x328183554}

[[目的到源的最小时延]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113108214}

[[Number of SD delay]{lang="EN-US"}]{#struct_0_13730_22192_x1386883997}

[[源到目的计算的时延数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112518390}

[[Number of DS delay]{lang="EN-US"}]{#struct_0_13730_22192_x373373618}

[[目的到源计算的时延数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112452854}

[[Sum of SD delay]{lang="EN-US"}]{#struct_0_13730_22192_49788833}

[[源到目的的时延和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113042681}

[[Sum of DS delay]{lang="EN-US"}]{#struct_0_13730_22192_1765489498}

[[目的到源的时延和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112977145}

[[Square-Sum of SD delay]{lang="EN-US"}]{#struct_0_13730_22192_x2093642177}

[[源到目的的时延的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112911609}

[[Square-Sum of DS delay]{lang="EN-US"}]{#struct_0_13730_22192_602469768}

[[目的到源的时延的平方和]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112846073}

[[SD lost packets]{lang="EN-US"}]{#struct_0_13730_22192_1121800669}

[[源到目的方向丢失的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113304825}

[[DS lost packets]{lang="EN-US"}]{#struct_0_13730_22192_810830084}

[[目的到源方向丢失的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113239289}

[[Lost packets for unknown reason]{lang="EN-US"}]{#struct_0_13730_22192_1979049435}

[[不能确定原因丢失的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1473897579}

[[Voice scores]{lang="EN-US"}]{#struct_0_13730_22192_x2113173753}

[[语音参数，只在]{style="font-family:宋体"}[voice]{lang="EN-US"}]{#struct_0_13730_22192_x1449035842}[类型测试有此信息]{style="font-family:宋体"}

[[Max MOS value]{lang="EN-US"}]{#struct_0_13730_22192_x2113108217}

[[最大]{style="font-family:宋体"}[MOS]{lang="EN-US"}]{#struct_0_13730_22192_179199944}[值]{style="font-family:宋体"}

[[Min MOS value]{lang="EN-US"}]{#struct_0_13730_22192_x2112518393}

[[最小]{style="font-family:宋体"}[MOS]{lang="EN-US"}]{#struct_0_13730_22192_x2112452857}[值]{style="font-family:宋体"}

[[Max ICPIF value]{lang="EN-US"}]{#struct_0_13730_22192_x1516295108}

[[最大]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}]{#struct_0_13730_22192_x2113042680}[值]{style="font-family:宋体"}

[[Min ICPIF value]{lang="EN-US"}]{#struct_0_13730_22192_x963393857}

[[最小]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}]{#struct_0_13730_22192_x2112977144}[值]{style="font-family:宋体"}

[[Reaction statistics]{lang="EN-US"}]{#struct_0_13730_22192_635241178}

[[阈值告警组在统计周期内的监测结果]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112911608}

[[Index]{lang="EN-US"}]{#struct_0_13730_22192_x963614173}

[[阈值告警组的编号]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112846072}

[[Checked Element]{lang="EN-US"}]{#struct_0_13730_22192_x1607082686}

[[监测对象]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113304824}

[[Threshold Type]{lang="EN-US"}]{#struct_0_13730_22192_x1918053271}

[[阈值类型]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113239288}

[[Checked Num]{lang="EN-US"}]{#struct_0_13730_22192_412965494}

[[已监测的样本个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113173752}

[[Over-threshold Num]{lang="EN-US"}]{#struct_0_13730_22192_1279847513}

[[超出阈值的样本个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113108216}

[[Path]{lang="EN-US"}]{#struct_0_13730_22192_x2112518392}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_789425796}[测试结果的路径序号，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Hop IP]{lang="EN-US"}]{#struct_0_13730_22192_x2112452856}

[[本跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_1212588247}[地址，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Path-jitter results]{lang="EN-US"}]{#struct_0_13730_22192_x2113042683}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_602690084}[测试的结果，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Jitter number]{lang="EN-US"}]{#struct_0_13730_22192_x2112977147}

[[计算抖动次数，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2112911611}[测试中存在此信息]{style="font-family:宋体"}

[[Min/Max/Average jitter]{lang="EN-US"}]{#struct_0_13730_22192_246304944}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_x2112846075}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均抖动时延，单位为毫秒，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Positive jitter number]{lang="EN-US"}]{#struct_0_13730_22192_315231615}

[[正抖动时延的数目，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2113304827}[测试中存在此信息]{style="font-family:宋体"}

[[Min/Max/Average positive jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2113239291}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_1622753539}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均正抖动时延，单位为毫秒，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Sum/Square-Sum positive jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2113173755}

[[正抖动时延之和]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_1683132040}[平方和，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Negative jitter number]{lang="EN-US"}]{#struct_0_13730_22192_x2113108219}

[[负抖动时延的数目，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x2112518395}[测试中存在此信息]{style="font-family:宋体"}

[[Min/Max/Average negative jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1132888505}

[[最小]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_x2112452859}[最大]{style="font-family:宋体"}[/]{lang="EN-US"}[平均负抖动时延，单位为毫秒，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[[Sum/Square-Sum negative jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1065956414}

[[负抖动时延之和]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13730_22192_x2113042682}[平方和，只在]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中存在此信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display nqa statistics]{lang="EN-US"}]{#struct_0_13730_22192_x2126193271}[命令显示阈值告警功能相关字段取值描述]{style="font-family:黑体"}

[]{#table_struct_0_42560662}[[监测对象]{style="font-family:黑体"}]{#struct_0_13730_22192_x1256746640}

[[阈值类型]{style="font-family:黑体"}]{#struct_0_13730_22192_1967522364}

[[监测的样本范围]{style="font-family:黑体"}]{#struct_0_13730_22192_x2112977146}

[[Checked Num]{lang="EN-US"}]{#struct_0_13730_22192_x527558236}[取值]{style="font-family:黑体"}

[[Over-threshold Num]{lang="EN-US"}]{#struct_0_13730_22192_240887313}[取值]{style="font-family:黑体"}

[[probe-duration]{lang="EN-US"}]{#struct_0_13730_22192_183607753}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_978958155}

[[统计周期内，进行的探测]{style="font-family:宋体"}]{#struct_0_13730_22192_x1099036276}

[[统计周期内，已完成的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112911610}

[[统计周期内，探测持续时间不在阈值范围内的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x1319778997}

[[average]{lang="EN-US"}]{#struct_0_13730_22192_x481728688}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1764925501}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1931241045}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1621948646}

[[consecutive]{lang="EN-US"}]{#struct_0_13730_22192_x2112846074}

[[统计周期内，进行的探测]{style="font-family:宋体"}]{#struct_0_13730_22192_1881315556}

[[统计周期内，已完成的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_950648473}

[[统计周期内，探测持续时间不在阈值范围内的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_1258492796}

[[probe-fail]{lang="EN-US"}]{#struct_0_13730_22192_1462188894}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_x2113304826}

[[统计周期内，进行的探测]{style="font-family:宋体"}]{#struct_0_13730_22192_1214114611}

[[统计周期内，已完成的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x437659789}

[[统计周期内，失败的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_220861210}

[[consecutive]{lang="EN-US"}]{#struct_0_13730_22192_1888104053}

[[统计周期内，进行的探测]{style="font-family:宋体"}]{#struct_0_13730_22192_x2113239290}

[[统计周期内，已完成的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_56669598}

[[统计周期内，失败的探测次数]{style="font-family:宋体"}]{#struct_0_13730_22192_x160885945}

[[RTT]{lang="EN-US"}]{#struct_0_13730_22192_x50370357}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_x2113173754}

[[统计周期内，发送的报文]{style="font-family:宋体"}]{#struct_0_13730_22192_117048099}

[[统计周期内，已发送的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_490615946}

[[统计周期内，往返时间不在阈值范围内的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_90712055}

[[average]{lang="EN-US"}]{#struct_0_13730_22192_x2113108218}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1294945191}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1337242976}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_2073034388}

[[jitter-DS/jitter-SD]{lang="EN-US"}]{#struct_0_13730_22192_x2112518394}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_1595994850}

[[统计周期内，发送的报文]{style="font-family:宋体"}]{#struct_0_13730_22192_616770036}

[[统计周期内，已发送的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_1555969342}

[[统计周期内，单向时延抖动不在阈值范围内的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x2112452858}

[[average]{lang="EN-US"}]{#struct_0_13730_22192_1662926941}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x1545859510}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x190728378}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_411861359}

[[OWD-DS/OWD-SD]{lang="EN-US"}]{#struct_0_13730_22192_x372862192}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x962532288}

[[统计周期内，发送的报文]{style="font-family:宋体"}]{#struct_0_13730_22192_x190662842}

[[统计周期内，已发送的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_406601013}

[[统计周期内，单向时延不在阈值范围内的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_1748582088}

[[packet-loss]{lang="EN-US"}]{#struct_0_13730_22192_x190597306}

[[accumulate]{lang="EN-US"}]{#struct_0_13730_22192_x825058655}

[[统计周期内，发送的报文]{style="font-family:宋体"}]{#struct_0_13730_22192_x1806457529}

[[统计周期内，已发送的报文个数]{style="font-family:宋体"}]{#struct_0_13730_22192_x190531770}

[[统计周期内的丢包数]{style="font-family:宋体"}]{#struct_0_13730_22192_1563668846}

[[ICPIF]{lang="EN-US"}]{#struct_0_13730_22192_1586343597}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x190990522}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_358426248}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_1660781951}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x190924986}

[[MOS]{lang="EN-US"}]{#struct_0_13730_22192_1947072766}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_408836774}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x190859450}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x761852623}

[[-]{lang="EN-US"}]{#struct_0_13730_22192_x479065345}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x543596696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics interval]{lang="EN-US"}**]{#struct_0_13730_22192_613635475}

::: {#-1430390705 .myid}
[]{#_Toc404796647}[]{#struct_0_13730_22192_x190793914}[]{#_Toc330975605}

**NQA \-- NQA客户端配置命令 \-- expect data**

------------------------------------------------------------------------

[**[expect data]{lang="EN-US"}**]{#struct_0_13730_22192_x2832264}[命令用来配置期望的应答内容。]{style="font-family:宋体"}

[**[undo ]{lang="SV"}[expect data]{lang="EN-US"}**]{#struct_0_13730_22192_286412641}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x404487541}

[**[expect data ]{lang="EN-US"}***[expression ]{lang="EN-US"}*[\[ **offset** *number* \]]{lang="EN-US"}]{#struct_0_13730_22192_x1913958601}

[**[undo ]{lang="SV"}[expect data]{lang="EN-US"}**]{#struct_0_13730_22192_382537393}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1003260109}

[[未配置期望的应答内容]{style="font-family:宋体"}]{#struct_0_13730_22192_x190204090}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1133574118}

[[HTTP/TCP/UDP]{lang="EN-US"}]{#struct_0_13730_22192_938754573}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_522968061}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_812131233}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1052363011}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_959551261}

[*[expression]{lang="EN-US"}*]{#struct_0_13730_22192_x179008262}[：期望收到的应答内容，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[offset]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_13730_22192_x190138554}[：所期望的内容在返回报文中的偏移量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_23953607}

[[在]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1267316596}[测试过程中，配置了该命令以后，]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端会检查接收到的测试报文中的应答内容：如果应答内容和该命令配置内容相同，则表示当前]{style="font-family:宋体"}[NQA]{lang="EN-US"}[目的端设备合法；否则为非法设备。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x837284767}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板，仅当回应报文中存在]{style="font-family:宋体"}[Content-Length]{lang="EN-US"}[头域时，进行期望应答内容的检查，否则不做检查。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_13730_22192_1060048767}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板，仅当]{style="font-family:宋体"}**[data-fill]{lang="EN-US"}**[和]{style="font-family:宋体"}**[expect data]{lang="EN-US"}**[命令都配置时，进行期望应答内容的检查，否则不做检查。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_13730_22192_970385846}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板，由于]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数据字段的前]{style="font-family:宋体"}[5]{lang="EN-US"}[个字节具有特定用途。缺省情况下，配置]{style="font-family:宋体"}**[expect data]{lang="EN-US"}**[后从第]{style="font-family:宋体"}[6]{lang="EN-US"}[个字节开始进行偏移检查。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x566120710}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1889328961}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置期望的应答为]{style="font-family:宋体"}[welcome!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190728377}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] expect data welcome!]{lang="EN-US"}
:::

::: {#-1504046040 .myid}
[]{#_Toc404796648}[]{#struct_0_13730_22192_412320111}[]{#_Toc330975606}

**NQA \-- NQA客户端配置命令 \-- expect status**

------------------------------------------------------------------------

[**[expect status]{lang="EN-US"}**]{#struct_0_13730_22192_401314747}[命令用来配置期望的应答状态码。]{style="font-family:宋体"}

[**[undo ]{lang="SV"}[expect status]{lang="EN-US"}**]{#struct_0_13730_22192_997090393}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x556414830}

[**[expect status]{lang="EN-US"}**[ *status-list*]{lang="EN-US"}]{#struct_0_13730_22192_935600159}

[**[undo ]{lang="SV"}[expect status]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[status-list]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_13730_22192_1015991813}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_2095681380}

[[未配置期望状态码。]{style="font-family:宋体"}]{#struct_0_13730_22192_x70199349}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190662841}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_406535477}[类型的模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1051463951}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1795081911}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1709761554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_608016414}

[*[status-list]{lang="EN-US"}*]{#struct_0_13730_22192_x1933038596}[：状态码列表，即]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[模板类型期望收到的状态码范围。表示方式为]{style="font-family:宋体"}*[status-list]{lang="EN-US"}*[ = { *status-num*1 \[ to *status-num*2 \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[status-num]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[999]{lang="EN-US"}[，]{style="font-family:宋体"}*[status-num]{lang="EN-US"}*[2]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[status-num]{lang="EN-US"}*[1]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1773809665}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x190597305}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板支持配置状态码。]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文的状态码是由]{style="font-family:宋体"}[3]{lang="EN-US"}[位十进制数组成的字段，它包含]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器的状态信息，用户可以根据该状态码了解]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器的状态。状态码的第一位规定状态码的类型，后两位编码没有规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x825255263}

[[\# ]{lang="SV"}]{#struct_0_13730_22192_1770758879}[在]{style="font-family:宋体"}[HTTP]{lang="SV"}[类型的]{style="font-family:
宋体"}[NQA]{lang="SV"}[模板视图下，配置期望状态码，允许状态码为]{style="font-family:宋体"}[200]{lang="SV"}[、]{style="font-family:宋体"}[300]{lang="SV"}[、]{style="font-family:宋体"}[400]{lang="SV"}[～]{style="font-family:
宋体"}[500]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1669435334}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] expect status 200 300 400 to 500]{lang="EN-US"}
:::

::: {#786503706 .myid}
[]{#_Toc404796649}[]{#struct_0_13730_22192_x829449647}[]{#_Toc330975607}

**NQA \-- NQA客户端配置命令 \-- expect ip**

------------------------------------------------------------------------

[**[expect ip]{lang="EN-US"}**]{#struct_0_13730_22192_253893327}[命令用来配置期望返回的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo expect ip]{lang="EN-US"}**]{#struct_0_13730_22192_x567051290}[命令用来取消期望返回的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_2048496883}

[**[expect ip ]{lang="SV"}**]{#struct_0_13730_22192_x190531769}*[ip-address]{lang="SV"}*

[**[undo expect ip]{lang="SV"}**]{#struct_0_13730_22192_1563079021}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1543316368}

[[未配置期望返回的]{style="font-family:宋体"}]{#struct_0_13730_22192_1821149272}[IP]{lang="SV"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x382513865}

[[DNS]{lang="SV"}]{#struct_0_13730_22192_1954074674}[类型的]{style="font-family:宋体"}[NQA]{lang="SV"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x928623958}

[[network-admin]{lang="SV"}]{#struct_0_13730_22192_33906542}

[[mdc-admin]{lang="SV"}]{#struct_0_13730_22192_x190990521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_358229640}

[*[ip-address]{lang="SV"}*]{#struct_0_13730_22192_x2138155037}[：]{style="font-family:宋体"}[DNS]{lang="SV"}[探测期望返回的]{style="font-family:
宋体"}[IP]{lang="SV"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1396494998}

[[在]{style="font-family:宋体"}]{#struct_0_13730_22192_110981106}[DNS]{lang="SV"}[测试中，]{style="font-family:宋体"}[NQA]{lang="SV"}[客户端通过该命令配置的]{style="font-family:宋体"}[IP]{lang="SV"}[地址与]{style="font-family:宋体"}[DNS]{lang="SV"}[服务器通过域名解析出的]{style="font-family:宋体"}[IP]{lang="SV"}[地址进行比较]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若相同]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则证明目前测试的]{style="font-family:宋体"}[DNS]{lang="SV"}[服务器合法]{style="font-family:宋体"}[，]{style="font-family:宋体"}[否则为非法]{style="font-family:宋体"}[DNS]{lang="SV"}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x141191293}

[[\# ]{lang="SV"}]{#struct_0_13730_22192_x1743223457}[在]{style="font-family:宋体"}[DNS]{lang="SV"}[类型的]{style="font-family:
宋体"}[NQA]{lang="SV"}[模板视图下，]{style="font-family:宋体"}[配置期望返回的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190924985}

[\[Sysname\] nqa template dns dnstplt]{lang="EN-US"}

[\[Sysname-nqatplt-dns-dnstplt\] expect ip 1.1.1.1]{lang="EN-US"}
:::

::: {#1143731253 .myid}
[]{#_Toc404796650}[]{#struct_0_13730_22192_1947007230}[]{#_Toc330975608}

**NQA \-- NQA客户端配置命令 \-- expect ipv6**

------------------------------------------------------------------------

[**[expect ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_x378929968}[命令用来配置期望返回的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo expect ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_1739516267}[命令用来取消期望返回的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1236871999}

[**[expect ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_13730_22192_x789602433}

[**[undo ]{lang="SV"}[expect ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_1628920820}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1679110842}

[[无期望返回的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13730_22192_x1099025173}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190859449}

[[DNS]{lang="SV"}]{#struct_0_13730_22192_x761393870}[类型的]{style="font-family:宋体"}[NQA]{lang="SV"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1126858444}

[[network-admin]{lang="SV"}]{#struct_0_13730_22192_871421876}

[[mdc-admin]{lang="SV"}]{#struct_0_13730_22192_x566967351}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x722972192}

[*[ipv6-address]{lang="SV"}*]{#struct_0_13730_22192_x2008618247}[：]{style="font-family:宋体"}[DNS]{lang="SV"}[探测期望返回的]{style="font-family:
宋体"}[IPv6]{lang="SV"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1593211187}

[[在]{style="font-family:宋体"}]{#struct_0_13730_22192_x190793913}[DNS]{lang="SV"}[测试中，]{style="font-family:宋体"}[NQA]{lang="SV"}[客户端通过该命令配置的]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址与]{style="font-family:宋体"}[DNS]{lang="SV"}[服务器通过域名解析出的]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址进行比较]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若相同]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则证明目前测试的]{style="font-family:宋体"}[DNS]{lang="SV"}[服务器合法]{style="font-family:宋体"}[，]{style="font-family:宋体"}[否则为非法]{style="font-family:宋体"}[DNS]{lang="SV"}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x3028872}

[[\# ]{lang="SV"}]{#struct_0_13730_22192_x712281990}[在]{style="font-family:宋体"}[DNS]{lang="SV"}[类型的]{style="font-family:
宋体"}[NQA]{lang="SV"}[模板视图下，]{style="font-family:宋体"}[配置期望返回的]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址为]{style="font-family:宋体"}[1::1]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_13730_22192_x1513988776}

[\[Sysname\] nqa template dns dnstplt]{lang="EN-US"}

[\[Sysname-nqatplt-dns-dnstplt\] expect ipv6 1::1]{lang="EN-US"}
:::

::: {#1969920693 .myid}
[]{#_Toc404796651}[]{#struct_0_13730_22192_x589977746}[]{#_Toc200180625}[]{#_Toc201634445}[]{#_Toc202085519}[]{#_Toc202085824}

**NQA \-- NQA客户端配置命令 \-- filename**

------------------------------------------------------------------------

[**[filename]{lang="EN-US"}**]{#struct_0_13730_22192_581411611}[命令用来配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器和客户端之间传送文件的文件名。]{style="font-family:宋体"}

[**[undo filename]{lang="EN-US"}**]{#struct_0_13730_22192_1001315641}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_613772048}

[**[filename]{lang="EN-US"}**[ *filename*]{lang="EN-US"}]{#struct_0_13730_22192_x190204089}

[**[undo]{lang="EN-US"}**[ **filename**]{lang="EN-US"}]{#struct_0_13730_22192_1133115367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_2126630391}

[[未配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_13730_22192_x1810290790}[服务器和客户端之间传送文件的文件名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_528334263}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_2125561182}[测试类型视图]{style="font-family:宋体"}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_668048405}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x409261201}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x190138553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_23494855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2038376981}

[*[filename]{lang="EN-US"}*]{#struct_0_13730_22192_629559914}[：]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器和客户端之间传送文件的文件名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[/]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x952491796}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x5538315}[配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器和客户端之间要传送文件的文件名为]{style="font-family:宋体"}[config.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_820354869}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type ftp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-ftp\] filename config.txt]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x190728380}[在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器和客户端之间要传送文件的文件名为]{style="font-family:宋体"}[config.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_412385656}

[\[Sysname\] nqa template ftp ftptplt]{lang="EN-US"}

[\[Sysname-nqatplt-ftp-ftptplt\] filename config.txt]{lang="EN-US"}
:::

::: {#1318637495 .myid}
[]{#_Toc404796652}[]{#struct_0_13730_22192_1558459449}

**NQA \-- NQA客户端配置命令 \-- frequency**

------------------------------------------------------------------------

[**[frequency]{lang="EN-US"}**]{#struct_0_13730_22192_x2035591995}[命令用来配置测试组连续两次测试开始时间的时间间隔。]{style="font-family:宋体"}

[**[undo frequency]{lang="EN-US"}**]{#struct_0_13730_22192_2141761343}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_232565717}

[**[frequency]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_13730_22192_x629951735}

[**[undo]{lang="EN-US"}**[ **frequency**]{lang="EN-US"}]{#struct_0_13730_22192_944272984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190662844}

[[在]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_406732085}[测试类型视图下，]{style="font-family:宋体"}[Voice]{lang="EN-US"}[、]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中连续两次测试开始时间的时间间隔为]{style="font-family:宋体"}[60000]{lang="EN-US"}[毫秒；其他类型的测试中连续两次测试开始时间的时间间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒，即只进行一次测试。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1716797093}[模板视图下，测试中连续两次测试开始时间的时间间隔为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x631473819}

[[任意测试类型视图]{style="font-family:宋体"}]{#struct_0_13730_22192_2041993006}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1220526449}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1400719875}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_723139843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x190597308}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x824927583}

[*[interval]{lang="EN-US"}*]{#struct_0_13730_22192_573410602}[：连续两次测试开始时间的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[604800000]{lang="EN-US"}[，单位为毫秒。时间间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示两次测试的时间间隔为无穷，即只进行一次测试，此时不会生成统计结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x792192317}

[[通过]{style="font-family:宋体"}**[nqa]{lang="EN-US"}**[ **schedule**]{lang="EN-US"}]{#struct_0_13730_22192_216743018}[命令启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组后，每隔]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[时间启动一次测试。]{style="font-family:宋体"}

[[需要注意的时，如果到达]{style="font-family:宋体"}**[frequency]{lang="EN-US"}**]{#struct_0_13730_22192_1940473799}[指定的时间间隔时，上次测试尚未完成，则不启动新一轮测试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1932512958}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1290666581}[配置连续两次测试开始时间的时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190531772}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] frequency 1000]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_13730_22192_1563537774}[在]{style="font-family:宋体"}[DNS]{lang="SV"}[类型的]{style="font-family:
宋体"}[NQA]{lang="SV"}[模板视图下，]{style="font-family:宋体"}[配置连续两次测试开始时间的时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x872184990}

[\[Sysname\] nqa template dns dnstplt]{lang="EN-US"}

[\[Sysname-nqatplt-dns-dnstplt\] frequency 1000]{lang="EN-US"}
:::

::: {#-1603435295 .myid}
[]{#_Toc404796653}[]{#struct_0_13730_22192_x468003743}

**NQA \-- NQA客户端配置命令 \-- history-record enable**

------------------------------------------------------------------------

[**[history-record enable]{lang="EN-US"}**]{#struct_0_13730_22192_511671853}[命令用来开启]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史记录保存功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **history-record enable**]{lang="EN-US"}]{#struct_0_13730_22192_511351203}[命令用来关闭]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史记录保存功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_432409423}

[**[history-record enable]{lang="EN-US"}**]{#struct_0_13730_22192_x190990524}

[**[undo history-record enable]{lang="EN-US"}**]{#struct_0_13730_22192_358557320}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_494205625}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_624587566}[测试类型的历史记录保存功能处于开启状态，其他类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史记录保存功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1611712902}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_376314765}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1314224994}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x223094838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_502476297}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190924988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果开启]{style="font-family:宋体"}]{#struct_0_13730_22192_1946679550}[NQA]{lang="EN-US"}[测试组的历史记录保存功能，则系统会记录该]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史信息，通过]{style="font-family:宋体"}**[display nqa history]{lang="EN-US"}**[命令可以查看该测试组的历史记录信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果关闭]{style="font-family:宋体"}]{#struct_0_13730_22192_1872190722}[NQA]{lang="EN-US"}[测试组的历史记录保存功能，则系统不会记录该测试组的历史信息，原有的历史记录信息也会被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1640090394}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x555817399}[开启]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的历史记录保存功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1428603608}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] history-record enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1261596305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nqa history]{lang="EN-US"}**]{#struct_0_13730_22192_x190859452}
:::

::: {#634423072 .myid}
[]{#_Toc404796654}[]{#struct_0_13730_22192_x761721551}

**NQA \-- NQA客户端配置命令 \-- history-record keep-time**

------------------------------------------------------------------------

[**[history-record keep-time]{lang="EN-US"}**]{#struct_0_13730_22192_x1625123324}[命令用来配置]{style="font-family:
宋体"}[NQA]{lang="EN-US"}[测试组中历史记录的保存时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **history-record keep-time**]{lang="EN-US"}]{#struct_0_13730_22192_x1035401185}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x665495698}

[**[history-record keep-time ]{lang="EN-US"}***[keep-time]{lang="EN-US"}*]{#struct_0_13730_22192_1387685971}

[**[undo history-record keep-time]{lang="EN-US"}**]{#struct_0_13730_22192_x1118388688}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x614448464}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x190793916}[测试组中历史记录的保存时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2701192}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_332335692}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x860995131}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x2070058833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_439091992}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_679094512}

[*[keep-time]{lang="EN-US"}*]{#struct_0_13730_22192_303339933}[：历史记录的保存时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190204092}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1133443046}[测试结束后，开始计算该测试组中所有历史记录的保存时间。保存时间达到配置的值后，将删除这些记录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x256931538}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1230667346}[配置]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组中历史记录的保存时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1606633724}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] history-record keep-time 100]{lang="EN-US"}
:::

::: {#346259929 .myid}
[]{#_Toc404796655}[]{#struct_0_13730_22192_1964062525}

**NQA \-- NQA客户端配置命令 \-- history-record number**

------------------------------------------------------------------------

[**[history-record number]{lang="EN-US"}**]{#struct_0_13730_22192_x604029692}[命令用来配置在一个测试组中能够保存的最大历史记录个数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **history-record number**]{lang="EN-US"}]{#struct_0_13730_22192_x190138556}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_23822535}

[**[history-record number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_13730_22192_708702903}

[**[undo history-record number]{lang="EN-US"}**]{#struct_0_13730_22192_1666330028}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1015524372}

[[一个测试组中能够保存的最大历史记录个数为]{style="font-family:宋体"}[50]{lang="EN-US"}]{#struct_0_13730_22192_x638671545}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_305229373}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_x1492009347}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1387659873}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x190728379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_411926895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2021354175}

[*[number]{lang="EN-US"}*]{#struct_0_13730_22192_x920767553}[：在一个测试组中能够保存的最大历史记录个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1701147427}

[[如果一个测试组中历史记录个数超过设定的最大数目，则最早的历史记录将会被删除。]{style="font-family:宋体"}]{#struct_0_13730_22192_x479601390}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1421250093}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x322423783}[配置一个测试组中能够保存的最大历史记录数为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190662843}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] history-record number 10]{lang="EN-US"}
:::

::: {#937814361 .myid}
[]{#_Toc404796656}[]{#struct_0_13730_22192_399978040}

**NQA \-- NQA客户端配置命令 \-- init-ttl**

------------------------------------------------------------------------

[**[init-ttl]{lang="EN-US"}**]{#struct_0_13730_22192_744640590}[命令用来配置]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测报文的初始跳数。]{style="font-family:宋体"}

[**[undo init-ttl]{lang="EN-US"}**]{#struct_0_13730_22192_617204635}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1872155425}

[**[init-ttl ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_13730_22192_x495152457}

[**[undo init-ttl]{lang="EN-US"}**]{#struct_0_13730_22192_x339723159}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1599383730}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_360562418}[探测报文的初始跳数为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_334032397}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_905299539}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1890124556}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x931990126}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_399912504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1093053921}

[*[value]{lang="EN-US"}*]{#struct_0_13730_22192_889191134}[：]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测报文的初始跳数，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x87687482}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1998902641}[配置]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测报文的初始跳数为]{style="font-family:宋体"}[5]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1604882860}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-tracert]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-tracert\] init-ttl 5]{lang="EN-US"}
:::

::: {#-1694695326 .myid}
[]{#_Toc404796657}[]{#struct_0_13730_22192_x557900154}[]{#_Toc382384262}

**NQA \-- NQA客户端配置命令 \-- key**

------------------------------------------------------------------------

[**[key]{lang="EN-US"}**]{#struct_0_13730_22192_x1052970264}[命令用来设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证使用的共享密钥。]{style="font-family:宋体"}

[**[undo key]{lang="EN-US"}**]{#struct_0_13730_22192_x917298265}[命令用来取消设置的共享密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1670023475}

[**[key ]{lang="EN-US"}**[{ **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_13730_22192_1533210765}

[**[undo key]{lang="EN-US"}**]{#struct_0_13730_22192_x930278050}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1117882052}

[[未设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_13730_22192_955849450}[认证使用的]{style="font-family:宋体"}[共享密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_325808072}

[[RADIUS]{lang="EN-US"}]{#struct_0_13730_22192_1008183787}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x698503384}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1944664004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1358072616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1815445038}

[**[cipher]{lang="EN-US"}**]{#struct_0_13730_22192_x2131795341}[：表示以密文方式设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证使用的]{style="font-family:宋体"}[共享密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13730_22192_x1158573908}[：表示以明文方式设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证使用的]{style="font-family:宋体"}[共享密钥。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_13730_22192_933602871}[：设置的明文密钥或密文密钥，区分大小写。明文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串；密文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_466474874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须保证设备上设置的共享密钥与]{style="font-family:宋体"}]{#struct_0_13730_22192_x1720699568}[RADIUS]{lang="EN-US"}[服务器上的完全一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1118611924}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_597619730}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_204368619}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证使用的]{style="font-family:宋体"}[共享密钥为明文]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1610843154}

[\[Sysname\] nqa template radius radiustplt]{lang="EN-US"}

[\[Sysname-nqatplt-radius-radiustplt\] key simple abc]{lang="EN-US"}
:::

::: {#1372356748 .myid}
[]{#_Toc404796658}[]{#struct_0_13730_22192_406666549}

**NQA \-- NQA客户端配置命令 \-- lsr-path**

------------------------------------------------------------------------

[**[lsr-path]{lang="EN-US"}**]{#struct_0_13730_22192_918980239}[命令用来配置松散路由。]{style="font-family:宋体"}

[**[undo lsr-path]{lang="EN-US"}**]{#struct_0_13730_22192_862170307}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x878400719}

[**[lsr-path ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[&*\<*1*-*8*\>*]{lang="EN-US"}]{#struct_0_13730_22192_x1294466434}

[**[undo]{lang="EN-US"}[ lsr-path]{lang="EN-US"}**]{#struct_0_13730_22192_507693803}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190597307}

[[未配置松散路由。]{style="font-family:宋体"}]{#struct_0_13730_22192_x825124191}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_613559906}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x809294072}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_189842213}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_2089316084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1059738508}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x374683256}

[*[ip-address]{lang="EN-US"}*[&*\<*1*-*8*\>*]{lang="EN-US"}]{#struct_0_13730_22192_x190531771}[：松散路由]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1563603310}

[[通过本命令配置松散路由，用户只需给出]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_334803291}[测试报文必须经过的一些"节点"，并不需要给出一条完备的路径，无直接连接的"节点"之间的路由需要路由器寻址功能补充。]{style="font-family:宋体"}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1660595683}[测试中，]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端通过]{style="font-family:宋体"}[tracert]{lang="EN-US"}[过程使用该命令配置的松散路由进行探路，并根据收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文计算主要"节点"时延和时延抖动。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1799052824}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_752238594}[配置松散路由为]{style="font-family:宋体"}[10.1.1.20]{lang="EN-US"}[和]{style="font-family:宋体"}[10.1.2.10]{lang="EN-US"}[两跳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_136887339}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type path-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test- path-jitter\] lsr-path 10.1.1.20 10.1.2.10]{lang="EN-US"}
:::

::: {#-414792311 .myid}
[]{#_Toc404796659}[]{#struct_0_13730_22192_399388215}

**NQA \-- NQA客户端配置命令 \-- max-failture**

------------------------------------------------------------------------

[**[max-failure]{lang="EN-US"}**]{#struct_0_13730_22192_1169188232}[命令用来配置一次]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试中连续探测失败的最大次数。]{style="font-family:宋体"}

[**[undo max-failure]{lang="EN-US"}**]{#struct_0_13730_22192_591900372}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_915052114}

[**[max-failure]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_13730_22192_x404959753}

[**[undo max-failure]{lang="EN-US"}**]{#struct_0_13730_22192_1222576951}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1062516220}

[[一次]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_683819333}[测试中连续探测失败的最大次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1509069875}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_399322679}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x430819034}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_2111247189}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1714908421}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1777051863}

[*[value]{lang="EN-US"}*]{#struct_0_13730_22192_x351747983}[：表示一次]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试中连续探测失败的最大次数。取值范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[和]{style="font-family:
宋体"}[255]{lang="EN-US"}[意味着]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测不会因为连续探测失败而停止测试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x861158793}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1102674914}[配置一次]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试中连续探测失败的最大次数为]{style="font-family:宋体"}[20]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1658456557}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-tracert]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-tracert\] max-failure 20]{lang="EN-US"}
:::

::: {#1985170617 .myid}
[]{#_Toc404796660}[]{#struct_0_13730_22192_1208529052}[]{#_Toc330304366}[]{#_Toc330304367}

**NQA \-- NQA客户端配置命令 \-- mode**

------------------------------------------------------------------------

[**[mode]{lang="EN-US"}**]{#struct_0_13730_22192_x190990523}[命令用来配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试的数据传输方式。]{style="font-family:宋体"}

[**[undo mode]{lang="EN-US"}**]{#struct_0_13730_22192_358360712}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x179778300}

[**[mode ]{lang="EN-US"}**[{ **active** \| **passive** }]{lang="EN-US"}]{#struct_0_13730_22192_x436052534}

[**[undo]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_13730_22192_971557606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1710355491}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_x2013553538}[测试的数据传输方式为主动方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1431652358}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_x190924987}[测试类型视图]{style="font-family:宋体"}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_1947138302}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1595610993}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1228646428}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_323498677}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1888214461}

[**[active]{lang="EN-US"}**]{#struct_0_13730_22192_1563653009}[：设置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[的数据传输方式为主动方式。]{style="font-family:宋体"}

[**[passive]{lang="EN-US"}**]{#struct_0_13730_22192_x1237470886}[：设置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[的数据传输方式为被动方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1264054121}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_x190859451}[的数据传输方式分为：主动方式和被动方式。主动方式是指在建立数据连接时由服务器主动发起连接请求；被动方式是指在建立数据连接时由客户端主动发起连接请求。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x761918159}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_347765963}[配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试的数据传输方式为被动方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1283920725}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type ftp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-ftp\] mode passive]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_966030921}[在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置数据传输方式为被动方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_166543800}

[\[Sysname\] nqa template ftp ftptplt]{lang="EN-US"}

[\[Sysname-nqatplt-ftp-ftptplt\] mode passive]{lang="EN-US"}
:::

::: {#-968771596 .myid}
[]{#_Toc404796661}[]{#struct_0_13730_22192_x190793915}

**NQA \-- NQA客户端配置命令 \-- next-hop**

------------------------------------------------------------------------

[**[next-hop]{lang="EN-US"}**]{#struct_0_13730_22192_x2897800}[命令用来配置探测报文的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo next-hop]{lang="EN-US"}**]{#struct_0_13730_22192_x508074448}[命令用来删除所配置的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1927725797}

[**[next-hop]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_13730_22192_x2032872025}

[**[undo]{lang="EN-US"}**[ **next-hop**]{lang="EN-US"}]{#struct_0_13730_22192_x823188567}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x480926297}

[[未配置下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_x1795740018}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_680022549}

[[ICMP-echo]{lang="EN-US"}]{#struct_0_13730_22192_x190204091}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1133639654}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x673889007}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1721166223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1481553268}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13730_22192_916025121}[：探测报文的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_730392112}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_536575978}[配置探测报文的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190138555}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] next-hop 10.1.1.1]{lang="EN-US"}
:::

::: {#997716835 .myid}
[]{#_Toc404796662}[]{#struct_0_13730_22192_399126071}

**NQA \-- NQA客户端配置命令 \-- no-fragment enable**

------------------------------------------------------------------------

[**[no-fragment enable]{lang="EN-US"}**]{#struct_0_13730_22192_1660243944}[命令用来开启]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测类型的禁止报文分片功能。]{style="font-family:宋体"}

[**[undo no-fragment enable]{lang="EN-US"}**]{#struct_0_13730_22192_x1405701662}[命令用来关闭]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测类型的禁止报文分片功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_399060535}

[**[no-fragment enable]{lang="EN-US"}**]{#struct_0_13730_22192_859614785}

[**[undo no-fragment enable]{lang="EN-US"}**]{#struct_0_13730_22192_530900724}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1263366323}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_279515027}[测试类型的禁止报文分片功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_67718085}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_1109163925}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2111983826}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x606524711}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1350222765}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x134333409}

[[开启此功能后，设备发送的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_x2074931}[报文头部的]{style="font-family:宋体"}[DF]{lang="EN-US"}[（]{style="font-family:宋体"}[don\'t fragment]{lang="EN-US"}[）字段会被置一，这样报文在转发过程中将无法被分片。通过配置这条命令可以对一条链路的路径]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值进行测试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x137912822}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_398994999}[开启]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测类型的禁止报文分片功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1742749077}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-tracert]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-tracert\] no-fragment enable]{lang="EN-US"}
:::

::: {#-624693529 .myid}
[]{#_Toc404796663}[]{#struct_0_13730_22192_23888071}

**NQA \-- NQA客户端配置命令 \-- nqa**

------------------------------------------------------------------------

[**[nqa]{lang="EN-US"}**]{#struct_0_13730_22192_637453597}[命令用来创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组，并进入]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组视图。]{style="font-family:宋体"}

[**[undo nqa]{lang="EN-US"}**]{#struct_0_13730_22192_490960007}[命令用来删除]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1928794028}

[**[nqa]{lang="EN-US"}***[ ]{lang="EN-US"}***[entry]{lang="EN-US"}***[ admin-name]{lang="EN-US"}*[ *operation-tag*]{lang="EN-US"}]{#struct_0_13730_22192_x1447468779}

[**[undo nqa]{lang="EN-US"}**[ { **all** \| **entry** *admin-name* *operation-tag* }]{lang="EN-US"}]{#struct_0_13730_22192_x1804485508}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190728382}

[[设备上不存在任何]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_412516728}[测试组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2072008215}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x1705069383}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x844674921}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1599848670}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1122608397}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1987323779}

[*[admin-name]{lang="EN-US"}*]{#struct_0_13730_22192_x140974651}[：创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[*[operation-tag]{lang="EN-US"}*]{#struct_0_13730_22192_x190662846}[：测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_13730_22192_406863157}[：所有]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_11580457}

[[如果配置了测试组的测试类型，执行]{style="font-family:宋体"}**[nqa entry]{lang="EN-US"}**]{#struct_0_13730_22192_1618333261}[命令进入该测试组时，系统将直接进入测试类型视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1755031416}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1099059082}[创建一个管理员名为]{style="font-family:宋体"}[admin]{lang="EN-US"}[，测试操作标签为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组，并进入]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1232796567}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\]]{lang="EN-US"}
:::

::: {#-518589374 .myid}
[]{#struct_0_13730_22192_x190597310}[]{#_Toc404796664}[]{#_Toc330975627}

**NQA \-- NQA客户端配置命令 \-- nqa template**

------------------------------------------------------------------------

[**[nqa template]{lang="EN-US"}**]{#struct_0_13730_22192_x825451870}[命令用来创建指定类型]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板，并进入]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[**[undo nqa template]{lang="EN-US"}**]{#struct_0_13730_22192_x2110491144}[命令用来删除]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x469355910}

[**[nqa template ]{lang="EN-US"}**[{ **dns** \| **ftp** \| **http** \| **icmp** \| **radius** \| **tcp** \| **udp** } *name*]{lang="EN-US"}]{#struct_0_13730_22192_464349163}

[**[undo nqa template ]{lang="EN-US"}**[{ **dns** \| **ftp** \| **http** \| **icmp** \| **radius** \| **tcp** \| **udp** } *name*]{lang="EN-US"}]{#struct_0_13730_22192_x1688558606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x437698016}

[[设备上不存在任何类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_2115340204}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190531774}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_1563930990}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x410955093}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_76558556}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1485819279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1500399154}

[**[dns]{lang="EN-US"}**]{#struct_0_13730_22192_585886134}[：配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[**[ftp]{lang="EN-US"}**]{#struct_0_13730_22192_1308335622}[：配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_13730_22192_105409302}[：配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[**[icmp]{lang="EN-US"}**]{#struct_0_13730_22192_1114425154}[：配置]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[**[radius]{lang="EN-US"}**]{#struct_0_13730_22192_x154550091}[：配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_13730_22192_585886133}[：配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[**[udp]{lang="EN-US"}**]{#struct_0_13730_22192_1308335627}[：配置]{style="font-family:宋体"}[UDP]{lang="EN-US"}[模板类型。]{style="font-family:宋体"}

[*[name]{lang="EN-US"}*]{#struct_0_13730_22192_66272642}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1931563216}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_358189332}[创建一个类型为]{style="font-family:宋体"}[icmp]{lang="EN-US"}[名称为]{style="font-family:宋体"}[icmptplt]{lang="EN-US"}[的模板，并进入]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190990526}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\]]{lang="EN-US"}
:::

::: {#2083155541 .myid}
[]{#_Toc404796665}[]{#struct_0_13730_22192_358688392}

**NQA \-- NQA客户端配置命令 \-- nqa agent enable**

------------------------------------------------------------------------

[**[nqa agent enable]{lang="EN-US"}**]{#struct_0_13730_22192_376830186}[命令用来开启]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端功能。]{style="font-family:宋体"}

[**[undo nqa agent enable]{lang="EN-US"}**]{#struct_0_13730_22192_x668876927}[命令用来关闭]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端功能，并停止所有正在进行的测试。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1641882261}

[**[nqa agent]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_13730_22192_878253501}

[**[undo nqa agent enable]{lang="EN-US"}**]{#struct_0_13730_22192_x1906518083}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190924990}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1947203839}[客户端功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x436023430}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_188307019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1209694057}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x491260401}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1244125821}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x6076244}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x2107448045}[开启]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190859454}

[\[Sysname\] nqa agent enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x762114767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_x1781992662}
:::

::: {#901204186 .myid}
[]{#_Toc404796666}[]{#struct_0_13730_22192_x275986306}[]{#_Toc294281670}[]{#_Toc145488655}[]{#_Toc145488658}

**NQA \-- NQA客户端配置命令 \-- nqa schedule**

------------------------------------------------------------------------

[**[nqa schedule]{lang="EN-US"}**]{#struct_0_13730_22192_x1691435386}[命令用来配置测试组的启动时间和持续时间。]{style="font-family:宋体"}

[**[undo nqa schedule]{lang="EN-US"}**]{#struct_0_13730_22192_437603648}[命令用来停止该测试组的测试。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_310827950}

[**[nqa schedule ]{lang="EN-US"}***[admin-name]{lang="EN-US"}*[ *operation-tag* **start-time** { *hh*:*mm*:*ss* \[ *yyyy/mm/dd \| mm/dd/yyyy* \] \| **now** } **lifetime** { *lifetime \|* **forever** } \[ **recurring** \]]{lang="EN-US"}]{#struct_0_13730_22192_1000682649}

[**[undo nqa schedule]{lang="EN-US"}[ ]{lang="EN-US"}***[admin-name]{lang="EN-US"}*[ *operation-tag*]{lang="EN-US"}]{#struct_0_13730_22192_x190793918}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2570120}

[[未配置]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_211692178}[调度功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_2110030520}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_2120677542}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_2091692810}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1385259833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x473741452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190204094}

[*[admin-name]{lang="EN-US"}*]{#struct_0_13730_22192_1133836262}[：创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[*[operation-tag]{lang="EN-US"}*]{#struct_0_13730_22192_x229102877}[：测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，字符串中不能包括"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[**[start-time]{lang="EN-US"}**]{#struct_0_13730_22192_x387585530}[：指定测试组的启动时间和日期。]{style="font-family:宋体"}

[*[hh]{lang="EN-US"}*[:*mm*:*ss*]{lang="EN-US"}]{#struct_0_13730_22192_882478033}[：测试组的启动时间，小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟]{style="font-family:宋体"}[:]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[*[yyyy/mm/dd]{lang="EN-US"}*]{#struct_0_13730_22192_x2114957981}[：测试组的启动日期，年]{style="font-family:宋体"}[:]{lang="EN-US"}[月]{style="font-family:宋体"}[:]{lang="EN-US"}[日，缺省值为系统的当前日期，年的取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mm/dd/yyyy]{lang="EN-US"}*]{#struct_0_13730_22192_x50106037}[：测试组的启动日期，月]{style="font-family:宋体"}[:]{lang="EN-US"}[日]{style="font-family:宋体"}[:]{lang="EN-US"}[年，缺省值为系统的当前日期，年的取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[now]{lang="EN-US"}**]{#struct_0_13730_22192_2091774076}[：测试组立即开始测试。]{style="font-family:宋体"}

[**[lifetime]{lang="EN-US"}**]{#struct_0_13730_22192_x190138558}[：指定测试的持续时间。]{style="font-family:宋体"}

[*[lifetime]{lang="EN-US"}*]{#struct_0_13730_22192_23167175}[：测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[forever]{lang="EN-US"}**]{#struct_0_13730_22192_x1609078365}[：测试组将一直进行测试。]{style="font-family:宋体"}

[**[recurring]{lang="EN-US"}**]{#struct_0_13730_22192_x293806755}[：指定测试组每天都被调度运行。每天启动测试的时间由]{style="font-family:宋体"}[start-time]{lang="EN-US"}[参数指定。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x866512934}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[测试组被调度后不允许进入测试组视图和测试类型视图。]{style="font-family:宋体"}]{#struct_0_13730_22192_1884555866}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统时间在启动时间～启动时间＋持续时间范围内时，测试组进行测试。执行]{style="font-family:宋体"}]{#struct_0_13730_22192_x2026914352}**[nqa schedule]{lang="EN-US"}**[命令时，如果系统时间尚未到达启动时间，则到达启动时间后，启动测试；如果系统时间在启动时间～启动时间＋持续时间之间，则立即启动测试；如果系统时间已经超过启动时间＋持续时间，则不会启动测试。]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}**[display clock]{lang="EN-US"}**[命令可以显示系统的当前时间。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_13730_22192_1995301975}[lifetime]{lang="EN-US"}[时间请保证一次测试能够完成，否则无法完成正常的联动操作]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1678580684}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x190728381}[启动管理员名字为]{style="font-family:宋体"}[admin]{lang="EN-US"}[，标签为]{style="font-family:宋体"}[test]{lang="EN-US"}[的测试组进行测试，测试组的启动时间为]{style="font-family:宋体"}[2008]{lang="EN-US"}[年]{style="font-family:宋体"}[8]{lang="EN-US"}[月]{style="font-family:
宋体"}[8]{lang="EN-US"}[日以后（包含当天）的每天的]{style="font-family:宋体"}[08:08:08]{lang="EN-US"}[，测试持续时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_412451192}

[\[Sysname\] nqa schedule admin test start-time 08:08:08 2008/08/08 lifetime 1000 recurring]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1264086115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[destination ip]{lang="EN-US"}**]{#struct_0_13730_22192_1168270050}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display clock]{lang="EN-US"}**]{#struct_0_13730_22192_x211463151}[（基础配置命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[设备管理）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa entry ]{lang="EN-US"}**]{#struct_0_13730_22192_x539986737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[type]{lang="EN-US"}**]{#struct_0_13730_22192_x1741358654}
:::

::: {#413930059 .myid}
[]{#_Toc404796667}[]{#struct_0_13730_22192_x816627956}[]{#_Toc312165603}[]{#_Toc145488661}

**NQA \-- NQA客户端配置命令 \-- operation (FTP test type view)**

------------------------------------------------------------------------

[**[operation]{lang="EN-US"}**]{#struct_0_13730_22192_x190662845}[命令用来配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试的操作方式。]{style="font-family:宋体"}

[**[undo operation]{lang="EN-US"}**]{#struct_0_13730_22192_406797621}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1007945439}

[**[operation ]{lang="EN-US"}**[{ **get** \| **put** }]{lang="EN-US"}]{#struct_0_13730_22192_642295083}

[**[undo operation]{lang="EN-US"}**]{#struct_0_13730_22192_1927812863}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x555475948}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_691710853}[测试的操作方式为]{style="font-family:宋体"}**[get]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x112423916}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_x190597309}[测试类型视图]{style="font-family:宋体"}

[[FTP]{lang="EN-US"}]{#struct_0_13730_22192_x824993119}[类型的模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2133172337}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1168418126}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1775677042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1335524295}

[**[get]{lang="EN-US"}**]{#struct_0_13730_22192_x504544747}[：从]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器获取文件。]{style="font-family:宋体"}

[**[put]{lang="EN-US"}**]{#struct_0_13730_22192_255312818}[：向]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器传送文件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1230848754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行]{style="font-family:宋体"}]{#struct_0_13730_22192_x190531773}**[put]{lang="EN-US"}**[操作时，若配置了]{style="font-family:宋体"}**[filename]{lang="EN-US"}**[，发送数据前判断]{style="font-family:宋体"}**[filename]{lang="EN-US"}**[指定的文件是否存在，如果存在则上传该文件，如果不存在则探测失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行]{style="font-family:宋体"}]{#struct_0_13730_22192_1563472238}**[get]{lang="EN-US"}**[操作时，如果]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器上没有以]{style="font-family:宋体"}**[url]{lang="EN-US"}**[中所配置的文件名为名字的文件，则测试不会成功。进行]{style="font-family:宋体"}**[get]{lang="EN-US"}**[操作时，设备上不会保存从服务器获取的文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行]{style="font-family:宋体"}]{#struct_0_13730_22192_x49333120}**[get]{lang="EN-US"}[、]{style="font-family:宋体"}[put]{lang="EN-US"}**[操作时，请选用较小的文件进行测试，如果文件较大，可能会因为超时而导致测试失败，或由于占用较多的网络带宽而影响其他业务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_962507049}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_840257904}[配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试的操作方式为]{style="font-family:宋体"}**[put]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1769646435}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type ftp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-ftp\] operation put]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x806584279}[在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试的操作方式为]{style="font-family:宋体"}**[put]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190990525}

[\[Sysname\] nqa template ftp ftptplt]{lang="EN-US"}

[\[Sysname-nqatplt-ftp-ftptplt\] operation put]{lang="EN-US"}
:::

::: {#1557210136 .myid}
[]{#_Toc404796668}[]{#struct_0_13730_22192_358491784}

**NQA \-- NQA客户端配置命令 \-- operation (HTTP test type view)**

------------------------------------------------------------------------

[**[operation]{lang="EN-US"}**]{#struct_0_13730_22192_111135669}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试的操作方式。]{style="font-family:宋体"}

[**[undo operation]{lang="EN-US"}**]{#struct_0_13730_22192_2099244663}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1157358000}

[**[operation ]{lang="EN-US"}**[{ **get** \| **post** \| **raw** }]{lang="EN-US"}]{#struct_0_13730_22192_x2069472611}

[**[undo operation]{lang="EN-US"}**]{#struct_0_13730_22192_x1718624861}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_600332397}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x190924989}[测试的操作方式为]{style="font-family:宋体"}**[get]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1946745086}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_375252380}[测试类型视图]{style="font-family:宋体"}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x1309884638}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1301785325}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1025837473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1724638450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1542324751}

[**[get]{lang="EN-US"}**]{#struct_0_13730_22192_x190859453}[：从]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器获取数据。]{style="font-family:宋体"}

[**[post]{lang="EN-US"}**]{#struct_0_13730_22192_x761787087}[：向]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器提交数据。]{style="font-family:宋体"}

[**[raw]{lang="EN-US"}**]{#struct_0_13730_22192_693129643}[：使用原始报文向服务器发送探测报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x363327971}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_1651855655}[测试的操作方式为]{style="font-family:宋体"}**[get]{lang="EN-US"}**[或]{style="font-family:宋体"}**[post]{lang="EN-US"}**[时，请求报文内容从]{style="font-family:宋体"}[url]{lang="EN-US"}[中获取。]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试的操作方式为]{style="font-family:宋体"}**[raw]{lang="EN-US"}**[时，请求报文为]{style="font-family:宋体"}**[raw-request]{lang="EN-US"}**[子视图中配置的内容。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x585245434}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_71207757}[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试的操作方式为]{style="font-family:宋体"}**[raw]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x190793917}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type http]{lang="EN-US"}

[\[Sysname-nqa-admin-test-http\] operation raw]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x2766728}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试的操作方式为]{style="font-family:宋体"}**[raw]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x58520326}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] operation raw]{lang="EN-US"}
:::

::: {#176950731 .myid}
[]{#_Toc404796669}[]{#struct_0_13730_22192_398994998}

**NQA \-- NQA客户端配置命令 \-- out interface**

------------------------------------------------------------------------

[**[out interface]{lang="EN-US"}**]{#struct_0_13730_22192_1742749076}[命令用来指定探测报文的出接口。]{style="font-family:宋体"}

[**[undo out interface]{lang="EN-US"}**]{#struct_0_13730_22192_1596546272}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_879509820}

[**[out interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13730_22192_x262550179}

[**[undo out interface]{lang="EN-US"}**]{#struct_0_13730_22192_1061167400}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_536249322}

[[未指定探测报文的出接口。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1520721633}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1772416625}

[[DHCP/ICMP-echo/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_399978038}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x447000506}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1383010410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x828606607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1240655772}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1146313625}[：探测报文出接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1738047696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令指定的接口必须处于]{style="font-family:宋体"}]{#struct_0_13730_22192_638151040}[UP]{lang="EN-US"}[状态，否则]{style="font-family:宋体"}[NQA]{lang="EN-US"}[探测过程将会失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_1670273320}[ICMP-echo]{lang="EN-US"}[测试类型，如果配置]{style="font-family:宋体"}**[next-hop]{lang="EN-US"}**[命令，此配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x115496479}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13730_22192_x522404904}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1723150059}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[作为]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测报文出接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_399912502}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-tracert]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-tracert\] out interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13730_22192_1093053919}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_888666843}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[作为]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测报文的出接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x588780572}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-tracert]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-tracert\] out interface vlan-interface 2]{lang="EN-US"}
:::

::: {#-231203086 .myid}
[]{#_Toc404796670}[]{#struct_0_13730_22192_483381158}

**NQA \-- NQA客户端配置命令 \-- password**

------------------------------------------------------------------------

[**[password]{lang="EN-US"}**]{#struct_0_13730_22192_2020837901}[命令用来配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[登录密码。]{style="font-family:宋体"}

[**[undo password]{lang="EN-US"}**]{#struct_0_13730_22192_1541321148}[命令用来取消已配置的登录密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x427313001}

[**[password]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_13730_22192_68837064}**[cipher]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[simple]{lang="EN-US"}**[ } ]{lang="EN-US"}*[password]{lang="EN-US"}*

[**[undo password]{lang="EN-US"}**]{#struct_0_13730_22192_x190204093}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1133508582}

[[未配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_13730_22192_100317528}[或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[的登录密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_869558986}

[[FTP/HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x430811013}[测试类型视图]{style="font-family:宋体"}

[[FTP/HTTP/RADIUS]{lang="EN-US"}]{#struct_0_13730_22192_1754951291}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1262202709}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1851145540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1898896879}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x190138557}

[**[cipher]{lang="EN-US"}**]{#struct_0_13730_22192_23756999}[：表示以密文形式设置密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13730_22192_x1840772232}[：表示以明文形式设置密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_13730_22192_x501193888}[：测试使用的密码，区分大小写。]{style="font-family:宋体"}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[的登录密码，明文形式输入密码时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，密文形式输入密码时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[密码，明文形式输入时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，密文形式输入时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x242058181}

[[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_13730_22192_1699198266}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_783463355}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1249546491}[配置录]{style="font-family:宋体"}[FTP]{lang="EN-US"}[登录密码为]{style="font-family:宋体"}[ftpuser]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375355563}

[[\[Sysname\] nqa entry admin test]{lang="EN-US"}]{#struct_0_13730_22192_x1096576263}

[[\[Sysname-nqa-admin-test\] type ftp]{lang="EN-US"}]{#struct_0_13730_22192_999439189}

[[\[Sysname-nqa-admin-test-ftp\] password simple ftpuser]{lang="EN-US"}]{#struct_0_13730_22192_x105971130}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_943875681}[在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[登录密码为]{style="font-family:宋体"}[ftpuser]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1966360973}

[\[Sysname\] nqa template ftp ftptplt]{lang="EN-US"}

[\[Sysname-nqatplt-ftp-ftptplt\] password simple ftpuser]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_501765102}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[operation]{lang="EN-US"}**]{#struct_0_13730_22192_x392658870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[username]{lang="EN-US"}**]{#struct_0_13730_22192_1375421099}
:::

::: {#-362870311 .myid}
[]{#_Toc404796671}[]{#struct_0_13730_22192_x1854029841}[]{#_Toc171419736}[]{#_Toc171481438}[]{#_Toc172364097}[]{#_Toc154997911}[]{#_Toc154997912}[]{#_Toc154997914}[]{#_Toc154997915}[]{#_Toc154997916}[]{#_Toc154997917}[]{#_Toc154997918}[]{#_Toc154997919}[]{#_Toc154997920}[]{#_Toc154997921}[]{#_Toc154997922}[]{#_Toc154997923}[]{#_Toc154997924}[]{#_Toc154997925}[]{#_Toc154997926}[]{#_Toc154997929}

**NQA \-- NQA客户端配置命令 \-- probe count**

------------------------------------------------------------------------

[**[probe count]{lang="EN-US"}**]{#struct_0_13730_22192_1235220099}[命令用来配置一次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试中探测的次数。]{style="font-family:宋体"}

[**[undo probe count]{lang="EN-US"}**]{#struct_0_13730_22192_1656755540}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1375543900}

[**[probe count]{lang="EN-US"}**[ *times*]{lang="EN-US"}]{#struct_0_13730_22192_x798619011}

[**[undo probe count]{lang="EN-US"}**]{#struct_0_13730_22192_984616180}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1378408026}

[[对于]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_1375486635}[测试类型，对于一个]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值的节点发送的探测报文次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次；其他类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试一次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试中的探测次数为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1202057254}

[[DHCP/DNS/DLSw/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_x452296258}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1346254400}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_2077061548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x50809873}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1885967704}

[*[times]{lang="EN-US"}*]{#struct_0_13730_22192_x2077240292}[：对于]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试类型，配置对于一个]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值的节点发送的探测报文次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[；对于其他测试类型，配置的是一次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试中进行探测的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375552171}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_x295035499}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[DLSw]{lang="EN-US"}[测试，一次探测操作是指建立一次连接；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_557810441}[和]{lang="EN-US" style="font-family:宋体"}[Voice]{lang="EN-US"}[测试，一次探测操作是指连续发送多个探测报文，发送探测报文的个数由]{lang="EN-US" style="font-family:宋体"}**[probe packet-number]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:
宋体"}[指定]{style="font-family:宋体"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_x1919486386}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[、]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[和]{style="font-family:宋体"}[DNS]{lang="EN-US"}[测试，一次探测操作是指完成一次相应的功能，例如上传或下载一个文件，获取一个]{style="font-family:宋体"}[Web]{lang="EN-US"}[页面，为接口申请一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，将一个域名解析为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_367798976}[ICMP-echo]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-echo]{lang="EN-US"}[测试，一次探测操作是指发送一个探测报文；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_x1225584124}[SNMP]{lang="EN-US"}[测试，一次探测操作是指发送三个]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议报文，分别对应]{style="font-family:宋体"}[SNMP v1]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMP v2c]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMP v3]{lang="EN-US"}[三个版本；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_499784343}[Path-jitter]{lang="EN-US"}[测试，一次探测操作分为两个步骤：首先通过]{style="font-family:宋体"}[tracert]{lang="EN-US"}[探路获取到达目的地址的路径（最大为]{style="font-family:宋体"}[64]{lang="EN-US"}[跳）；再根据]{style="font-family:宋体"}[tracert]{lang="EN-US"}[结果，分别向路径上的每一跳发送多个]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文，发送探测报文的个数由用户来设定；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_399257149}[UDP-tracert]{lang="EN-US"}[测试，对目的节点进行的整个]{style="font-family:宋体"}[Tracert]{lang="EN-US"}[过程称为一次测试，对于一个特定]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值的节点发送一个探测报文的操作称为一次探测，对于同一个]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值的节点发送探测报文的次数由]{style="font-family:宋体"}**[probe count]{lang="EN-US"}**[命令来设定。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_523887728}[测试来说，对于同一个]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的节点，设备会发送数量为]{style="font-family:宋体"}**[probe count]{lang="EN-US"}**[命令配置的探测报文，系统在进行第一次探测之后，等待回应；对于其他类型的测试，如果配置的次数大于]{style="font-family:宋体"}[1]{lang="EN-US"}[，那么系统在进行第一次探测之后，等待回应。如果到达]{style="font-family:宋体"}**[probe timeout]{lang="EN-US"}**[命令指定的探测超时时间时，仍然没有收到回应，则发起第二次探测。如此反复，直到完成指定次数的探测。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[Voice]{lang="EN-US"}]{#struct_0_13730_22192_1750508758}[和]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试不支持该命令，一次测试中只能进行一次探测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375093419}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_55028129}[配置一次]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[测试中探测的次数为]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1048696213}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] probe count 10]{lang="EN-US"}
:::

::: {#-366870707 .myid}
[]{#_Toc404796672}[]{#struct_0_13730_22192_x1308911343}

**NQA \-- NQA客户端配置命令 \-- probe packet-interval**

------------------------------------------------------------------------

[**[probe packet-interval]{lang="EN-US"}**]{#struct_0_13730_22192_x2084669603}[命令用来配置测试中发送探测报文的时间间隔。]{style="font-family:宋体"}

[**[undo probe packet-interval]{lang="EN-US"}**]{#struct_0_13730_22192_1894928574}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1503153487}

[**[probe packet-interval ]{lang="EN-US"}***[packet-interval]{lang="EN-US"}*]{#struct_0_13730_22192_1375158955}

[**[undo probe packet-interval]{lang="EN-US"}**]{#struct_0_13730_22192_951816213}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1444595240}

[[测试中发送探测报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_13730_22192_x1871210700}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1426165111}

[[Path-jitter/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_1220548547}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_950851601}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1518217891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1621522938}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375224491}

[*[packet-interval]{lang="EN-US"}*]{#struct_0_13730_22192_x330365012}[：测试中发送探测报文的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x631661780}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x309957055}[配置]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试中发送探测报文的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_886656917}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] probe packet-interval 100]{lang="EN-US"}
:::

::: {#-1208669460 .myid}
[]{#_Toc404796673}[]{#struct_0_13730_22192_312884432}

**NQA \-- NQA客户端配置命令 \-- probe packet-number**

------------------------------------------------------------------------

[**[probe packet-number]{lang="EN-US"}**]{#struct_0_13730_22192_x17213560}[命令用来配置一次探测中发送探测报文的个数。]{style="font-family:宋体"}

[**[undo probe packet-number]{lang="EN-US"}**]{#struct_0_13730_22192_1375290027}[命令用恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_856569159}

[**[probe packet-number ]{lang="EN-US"}***[packet-number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_13730_22192_564191684}

[**[undo probe packet-number]{lang="EN-US"}**]{#struct_0_13730_22192_x1478068700}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1513029945}

[[一次]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x625986203}[或]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[探测中发送]{style="font-family:宋体"}[10]{lang="EN-US"}[个探测报文；一次]{style="font-family:宋体"}[Voice]{lang="EN-US"}[探测中发送]{style="font-family:宋体"}[1000]{lang="EN-US"}[个探测报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x740419450}

[[Path-jitter/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_565979845}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1524349326}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1375879851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_556997263}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1085876983}

[*[packet-number]{lang="EN-US"}*]{#struct_0_13730_22192_608067496}[：一次探测中发送探测报文的个数，对于]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[和]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[；对于]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_834743085}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1644453112}[配置一次]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[探测中发送]{style="font-family:宋体"}[100]{lang="EN-US"}[个探测报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1386492233}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] probe packet-number 100]{lang="EN-US"}
:::

::: {#1440553634 .myid}
[]{#_Toc404796674}[]{#struct_0_13730_22192_1375945387}

**NQA \-- NQA客户端配置命令 \-- probe packet-timeout**

------------------------------------------------------------------------

[**[probe packet-timeout]{lang="EN-US"}**]{#struct_0_13730_22192_x1472425543}[命令用来配置一次探测中等待响应报文的超时时间。]{style="font-family:宋体"}

[**[undo probe packet-timeout]{lang="EN-US"}**]{#struct_0_13730_22192_x2018214450}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1257714226}

[**[probe packet-timeout]{lang="EN-US"}***[ packet-timeout]{lang="EN-US"}*]{#struct_0_13730_22192_x722072474}

[**[undo probe packet-timeout]{lang="EN-US"}**]{#struct_0_13730_22192_x817370712}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x649014723}

[[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x106611201}[和]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中等待响应报文的超时时间为]{style="font-family:宋体"}[3000]{lang="EN-US"}[毫秒；]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试中等待响应报文的超时时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375355564}

[[Path-jitter/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1096117511}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_261571118}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_876315617}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_157165852}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1039044586}

[*[packet-timeout]{lang="EN-US"}*]{#struct_0_13730_22192_1518617255}[：一次探测中等待响应报文的超时时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x290424454}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_440531092}[配置]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试中等待响应报文的超时时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375421100}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] probe packet-timeout 100]{lang="EN-US"}
:::

::: {#81035479 .myid}
[]{#_Toc404796675}[]{#struct_0_13730_22192_101695464}

**NQA \-- NQA客户端配置命令 \-- probe timeout**

------------------------------------------------------------------------

[**[probe timeout]{lang="EN-US"}**]{#struct_0_13730_22192_729863790}[命令用来配置探测的超时时间。]{style="font-family:宋体"}

[**[undo probe timeout]{lang="EN-US"}**]{#struct_0_13730_22192_x1713261924}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x781086874}

[**[probe timeout]{lang="EN-US"}**[ *timeout*]{lang="EN-US"}]{#struct_0_13730_22192_1805266234}

[**[undo probe timeout]{lang="EN-US"}**]{#struct_0_13730_22192_x1491399329}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375486636}

[[探测的超时时间为]{style="font-family:宋体"}[3000]{lang="EN-US"}]{#struct_0_13730_22192_1202122790}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_377436814}

[[DHCP/DNS/DLSw/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_1775404871}[测试类型视图]{style="font-family:宋体"}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1389430509}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_728135406}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_671035385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1019508432}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1940424746}

[*[timeout]{lang="EN-US"}*]{#struct_0_13730_22192_1375552172}[：一次探测的超时时间，单位为毫秒。在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[探测中，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[86400000]{lang="EN-US"}[；在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[、]{style="font-family:宋体"}[DNS]{lang="EN-US"}[、]{style="font-family:宋体"}[DLSw]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-echo]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[探测中，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x295101035}

[[如果]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1760866566}[探测没有在]{style="font-family:宋体"}**[probe timeout]{lang="EN-US"}**[命令指定的时间内完成，则认为本次探测超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1282666901}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_541927437}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[探测的超时时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1263876408}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type dhcp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-dhcp\] probe timeout 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_593159460}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测的超时时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375093420}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] probe timeout 10000]{lang="EN-US"}
:::

::: {#-70860042 .myid}
[]{#_Toc404796676}[]{#struct_0_13730_22192_55617956}

**NQA \-- NQA客户端配置命令 \-- raw-request**

------------------------------------------------------------------------

[**[raw-request]{lang="EN-US"}**]{#struct_0_13730_22192_x649295207}[命令用来进入]{style="font-family:宋体"}[raw-request]{lang="EN-US"}[子视图，并在该子视图下配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试请求报文内容。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **raw-request**]{lang="EN-US"}]{#struct_0_13730_22192_1415164634}[命令用来删除配置的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试请求报文内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_974837617}

[**[raw-request]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13730_22192_x1514690977}

[**[undo]{lang="EN-US"}**[ **raw-request**]{lang="EN-US"}]{#struct_0_13730_22192_x458631451}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375158956}

[[没有配置报文内容。]{style="font-family:宋体"}]{#struct_0_13730_22192_951750677}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x475395108}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x1815126033}[测试类型视图]{style="font-family:宋体"}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x961695915}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_883255436}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1631476721}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1254173538}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x208550112}

[[每次使用]{style="font-family:宋体"}**[raw-request]{lang="EN-US"}**]{#struct_0_13730_22192_1375224492}[命令进入]{style="font-family:宋体"}[raw-request]{lang="EN-US"}[子视图时，之前在该子视图下配置的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试请求报文内容会被清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x330561620}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_547057111}[进入]{style="font-family:宋体"}[raw-request]{lang="EN-US"}[子视图，并在该子视图下配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试请求报文的内容。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x760827954}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type http]{lang="EN-US"}

[\[Sysname-nqa-admin-test-http\] raw-request]{lang="EN-US"}

[\[Sysname-nqa-admin-test-http-raw-request\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_697127425}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，进入]{style="font-family:宋体"}[raw-request]{lang="EN-US"}[子视图，并在该子视图下配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试请求报文的内容。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x609162831}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] raw-request]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt-raw-request\]]{lang="EN-US"}
:::

::: {#-1965459083 .myid}
[]{#_Toc404796677}[]{#struct_0_13730_22192_1375290028}[]{#_Toc250551348}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element icpif**

------------------------------------------------------------------------

[**[reaction checked-element icpif]{lang="EN-US"}**]{#struct_0_13730_22192_856503623}[命令用来创建监测]{style="font-family:
宋体"}[Voice]{lang="EN-US"}[测试]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x993318665}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_383549682}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_x378330139}**[ ]{lang="EN-US"}[icpif threshold-value]{lang="EN-US"}[ ]{lang="EN-US"}***[upper-threshold lower-threshold]{lang="EN-US"}*[ \[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1006108127}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1087193347}

[[未创建监测]{style="font-family:宋体"}[Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1873149252}[测试]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值的阈值告警组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1759720653}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_1375879852}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_557193871}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1417051682}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1808756606}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x741378886}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_2140386780}[：阈值告警组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-value]{lang="EN-US"}**]{#struct_0_13730_22192_661027608}[：指定阈值范围。]{style="font-family:宋体"}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_1505087643}[：阈值上限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_1375945388}[：阈值下限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，且必须小于等于阈值上限。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_x1472884295}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_1866035445}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_1432918743}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1525761840}

[[阈值告警组创建后，不能再通过]{style="font-family:宋体"}**[reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x804547423}[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_840191762}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x833512339}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测每次]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试的]{style="font-family:宋体"}[ICPIF]{lang="EN-US"}[值，若超出阈值范围，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375355561}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type voice]{lang="EN-US"}

[\[Sysname-nqa-admin-test-voice\] reaction 1 checked-element icpif threshold-value 50 5 action-type trap-only]{lang="EN-US"}
:::

::: {#-491063661 .myid}
[]{#_Toc250551349}[]{#_Toc404796678}[]{#struct_0_13730_22192_x1096445191}[]{#_Toc250551355}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element { jitter-ds \| jitter-sd }**

------------------------------------------------------------------------

[**[reaction checked-element ]{lang="EN-US"}**[{ **jitter-ds** \| **jitter-sd** }]{lang="EN-US"}]{#struct_0_13730_22192_386550309}[命令用来创建监测单向时延抖动的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_22456697}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1696025901}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_x196823427}[ ]{lang="EN-US"}[{ **jitter-ds** \| **jitter-sd** } ]{lang="EN-US"}**[threshold-type ]{lang="EN-US"}**[{ **accumulate** *accumulate-occurrences* \| **average** } **threshold-value** *upper-threshold lower-threshold* \[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_783534298}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x419502990}

[[未创建监测单向时延抖动的阈值告警组。]{style="font-family:宋体"}]{#struct_0_13730_22192_1375421097}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1854947345}

[[UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x609196694}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1974721035}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1991983090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1853233797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1121712912}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x472797537}[：阈值告警组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[jitter-ds]{lang="EN-US"}**]{#struct_0_13730_22192_1375486633}[：监测从目的到源的单向时延抖动。]{style="font-family:宋体"}

[**[jitter-sd]{lang="EN-US"}**]{#struct_0_13730_22192_1201926182}[：监测从源到目的的单向时延抖动。]{style="font-family:宋体"}

[**[threshold-type]{lang="EN-US"}**]{#struct_0_13730_22192_x1075835903}[：指定阈值类型。]{style="font-family:宋体"}

[**[accumulate]{lang="EN-US"}**[ *accumulate-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_972859000}[：每次测试中，累计的单向时延抖动超出阈值的报文个数。对于]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[14999]{lang="EN-US"}[；对于]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[59999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[average]{lang="EN-US"}**]{#struct_0_13730_22192_x52342428}[：每次测试中，单向时延抖动的平均值。]{style="font-family:宋体"}

[**[threshold-value]{lang="EN-US"}**]{#struct_0_13730_22192_1316957939}[：指定阈值范围。]{style="font-family:宋体"}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_454260888}[：阈值上限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_1781126248}[：阈值下限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，且必须小于等于阈值上限，单位为毫秒。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_1375552169}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_x295559788}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_202640539}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1198274037}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[阈值告警组创建后，不能再通过]{style="font-family:宋体"}]{#struct_0_13730_22192_131245616}**[reaction]{lang="EN-US"}**[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监测的对象是探测成功的报文，探测失败的报文不参与计数。]{style="font-family:宋体"}]{#struct_0_13730_22192_x116396587}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1299889018}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x2041430479}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[探测报文的从目的到源的单向时延抖动，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试的平均单向时延抖动，若超出阈值，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375093417}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] reaction 1 checked-element jitter-ds threshold-type average threshold-value 50 5 action-type trap-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_55159201}[创建编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[探测报文的从目的到源的单向时延抖动，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试中累计的单向时延抖动超出阈值的报文个数，若达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[个，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x677907235}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] reaction 2 checked-element jitter-ds threshold-type accumulate 100 threshold-value 50 5 action-type trap-only]{lang="EN-US"}
:::

::: {#-1137905355 .myid}
[]{#_Toc404796679}[]{#struct_0_13730_22192_1447512555}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element mos**

------------------------------------------------------------------------

[**[reaction checked-element mos]{lang="EN-US"}**]{#struct_0_13730_22192_218913274}[命令用来创建监测]{style="font-family:
宋体"}[Voice]{lang="EN-US"}[测试]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_99647830}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1653235001}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_1375158953}**[ ]{lang="EN-US"}[mos threshold-value]{lang="EN-US"}[ ]{lang="EN-US"}***[upper-threshold lower-threshold]{lang="EN-US"}*[ \[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_951422997}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x763342034}

[[未创建监测]{style="font-family:宋体"}[Voice]{lang="EN-US"}]{#struct_0_13730_22192_175770165}[测试]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值的阈值告警组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1559146511}

[[Voice]{lang="EN-US"}]{#struct_0_13730_22192_x404002482}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x693631168}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1129467443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1375224489}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x329840723}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1707015714}[：阈值告警组的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-value]{lang="EN-US"}**]{#struct_0_13730_22192_x1056914269}[：指定阈值范围。]{style="font-family:宋体"}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_x1573817754}[：阈值上限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_x534828532}[：阈值下限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，且必须小于等于阈值上限。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_x314472463}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_541452653}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_1375290025}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_856700231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[实际的阈值下限（或阈值上限）为输入的阈值下限]{style="font-family:宋体"}]{#struct_0_13730_22192_x1861658999}[/100]{lang="EN-US"}[（或阈值上限]{style="font-family:宋体"}[/100]{lang="EN-US"}[），即如果输入的阈值下限和阈值上限分别为]{style="font-family:宋体"}[100]{lang="EN-US"}[、]{style="font-family:宋体"}[200]{lang="EN-US"}[，则]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值在]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[之间时，未超出阈值。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[阈值告警组创建后，不能再通过]{style="font-family:宋体"}]{#struct_0_13730_22192_x533844144}**[reaction]{lang="EN-US"}**[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_672338086}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1929177667}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测每次]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试的]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值，阈值上限为]{style="font-family:宋体"}[200]{lang="EN-US"}[，下限为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试的]{style="font-family:宋体"}[MOS]{lang="EN-US"}[值，若超出阈值范围，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_2121193267}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type voice]{lang="EN-US"}

[\[Sysname-nqa-admin-test-voice\] reaction 1 checked-element mos threshold-value 200 100 action-type trap-only]{lang="EN-US"}
:::

::: {#-794808683 .myid}
[]{#_Toc250551350}[]{#_Toc404796680}[]{#struct_0_13730_22192_x297827127}[]{#_Toc250551356}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element { owd-ds \| owd-sd }**

------------------------------------------------------------------------

[**[reaction checked-element ]{lang="EN-US"}**[{ **owd-ds** \| **owd-sd** }]{lang="EN-US"}]{#struct_0_13730_22192_1375879849}[命令用来创建监测单向时延的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_556472976}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x552266957}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_1595160129}[ ]{lang="EN-US"}[{ **owd-ds** \| **owd-sd** } ]{lang="EN-US"}**[threshold-value ]{lang="EN-US"}***[upper-threshold lower-threshold]{lang="EN-US"}*

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_1810913423}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_899130923}

[[未创建监测单向时延的阈值告警组。]{style="font-family:宋体"}]{#struct_0_13730_22192_1682790689}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1448310552}

[[UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_1375945385}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1472556615}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_744290234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_427246079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1985421441}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1477973115}[：阈值告警组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[owd-ds]{lang="EN-US"}**]{#struct_0_13730_22192_616294544}[：监测每个探测报文的从目的到源的单向时延。]{style="font-family:宋体"}

[**[owd-sd]{lang="EN-US"}**]{#struct_0_13730_22192_x1351385607}[：监测每个探测报文的从源到目的的单向时延。]{style="font-family:宋体"}

[**[threshold-value]{lang="EN-US"}**]{#struct_0_13730_22192_1375355562}[：指定阈值范围。]{style="font-family:宋体"}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_x1096510727}[：阈值上限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_658015882}[：阈值下限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，且必须小于等于阈值上限，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x368724815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[阈值告警组创建后，不能再通过]{style="font-family:宋体"}]{#struct_0_13730_22192_x788073516}**[reaction]{lang="EN-US"}**[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监测的对象是探测成功的报文，探测失败的报文不参与计数。]{style="font-family:宋体"}]{#struct_0_13730_22192_1599917931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监测单向时延的阈值告警组不支持触发动作，但可以通过相关显示命令]{lang="EN-US" style="font-family:宋体"}**[display nqa reaction counters]{lang="EN-US"}**]{#struct_0_13730_22192_x1673868255}[和]{lang="EN-US" style="font-family:宋体"}**[display nqa statistics]{lang="EN-US"}**[显示当前的监测结果。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x185372678}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1202365606}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测每个]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[探测报文的从目的到源的单向时延，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。收到探测报文的应答报文后，计算该探测报文从目的到源的单向时延，若超出阈值范围，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375421098}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] reaction 1 checked-element owd-ds threshold-value 50 5]{lang="EN-US"}
:::

::: {#1008326609 .myid}
[]{#_Toc404796681}[]{#struct_0_13730_22192_x1854095377}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element packet-loss**

------------------------------------------------------------------------

[**[reaction checked-element packet-loss]{lang="EN-US"}**]{#struct_0_13730_22192_1423180541}[命令用来创建监测每次测试中丢包数的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction ]{lang="EN-US"}**]{#struct_0_13730_22192_865405591}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1659096123}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_x2062965964}**[ ]{lang="EN-US"}[packet-loss ]{lang="EN-US"}[threshold-type]{lang="EN-US"}**[ **accumulate**]{lang="EN-US"}**[ ]{lang="EN-US"}***[accumulate-occurrences ]{lang="EN-US"}*[\[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_215020773}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x749737968}

[[未创建监测每次测试中丢包数的阈值告警组。]{style="font-family:宋体"}]{#struct_0_13730_22192_1375486634}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1201991718}

[[UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_84907871}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x621298095}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x133192314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x263402681}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1061685890}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1395549544}[：阈值告警组的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-type]{lang="EN-US"}**]{#struct_0_13730_22192_1375552170}[：指定阈值类型。]{style="font-family:宋体"}

[**[accumulate]{lang="EN-US"}**[ *accumulate-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_x294969963}[：每次测试中，累计的丢包数。对于]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15000]{lang="EN-US"}[；对于]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_1425214737}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_982475187}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_1399440937}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_49961002}

[[阈值告警组创建后，不能再通过]{style="font-family:宋体"}**[reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x190166964}[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_776015570}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x93224659}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测每次]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试的丢包数。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试中累计的丢包数，若达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[个，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375093418}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] reaction 1 checked-element packet-loss threshold-type accumulate 100 action-type trap-only]{lang="EN-US"}
:::

::: {#986799622 .myid}
[]{#_Toc404796682}[]{#struct_0_13730_22192_55093665}[]{#_Toc250551351}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element probe-duration**

------------------------------------------------------------------------

[**[reaction checked-element probe-duration]{lang="EN-US"}**]{#struct_0_13730_22192_x717619998}[命令用来创建监测探测持续时间的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x1479933148}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_455256813}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_x1623870197}**[ ]{lang="EN-US"}[probe-duration ]{lang="EN-US"}[threshold-type ]{lang="EN-US"}**[{ **accumulate** *accumulate-occurrences* \| **average** \| **consecutive** *consecutive-occurrences* } **threshold-value** *upper-threshold lower-threshold* \[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_1997206371}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375158954}

[[未创建监测探测持续时间的阈值告警组。]{style="font-family:宋体"}]{#struct_0_13730_22192_951881749}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x671377336}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo]{lang="EN-US"}]{#struct_0_13730_22192_x918664895}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_2001577298}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_203126100}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1484811331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1840947370}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_1375224490}[：阈值告警组的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-type]{lang="EN-US"}**]{#struct_0_13730_22192_x330430548}[：指定阈值类型。]{style="font-family:宋体"}

[**[accumulate]{lang="EN-US"}**[ *accumulate-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_1687478935}[：每次测试中，累计的探测持续时间超出阈值的探测次数。]{style="font-family:宋体"}*[accumulate-occurrences]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[average]{lang="EN-US"}**]{#struct_0_13730_22192_2013123096}[：每次测试中，探测持续时间的平均值。]{style="font-family:宋体"}

[**[consecutive]{lang="EN-US"}**[ *consecutive-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_x2085315975}[：测试组启动后，连续的探测持续时间超出阈值的探测次数。]{style="font-family:宋体"}*[consecutive-occurrences]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-value]{lang="EN-US"}**]{#struct_0_13730_22192_x2090766489}[：指定阈值范围。]{style="font-family:宋体"}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_691658206}[：阈值上限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_705166751}[：阈值下限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，且必须小于等于阈值上限，单位为毫秒。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_231070247}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_1375290026}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_856634695}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}[DNS]{lang="EN-US"}[测试不支持发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[，]{style="font-family:宋体"}[DNS]{lang="EN-US"}[测试类型视图下无此参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1076090532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[阈值告警组创建后，不能再通过]{style="font-family:宋体"}]{#struct_0_13730_22192_x687695664}**[reaction]{lang="EN-US"}**[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监测的对象是成功的探测，失败的探测不参与计数。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1532064716}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_2039392985}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1299386059}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测的持续时间，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试的平均探测持续时间，若超出阈值，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375879850}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction 1 checked-element probe-duration threshold-type average threshold-value 50 5 action-type trap-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_557062799}[创建编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测的持续时间，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试中累计的持续时间超出阈值的探测次数，若达到或超过]{style="font-family:宋体"}[10]{lang="EN-US"}[次，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_986278856}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction 2 checked-element probe-duration threshold-type accumulate 10 threshold-value 50 5 action-type trap-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_609012897}[创建编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测的持续时间，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次探测结束后，检查测试组启动以来连续的持续时间超出阈值的探测次数，若达到或超过]{style="font-family:宋体"}[10]{lang="EN-US"}[次，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x536635920}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction 3 checked-element probe-duration threshold-type consecutive 10 threshold-value 50 5 action-type trap-only]{lang="EN-US"}
:::

::: {#-173672993 .myid}
[]{#_Toc404796683}[]{#struct_0_13730_22192_832019403}[]{#_Toc250551352}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element probe-fail (for trap)**

------------------------------------------------------------------------

[**[reaction checked-element probe-fail]{lang="EN-US"}**]{#struct_0_13730_22192_1375945386}[命令用来创建监测探测失败次数的阈值告警组。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x1472491079}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x356107416}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element** **probe-fail** **threshold-type** { **accumulate** *accumulate-occurrences* \| **consecutive** *consecutive-occurrences* } \[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}]{#struct_0_13730_22192_x512572982}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_184019279}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x563193222}

[[未创建监测探测失败次数的阈值告警组。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1642955117}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x119491178}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo]{lang="EN-US"}]{#struct_0_13730_22192_1375355559}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1096969480}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1776004815}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_872941427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1228899691}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1352073831}[：阈值告警组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-type]{lang="EN-US"}**]{#struct_0_13730_22192_x423449281}[：指定阈值类型。]{style="font-family:宋体"}

[**[accumulate]{lang="EN-US"}**[ *accumulate-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_x1645077805}[：一次测试中，累计的探测失败次数。]{style="font-family:宋体"}*[accumulate-occurrences]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[consecutive]{lang="EN-US"}**[ *consecutive-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_1375421095}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动以来，连续的探测失败次数。]{style="font-family:宋体"}*[consecutive-occurrences]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_x1854816273}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_x2094459582}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_x1173355513}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}[DNS]{lang="EN-US"}[测试不支持发送]{style="font-family:宋体"}[trap]{lang="EN-US"}[，]{style="font-family:宋体"}[DNS]{lang="EN-US"}[测试类型视图下无此参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x658315901}

[[阈值告警组创建后，不能再通过]{style="font-family:宋体"}**[reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x21386432}[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1264690575}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_2084721539}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测的失败次数。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试中累计的探测失败次数，若达到或超过]{style="font-family:宋体"}[10]{lang="EN-US"}[次，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375486631}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction 1 checked-element probe-fail threshold-type accumulate 10 action-type trap-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1201795110}[创建编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测的失败次数。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次探测结束后，检查测试组启动以来连续的探测失败次数，若达到或超过]{style="font-family:宋体"}[10]{lang="EN-US"}[次，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1502647663}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction 2 checked-element probe-fail threshold-type consecutive 10 action-type trap-only]{lang="EN-US"}
:::

::: {#1233992268 .myid}
[]{#_Toc404796684}[]{#struct_0_13730_22192_1042755435}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element probe-fail (for trigger)**

------------------------------------------------------------------------

[**[reaction checked-element probe-fail]{lang="EN-US"}**]{#struct_0_13730_22192_x1214061145}[命令用来建立联动项，对当前所在测试组中的探测进行监测，当连续探测失败次数达到阈值时，就触发其他模块联动。]{style="font-family:宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_x1348381109}[命令用来删除指定的联动项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1266600402}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_1375552167}**[ ]{lang="EN-US"}[probe-fail threshold-type]{lang="EN-US"}[ ]{lang="EN-US"}[consecutive]{lang="EN-US"}**[ ]{lang="EN-US"}*[consecutive-occurrences]{lang="EN-US"}*[ **action-type** **trigger-only**]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x294904428}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1794639628}

[[未配置联动项。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1964548807}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x960390240}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo]{lang="EN-US"}]{#struct_0_13730_22192_x1469767449}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_323689100}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1610377578}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1266206239}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375093415}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_55290273}[：联动项序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-type]{lang="EN-US"}**]{#struct_0_13730_22192_550088452}[：指定门限类型。]{style="font-family:宋体"}

[**[consecutive]{lang="EN-US"}**[ *consecutive-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_x1456544789}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动以来，连续的探测失败次数。]{style="font-family:宋体"}*[consecutive-occurrences]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_295119460}[：触发的动作类型。]{style="font-family:宋体"}

[**[trigger-only]{lang="EN-US"}**]{#struct_0_13730_22192_x1426111037}[：条件满足时，触发其它模块联动。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_577456333}

[[联动项创建后，不能再通过]{style="font-family:宋体"}**[reaction]{lang="EN-US"}**]{#struct_0_13730_22192_183212291}[命令修改该联动项的内容。若要修改联动项的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除联动项，再利用新的参数创建联动项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375158951}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_951554069}[建立序号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的联动项，连续探测失败]{style="font-family:宋体"}[3]{lang="EN-US"}[次，触发其他模块联动。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1559616864}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type tcp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-tcp\] reaction 1 checked-element probe-fail threshold-type consecutive 3 action-type trigger-only]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1785801427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[track]{lang="EN-US"}**]{#struct_0_13730_22192_1888873222}[（可靠性命令参考]{style="font-family:
宋体"}[/Track]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#494297214 .myid}
[]{#_Toc404796685}[]{#struct_0_13730_22192_789774801}[]{#_Toc250551354}

**NQA \-- NQA客户端配置命令 \-- reaction checked-element rtt**

------------------------------------------------------------------------

[**[reaction checked-element rtt]{lang="EN-US"}**]{#struct_0_13730_22192_738826635}[命令用来创建监测报文往返时延的阈值告警组。]{style="font-family:
宋体"}

[**[undo reaction]{lang="EN-US"}**]{#struct_0_13730_22192_1375224487}[命令用来删除指定的阈值告警组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x330758227}

[**[reaction]{lang="EN-US"}**[ *item-number* **checked-element**]{lang="EN-US"}]{#struct_0_13730_22192_99911568}**[ ]{lang="EN-US"}[rtt ]{lang="EN-US"}[threshold-type ]{lang="EN-US"}**[{ **accumulate** *accumulate-occurrences* \| **average** } **threshold-value** *upper-threshold lower-threshold* \[ **action-type** { **none** \| **trap-only** } \]]{lang="EN-US"}

[**[undo reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x958713073}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2008640294}

[[未创建监测报文往返时延的阈值告警组。]{style="font-family:宋体"}]{#struct_0_13730_22192_1443139953}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1133093585}

[[UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_1552662120}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1155218326}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1375290023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_856831303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x894841979}

[*[item-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1877954037}[：阈值告警组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold-type]{lang="EN-US"}**]{#struct_0_13730_22192_x179211173}[：指定阈值类型。]{style="font-family:宋体"}

[**[accumulate]{lang="EN-US"}**[ *accumulate-occurrences*]{lang="EN-US"}]{#struct_0_13730_22192_1108315451}[：每次测试中，累计的]{style="font-family:宋体"}[RTT]{lang="EN-US"}[超出阈值的报文个数。对于]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15000]{lang="EN-US"}[；对于]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[average]{lang="EN-US"}**]{#struct_0_13730_22192_634612497}[：每次测试中，报文往返时间的平均值。]{style="font-family:宋体"}

[**[threshold-value]{lang="EN-US"}**]{#struct_0_13730_22192_2111918981}[：指定阈值范围。]{style="font-family:宋体"}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_1375879847}[：阈值上限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_13730_22192_557390480}[：阈值下限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，且必须小于等于阈值上限，单位为毫秒。]{style="font-family:宋体"}

[**[action-type]{lang="EN-US"}**]{#struct_0_13730_22192_1261172071}[：触发的动作类型，缺省动作类型为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_13730_22192_405355750}[：只在显示信息中记录监测结果，]{style="font-family:宋体"}[不向网管发送]{style="font-family:宋体"}[T]{lang="EN-US"}[rap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[trap-only]{lang="EN-US"}**]{#struct_0_13730_22192_2034687988}[：条件满足时，在显示信息中记录监测结果的同时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2087408893}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[阈值告警组创建后，不能再通过]{style="font-family:宋体"}]{#struct_0_13730_22192_337908569}**[reaction]{lang="EN-US"}**[命令修改该阈值告警组的内容。若要修改阈值告警组的内容，则需要先通过]{style="font-family:宋体"}**[undo reaction]{lang="EN-US"}**[命令用来删除阈值告警组，再利用新的参数创建阈值告警组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[监测的对象是探测成功的报文，探测失败的报文不参与计数。]{style="font-family:宋体"}]{#struct_0_13730_22192_938379869}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375945383}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1472163399}[创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的阈值告警组，监测]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[探测报文的往返时间，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试的平均报文往返时间，若超出阈值，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1769019782}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] reaction 1 checked-element rtt threshold-type average threshold-value 50 5 action-type trap-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x199810170}[创建编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的阈值告警组，监测每个]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[探测报文的往返时间，阈值上限为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，下限为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组启动前，初始的阈值状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[。每次测试结束后，检查本次测试中累计的]{style="font-family:宋体"}[RTT]{lang="EN-US"}[超出阈值的报文个数，若达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[个，阈值状态置为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[；反之，置为]{style="font-family:宋体"}[below-threshold]{lang="EN-US"}[。当阈值状态改变时，向网管发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1351604570}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-jitter\] reaction 1 checked-element rtt threshold-type accumulate 100 threshold-value 50 5 action-type trap-only]{lang="EN-US"}
:::

::: {#-495341763 .myid}
[]{#_Toc404796686}[]{#struct_0_13730_22192_1758800377}

**NQA \-- NQA客户端配置命令 \-- reaction trap**

------------------------------------------------------------------------

[**[reaction trap]{lang="EN-US"}**]{#struct_0_13730_22192_x1381424113}[命令用来配置在指定条件下向网管服务器发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[undo reaction trap]{lang="EN-US"}**]{#struct_0_13730_22192_1375355560}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1096379655}

[**[reaction trap ]{lang="EN-US"}**[{ **path-change** \| **probe-failure** *consecutive-probe-failures* \| **test-complete** \| **test-failure** \[ *cumulate-probe-failures* \] }]{lang="EN-US"}]{#struct_0_13730_22192_970531983}

[**[undo reaction trap ]{lang="EN-US"}**[{ **probe-failure** \| **test-complete** \| **test-failure** }]{lang="EN-US"}]{#struct_0_13730_22192_1686592388}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x370635360}

[[不向网管服务器发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_13730_22192_1101357204}[消息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x7437858}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1605643069}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375421096}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1855012881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x379519393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_991422710}

[**[path-change]{lang="EN-US"}**]{#struct_0_13730_22192_1965537693}[：当进行]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[类型测试时，在配置了]{style="font-family:宋体"}**[frequency]{lang="EN-US"}**[命令后进行连续测试后，如果检测到当前路径相对于上一次测试路径发生变化，则设备发送一次]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[probe-failure ]{lang="EN-US"}***[consecutive-probe-failures]{lang="EN-US"}*]{#struct_0_13730_22192_x1935173750}[：每次探测结束后，计算本次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试中探测连续失败的次数，如果连续失败次数大于或等于]{style="font-family:宋体"}*[consecutive-probe-failures]{lang="EN-US"}*[，则向网管服务器发送探测失败的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。一次测试中，可能发送多次]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}*[consecutive-probe-failures]{lang="EN-US"}*[为一次测试中连续探测失败的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[test-complete]{lang="EN-US"}**]{#struct_0_13730_22192_118556405}[：对于非]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[类型测试，当测试完成时发送测试完成的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。对于]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[类型测试，测试出到达目的设备的路径后，发送测试完成的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[test-failure]{lang="EN-US"}**[ *cumulate-probe-failures*]{lang="EN-US"}]{#struct_0_13730_22192_1141721400}[：对于非]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[类型测试，一次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试结束后，计算本次]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试中探测失败的累计次数，如果累计失败次数大于或等于]{style="font-family:宋体"}*[cumulate-probe-failures]{lang="EN-US"}*[，则向网管服务器发送测试失败的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}*[cumulate-probe-failures]{lang="EN-US"}*[为一次测试中累计探测失败的次数，为必须输入的参数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。对于]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[类型测试，只要未能测试出到达目的地的路径，就发送一次]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。用户不能输入参数]{style="font-family:宋体"}*[cumulate-probe-failures]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1432664080}

[[UDP-jitter ]{lang="EN-US"}]{#struct_0_13730_22192_x1862778251}[和]{style="font-family:宋体"}[Voice]{lang="EN-US"}[测试只支持]{style="font-family:宋体"}**[reaction trap test-complete]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_1965472157}[测试支持]{style="font-family:宋体"}**[reaction trap path-change]{lang="EN-US"}**[，]{style="font-family:宋体"}**[reaction trap test-complete]{lang="EN-US"}**[和]{style="font-family:宋体"}**[reaction trap test-failure]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375486632}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1201860646}[配置]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[测试中连续探测失败次数大于或等于]{style="font-family:宋体"}[5]{lang="EN-US"}[次时，发送探测失败的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x291233050}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction trap probe-failure 5]{lang="EN-US"}
:::

::: {#2021511427 .myid}
[]{#_Toc404796687}[]{#struct_0_13730_22192_64604077}[]{#_Toc330975614}[]{#_Toc322348110}[]{#_Toc324405619}

**NQA \-- NQA客户端配置命令 \-- reaction trigger probe-fail**

------------------------------------------------------------------------

[**[undo reaction trigger probe-fail]{lang="EN-US"}**]{#struct_0_13730_22192_438996993}[命令]{style="font-family:宋体"}**[     ]{lang="EN-US"}**[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1111240938}

[**[reaction trigger probe-fail]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_13730_22192_1375552168}

[**[undo reaction trigger probe-fail]{lang="EN-US"}**]{#struct_0_13730_22192_x295494252}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1411909484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2143895412}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1696534876}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_296635918}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_105256563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1375093416}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_55224737}

[*[count]{lang="EN-US"}*]{#struct_0_13730_22192_575897972}*[：]{style="font-family:宋体"}*[连续探测失败的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x242007228}

[[外部特性调用]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1362769563}[模板后进行相应的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试，使用此命令可以设定节点失效的连续测试失败次数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x240600047}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1252519532}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置确定节点失效需要连续探测失败]{style="font-family:宋体"}[5]{lang="EN-US"}[次。当连续探测失败的次数达到]{style="font-family:宋体"}[5]{lang="EN-US"}[次时，]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端把探测失败的消息发送给外部特性，使外部特性能利用]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试的结果进行相应处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1311229650}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] reaction trigger probe-fail 5]{lang="EN-US"}
:::

::: {#-348638170 .myid}
[]{#_Toc404796688}[]{#struct_0_13730_22192_1375158952}[]{#_Toc330975615}[]{#_Toc322348111}[]{#_Toc324405620}

**NQA \-- NQA客户端配置命令 \-- reaction trigger probe-pass**

------------------------------------------------------------------------

[**[undo reaction trigger probe-pass]{lang="EN-US"}**]{#struct_0_13730_22192_x1963556472}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x845476177}

[**[reaction trigger probe-pass]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_13730_22192_x832023119}

[**[undo reaction trigger probe-pass]{lang="EN-US"}**]{#struct_0_13730_22192_2008110665}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x293267710}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375224488}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x329906259}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_224204932}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_514281674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1705473476}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1845449015}

[*[count]{lang="EN-US"}*]{#struct_0_13730_22192_1313146745}*[：]{style="font-family:宋体"}*[连续探测成功的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_672722496}

[[外部特性调用]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1274168242}[模板后进行相应的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试，使用此命令可以设定节点有效的连续探测成功次数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1375290024}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_856765767}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置确定节点有效需要连续探测成功]{style="font-family:宋体"}[5]{lang="EN-US"}[次。当连续探测成功的次数达到]{style="font-family:宋体"}[5]{lang="EN-US"}[次时，]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端把探测成功的消息发送给外部特性，使外部特性能利用]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试的结果进行相应处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_478322024}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] reaction trigger probe-pass 5]{lang="EN-US"}
:::

::: {#1299051592 .myid}
[]{#_Toc404796689}[]{#struct_0_13730_22192_2032755372}[]{#_Toc161908927}[]{#_Toc161908928}[]{#_Toc161908929}[]{#_Toc161908930}[]{#_Toc161908931}[]{#_Toc161908932}[]{#_Toc161908933}[]{#_Toc161908934}[]{#_Toc161908935}[]{#_Toc161908936}[]{#_Toc161908937}[]{#_Toc161908938}[]{#_Toc161908939}[]{#_Toc161908940}[]{#_Toc161908941}[]{#_Toc161908942}[]{#_Toc161908944}[]{#_Toc158457656}[]{#_Toc161908945}[]{#_Toc158457657}[]{#_Toc161908946}[]{#_Toc158457658}[]{#_Toc161908947}[]{#_Toc158457659}[]{#_Toc161908948}[]{#_Toc158457660}[]{#_Toc161908949}[]{#_Toc158457661}[]{#_Toc161908950}[]{#_Toc158457662}[]{#_Toc161908951}[]{#_Toc158457663}[]{#_Toc161908952}[]{#_Toc158457664}[]{#_Toc161908953}[]{#_Toc158457665}[]{#_Toc161908954}[]{#_Toc158457666}[]{#_Toc161908955}[]{#_Toc158457667}[]{#_Toc161908956}[]{#_Toc158457668}[]{#_Toc161908957}[]{#_Toc158457669}[]{#_Toc161908958}[]{#_Toc158457670}[]{#_Toc161908959}[]{#_Toc158457671}[]{#_Toc161908960}[]{#_Toc158457672}[]{#_Toc161908961}[]{#_Toc158457673}[]{#_Toc161908962}[]{#_Toc158457675}[]{#_Toc161908964}[]{#_Toc154997940}[]{#_Toc154997941}[]{#_Toc154997942}[]{#_Toc154997943}[]{#_Toc154997944}[]{#_Toc154997945}[]{#_Toc154997946}[]{#_Toc154997947}[]{#_Toc154997948}[]{#_Toc154997949}[]{#_Toc154997950}[]{#_Toc154997951}[]{#_Toc154997952}[]{#_Toc154997953}[]{#_Toc154997954}[]{#_Toc154997956}[]{#_Toc154997957}[]{#_Toc145488671}[]{#_Toc144546231}[]{#_Toc144546232}

**NQA \-- NQA客户端配置命令 \-- resolve-target**

------------------------------------------------------------------------

[**[resolve-target]{lang="EN-US"}**]{#struct_0_13730_22192_x1600077447}[命令用来配置要解析的域名。]{style="font-family:宋体"}

[**[undo resolve-target]{lang="EN-US"}**]{#struct_0_13730_22192_x1858145573}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_482519622}

[**[resolve-target ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_13730_22192_1375879848}

[**[undo resolve-target]{lang="EN-US"}**]{#struct_0_13730_22192_556538512}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_2127268335}

[[没有配置要解析的域名。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1818965004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_424041289}

[[DNS]{lang="EN-US"}]{#struct_0_13730_22192_348997146}[测试类型视图]{style="font-family:宋体"}

[[DNS]{lang="EN-US"}]{#struct_0_13730_22192_1581310570}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x812157035}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x46315852}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1375945384}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1472622151}

[*[domain-name]{lang="EN-US"}*]{#struct_0_13730_22192_717198492}[：要解析的域名，]{style="font-family:宋体"}[由"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成（如]{style="font-family:宋体"}[aabbcc.com]{lang="EN-US"}[），每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符，区分大小写。字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["及"]{style="font-family:宋体"}[\_]{lang="EN-US"}["，不能出现连续"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1077088552}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x172135952}[配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[测试要解析的域名为]{style="font-family:宋体"}[domain1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_373383114}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type dns]{lang="EN-US"}

[\[Sysname-nqa-admin-test-dns\] resolve-target domain1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_107779729}[在]{style="font-family:宋体"}[DNS]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试要解析的域名为]{style="font-family:宋体"}[domain1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353527792}

[\[Sysname\] nqa template dns dnstplt]{lang="EN-US"}

[\[Sysname-nqatplt-dns-dnstplt\] resolve-target domain1]{lang="EN-US"}
:::

::: {#-195506916 .myid}
[]{#_Toc404796690}[]{#struct_0_13730_22192_169103589}[]{#_Toc330975617}

**NQA \-- NQA客户端配置命令 \-- resolve-type**

------------------------------------------------------------------------

[**[resolve-type]{lang="EN-US"}**]{#struct_0_13730_22192_1739241078}[命令用来配置域名解析类型。]{style="font-family:宋体"}

[**[undo resolve-type]{lang="EN-US"}**]{#struct_0_13730_22192_x713383740}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x363432826}

[**[resolve-type ]{lang="EN-US"}**[{ **A** \| **AAAA** }]{lang="EN-US"}]{#struct_0_13730_22192_x1070527876}

[**[undo resolve-type]{lang="EN-US"}**]{#struct_0_13730_22192_x1062659818}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1514126419}

[[域名解析类型为]{style="font-family:宋体"}**[A]{lang="EN-US"}**]{#struct_0_13730_22192_x1353462256}[类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1184473464}

[[DNS]{lang="EN-US"}]{#struct_0_13730_22192_x789707903}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1951161635}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x588155825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_911313775}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1922852946}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353396720}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1929508194}[在]{style="font-family:宋体"}[DNS]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置测试的域名解析类型为]{style="font-family:宋体"}**[AAAA]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x338831330}

[\[Sysname\] nqa template dns dnstplt]{lang="EN-US"}

[\[Sysname-nqatplt-dns-dnstplt\] resolve-type AAAA]{lang="EN-US"}
:::

::: {#-1068800216 .myid}
[]{#_Toc404796691}[]{#struct_0_13730_22192_741830269}

**NQA \-- NQA客户端配置命令 \-- route-option bypass-route**

------------------------------------------------------------------------

[**[route-option bypass-route]{lang="EN-US"}**]{#struct_0_13730_22192_x438500847}[命令用来启动路由表旁路功能，探测直连目的地的连通情况。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **route-option bypass-route**]{lang="EN-US"}]{#struct_0_13730_22192_x1173953928}[命令用来关闭路由表旁路功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1425126730}

[**[route-option bypass-route]{lang="EN-US"}**]{#struct_0_13730_22192_x1353331184}

[**[undo route-option bypass-route]{lang="EN-US"}**]{#struct_0_13730_22192_x1126094010}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1950743027}

[[路由表旁路功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13730_22192_1989384884}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x237549063}

[[DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x460451149}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x899181085}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1012748033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1353789936}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1536286657}

[[启动该功能后，将不进行路由查找，而直接将报文发送到直连网络的目的地。]{style="font-family:宋体"}]{#struct_0_13730_22192_744565803}

[[在设备上启动该功能后，设备转发探测报文可以经过的最大跳数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_13730_22192_157316304}[，]{style="font-family:宋体"}**[ttl]{lang="EN-US"}**[命令设置的跳数不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_287886851}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1278639449}[启动路由旁路功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_863913890}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] route-option bypass-route]{lang="EN-US"}
:::

::: {#1179169449 .myid}
[]{#_Toc404796692}[]{#struct_0_13730_22192_1783681946}

**NQA \-- NQA客户端配置命令 \-- source interface**

------------------------------------------------------------------------

[**[source interface]{lang="EN-US"}**]{#struct_0_13730_22192_x1353724400}[命令用来使用指定接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为测试中探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo source interface]{lang="EN-US"}**]{#struct_0_13730_22192_1469659672}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1790368954}

[**[source interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13730_22192_1304858321}

[**[undo source interface]{lang="EN-US"}**]{#struct_0_13730_22192_1952368572}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1621636597}

[[未指定测试中探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_x384712231}[地址，以报文发送接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为探测报文中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_640244698}

[[ICMP-echo/UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_1414459167}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_300504723}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_741374262}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_749863330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1806966736}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13730_22192_x707235374}[：探测报文源接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1568000063}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source ip]{lang="EN-US"}**]{#struct_0_13730_22192_2119228392}[命令]{lang="EN-US" style="font-family:宋体"}[或]{style="font-family:宋体"}**[source ipv6]{lang="EN-US"}**[命令]{style="font-family:宋体"}[和]{lang="EN-US" style="font-family:宋体"}**[source interface]{lang="EN-US"}**[命令是互相覆盖的关系，新的配置会覆盖已有配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令指定的接口必须处于]{style="font-family:宋体"}]{#struct_0_13730_22192_x1353593328}[UP]{lang="EN-US"}[状态，否则探测将会失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1352492490}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13730_22192_x1835797226}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1433141979}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1051352988}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] source interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_166444147}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x2080978975}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] source interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13730_22192_x1353003504}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_194968719}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1716716396}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] source interface vlan-interface 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_2033507210}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1548921579}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] source interface vlan-interface 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x192170162}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source ip]{lang="EN-US"}**]{#struct_0_13730_22192_1403594140}
:::

::: {#2050190574 .myid}
[]{#_Toc404796693}[]{#struct_0_13730_22192_x1352937968}

**NQA \-- NQA客户端配置命令 \-- source ip**

------------------------------------------------------------------------

[**[source ip]{lang="EN-US"}**]{#struct_0_13730_22192_x337005641}[命令用来配置测试操作中探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo source ip]{lang="EN-US"}**]{#struct_0_13730_22192_x195454300}[命令用来取消已配置的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即以报文发送接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为探测报文中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_481818769}

[**[source ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_13730_22192_x37264285}

[**[undo]{lang="EN-US"}**[ **source ip**]{lang="EN-US"}]{#struct_0_13730_22192_x534254598}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1295978365}

[[未配置测试操作中探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13730_22192_x2123976016}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353527791}

[[DLSw/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/DHCP/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1396980352}[测试类型视图]{style="font-family:宋体"}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1932158639}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_1002943292}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1661972017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_137051097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_363017311}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13730_22192_832536851}[：测试操作中探测报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1077284191}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}]{#struct_0_13730_22192_x1353462255}[/UDP-tracert]{lang="EN-US"}[测试类型，]{lang="EN-US" style="font-family:宋体"}**[source ip]{lang="EN-US"}**[命令和]{lang="EN-US" style="font-family:宋体"}**[source interface]{lang="EN-US"}**[命令是互相覆盖的关系，新的配置会覆盖已有配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source ip]{lang="EN-US"}**]{#struct_0_13730_22192_1544409891}[命令配置的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须是设备上接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，且接口为]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，否则测试将会失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_865274520}[NQA]{lang="EN-US"}[模板类型来说，当源地址类型和目的地址类型不一致时，以目的地址类型为准，进行该类型的报文探测，此时源地址的配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_486038733}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1292865820}[配置]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[探测报文中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1068720983}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] source ip 10.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1337761388}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测报文中的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353396719}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] source ip 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_719720149}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source interface]{lang="EN-US"}**]{#struct_0_13730_22192_1193593425}
:::

::: {#1781702182 .myid}
[]{#_Toc404796694}[]{#struct_0_13730_22192_1004272183}[]{#_Toc330975619}

**NQA \-- NQA客户端配置命令 \-- source ipv6**

------------------------------------------------------------------------

[**[source ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_1150892782}[命令用来配置测试操作中探测报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo source ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_x10601765}[命令用来取消已配置的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，即以报文发送接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为探测报文中的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_786517578}

[**[source ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_13730_22192_x17202890}

[**[undo]{lang="EN-US"}**[ **source ipv6**]{lang="EN-US"}]{#struct_0_13730_22192_x1353331183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1885608897}

[[未配置测试操作中探测报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13730_22192_613400403}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1526782675}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_2119370205}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1189480447}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1099604064}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x765908271}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353789935}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13730_22192_1939571184}[：测试操作中探测报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2120704027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}]{#struct_0_13730_22192_x216244413}[测试类型，]{lang="EN-US" style="font-family:宋体"}**[source ip]{lang="EN-US"}[v6]{lang="EN-US"}**[命令和]{lang="EN-US" style="font-family:宋体"}**[source interface]{lang="EN-US"}**[命令是互相覆盖的关系，新的配置会覆盖已有配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source ipv6]{lang="EN-US"}**]{#struct_0_13730_22192_205825126}[命令配置的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址必须是设备上接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，且接口为]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，否则测试将会失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13730_22192_865995416}[NQA]{lang="EN-US"}[模板类型来说，当源地址类型和目的地址类型不一致时，以目的地址类型为准，进行该类型的报文探测，此时源地址的配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1525570643}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1575660145}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测报文中的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1901642286}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] source ipv6 1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353724399}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source interface]{lang="EN-US"}**]{#struct_0_13730_22192_x1614995292}
:::

::: {#-1015706045 .myid}
[]{#_Toc404796695}[]{#struct_0_13730_22192_x1106861360}

**NQA \-- NQA客户端配置命令 \-- source port**

------------------------------------------------------------------------

[**[source port]{lang="EN-US"}**]{#struct_0_13730_22192_x733300893}[命令用来配置测试操作中探测报文的源端口号。]{style="font-family:宋体"}

[**[undo source port]{lang="EN-US"}**]{#struct_0_13730_22192_x639180216}[命令用来取消已配置的源端口号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1702960626}

[**[source port ]{lang="FR"}**]{#struct_0_13730_22192_2086774240}*[port-number]{lang="FR"}*

[**[undo]{lang="FR"}**]{#struct_0_13730_22192_1210072386}[ **source port**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353658863}

[[未指定源端口号。]{style="font-family:宋体"}]{#struct_0_13730_22192_x2072148272}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_457394496}

[[SNMP/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1068830428}[测试类型视图]{style="font-family:宋体"}

[[DNS]{lang="EN-US"}]{#struct_0_13730_22192_2123159371}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_363282538}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x2016558047}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1705555123}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_736146450}

[*[port-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1353593327}[：探测报文的源端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_213591451}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1976055012}[配置探测报文的源端口号为]{style="font-family:宋体"}[8000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_592876247}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type udp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-udp-echo\] source port 8000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1256262840}[在]{style="font-family:宋体"}[DNS]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测报文的源端口号为]{style="font-family:宋体"}[8000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1842004959}

[\[Sysname\] nqa template dns dnstplt]{lang="EN-US"}

[\[Sysname-nqatplt-dns-dnstplt\] source port 8000]{lang="EN-US"}
:::

::: {#986500697 .myid}
[]{#_Toc404796696}[]{#struct_0_13730_22192_x1353003503}[]{#_Toc199826519}

**NQA \-- NQA客户端配置命令 \-- statistics hold-time**

------------------------------------------------------------------------

[**[statistics hold-time]{lang="EN-US"}**]{#struct_0_13730_22192_598253246}[命令用来配置统计组的保留时间。]{style="font-family:宋体"}

[**[undo statistics hold-time]{lang="EN-US"}**]{#struct_0_13730_22192_640056735}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_723280748}

[**[statistics hold-time ]{lang="EN-US"}***[hold-time]{lang="EN-US"}*]{#struct_0_13730_22192_236691140}

[**[undo statistics hold-time]{lang="EN-US"}**]{#struct_0_13730_22192_x1748321635}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x2001828361}

[[统计组的保留时间为]{style="font-family:宋体"}[120]{lang="EN-US"}]{#struct_0_13730_22192_x1706288770}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x275606597}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1352937967}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x384059808}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1258089527}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x100119400}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1558841938}

[*[hold-time]{lang="EN-US"}*]{#struct_0_13730_22192_x2047692944}[：]{style="font-family:宋体"}[统计组的保留时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x303351066}

[[统计组具有老化功能。统计组保存一定时间后将被删除，以便记录新的统计组信息。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1409849950}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353527794}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x637465465}[配置统计组的保留时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_124296081}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] statistics hold-time 3]{lang="EN-US"}
:::

::: {#-31996454 .myid}
[]{#_Toc199826548}[]{#_Toc404796697}[]{#struct_0_13730_22192_1773093552}[]{#_Toc199817475}[]{#_Toc199824930}[]{#_Toc199825534}[]{#_Toc199825863}[]{#_Toc199826192}[]{#_Toc199826520}[]{#_Toc199817476}[]{#_Toc199824931}[]{#_Toc199825535}[]{#_Toc199825864}[]{#_Toc199826193}[]{#_Toc199826521}[]{#_Toc199817477}[]{#_Toc199824932}[]{#_Toc199825536}[]{#_Toc199825865}[]{#_Toc199826194}[]{#_Toc199826522}[]{#_Toc199817478}[]{#_Toc199824933}[]{#_Toc199825537}[]{#_Toc199825866}[]{#_Toc199826195}[]{#_Toc199826523}[]{#_Toc199817479}[]{#_Toc199824934}[]{#_Toc199825538}[]{#_Toc199825867}[]{#_Toc199826196}[]{#_Toc199826524}[]{#_Toc199817480}[]{#_Toc199824935}[]{#_Toc199825539}[]{#_Toc199825868}[]{#_Toc199826197}[]{#_Toc199826525}[]{#_Toc199817481}[]{#_Toc199824936}[]{#_Toc199825540}[]{#_Toc199825869}[]{#_Toc199826198}[]{#_Toc199826526}[]{#_Toc199817483}[]{#_Toc199824938}[]{#_Toc199825542}[]{#_Toc199825871}[]{#_Toc199826200}[]{#_Toc199826528}[]{#_Toc199817484}[]{#_Toc199824939}[]{#_Toc199825543}[]{#_Toc199825872}[]{#_Toc199826201}[]{#_Toc199826529}[]{#_Toc199817485}[]{#_Toc199824940}[]{#_Toc199825544}[]{#_Toc199825873}[]{#_Toc199826202}[]{#_Toc199826530}[]{#_Toc199817486}[]{#_Toc199824941}[]{#_Toc199825545}[]{#_Toc199825874}[]{#_Toc199826203}[]{#_Toc199826531}[]{#_Toc199817487}[]{#_Toc199824942}[]{#_Toc199825546}[]{#_Toc199825875}[]{#_Toc199826204}[]{#_Toc199826532}[]{#_Toc199817488}[]{#_Toc199824943}[]{#_Toc199825547}[]{#_Toc199825876}[]{#_Toc199826205}[]{#_Toc199826533}[]{#_Toc199817489}[]{#_Toc199824944}[]{#_Toc199825548}[]{#_Toc199825877}[]{#_Toc199826206}[]{#_Toc199826534}[]{#_Toc199817490}[]{#_Toc199824945}[]{#_Toc199825549}[]{#_Toc199825878}[]{#_Toc199826207}[]{#_Toc199826535}[]{#_Toc199817491}[]{#_Toc199824946}[]{#_Toc199825550}[]{#_Toc199825879}[]{#_Toc199826208}[]{#_Toc199826536}[]{#_Toc199817492}[]{#_Toc199824947}[]{#_Toc199825551}[]{#_Toc199825880}[]{#_Toc199826209}[]{#_Toc199826537}[]{#_Toc199817493}[]{#_Toc199824948}[]{#_Toc199825552}[]{#_Toc199825881}[]{#_Toc199826210}[]{#_Toc199826538}[]{#_Toc199817494}[]{#_Toc199824949}[]{#_Toc199825553}[]{#_Toc199825882}[]{#_Toc199826211}[]{#_Toc199826539}[]{#_Toc199817495}[]{#_Toc199824950}[]{#_Toc199825554}[]{#_Toc199825883}[]{#_Toc199826212}[]{#_Toc199826540}[]{#_Toc199817496}[]{#_Toc199824951}[]{#_Toc199825555}[]{#_Toc199825884}[]{#_Toc199826213}[]{#_Toc199826541}[]{#_Toc199817497}[]{#_Toc199824952}[]{#_Toc199825556}[]{#_Toc199825885}[]{#_Toc199826214}[]{#_Toc199826542}[]{#_Toc199817499}[]{#_Toc199824954}[]{#_Toc199825558}[]{#_Toc199825887}[]{#_Toc199826216}[]{#_Toc199826544}[]{#_Toc199817500}[]{#_Toc199824955}[]{#_Toc199825559}[]{#_Toc199825888}[]{#_Toc199826217}[]{#_Toc199826545}[]{#_Toc199817501}[]{#_Toc199824956}[]{#_Toc199825560}[]{#_Toc199825889}[]{#_Toc199826218}[]{#_Toc199826546}

**NQA \-- NQA客户端配置命令 \-- statistics interval**

------------------------------------------------------------------------

[**[statistics interval]{lang="EN-US"}**]{#struct_0_13730_22192_1491052966}[命令用来配置对测试结果进行统计的时间间隔。]{style="font-family:宋体"}

[**[undo statistics interval]{lang="EN-US"}**]{#struct_0_13730_22192_x1213042819}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1213906241}

[**[statistics interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_13730_22192_x1847005896}

[**[undo statistics interval]{lang="EN-US"}**]{#struct_0_13730_22192_x1353462258}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1634812158}

[[对测试结果进行统计的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_13730_22192_391140503}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1428052725}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1645929192}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x273235005}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_419389358}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1333533591}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353396722}

[*[interval]{lang="EN-US"}*]{#struct_0_13730_22192_x1202659688}[：对测试结果进行统计的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[35791394]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x840802232}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_2135042205}[将统计时间间隔内完成的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试归为一组，计算该组测试结果的统计值，这些统计值构成一个统计组。通过]{style="font-family:宋体"}**[display nqa statistics]{lang="EN-US"}**[命令可以显示该统计组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1172704816}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_308240253}[配置对测试结果进行统计的时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1610381765}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] statistics interval 2]{lang="EN-US"}
:::

::: {#1131847860 .myid}
[]{#_Toc404796698}[]{#struct_0_13730_22192_x1600919609}

**NQA \-- NQA客户端配置命令 \-- statistics max-group**

------------------------------------------------------------------------

[**[statistics max-group]{lang="EN-US"}**]{#struct_0_13730_22192_x1353331186}[命令用来配置能够保留的最大统计组个数。]{style="font-family:宋体"}

[**[undo statistics max-group]{lang="EN-US"}**]{#struct_0_13730_22192_2006073872}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_279487189}

[**[statistics max-group ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_13730_22192_x1066215905}

[**[undo statistics max-group]{lang="EN-US"}**]{#struct_0_13730_22192_77396779}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1833346753}

[[能够保留的最大统计组个数为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_13730_22192_x1102435323}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x525379705}

[[DHCP/DLSw/DNS/FTP/HTTP/ICMP-echo/Path-jitter/SNMP/TCP/UDP-echo/UDP-jitter/Voice]{lang="EN-US"}]{#struct_0_13730_22192_x1353789938}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1595881225}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1372652920}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1801199097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x452248265}

[*[number]{lang="EN-US"}*]{#struct_0_13730_22192_923571897}[：]{style="font-family:宋体"}[能够保留的最大统计组个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1859725407}

[[当保留的统计组数目达到最大值时，如果形成新的统计组，保存时间最久的统计组将被删除。]{style="font-family:宋体"}]{#struct_0_13730_22192_x1545204314}

[[需要注意的是，能够保留的最大统计组个数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13730_22192_534550246}[时，不进行统计]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353724402}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_306860258}[配置能够保留的最大统计组个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1552337734}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] statistics max-group 5]{lang="EN-US"}
:::

::: {#-786043255 .myid}
[]{#_Toc404796699}[]{#struct_0_13730_22192_x2091247161}[]{#_Toc279590563}[]{#_Toc199817506}[]{#_Toc199824959}[]{#_Toc199825563}[]{#_Toc199825892}[]{#_Toc199826221}[]{#_Toc199826549}[]{#_Toc199817507}[]{#_Toc199824960}[]{#_Toc199825564}[]{#_Toc199825893}[]{#_Toc199826222}[]{#_Toc199826550}[]{#_Toc199817508}[]{#_Toc199824961}[]{#_Toc199825565}[]{#_Toc199825894}[]{#_Toc199826223}[]{#_Toc199826551}[]{#_Toc199817509}[]{#_Toc199824962}[]{#_Toc199825566}[]{#_Toc199825895}[]{#_Toc199826224}[]{#_Toc199826552}[]{#_Toc199817510}[]{#_Toc199824963}[]{#_Toc199825567}[]{#_Toc199825896}[]{#_Toc199826225}[]{#_Toc199826553}[]{#_Toc199817511}[]{#_Toc199824964}[]{#_Toc199825568}[]{#_Toc199825897}[]{#_Toc199826226}[]{#_Toc199826554}[]{#_Toc330304399}[]{#_Toc330304400}[]{#_Toc330304401}[]{#_Toc330304402}[]{#_Toc330304403}[]{#_Toc330304404}[]{#_Toc330304405}[]{#_Toc330304406}[]{#_Toc330304407}[]{#_Toc330304408}[]{#_Toc330304409}[]{#_Toc330304410}[]{#_Toc330304411}[]{#_Toc330304412}[]{#_Toc330304413}[]{#_Toc330304414}[]{#_Toc330304415}[]{#_Toc330304416}[]{#_Toc330304417}[]{#_Toc330304418}[]{#_Toc200180654}[]{#_Toc201634474}[]{#_Toc202085548}[]{#_Toc202085853}[]{#_Toc200180655}[]{#_Toc201634475}[]{#_Toc202085549}[]{#_Toc202085854}[]{#_Toc200180656}[]{#_Toc201634476}[]{#_Toc202085550}[]{#_Toc202085855}[]{#_Toc200180657}[]{#_Toc201634477}[]{#_Toc202085551}[]{#_Toc202085856}[]{#_Toc200180658}[]{#_Toc201634478}[]{#_Toc202085552}[]{#_Toc202085857}[]{#_Toc200180659}[]{#_Toc201634479}[]{#_Toc202085553}[]{#_Toc202085858}[]{#_Toc200180660}[]{#_Toc201634480}[]{#_Toc202085554}[]{#_Toc202085859}[]{#_Toc200180661}[]{#_Toc201634481}[]{#_Toc202085555}[]{#_Toc202085860}[]{#_Toc200180662}[]{#_Toc201634482}[]{#_Toc202085556}[]{#_Toc202085861}[]{#_Toc200180663}[]{#_Toc201634483}[]{#_Toc202085557}[]{#_Toc202085862}[]{#_Toc200180664}[]{#_Toc201634484}[]{#_Toc202085558}[]{#_Toc202085863}[]{#_Toc200180665}[]{#_Toc201634485}[]{#_Toc202085559}[]{#_Toc202085864}[]{#_Toc200180666}[]{#_Toc201634486}[]{#_Toc202085560}[]{#_Toc202085865}[]{#_Toc200180667}[]{#_Toc201634487}[]{#_Toc202085561}[]{#_Toc202085866}[]{#_Toc200180668}[]{#_Toc201634488}[]{#_Toc202085562}[]{#_Toc202085867}[]{#_Toc200180669}[]{#_Toc201634489}[]{#_Toc202085563}[]{#_Toc202085868}[]{#_Toc200180670}[]{#_Toc201634490}[]{#_Toc202085564}[]{#_Toc202085869}[]{#_Toc200180671}[]{#_Toc201634491}[]{#_Toc202085565}[]{#_Toc202085870}[]{#_Toc200180672}[]{#_Toc201634492}[]{#_Toc202085566}[]{#_Toc202085871}[]{#_Toc200180673}[]{#_Toc201634493}[]{#_Toc202085567}[]{#_Toc202085872}[]{#_Toc200180674}[]{#_Toc201634494}[]{#_Toc202085568}[]{#_Toc202085873}[]{#_Toc200180677}[]{#_Toc201634497}[]{#_Toc202085571}[]{#_Toc202085876}[]{#_Toc200180678}[]{#_Toc201634498}[]{#_Toc202085572}[]{#_Toc202085877}

**NQA \-- NQA客户端配置命令 \-- target-only**

------------------------------------------------------------------------

[**[target-only]{lang="EN-US"}**]{#struct_0_13730_22192_198330722}[命令用来配置]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[测试中仅针对到达目的地址的完整路径进行探测，不逐跳进行探测。]{style="font-family:宋体"}

[**[undo target-only]{lang="EN-US"}**]{#struct_0_13730_22192_x1731209880}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x922234171}

[**[target-only]{lang="EN-US"}**]{#struct_0_13730_22192_x1353658866}

[**[undo target-only]{lang="EN-US"}**]{#struct_0_13730_22192_1463304137}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x639621538}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_701001272}[测试中会逐跳进行探测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_786367079}

[[Path-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x1809172201}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_575795210}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1922771407}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1353593330}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1708788386}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1452823865}[配置仅对目的地址探测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1913821439}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type path-jitter]{lang="EN-US"}

[\[Sysname-nqa-admin-test- path-jitter\] target-only]{lang="EN-US"}
:::

::: {#-175272329 .myid}
[]{#_Toc404796700}[]{#struct_0_13730_22192_943777094}[]{#_Toc330304420}[]{#_Toc330304421}[]{#_Toc330304422}[]{#_Toc330304423}[]{#_Toc330304424}[]{#_Toc330304425}[]{#_Toc330304426}[]{#_Toc330304427}[]{#_Toc330304428}[]{#_Toc330304429}[]{#_Toc330304430}[]{#_Toc330304431}[]{#_Toc330304432}[]{#_Toc330304433}[]{#_Toc330304434}[]{#_Toc330304435}[]{#_Toc330304436}[]{#_Toc330304437}[]{#_Toc330304438}[]{#_Toc330304439}[]{#_Toc330304440}

**NQA \-- NQA客户端配置命令 \-- tos**

------------------------------------------------------------------------

[**[tos]{lang="EN-US"}**]{#struct_0_13730_22192_972108486}[命令用来配置]{style="font-family:宋体"}[NQA]{lang="EN-US"}[探测报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中服务类型域的值。]{style="font-family:宋体"}

[**[undo tos]{lang="EN-US"}**]{#struct_0_13730_22192_x227574015}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353003506}

[**[tos]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_13730_22192_1357768133}

[**[undo]{lang="EN-US"}**[ **tos**]{lang="EN-US"}]{#struct_0_13730_22192_x549467765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1407306316}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x802157244}[探测报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中服务类型域的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_194793132}

[[任意测试类型视图]{style="font-family:宋体"}]{#struct_0_13730_22192_776124232}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x2051726533}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_2080530563}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1352937970}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_19159183}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_84318777}

[*[value]{lang="EN-US"}*]{#struct_0_13730_22192_x1468422050}[：探测报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中服务类型域的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1640440104}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_809255761}[配置探测报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中服务类型域的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1622468235}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] tos 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x236464074}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中服务类型域的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353527793}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] tos 1]{lang="EN-US"}
:::

::: {#-1384405014 .myid}
[]{#_Toc404796701}[]{#struct_0_13730_22192_1735187530}

**NQA \-- NQA客户端配置命令 \-- ttl**

------------------------------------------------------------------------

[**[ttl]{lang="EN-US"}**]{#struct_0_13730_22192_4372267}[命令用来配置探测报文在网络中可以经过的最大跳数。]{style="font-family:宋体"}

[**[undo ttl]{lang="EN-US"}**]{#struct_0_13730_22192_x60331088}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1452216040}

[**[ttl]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_13730_22192_x895197517}

[**[undo ttl]{lang="EN-US"}**]{#struct_0_13730_22192_2011273790}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x790193510}

[[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_367970255}[类型测试报文在网络中可以经过的最大跳数是]{style="font-family:宋体"}[30]{lang="EN-US"}[跳。其它测试类型下探测报文在网络中可以经过的最大跳数为]{style="font-family:宋体"}[20]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353462257}

[[DLSw/DNS/FTP/HTTP/ICMP-echo/SNMP/TCP/UDP-echo/UDP-jitter/UDP-tracert/Voice]{lang="EN-US"}]{#struct_0_13730_22192_381610477}[测试类型视图]{style="font-family:宋体"}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x718221577}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_362896730}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x617302597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1946282268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x784770332}

[*[value]{lang="EN-US"}*]{#struct_0_13730_22192_x449428215}[：]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[测试类型表示允许探测报文填充的最大跳数值，其它测试类型表示探测报文在网络中可以经过的最大跳数，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1523758629}

[[配置]{style="font-family:宋体"}**[route-option bypass-route]{lang="EN-US"}**]{#struct_0_13730_22192_x1353396721}[命令后，探测报文在网络中可以经过的最大跳数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}**[ttl]{lang="EN-US"}**[命令不会生效。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_13730_22192_1965210011}[类型测试时，如果使用]{style="font-family:宋体"}**[init-ttl]{lang="EN-US"}**[命令配置的初始跳数值大于此值，测试将无法启动。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_363424253}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_560199055}[配置探测报文在网络中可以经过的最大跳数为]{style="font-family:宋体"}[16]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_983699929}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] ttl 16]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x192715710}[在]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置探测报文在网络中可以经过的最大跳数为]{style="font-family:宋体"}[16]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_622429210}

[\[Sysname\] nqa template icmp icmptplt]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-icmptplt\] ttl 16]{lang="EN-US"}
:::

::: {#-1051447130 .myid}
[]{#_Toc404796702}[]{#struct_0_13730_22192_x1246757041}

**NQA \-- NQA客户端配置命令 \-- type**

------------------------------------------------------------------------

[**[type]{lang="EN-US"}**]{#struct_0_13730_22192_x1353331185}[命令用来配置当前测试组的测试类型，并进入测试组测试类型视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1602789345}

[**[type]{lang="EN-US"}**[ { **dhcp** \| **dlsw** \| **dns** \| **ftp** \| **http** \| **icmp-echo** \| **path-jitter** \| **snmp** \| **tcp** \| **udp-echo** \| **udp-jitter** \| **udp-tracert** \| **voice** }]{lang="EN-US"}]{#struct_0_13730_22192_781335799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1163288546}

[[没有配置测试类型。]{style="font-family:宋体"}]{#struct_0_13730_22192_1797173050}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_353172159}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x771123177}[测试组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_443643539}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1344751218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1353789937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1192596698}

[**[dhcp]{lang="EN-US"}**]{#struct_0_13730_22192_563503179}[：测试类型为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dlsw]{lang="EN-US"}**]{#struct_0_13730_22192_1745325956}[：测试类型为]{style="font-family:宋体"}[DLSw]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dns]{lang="EN-US"}**]{#struct_0_13730_22192_397534762}[：测试类型为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ftp]{lang="EN-US"}**]{#struct_0_13730_22192_x877169879}[：测试类型为]{style="font-family:宋体"}[FTP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_13730_22192_427092100}[：测试类型为]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[icmp-echo]{lang="EN-US"}**]{#struct_0_13730_22192_1336060448}[：测试类型为]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[path-jitter]{lang="EN-US"}**]{#struct_0_13730_22192_x1353724401}[：测试类型为]{style="font-family:宋体"}[Path-jitter]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[snmp]{lang="EN-US"}**]{#struct_0_13730_22192_x1259223683}[：测试类型为]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_13730_22192_x924140130}[：测试类型为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[udp-echo]{lang="EN-US"}**]{#struct_0_13730_22192_x1969422124}[：测试类型为]{style="font-family:宋体"}[UDP-echo]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[udp-jitter]{lang="EN-US"}**]{#struct_0_13730_22192_x780683147}[：测试类型为]{style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[udp-tracert]{lang="EN-US"}**]{#struct_0_13730_22192_1965078939}[：测试类型为]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[voice]{lang="EN-US"}**]{#struct_0_13730_22192_997773460}[：测试类型为]{style="font-family:宋体"}[Voice]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1326504678}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x615771824}[配置测试组的测试类型为]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试，并进入测试组测试类型视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353658865}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type ftp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-ftp\]]{lang="EN-US"}
:::

::: {#-1384273943 .myid}
[]{#_Toc404796703}[]{#struct_0_13730_22192_x1265579218}

**NQA \-- NQA客户端配置命令 \-- url**

------------------------------------------------------------------------

[**[url]{lang="EN-US"}**]{#struct_0_13730_22192_x1959008928}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[和]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试访问的网址。]{style="font-family:宋体"}

[**[undo url]{lang="EN-US"}**]{#struct_0_13730_22192_2109535751}[命令用来取消已配置的测试访问的网址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x533373290}

[**[url ]{lang="EN-US"}***[url]{lang="EN-US"}*]{#struct_0_13730_22192_x909093149}

[**[undo url]{lang="EN-US"}**]{#struct_0_13730_22192_1171815391}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1697756266}

[[没有配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_1007567299}[和]{style="font-family:宋体"}[FTP]{lang="EN-US"}[测试访问的网址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1880256041}

[[FTP/HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x1353593329}[测试类型视图]{style="font-family:宋体"}

[[FTP/HTTP]{lang="EN-US"}]{#struct_0_13730_22192_1376390865}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1188874968}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x2009302196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1207126589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_616211436}

[*[url]{lang="EN-US"}*]{#struct_0_13730_22192_x588117932}[：测试操作访问的目标资源地址，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}*[url]{lang="EN-US"}*[中不允许有字符]{style="font-family:宋体"}[?]{lang="EN-US"}[。]{style="font-family:宋体"}*[url]{lang="EN-US"}*[中的主机名部分，由"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成（如]{style="font-family:宋体"}[aabbcc.com]{lang="EN-US"}[），每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符，区分大小写；字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["及"]{style="font-family:宋体"}[\_]{lang="EN-US"}["，不能出现连续"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_2078450232}[测试类型时，]{style="font-family:宋体"}*[url]{lang="EN-US"}*[格式为]{style="font-family:宋体"}[http://*host/resource*]{lang="EN-US"}[或]{style="font-family:宋体"}[http]{lang="EN-US"}[://*host*:*port*/]{lang="EN-US"}*[resource]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP]{lang="EN-US"}]{#struct_0_13730_22192_920070413}[测试类型时，]{lang="EN-US" style="font-family:
宋体"}*[url]{lang="EN-US"}*[格式为]{style="font-family:
宋体"}[ftp://*host*/*filename*]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[ftp://*host*:*port*/*filename*]{lang="EN-US"}

[*[filename]{lang="EN-US"}*]{#struct_0_13730_22192_x1353003505}[取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1761052660}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x478855929}[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试访问的网址为]{style="font-family:宋体"}[http://www.company.com/index.html]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_203382998}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type http]{lang="EN-US"}

[\[Sysname-nqa-admin-test-http\] url ]{lang="EN-US"}[[http://www.company.com/index.html]{lang="EN-US" style="color:windowtext;
text-decoration:none"}](http://www.company.com/index.html)

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x425183273}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图，配置测试访问的网址为]{style="font-family:宋体"}[http://www.company.com/index.html]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_161570465}

[\[Sysname\] nqa template http httptplt]{lang="EN-US"}

[\[Sysname-nqatplt-http-httptplt\] url ]{lang="EN-US"}[[http://www.company.com/index.html]{lang="EN-US" style="color:windowtext;
text-decoration:none"}](http://www.company.com/index.html)
:::

::: {#-2032495825 .myid}
[]{#_Toc404796704}[]{#struct_0_13730_22192_824366890}

**NQA \-- NQA客户端配置命令 \-- username**

------------------------------------------------------------------------

[**[username]{lang="EN-US"}**]{#struct_0_13730_22192_x1352937969}[命令用来配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[登录用户名。]{style="font-family:宋体"}

[**[undo username]{lang="EN-US"}**]{#struct_0_13730_22192_x1903089582}[命令用来取消已配置的登录用户名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1026950036}

[**[username ]{lang="EN-US"}**]{#struct_0_13730_22192_x1145907534}*[username]{lang="EN-US"}*

[**[undo username]{lang="EN-US"}**]{#struct_0_13730_22192_1737807016}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_1828697666}

[[未配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_13730_22192_1511702269}[或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[登录用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_267393927}

[[FTP/HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x1353527796}[测试类型视图]{style="font-family:宋体"}

[[FTP/HTTP/RADIUS]{lang="EN-US"}]{#struct_0_13730_22192_x1800264879}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x543878446}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_574076581}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1404687782}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1998619009}

[*[username]{lang="EN-US"}*]{#struct_0_13730_22192_1917206264}[：测试使用的用户名，区分大小写。]{style="font-family:宋体"}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[登录用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x882708833}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_886218808}[配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[登录用户名为]{style="font-family:宋体"}[administrator]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353462260}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type ftp]{lang="EN-US"}

[\[Sysname-nqa-admin-test-ftp\] username administrator]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1991239126}[在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[登录用户名为]{style="font-family:宋体"}[administrator]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x726806567}

[\[Sysname\] nqa template ftp ftptplt]{lang="EN-US"}

[\[Sysname-nqatplt-ftp-ftptplt\] username administrator]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1278023843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[operation]{lang="EN-US"}**]{#struct_0_13730_22192_1137617318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password]{lang="EN-US"}**]{#struct_0_13730_22192_x470829305}
:::

::: {#1902401671 .myid}
[]{#_Toc404796705}[]{#struct_0_13730_22192_x1353396724}[]{#_Toc312165596}

**NQA \-- NQA客户端配置命令 \-- version**

------------------------------------------------------------------------

[**[version]{lang="EN-US"}**]{#struct_0_13730_22192_x39860274}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试所使用的版本。]{style="font-family:宋体"}

[**[undo version]{lang="PT-BR"}**]{#struct_0_13730_22192_92355893}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1354446464}

[**[version ]{lang="PT-BR"}**]{#struct_0_13730_22192_1956538601}[{ **v1.0** \| **v1.1** } ]{lang="PT-BR"}

[**[undo version]{lang="PT-BR"}**]{#struct_0_13730_22192_x1502557882}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x675042305}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_18213584}[测试使用的版本为]{style="font-family:宋体"}[1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x839661314}

[[HTTP]{lang="EN-US"}]{#struct_0_13730_22192_x1353331188}[测试类型视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_487044098}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1210785920}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1004495511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x461280660}

[**[v1.0]{lang="EN-US"}**]{#struct_0_13730_22192_x1299832676}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试使用的版本为]{style="font-family:宋体"}[1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[v1]{lang="EN-US"}**[.1]{lang="EN-US"}]{#struct_0_13730_22192_1301206415}[：]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[测试使用的版本为]{style="font-family:宋体"}[1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_284495201}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1353789940}[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[测试使用的版本为]{style="font-family:宋体"}[1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1952177121}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type http]{lang="EN-US"}

[\[Sysname-nqa-admin-test-http\] version v1.1]{lang="EN-US"}
:::

::::: {#1715388964 .myid}
[]{#_Toc279084546}[]{#struct_0_13730_22192_x967943100}[]{#_Toc404796706}[]{#_Toc161908974}[]{#_Toc161908975}[]{#_Toc161908976}[]{#_Toc161908977}[]{#_Toc161908978}[]{#_Toc161908979}[]{#_Toc161908980}[]{#_Toc161908981}[]{#_Toc161908982}[]{#_Toc161908983}[]{#_Toc161908984}[]{#_Toc161908985}[]{#_Toc161908986}[]{#_Toc161908987}[]{#_Toc161908988}[]{#_Toc161908990}

**NQA \-- NQA客户端配置命令 \-- vpn-instance**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NQA命令.files/image001.png){#图片 1 border="0" width="61" height="25"}]{lang="EN-US"}]{#struct_0_13730_22192_2027061114}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的实际情况有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13730_22192_1136565243}
:::

[ ]{lang="EN-US"}

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_13730_22192_688442733}[命令用来指定测试操作所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_13730_22192_296662845}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353724404}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_13730_22192_x499708796}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_13730_22192_2135064953}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_x316787149}

[[未指定测试操作所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_13730_22192_1965180759}[，]{style="font-family:宋体"}[NQA]{lang="EN-US"}[用来测试公网的连通性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x961981518}

[[任意测试类型视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x680421819}

[[任意类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1510098555}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x546116417}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1353658868}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1312633385}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_1242382795}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_13730_22192_x208643396}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_x68125424}

[[指定测试操作所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_13730_22192_785192623}[后，]{style="font-family:宋体"}[NQA]{lang="EN-US"}[将测试指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内隧道的连通情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1633922859}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1040269089}[指定测试操作所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353593332}

[\[Sysname\] nqa entry admin test]{lang="EN-US"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] vpn-instance vpn1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x545988972}[在]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板视图下，指定测试操作所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_473675399}

[\[Sysname\] nqa template ftp ftptplt]{lang="EN-US"}

[\[Sysname-nqatplt-ftp-ftptplt\] vpn-instance vpn1]{lang="EN-US"}
:::::

::: {#1832562561 .myid}
[]{#_Toc404796708}[]{#struct_0_13730_22192_x1353003508}

**NQA \-- NQA服务器端命令 \-- display nqa server**

------------------------------------------------------------------------

[**[display nqa server]{lang="EN-US"}**]{#struct_0_13730_22192_1808106827}[命令用来显示服务器的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x251327233}

[**[display nqa server]{lang="EN-US"}**]{#struct_0_13730_22192_x700726802}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1554457926}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13730_22192_960461939}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_307387067}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1331702550}

[[network-operator]{lang="EN-US"}]{#struct_0_13730_22192_x1032847883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1352937972}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13730_22192_x1143640231}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1941161130}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1010999786}[显示服务器的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display nqa server]{lang="EN-US"}]{#struct_0_13730_22192_x441961405}

[NQA server status: enabled]{lang="EN-US"}

[TCP connect:]{lang="EN-US"}

[   IP Address          Port      ToS    Vpn-instance]{lang="EN-US"}

[   2.2.2.2             2000      200    -]{lang="EN-US"}

[UDP echo:]{lang="EN-US"}

[   IP Address          Port      ToS    Vpn-instance]{lang="EN-US"}

[   3.3.3.3             3000      255    vpn1]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display nqa server status]{lang="EN-US"}]{#struct_0_13730_22192_1357153870}[命令输出信息描述]{style="font-family:黑体"}

[]{#table_struct_0_37558676}[[字段]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353527795}
:::

[[描述命令]{style="font-family:黑体"}]{#struct_0_13730_22192_928618476}

[[NQA server status]{lang="EN-US"}]{#struct_0_13730_22192_1965078946}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1966061986}[服务器状态，包括的取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_13730_22192_1965996450}[：未启用]{lang="EN-US" style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器功能；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_13730_22192_190254668}[：启用了]{lang="EN-US" style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器功能；]{lang="EN-US" style="font-family:宋体"}

[[tcp-connect]{lang="EN-US"}]{#struct_0_13730_22192_x129734711}

[[NQA TCP]{lang="EN-US"}]{#struct_0_13730_22192_394145552}[测试中服务器的状态信息]{style="font-family:宋体"}

[[udp-echo]{lang="EN-US"}]{#struct_0_13730_22192_1546837509}

[[NQA UDP]{lang="EN-US"}]{#struct_0_13730_22192_1540225990}[测试中服务器的状态信息]{style="font-family:宋体"}

[[IP Address]{lang="EN-US"}]{#struct_0_13730_22192_x1353462259}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x68728217}[服务器]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[监听服务的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_13730_22192_x354002164}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_1553008749}[服务器]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[监听服务的端口号]{style="font-family:宋体"}

[[ToS]{lang="EN-US"}]{#struct_0_13730_22192_1239080240}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x334897872}[服务器]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[监听服务的回应报文携带的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Vpn-instance]{lang="EN-US"}]{#struct_0_13730_22192_x849098260}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x1353396723}[服务器的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#752517052 .myid}
[]{#_Toc404796709}[]{#struct_0_13730_22192_1526223667}

**NQA \-- NQA服务器端命令 \-- nqa server enable**

------------------------------------------------------------------------

[**[nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_228823540}[命令用来开启]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器功能。]{style="font-family:宋体"}

[**[undo nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_x1029328458}[命令用来关闭]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1573663702}

[**[nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_1253747039}

[**[undo nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_x827591562}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13730_22192_904361430}

[[NQA]{lang="EN-US"}]{#struct_0_13730_22192_x810905904}[服务器功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1353331187}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_439989931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_81602768}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_157614204}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_1387929121}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1021622772}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_x1286298401}[开启]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x1353789939}

[\[Sysname\] nqa server enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x29797284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nqa server]{lang="EN-US"}**]{#struct_0_13730_22192_823606608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa server tcp-connect]{lang="EN-US"}**]{#struct_0_13730_22192_x33471114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa server udp-echo]{lang="EN-US"}**]{#struct_0_13730_22192_263679511}
:::

::: {#-730031140 .myid}
[]{#_Toc404796710}[]{#struct_0_13730_22192_x1882799756}

**NQA \-- NQA服务器端命令 \-- nqa server tcp-connect**

------------------------------------------------------------------------

[**[nqa server tcp-connect]{lang="EN-US"}**]{#struct_0_13730_22192_x985136557}[命令用来在]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器上创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听服务。]{style="font-family:宋体"}

[**[undo nqa server tcp-connect]{lang="EN-US"}**]{#struct_0_13730_22192_x1085723238}[命令用来删除已建立的]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[监听服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x617139372}

[**[nqa server tcp-connect]{lang="EN-US"}**[ *ip-address port-number* \[ **vpn-instance** *vpn-instance-name* \] \[ **tos** *tos* \]]{lang="EN-US"}]{#struct_0_13730_22192_x1353724403}

[**[undo nqa server tcp-connect]{lang="EN-US"}**[ *ip-address port-number*]{lang="EN-US"}]{#struct_0_13730_22192_1872944199}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_1036912213}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_x1472135893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x470367408}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_x375305947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_902717427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1962311840}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13730_22192_x1305187572}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听服务的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1353658867}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听服务的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13730_22192_1057360632}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听的是公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[tos]{lang="EN-US"}***[ tos]{lang="EN-US"}*]{#struct_0_13730_22192_1965341089}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器应答报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[域的值。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_621356343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在测试类型为]{style="font-family:宋体"}]{#struct_0_13730_22192_x1466922745}[TCP]{lang="EN-US"}[时，才需在]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器上配置此命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令可以指定发送应答]{style="font-family:宋体"}]{#struct_0_13730_22192_x1909561362}[NQA]{lang="EN-US"}[探测报文（]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文）中携带的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所配置的]{style="font-family:宋体"}]{#struct_0_13730_22192_1671334918}[IP]{lang="EN-US"}[地址和端口号必须与]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端的配置一致，且不能与已有的监听服务冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所配置的]{style="font-family:宋体"}]{#struct_0_13730_22192_x1273297004}[IP]{lang="EN-US"}[地址必须是作为服务器的设备上的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，否则配置无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议不要配置]{style="font-family:宋体"}]{#struct_0_13730_22192_x1353593331}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[之间的端口（知名端口），否则可能导致]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试失败或该知名端口对应的服务不可用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_1020094969}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_1932157306}[创建]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[169.254.10.2]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[9000]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_x145705173}

[\[Sysname\] nqa server tcp-connect 169.254.10.2 9000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1935756385}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nqa server]{lang="EN-US"}**]{#struct_0_13730_22192_1629544792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_186605783}
:::

::: {#748206058 .myid}
[]{#_Toc404796711}[]{#struct_0_13730_22192_295994378}

**NQA \-- NQA服务器端命令 \-- nqa server udp-echo**

------------------------------------------------------------------------

[**[nqa server udp-echo]{lang="EN-US"}**]{#struct_0_13730_22192_x1353003507}[命令用来在]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器上创建]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听服务。]{style="font-family:宋体"}

[**[undo nqa server udp-echo]{lang="EN-US"}**]{#struct_0_13730_22192_x1371115222}[命令用来删除已建立的]{style="font-family:
宋体"}[UDP]{lang="EN-US"}[监听服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1227869707}

[**[nqa server udp-echo]{lang="EN-US"}**[ *ip-address port-number* \[ **vpn-instance** *vpn-instance-name* \] \[ **tos** *tos* \]]{lang="EN-US"}]{#struct_0_13730_22192_744570788}

[**[undo nqa server udp-echo]{lang="EN-US"}**[ *ip-address port-number*]{lang="EN-US"}]{#struct_0_13730_22192_1926947452}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1709654493}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13730_22192_880129169}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1191792039}

[[network-admin]{lang="EN-US"}]{#struct_0_13730_22192_1597696981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13730_22192_x1352937971}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1546924758}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13730_22192_x1892806641}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听服务的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_13730_22192_x1089689608}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听服务的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13730_22192_453233093}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听的是公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[tos]{lang="EN-US"}***[ tos]{lang="EN-US"}*]{#struct_0_13730_22192_1965210017}[：]{style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器应答报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[域的值。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13730_22192_1057030135}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在测试类型为]{lang="EN-US" style="font-family:宋体"}[UDP-jitter]{lang="EN-US"}]{#struct_0_13730_22192_x563469038}[、]{lang="EN-US" style="font-family:宋体"}[UDP-echo]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Voice]{lang="EN-US"}[时，才需在]{lang="EN-US" style="font-family:宋体"}[NQA]{lang="EN-US"}[服务器上配置此命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令可以指定发送应答]{style="font-family:宋体"}]{#struct_0_13730_22192_212556149}[NQA]{lang="EN-US"}[探测报文（]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文）中携带的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的]{style="font-family:宋体"}]{#struct_0_13730_22192_x526869484}[IP]{lang="EN-US"}[地址和端口号必须与]{style="font-family:宋体"}[NQA]{lang="EN-US"}[客户端的配置一致，且不能与已有的监听服务冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所配置的]{style="font-family:宋体"}]{#struct_0_13730_22192_x952165546}[IP]{lang="EN-US"}[地址必须是作为服务器的设备上的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，否则配置无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议不要配置]{style="font-family:宋体"}]{#struct_0_13730_22192_1557834491}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[之间的端口（知名端口），否则可能导致]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试失败或该知名端口对应的服务不可用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13730_22192_x1806413403}

[[\# ]{lang="EN-US"}]{#struct_0_13730_22192_984058401}[创建]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[169.254.10.2]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}[9000]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13730_22192_1375178480}

[\[Sysname\] nqa server udp-echo 169.254.10.2 9000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13730_22192_1285001224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nqa server]{lang="EN-US"}**]{#struct_0_13730_22192_212621685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa server enable]{lang="EN-US"}**]{#struct_0_13730_22192_1363295716}[]{#_username_1}[]{#_nqa_server_enable}[]{#_nqa_server_tcpconnect}[]{#_nqa_server_udpecho}
:::
