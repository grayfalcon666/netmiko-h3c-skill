::: {#-2078459863 .myid}
[]{#_Toc404793881}[]{#struct_0_x1925_35545_x399310354}

**ND攻击防御 \-- ND协议报文源MAC地址一致性检查命令 \-- ipv6 nd check log enable**

------------------------------------------------------------------------

[**[ipv6 nd check log enable]{lang="EN-US"}**]{#struct_0_x1925_35545_x1112267319}[命令开启]{style="font-family:
宋体"}[ND]{lang="EN-US"}[日志信息功能。]{style="font-family:宋体"}

[**[undo ipv6 nd check log enable]{lang="EN-US"}**]{#struct_0_x1925_35545_x1996061118}[命令关闭]{style="font-family:
宋体"}[ND]{lang="EN-US"}[日志信息功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1925_35545_252462981}

[**[ipv6 nd check log enable]{lang="EN-US"}**]{#struct_0_x1925_35545_769474834}

[**[undo ipv6 nd check log enable]{lang="EN-US"}**]{#struct_0_x1925_35545_730700165}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x2026864894}

[[设备]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x1925_35545_2138627175}[日志信息功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1925_35545_118926094}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1925_35545_x1127319624}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1925_35545_1547367336}

[[network-admin]{lang="EN-US"}]{#struct_0_x1925_35545_809303278}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1925_35545_1240107272}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1925_35545_1900412083}

[[设备生成的]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x1925_35545_x1420477896}[日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[[为了防止设备输出过多的]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x1925_35545_x1766979440}[日志信息，一般情况下建议不要打开此功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x1673002120}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_1278033648}[开启]{style="font-family:宋体"}[ND]{lang="EN-US"}[日志信息功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1925_35545_x1541101146}

[\[Sysname\] ipv6 nd check log enable]{lang="EN-US"}
:::

::: {#1828487718 .myid}
[]{#_Toc404793882}[]{#struct_0_x1925_35545_x237064882}

**ND攻击防御 \-- ND协议报文源MAC地址一致性检查命令 \-- ipv6 nd mac-check enable**

------------------------------------------------------------------------

[**[ipv6 nd mac-check enable]{lang="EN-US"}**]{#struct_0_x1925_35545_1120079675}[命令用来开启]{style="font-family:
宋体"}[ND]{lang="EN-US"}[协议报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能。]{style="font-family:宋体"}

[**[undo ipv6 nd mac-check enable]{lang="EN-US"}**]{#struct_0_x1925_35545_889539928}[命令用来关闭]{style="font-family:
宋体"}[ND]{lang="EN-US"}[协议报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x1847371476}

[**[ipv6 nd mac-check enable]{lang="EN-US"}**]{#struct_0_x1925_35545_1431647949}

[**[undo ipv6 nd mac-check enable]{lang="EN-US"}**]{#struct_0_x1925_35545_1813034756}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x1617766508}

[[ND]{lang="EN-US"}]{#struct_0_x1925_35545_1582193071}[协议报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x969211204}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1925_35545_x102787779}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1925_35545_1048858453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1925_35545_x127604823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1925_35545_x246534356}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1925_35545_155400397}

[[网关设备开启该功能后，会对接收到的]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x1925_35545_1443612486}[协议报文进行检查，如果]{style="font-family:宋体"}[ND]{lang="EN-US"}[报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和以太网数据帧首部的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，则丢弃该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x743548314}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_1225504261}[开启]{style="font-family:宋体"}[ND]{lang="EN-US"}[协议报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能。]{style="font-family:宋体"}

[[\<Sysname\> syatem-view]{lang="EN-US"}]{#struct_0_x1925_35545_x1594269493}

[\[Sysname\] ipv6 nd mac-check enable]{lang="EN-US"}
:::

::: {#-40932505 .myid}
[]{#_Toc234918604}[]{#_Toc138417073}[]{#_Toc137020654}[]{#_Toc59352302}[]{#_Toc52166669}[]{#_Toc59352304}[]{#_Toc59352315}[]{#_Toc404793884}[]{#struct_0_x1925_35545_x793500566}[]{#_Toc257724713}[]{#_Toc234918608}[]{#_Toc216496421}[]{#_Toc216500952}[]{#_Toc217899533}[]{#_Toc216496422}[]{#_Toc216500953}[]{#_Toc217899534}[]{#_Toc216496423}[]{#_Toc216500954}[]{#_Toc217899535}[]{#_Toc216496424}[]{#_Toc216500955}[]{#_Toc217899536}[]{#_Toc216496425}[]{#_Toc216500956}[]{#_Toc217899537}[]{#_Toc216496426}[]{#_Toc216500957}[]{#_Toc217899538}[]{#_Toc216496427}[]{#_Toc216500958}[]{#_Toc217899539}[]{#_Toc216496428}[]{#_Toc216500959}[]{#_Toc217899540}[]{#_Toc216496429}[]{#_Toc216500960}[]{#_Toc217899541}[]{#_Toc216496430}[]{#_Toc216500961}[]{#_Toc217899542}[]{#_Toc216496431}[]{#_Toc216500962}[]{#_Toc217899543}[]{#_Toc216496432}[]{#_Toc216500963}[]{#_Toc217899544}[]{#_Toc216496433}[]{#_Toc216500964}[]{#_Toc217899545}[]{#_Toc216496435}[]{#_Toc216500966}[]{#_Toc217899547}[]{#_Toc216496436}[]{#_Toc216500967}[]{#_Toc217899548}[]{#_Toc216496437}[]{#_Toc216500968}[]{#_Toc217899549}[]{#_Toc216496453}[]{#_Toc216500984}[]{#_Toc217899565}[]{#_Toc216496454}[]{#_Toc216500985}[]{#_Toc217899566}[]{#_Toc216496455}[]{#_Toc216500986}[]{#_Toc217899567}[]{#_Toc216496456}[]{#_Toc216500987}[]{#_Toc217899568}[]{#_Toc216496457}[]{#_Toc216500988}[]{#_Toc217899569}[]{#_Toc216496458}[]{#_Toc216500989}[]{#_Toc217899570}[]{#_Toc216496459}[]{#_Toc216500990}[]{#_Toc217899571}[]{#_Toc216496460}[]{#_Toc216500991}[]{#_Toc217899572}[]{#_Toc216496461}[]{#_Toc216500992}[]{#_Toc217899573}[]{#_Toc216496462}[]{#_Toc216500993}[]{#_Toc217899574}[]{#_Toc216496463}[]{#_Toc216500994}[]{#_Toc217899575}[]{#_Toc216496464}[]{#_Toc216500995}[]{#_Toc217899576}[]{#_Toc216496465}[]{#_Toc216500996}[]{#_Toc217899577}[]{#_Toc216496466}[]{#_Toc216500997}[]{#_Toc217899578}[]{#_Toc216496467}[]{#_Toc216500998}[]{#_Toc217899579}[]{#_Toc216496468}[]{#_Toc216500999}[]{#_Toc217899580}[]{#_Toc216496469}[]{#_Toc216501000}[]{#_Toc217899581}[]{#_Toc216496470}[]{#_Toc216501001}[]{#_Toc217899582}[]{#_Toc216496472}[]{#_Toc216501003}[]{#_Toc217899584}[]{#_Toc216496473}[]{#_Toc216501004}[]{#_Toc217899585}[]{#_Toc216496477}[]{#_Toc216501008}[]{#_Toc217899589}[]{#_Toc216496493}[]{#_Toc216501024}[]{#_Toc217899605}

**ND攻击防御 \-- ND Detection配置命令 \-- display ipv6 nd detection statistics**

------------------------------------------------------------------------

[**[display ipv6 nd detection statistics]{lang="EN-US"}**]{#struct_0_x1925_35545_x2142558709}[命令用来显示]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[进行用户合法性检查时丢弃]{style="font-family:宋体"}[ND]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1925_35545_662424515}

[**[display ipv6 nd detection]{lang="EN-US"}[ statistics]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1925_35545_2027010122}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x1580980383}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1925_35545_1937197332}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1925_35545_50968362}

[[network-admin]{lang="EN-US"}]{#struct_0_x1925_35545_963719578}

[[network-operator]{lang="EN-US"}]{#struct_0_x1925_35545_1666837508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1925_35545_x1410683544}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1925_35545_x693991558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x384323095}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1925_35545_x541601801}[：显示指定接口]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[进行用户合法性检查时丢弃]{style="font-family:宋体"}[ND]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1925_35545_378242602}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_x1501079385}[显示]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[进行用户合法性检查时丢弃报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 nd detection statistics]{lang="EN-US"}]{#struct_0_x1925_35545_x1677061942}

[ND packets dropped by ND detection:]{lang="EN-US"}

[Interface         Packets dropped]{lang="EN-US"}

[GE1/0/1           78]{lang="EN-US"}

[GE1/0/2           0]{lang="EN-US"}

[GE1/0/3           0]{lang="EN-US"}

[GE1/0/4           0]{lang="EN-US"}

[]{#struct_0_x1925_35545_x885440440}[[表1-1 ]{lang="EN-US"}[display ipv6 nd detection statistics]{lang="EN-US"}]{#_Toc229978447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_385215467}[[字段]{style="font-family:黑体"}]{#struct_0_x1925_35545_286934254}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1925_35545_x657575974}

[[ND packets dropped by ND detection]{lang="EN-US"}]{#struct_0_x1925_35545_x205149337}[：]{style="font-family:宋体"}

[[根据]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}]{#struct_0_x1925_35545_1751321169}[丢弃的]{style="font-family:宋体"}[ND]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1925_35545_x436424550}

[[ND]{lang="EN-US"}]{#struct_0_x1925_35545_1318199811}[报文入接口]{style="font-family:宋体"}

[[Packets dropped]{lang="EN-US"}]{#struct_0_x1925_35545_942486852}

[[丢弃的报文数目]{style="font-family:宋体"}]{#struct_0_x1925_35545_x1411909814}

[ ]{lang="EN-US"}

::: {#-810657079 .myid}
[]{#_Toc138417095}[]{#_Toc137020676}[]{#_Toc59352325}[]{#_Toc52166663}[]{#_Toc404793885}[]{#struct_0_x1925_35545_1774751200}[]{#_Toc257724714}[]{#_Toc234918605}[]{#_Toc216496540}[]{#_Toc216501071}[]{#_Toc217899652}[]{#_Toc216496541}[]{#_Toc216501072}[]{#_Toc217899653}[]{#_Toc216496544}[]{#_Toc216501075}[]{#_Toc217899656}[]{#_Toc216496545}[]{#_Toc216501076}[]{#_Toc217899657}[]{#_Toc216496546}[]{#_Toc216501077}[]{#_Toc217899658}[]{#_Toc216496547}[]{#_Toc216501078}[]{#_Toc217899659}[]{#_Toc216496548}[]{#_Toc216501079}[]{#_Toc217899660}[]{#_Toc216496549}[]{#_Toc216501080}[]{#_Toc217899661}[]{#_Toc216496550}[]{#_Toc216501081}[]{#_Toc217899662}[]{#_Toc216496551}[]{#_Toc216501082}[]{#_Toc217899663}[]{#_Toc216496552}[]{#_Toc216501083}[]{#_Toc217899664}[]{#_Toc216496553}[]{#_Toc216501084}[]{#_Toc217899665}[]{#_Toc216496554}[]{#_Toc216501085}[]{#_Toc217899666}[]{#_Toc216496555}[]{#_Toc216501086}[]{#_Toc217899667}[]{#_Toc90625854}[]{#_Toc90625857}

**ND攻击防御 \-- ND Detection配置命令 \-- ipv6 nd detection enable**

------------------------------------------------------------------------

[**[ipv6 nd detection enable]{lang="EN-US"}**]{#struct_0_x1925_35545_979943434}[命令用来开启]{style="font-family:
宋体"}[ND Detection]{lang="EN-US"}[功能，即对]{style="font-family:
宋体"}[ND]{lang="EN-US"}[报文进行合法性检查。]{style="font-family:宋体"}

[**[undo ipv6 nd detection enable]{lang="EN-US"}**]{#struct_0_x1925_35545_924862520}[命令用来关闭]{style="font-family:
宋体"}[ND Detection]{lang="EN-US"}[功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1925_35545_170722155}

[**[ipv6 nd detection enable]{lang="EN-US"}**]{#struct_0_x1925_35545_21993675}

[**[undo ipv6 nd detection enable]{lang="EN-US"}**]{#struct_0_x1925_35545_419806503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x201350790}

[[ND Detection]{lang="EN-US"}]{#struct_0_x1925_35545_1659105546}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x1911890450}

[[VLAN]{lang="EN-US"}]{#struct_0_x1925_35545_870889148}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x2100776179}

[[network-admin]{lang="EN-US"}]{#struct_0_x1925_35545_900597057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1925_35545_x247884130}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x52084889}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_1804314300}[在]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[内开启]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1925_35545_478869113}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan10\] ipv6 nd detection enable]{lang="EN-US"}
:::

::: {#-1615090960 .myid}
[]{#_Toc404793886}[]{#struct_0_x1925_35545_x738207796}[]{#_Toc257724715}[]{#_Toc234918606}

**ND攻击防御 \-- ND Detection配置命令 \-- ipv6 nd detection trust**

------------------------------------------------------------------------

[**[ipv6 nd detection trust]{lang="EN-US"}**]{#struct_0_x1925_35545_x1460567016}[命令用来配置端口为]{style="font-family:宋体"}[ND]{lang="EN-US"}[信任端口。]{style="font-family:宋体"}

[**[undo ipv6 nd detection trust]{lang="EN-US"}**]{#struct_0_x1925_35545_366614174}[命令用来配置端口为]{style="font-family:
宋体"}[ND]{lang="EN-US"}[非信任端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1925_35545_907788225}

[**[ipv6 nd detection trust]{lang="EN-US"}**]{#struct_0_x1925_35545_x2036056880}

[**[undo ipv6 nd detection trust]{lang="EN-US"}**]{#struct_0_x1925_35545_1911025028}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1925_35545_1429758712}

[[端口为]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x1925_35545_x1285826472}[非信任端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x438786470}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1925_35545_x358942337}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1925_35545_2044856759}

[[network-admin]{lang="EN-US"}]{#struct_0_x1925_35545_2124768865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1925_35545_x1679111138}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x804533863}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_524254378}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为]{style="font-family:宋体"}[ND]{lang="EN-US"}[信任端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1925_35545_x1769423212}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd detection trust]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_x866357490}[配置二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="EN-US"}[为]{style="font-family:宋体"}[ND]{lang="EN-US"}[信任端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1925_35545_x1703915223}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] ipv6 nd detection trust]{lang="EN-US"}
:::

::: {#1473241262 .myid}
[]{#_Toc234918603}[]{#_Toc138417108}[]{#_Toc137020689}[]{#_Toc404793887}[]{#struct_0_x1925_35545_1292145637}[]{#_Toc257724716}[]{#_Toc234918609}[]{#_Toc90625873}

**ND攻击防御 \-- ND Detection配置命令 \-- reset ipv6 nd detection statistics**

------------------------------------------------------------------------

[**[reset ipv6 nd detection statistics]{lang="EN-US"}**]{#struct_0_x1925_35545_x1651657122}[命令用来清除]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1925_35545_1971839819}

[**[reset ipv6 nd ]{lang="EN-US"}[detection statistics]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1925_35545_668539531}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1925_35545_1685037137}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1925_35545_160945477}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1925_35545_824047056}

[[network-admin]{lang="EN-US"}]{#struct_0_x1925_35545_315841781}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1925_35545_558684924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1925_35545_782382276}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1925_35545_x75234150}[：表示清除指定接口的统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1925_35545_x1343062612}

[[\# ]{lang="EN-US"}]{#struct_0_x1925_35545_x1145717667}[清除所有的]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 nd detection statistics]{lang="EN-US"}]{#struct_0_x1925_35545_x1119721467}
:::
