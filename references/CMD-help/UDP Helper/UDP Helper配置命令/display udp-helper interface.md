::: {#-1115013693 .myid}
[]{#_Toc404786704}[]{#struct_0_x1562_x8906_64156503}

**UDP Helper \-- UDP Helper配置命令 \-- display udp-helper interface**

------------------------------------------------------------------------

[**[display udp-helper interface]{lang="EN-US"}**]{#struct_0_x1562_x8906_x289016707}[命令用来显示指定接口下广播转单播中继转发的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1803539140}

[**[display udp-helper]{lang="EN-US"}**[ **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1562_x8906_497020448}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1761276586}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x878702681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1824123872}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x1733586539}

[[network-operator]{lang="EN-US"}]{#struct_0_x1562_x8906_1800645775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x960925632}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1562_x8906_x1489803089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1505320207}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1562_x8906_449111232}[：接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_691165717}

[[通过本命令可以查看指定]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x2084218096}[接口配置的广播转单播中继转发的目的服务器信息以及广播转单播中继转发处理的报文数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1136202156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_x8906_276364950}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_x191752369}[显示]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[中继转发相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display udp-helper interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1562_x8906_x507890908}

[Interface                ]{lang="EN-US"}[Server VPN instance]{lang="EN-US" style="font-size:8.0pt;color:black"}[            Server address   Packets sent ]{lang="EN-US"}

[GigabitEthernet1/0/1     abc                           192.1.1.2        0]{lang="EN-US"}

[GigabitEthernet1/0/1     N/A                           192.1.1.2        0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_x8906_x1110695473}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_763722110}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[中继转发相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display udp-helper interface vlan-interface 1]{lang="EN-US"}]{#struct_0_x1562_x8906_x284757531}

[Interface                ]{lang="EN-US"}[Server VPN]{lang="EN-US" style="font-size:8.0pt;color:black"}[ instance           Server address Packets sent]{lang="EN-US"}

[Vlan-interface1          abc                           192.1.1.2      0]{lang="EN-US"}

[Vlan-interface1          N/A                           192.1.1.2      0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display udp-helper interface]{lang="EN-US"}]{#struct_0_x1562_x8906_273952525}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x897150439}[[字段]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1638973882}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1423739030}

[[Interface]{lang="EN-US"}]{#struct_0_x1562_x8906_x1277670155}

[[接口名]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x960794560}

[[Server VPN]{lang="EN-US" style="font-size:8.0pt;color:black"}[ instance]{lang="EN-US"}]{#struct_0_x1562_x8906_2023903341}

[[中继转发目的服务器所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1562_x8906_1394639843}[实例名]{style="font-family:宋体"}

[[Server address]{lang="EN-US"}]{#struct_0_x1562_x8906_x1482820655}

[[中继转发目的服务器地址]{style="font-family:宋体"}]{#struct_0_x1562_x8906_968516698}

[[Packets sent]{lang="EN-US"}]{#struct_0_x1562_x8906_204766872}

[[广播转单播]{style="font-family:宋体"}[UDP Helper ]{lang="EN-US"}]{#struct_0_x1562_x8906_1626659949}[处理的报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x847033076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset udp-helper statistics]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1754031156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-helper server]{lang="EN-US"}**]{#struct_0_x1562_x8906_x960729024}

::: {#-233396458 .myid}
[]{#_Toc404786705}[]{#struct_0_x1562_x8906_1269952812}

**UDP Helper \-- UDP Helper配置命令 \-- reset udp-helper statistics**

------------------------------------------------------------------------

[**[reset udp-helper statistics]{lang="EN-US"}**]{#struct_0_x1562_x8906_x963363876}[命令用来清除广播转单播中继转发的报文统计数目。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1991541061}

[**[reset udp-helper statistics]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1967380870}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1628480828}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x837799871}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1739395826}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x1490432460}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x15672868}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x960663488}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_2016444255}[清除广播转单播中继转发的报文统计数目。]{style="font-family:宋体"}

[[\<Sysname\> reset udp-helper statistics]{lang="EN-US"}]{#struct_0_x1562_x8906_x34157679}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1700943254}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display udp-helper interface]{lang="EN-US"}**]{#struct_0_x1562_x8906_x8081878}
:::

::: {#-1041663231 .myid}
[]{#_Toc404786706}[]{#struct_0_x1562_x8906_2023444588}[]{#_Toc367122832}

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper broadcast-map**

------------------------------------------------------------------------

[**[udp-helper broadcast-map]{lang="EN-US"}**]{#struct_0_x1562_x8906_611276143}[命令用来配置广播转组播中继转发。]{style="font-family:
宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1562_x8906_1610445311}**[udp-helper broadcast-map]{lang="EN-US"}**[命令用来]{style="font-family:宋体"}[取消]{style="font-family:宋体"}[广播转组播中继转发。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1891918450}

[**[udp-helper broadcast-map]{lang="EN-US"}**]{#struct_0_x1562_x8906_2023247980}[ *multicast-address* \[ **acl** *acl-number* \]]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1562_x8906_x2086554998}**[udp-helper broadcast-map]{lang="EN-US"}**[ *multicast-address*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1001605291}

[[没有配置广播转组播中继转发。]{style="font-family:宋体"}]{#struct_0_x1562_x8906_1380346550}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_106717384}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_2023313516}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1755413364}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_1367118884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_1008905933}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1188325833}

[*[multicast-address]{lang="EN-US"}*]{#struct_0_x1562_x8906_2023641196}[：组播地址。中继处理]{style="font-family:宋体"}[UDP]{lang="EN-US"}[广播报文时，将其目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址从广播地址修改为指定的组播地址。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_x1562_x8906_605199413}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号。通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[来实现对接口入方向的报文进行过滤，符合条件的才会按照配置的组播中继进行转发。支持基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[）与高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_590296516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请在接收广播报文的入接口上配置广播转组播中继转发。]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x1189979936}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口上最多可以配置的广播中继个数为]{style="font-family:宋体"}]{#struct_0_x1562_x8906_989010613}[20]{lang="EN-US"}[个（包括广播转单播和广播转组播）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_2023706732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_x8906_1399733771}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_x1477772670}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置广播转组播映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_1254502292}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] udp-helper broadcast-map 225.0.0.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x958317759}[应用]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_2023510124}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口上配置广播转组播映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_x2116933760}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-vlan-interface 100\] udp-helper broadcast-map 225.0.0.1]{lang="EN-US"}
:::

::: {#-1490776638 .myid}
[]{#_Toc404786707}[]{#struct_0_x1562_x8906_1595306099}[]{#_Toc367123779}

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper enable**

------------------------------------------------------------------------

[**[udp-helper enable]{lang="EN-US"}**]{#struct_0_x1562_x8906_1005470204}[命令用来使能]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo udp-helper enable]{lang="EN-US"}**]{#struct_0_x1562_x8906_1141187430}[命令用来关闭]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x2077360977}

[**[udp-helper enable]{lang="EN-US"}**]{#struct_0_x1562_x8906_x960597952}

[**[undo udp-helper enable]{lang="EN-US"}**]{#struct_0_x1562_x8906_1644319079}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_2080922988}

[[UDP Helper]{lang="EN-US"}]{#struct_0_x1562_x8906_1650425962}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x180363901}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x124858386}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1795401404}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_2029839245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_524107726}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x851317815}

[[使能]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}]{#struct_0_x1562_x8906_x960532416}[功能后，只有当全局配置了需要中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，并且接口下配置了]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[相关配置时，]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x702150052}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_x928714535}[使能]{style="font-family:宋体"}[UDP Helper]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_109915922}

[\[Sysname\] udp-helper enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_2023903340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-helper port]{lang="EN-US"}**]{#struct_0_x1562_x8906_1394705379}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-helper server]{lang="EN-US"}**]{#struct_0_x1562_x8906_753382948}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-helper multicast-map]{lang="EN-US"}**]{#struct_0_x1562_x8906_2023968876}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-helper broadcast-map]{lang="EN-US"}**]{#struct_0_x1562_x8906_x962213145}
:::

::::: {#1796265188 .myid}
[]{#_Toc404786708}[]{#struct_0_x1562_x8906_1098612335}[]{#_Toc367122834}

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper multicast-map**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](UDP%20Helper命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x1562_x8906_1210478386}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1562_x8906_2023379051}
:::

**[ ]{lang="EN-US"}**

[**[udp-helper multicast-map]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1000783830}[命令用于配置组播]{style="font-family:
宋体"}[MAP]{lang="PT-BR"}[映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1387274881}**[udp-helper multicast-map]{lang="EN-US"}**[命令用来取消]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[MAP]{lang="PT-BR"}[映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x940617661}

[**[udp-helper multicast-map]{lang="EN-US"}**]{#struct_0_x1562_x8906_1565969035}[ *multicast-address ip-address*]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **global** \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **acl** *acl-number* \]]{lang="EN-US"}

[**[undo udp-helper multicast-map ]{lang="EN-US"}**]{#struct_0_x1562_x8906_2023444587}*[multicast-address ip-address ]{lang="EN-US"}*[\[ **global** \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_610293103}

[[没有配置组播]{style="font-family:宋体"}[MAP]{lang="EN-US"}]{#struct_0_x1562_x8906_x2054521948}[映射。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x522475497}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_2023247979}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x2086096259}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x851059415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x1665981983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_2023313515}

[*[multicast-address]{lang="EN-US"}*]{#struct_0_x1562_x8906_x1755478900}[：组播地址。需要做中继处理的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[组播报文的目的地址。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1562_x8906_x1668742372}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，只能为单播地址或定向广播地址，不支持配置为受限广播地址。中继处理]{style="font-family:宋体"}[UDP]{lang="EN-US"}[组播报文时，将其目的地址从组播地址修改为指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[global]{lang="EN-US"}**]{#struct_0_x1562_x8906_1206977303}[：表示在公网中转发组播中继的报文。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance -name]{lang="EN-US"}*]{#struct_0_x1562_x8906_x1868267372}[：表示在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中转发组播中继的报文，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}***[ acl]{lang="EN-US"}*]{#struct_0_x1562_x8906_2023641195}*[-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号。通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[来实现对接口入方向的报文进行过滤，符合条件的才会按照配置的组播中继进行转发。支持基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[）与高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_605264949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[组播]{style="font-family:宋体"}]{#struct_0_x1562_x8906_1607480988}[MAP]{lang="EN-US"}[包括组播转广播和组播转单播两种情况，当]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为单播地址时，则将组播报文转换为单播报文，当]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为广播地址时，则将组播报文转换为广播报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请在接收组播报文的入接口上配置组播]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x219733139}[MAP]{lang="EN-US"}[映射，配置指定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[时在配置指定的私网内转发中继后的报文，当配置指定了]{style="font-family:宋体"}[global]{lang="EN-US"}[时在公网中转发中继后的报文，当两者都未指定时在当前接口绑定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中转发中继后的报文，若接口未绑定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则在公网中转发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下配置组播]{style="font-family:宋体"}]{#struct_0_x1562_x8906_2023706731}[MAP]{lang="PT-BR"}[映射时，同一个组播地址可以映射给]{style="font-family:宋体"}[16]{lang="PT-BR"}[个]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址]{style="font-family:宋体"}[。配置成功的组播]{style="font-family:宋体"}[MAP]{lang="EN-US"}[映射，同一个组播报文会同时转发给配置的单播地址和配置的定向广播地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1399799307}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_82198233}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置目地地址为]{style="font-family:宋体"}[225.0.0.1]{lang="EN-US"}[的组播报文转为地址为]{style="font-family:宋体"}[192.168.1.0]{lang="EN-US"}[网段的子网的广播地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_984258664}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] udp-helper multicast-map 225.0.0.1 192.168.1.255]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_2023510123}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置目地地址为]{style="font-family:宋体"}[225.0.0.1]{lang="EN-US"}[的组播报文转为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[a]{lang="EN-US"}[内的服务器]{style="font-family:宋体"}[192.168.1.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_x2116475008}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[ GigabitEthernet1/0/1]{lang="EN-US"}[\] udp-helper multicast-map 225.0.0.1 192.168.1.255 vpn-instance a]{lang="EN-US"}
:::::

::: {#1884481376 .myid}
[]{#_Toc404786709}[]{#struct_0_x1562_x8906_x1509212391}[]{#_Toc303688809}[]{#_Toc303688810}

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper port**

------------------------------------------------------------------------

[**[udp-helper port]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1219727576}[命令用来配置需要中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[**[undo udp-helper port]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1703708349}[命令用来取消对需要中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_952541877}

[**[udp-helper port ]{lang="EN-US"}**[{ *port-number* **\| dns \| netbios-ds \| netbios-ns \| tacacs \| tftp \| time** }]{lang="EN-US"}]{#struct_0_x1562_x8906_x844171814}

[**[undo udp-helper port ]{lang="EN-US"}**[{ *port-number* **\| dns \| netbios-ds \| netbios-ns \| tacacs \| tftp \| time** }]{lang="EN-US"}]{#struct_0_x1562_x8906_x960466880}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_847961326}

[[没有配置中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x1562_x8906_626770671}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_51769569}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_308469857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_978176607}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_x993493401}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_1542441044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_1400223720}

[*[port-number]{lang="EN-US"}*]{#struct_0_x1562_x8906_x961449920}[：需要中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[（不支持]{style="font-family:宋体"}[67]{lang="EN-US"}[和]{style="font-family:宋体"}[68]{lang="EN-US"}[）。有些]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号在某些设备上不支持，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[dns]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1824657143}[：对]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文进行中继转发，对应的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[53]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[netbios-ds]{lang="EN-US"}**]{#struct_0_x1562_x8906_x754117018}[：对]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[数据服务报文进行中继转发，对应的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[138]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[netbios-ns]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1836727865}[：对]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[名字服务报文进行中继转发，对应的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[137]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tacacs]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1927910560}[：对终端访问控制器访问控制系统报文进行中继转发，对应的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tftp]{lang="EN-US"}**]{#struct_0_x1562_x8906_x120326341}[：对简单文件传输协议报文进行中继转发，对应的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[69]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time]{lang="EN-US"}**]{#struct_0_x1562_x8906_x239659067}[：对时间服务报文进行中继转发，对应的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[37]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_135205652}

[[需要中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x1562_x8906_x1801950863}[端口有两种配置方法：指定端口号配置和指定参数配置。例如：]{style="font-family:宋体"}**[udp-helper port]{lang="EN-US"}**[ 53]{lang="EN-US"}[和]{style="font-family:宋体"}**[udp-helper port]{lang="EN-US"}**[ **dns**]{lang="EN-US"}[的效果是一样的。]{style="font-family:宋体"}

[[设备上最多可以配置]{style="font-family:宋体"}[256]{lang="EN-US"}]{#struct_0_x1562_x8906_x1154017828}[个需要中继转发的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x961384384}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_64090967}[配置对目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的广播报文进行中继转发。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_x329778050}

[\[Sysname\] udp-helper port 100]{lang="EN-US"}
:::

::: {#1761323954 .myid}
[]{#_Toc404786710}[]{#struct_0_x1562_x8906_1359324752}[]{#_Toc303688812}[]{#_Toc303688813}

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper server**

------------------------------------------------------------------------

[**[udp-helper server]{lang="EN-US"}**]{#struct_0_x1562_x8906_1270698693}[命令用来配置广播转单播中继转发的目的服务器。]{style="font-family:宋体"}

[**[undo udp-helper server]{lang="EN-US"}**]{#struct_0_x1562_x8906_x1753837580}[命令用来删除广播转单播中继转发的目的服务器的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1427868086}

[**[udp-helper server]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **global** \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1562_x8906_1476359542}

[**[undo udp-helper server]{lang="EN-US"}**[ \[ *ip-address* ]{lang="EN-US"}[\[ **global** \| **vpn-instance** *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_x1562_x8906_454368179}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x960925635}

[[没有配置广播转单播中继转发的目的服务器。]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x1490130769}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1667126880}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x184594575}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x849930438}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_808653234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_x8906_70035324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x294311378}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1562_x8906_x1364545232}[：目的服务器的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制形式。]{lang="EN-US" style="font-family:宋体"}

[**[global]{lang="EN-US"}**]{#struct_0_x1562_x8906_2023444586}[：指定只在公网中转发中继后的报文。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1562_x8906_2023247978}[：]{lang="EN-US" style="font-family:
宋体"}[表示]{style="font-family:宋体"}[在指定的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中转发]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x960860099}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请在接收广播报文的入接口上配置中继转发的目的服务器。一个接口上最多可以配置的广播中继个数为]{style="font-family:宋体"}]{#struct_0_x1562_x8906_x1110498865}[20]{lang="EN-US"}[个（包括广播转单播和广播转组播）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_x8906_1966783960}**[undo]{lang="EN-US"}[ udp-helper server]{lang="EN-US"}**[命令时如果不指定]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，将会删除该接口下配置的所有]{lang="EN-US" style="font-family:宋体"}[广播转单播]{style="font-family:宋体"}[中继转发的目的服务器。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[带]{style="font-family:宋体"}]{#struct_0_x1562_x8906_2023641194}**[vpn-instance]{lang="EN-US"}**[关键字的]{style="font-family:宋体"}[server]{lang="EN-US"}[配置与带]{style="font-family:宋体"}**[global]{lang="EN-US"}**[关键字的相同的]{style="font-family:宋体"}[server]{lang="EN-US"}[配置不互相覆盖，当配置指定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例时在配置的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中转发，配置指定了]{style="font-family:宋体"}**[global]{lang="EN-US"}**[时在公网中转发，两者均未指定时默认在接口下绑定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中转发，若接口未绑定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则在公网中转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_119910722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_x8906_x193475289}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_x936082434}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置广播转单播中继转发的目的服务器为]{style="font-family:宋体"}[192.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_x784741658}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] udp-helper server 192.1.1.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_2023706730}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置广播转单播中继转发的目的服务器为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[a]{lang="EN-US"}[内的]{style="font-family:宋体"}[192.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_1399864843}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] udp-helper server 192.1.1.2 vpn-instance a]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_x8906_714455466}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_1553422151}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上配置广播转单播中继转发的目的服务器为]{style="font-family:宋体"}[192.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_x960794563}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] udp-helper server 192.1.1.2 ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_x8906_2023510122}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上配置广播转单播中继转发的目的服务器为公网内的]{style="font-family:宋体"}[192.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_x8906_2023575658}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] udp-helper server 192.1.1.2 global]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_x8906_x1482755119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display udp-helper interface]{lang="EN-US"}**]{#struct_0_x1562_x8906_x377887842}

[ ]{lang="EN-US"}
:::
