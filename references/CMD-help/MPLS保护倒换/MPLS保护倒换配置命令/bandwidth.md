::: {#1742433432 .myid}
[]{#_Toc404791780}[]{#struct_0_13803_16300_1729045219}[]{#_Toc359419173}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_13803_16300_x1086094847}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_13803_16300_x23017879}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_1876002529}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_13803_16300_1181949503}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_13803_16300_1843611150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_833730602}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13803_16300_545080781}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_748544615}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_1872512569}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_x876470892}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1086029311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_x735241663}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x432575153}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_13803_16300_2039847794}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_334997962}

[[接口的期望带宽会对下列内容有影响：]{style="font-family:宋体"}]{#struct_0_13803_16300_x870362206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBQ]{lang="EN-US"}]{#struct_0_13803_16300_1176431444}[队列带宽。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路开销值。具体介绍请参见"三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_13803_16300_x1460879388}[路由配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1085963775}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_1984980838}[配置隧道捆绑接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_1317434954}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] bandwidth 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x796272888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_768162884}
:::

::: {#1948332219 .myid}
[]{#_Toc404791781}[]{#struct_0_13803_16300_480163817}[]{#_Toc359419175}[]{#_Toc309912009}[]{#_Toc359572688}[]{#_Toc359573129}[]{#_Toc359573573}[]{#_Toc359574017}[]{#_Toc360433505}[]{#_Toc359572689}[]{#_Toc359573130}[]{#_Toc359573574}[]{#_Toc359574018}[]{#_Toc360433506}[]{#_Toc359572690}[]{#_Toc359573131}[]{#_Toc359573575}[]{#_Toc359574019}[]{#_Toc360433507}[]{#_Toc359572691}[]{#_Toc359573132}[]{#_Toc359573576}[]{#_Toc359574020}[]{#_Toc360433508}[]{#_Toc359572692}[]{#_Toc359573133}[]{#_Toc359573577}[]{#_Toc359574021}[]{#_Toc360433509}[]{#_Toc359572693}[]{#_Toc359573134}[]{#_Toc359573578}[]{#_Toc359574022}[]{#_Toc360433510}[]{#_Toc359572694}[]{#_Toc359573135}[]{#_Toc359573579}[]{#_Toc359574023}[]{#_Toc360433511}[]{#_Toc359572695}[]{#_Toc359573136}[]{#_Toc359573580}[]{#_Toc359574024}[]{#_Toc360433512}[]{#_Toc359572696}[]{#_Toc359573137}[]{#_Toc359573581}[]{#_Toc359574025}[]{#_Toc360433513}[]{#_Toc359572697}[]{#_Toc359573138}[]{#_Toc359573582}[]{#_Toc359574026}[]{#_Toc360433514}[]{#_Toc359572698}[]{#_Toc359573139}[]{#_Toc359573583}[]{#_Toc359574027}[]{#_Toc360433515}[]{#_Toc359572699}[]{#_Toc359573140}[]{#_Toc359573584}[]{#_Toc359574028}[]{#_Toc360433516}[]{#_Toc359572700}[]{#_Toc359573141}[]{#_Toc359573585}[]{#_Toc359574029}[]{#_Toc360433517}[]{#_Toc359572701}[]{#_Toc359573142}[]{#_Toc359573586}[]{#_Toc359574030}[]{#_Toc360433518}[]{#_Toc359572702}[]{#_Toc359573143}[]{#_Toc359573587}[]{#_Toc359574031}[]{#_Toc360433519}[]{#_Toc359572703}[]{#_Toc359573144}[]{#_Toc359573588}[]{#_Toc359574032}[]{#_Toc360433520}[]{#_Toc359572704}[]{#_Toc359573145}[]{#_Toc359573589}[]{#_Toc359574033}[]{#_Toc360433521}[]{#_Toc359572804}[]{#_Toc359573245}[]{#_Toc359573689}[]{#_Toc359574133}[]{#_Toc360433621}[]{#_Toc359572805}[]{#_Toc359573246}[]{#_Toc359573690}[]{#_Toc359574134}[]{#_Toc360433622}[]{#_Toc359572812}[]{#_Toc359573253}[]{#_Toc359573697}[]{#_Toc359574141}[]{#_Toc360433629}[]{#_Toc359572813}[]{#_Toc359573254}[]{#_Toc359573698}[]{#_Toc359574142}[]{#_Toc360433630}[]{#_Toc359572849}[]{#_Toc359573290}[]{#_Toc359573734}[]{#_Toc359574178}[]{#_Toc360433666}[]{#_Toc359572850}[]{#_Toc359573291}[]{#_Toc359573735}[]{#_Toc359574179}[]{#_Toc360433667}[]{#_Toc359572851}[]{#_Toc359573292}[]{#_Toc359573736}[]{#_Toc359574180}[]{#_Toc360433668}[]{#_Toc359572852}[]{#_Toc359573293}[]{#_Toc359573737}[]{#_Toc359574181}[]{#_Toc360433669}[]{#_Toc359572853}[]{#_Toc359573294}[]{#_Toc359573738}[]{#_Toc359574182}[]{#_Toc360433670}[]{#_Toc359572854}[]{#_Toc359573295}[]{#_Toc359573739}[]{#_Toc359574183}[]{#_Toc360433671}[]{#_Toc359572855}[]{#_Toc359573296}[]{#_Toc359573740}[]{#_Toc359574184}[]{#_Toc360433672}[]{#_Toc359572856}[]{#_Toc359573297}[]{#_Toc359573741}[]{#_Toc359574185}[]{#_Toc360433673}[]{#_Toc359572857}[]{#_Toc359573298}[]{#_Toc359573742}[]{#_Toc359574186}[]{#_Toc360433674}[]{#_Toc359572858}[]{#_Toc359573299}[]{#_Toc359573743}[]{#_Toc359574187}[]{#_Toc360433675}[]{#_Toc359572859}[]{#_Toc359573300}[]{#_Toc359573744}[]{#_Toc359574188}[]{#_Toc360433676}[]{#_Toc359572860}[]{#_Toc359573301}[]{#_Toc359573745}[]{#_Toc359574189}[]{#_Toc360433677}[]{#_Toc359572861}[]{#_Toc359573302}[]{#_Toc359573746}[]{#_Toc359574190}[]{#_Toc360433678}[]{#_Toc359572862}[]{#_Toc359573303}[]{#_Toc359573747}[]{#_Toc359574191}[]{#_Toc360433679}[]{#_Toc359572863}[]{#_Toc359573304}[]{#_Toc359573748}[]{#_Toc359574192}[]{#_Toc360433680}[]{#_Toc359572864}[]{#_Toc359573305}[]{#_Toc359573749}[]{#_Toc359574193}[]{#_Toc360433681}[]{#_Toc359572865}[]{#_Toc359573306}[]{#_Toc359573750}[]{#_Toc359574194}[]{#_Toc360433682}[]{#_Toc359572866}[]{#_Toc359573307}[]{#_Toc359573751}[]{#_Toc359574195}[]{#_Toc360433683}[]{#_Toc359572867}[]{#_Toc359573308}[]{#_Toc359573752}[]{#_Toc359574196}[]{#_Toc360433684}[]{#_Toc359572868}[]{#_Toc359573309}[]{#_Toc359573753}[]{#_Toc359574197}[]{#_Toc360433685}[]{#_Toc359572869}[]{#_Toc359573310}[]{#_Toc359573754}[]{#_Toc359574198}[]{#_Toc360433686}[]{#_Toc359572870}[]{#_Toc359573311}[]{#_Toc359573755}[]{#_Toc359574199}[]{#_Toc360433687}[]{#_Toc359572871}[]{#_Toc359573312}[]{#_Toc359573756}[]{#_Toc359574200}[]{#_Toc360433688}[]{#_Toc359572872}[]{#_Toc359573313}[]{#_Toc359573757}[]{#_Toc359574201}[]{#_Toc360433689}[]{#_Toc359572873}[]{#_Toc359573314}[]{#_Toc359573758}[]{#_Toc359574202}[]{#_Toc360433690}[]{#_Toc359572874}[]{#_Toc359573315}[]{#_Toc359573759}[]{#_Toc359574203}[]{#_Toc360433691}[]{#_Toc359572875}[]{#_Toc359573316}[]{#_Toc359573760}[]{#_Toc359574204}[]{#_Toc360433692}[]{#_Toc359572876}[]{#_Toc359573317}[]{#_Toc359573761}[]{#_Toc359574205}[]{#_Toc360433693}[]{#_Toc359572877}[]{#_Toc359573318}[]{#_Toc359573762}[]{#_Toc359574206}[]{#_Toc360433694}[]{#_Toc359572878}[]{#_Toc359573319}[]{#_Toc359573763}[]{#_Toc359574207}[]{#_Toc360433695}[]{#_Toc359572879}[]{#_Toc359573320}[]{#_Toc359573764}[]{#_Toc359574208}[]{#_Toc360433696}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_13803_16300_x1247431548}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1085898239}

[**[default]{lang="EN-US"}**]{#struct_0_13803_16300_1484840136}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_311326315}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x342319477}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_1118775911}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_1109156502}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_x525202175}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1179522586}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_13803_16300_x1650318593}

[[您可以在执行]{style="font-family:宋体"}]{#struct_0_13803_16300_x1086356991}**[default]{lang="EN-US"}**[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_13803_16300_x40418}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x2047211388}[将隧道捆绑接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x1180470708}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404791782}[]{#struct_0_13803_16300_1758624218}[]{#_Toc359419174}[]{#_Toc347996124}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_13803_16300_x1754443165}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_13803_16300_x286425145}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1086291455}

[**[description]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13803_16300_474197915}*[text]{lang="EN-US"}*

[**[undo description]{lang="EN-US"}**]{#struct_0_13803_16300_x235911431}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_x313168292}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_13803_16300_1435858667}["，比如；"]{style="font-family:宋体"}[Tunnel-Bundle1 Interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1274889999}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x849332906}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_x399169609}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1086225919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_1231994659}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1609219699}

[*[text]{lang="EN-US"}*]{#struct_0_13803_16300_x833893998}[：接口的描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_907433913}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_13803_16300_x304662078}

[[本命令仅用于标识某接口，并无特别的功能。使用]{style="font-family:宋体"}]{#struct_0_13803_16300_x1521416081}**[display interface]{lang="EN-US"}**[等命令可以看到设置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x984912319}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x1086160383}[设置接口]{style="font-family:宋体"}[Tunnel-bundle2]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[tunnel-bundle2]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x1264627465}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] ]{lang="EN-US"}[description]{lang="EN-US"}[ tunnel-bundle2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_1897560293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_707418131}
:::

::: {#-1511398521 .myid}
[]{#_Toc404791783}[]{#struct_0_13803_16300_x345921848}[]{#_Toc359419176}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- destination**

------------------------------------------------------------------------

[]{#_Toc275248925}[]{#_Toc67195986}[]{#_Toc67145811}[]{#_Toc61012174}[]{#_Toc347996171}[**[destination]{lang="EN-US"}**]{#struct_0_13803_16300_1052673610}[命令用来配置]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的隧道目的端地址。]{style="font-family:宋体"}

[**[undo destination]{lang="EN-US"}**]{#struct_0_13803_16300_467584765}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1085570559}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_13803_16300_x890000147}

[**[undo destination]{lang="EN-US"}**]{#struct_0_13803_16300_1851925821}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_x819929887}

[[未指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1702886585}[接口的隧道目的端地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x161139456}

[[Tunnel-Bundle ]{lang="EN-US"}]{#struct_0_13803_16300_787869825}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_1092449662}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1085505023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_1736971023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x2104516774}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13803_16300_1224864652}[：隧道的目的端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_1912299631}

[[MPLS L3VPN]{lang="EN-US"}]{#struct_0_13803_16300_x1423755871}[、]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[和]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[根据本命令配置的隧道目的端地址，判断捆绑隧道是否可以作为承载]{style="font-family:宋体"}[VPN]{lang="EN-US"}[业务的公网隧道。远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址与]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的隧道目的端地址相同时，该捆绑隧道可以作为]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[和]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的公网隧道。]{style="font-family:宋体"}

[[建议为成员接口和]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_510017296}[接口配置相同的目的端地址。如果不同，则需要确保通过成员接口能够到达]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的目的端地址；否则，会导致流量转发不通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1118361205}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_411565745}[设置隧道捆绑接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的隧道目的端地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x1086094848}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] destination 2.2.2.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_380266648}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_606078168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_168995283}
:::

::: {#-1903358103 .myid}
[]{#_Toc404791784}[]{#struct_0_13803_16300_x154759915}[]{#_Toc359419182}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display interface tunnel-bundle**

------------------------------------------------------------------------

[**[display interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_x1059052822}[命令用来显示隧道捆绑接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x637699828}

[**[display interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_13803_16300_x299065851}**[tunnel-bundle]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[number ]{lang="EN-US"}*[\] \] \[ ]{lang="EN-US"}**[brief]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[description]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[down ]{lang="EN-US"}**[\] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1086029312}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13803_16300_830842278}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_524833745}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1372263437}

[[network-operator]{lang="EN-US"}]{#struct_0_13803_16300_1311238566}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1567905215}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13803_16300_619353899}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1085963776}

[*[number]{lang="EN-US"}*]{#struct_0_13803_16300_x743902517}[：显示指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号，取值为已经创建的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_13803_16300_861808763}[：显示接口的概要信息。不指定该参数时，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_13803_16300_1416857029}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_13803_16300_x1260386928}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x283543366}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_1754124338}[参数，则显示设备支持的所有接口的信息。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_x281652602}[参数，不指定]{lang="EN-US" style="font-family:
宋体"}*[number]{lang="EN-US"}*[参数，则显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_1094081526}

[[\# ]{lang="PT-BR"}]{#struct_0_13803_16300_x89398252}[显示接口]{style="font-family:宋体"}[Tunnel-Bundle100]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel-bundle 100]{lang="EN-US"}]{#struct_0_13803_16300_x1085898240}

[Tunnel-Bundle100]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Tunnel-Bundle100 Interface]{lang="EN-US"}

[Bandwidth: 64kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Tunnel-Bundle destination unknown]{lang="EN-US"}

[Tunnel type: CRLSP]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface tunnel-bundle]{lang="EN-US"}]{#struct_0_13803_16300_x887485179}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1654035796}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_13803_16300_x1765831690}
:::

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_13803_16300_x1086356992}

[[Tunnel-Bundle100]{lang="EN-US"}]{#struct_0_13803_16300_403244109}

[[接口]{style="font-family:宋体"}[Tunnel-Bundle100]{lang="EN-US"}]{#struct_0_13803_16300_x1996715014}[的相关信息]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_13803_16300_1388913905}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x104857168}[接口的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_13803_16300_1701203893}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_13803_16300_x362500215}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_13803_16300_x1086291456}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_13803_16300_877482442}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1403051515}[接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_13803_16300_1708223649}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_13803_16300_633319316}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_13803_16300_x1086225920}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_13803_16300_x690254106}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1034422290}[接口的描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_13803_16300_510299807}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x153831758}[接口的期望带宽]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_13803_16300_x1086160384}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_301456476}[接口的最大传输单元]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_13803_16300_2029571954}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1033004000}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有为]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_13803_16300_x1085570560}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Tunnel-Bundle destination]{lang="EN-US"}]{#struct_0_13803_16300_1032510762}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1596582798}[接口的隧道目的端地址，取值为]{style="font-family:宋体"}[unknown]{lang="EN-US"}[表示未指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的隧道目的端地址]{style="font-family:宋体"}

[[Tunnel type]{lang="EN-US"}]{#struct_0_13803_16300_570581933}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1085505024}[接口的隧道模式，目前取值只能为]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_13803_16300_977456136}

[[最近一次清除计数时间]{style="font-family:宋体"}]{#struct_0_13803_16300_x979575314}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_13803_16300_22569010}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_13803_16300_x1086094849}[秒钟的平均输入速率：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_13803_16300_x1185817293}[表示平均每秒输入的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_13803_16300_780024429}[表示平均每秒输入的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_13803_16300_1887755413}[表示平均每秒输入的包数]{lang="EN-US" style="font-family:宋体"}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_13803_16300_x1086029313}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_13803_16300_x1898041077}[秒钟的平均输出速率：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_13803_16300_292483410}[表示平均每秒输出的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_13803_16300_11817963}[表示平均每秒输出的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_13803_16300_x1085963777}[表示平均每秒输出的包数]{lang="EN-US" style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_13803_16300_822181424}

[[总计输入的报文数，总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}]{#struct_0_13803_16300_x2130740215}

[[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_13803_16300_x1085898241}

[[总计输出的报文数，总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}]{#struct_0_13803_16300_1841398176}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x1789531952}[显示接口]{style="font-family:宋体"}[Tunnel-Bundle100]{lang="EN-US"}[的概要信息]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel-bundle 100 brief]{lang="EN-US"}]{#struct_0_13803_16300_x1086356993}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Tunnel-B100          UP   UP       \--              aaaaaaaaaaaaaaaaaaaaaaaaaaa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x1162839832}[显示接口]{style="font-family:宋体"}[Tunnel-Bundle100]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel-bundle 100 brief  description]{lang="EN-US"}]{#struct_0_13803_16300_x64548060}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Tunnel-B100          UP   UP       \--              aaaaaaaaaaaaaaaaaaaaaaaaaaaaa]{lang="EN-US"}

[Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_907809101}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel-bundle brief down]{lang="EN-US"}]{#struct_0_13803_16300_x1434198541}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Tunnel-B100          DOWN Not connected]{lang="EN-US"}

[Tunnel-B101          DOWN Not connected]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface tunnel-bundle brief]{lang="EN-US"}]{#struct_0_13803_16300_x1831924784}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1648421942}[[字段]{style="font-size:9.0pt;
   font-family:宋体"}]{#struct_0_13803_16300_x1086291457}

[[描述]{style="font-size:9.0pt;font-family:宋体"}]{#struct_0_13803_16300_x688601499}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_13803_16300_651672015}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_13803_16300_x888543595}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_13803_16300_x1551118279}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_13803_16300_x1086225921}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_13803_16300_875829835}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_13803_16300_x1013128266}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_13803_16300_x2063239308}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的链路层协议状态显示是]{style="font-family:宋体"}[UP]{lang="EN-US"}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_13803_16300_x1145776531}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_13803_16300_x1086160385}

[[Link]{lang="EN-US"}]{#struct_0_13803_16300_1867540417}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_13803_16300_x81308886}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_13803_16300_1153070735}[：表示本链路物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_13803_16300_x931453678}[：表示本链路物理上是不通的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_13803_16300_x1085570561}[：表示本链路被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_13803_16300_x533573179}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：]{style="font-family:宋体"}]{#struct_0_13803_16300_1428969235}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_13803_16300_x1299493845}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_13803_16300_x1231892496}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_13803_16300_x1085505025}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_13803_16300_x1751427219}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13803_16300_1094139369}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_13803_16300_x1086094850}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_13803_16300_736562544}

[[Cause]{lang="EN-US"}]{#struct_0_13803_16300_1091338275}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_13803_16300_x178146313}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_13803_16300_x1086029314}[：表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_13803_16300_24273224}[：表示未成功建立捆绑隧道]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1530258733 .myid}
[]{#_Toc404791785}[]{#struct_0_13803_16300_746458357}[]{#_Toc359419193}[]{#_Toc360433701}[]{#_Toc360433702}[]{#_Toc360433703}[]{#_Toc360433704}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display mpls forwarding protection**

------------------------------------------------------------------------

[**[display mpls forwarding protection]{lang="EN-US"}**]{#struct_0_13803_16300_1537251195}[命令用来显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1085963778}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1194241211}

[**[display mpls forwarding protection]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_13803_16300_1107311543}**[tunnel-bundle]{lang="EN-US"}**[ *number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13803_16300_451385508}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mpls forwarding protection]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_13803_16300_915098754}**[tunnel-bundle]{lang="EN-US"}**[ *number* \] \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13803_16300_x384691255}[模式：]{style="font-family:宋体"}

[**[display mpls forwarding protection]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_13803_16300_x1085898242}**[tunnel-bundle]{lang="EN-US"}**[ *number* \] \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x2050284593}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13803_16300_x1379017342}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_x953601314}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_376667695}

[[network-operator]{lang="EN-US"}]{#struct_0_13803_16300_x1242626254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_1157336839}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13803_16300_x390239851}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1086356994}

[**[tunnel-bundle]{lang="IT"}**[ ]{lang="IT"}*[number]{lang="EN-US"}*]{#struct_0_13803_16300_x403324945}[：显示指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口对应]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号，取值为已经创建的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号。如果不指定本参数，则显示所有]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13803_16300_x1326201999}[：显示指定单板上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。如果不指定本参数，则显示主用主控板上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13803_16300_1462732272}[：显示指定成员设备上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13803_16300_2099821960}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}]{#struct_0_13803_16300_128531624}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组转发状态信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备主用主控板上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}]{#struct_0_13803_16300_1955649167}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组转发状态信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备主用主控板上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_13803_16300_x1259534961}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组转发状态信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_434790599}

[[\# ]{lang="PT-BR"}]{#struct_0_13803_16300_x284438608}[显示所有]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的转发状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls forwarding protection]{lang="EN-US"}]{#struct_0_13803_16300_x1086291458}

[Total number of protection groups: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[State:]{lang="EN-US"}

[  N: Normal    UA: Unavailable    PA: Protecting administrative]{lang="EN-US"}

[  PF: Protecting failure    WTR: Wait-to-Restore    DNR: Do-not-Revert]{lang="EN-US"}

[ ]{lang="EN-US"}

[  M: Manual switch    F: Forced switch   P: Protection tunnel failure]{lang="EN-US"}

[  W: Working tunnel failure    HO: Hold off    LO: Lockout of protection]{lang="EN-US"}

[ ]{lang="EN-US"}

[  L: Local    R: Remote]{lang="EN-US"}

[ ]{lang="EN-US"}

[Group ID    Working tunnel    Protection tunnel    State]{lang="EN-US"}

[2           100               200                  UA:LO:R]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mpls forwarding protection]{lang="EN-US"}]{#struct_0_13803_16300_x285316972}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1646284102}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_13803_16300_478227910}
:::

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_13803_16300_2036609651}

[[Group ID]{lang="EN-US"}]{#struct_0_13803_16300_53819678}

[[保护组]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13803_16300_447137019}

[[Working tunnel]{lang="EN-US"}]{#struct_0_13803_16300_x1925242900}

[[工作隧道的编号]{style="font-family:宋体"}]{#struct_0_13803_16300_x1086225922}

[[Protection tunnel]{lang="EN-US"}]{#struct_0_13803_16300_x1853053520}

[[保护隧道的编号]{style="font-family:宋体"}]{#struct_0_13803_16300_494075713}

[[State]{lang="EN-US"}]{#struct_0_13803_16300_747038766}

[[本字段的取值由三部分组成：保护组的当前状态、进入该状态的原因及原因的来源]{style="font-family:宋体"}]{#struct_0_13803_16300_x781884887}

[[保护组的当前状态取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1326704671}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_13803_16300_x1086160386}[：表示]{style="font-family:宋体"}[Normal state]{lang="EN-US"}[，即工作隧道和保护隧道都正常工作，流量在工作隧道上传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UA]{lang="EN-US"}]{#struct_0_13803_16300_x861342938}[：表示]{style="font-family:宋体"}[Unavailable state]{lang="EN-US"}[，即保护隧道不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PA]{lang="EN-US"}]{#struct_0_13803_16300_1469712924}[：表示]{style="font-family:宋体"}[Protecting administrative state]{lang="EN-US"}[，即执行外部倒换命令使得流量在保护隧道上传输]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PF]{lang="EN-US"}]{#struct_0_13803_16300_859258019}[：表示]{style="font-family:宋体"}[Protecting failure state]{lang="EN-US"}[，即工作隧道出现故障，流量倒换到保护隧道上传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_13803_16300_x1085570562}[：表示]{style="font-family:宋体"}[Wait-to-Restore state]{lang="EN-US"}[，即工作隧道故障恢复后，等待]{style="font-family:宋体"}[WTR]{lang="EN-US"}[时间将流量从保护隧道回切到工作隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNR]{lang="EN-US"}]{#struct_0_13803_16300_x2099657120}[：表示]{style="font-family:宋体"}[Do-not-Revert state]{lang="EN-US"}[，即工作隧道故障恢复后，不将流量从保护隧道回切到工作隧道]{style="font-family:宋体"}

[[保护组进入某个状态的原因包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_1332014496}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LO]{lang="EN-US"}]{#struct_0_13803_16300_1589396134}[：表示]{style="font-family:宋体"}[Lockout of protection]{lang="EN-US"}[，即执行锁定倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_13803_16300_x1793695545}[：表示通过信令协议检测到保护隧道出现故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}]{#struct_0_13803_16300_x1085505026}[：表示通过信令协议检测到工作隧道出现故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_13803_16300_2140255550}[：表示]{style="font-family:宋体"}[Forced switch]{lang="EN-US"}[，即执行强制倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_13803_16300_642373951}[：表示]{style="font-family:宋体"}[Manual switch]{lang="EN-US"}[，即执行手工倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HO]{lang="EN-US"}]{#struct_0_13803_16300_1444359878}[：表示]{style="font-family:宋体"}[Hold off]{lang="EN-US"}[，即工作隧道出现故障后，等待倒换延迟时间，再将流量切换到保护隧道上传输]{style="font-family:宋体"}

[[原因的来源包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1086094851}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_13803_16300_x829521397}[：表示来自于本地]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_13803_16300_x1673300515}[：表示来自于远端]{style="font-family:宋体"}

[[例如，]{style="font-family:宋体"}[UA:LO:L]{lang="EN-US"}]{#struct_0_13803_16300_1411572003}[表示由于本地执行锁定倒换命令，导致保护组进入保护隧道不可用状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1069305479 .myid}
[]{#_Toc404791786}[]{#struct_0_13803_16300_96475980}[]{#_Toc359419192}[]{#_Toc360433706}[]{#_Toc360433707}[]{#_Toc360433708}[]{#_Toc360433709}[]{#_Toc360433710}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display mpls protection**

------------------------------------------------------------------------

[**[display mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_x1086029315}[命令用来显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的当前运行状态和相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_1590357165}

[**[display mpls protection ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_13803_16300_x702427796}**[tunnel-bundle]{lang="EN-US"}***[ ]{lang="EN-US"}[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_633163579}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13803_16300_1712500578}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_1962804350}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x87349965}

[[network-operator]{lang="EN-US"}]{#struct_0_13803_16300_x1221400305}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1085963779}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13803_16300_371842730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_1904701889}

[**[tunnel-bundle]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_13803_16300_1475909660}[：显示指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口对应]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的当前运行状态和相关信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号，取值为已经创建的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号。如果不指定本参数，则显示所有]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的当前运行状态和相关信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_13803_16300_x992470417}[：显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1194121692}

[[\# ]{lang="PT-BR"}]{#struct_0_13803_16300_376864884}[显示所有]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的当前运行状态和相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls protection]{lang="EN-US"}]{#struct_0_13803_16300_x1085898243}

[Total number of protection groups: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[State:]{lang="EN-US"}

[  N: Normal    UA: Unavailable    PA: Protecting administrative]{lang="EN-US"}

[  PF: Protecting failure    WTR: Wait-to-Restore    DNR: Do-not-Revert]{lang="EN-US"}

[ ]{lang="EN-US"}

[  M: Manual switch    F: Forced switch   P: Protection tunnel failure]{lang="EN-US"}

[  W: Working tunnel failure    HO: Hold off    LO: Lockout of protection]{lang="EN-US"}

[ ]{lang="EN-US"}

[  L: Local    R: Remote]{lang="EN-US"}

[ ]{lang="EN-US"}

[Group ID   Type            Working tunnel    Protection tunnel    State]{lang="EN-US"}

[2          Tunnel bundle   100               200                  UA:LO:R]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display mpls protection]{lang="EN-US"}]{#struct_0_13803_16300_678598762}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1675579276}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_13803_16300_x846743454}
:::

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_13803_16300_x1782342445}

[[Group ID]{lang="EN-US"}]{#struct_0_13803_16300_1257632701}

[[保护组]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13803_16300_1287338905}

[[Type]{lang="EN-US"}]{#struct_0_13803_16300_x1086356995}

[[保护组的隧道类型，目前取值只能是]{style="font-family:宋体"}[Tunnel bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1969408886}[，表示隧道捆绑接口类型]{style="font-family:宋体"}

[[Working tunnel]{lang="EN-US"}]{#struct_0_13803_16300_x886251716}

[[工作隧道的编号]{style="font-family:宋体"}]{#struct_0_13803_16300_930265314}

[[Protection tunnel]{lang="EN-US"}]{#struct_0_13803_16300_x1017066319}

[[保护隧道的编号]{style="font-family:宋体"}]{#struct_0_13803_16300_1629282028}

[[State]{lang="EN-US"}]{#struct_0_13803_16300_x1086291459}

[[本字段的取值由三部分组成：保护组的当前状态、进入该状态的原因及原因的来源]{style="font-family:宋体"}]{#struct_0_13803_16300_x1851400913}

[[保护组的当前状态取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1423762255}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_13803_16300_x1422857841}[：表示]{style="font-family:宋体"}[Normal state]{lang="EN-US"}[，即工作隧道和保护隧道都正常工作，流量在工作隧道上传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UA]{lang="EN-US"}]{#struct_0_13803_16300_236338879}[：表示]{style="font-family:宋体"}[Unavailable state]{lang="EN-US"}[，即保护隧道不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PA]{lang="EN-US"}]{#struct_0_13803_16300_x1086225923}[：表示]{style="font-family:宋体"}[Protecting administrative state]{lang="EN-US"}[，即执行外部倒换命令使得流量在保护隧道上传输]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PF]{lang="EN-US"}]{#struct_0_13803_16300_x286969579}[：表示]{style="font-family:宋体"}[Protecting failure state]{lang="EN-US"}[，即工作隧道出现故障，流量倒换到保护隧道上传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_13803_16300_x448457459}[：表示]{style="font-family:宋体"}[Wait-to-Restore state]{lang="EN-US"}[，即工作隧道故障恢复后，等待]{style="font-family:宋体"}[WTR]{lang="EN-US"}[时间将流量从保护隧道回切到工作隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNR]{lang="EN-US"}]{#struct_0_13803_16300_x1512191414}[：表示]{style="font-family:宋体"}[Do-not-Revert state]{lang="EN-US"}[，即工作隧道故障恢复后，不将流量从保护隧道回切到工作隧道]{style="font-family:宋体"}

[[保护组进入某个状态的原因包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1086160387}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LO]{lang="EN-US"}]{#struct_0_13803_16300_704741003}[：表示]{style="font-family:宋体"}[Lockout of protection]{lang="EN-US"}[，即执行锁定倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_13803_16300_476260713}[：表示通过信令协议检测到保护隧道出现故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}]{#struct_0_13803_16300_x1799786552}[：表示通过信令协议检测到工作隧道出现故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_13803_16300_x826704624}[：表示]{style="font-family:宋体"}[Forced switch]{lang="EN-US"}[，即执行强制倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_13803_16300_x1085570563}[：表示]{style="font-family:宋体"}[Manual switch]{lang="EN-US"}[，即执行手工倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HO]{lang="EN-US"}]{#struct_0_13803_16300_629226235}[：表示]{style="font-family:宋体"}[Hold off]{lang="EN-US"}[，即工作隧道出现故障后，等待倒换延迟时间，再将流量切换到保护隧道上传输]{style="font-family:宋体"}

[[原因的来源包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_693522869}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_13803_16300_x702833611}[：表示来自于本地]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_13803_16300_x1085505027}[：表示来自于远端]{style="font-family:宋体"}

[[例如，]{style="font-family:宋体"}[UA:LO:L]{lang="EN-US"}]{#struct_0_13803_16300_x588627805}[表示由于本地执行锁定倒换命令，导致保护组进入保护隧道不可用状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x249322756}[显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls protection verbose]{lang="EN-US"}]{#struct_0_13803_16300_836219455}

[Protection group ID         : 2]{lang="EN-US"}

[   Protection group type    : Tunnel bundle]{lang="EN-US"}

[   Tunnel bundle name       : Tunnel-Bundle200]{lang="EN-US"}

[   Working tunnel           : Tunnel100]{lang="EN-US"}

[   Protection tunnel        : Tunnel200]{lang="EN-US"}

[   Protection mode          : 1:1]{lang="EN-US"}

[   Switching mode           : Bidirectional]{lang="EN-US"}

[   Tunnel in use            : Working-path]{lang="EN-US"}

[   Working tunnel state     : No defect]{lang="EN-US"}

[   Protection tunnel state  : Signal failure]{lang="EN-US"}

[   Holdoff time             : 5s (Remaining: 3s)]{lang="EN-US"}

[   Wait to restore time     : 30s (Remaining: 10s)]{lang="EN-US"}

[   Message interval          : 5s]{lang="EN-US"}

[   Revertive mode           : Revertive]{lang="EN-US"}

[   State                    : Unavailable (UA),]{lang="EN-US"}

[                              Protection tunnel failure (P),]{lang="EN-US"}

[                              Local (L)]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display mpls protection verbose]{lang="EN-US"}]{#struct_0_13803_16300_x1895153693}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1675636392}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_13803_16300_2128090698}

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_13803_16300_x806279336}

[[Protection group ID]{lang="EN-US"}]{#struct_0_13803_16300_x2035414480}

[[保护组]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13803_16300_x2094674637}

[[Protection group type]{lang="EN-US"}]{#struct_0_13803_16300_836284991}

[[保护组的隧道类型，目前取值只能是]{style="font-family:宋体"}[Tunnel bundle]{lang="EN-US"}]{#struct_0_13803_16300_1710308897}[，表示隧道捆绑接口类型]{style="font-family:宋体"}

[[Tunnel bundle name]{lang="EN-US"}]{#struct_0_13803_16300_x1052661226}

[[保护组关联的隧道捆绑接口名称]{style="font-family:宋体"}]{#struct_0_13803_16300_1984749090}

[[Working tunnel]{lang="EN-US"}]{#struct_0_13803_16300_901138125}

[[工作隧道的接口名称]{style="font-family:宋体"}]{#struct_0_13803_16300_x824463694}

[[Protection tunnel]{lang="EN-US"}]{#struct_0_13803_16300_836350527}

[[保护隧道的接口名称]{style="font-family:宋体"}]{#struct_0_13803_16300_x319114220}

[[Protection mode]{lang="EN-US"}]{#struct_0_13803_16300_998024324}

[[保护模式，取值包括]{style="font-family:宋体"}[1+1]{lang="EN-US"}]{#struct_0_13803_16300_x822271835}[和]{style="font-family:宋体"}[1:1]{lang="EN-US"}

[[Switching mode]{lang="EN-US"}]{#struct_0_13803_16300_1130263886}

[[切换模式，取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_836416063}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bidirectional]{lang="EN-US"}]{#struct_0_13803_16300_x825856651}[：]{style="font-family:宋体"}[双向切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unidirectional]{lang="EN-US"}]{#struct_0_13803_16300_969218209}[：]{style="font-family:宋体"}[单向切换]{lang="EN-US" style="font-family:宋体"}

[[Tunnel in use]{lang="EN-US"}]{#struct_0_13803_16300_1969065318}

[[当前转发流量使用的隧道，取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_x121922862}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Working-path]{lang="EN-US"}]{#struct_0_13803_16300_835957311}[：表示当前使用的隧道是工作隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protection-path]{lang="EN-US"}]{#struct_0_13803_16300_90431619}[：表示当前使用的隧道是保护隧道]{style="font-family:宋体"}

[[Working tunnel state]{lang="EN-US"}]{#struct_0_13803_16300_x1600280163}

[[工作隧道的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1024578521}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No defect]{lang="EN-US"}]{#struct_0_13803_16300_836022847}[：表示]{style="font-family:宋体"}[没有缺陷]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Signal failure]{lang="EN-US"}]{#struct_0_13803_16300_1421658302}[：表示通过信令协议检测出缺陷]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAM defect]{lang="EN-US"}]{#struct_0_13803_16300_x1922574218}[：表示通过]{style="font-family:宋体"}[OAM]{lang="EN-US"}[机制检测出缺陷]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote defect]{lang="EN-US"}]{#struct_0_13803_16300_836088383}[：表示从远端接收到的缺陷]{style="font-family:宋体"}

[[Protection tunnel state]{lang="EN-US"}]{#struct_0_13803_16300_596954157}

[[保护隧道的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_698726347}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No defect]{lang="EN-US"}]{#struct_0_13803_16300_387048723}[：表示]{style="font-family:宋体"}[没有缺陷]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Signal failure]{lang="EN-US"}]{#struct_0_13803_16300_836153919}[：表示通过信令协议检测出缺陷]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAM defect]{lang="EN-US"}]{#struct_0_13803_16300_x936559414}[：表示通过]{style="font-family:宋体"}[OAM]{lang="EN-US"}[机制检测出缺陷]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote defect]{lang="EN-US"}]{#struct_0_13803_16300_x47574350}[：表示从远端接收到的缺陷]{style="font-family:宋体"}

[[Holdoff time]{lang="EN-US"}]{#struct_0_13803_16300_2106029885}

[[倒换延迟时间，及当前的倒换延迟剩余时间，单位为秒]{style="font-family:宋体"}]{#struct_0_13803_16300_836743743}

[[Wait to testore time]{lang="EN-US"}]{#struct_0_13803_16300_990420269}

[[回切时间，及当前的回切剩余时间，单位为秒]{style="font-family:宋体"}]{#struct_0_13803_16300_x501524347}

[[Message interval]{lang="EN-US"}]{#struct_0_13803_16300_117359538}

[[PSC]{lang="EN-US"}]{#struct_0_13803_16300_836809279}[控制报文的发送时间间隔，单位为秒]{style="font-family:宋体"}

[[Revertive mode]{lang="EN-US"}]{#struct_0_13803_16300_1988318868}

[[回切模式，取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_576574139}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Revertive]{lang="EN-US"}]{#struct_0_13803_16300_836219454}[：支持回切]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-revertive]{lang="EN-US"}]{#struct_0_13803_16300_x1895153692}[：不支持回切]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13803_16300_x600792657}

[[本字段的取值由三部分组成：保护组的当前状态、进入该状态的原因及原因的来源]{style="font-family:宋体"}]{#struct_0_13803_16300_836284990}

[[保护组的当前状态取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_1710308896}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal (N)]{lang="EN-US"}]{#struct_0_13803_16300_x1052726762}[：表示工作隧道和保护隧道都正常工作，流量在工作隧道上传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unavailable (UA)]{lang="EN-US"}]{#struct_0_13803_16300_836350526}[：表示保护隧道不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protecting administrative (PA)]{lang="EN-US"}]{#struct_0_13803_16300_x319114219}[：表示执行外部倒换命令使得流量在保护隧道上传输]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protecting failure]{lang="EN-US"}]{#struct_0_13803_16300_998483079}[ ]{lang="EN-US"}[(PF)]{lang="EN-US"}[：表示工作隧道出现故障，流量倒换到保护隧道上传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-to-Restore (WTR)]{lang="EN-US"}]{#struct_0_13803_16300_836416062}[：表示工作隧道故障恢复后，等待]{style="font-family:宋体"}[WTR]{lang="EN-US"}[时间将流量从保护隧道回切到工作隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Do-not-Revert (DNR)]{lang="EN-US"}]{#struct_0_13803_16300_x825856650}[：表示工作隧道故障恢复后，不将流量从保护隧道回切到工作隧道]{style="font-family:宋体"}

[[保护组进入某个状态的原因包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_969152673}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lockout of protection]{lang="EN-US"}]{#struct_0_13803_16300_835957310}[ ]{lang="EN-US"}[(]{lang="EN-US"}[LO]{lang="EN-US"}[)]{lang="EN-US"}[：表示执行锁定倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protection tunnel failure]{lang="EN-US"}]{#struct_0_13803_16300_90431620}[ ]{lang="EN-US"}[(]{lang="EN-US"}[P]{lang="EN-US"}[)]{lang="EN-US"}[：表示通过信令协议检测到保护隧道出现故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Working tunnel failure]{lang="EN-US"}]{#struct_0_13803_16300_836022846}[ ]{lang="EN-US"}[(]{lang="EN-US"}[W]{lang="EN-US"}[)]{lang="EN-US"}[：表示通过信令协议检测到工作隧道出现故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forced switch]{lang="EN-US"}]{#struct_0_13803_16300_1421658301}[ ]{lang="EN-US"}[(]{lang="EN-US"}[F]{lang="EN-US"}[)]{lang="EN-US"}[：表示执行强制倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual switch]{lang="EN-US"}]{#struct_0_13803_16300_x1922639754}[ ]{lang="EN-US"}[(]{lang="EN-US"}[M]{lang="EN-US"}[)]{lang="EN-US"}[：表示执行手工倒换命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold off]{lang="EN-US"}]{#struct_0_13803_16300_836088382}[ ]{lang="EN-US"}[(]{lang="EN-US"}[HO]{lang="EN-US"}[)]{lang="EN-US"}[：表示工作隧道出现故障后，等待倒换延迟时间，再将流量切换到保护隧道上传输]{style="font-family:宋体"}

[[原因的来源包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_596954156}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_13803_16300_698726346}[ ]{lang="EN-US"}[(]{lang="EN-US"}[L]{lang="EN-US"}[)]{lang="EN-US"}[：表示来自于本地]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote]{lang="EN-US"}]{#struct_0_13803_16300_836153918}[ ]{lang="EN-US"}[(]{lang="EN-US"}[R]{lang="EN-US"}[)]{lang="EN-US"}[：表示来自于远端]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-871041182 .myid}
[]{#_Toc404791787}[]{#struct_0_13803_16300_x47246670}[]{#_Toc359419181}[]{#_Toc360433712}[]{#_Toc360433713}[]{#_Toc360433714}[]{#_Toc360433715}[]{#_Toc293393940}[]{#_Toc293393941}[]{#_Toc293393942}[]{#_Toc293393943}[]{#_Toc293393944}[]{#_Toc293393945}[]{#_Toc293393946}[]{#_Toc293393947}[]{#_Toc293393948}[]{#_Toc293393949}[]{#_Toc293393950}[]{#_Toc293393951}[]{#_Toc293393952}[]{#_Toc293393953}[]{#_Toc293393954}[]{#_Toc293393955}[]{#_Toc293393958}[]{#_Toc293393959}[]{#_Toc293393975}[]{#_Toc293393976}[]{#_Toc293393978}[]{#_Toc293393979}[]{#_Toc293393980}[]{#_Toc293393981}[]{#_Toc293393994}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display tunnel-bundle**

------------------------------------------------------------------------

[**[display tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_1044758049}[命令用来显示]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口及其成员接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x229447599}

[**[display tunnel-bundle ]{lang="EN-US"}**[\[ *number*]{lang="EN-US"}]{#struct_0_13803_16300_836743742}**[ ]{lang="EN-US"}**[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_990420268}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13803_16300_x501524346}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_117294002}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x42257442}

[[network-operator]{lang="EN-US"}]{#struct_0_13803_16300_362557131}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_848142428}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13803_16300_912810747}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_836809278}

[*[number]{lang="EN-US"}*]{#struct_0_13803_16300_1988318867}[：显示指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口及其成员接口的信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号，取值为已经创建的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号。如果不指定本参数，则显示所有]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口及其成员接口的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_576377531}

[[\# ]{lang="PT-BR"}]{#struct_0_13803_16300_1336576628}[显示所有]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口及其成员口的信息。]{style="font-family:宋体"}[]{#_Ref329182139}

[[\<Sysname\> display tunnel-bundle]{lang="EN-US"}]{#struct_0_13803_16300_836219453}

[Total number of tunnel bundles: 1, 1 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Tunnel bundle name: Tunnel-Bundle 2]{lang="EN-US"}

[Bundle state           : Up]{lang="EN-US"}

[Bundle attributes      :]{lang="EN-US"}

[  Working mode         : 1:1]{lang="EN-US"}

[  Tunnel type          : CR-LSP]{lang="EN-US"}

[  Tunnel destination   : 3.3.3.3]{lang="EN-US"}

[Bundle members:]{lang="EN-US"}

[  Member         State        Role]{lang="EN-US"}

[  Tunnel4        Up           Working]{lang="EN-US"}

[  Tunnel5        Up           Protection]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display tunnel-bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1895153695}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1671931476}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_13803_16300_1321521644}
:::

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_13803_16300_1945675732}

[[Total number of tunnel bundles]{lang="EN-US"}]{#struct_0_13803_16300_x293542464}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x480232238}[接口的总数，以及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口数目]{style="font-family:宋体"}

[[Tunnel bundle name]{lang="EN-US"}]{#struct_0_13803_16300_172317455}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_836284989}[接口的名称]{style="font-family:宋体"}

[[Bundle state]{lang="EN-US"}]{#struct_0_13803_16300_x628343271}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x631611680}[接口的状态，取值包括]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Bundle attributes]{lang="EN-US"}]{#struct_0_13803_16300_2013687361}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_1800826243}[接口的属性]{style="font-family:宋体"}

[[Working mode]{lang="EN-US"}]{#struct_0_13803_16300_836350525}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x319114222}[接口的模式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Load Balancing]{lang="EN-US"}]{#struct_0_13803_16300_997893252}[：表示负载分担模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1+1]{lang="EN-US"}]{#struct_0_13803_16300_45759788}[：表示]{style="font-family:宋体"}[1+1]{lang="EN-US"}[保护倒换模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1:1]{lang="EN-US"}]{#struct_0_13803_16300_x1071611962}[：表示]{style="font-family:宋体"}[1:1]{lang="EN-US"}[保护倒换模式]{style="font-family:宋体"}

[[Load Balancing]{lang="EN-US"}]{#struct_0_13803_16300_836416061}[模式的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}["]{style="font-family:宋体"}

[[Tunnel type]{lang="EN-US"}]{#struct_0_13803_16300_x825856653}

[[隧道类型，目前取值仅支持]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_13803_16300_969349281}

[[Tunnel destination]{lang="EN-US"}]{#struct_0_13803_16300_1225886875}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_835957309}[接口的隧道目的端地址]{style="font-family:宋体"}

[[Bundle members]{lang="EN-US"}]{#struct_0_13803_16300_x1865883525}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1723403245}[接口中的成员接口信息]{style="font-family:宋体"}

[[Member]{lang="EN-US"}]{#struct_0_13803_16300_2054190368}

[[成员接口的名称]{style="font-family:宋体"}]{#struct_0_13803_16300_836022845}

[[State]{lang="EN-US"}]{#struct_0_13803_16300_1421658300}

[[成员接口的状态]{style="font-family:宋体"}]{#struct_0_13803_16300_x1922705290}

[[Role]{lang="EN-US"}]{#struct_0_13803_16300_x1291901646}

[[成员接口的角色，取值包括：]{style="font-family:宋体"}]{#struct_0_13803_16300_836088381}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Working]{lang="EN-US"}]{#struct_0_13803_16300_596954159}[：表示成员接口对应的隧道为工作隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protection]{lang="EN-US"}]{#struct_0_13803_16300_698726337}[：表示成员接口对应的隧道为保护隧道]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1590675272 .myid}
[]{#_Toc404791788}[]{#struct_0_13803_16300_x1569266413}[]{#_Toc359419172}[]{#_Toc360433717}[]{#_Toc360433749}[]{#_Toc360433750}[]{#_Toc360433751}[]{#_Toc360433752}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- interface tunnel-bundle protection**

------------------------------------------------------------------------

[]{#struct_0_13803_16300_197754447}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}[]{#_Toc137103150}[]{#_Toc297726930}[]{#_Toc347996122}[]{#_Toc345166888}[]{#_Toc85816095}[]{#_Toc85816096}[]{#_Toc85816097}[]{#_Toc85816098}[]{#_Toc85816099}[]{#_Toc85816100}[]{#_Toc85816101}[]{#_Toc85816102}[]{#_Toc85816103}[]{#_Toc85816104}[]{#_Toc85816105}[]{#_Toc85816106}[]{#_Toc85816107}[]{#_Toc85816108}[]{#_Toc85816109}[]{#_Toc85816110}[]{#_Toc85816111}[]{#_Toc85816112}[]{#_Toc85816113}[]{#_Toc85816114}[]{#_Toc85816115}[]{#_Toc85816116}[]{#_Toc85816117}[]{#_Toc85816118}[]{#_Toc85816119}[]{#_Toc85816120}[]{#_Toc85816121}[]{#_Toc85816122}[]{#_Toc85816123}[]{#_Toc85816124}[]{#_Toc85816125}[]{#_Toc85816126}[]{#_Toc37747171}[]{#_Hlt23321500}[]{#_Hlt9334992}[]{#_Toc85816127}[]{#_Toc85816129}[]{#_Toc85816130}[]{#_Toc85816131}[]{#_Toc85816138}[]{#_Toc85816139}[]{#_Toc85816140}[]{#_Toc85816141}[]{#_Toc85816142}[]{#_Toc85816156}[]{#_Toc85816157}[]{#_Toc85816158}[]{#_Toc85816159}[]{#_Toc85816166}[]{#_Toc85816167}[]{#_Toc85816168}[]{#_Toc85816169}[]{#_Toc85816182}[]{#_Toc85816183}[]{#_Toc85816204}[]{#_Toc85816205}[]{#_Toc85816206}[]{#_Toc85816207}[]{#_Toc85816208}[]{#_Toc85816209}[]{#_Toc85816210}[]{#_Toc85816211}[]{#_Toc85816212}[]{#_Toc85816213}[]{#_Toc85816214}[]{#_Toc85816227}[]{#_Toc85816228}[]{#_Toc85816229}[]{#_Toc85816230}[]{#_Toc85816231}[]{#_Toc85816232}[]{#_Toc85816233}[]{#_Toc85816240}[]{#_Toc85816241}[]{#_Toc85816242}[]{#_Toc85816243}[]{#_Toc85816244}[]{#_Toc85816245}[]{#_Toc85816246}[]{#_Toc85816247}[]{#_Toc85816248}[]{#_Toc85816249}[]{#_Toc85816250}[]{#_Toc85816251}[]{#_Toc85816252}[]{#_Toc85816253}[]{#_Toc85816254}[]{#_Toc85816255}[]{#_Toc85816256}[]{#_Toc85816257}[]{#_Toc85816258}[]{#_Toc85816268}[]{#_Toc85816269}[]{#_Toc85816270}[]{#_Toc85816271}[]{#_Toc85816272}[]{#_Toc85816273}[]{#_Toc85816274}[]{#_Toc85816281}[]{#_Toc85816282}[]{#_Toc85816283}[]{#_Toc85816284}[]{#_Toc85816306}[]{#_Toc85816307}[]{#_Toc85816308}[]{#_Toc85816309}[]{#_Toc85816337}[]{#_Toc85816338}[]{#_Toc85816340}[]{#_Toc85816341}[]{#_Toc85816342}[]{#_Toc85816352}[]{#_Toc85816353}[]{#_Toc85816354}[]{#_Toc85816355}[]{#_Toc85816356}[]{#_Toc85816357}[]{#_Toc85816358}[]{#_Toc85816359}[]{#_Toc85816360}[]{#_Toc85816361}[]{#_Toc85816362}[]{#_Toc85816363}[]{#_Toc85816364}[]{#_Toc85816365}[]{#_Toc85816366}[]{#_Toc85816367}[]{#_Toc85816368}[]{#_Toc85816399}[]{#_Toc85816400}[]{#_Toc85816401}[]{#_Toc85816403}[]{#_Toc85816408}[]{#_Toc85816409}[]{#_Toc85816410}[]{#_Toc85816411}[]{#_Toc85816412}[]{#_Toc85816413}[]{#_Toc85816423}[]{#_Toc85816424}[]{#_Toc85816425}[]{#_Toc85816426}[]{#_Toc85816427}[]{#_Toc85816455}[]{#_Toc85816456}[]{#_Toc85816457}[]{#_Hlt15267207}[]{#_Toc85816458}[]{#_Toc85816459}[]{#_Toc85816460}[]{#_Toc85816461}[]{#_Toc85816462}[]{#_Toc85816463}[]{#_Toc85816464}[]{#_Toc85816465}[]{#_Toc85816467}[]{#_Toc85816468}[]{#_Toc85816469}[]{#_Toc85816470}[]{#_Toc85816471}[]{#_Toc85816472}[]{#_Toc85816473}[]{#_Toc85816474}[]{#_Toc85816475}[]{#_Toc85816476}[]{#_Toc85816477}[]{#_Toc85816478}[]{#_Toc85816479}[]{#_Toc85816480}[]{#_Toc85816481}[]{#_Toc85816482}[]{#_Toc85816483}[]{#_Toc85816484}[]{#_Toc85816485}[]{#_Toc85816645}[]{#_Toc85816646}[]{#_Toc85816647}[]{#_Toc85816648}[]{#_Toc85816649}[]{#_Toc85816650}[]{#_Toc85816651}[]{#_Toc85816652}[]{#_Toc85816653}[]{#_Toc85816654}[]{#_Toc85816655}[]{#_Toc85816656}[]{#_Toc85816657}[]{#_Toc85816658}[]{#_Toc85816659}[]{#_Toc85816675}[]{#_Toc85816676}[]{#_Toc85816677}[]{#_Toc85816678}[]{#_Toc85816680}[]{#_Toc85816683}[]{#_Toc85816685}[]{#_Toc85816686}[]{#_Toc85816687}[]{#_Toc85816689}[]{#_Toc85816694}[]{#_Toc85816695}[]{#_Toc85816696}[]{#_Toc85816699}[]{#_Toc85816702}[]{#_Toc85816703}[]{#_Hlt15796603}[]{#_Toc85816704}[]{#_Toc85816705}[]{#_Toc85816706}[]{#_Toc85816707}[]{#_Toc85816708}[]{#_Toc85816709}[]{#_Toc85816710}[]{#_Toc85816713}[]{#_Toc85816714}[]{#_Toc85816715}[]{#_Toc85816716}[]{#_Toc85816717}[]{#_Toc85816718}[]{#_Toc85816719}[]{#_Toc85816720}[]{#_Toc85816721}[]{#_Toc85816722}[]{#_Toc85816723}[]{#_Toc85816742}[]{#_Toc85816743}[]{#_Toc85816744}[]{#_Toc85816745}[]{#_Toc85816752}[]{#_Toc85816753}[]{#_Toc85816754}[]{#_Toc85816755}[]{#_Toc85816774}[]{#_Toc85816775}[]{#_Toc85816776}[]{#_Toc85816777}[]{#_Toc85816787}[]{#_Toc85816788}[]{#_Toc85816789}[]{#_Toc85816790}[]{#_Toc85816791}[]{#_Toc85816792}[]{#_Toc85816793}[]{#_Toc85816794}[]{#_Toc85816795}[]{#_Toc85816796}[]{#_Toc85816797}[]{#_Toc85816816}[]{#_Hlt24806861}[]{#_Toc85816817}[]{#_Toc85816818}[]{#_Toc85816819}[]{#_Toc85816820}[]{#_Toc85816851}[]{#_Toc85816852}[]{#_Toc85816853}[]{#_Toc85816854}[]{#_Toc85816861}[]{#_Toc37747192}[]{#_Toc37747193}[]{#_Toc37747194}[]{#_Toc37747195}[]{#_Toc37747202}[]{#_Toc85816862}[]{#_Toc85816863}[]{#_Toc85816864}[]{#_Toc85816865}[]{#_Toc85816872}[]{#_Toc85816873}[]{#_Toc85816874}[]{#_Toc85816875}[]{#_Toc85816878}[]{#_Toc85816881}[]{#_Toc85816883}[]{#_Toc85816884}[]{#_Hlt23751682}[]{#_Hlt12087209}[]{#_Toc85816885}[]{#_Toc85816886}[]{#_Toc85816887}[]{#_Toc85816888}[]{#_Toc85816889}[]{#_Toc85816890}[]{#_Toc85816891}[]{#_Toc85816892}[]{#_Toc85816893}[]{#_Toc85816894}[]{#_Toc85816895}[]{#_Toc85816896}[]{#_Toc85816897}[]{#_Toc85816898}[]{#_Toc85816899}[]{#_Toc85816909}[]{#_Toc85816910}[]{#_Toc85816911}[]{#_Toc85816912}[]{#_Toc85816913}[]{#_Toc85816914}[]{#_Toc85816930}[]{#_Toc85816931}[]{#_Toc85816932}[]{#_Toc85816933}[]{#_Toc85816935}[]{#_Toc85816937}[]{#_Toc85816939}[]{#_Toc85816940}[]{#_Toc85816941}[]{#_Toc85816942}[]{#_Toc85816943}[]{#_Toc85816944}[]{#_Toc85816945}[]{#_Toc85816955}[]{#_Toc85816956}[]{#_Toc85816957}[]{#_Toc85816958}[]{#_Toc85816959}[]{#_Toc85816960}[]{#_Toc85816970}[]{#_Toc85816971}[]{#_Toc85816972}[]{#_Toc85816973}[]{#_Toc85816983}[]{#_Toc85816984}[]{#_Hlt25036508}[]{#_Toc85816985}[]{#_Toc85816986}[]{#_Hlt25036644}[]{#_Toc85816987}[]{#_Toc85816988}[]{#_Hlt24620344}[]{#_Hlt24620750}[]{#_Toc85816989}[]{#_Toc85816990}[]{#_Toc85816991}[]{#_Toc85816992}[]{#_Toc85816993}[]{#_Toc85816994}[]{#_Toc85816995}[]{#_Toc85816996}[]{#_Toc85816997}[]{#_Toc85816998}[]{#_Toc85816999}[]{#_Toc85817000}[]{#_Hlt24621022}[]{#_Toc85817001}[]{#_Toc85817009}[]{#_Toc85817010}[]{#_Toc85817011}[]{#_Toc85817012}[]{#_Toc85817022}[]{#_Toc85817029}[]{#_Toc85817030}[]{#_Toc85817031}[]{#_Hlt24797856}[]{#_Toc85817032}[]{#_Toc85817033}[]{#_Toc85817034}[]{#_Toc85817035}[]{#_Toc85817036}[]{#_Toc85817037}[]{#_Toc85817038}[]{#_Toc85817039}[]{#_Toc85817040}[]{#_Toc85817041}[]{#_Toc85817051}[]{#_Toc85817052}[]{#_Toc85817053}[]{#_Toc85817054}[]{#_Toc85817055}[]{#_Toc85817056}[]{#_Toc85817057}[]{#_Toc85817058}[]{#_Toc85817065}[]{#_Toc85817066}[]{#_Toc85817067}[]{#_Toc85817068}[]{#_Toc85817069}[]{#_Toc85817079}[]{#_Toc85817080}[]{#_Toc85817081}[]{#_Toc85817082}[]{#_Toc85817083}[]{#_Toc85817084}[]{#_Toc85817085}[]{#_Toc85817086}[]{#_Toc85817087}[]{#_Toc85817088}[]{#_Toc85817089}[]{#_Toc85817090}[]{#_Toc85817091}[]{#_Toc85817092}[]{#_Toc85817105}[]{#_Toc85817106}[]{#_Toc85817107}[]{#_Toc85817108}[]{#_Toc85817109}[]{#_Toc85817110}[]{#_Toc85817111}[]{#_Toc85817112}[]{#_Toc85817119}[]{#_Toc85817120}[]{#_Toc85817121}[]{#_Toc85817122}[]{#_Toc85817123}[]{#_Toc85817124}[]{#_Toc85817125}[]{#_Toc85817126}[]{#_Toc85817127}[]{#_Toc85817128}[]{#_Toc85817129}[]{#_Toc85817136}[]{#_Toc85817137}[]{#_Toc85817138}[]{#_Toc85817139}[]{#_Toc85817140}[]{#_Toc85817141}[]{#_Toc85817142}[]{#_Toc85817143}[]{#_Toc85817144}[]{#_Toc85817149}[]{#_Toc85817150}[]{#_Toc85817151}[]{#_Toc85817152}[]{#_Toc85817153}[]{#_Toc85817154}[]{#_Toc85817155}[]{#_Toc85817156}[]{#_Toc85817157}[]{#_Toc85817158}[]{#_Toc85817159}[]{#_Toc85817160}[]{#_Toc85817161}[]{#_Toc85817163}[]{#_Toc85817164}[]{#_Toc85817165}[]{#_Toc85817166}[]{#_Toc85817167}[]{#_Toc85817168}[]{#_Toc85817169}[]{#_Toc85817170}[]{#_Toc85817171}[]{#_Toc85817172}[]{#_Toc85817173}[]{#_Toc85817174}[]{#_Toc85817175}[]{#_Toc85817176}[]{#_Toc85817177}[]{#_Toc85817178}[]{#_Toc85817179}[]{#_Toc85817180}[]{#_Toc85817181}[]{#_Toc85817182}[]{#_Toc85817183}[]{#_Toc85817184}[]{#_Toc85817185}[]{#_Toc85817186}[]{#_Toc85817187}[]{#_Toc85817188}[]{#_Toc85817189}[]{#_Toc85817190}[]{#_Toc85817191}[]{#_Toc85817192}[]{#_Toc85817193}[]{#_Toc85817194}[]{#_Toc85817195}[]{#_Toc85817196}[]{#_Toc85817203}[]{#_Toc85817204}[]{#_Toc85817207}[]{#_Toc85817208}[]{#_Toc85817209}[]{#_Toc85817210}[]{#_Toc85817211}[]{#_Toc85817212}[]{#_Toc85817213}[]{#_Toc85817214}[]{#_Toc85817215}[]{#_Toc85817216}[]{#_Toc85817217}[]{#_Toc85817227}[]{#_Toc85817228}[]{#_Toc85817239}[]{#_Toc85817240}[]{#_Toc85817241}[]{#_Toc85817251}[]{#_Toc85817252}[]{#_Toc85817253}[]{#_Toc85817254}[]{#_Toc85817255}[]{#_Toc85817256}[]{#_Toc85817257}[]{#_Toc85817258}[]{#_Toc85817268}[]{#_Toc85817269}[]{#_Toc85817270}[]{#_Toc85817271}[]{#_Toc85817272}[]{#_Toc85817273}[]{#_Toc85817274}[]{#_Toc85817275}[]{#_Toc85817276}[]{#_Toc85817277}[]{#_Toc85817287}[]{#_Toc85817288}[]{#_Toc85817289}[]{#_Toc85817290}[]{#_Toc85817300}[]{#_Toc85817301}[]{#_Toc85817302}[]{#_Toc85817303}[]{#_Toc85817304}[]{#_Toc85817305}[]{#_Toc85817306}[]{#_Toc85817316}[]{#_Toc85817317}[]{#_Toc85817318}[]{#_Toc85817319}[]{#_Toc85817320}[]{#_Toc85817321}[]{#_Toc85817324}[]{#_Toc85817326}[]{#_Toc85817327}[]{#_Toc85817337}[]{#_Toc85817338}[]{#_Toc85817339}[]{#_Toc85817340}[]{#_Toc85817341}[]{#_Toc85817348}[]{#_Toc85817352}[]{#_Toc85817353}[]{#_Toc85817354}[]{#_Toc85817364}[]{#_Toc85817365}[]{#_Toc85817366}[]{#_Toc85817367}[]{#_Toc85817368}[]{#_Toc85817369}[]{#_Toc85817379}[]{#_Toc85817380}[]{#_Toc85817381}[]{#_Toc85817382}[]{#_Toc85817383}[]{#_Toc85817405}[]{#_Toc85817406}[]{#_Toc85817408}[]{#_Toc85817409}[]{#_Toc85817410}[]{#_Toc85817411}[]{#_Toc85817418}[]{#_Toc85817419}[]{#_Toc85817420}[]{#_Toc85817421}[]{#_Toc85817422}[]{#_Toc85817423}[]{#_Toc85817424}[]{#_Toc85817425}[]{#_Toc85817426}[]{#_Toc85817427}[]{#_Toc85817428}[]{#_Toc85817429}[]{#_Toc85817430}[]{#_Toc85817431}[]{#_Toc85817441}[]{#_Toc85817442}[]{#_Toc85817443}[]{#_Toc85817444}[]{#_Toc85817445}[]{#_Toc85817447}[]{#_Toc85817448}[]{#_Toc85817449}[]{#_Toc85817450}[]{#_Toc85817451}[]{#_Toc85817461}[]{#_Toc85817462}[]{#_Toc85817463}[]{#_Toc85817464}[]{#_Toc85817465}[]{#_Toc85817466}[]{#_Toc85817476}[]{#_Toc85817477}[]{#_Toc85817478}[]{#_Toc85817479}[]{#_Toc85817480}[]{#_Toc85817487}[]{#_Toc85817488}[]{#_Toc85817489}[]{#_Toc85817490}[]{#_Toc85817497}[]{#_Toc85817498}[]{#_Toc85817499}[]{#_Toc85817500}[]{#_Toc85817501}[]{#_Toc85817502}[]{#_Toc85817503}[]{#_Toc85817504}[]{#_Toc85817505}[]{#_Toc85817506}[]{#_Toc85817507}[]{#_Toc85817508}[]{#_Toc85817509}[]{#_Toc85817510}[]{#_Toc85817511}[]{#_Toc85817512}[]{#_Toc85817513}[]{#_Toc85817514}[]{#_Toc85817515}[]{#_Toc85817516}[]{#_Toc85817537}[]{#_Toc85817538}[]{#_Toc85817539}[]{#_Toc85817540}[]{#_Toc85817541}[]{#_Toc85817542}[]{#_Toc85817543}[]{#_Toc85817544}[]{#_Toc85817545}[]{#_Toc85817546}[]{#_Toc85817547}[]{#_Toc85817548}[]{#_Toc85817549}[]{#_Toc85817550}[]{#_Toc85817551}[]{#_Toc85817552}[]{#_Toc85817553}[]{#_Toc85817554}[]{#_Toc85817555}[]{#_Toc85817556}[]{#_Toc85817566}[]{#_Toc85817567}[]{#_Toc85817568}[]{#_Toc85817569}[]{#_Toc85817570}[]{#_Toc85817571}[]{#_Toc85817572}[]{#_Toc85817573}[]{#_Toc85817574}[]{#_Toc85817575}[]{#_Toc85817585}[]{#_Toc85817586}[]{#_Toc85817587}[]{#_Toc85817588}[]{#_Toc85817589}[]{#_Toc85817590}[]{#_Toc85817600}[]{#_Toc85817601}[]{#_Toc85817602}[]{#_Toc85817603}[]{#_Toc85817604}[]{#_Toc85817605}[]{#_Toc85817606}[]{#_Toc85817607}[]{#_Toc85817617}[]{#_Toc85817618}[]{#_Toc85817619}[]{#_Toc85817620}[]{#_Toc85817622}[]{#_Toc85817623}[]{#_Toc85817624}[]{#_Toc85817625}[]{#_Toc85817626}[]{#_Toc85817636}[]{#_Toc85817637}[]{#_Toc85817638}[]{#_Toc85817639}[]{#_Toc85817640}[]{#_Toc85817641}[]{#_Toc85817642}[]{#_Toc85817643}[]{#_Toc85817644}[]{#_Toc85817657}[]{#_Toc85817658}[]{#_Toc85817659}[]{#_Toc85817660}[]{#_Toc85817661}[]{#_Toc85817662}[]{#_Toc85817663}[]{#_Toc85817664}[]{#_Toc85817665}[]{#_Toc85817666}[]{#_Toc85817667}[]{#_Toc85817671}[]{#_Toc85817672}[]{#_Hlt21938307}[]{#_Toc85817673}[]{#_Toc85817674}[]{#_Toc85817675}[]{#_Toc85817676}[]{#_Toc85817677}[]{#_Toc85817678}[]{#_Toc85817679}[]{#_Toc85817680}[]{#_Toc85817681}[]{#_Toc85817682}[]{#_Toc85817683}[]{#_Toc85817684}[]{#_Toc85817685}[]{#_Toc85817686}[]{#_Toc85817687}[]{#_Toc85817688}[]{#_Toc85817689}[]{#_Toc85817690}[]{#_Toc85817691}[]{#_Toc85817692}[]{#_Toc85817693}[]{#_Toc85817694}[]{#_Toc85817695}[]{#_Toc85817696}[]{#_Toc85817697}[]{#_Toc85817698}[]{#_Toc85817699}[]{#_Toc85817700}[]{#_Toc85817701}[]{#_Toc85817702}[]{#_Toc85817703}[]{#_Hlt15977823}[]{#_Toc85817704}[]{#_Toc85817705}[]{#_Toc85817706}[]{#_Toc85817707}[]{#_Toc85817708}[]{#_Toc85817709}[]{#_Toc85817710}[]{#_Toc85817711}[]{#_Toc85817712}[]{#_Toc85817713}[]{#_Toc85817714}[]{#_Toc85817715}[]{#_Toc85817725}[]{#_Toc85817726}[]{#_Toc85817727}[]{#_Toc85817728}[]{#_Toc85817729}[]{#_Toc85817730}[]{#_Toc85817740}[]{#_Toc85817741}[]{#_Hlt23405451}[]{#_Toc85817742}[]{#_Toc85817743}[]{#_Toc85817744}[]{#_Toc85817745}[]{#_Toc85817755}[]{#_Toc85817756}[]{#_Toc85817757}[]{#_Toc85817758}[]{#_Toc85817759}[]{#_Toc85817760}[]{#_Toc85817770}[]{#_Toc85817771}[]{#_Toc85817772}[]{#_Toc85817773}[]{#_Toc85817774}[]{#_Toc85817784}[]{#_Toc85817785}[]{#_Toc85817786}[]{#_Toc85817787}[]{#_Toc85817788}[]{#_Toc85817789}[]{#_Toc85817790}[]{#_Toc85817800}[]{#_Toc85817801}[]{#_Toc56323509}[]{#_Toc56323510}[]{#_Toc56323511}[]{#_Toc56323512}[]{#_Toc56323522}[]{#_Toc56323523}[]{#_Toc85817802}[]{#_Toc85817803}[]{#_Toc85817804}[]{#_Toc85817805}[]{#_Toc85817815}[]{#_Toc85817816}[]{#_Toc85817817}[]{#_Toc85817818}[]{#_Toc85817819}[]{#_Toc85817829}[]{#_Toc85817830}[]{#_Toc85817831}[]{#_Toc85817832}[]{#_Toc85817833}[]{#_Toc85817834}[]{#_Toc85817844}[]{#_Toc85817845}[]{#_Toc85817846}[]{#_Toc85817847}[]{#_Toc85817848}[]{#_Toc85817849}[]{#_Toc85817859}[]{#_Toc85817860}[]{#_Toc85817861}[]{#_Hlt25378447}[]{#_Toc85817863}[]{#_Toc85817864}[]{#_Toc85817874}[]{#_Toc85817875}[]{#_Toc85817876}[]{#_Toc85817877}[]{#_Toc85817878}[]{#_Toc85817879}[]{#_Toc85817889}[]{#_Toc85817890}[]{#_Toc56323530}[]{#_Toc56323531}[]{#_Toc56323532}[]{#_Toc56323533}[]{#_Toc56323543}[]{#_Toc56323544}[]{#_Toc85817891}[]{#_Toc85817892}[]{#_Toc85817893}[]{#_Toc85817894}[]{#_Toc85817904}[]{#_Toc85817905}[]{#_Toc85817906}[]{#_Toc85817907}[]{#_Toc85817908}[]{#_Toc85817909}[]{#_Toc85817910}[]{#_Toc85817911}[]{#_Toc85817912}[]{#_Toc85817913}[]{#_Toc85817923}[]{#_Toc85817924}[]{#_Toc85817925}[]{#_Toc85817926}[]{#_Toc85817927}[]{#_Toc85817928}[]{#_Toc85817944}[]{#_Toc85817945}[]{#_Toc85817946}[]{#_Toc85817947}[]{#_Toc85817948}[]{#_Toc85817949}[]{#_Toc85817950}[]{#_Toc85817951}[]{#_Toc85817952}[]{#_Toc85817954}[]{#_Toc85817956}[]{#_Toc85817957}[]{#_Toc85817959}[]{#_Toc85817961}[]{#_Toc85817963}[]{#_Toc85817964}[]{#_Toc85817966}[]{#_Toc85817969}[]{#_Toc85817975}[]{#_Toc85817976}[]{#_Toc85817981}[]{#_Toc85817982}[]{#_Toc85817983}[]{#_Toc85817984}[]{#_Toc85817985}[]{#_Toc85817986}[]{#_Toc85817987}[]{#_Toc85817989}[]{#_Toc85817991}[]{#_Toc85817992}[]{#_Toc85817994}[]{#_Toc85817998}[]{#_Toc85817999}[]{#_Toc85818001}[]{#_Toc85818003}[]{#_Toc85818005}[]{#_Toc85818006}[]{#_Toc85818012}[]{#_Toc85818013}[]{#_Toc85818018}[]{#_Toc85818019}[]{#_Toc85818020}[]{#_Toc85818021}[]{#_Toc85818022}[]{#_Toc85818023}[]{#_Toc85818024}[]{#_Toc85818026}[]{#_Toc85818028}[]{#_Toc85818030}[]{#_Toc85818032}[]{#_Toc85818035}[]{#_Toc85818041}[]{#_Toc85818043}[]{#_Toc85818046}[]{#_Toc85818047}[]{#_Toc85818053}[]{#_Toc85818054}[]{#_Toc85818059}[]{#_Toc85818060}[]{#_Toc85818061}[]{#_Toc85818062}[]{#_Toc85818063}[]{#_Toc85818064}[]{#_Toc85818065}[]{#_Toc85818067}[]{#_Toc85818069}[]{#_Toc85818071}[]{#_Toc85818073}[]{#_Toc85818075}[]{#_Toc85818076}[]{#_Toc85818077}[]{#_Toc85818079}[]{#_Toc85818082}[]{#_Toc85818083}[]{#_Toc85818084}[]{#_Toc85818086}[]{#_Toc85818088}[]{#_Toc85818089}[]{#_Toc85818091}[]{#_Toc85818092}[]{#_Toc85818093}[]{#_Toc85818094}[]{#_Toc85818095}[]{#_Toc85818098}[]{#_Toc85818100}[]{#_Toc85818101}[]{#_Toc85818103}[]{#_Toc85818104}[]{#_Toc85818105}[]{#_Toc85818107}[]{#_Toc85818108}[]{#_Toc85818109}[]{#_Toc85818110}[]{#_Toc85818111}[]{#_Toc85818112}[]{#_Toc85818113}[]{#_Toc85818114}[]{#_Toc85818116}[]{#_Toc85818118}[]{#_Toc85818120}[]{#_Toc85818122}[]{#_Toc85818125}[]{#_Toc85818127}[]{#_Toc85818132}[]{#_Toc85818134}[]{#_Toc85818136}[]{#_Toc85818138}[]{#_Toc85818139}[]{#_Toc85818145}[]{#_Toc85818146}[]{#_Toc85818151}[]{#_Toc85818152}[]{#_Toc85818153}[]{#_Toc85818154}[]{#_Toc85818155}[]{#_Toc85818156}[]{#_Toc85818157}[]{#_Toc85818159}[]{#_Toc85818161}[]{#_Toc85818164}[]{#_Toc85818166}[]{#_Toc85818168}[]{#_Toc85818170}[]{#_Toc85818172}[]{#_Toc85818173}[]{#_Toc85818174}[]{#_Toc85818175}[]{#_Toc85818177}[]{#_Toc85818179}[]{#_Toc85818181}[]{#_Toc85818187}[]{#_Toc85818188}[]{#_Toc85818189}[]{#_Toc85818190}[]{#_Toc85818191}[]{#_Toc85818192}[]{#_Toc85818193}[]{#_Toc85818195}[]{#_Toc85818196}[]{#_Toc85818197}[]{#_Toc85818198}[]{#_Toc85818199}[]{#_Toc85818209}[]{#_Toc85818213}[]{#_Toc85818217}[]{#_Toc85818221}[]{#_Toc85818225}[]{#_Toc85818229}[]{#_Toc85818233}[]{#_Toc85818237}[]{#_Toc85818241}[]{#_Toc85818245}[]{#_Toc85818249}[]{#_Toc85818253}[]{#_Toc85818257}[]{#_Toc85818261}[]{#_Toc85818269}[]{#_Toc85818273}[]{#_Toc85818277}[]{#_Toc85818281}[]{#_Toc85818285}[]{#_Toc85818286}[]{#_Toc85818287}[]{#_Toc85818288}[]{#_Toc85818289}[]{#_Toc85818290}[]{#_Toc85818291}[]{#_Toc85818292}[]{#_Toc85818293}[]{#_Toc85818294}[]{#_Toc85818295}[]{#_Toc85818296}[]{#_Hlt9156368}[]{#_Toc85818297}[]{#_Toc85818298}[]{#_Toc85818299}[]{#_Toc85818300}[]{#_Toc85818301}[]{#_Toc85818302}[]{#_Toc85818303}[]{#_Toc85818304}[]{#_Toc85818305}[]{#_Toc85818306}[]{#_Toc85818316}[]{#_Toc85818317}[]{#_Toc85818318}[]{#_Toc85818319}[]{#_Toc85818320}[]{#_Toc85818330}[]{#_Toc85818331}[]{#_Toc85818332}[]{#_Toc85818334}[]{#_Toc85818336}[]{#_Toc85818337}[]{#_Toc85818338}[]{#_Toc85818339}[]{#_Toc85818349}[]{#_Toc85818350}[]{#_Toc85818351}[]{#_Toc85818352}[]{#_Toc85818353}[]{#_Toc85818354}[]{#_Toc85818355}[]{#_Toc85818356}[]{#_Toc85818357}[]{#_Toc85818358}[]{#_Toc85818370}[]{#_Toc85818371}[]{#_Toc85818372}[]{#_Toc85818373}[]{#_Toc85818374}[]{#_Toc85818386}[]{#_Toc85818387}[]{#_Toc85818389}[]{#_Toc85818390}[]{#_Toc85818391}[]{#_Toc85818392}[]{#_Toc85818402}[]{#_Toc85818404}[]{#_Toc85818405}[]{#_Toc85818406}[]{#_Toc85818407}[]{#_Toc85818417}[]{#_Toc85818418}[]{#_Toc85818419}[]{#_Hlt23324581}[]{#_Toc85818420}[]{#_Toc85818421}[]{#_Hlt23741538}[]{#_Toc85818422}[]{#_Toc85818433}[]{#_Toc85818434}[]{#_Toc85818435}[]{#_Toc85818436}[]{#_Toc85818446}[]{#_Toc85818447}[]{#_Toc85818448}[]{#_Toc85818449}[]{#_Toc85818450}[]{#_Toc85818451}[]{#_Toc85818452}[]{#_Toc85818462}[]{#_Toc85818463}[]{#_Toc85818465}[]{#_Toc85818466}[]{#_Toc85818467}[]{#_Toc85818468}[]{#_Toc85818478}[]{#_Toc85818479}[]{#_Toc85818481}[]{#_Toc85818482}[]{#_Toc85818483}[]{#_Toc85818484}[]{#_Toc85818494}[]{#_Toc85818495}[]{#_Toc85818497}[]{#_Toc85818498}[]{#_Toc85818499}[]{#_Toc85818500}[]{#_Toc85818510}[]{#_Toc85818511}[]{#_Toc85818512}[]{#_Toc85818514}[]{#_Toc85818516}[]{#_Toc85818527}[]{#_Toc85818528}[]{#_Toc85818530}[]{#_Toc85818531}[]{#_Toc85818532}[]{#_Toc85818543}[]{#_Toc85818544}[]{#_Toc85818545}[]{#_Toc85818547}[]{#_Toc85818548}[]{#_Toc85818549}[]{#_Toc85818550}[]{#_Toc85818584}[]{#_Toc85818585}[]{#_Toc85818586}[]{#_Toc85818587}[]{#_Toc85818588}[]{#_Toc85818589}[]{#_Toc85818590}[]{#_Toc85818591}[]{#_Toc85818592}[]{#_Toc85818594}[]{#_Toc85818595}[]{#_Toc85818596}[]{#_Toc85818597}[]{#_Toc85818598}[]{#_Toc85818599}[]{#_Toc85818602}[]{#_Toc85818604}[]{#_Toc85818606}[]{#_Toc85818607}[]{#_Toc85818608}[]{#_Toc85818609}[]{#_Toc85818610}[]{#_Toc85818616}[]{#_Hlt25146204}[]{#_Hlt12271448}[]{#_Toc85818617}[]{#_Toc85818618}[]{#_Toc85818619}[]{#_Toc85818620}[]{#_Toc85818621}[]{#_Toc85818622}[]{#_Toc85818623}[]{#_Toc85818624}[]{#_Toc85818625}[]{#_Toc85818626}[]{#_Toc85818627}[]{#_Toc85818628}[]{#_Toc85818656}[]{#_Toc85818657}[]{#_Toc85818658}[]{#_Toc85818659}[]{#_Toc85818660}[]{#_Toc85818661}[]{#_Toc85818662}[]{#_Toc85818663}[]{#_Toc85818664}[]{#_Toc85818665}[]{#_Toc85818690}[]{#_Toc85818691}[]{#_Toc85818692}[]{#_Hlt15375565}[]{#_Toc85818693}[]{#_Toc85818694}[]{#_Toc85818695}[]{#_Toc85818696}[]{#_Toc85818697}[]{#_Toc85818698}[]{#_Toc85818699}[]{#_Toc85818700}[]{#_Toc85818701}[]{#_Toc85818702}[]{#_Toc85818703}[]{#_Toc85818704}[]{#_Toc85818717}[]{#_Toc85818718}[]{#_Toc85818719}[]{#_Toc85818720}[]{#_Toc85818721}[]{#_Toc85818722}[]{#_Toc85818723}[]{#_Toc85818733}[]{#_Toc85818734}[]{#_Toc85818738}[]{#_Toc85818739}[]{#_Toc85818740}[]{#_Toc85818741}[]{#_Toc85818742}[]{#_Toc85818743}[]{#_Toc85818744}[]{#_Toc85818745}[]{#_Toc85818746}[]{#_Toc85818747}[]{#_Toc85818748}[]{#_Toc85818764}[]{#_Toc85818765}[]{#_Toc85818766}[]{#_Toc85818767}[]{#_Toc85818768}[]{#_Toc85818769}[]{#_Toc85818770}[]{#_Toc85818774}[]{#_Toc85818777}[]{#_Hlt23410930}[]{#_Toc85818778}[]{#_Toc85818779}[]{#_Toc85818780}[]{#_Toc85818781}[]{#_Toc85818782}[]{#_Toc85818801}[]{#_Toc85818802}[]{#_Hlt23410927}[]{#_Toc85818803}[]{#_Toc85818804}[]{#_Toc85818805}[]{#_Toc85818806}[]{#_Toc85818807}[]{#_Toc85818808}[]{#_Toc85818809}[]{#_Toc85818810}[]{#_Toc85818811}[]{#_Toc85818812}[]{#_Toc85818813}[]{#_Toc85818814}[]{#_Toc85818815}[]{#_Toc85818816}[]{#_Toc85818817}[]{#_Toc85818818}[]{#_Toc85818819}**[interface tunnel-bundle protection]{lang="EN-US"}**[命令用来创建保护倒换模式的隧道捆绑接口（]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口），并进入]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_836153917}[命令]{style="font-family:
宋体"}[用来删除指定的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x936559408}

[**[interface tunnel-bundle]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_13803_16300_x47836495}**[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[protection ]{lang="EN-US"}**[{]{lang="EN-US"}**[ oneplusone]{lang="EN-US"}**[ \|]{lang="EN-US"}**[ onetoone }]{lang="EN-US"}**[ \]]{lang="EN-US"}

[**[undo interface tunnel-bundle]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_13803_16300_x1367681905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_751600244}

[[设备上不存在任何]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_665322092}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_1245579083}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13803_16300_x1149281106}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_836743741}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_990420271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_1837127805}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_192526123}

[*[number]{lang="EN-US"}*]{#struct_0_13803_16300_x407459654}[：]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[oneplusone]{lang="EN-US"}**]{#struct_0_13803_16300_x1594094888}[：指定为]{style="font-family:宋体"}[1+1]{lang="EN-US"}[保护倒换方式。]{style="font-family:宋体"}

[**[onetoone]{lang="EN-US"}**]{#struct_0_13803_16300_x1320733513}[：指定为]{style="font-family:宋体"}[1:1]{lang="EN-US"}[保护倒换方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x49719215}

[[创建保护倒换模式的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_836809277}[接口后，还需要在]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口视图下通过]{style="font-family:宋体"}**[member interface]{lang="EN-US"}**[命令为]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口指定两个成员接口：一个作为工作隧道，一个作为保护隧道。两条隧道形成一条具有保护作用的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[捆绑隧道，构成一个]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护组。在]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[保护组内，设备根据外部倒换命令、信令倒换，决定转发流量使用的隧道。]{style="font-family:宋体"}

[[MPLS]{lang="EN-US"}]{#struct_0_13803_16300_1988318862}[的保护倒换方式分为如下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1:1]{lang="EN-US"}]{#struct_0_13803_16300_576180923}[保护倒换：正常情况下，流量在工作隧道上传输；当隧道的头节点或尾节点通过检测机制（如]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[）发现工作隧道发生故障、或执行外部倒换命令时，通知头节点根据保护倒换状态决定流量在工作隧道或保护隧道上传输。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1+1]{lang="EN-US"}]{#struct_0_13803_16300_1505431845}[保护倒换：在正常情况下，流量在工作隧道、保护隧道上都传输，隧道的尾节点选择从工作隧道上接收流量；当隧道的头节点或尾节点通过检测机制（如]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[）发现工作隧道发生故障、或执行外部倒换命令时，通知隧道的尾节点根据保护倒换状态决定从工作隧道或保护隧道上接收流量。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13803_16300_1476040700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建保护倒换模式的]{lang="EN-US" style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x371247865}[接口时，必须指定]{lang="EN-US" style="font-family:宋体"}**[protection ]{lang="EN-US"}**[{ **oneplusone** \| **onetoone** }]{lang="EN-US"}[参数；进入已经创建的]{lang="EN-US" style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口时，可以不指定该参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能通过重复执行本命令，修改]{lang="EN-US" style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x418363170}[接口的保护倒换方式。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_325743730}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_1293479126}[创建]{style="font-family:宋体"}[1:1]{lang="EN-US"}[保护倒换方式的隧道捆绑接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_836219452}

[\[Sysname\] interface tunnel-bundle 2 protection onetoone]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1895153694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[destination]{lang="EN-US"}**]{#struct_0_13803_16300_x1407361711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tunnel bundle]{lang="EN-US"}**]{#struct_0_13803_16300_442505124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member interface]{lang="EN-US"}**]{#struct_0_13803_16300_x969763980}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_x138248384}
:::

::: {#857643302 .myid}
[]{#_Toc404791789}[]{#struct_0_13803_16300_x323516735}[]{#_Toc359419178}[]{#_Toc360433754}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- member interface**

------------------------------------------------------------------------

[**[member interface]{lang="EN-US"}**]{#struct_0_13803_16300_836284988}[命令用来为]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口指定成员接口。]{style="font-family:宋体"}

[**[undo member interface]{lang="EN-US"}**]{#struct_0_13803_16300_x628343272}[命令用来从]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口中删除指定的成员接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x631415072}

[**[member interface tunnel ]{lang="EN-US"}**]{#struct_0_13803_16300_70294418}*[tunnel-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[protection]{lang="EN-US"}**[ \]]{lang="EN-US"}

[**[undo member interface tunnel ]{lang="EN-US"}**]{#struct_0_13803_16300_918198260}*[tunnel-number]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_1017425197}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x400072071}[接口下不存在任何成员接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1991375035}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x1613774969}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_836350524}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x319114221}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_997958788}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_396990859}

[*[tunnel-number]{lang="EN-US"}*]{#struct_0_13803_16300_1917232468}[：指定成员接口。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号，本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[protection]{lang="EN-US"}**]{#struct_0_13803_16300_710941747}[：指定该成员接口为备用成员]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口，即该成员接口对应的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道为保护隧道。如果不指定本参数，则成员接口为主用成员接口，即该成员接口对应的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道为工作隧道。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_256927562}

[[保护倒换模式的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_682593809}[接口下只能指定两个成员接口：一个主用成员接口和一个备用成员接口。设备根据外部倒换命令、信令倒换，决定转发流量使用的成员接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_1344453585}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_836416060}[配置接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的主用成员接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[接口，备用成员接口为]{style="font-family:宋体"}[Tunnel2]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x825856652}

[\[Sysname\] interface tunnel-bundle 2 protection onetoone]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] member interface tunnel 1]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] member interface tunnel 2 protection]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_969283745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_824896476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_x992834528}
:::

::: {#163473464 .myid}
[]{#_Toc404791790}[]{#struct_0_13803_16300_x817301225}[]{#_Toc359419184}[]{#_Toc360433756}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- mpls protection**

------------------------------------------------------------------------

[**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_x269722205}[命令用来开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能，并进入]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换视图。]{style="font-family:宋体"}

[**[undo mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_835957308}[命令用来关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1865883524}

[**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_x157319304}

[**[undo mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_766648933}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_x239072989}

[[MPLS]{lang="EN-US"}]{#struct_0_13803_16300_836022844}[保护倒换功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_1421658299}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13803_16300_415488125}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_1682938376}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_836088380}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_596954158}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_698726336}

[[只有执行本命令开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_13803_16300_x1569266414}[保护倒换功能后，才能执行]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换的其他命令。]{style="font-family:宋体"}

[[如果没有开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_13803_16300_x561760440}[保护倒换功能，则保护倒换模式的隧道捆绑接口仅能按照指定的保护倒换方式进行流量转发。只有开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能后，才能进行]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换操作，如执行外部倒换命令、在隧道的两端协调保护倒换状态等。]{style="font-family:宋体"}

[[如果不开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_13803_16300_x1855381142}[保护倒换功能，则创建保护倒换模式的隧道捆绑接口，并为其添加成员接口后，执行]{style="font-family:宋体"}**[display mpls protection]{lang="EN-US"}**[命令不会显示该接口对应的保护组信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_836153916}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x936559407}[开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能，并进入]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x47508815}

[\[Sysname\] mpls protection]{lang="EN-US"}

[\[Sysname-mpls-protection\]]{lang="EN-US"}
:::

::: {#-1741782111 .myid}
[]{#_Toc404791791}[]{#struct_0_13803_16300_x1769710402}[]{#_Toc359419186}[]{#_Toc360433758}[]{#_Toc360433759}[]{#_Toc360433760}[]{#_Toc359572667}[]{#_Toc359573108}[]{#_Toc359573552}[]{#_Toc359573996}[]{#_Toc360433762}[]{#_Toc359572668}[]{#_Toc359573109}[]{#_Toc359573553}[]{#_Toc359573997}[]{#_Toc360433763}[]{#_Toc359572669}[]{#_Toc359573110}[]{#_Toc359573554}[]{#_Toc359573998}[]{#_Toc360433764}[]{#_Toc359572670}[]{#_Toc359573111}[]{#_Toc359573555}[]{#_Toc359573999}[]{#_Toc360433765}[]{#_Toc359572671}[]{#_Toc359573112}[]{#_Toc359573556}[]{#_Toc359574000}[]{#_Toc360433766}[]{#_Toc359572672}[]{#_Toc359573113}[]{#_Toc359573557}[]{#_Toc359574001}[]{#_Toc360433767}[]{#_Toc359572673}[]{#_Toc359573114}[]{#_Toc359573558}[]{#_Toc359574002}[]{#_Toc360433768}[]{#_Toc359572674}[]{#_Toc359573115}[]{#_Toc359573559}[]{#_Toc359574003}[]{#_Toc360433769}[]{#_Toc359572675}[]{#_Toc359573116}[]{#_Toc359573560}[]{#_Toc359574004}[]{#_Toc360433770}[]{#_Toc359572676}[]{#_Toc359573117}[]{#_Toc359573561}[]{#_Toc359574005}[]{#_Toc360433771}[]{#_Toc359572679}[]{#_Toc359573120}[]{#_Toc359573564}[]{#_Toc359574008}[]{#_Toc360433774}[]{#_Toc359572680}[]{#_Toc359573121}[]{#_Toc359573565}[]{#_Toc359574009}[]{#_Toc360433775}[]{#_Toc359572681}[]{#_Toc359573122}[]{#_Toc359573566}[]{#_Toc359574010}[]{#_Toc360433776}[]{#_Toc359572682}[]{#_Toc359573123}[]{#_Toc359573567}[]{#_Toc359574011}[]{#_Toc360433777}[]{#_Toc359572683}[]{#_Toc359573124}[]{#_Toc359573568}[]{#_Toc359574012}[]{#_Toc360433778}[]{#_Toc359572684}[]{#_Toc359573125}[]{#_Toc359573569}[]{#_Toc359574013}[]{#_Toc360433779}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection holdoff**

------------------------------------------------------------------------

[**[protection holdoff]{lang="EN-US"}**]{#struct_0_13803_16300_836743740}[命令用来配置检测到工作隧道发生故障后的倒换延迟时间。]{style="font-family:宋体"}

[**[undo protection holdoff]{lang="EN-US"}**]{#struct_0_13803_16300_990420270}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_1837127806}

[**[protection holdoff ]{lang="EN-US"}***[holdoff-time]{lang="EN-US"}*]{#struct_0_13803_16300_192722731}

[**[undo protection holdoff]{lang="EN-US"}**]{#struct_0_13803_16300_x102187130}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_1430605487}

[[倒换延迟时间为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13803_16300_x1333932582}[，即检测到工作隧道故障后立即将流量倒换到保护隧道传输。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_836809276}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_1988318861}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_575984315}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x205867824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1305849927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_2023825735}

[*[holdoff-time]{lang="EN-US"}*]{#struct_0_13803_16300_x1333147511}[：倒换延迟时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1819211209}

[[工作隧道出现故障时，等待倒换延迟时间超时后，再将流量切换到保护隧道上传输。若在倒换延迟时间内，工作隧道恢复正常，则不会进行倒换，避免因网络抖动而引起重复倒换。]{style="font-family:宋体"}]{#struct_0_13803_16300_1906036380}

[[只有执行]{style="font-family:宋体"}]{#struct_0_13803_16300_836219451}**[mpls protection]{lang="EN-US"}**[命令开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能后，才能执行本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1895153697}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_158722230}[配置接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的倒换延迟时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x781742467}

[\[Sysname\] interface tunnel-bundle 2 protection onetoone]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] protection holdoff 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_219110360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_x390205958}
:::

::: {#630605518 .myid}
[]{#_Toc404791792}[]{#struct_0_13803_16300_x929266865}[]{#_Toc359419187}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection revertive**

------------------------------------------------------------------------

[**[protection revertive]{lang="EN-US"}**]{#struct_0_13803_16300_836284987}[命令用来配置保护组的回切模式和回切等待时间。]{style="font-family:宋体"}

[**[undo protection revertive]{lang="EN-US"}**]{#struct_0_13803_16300_x628343261}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x631611679}

[**[protection revertive ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_13803_16300_2014277180}**[never]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[wtr]{lang="EN-US"}**[ \[ *wtr-time* \] }]{lang="EN-US"}

[**[undo protection revertive]{lang="EN-US"}**]{#struct_0_13803_16300_2051632389}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_2146906004}

[[工作隧道故障恢复后，流量会立即从保护隧道回切到工作隧道。]{style="font-family:宋体"}]{#struct_0_13803_16300_290290282}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_1613966568}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_983362873}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_836350523}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x319114216}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_997631111}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_611311256}

[**[never]{lang="EN-US"}**]{#struct_0_13803_16300_x1141572085}[：指定为不回切模式，即工作隧道故障恢复后，流量继续在保护隧道上传输，如果保护隧道未出现故障，则流量不会回切到工作隧道。]{style="font-family:宋体"}

[**[wtr]{lang="EN-US"}**]{#struct_0_13803_16300_x1898803617}[：指定为可回切模式，即工作隧道故障恢复后，流量从保护隧道回切到工作隧道。]{style="font-family:宋体"}

[*[wtr-time]{lang="EN-US"}*]{#struct_0_13803_16300_1640611820}[：指定回切时间，取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[3600]{lang="FR"}[，单位为秒，缺省值为]{style="font-family:宋体"}[600]{lang="FR"}[秒。]{style="font-family:宋体"}[工作隧道故障恢复后，如果在回切时间超时时，工作隧道仍然处于正常状态，则将流量从保护隧道回切到工作隧道。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x340805588}

[[通常情况下，工作隧道优于保护隧道，两条隧道都正常工作时，应优先使用工作隧道转发流量。工作隧道故障恢复后，流量立即从保护隧道回切到工作隧道，可以确保流量优先使用工作隧道转发。但是在网络抖动的情况下，立即回切可能会导致流量频繁在工作隧道和保护隧道之间倒换，影响流量的正常转发，并增加了设备的负担。通过配置不回切模式或指定回切时间，可以解决上述问题。]{style="font-family:宋体"}]{#struct_0_13803_16300_514110473}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1290641338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[隧道两端配置的回切模式和回切时间必须相同。]{style="font-family:宋体"}]{#struct_0_13803_16300_836416059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有执行]{lang="EN-US" style="font-family:宋体"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_1895132539}[命令开启]{lang="EN-US" style="font-family:
宋体"}[MPLS]{lang="EN-US"}[保护倒换功能后，才能执行本命令。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1901367465}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_2084628716}[配置接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[对应的保护组工作在可回切模式，并指定回切时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_610190940}

[\[Sysname\] interface tunnel-bundle 2 protection onetoone]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] protection revertive wtr 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1948901249}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_778827295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protection switching-mode bidirectional]{lang="EN-US"}**]{#struct_0_13803_16300_1164145784}
:::

::: {#-2034418501 .myid}
[]{#_Toc404791793}[]{#struct_0_13803_16300_x1890018644}[]{#_Toc359419189}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection switch**

------------------------------------------------------------------------

[**[protection switch]{lang="EN-US"}**]{#struct_0_13803_16300_x704042204}[命令用来在指定]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口上执行外部倒换命令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_835957307}

[**[protection switch]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_13803_16300_x1865883519}**[clear]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[force]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[lock]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[manual]{lang="EN-US"}**[ }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_958622551}

[[未配置外部倒换命令。]{style="font-family:宋体"}]{#struct_0_13803_16300_1885920323}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_1863218761}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_2143661880}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_927116330}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_1317914507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_1208800874}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x2052119833}

[**[clear]{lang="EN-US"}**]{#struct_0_13803_16300_x1264065682}[：表示清除倒换，即清除所有已执行的外部倒换命令。]{style="font-family:宋体"}

[**[force]{lang="EN-US"}**]{#struct_0_13803_16300_836022843}[：表示强制倒换，即强制流量在保护隧道上传输。]{style="font-family:宋体"}

[**[lock]{lang="EN-US"}**]{#struct_0_13803_16300_1421658306}[：表示锁定倒换，即将流量锁定在工作隧道上传输。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_13803_16300_x1922836362}[：表示手工倒换，即手动将流量从工作隧道倒换到保护隧道上传输，如果保护隧道存在故障，则不进行流量倒换。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x726926006}

[[触发流量在工作隧道和保护隧道之间倒换的方式分为外部倒换和信令倒换两类。优先级从高到低依次为：]{style="font-family:宋体"}]{#struct_0_13803_16300_x1829431162}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[清除倒换]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13803_16300_841734172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[锁定倒换]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13803_16300_146319986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[强制倒换]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13803_16300_198910834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[保护隧道的信令倒换，即通过信令协议检测到保护隧道发生故障]{style="font-family:宋体"}]{#struct_0_13803_16300_x2124492161}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[工作隧道的信令倒换，即通过信令协议检测到工作隧道发生故障]{style="font-family:宋体"}]{#struct_0_13803_16300_836088379}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信令清除倒换，即通过信令协议检测到工作隧道或保护隧道故障恢复]{style="font-family:宋体"}]{#struct_0_13803_16300_x977023961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手工倒换]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13803_16300_x586451404}

[[如果同时存在多种触发方式，则由优先级高的触发方式决定当前传输流量的隧道。]{style="font-family:宋体"}]{#struct_0_13803_16300_1517992324}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13803_16300_x2055005495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13803_16300_x1282951870}**[mpls protection]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能后，才能执行本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令指定不同的外部倒换命令时，优先级高的倒换命令覆盖优先级低的倒换命令。设备上已经执行了外部倒换命令时，若要将其修改为低优先级的外部倒换命令，则需要先配置清除倒换（]{style="font-family:宋体"}]{#struct_0_13803_16300_1010613102}**[clear]{lang="EN-US"}**[）命令，再配置低优先级的外部倒换命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x796416238}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_836153915}[配置接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[上执行强制倒换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x936559410}

[\[Sysname\] interface tunnel-bundle 2 protection oneplusone]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] protection switch force]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x47312206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_1833167660}
:::

::: {#501840734 .myid}
[]{#_Toc404791794}[]{#struct_0_13803_16300_x1496795347}[]{#_Toc359419188}[]{#_Toc359572889}[]{#_Toc359573330}[]{#_Toc359573774}[]{#_Toc359572890}[]{#_Toc359573331}[]{#_Toc359573775}[]{#_Toc359572891}[]{#_Toc359573332}[]{#_Toc359573776}[]{#_Toc359572892}[]{#_Toc359573333}[]{#_Toc359573777}[]{#_Toc359572893}[]{#_Toc359573334}[]{#_Toc359573778}[]{#_Toc359572894}[]{#_Toc359573335}[]{#_Toc359573779}[]{#_Toc359572895}[]{#_Toc359573336}[]{#_Toc359573780}[]{#_Toc359572896}[]{#_Toc359573337}[]{#_Toc359573781}[]{#_Toc359572897}[]{#_Toc359573338}[]{#_Toc359573782}[]{#_Toc359572898}[]{#_Toc359573339}[]{#_Toc359573783}[]{#_Toc359572899}[]{#_Toc359573340}[]{#_Toc359573784}[]{#_Toc359572900}[]{#_Toc359573341}[]{#_Toc359573785}[]{#_Toc359572901}[]{#_Toc359573342}[]{#_Toc359573786}[]{#_Toc359572902}[]{#_Toc359573343}[]{#_Toc359573787}[]{#_Toc359572903}[]{#_Toc359573344}[]{#_Toc359573788}[]{#_Toc359572904}[]{#_Toc359573345}[]{#_Toc359573789}[]{#_Toc359572905}[]{#_Toc359573346}[]{#_Toc359573790}[]{#_Toc359572978}[]{#_Toc359573419}[]{#_Toc359573863}[]{#_Toc359572979}[]{#_Toc359573420}[]{#_Toc359573864}[]{#_Toc359573001}[]{#_Toc359573442}[]{#_Toc359573886}[]{#_Toc359573002}[]{#_Toc359573443}[]{#_Toc359573887}[]{#_Toc359573006}[]{#_Toc359573447}[]{#_Toc359573891}[]{#_Toc359573018}[]{#_Toc359573459}[]{#_Toc359573903}[]{#_Toc359573019}[]{#_Toc359573460}[]{#_Toc359573904}[]{#_Toc359573020}[]{#_Toc359573461}[]{#_Toc359573905}[]{#_Toc359573021}[]{#_Toc359573462}[]{#_Toc359573906}[]{#_Toc359573022}[]{#_Toc359573463}[]{#_Toc359573907}[]{#_Toc359573023}[]{#_Toc359573464}[]{#_Toc359573908}[]{#_Toc359573024}[]{#_Toc359573465}[]{#_Toc359573909}[]{#_Toc359573025}[]{#_Toc359573466}[]{#_Toc359573910}[]{#_Toc359573026}[]{#_Toc359573467}[]{#_Toc359573911}[]{#_Toc359573027}[]{#_Toc359573468}[]{#_Toc359573912}[]{#_Toc359573028}[]{#_Toc359573469}[]{#_Toc359573913}[]{#_Toc359573029}[]{#_Toc359573470}[]{#_Toc359573914}[]{#_Toc359573030}[]{#_Toc359573471}[]{#_Toc359573915}[]{#_Toc359573031}[]{#_Toc359573472}[]{#_Toc359573916}[]{#_Toc359573032}[]{#_Toc359573473}[]{#_Toc359573917}[]{#_Toc359573033}[]{#_Toc359573474}[]{#_Toc359573918}[]{#_Toc359573034}[]{#_Toc359573475}[]{#_Toc359573919}[]{#_Toc359573035}[]{#_Toc359573476}[]{#_Toc359573920}[]{#_Toc359573036}[]{#_Toc359573477}[]{#_Toc359573921}[]{#_Toc359573037}[]{#_Toc359573478}[]{#_Toc359573922}[]{#_Toc359573038}[]{#_Toc359573479}[]{#_Toc359573923}[]{#_Toc359573039}[]{#_Toc359573480}[]{#_Toc359573924}[]{#_Toc359573040}[]{#_Toc359573481}[]{#_Toc359573925}[]{#_Toc359573041}[]{#_Toc359573482}[]{#_Toc359573926}[]{#_Toc359573042}[]{#_Toc359573483}[]{#_Toc359573927}[]{#_Toc359573043}[]{#_Toc359573484}[]{#_Toc359573928}[]{#_Toc359573044}[]{#_Toc359573485}[]{#_Toc359573929}[]{#_Toc359573045}[]{#_Toc359573486}[]{#_Toc359573930}[]{#_Toc359573046}[]{#_Toc359573487}[]{#_Toc359573931}[]{#_Toc359573047}[]{#_Toc359573488}[]{#_Toc359573932}[]{#_Toc359573048}[]{#_Toc359573489}[]{#_Toc359573933}[]{#_Toc359573049}[]{#_Toc359573490}[]{#_Toc359573934}[]{#_Toc359573050}[]{#_Toc359573491}[]{#_Toc359573935}[]{#_Toc359573051}[]{#_Toc359573492}[]{#_Toc359573936}[]{#_Toc359573052}[]{#_Toc359573493}[]{#_Toc359573937}[]{#_Toc359573053}[]{#_Toc359573494}[]{#_Toc359573938}[]{#_Toc359573075}[]{#_Toc359573516}[]{#_Toc359573960}[]{#_Toc359573076}[]{#_Toc359573517}[]{#_Toc359573961}[]{#_Toc359573089}[]{#_Toc359573530}[]{#_Toc359573974}[]{#_Toc359573090}[]{#_Toc359573531}[]{#_Toc359573975}[]{#_Toc359573091}[]{#_Toc359573532}[]{#_Toc359573976}[]{#_Toc359573092}[]{#_Toc359573533}[]{#_Toc359573977}[]{#_Toc359573093}[]{#_Toc359573534}[]{#_Toc359573978}[]{#_Toc359573094}[]{#_Toc359573535}[]{#_Toc359573979}[]{#_Toc359573095}[]{#_Toc359573536}[]{#_Toc359573980}[]{#_Toc359573096}[]{#_Toc359573537}[]{#_Toc359573981}[]{#_Toc359573097}[]{#_Toc359573538}[]{#_Toc359573982}[]{#_Toc359574218}[]{#_Toc360433784}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection switching-mode bidirectional**

------------------------------------------------------------------------

[**[protection ]{lang="EN-US"}**]{#struct_0_13803_16300_1974793538}**[switching-mode]{lang="EN-US"}[ bidirectional]{lang="EN-US"}**[命令用来配置保护组采用双向路径切换方式。]{style="font-family:宋体"}

[**[undo protection switching-mode bidirectional]{lang="EN-US"}**]{#struct_0_13803_16300_x2006144700}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_836743739}

[**[protection switching-mode bidirectional]{lang="EN-US"}**]{#struct_0_13803_16300_x965894873}

[**[undo protection switching-mode bidirectional]{lang="EN-US"}**]{#struct_0_13803_16300_1028453425}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_x604663505}

[[保护组采用单向路径切换方式。]{style="font-family:宋体"}]{#struct_0_13803_16300_x50496248}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x893450088}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_563226157}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_x829321288}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_836809275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_1988318864}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_576311995}

[[MPLS TE]{lang="EN-US"}]{#struct_0_13803_16300_1815679590}[隧道为双向隧道时，该隧道可以采用如下方式切换流量转发路径：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单向路径切换：外部倒换命令或信令倒换触发一个方向的流量进行保护倒换时，只切换该方向流量的转发隧道，另一个方向的转发隧道不受影响。]{style="font-family:宋体"}]{#struct_0_13803_16300_x1377618649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[双向路径切换：外部倒换命令或信令倒换触发一个方向的流量进行保护倒换时，不仅切换该方向流量的转发隧道，还通过]{style="font-family:宋体"}]{#struct_0_13803_16300_x1756423896}[PSC]{lang="EN-US"}[（]{style="font-family:宋体"}[Protection State Coordination]{lang="EN-US"}[，保护状态协调）控制报文通知远端切换另一个方向流量的转发隧道。]{style="font-family:宋体"}

[[1:1]{lang="EN-US"}]{#struct_0_13803_16300_1226939529}[保护倒换支持单向路径切换和双向路径切换；]{style="font-family:宋体"}[1+1]{lang="EN-US"}[保护倒换只支持双向路径切换。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13803_16300_1728138282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13803_16300_x101001072}**[mpls protection]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能后，才能执行本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[双向路径切换方式要求工作隧道和保护隧道都是双向隧道，且两端保护组都采用双向路径切换方式，否则双向切换功能无法正常运行。]{style="font-family:宋体"}]{#struct_0_13803_16300_x1537448682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1+1]{lang="EN-US"}]{#struct_0_13803_16300_x939410535}[保护倒换方式只支持双向路径切换方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_836219450}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x1895153696}[配置接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[对应的保护组采用双向路径切换方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_1724806171}

[\[Sysname\] interface tunnel-bundle 2 protection onetoone]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] protection switching-mode bidirectional]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_245713320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_1511373406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protection holdoff]{lang="EN-US"}**]{#struct_0_13803_16300_692627318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[psc message-interval]{lang="EN-US"}**]{#struct_0_13803_16300_x2101709838}
:::

::: {#242666725 .myid}
[]{#_Toc404791795}[]{#struct_0_13803_16300_1054428027}[]{#_Toc359419185}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- psc message-interval**

------------------------------------------------------------------------

[**[psc message-interval]{lang="EN-US"}**]{#struct_0_13803_16300_1081657703}[命令用来配置]{style="font-family:宋体"}[PSC]{lang="EN-US"}[控制报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo psc message-interval]{lang="EN-US"}**]{#struct_0_13803_16300_x341977855}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_836284986}

[**[psc message-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_13803_16300_x628343262}

[**[undo psc message-interval]{lang="EN-US"}**]{#struct_0_13803_16300_x631415071}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_70491026}

[[PSC]{lang="EN-US"}]{#struct_0_13803_16300_x872265186}[控制报文的发送时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1695850586}

[[MPLS]{lang="EN-US"}]{#struct_0_13803_16300_734085508}[保护倒换视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1055994497}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_2042253673}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_330941043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_836350522}

[*[interval]{lang="EN-US"}*]{#struct_0_13803_16300_x319114215}[：]{style="font-family:宋体"}[PSC]{lang="EN-US"}[控制报文的发送时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_997696647}

[[采用双向路径切换时，两个方向的隧道需要同时进行切换，因此隧道两端的设备需要周期性发送]{style="font-family:宋体"}[PSC]{lang="EN-US"}]{#struct_0_13803_16300_957484957}[控制报文来协调隧道两端的保护状态，以达到双向隧道同时切换的目的。]{style="font-family:宋体"}

[[可以根据需要修改]{style="font-family:宋体"}[PSC]{lang="EN-US"}]{#struct_0_13803_16300_x24430038}[控制报文的发送时间间隔，避免协议报文占用过多的带宽和设备资源。]{style="font-family:宋体"}

[[只有执行]{style="font-family:宋体"}]{#struct_0_13803_16300_1235882229}**[mpls protection]{lang="EN-US"}**[命令开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换功能后，才能执行本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1113653941}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x637964052}[配置]{style="font-family:宋体"}[PSC]{lang="EN-US"}[控制报文的发送时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x677441402}

[\[Sysname\] mpls protection]{lang="EN-US"}

[\[sys-mpls-protection\] psc message-interval 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_836416058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls protection]{lang="EN-US"}**]{#struct_0_13803_16300_1895132540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protection switching-mode bidirectional]{lang="EN-US"}**]{#struct_0_13803_16300_x1901957284}
:::

::: {#2052875588 .myid}
[]{#_Toc404791796}[]{#struct_0_13803_16300_638473614}[]{#_Toc359419183}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_13803_16300_1388659224}[命令用来清除接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_755582705}

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_13803_16300_x902964134}[ \[ ]{lang="EN-US"}**[tunnel-bundle]{lang="EN-US"}**[ \[ *number* \] ]{lang="EN-US"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_373212210}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13803_16300_x695011921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_1900196007}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_835957306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1865883518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1770260804}

[**[tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_x1740766355}[：指定接口类型为隧道捆绑接口。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_13803_16300_1921844086}[：隧道捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_x2090639244}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_13803_16300_x1485641206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_726315708}[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_1429301868}[而不指定]{lang="EN-US" style="font-family:
宋体"}*[number]{lang="EN-US"}*[，则清除所有隧道捆绑接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_1035970716}[和]{lang="EN-US" style="font-family:
宋体"}*[number]{lang="EN-US"}*[，则清除指定隧道捆绑接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_588714997}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_836022842}[清除接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters ]{lang="EN-US"}]{#struct_0_13803_16300_1421658305}[tunnel-bundle]{lang="EN-US"}[ 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1922901898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_2098298964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface tunnel-bundle]{lang="EN-US"}**]{#struct_0_13803_16300_x383604980}
:::

::::: {#-780779607 .myid}
[]{#_Toc359419179}[]{#_Toc404791797}[]{#struct_0_13803_16300_1165629344}[]{#_Toc360634003}[]{#_Toc303865071}[]{#_Toc215545670}[]{#_Toc215479545}[]{#_Toc360433788}[]{#_Toc360433789}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- service**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS保护倒换命令.files/image001.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_13803_16300_137765705}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13803_16300_1909226439}
:::

[ ]{lang="EN-US"}

[**[service]{lang="EN-US"}**]{#struct_0_13803_16300_836088378}[命令用来指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_13803_16300_x977023962}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_x586385868}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13803_16300_1522895785}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_13803_16300_1282462990}

[**[undo service slot]{lang="EN-US"}**]{#struct_0_13803_16300_1775996351}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13803_16300_2136076164}[模式：]{style="font-family:宋体"}

[**[service chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_13803_16300_x2060312726}**[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*

[**[undo service chassis]{lang="EN-US"}**]{#struct_0_13803_16300_836153914}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_x936559409}

[[没有指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}]{#struct_0_13803_16300_x47902031}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_x152305254}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x125064410}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_x1283248633}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_2090807089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_836743738}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13803_16300_x965894874}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13803_16300_1028650033}[：指定转发当前接口流量的单板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13803_16300_563164059}[：指定转发当前接口流量的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13803_16300_936891474}[：指定转发当前接口流量的设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}]{#struct_0_13803_16300_2029126869}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：指定转发当前接口流量的成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}]{#struct_0_13803_16300_x1126546131}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：指定转发当前接口流量的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_1719287234}

[[如果拔出指定的转发流量业务板，即使]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_1139243520}[接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[，流量也转发不通；如果重新插入指定的转发流量业务板，则流量可以恢复在指定板正常转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_2068744694}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_1178671503}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板转发接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的流量。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_836809274}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_1988318863}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备转发接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_576115387}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_1101963382}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号板转发接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[的流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x365646288}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\]]{lang="EN-US"}[ ]{lang="EN-US"}[service ]{lang="IT"}[chassis]{lang="EN-US"}[ ]{lang="EN-US"}[2 slot 2]{lang="IT"}
:::::

::: {#1170655049 .myid}
[]{#_Toc404791798}[]{#struct_0_13803_16300_x841491152}

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_13803_16300_583370220}[命令用来关闭隧道捆绑接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_13803_16300_x1892663900}[命令用来打开隧道捆绑接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13803_16300_967912582}

[**[shutdown]{lang="EN-US"}**]{#struct_0_13803_16300_x1498959678}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_13803_16300_x60854232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13803_16300_1226770446}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13803_16300_591541123}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13803_16300_18186251}

[[Tunnel-Bundle]{lang="EN-US"}]{#struct_0_13803_16300_x587050185}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13803_16300_764691453}

[[network-admin]{lang="EN-US"}]{#struct_0_13803_16300_x1892598364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13803_16300_409856909}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13803_16300_1612917329}

[[执行]{style="font-family:宋体"}]{#struct_0_13803_16300_1751546010}**[shutdown]{lang="EN-US"}**[命令不仅关闭隧道捆绑接口，还会关闭该隧道捆绑接口的成员接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13803_16300_1137797322}

[[\# ]{lang="EN-US"}]{#struct_0_13803_16300_x487475477}[关闭接口]{style="font-family:宋体"}[Tunnel-Bundle2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13803_16300_x987001866}

[\[Sysname\] interface tunnel-bundle 2]{lang="EN-US"}

[\[Sysname-tunnel-bundle2\] shutdown]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
