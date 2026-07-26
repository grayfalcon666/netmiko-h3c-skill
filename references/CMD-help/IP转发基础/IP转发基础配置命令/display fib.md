::: {#-1223034573 .myid}
[]{#_Toc289415221}[]{#_Toc138239296}[]{#_Toc136679734}[]{#_Toc404786485}[]{#struct_0_x7294_10991_x1006911381}[]{#_Toc291055660}[]{#_Toc271702012}[]{#_Toc238271212}

**IP转发基础 \-- IP转发基础配置命令 \-- display fib**

------------------------------------------------------------------------

[**[display fib]{lang="EN-US"}**]{#struct_0_x7294_10991_604586536}[命令用来显示]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x1359689338}

[**[display]{lang="EN-US"}**[ **fib** \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] \[ *ip-address* \[ *mask \| mask-length* \] \]]{lang="EN-US"}]{#struct_0_x7294_10991_x1589130829}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x1856764909}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7294_10991_2145331240}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x1186092215}

[[network-admin]{lang="EN-US"}]{#struct_0_x7294_10991_195058033}

[[network-operator]{lang="EN-US"}]{#struct_0_x7294_10991_x1838668691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7294_10991_688109848}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x7294_10991_x2105035491}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7294_10991_712655175}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x7294_10991_1620291134}[：显示指定拓扑的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；取值为]{style="font-family:宋体"}**[base]{lang="EN-US"}**[时表示公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x7294_10991_1671401047}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则显示公网的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x7294_10991_1833222115}[：显示与指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址匹配的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x7294_10991_843447954}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x7294_10991_1460297337}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x2113108920}

[**[display fib]{lang="EN-US"}**]{#struct_0_x7294_10991_196041073}[命令用来显示]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息，包括目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度、转发的下一跳地址、转发接口等内容。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7294_10991_85873481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置]{style="font-family:宋体"}]{#struct_0_x7294_10991_484033447}*[ip-address]{lang="EN-US"}*[时不指定掩码和掩码长度，则显示与指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址最长匹配的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置]{style="font-family:宋体"}]{#struct_0_x7294_10991_591027265}*[ip-address]{lang="EN-US"}*[时指定了掩码或掩码长度，则显示与指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码精确匹配的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x1268970712}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_1620618814}[显示指定拓扑的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\>[ ]{style="color:red"}display fib topology mt]{lang="EN-US"}]{#struct_0_x7294_10991_1863571574}

[ ]{lang="EN-US"}

[Destination count: 8 FIB entry count: 8]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flag:]{lang="EN-US"}

[  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static]{lang="EN-US"}

[  R:Relay     F:FRR]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination/Mask   Nexthop         Flag     OutInterface/Token       Label]{lang="EN-US"}

[0.0.0.0/32         127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[127.0.0.0/8        127.0.0.1       U        InLoop0                  Null]{lang="EN-US"}

[127.0.0.0/32       127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[127.0.0.1/32       127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[127.255.255.255/32 127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[224.0.0.0/4        0.0.0.0         UB       NULL0                    Null]{lang="EN-US"}

[224.0.0.0/24       0.0.0.0         UB       NULL0                    Null]{lang="EN-US"}

[255.255.255.255/32 127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_x128952332}[显示公网的所有]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display fib]{lang="EN-US"}]{#struct_0_x7294_10991_195975537}

[ ]{lang="EN-US"}

[Destination count: 5 FIB entry count: 6]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flag:]{lang="EN-US"}

[  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static]{lang="EN-US"}

[  R:Relay     F:FRR]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination/Mask   Nexthop         Flag     OutInterface/Token       Label]{lang="EN-US"}

[0.0.0.0/32         127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[1.1.1.0/24         192.168.126.1   USGF     M-GE0/0/0                Null]{lang="EN-US"}

[                   20.20.20.25     SGF      GE2/0/1                  Null]{lang="EN-US"}

[127.0.0.0/8        127.0.0.1       U        InLoop0                  Null]{lang="EN-US"}

[127.0.0.0/32       127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[127.0.0.1/32       127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x7294_10991_x58532432}[显示私网的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息]{style="font-family:宋体"}

[[\<Sysname\> display fib vpn-instance vpn1]{lang="EN-US"}]{#struct_0_x7294_10991_x1091430638}

[Destination count: 8 FIB entry count: 8]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flag:]{lang="EN-US"}

[  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static]{lang="EN-US"}

[  R:Relay     F:FRR]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination/Mask   Nexthop         Flag     OutInterface/Token       Label]{lang="EN-US"}

[0.0.0.0/32         127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[20.20.20.0/24      20.20.20.25     U        GE2/0/1                  Null]{lang="EN-US"}

[20.20.20.0/32      20.20.20.25     UBH      GE2/0/1                  Null]{lang="EN-US"}

[20.20.20.25/32     127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[20.20.20.25/32     20.20.20.25     H        GE2/0/1                  Null]{lang="EN-US"}

[20.20.20.255/32    20.20.20.25     UBH      GE2/0/1                  Null]{lang="EN-US"}

[30.30.30.0/24      30.30.30.30     U        GE2/0/2                  Null]{lang="EN-US"}

[30.30.30.0/32      30.30.30.30     UBH      GE2/0/2                  Null]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_2062246311}[显示目的地址为]{style="font-family:宋体"}[10.2.1]{lang="EN-US"}[.1]{lang="EN-US"}[的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display fib ]{lang="EN-US"}]{#struct_0_x7294_10991_195516786}[10.2.1]{lang="EN-US"}[.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination count: 1 FIB entry count: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flag:]{lang="EN-US"}

[  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static]{lang="EN-US"}

[  R:Relay     F:FRR]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination/Mask   Nexthop         Flag     OutInterface/Token       Label]{lang="EN-US"}

[10.2.1]{lang="EN-US"}[.1/32        127.0.0.1       UH       InLoop0                  Null]{lang="EN-US"}

[]{#struct_0_x7294_10991_x1653738313}[[表1-1 ]{lang="EN-US"}[display fib]{lang="EN-US"}]{#_Ref296523684}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1102936626}[[字段]{style="font-family:黑体"}]{#struct_0_x7294_10991_358621138}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7294_10991_x828513456}

[[Destination count]{lang="EN-US"}]{#struct_0_x7294_10991_x92643569}

[[目的地址的个数]{style="font-family:宋体"}]{#struct_0_x7294_10991_1816830862}

[[FIB entry count]{lang="EN-US"}]{#struct_0_x7294_10991_529859619}

[[FIB]{lang="EN-US"}]{#struct_0_x7294_10991_x535350979}[表项数目]{style="font-family:宋体"}

[[Destination/Mask]{lang="EN-US"}]{#struct_0_x7294_10991_195451250}

[[目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7294_10991_x1338361032}[掩码长度]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_x7294_10991_x1426277060}

[[转发的下一跳地址]{style="font-family:宋体"}]{#struct_0_x7294_10991_2105981722}

[[Flag]{lang="EN-US"}]{#struct_0_x7294_10991_2084145849}

[[路由的标志：]{style="font-family:宋体"}]{#struct_0_x7294_10991_1766306195}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x7294_10991_195385714}[：表示可用路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[G]{lang="EN-US"}]{#struct_0_x7294_10991_1557656528}[：表示网关路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x7294_10991_x1009030870}[：表示主机路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_x7294_10991_x1684750907}[：表示黑洞路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x7294_10991_x928336320}[：表示动态路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x7294_10991_1659180995}[：表示静态路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x7294_10991_195320178}[：表示迭代路由]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x7294_10991_1144238256}[：表示快速重路由]{lang="EN-US" style="font-family:
  宋体"}

[[OutInterface/Token]{lang="EN-US"}]{#struct_0_x7294_10991_x812324621}

[[转发接口]{style="font-family:宋体"}[/LSP]{lang="EN-US"}]{#struct_0_x7294_10991_x834362198}[索引号]{style="font-family:宋体"}

[[Label]{lang="EN-US"}]{#struct_0_x7294_10991_702270321}

[[内层标签值]{style="font-family:宋体"}]{#struct_0_x7294_10991_x584091801}

[ ]{lang="EN-US"}

::::: {#1577120789 .myid}
[]{#_Toc404786486}[]{#struct_0_x7294_10991_1884529253}[]{#_Toc380646926}

**IP转发基础 \-- IP转发基础配置命令 \-- ip last-hop hold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP转发基础命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7294_10991_1884070494}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x7294_10991_x495290519}
:::

[ ]{lang="EN-US"}

[**[ip last-hop hold ]{lang="EN-US"}**]{#struct_0_x7294_10991_x1540872830}[命令用来开启转发保持上一跳功能。]{style="font-family:宋体"}

[**[undo ip last-hop hold ]{lang="EN-US"}**]{#struct_0_x7294_10991_x1466453359}[命令用来关闭转发保持上一跳功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7294_10991_2124902373}

[**[ip last-hop hold]{lang="EN-US"}**]{#struct_0_x7294_10991_x1677914299}

[**[undo ip last-hop hold]{lang="EN-US"}**]{#struct_0_x7294_10991_1146311869}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7294_10991_676051090}

[[转发保持上一跳功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7294_10991_x1226427007}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x258538360}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7294_10991_x527591612}[三层以太网子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7294_10991_1824749010}

[[network-admin]{lang="EN-US"}]{#struct_0_x7294_10991_x1013166861}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7294_10991_1884004958}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7294_10991_1880246753}

[[接口上开启保持上一跳功能后，当正向流量的第一个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7294_10991_556949741}[报文从该接口发出，在高速缓存中会记录相应的流量特征以及上一跳信息，反向流量报文到达设备上进行转发时可以直接通过该上一跳信息指导报文进行转发。]{style="font-family:宋体"}

[[保持上一跳功能依赖于快速转发表项的建立，如果上一跳的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x7294_10991_1432777609}[地址发生变化，对应的快速转发表项需要重建才能使保持上一跳功能正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7294_10991_481277673}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_338221498}[开启转发保持上一跳功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_758661410}

[\[Sysname\] interface gigabitethernet 2/0/0]{lang="EN-US"}

[\[Sysname-GigabitEthernet2/0/0\] ip last-hop hold]{lang="EN-US"}
:::::

::::: {#1197604302 .myid}
[]{#_Toc404786489}[]{#struct_0_x7294_10991_x1935900603}[]{#_Toc391036358}[]{#_Toc385428141}

**负载分担 \-- 负载分担配置命令 \-- bandwidth-based-sharing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP转发基础命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7294_10991_x38489826}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x7294_10991_1430626452}
:::

[ ]{lang="EN-US"}

[**[bandwidth-based-sharing]{lang="EN-US"}**]{#struct_0_x7294_10991_x1740952674}[命令用来开启]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基]{style="font-family:宋体"}[于带宽的负]{style="font-family:宋体"}[载分担功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x7294_10991_x1641464145}**[bandwidth-based-sharing]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基于带]{style="font-family:宋体"}[宽的]{style="font-family:宋体"}[负载分担功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7294_10991_412291590}

[**[bandwidth-based-sharing]{lang="EN-US"}**]{#struct_0_x7294_10991_x1935900606}

[**[undo ]{lang="EN-US"}**]{#struct_0_x7294_10991_x798004713}**[bandwidth-based-sharing]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x996345939}

[[IPv4]{lang="EN-US"}]{#struct_0_x7294_10991_505775000}[基]{style="font-family:宋体"}[于带宽的负]{style="font-family:宋体"}[载分担功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7294_10991_1771574452}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7294_10991_1601373898}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x142495896}

[[network-admin]{lang="EN-US"}]{#struct_0_x7294_10991_2093527940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7294_10991_x1073889042}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x55613073}

[[开启]{style="font-family:宋体"}]{#struct_0_x7294_10991_x308350458}[IPv4]{lang="EN-US"}[基于带宽的负载分担功能情况下，如果转发时查到多个出接口]{style="font-family:宋体"}[/]{lang="EN-US"}[下一跳，则按照接口的带宽值计算出各个接口应该分配的报文比例，然后按照带宽比例对报文进行转发。]{style="font-family:宋体"}

[[支持负载分担的协议（如]{style="font-family:宋体"}[LISP]{lang="EN-US"}]{#struct_0_x7294_10991_x259460858}[）的设备，无论是否配置]{style="font-family:宋体"}**[bandwidth-based-sharing]{lang="EN-US"}**[，负载分担比例以协议定义的负载分担比例为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x532876660}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_x1289815586}[开启]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基]{style="font-family:宋体"}[于带宽的负]{style="font-family:宋体"}[载分担功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_181508104}

[\[Sysname\] ]{lang="EN-US"}[bandwidth-based-sharing]{lang="EN-US"}
:::::

::::: {#-1564794341 .myid}
[]{#_Toc404786490}[]{#struct_0_x7294_10991_x1676914677}

**负载分担 \-- 负载分担配置命令 \-- ip load-sharing local-first enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP转发基础命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7294_10991_339611774}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x7294_10991_1382859947}
:::

[ ]{lang="EN-US"}

[**[ip load-sharing local-first enable]{lang="EN-US"}**]{#struct_0_x7294_10991_813385265}[命令用来开启等价路由负载分担本地优先功能。]{style="font-family:宋体"}

[**[undo ip load-sharing local-first enable]{lang="EN-US"}**]{#struct_0_x7294_10991_x1445586713}[命令用来关闭等价路由负载分担本地优先功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7294_10991_1051968678}

[**[ip load-sharing local-first enable]{lang="EN-US"}**]{#struct_0_x7294_10991_939313349}

[**[undo ip load-sharing local-first enable]{lang="EN-US"}**]{#struct_0_x7294_10991_875370702}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x1317794217}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x7294_10991_x460069783}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7294_10991_1890775067}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7294_10991_x894912989}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x297779876}

[[network-admin]{lang="EN-US"}]{#struct_0_x7294_10991_x1099363116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7294_10991_x888016051}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7294_10991_779889975}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_x2100287808}[开启等价路由负载分担本地优先功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_x1044627134}

[\[Sysname\] ip load-sharing local-first enable]{lang="EN-US"}
:::::

::::: {#1719596007 .myid}
[]{#_Toc404786491}[]{#struct_0_x7294_10991_x944499931}[]{#_Toc361144273}[]{#_Toc354672458}[]{#_Toc352764128}

**负载分担 \-- 负载分担配置命令 \-- ip load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP转发基础命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7294_10991_x670160190}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x7294_10991_1834942962}
:::

**[ ]{lang="PT-BR"}**

[**[ip load-sharing mode]{lang="PT-BR"}**]{#struct_0_x7294_10991_1328853567}[命令用来配置负载分担方式。]{style="font-family:宋体"}

[**[undo ip load-sharing mode]{lang="PT-BR"}**]{#struct_0_x7294_10991_1394184367}[命令用来恢复缺省的负载分担方式。]{style="font-family:宋体"}[]{#_Toc274813078}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x829084932}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x7294_10991_x1264636407}[：]{style="font-family:宋体"}

[**[ip load-sharing mode ]{lang="PT-BR"}**]{#struct_0_x7294_10991_x1880828620}[{ **per-flow** \[ **algorithm** ]{lang="PT-BR"}*[algorithm-number]{lang="PT-BR" style="font-size:10.0pt"}***[ ]{lang="PT-BR"}**[\| ]{lang="PT-BR"}[\[ **dest-ip** \| **dest-port** \| **ip-pro** \| **src-ip** \| **src-port** \] \* \] \| **per-packet** }]{lang="PT-BR"}

[**[undo ip load-sharing mode]{lang="PT-BR"}**]{#struct_0_x7294_10991_479792223}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x7294_10991_x1585489619}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="PT-BR"}[集中式]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[ip load-sharing mode ]{lang="PT-BR"}**]{#struct_0_x7294_10991_x2029201432}[{ **per-flow** \[ **algorithm** ]{lang="PT-BR"}*[algorithm-number]{lang="PT-BR" style="font-size:10.0pt"}***[ ]{lang="PT-BR"}**[\| ]{lang="PT-BR"}[\[ **dest-ip** \| **dest-port** \| **ip-pro** \| **src-ip** \| **src-port** \] \* \] \| **per-packet** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="PT-BR"}

[**[undo ip load-sharing mode]{lang="EN-US"}**]{#struct_0_x7294_10991_965904426}[]{#_Toc274813056}**[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ ]{lang="EN-US"}**[cpu]{lang="PT-BR"}**[ *cpu-number*]{lang="PT-BR"}[ \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7294_10991_1328656959}[模式：]{style="font-family:宋体"}

[**[ip load-sharing mode ]{lang="EN-US"}**[{ **per-flow** \[ **algorithm** ]{lang="EN-US"}]{#struct_0_x7294_10991_x1366930845}*[algorithm-number]{lang="EN-US" style="font-size:10.0pt"}***[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}[\[ **dest-ip** \| **dest-port** \| **ip-pro** \| **src-ip** \| **src-port** \] \* \] \| **per-packet** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[**[undo ip load-sharing mode]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7294_10991_1592434827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x415946090}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x7294_10991_x1330922431}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7294_10991_2013280653}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7294_10991_x2119829409}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7294_10991_129741068}

[[network-admin]{lang="EN-US"}]{#struct_0_x7294_10991_1328722495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7294_10991_614735022}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x128834128}

[**[per-flow]{lang="EN-US"}**]{#struct_0_x7294_10991_374353778}[：基于报文逐流进行负载分担。]{style="font-family:宋体"}[]{#_Toc274813068}

[**[dest-ip]{lang="FR"}**]{#struct_0_x7294_10991_873198761}[：基于报文的目的]{style="font-family:宋体"}[IP]{lang="FR"}[地址逐流进行负载分担。[]{#_Toc274813069}本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[dest-port]{lang="FR"}**]{#struct_0_x7294_10991_657314298}[：基于报文的目的端口逐流进行负载分担。[]{#_Toc274813070}本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ip-pro]{lang="EN-US"}**]{#struct_0_x7294_10991_2063335518}[：基于报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议号逐流进行负载分担。[]{#_Toc274813071}本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[src-ip]{lang="EN-US"}**]{#struct_0_x7294_10991_x1161982546}[：基于报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址逐流进行负载分担。[]{#_Toc274813072}本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[src-port]{lang="PT-BR"}**]{#struct_0_x7294_10991_x1739481223}[：基于报文的源端口逐流进行负载分担。[]{#_Toc274813073}本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[algorithm]{lang="EN-US"}**]{#struct_0_x7294_10991_1329050175}*[ algorithm-number]{lang="EN-US"}*[：基于报文逐流进行负载分担的算法切换。]{style="font-family:宋体"}*[algorithm]{lang="EN-US"}[-]{lang="EN-US" style="font-family:,\"serif\""}[number]{lang="EN-US"}*[指定要进行算法切换的算法编号。范围为]{style="font-family:宋体"}[0\~7]{lang="EN-US"}[，当编号为]{style="font-family:宋体"}[0]{lang="EN-US" style="font-family:,\"serif\""}[时，表示设备内的缺省算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[**[per-packet]{lang="PT-BR"}**]{#struct_0_x7294_10991_x1331022875}[：基于报文逐包进行负载分担。[]{#_Toc274813074}本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x7294_10991_67701846}*[ slot-number]{lang="PT-BR"}*[：在指定单板上配置负载分担方式。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。如果未指定本参数，则在所有单板上配置负载分担方式。（分布式设备－独立运行模式）]{style="font-family:宋体"}[]{#_Toc274813075}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x7294_10991_668858064}[：在指定成员设备上配置负载分担方式。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，]{style="font-family:宋体"}[则在所有成员设备上配置负载分担方式]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x7294_10991_703859190}[：]{style="font-family:宋体"}[在指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上配置负载分担方式。]{style="font-family:宋体"}[slot-number]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则在所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上配置负载分担方式]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7294_10991_1814518051}[：在指定成员设备上指定单板上配置负载分担方式。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则在所有单板上配置负载分担方式。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）[]{#_Toc274813076}（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7294_10991_x2025024165}[：在指定单板上配置负载分担方式。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则在所有单板上配置负载分担方式。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x7294_10991_347860048}[：在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上配置负载分担方式。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7294_10991_x2142787241}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_1452563197}[配置基于报文逐包进行负载分担。[]{#_Toc274813085}（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_x1372207450}[]{#_Toc274813086}

[\[Sysname\] ip load-sharing mode per-packet]{lang="EN-US"}[]{#_Toc274813087}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_1329115711}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板基于报文逐包进行负载分担。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_x1318988303}

[\[Sysname\] ip load-sharing mode per-packet slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_x1429598670}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备基于报文逐包进行负载分担。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_x377383023}

[\[Sysname\] ip load-sharing mode per-packet slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7294_10991_x436832581}[配置]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板基于报文逐包进行负载分担。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7294_10991_958909525}

[\[Sysname\] ip load-sharing mode per-packet chassis 1 slot 2]{lang="EN-US"}
:::::
