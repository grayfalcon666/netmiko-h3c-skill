::: {#-1210365146 .myid}
[]{#_Toc404787158}[]{#_Toc370742252}[]{#struct_0_13981_19121_416534038}

**DHCPv6 \-- DHCPv6公共命令 \-- display ipv6 dhcp duid**

------------------------------------------------------------------------

[**[display ipv6 dhcp duid]{lang="EN-US"}**]{#struct_0_13981_19121_2044214962}[命令用来显示本设备的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2092735327}

[**[display ipv6 dhcp duid]{lang="EN-US"}**]{#struct_0_13981_19121_x283883496}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_936693978}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_612123256}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_2099904337}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1364144626}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_1302667619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1411939976}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_1633981916}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1225875625}

[[DUID]{lang="EN-US"}]{#struct_0_13981_19121_x1377407456}[（]{style="font-family:宋体"}[DHCP Unique Identifier]{lang="EN-US"}[，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[唯一标识符）是一台]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[设备（包括客户端、服务器和中继）的唯一标识。在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文交互过程中，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端、服务器和中继通过在报文中添加]{style="font-family:宋体"}[DUID]{lang="EN-US"}[来标识自己。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1628117440}

[[\# ]{lang="FR"}]{#struct_0_13981_19121_521927152}[显示本设备的]{style="font-family:宋体"}[DUID]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp duid]{lang="EN-US"}]{#struct_0_13981_19121_x1364079090}

[The DUID of this device: 0003000100e0fc005552.]{lang="EN-US"}
:::

::: {#-2081353140 .myid}
[]{#_Toc404787159}[]{#_Toc370742253}[]{#struct_0_13981_19121_x1937229490}[]{#_Toc337719091}

**DHCPv6 \-- DHCPv6公共命令 \-- ipv6 dhcp dscp**

------------------------------------------------------------------------

[**[ipv6 dhcp dscp]{lang="EN-US"}**]{#struct_0_13981_19121_x89713153}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继发送]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ipv6 dhcp dscp]{lang="EN-US"}**]{#struct_0_13981_19121_x435703546}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1630185651}

[**[ipv6 dhcp dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_13981_19121_75437404}

[**[undo ipv6 dhcp dscp]{lang="EN-US"}**]{#struct_0_13981_19121_289157966}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1117074142}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_2112214933}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x349844787}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1364013554}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1232069709}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1643852569}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_13981_19121_1987092243}[：]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1938911680}

[[DSCP]{lang="EN-US"}]{#struct_0_13981_19121_116127645}[优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继发送的]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1895894963}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x685757929}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继发送的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1365007653}

[\[Sysname\] ipv6 dhcp dscp 30]{lang="EN-US"}
:::

::: {#753778192 .myid}
[]{#_Toc404787160}[]{#struct_0_13981_19121_x1407231451}

**DHCPv6 \-- DHCPv6公共命令 \-- ipv6 dhcp log enable**

------------------------------------------------------------------------

[**[ipv6 dhcp log enable]{lang="EN-US"}**]{#struct_0_13981_19121_x539406466}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器日志信息功能。]{style="font-family:宋体"}

[**[undo ipv6 dhcp log enable]{lang="EN-US"}**]{#struct_0_13981_19121_238483810}[命令用来关闭]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[服务器日志信息功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x130366191}

[**[ipv6 dhcp log enable]{lang="EN-US"}**]{#struct_0_13981_19121_1437989125}

[**[undo ipv6 dhcp log enable]{lang="EN-US"}**]{#struct_0_13981_19121_1337803823}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1674479792}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x334161128}[服务器日志信息功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_272788851}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1683606221}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x882220957}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1407428059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1432345705}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1664142903}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_695745762}[服务器日志是为了满足管理员审计需求。设备生成]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[[比如大量]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1010116915}[客户端发生上下线操作时，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器需要输出大量日志信息，这可能会降低设备性能，影响]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器分配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的速度。为了避免该情况的发生，用户可以关闭]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器日志信息功能，使得]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器不再输出日志信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1200198000}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_111445912}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器日志信息功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1036334304}

[\[Sysname\] ipv6 dhcp log enable]{lang="EN-US"}
:::

::: {#-1275841970 .myid}
[]{#_Toc404787161}[]{#_Toc370742254}[]{#struct_0_13981_19121_x1363948018}[]{#_Toc266971096}[]{#_Toc265680005}[]{#_Toc263067816}[]{#_Toc207010292}[]{#_Toc207010025}[]{#_Toc139515316}[]{#_Toc137103149}

**DHCPv6 \-- DHCPv6公共命令 \-- ipv6 dhcp select**

------------------------------------------------------------------------

[**[ipv6 dhcp select]{lang="EN-US"}**]{#struct_0_13981_19121_115912458}[命令用来配置接口工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式。]{style="font-family:宋体"}

[**[undo ipv6 dhcp select]{lang="EN-US"}**]{#struct_0_13981_19121_1036735102}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1442787917}

[**[ipv6 dhcp select ]{lang="EN-US"}**[{ **relay** \| **server** }]{lang="EN-US"}]{#struct_0_13981_19121_x2143355821}

[**[undo ipv6 dhcp select]{lang="EN-US"}**]{#struct_0_13981_19121_x708808469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x189884741}

[[接口未工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x723183658}[服务器模式，也未工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式，接口接收到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文后，丢弃该报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x418160992}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1451938323}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1363882482}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x2123625136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x469389918}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_2046750887}

[[relay]{lang="EN-US"}]{#struct_0_13981_19121_x1846331602}[：配置接口工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式，即当接口收到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文时，将报文转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器，由]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端分配地址等参数。]{style="font-family:宋体"}

[[server]{lang="EN-US"}]{#struct_0_13981_19121_1095555066}[：配置接口工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器模式，即当接口收到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文时，将从]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的地址池中选择地址、前缀等参数分配给客户端。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x76237355}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x610238770}[服务器和]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端位于同一个网段时，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端可以直接从]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址等参数；]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器和]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端位于不同网段时，需要配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器之间转发报文。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13981_19121_1880454861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接口从]{style="font-family:宋体"}]{#struct_0_13981_19121_x996718248}[DHCPv6]{lang="EN-US"}[服务器模式切换到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式时，设备不会删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀绑定信息。建议接口从]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器模式切换到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式时，通过]{style="font-family:宋体"}**[reset ipv6 dhcp server ip-in-use]{lang="EN-US"}**[命令和]{style="font-family:宋体"}**[reset ipv6 dhcp server pd-in-use]{lang="EN-US"}**[命令清除已有的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀绑定信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议不要在一个接口上同时配置]{style="font-family:宋体"}]{#struct_0_13981_19121_x1363816946}[DHCPv6]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继]{style="font-family:宋体"}[/]{lang="EN-US"}[服务器功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x488307570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_434785}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1851055056}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_711908877}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp select server]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_348950648}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_8738947}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ipv6 dhcp select relay]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1199855523}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1363751410}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1558653179}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ipv6 dhcp select server]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x451295496}[配置接口]{style="font-family:宋体"}[Vlan-interface20]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x850744617}

[\[Sysname\] interface vlan-interface 20]{lang="EN-US"}

[\[Sysname-Vlan-interface20\] ipv6 dhcp select relay]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1504649281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_x2088616670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_x2099393072}
:::

::: {#196224333 .myid}
[]{#_Toc404787163}[]{#_Toc370742256}[]{#struct_0_13981_19121_760217851}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- address range**

------------------------------------------------------------------------

[**[address range]{lang="EN-US"}**]{#struct_0_13981_19121_x1364734450}[命令用来配置地址池中动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址范围。]{style="font-family:宋体"}

[**[undo address range]{lang="EN-US"}**]{#struct_0_13981_19121_309745982}[命令用来删除地址池中动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址范围。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x960284870}

[**[address range]{lang="EN-US"}[ ]{lang="EN-US"}***[start-ipv6-address]{lang="EN-US"}*[ *end-ipv6-address* \[ **preferred-lifetime** *preferred-lifetime* **valid-lifetime** *valid-lifetime* \]]{lang="EN-US"}]{#struct_0_13981_19121_x293211385}

[**[undo address range]{lang="EN-US"}**]{#struct_0_13981_19121_x1229803296}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x472780278}

[[未配置地址池中动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_252052129}[非临时地址范围，通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的网段内的单播地址都可以作为非临时地址分配给客户端。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1024695317}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_2047989196}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1206538102}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1364668914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1466189860}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x54844558}

[*[start-ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_1778824068}[：动态分配的起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址。]{style="font-family:宋体"}

[*[end-ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x1298200976}[：动态分配的结束]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址。]{style="font-family:宋体"}

[**[preferred-lifetime]{lang="EN-US"}**[ *preferred-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_x1192234446}[：指定地址池中分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址的首选生命期。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[为非临时地址的首选生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[604800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）。]{style="font-family:宋体"}

[**[valid-lifetime]{lang="EN-US"}**[ *valid-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_x514417011}[：指定地址池中分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址的有效生命期。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[为非临时地址的有效生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[2592000]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[天）。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x773699784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有在地址池下通过]{style="font-family:宋体"}**[address range]{lang="EN-US"}**]{#struct_0_13981_19121_x409933483}[命令配置动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址范围，则]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的网段内的单播地址都可以分配给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端。如果配置了]{style="font-family:宋体"}**[address range]{lang="EN-US"}**[命令，则只会从该地址范围内分配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址，即使该范围内的地址分配完毕，也不会从]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的地址范围内分配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址池下只能配置一个]{style="font-family:宋体"}]{#struct_0_13981_19121_x2145485516}[IPv6]{lang="EN-US"}[非临时地址范围，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range]{lang="EN-US"}**]{#struct_0_13981_19121_x740152502}[命令配置动态分配的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址范围必须在]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的网段内，否则无法分配。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1364210161}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x423248418}[配置地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[非临时地址范围为]{style="font-family:宋体"}[3ffe:501:ffff:100::10]{lang="EN-US"}[到]{style="font-family:宋体"}[3ffe:501:ffff:100::31]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1067558285}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] network 3ffe:501:ffff:100::/64]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] address range 3ffe:501:ffff:100::10 3ffe:501:ffff:100::31]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x553996711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x420989110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_13981_19121_x8053967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[temporary address range]{lang="EN-US"}**]{#struct_0_13981_19121_358611930}
:::

::: {#-1533740 .myid}
[]{#_Toc404787164}[]{#_Toc370742257}[]{#struct_0_13981_19121_854746933}[]{#_Toc349031154}[]{#_Toc348965402}[]{#_Toc348956694}[]{#_Toc348890621}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp option-group**

------------------------------------------------------------------------

[**[display ipv6 dhcp option-group]{lang="EN-US"}**]{#struct_0_13981_19121_355956334}[命令用来显示]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[选项组信息，包括静态和动态]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_340836134}

[**[display ipv6 dhcp option-group]{lang="EN-US"}**[ \[ *option-group-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_854681397}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1568074192}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x110483920}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1744008398}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1100540070}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x763878590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_854222644}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1294491134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_602168039}

[*[option-group-number]{lang="EN-US"}*]{#struct_0_13981_19121_x2020534994}[：显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组的信息。]{style="font-family:宋体"}*[option-group-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1123740159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1962488708}[选项组指的是通过]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp option-group]{lang="EN-US"}**[命令创建的选项组。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[动态]{style="font-family:宋体"}]{#struct_0_13981_19121_854157108}[DHCPv6]{lang="EN-US"}[选项组指的是设备作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项后，自动创建的选项组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1915212204}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1585585201}[显示所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp option-group]{lang="EN-US"}]{#struct_0_13981_19121_x343556651}

[[DHCPv6 option group: 1  ]{lang="EN-US"}]{#struct_0_13981_19121_780293522}

[[  DNS server addresses:]{lang="EN-US"}]{#struct_0_13981_19121_1360613974}

[[    Type: Static ]{lang="EN-US"}]{#struct_0_13981_19121_854353716}

[    Interface: N/A]{lang="EN-US"}

[[    1::1]{lang="EN-US"}]{#struct_0_13981_19121_642258448}

[[  DNS server addresses:]{lang="EN-US"}]{#struct_0_13981_19121_338772770}

[[    Type: Dynamic (DHCPv6 address allocation)]{lang="EN-US"}]{#struct_0_13981_19121_x652817180}

[[    Interface: GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_447726295}

[[    1::1]{lang="EN-US"}]{#struct_0_13981_19121_1568082305}

[[  Domain name:]{lang="EN-US"}]{#struct_0_13981_19121_x1685897983}

[[    Type: Static ]{lang="EN-US"}]{#struct_0_13981_19121_854288180}

[    Interface: N/A]{lang="EN-US"}

[[    aaa.com]{lang="EN-US"}]{#struct_0_13981_19121_x158477567}

[[  Domain name:]{lang="EN-US"}]{#struct_0_13981_19121_1026015826}

[[    Type: Dynamic (DHCPv6 address allocation)]{lang="EN-US"}]{#struct_0_13981_19121_x1152657903}

[[    Interface: GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_2048714036}

[[    aaa.com]{lang="EN-US"}]{#struct_0_13981_19121_x2036439861}

[[  Options:]{lang="EN-US"}]{#struct_0_13981_19121_854484788}

[[    Code: 23]{lang="EN-US"}]{#struct_0_13981_19121_941823831}

[[      Type: Dynamic (DHCPv6 prefix allocation)]{lang="EN-US"}]{#struct_0_13981_19121_x113260602}

[[      Interface: GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_1978651131}

[[      Length: 2 bytes]{lang="EN-US"}]{#struct_0_13981_19121_1203814439}

[[      Hex: ABCD]{lang="EN-US"}]{#struct_0_13981_19121_x843582129}

[[DHCPv6 option group: 20]{lang="EN-US"}]{#struct_0_13981_19121_854419252}

[[  DNS server addresses:]{lang="EN-US"}]{#struct_0_13981_19121_848131145}

[[    Type: Static ]{lang="EN-US"}]{#struct_0_13981_19121_175572474}

[    Interface: N/A]{lang="EN-US"}

[[    1::1]{lang="EN-US"}]{#struct_0_13981_19121_1645695551}

[[  DNS server addresses:]{lang="EN-US"}]{#struct_0_13981_19121_x1406605889}

[[    Type: Dynamic (DHCPv6 address allocation)]{lang="EN-US"}]{#struct_0_13981_19121_854615860}

[[    Interface: GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_704578133}

[[    1::1]{lang="EN-US"}]{#struct_0_13981_19121_961584677}

[[  Domain name:]{lang="EN-US"}]{#struct_0_13981_19121_1626541297}

[[    Type: Static ]{lang="EN-US"}]{#struct_0_13981_19121_x1627412514}

[    Interface: N/A]{lang="EN-US"}

[[    aaa.com]{lang="EN-US"}]{#struct_0_13981_19121_2087135012}

[[  Domain name:]{lang="EN-US"}]{#struct_0_13981_19121_854550324}

[[    Type: Dynamic (DHCPv6 address allocation)]{lang="EN-US"}]{#struct_0_13981_19121_1659496570}

[[    Interface: GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_x362911511}

[[    aaa.com]{lang="EN-US"}]{#struct_0_13981_19121_x1475701179}

[[  Options:]{lang="EN-US"}]{#struct_0_13981_19121_x62390209}

[[    Code: 23]{lang="EN-US"}]{#struct_0_13981_19121_955443961}

[[      Type: Dynamic (DHCPv6 prefix allocation)]{lang="EN-US"}]{#struct_0_13981_19121_x1757121934}

[[      Interface: GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_854746932}

[[      Length: 2 bytes]{lang="EN-US"}]{#struct_0_13981_19121_355956335}

[[      Hex: ABCD]{lang="EN-US"}]{#struct_0_13981_19121_340836133}

[[表1-1 ]{lang="EN-US"}[display ipv6 dhcp option-group]{lang="EN-US"}]{#struct_0_13981_19121_961908641}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x663832554}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1401549853}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_854681396}

[[DHCPv6 option group]{lang="EN-US"}]{#struct_0_13981_19121_1568074193}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x110549456}[选项组编号]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13981_19121_1697317568}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_854222643}[选项的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_13981_19121_x1294491141}[：表示静态]{style="font-family:
  宋体"}[DHCPv6]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Dynamic (DHCPv6 address allocation)]{lang="EN-US"}]{#struct_0_13981_19121_1005255958}[：表示动态地址申请得到的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Dynamic (DHCPv6 prefix allocation)]{lang="EN-US"}]{#struct_0_13981_19121_854157107}[：表示动态前缀申请得到的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Dynamic (DHCPv6 address and prefix allocation)]{lang="EN-US"}]{#struct_0_13981_19121_x1946714043}[：表示同时申请地址、前缀时得到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_13981_19121_1915212211}

[[接口名]{style="font-family:宋体"}]{#struct_0_13981_19121_1585257520}

[[DNS server addresses]{lang="EN-US"}]{#struct_0_13981_19121_858117506}

[[DNS]{lang="EN-US"}]{#struct_0_13981_19121_854353715}[服务器地址]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_13981_19121_642258447}

[[域名后缀]{style="font-family:宋体"}]{#struct_0_13981_19121_338772771}

[[SIP server addresses]{lang="EN-US"}]{#struct_0_13981_19121_854288179}

[[SIP]{lang="EN-US"}]{#struct_0_13981_19121_x967781640}[服务器地址]{style="font-family:宋体"}

[[SIP server domain names]{lang="EN-US"}]{#struct_0_13981_19121_2079757822}

[[SIP]{lang="EN-US"}]{#struct_0_13981_19121_80310128}[服务器域名]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_13981_19121_854484787}

[[自定义选项]{style="font-family:宋体"}]{#struct_0_13981_19121_941823844}

[[Code]{lang="EN-US"}]{#struct_0_13981_19121_1460717515}

[[自定义选项编码]{style="font-family:宋体"}]{#struct_0_13981_19121_854419251}

[[Length]{lang="EN-US"}]{#struct_0_13981_19121_848131144}

[[自定义选项长度，单位为字节]{style="font-family:宋体"}]{#struct_0_13981_19121_175572475}

[[Hex]{lang="EN-US"}]{#struct_0_13981_19121_854615859}

[[自定义选项内容，以十六进制字符串表示]{style="font-family:宋体"}]{#struct_0_13981_19121_x1634074018}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1954596150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp option-group]{lang="EN-US"}**]{#struct_0_13981_19121_x1003279395}

::: {#-743713820 .myid}
[]{#_Toc404787165}[]{#_Toc370742258}[]{#struct_0_13981_19121_x1184743789}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp pool**

------------------------------------------------------------------------

[**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_634099426}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1364144625}

[**[display ipv6 dhcp pool ]{lang="EN-US"}**[\[ *pool-name* \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_1705952146}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_916339088}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x2102365697}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1810622137}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1869145174}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_1118630196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x8059670}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x16813957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x550113153}

[*[pool-name]{lang="EN-US"}*]{#struct_0_13981_19121_x1364079089}[：显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1537278470}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1147818689}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x530258002}[显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp pool 1]{lang="EN-US"}]{#struct_0_13981_19121_x1364013553}

[DHCPv6 pool: 1]{lang="EN-US"}

[  Network: 3FFE:501:FFFF:100::/64]{lang="EN-US"}

[    Preferred lifetime 604800, valid lifetime 2592000]{lang="EN-US"}

[  Prefix pool: 1]{lang="EN-US"}

[    Preferred lifetime 24000, valid lifetime 36000]{lang="EN-US"}

[  Addresses:]{lang="EN-US"}

[    Range: from 3FFE:501:FFFF:100::1]{lang="EN-US"}

[           to 3FFE:501:FFFF:100::99]{lang="EN-US"}

[    Preferred lifetime 70480, valid lifetime 200000]{lang="EN-US"}

[    Total address number: 153]{lang="EN-US"}

[    Available: 153]{lang="EN-US"}

[    In-use: 0]{lang="EN-US"}

[  Temporary addresses:]{lang="EN-US"}

[    Range: from 3FFE:501:FFFF:100::200]{lang="EN-US"}

[           to 3FFE:501:FFFF:100::210]{lang="EN-US"}

[    Preferred lifetime 60480, valid lifetime 259200]{lang="EN-US"}

[    Total address number: 17]{lang="EN-US"}

[    Available: 17]{lang="EN-US"}

[    In-use: 0]{lang="EN-US"}

[  Static bindings:]{lang="EN-US"}

[    DUID: 0003000100e0fc000001]{lang="EN-US"}

[    IAID: 0000003f]{lang="EN-US"}

[    Prefix: 3FFE:501:FFFF:200::/64]{lang="EN-US"}

[      Preferred lifetime 604800, valid lifetime 2592000]{lang="EN-US"}

[    DUID: 0003000100e0fc00cff1]{lang="EN-US"}

[    IAID: 00000001]{lang="EN-US"}

[    Address: 3FFE:501:FFFF:2001::1/64]{lang="EN-US"}

[      Preferred lifetime 604800, valid lifetime 2592000]{lang="EN-US"}

[  DNS server addresses:]{lang="EN-US"}

[    2::2]{lang="EN-US"}

[  Domain name:]{lang="EN-US"}

[    aaa.com]{lang="EN-US"}

[  SIP server addresses:]{lang="EN-US"}

[    5::1]{lang="EN-US"}

[  SIP server domain names:]{lang="EN-US"}

[    bbb.com      ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1244246366}[显示引用未生效前缀的地址池的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp pool 1]{lang="EN-US"}]{#struct_0_13981_19121_849704596}

[DHCPv6 pool: 1]{lang="EN-US"}

[  Network: Not-available]{lang="EN-US"}

[    Preferred lifetime 604800, valid lifetime 2592000]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_13981_19121_x887435255}[显示配置恢复后地址池引用前缀未生效的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp pool 1]{lang="EN-US"}]{#struct_0_13981_19121_176131060}

[DHCPv6 pool: 1]{lang="EN-US"}

[  Network: 1::/64(Zombie)]{lang="EN-US"}

[    Preferred lifetime 604800, valid lifetime 2592000]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 dhcp pool]{lang="EN-US"}]{#struct_0_13981_19121_334014232}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1903188079}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x663596543}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_1128258762}

[[DHCPv6 pool]{lang="EN-US"}]{#struct_0_13981_19121_x1363948017}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_162966625}[地址池名称]{style="font-family:宋体"}

[[Network]{lang="EN-US"}]{#struct_0_13981_19121_158812772}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x590490331}[地址池中用于动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段。如果引用了未生效的前缀，则显示为]{style="font-family:宋体"}[Not-available]{lang="EN-US"}[；如果配置恢复后（如主备倒换）对应引用的前缀未生效，处于僵死状态，则显示为]{style="font-family:宋体"}[(Zombie)]{lang="EN-US"}

[[Prefix pool]{lang="EN-US"}]{#struct_0_13981_19121_457188903}

[[地址池引用的前缀池索引]{style="font-family:宋体"}]{#struct_0_13981_19121_1389692201}

[[Preferred lifetime]{lang="EN-US"}]{#struct_0_13981_19121_x1255371270}

[[租约首选生命期，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_x1363882481}

[[valid lifetime]{lang="EN-US"}]{#struct_0_13981_19121_x1720340609}

[[租约有效生命期，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_264750569}

[[Addresses]{lang="EN-US"}]{#struct_0_13981_19121_x697837153}

[[用于动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_569613120}[非临时地址信息]{style="font-family:宋体"}

[[Range]{lang="EN-US"}]{#struct_0_13981_19121_1344656110}

[[用于动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x2074507279}[地址范围]{style="font-family:宋体"}

[[Total address number]{lang="EN-US"}]{#struct_0_13981_19121_x1363816945}

[[可供分配的地址总数]{style="font-family:宋体"}]{#struct_0_13981_19121_1077776371}

[[Available]{lang="EN-US"}]{#struct_0_13981_19121_x2043613105}

[[空闲的地址总数]{style="font-family:宋体"}]{#struct_0_13981_19121_x873763043}

[[In-use]{lang="EN-US"}]{#struct_0_13981_19121_x118130887}

[[已分配的地址总数]{style="font-family:宋体"}]{#struct_0_13981_19121_x1363751409}

[[Temporary addresses]{lang="EN-US"}]{#struct_0_13981_19121_348865134}

[[用于动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x772348975}[临时地址信息]{style="font-family:宋体"}

[[Static bindings]{lang="EN-US"}]{#struct_0_13981_19121_x13935266}

[[静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1076638866}[地址或前缀信息]{style="font-family:宋体"}

[[DUID]{lang="EN-US"}]{#struct_0_13981_19121_x1364734449}

[[静态绑定的客户端]{style="font-family:宋体"}[DUID]{lang="EN-US"}]{#struct_0_13981_19121_x1612502783}

[[IAID]{lang="EN-US"}]{#struct_0_13981_19121_1957063739}

[[静态绑定的客户端]{style="font-family:宋体"}[IAID]{lang="EN-US"}]{#struct_0_13981_19121_x1019230399}[，未配置则显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[[Prefix]{lang="EN-US"}]{#struct_0_13981_19121_1506465583}

[[静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1364668913}[前缀]{style="font-family:宋体"}

[[Address]{lang="EN-US"}]{#struct_0_13981_19121_x99894081}

[[静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x2066274677}[地址]{style="font-family:宋体"}

[[DNS server addresses]{lang="EN-US"}]{#struct_0_13981_19121_1515100458}

[[为客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_13981_19121_x1946942200}[服务器地址]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_13981_19121_x1364210164}

[[为客户端分配的域名]{style="font-family:宋体"}]{#struct_0_13981_19121_x826532945}

[[SIP server addresses]{lang="EN-US"}]{#struct_0_13981_19121_x1849496973}

[[为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_13981_19121_x2089989519}[服务器地址]{style="font-family:宋体"}

[[SIP server domain names]{lang="EN-US"}]{#struct_0_13981_19121_x1364144628}

[[为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_13981_19121_x1473269903}[服务器域名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1426754730 .myid}
[]{#_Toc404787166}[]{#_Toc370742259}[]{#struct_0_13981_19121_1247960625}[]{#_Toc291747172}[]{#_Toc291747173}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp prefix-pool**

------------------------------------------------------------------------

[**[display ipv6 dhcp prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_x817151315}[命令用来显示前缀池的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1684430208}

[**[display ipv6 dhcp prefix-pool]{lang="EN-US"}**[ \[ *prefix-pool-number* \]\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_1735554797}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1922122258}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1364079092}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1194938392}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_941470391}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x2076916484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_130445251}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_1581464111}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1997452966}

[*[prefix-pool-number]{lang="EN-US"}*]{#struct_0_13981_19121_x17154187}[：显示指定前缀池的详细信息。]{style="font-family:宋体"}*[prefix-pool-number]{lang="EN-US"}*[为前缀池索引，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果不指定该参数，则显示所有前缀池的简要信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1537606151}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的前缀池的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的前缀池的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_510692808}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1364013556}[显示所有前缀池的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp prefix-pool]{lang="EN-US"}]{#struct_0_13981_19121_x69270295}

[Prefix-pool Prefix                                      Available In-use Static]{lang="EN-US"}

[1           5::/64                                      64        0      0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1244967267}[显示引用未生效前缀的前缀池的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp  prefix-pool]{lang="EN-US"}]{#struct_0_13981_19121_x353484924}

[Prefix-pool Prefix                                      Available In-use Static ]{lang="EN-US"}

[2           Not-available                               0         0      0]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_13981_19121_x1022549985}[显示配置恢复后前缀池引用前缀未生效的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp  prefix-pool]{lang="EN-US"}]{#struct_0_13981_19121_x1245032803}

[Prefix-pool Prefix                                      Available In-use Static ]{lang="EN-US"}

[11          21::/112(Zombie)                            0         64     0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1499316972}[显示前缀池]{style="font-family:宋体"}[1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp prefix-pool 1]{lang="EN-US"}]{#struct_0_13981_19121_x918158862}

[Prefix: 5::/64]{lang="EN-US"}

[Assigned length: 70]{lang="EN-US"}

[Total prefix number: 64]{lang="EN-US"}

[Available: 64]{lang="EN-US"}

[In-use: 0]{lang="EN-US"}

[Static: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x648906936}[显示前缀池]{style="font-family:宋体"}[1]{lang="EN-US"}[引用未生效前缀的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp prefix-pool 1]{lang="EN-US"}]{#struct_0_13981_19121_242570769}

[Prefix: Not-available]{lang="EN-US"}

[Assigned length: 70]{lang="EN-US"}

[Total prefix number: 0]{lang="EN-US"}

[Available: 0]{lang="EN-US"}

[In-use: 0]{lang="EN-US"}

[Static: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1378700644}[显示前缀池]{style="font-family:宋体"}[1]{lang="EN-US"}[引用生效前缀进程重启配置恢复后引用前缀未激活的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp prefix-pool 1]{lang="EN-US"}]{#struct_0_13981_19121_x1245098339}

[Prefix: 5::/64(Zombie)]{lang="EN-US"}

[Assigned length: 70]{lang="EN-US"}

[Total prefix number: 10]{lang="EN-US"}

[Available: 0]{lang="EN-US"}

[In-use: 10]{lang="EN-US"}

[Static: 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipv6 dhcp prefix-pool]{lang="EN-US"}]{#struct_0_13981_19121_31815404}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1926852247}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_1619027832}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x1363948020}

[[Prefix-pool]{lang="EN-US"}]{#struct_0_13981_19121_x240121294}

[[前缀池索引]{style="font-family:宋体"}]{#struct_0_13981_19121_1098286431}

[[Prefix]{lang="EN-US"}]{#struct_0_13981_19121_799949346}

[[前缀池中配置的前缀。如果引用了未生效的前缀，则显示为]{style="font-family:宋体"}[Not-available]{lang="EN-US"}]{#struct_0_13981_19121_1145757804}[；如果配置恢复后（如主备倒换）对应引用的前缀未生效，处于僵死状态，则显示为]{style="font-family:宋体"}[(Zombie)]{lang="EN-US"}

[[Available]{lang="EN-US"}]{#struct_0_13981_19121_1990524014}

[[空闲的前缀数量]{style="font-family:宋体"}]{#struct_0_13981_19121_1633102455}

[[In-use]{lang="EN-US"}]{#struct_0_13981_19121_x1363882484}

[[已分配的前缀数量]{style="font-family:宋体"}]{#struct_0_13981_19121_x960825722}

[[Static]{lang="EN-US"}]{#struct_0_13981_19121_848849105}

[[静态绑定的前缀数量]{style="font-family:宋体"}]{#struct_0_13981_19121_1540359471}

[[Assigned length]{lang="EN-US"}]{#struct_0_13981_19121_717315436}

[[分配的前缀长度]{style="font-family:宋体"}]{#struct_0_13981_19121_344190412}

[[Total prefix number]{lang="EN-US"}]{#struct_0_13981_19121_x1363816948}

[[可供分配的前缀数量]{style="font-family:宋体"}]{#struct_0_13981_19121_x37968876}

[ ]{lang="EN-US"}

::: {#1608950499 .myid}
[]{#_Toc404787167}[]{#_Toc370742260}[]{#struct_0_13981_19121_x1353228821}[]{#_Toc291747184}[]{#_Toc291747185}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server**

------------------------------------------------------------------------

[**[display ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_362595713}[命令用来显示接口上的]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[服务器信息，包括接口上引用的]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[地址池等信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x701319752}

[**[display ipv6 dhcp server]{lang="EN-US"}[ ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_x41809266}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x453646207}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1393112873}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1363751412}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1573514703}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1694047483}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1078103252}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x635590264}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1732371065}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13981_19121_1654497444}[：显示指定接口的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定该参数，则显示所有接口的]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[服务器信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x873925557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x522493774}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1364734452}[显示所有接口的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server]{lang="EN-US"}]{#struct_0_13981_19121_x853053432}

[Interface             Pool]{lang="EN-US"}

[GigabitEthernet1/0/1  1]{lang="EN-US"}

[GigabitEthernet1/0/2  global]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1388080171}[显示指定接口的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_x444848902}

[Using pool: 1]{lang="EN-US"}

[Preference value: 0]{lang="EN-US"}

[Allow-hint: Enabled]{lang="EN-US"}

[Rapid-commit: Disabled]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_314029738}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x145689581}[显示所有接口的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server]{lang="EN-US"}]{#struct_0_13981_19121_x1364668916}

[Interface             Pool]{lang="EN-US"}

[Vlan-interface2       1]{lang="EN-US"}

[Vlan-interface3       global]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_303390446}[显示指定接口的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server interface vlan-interface 2]{lang="EN-US"}]{#struct_0_13981_19121_x36095732}

[Using pool: 1]{lang="EN-US"}

[Preference value: 0]{lang="EN-US"}

[Allow-hint: Enabled]{lang="EN-US"}

[Rapid-commit: Disabled]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ipv6 dhcp server]{lang="EN-US"}]{#struct_0_13981_19121_2137018852}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1927402961}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x561861257}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_2020447839}

[[Interface]{lang="EN-US"}]{#struct_0_13981_19121_x799231157}

[[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x217730844}[服务器模式的接口]{style="font-family:宋体"}

[[Pool]{lang="EN-US"}]{#struct_0_13981_19121_x1364210163}

[[接口引用的地址池，如果显示为]{style="font-family:宋体"}[global]{lang="EN-US"}]{#struct_0_13981_19121_739550996}[，则表示接口上没有引用某个地址池，分配地址、前缀和其他网络参数时全局动态选择地址池]{style="font-family:宋体"}

[[Using pool]{lang="EN-US"}]{#struct_0_13981_19121_1618486551}

[[接口引用的地址池，如果显示为]{style="font-family:宋体"}[global]{lang="EN-US"}]{#struct_0_13981_19121_149876179}[，则表示接口上没有引用某个地址池，分配地址、前缀和其他网络参数时全局动态选择地址池]{style="font-family:宋体"}

[[Preference value]{lang="EN-US"}]{#struct_0_13981_19121_x1402346582}

[[服务器优先级，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13981_19121_693666978}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，该值越大，表示服务器的优先级越高]{style="font-family:宋体"}

[[Allow-hint]{lang="EN-US"}]{#struct_0_13981_19121_x1364144627}

[[是否支持优先为客户端分配其期望的地址和前缀：]{style="font-family:宋体"}]{#struct_0_13981_19121_x1426215736}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_13981_19121_x1605053389}[：表示支持优先为客户端分配其期望的地址和前缀]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_13981_19121_1376231247}[：表示忽略客户端期望的地址和前缀]{lang="EN-US" style="font-family:宋体"}

[[Rapid-commit]{lang="EN-US"}]{#struct_0_13981_19121_x1995063118}

[[是否支持地址和前缀快速分配功能：]{style="font-family:宋体"}]{#struct_0_13981_19121_x15317210}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_13981_19121_x1364079091}[：表示]{lang="EN-US" style="font-family:宋体"}[配置了]{style="font-family:宋体"}[地址和前缀快速分配功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_13981_19121_791653865}[：表示]{lang="EN-US" style="font-family:宋体"}[未配置]{style="font-family:宋体"}[地址和前缀快速分配功能]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2127340994 .myid}
[]{#_Toc404787168}[]{#_Toc370742261}[]{#struct_0_13981_19121_x938897447}[]{#_Toc291747187}[]{#_Toc291747188}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server conflict**

------------------------------------------------------------------------

[**[display ipv6 dhcp server conflict]{lang="EN-US"}**]{#struct_0_13981_19121_1821541698}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[的地址冲突信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1503811615}

[**[display ipv6 dhcp server conflict]{lang="EN-US"}**[ \[ **address** *ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_683098325}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x956338981}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1840277752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1155636389}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1364013555}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_1496813646}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1084291544}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x232985517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1398709234}

[**[address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_894451420}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址冲突信息。如果不指定本参数，则显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址冲突信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1537868288}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[的地址冲突信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[的地址冲突信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1299155630}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_264156766}[服务器在下列几种情况下会产生地址冲突信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1886326670}[客户端向]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器发送]{style="font-family:宋体"}[Decline]{lang="EN-US"}[报文，通知]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器为其分配的地址存在冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1363948019}[服务器检测到地址池内的可供分配的地址是设备自身的地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1681996399}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1553358727}[显示所有的地址冲突信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server conflict]{lang="EN-US"}]{#struct_0_13981_19121_x847066615}

[IPv6 address                                 Detect time]{lang="EN-US"}

[2001::1                                      Apr 25 16:57:20 2007]{lang="EN-US"}

[1::1:2                                       Apr 25 17:00:10 2007]{lang="EN-US"}

[]{#struct_0_13981_19121_621040839}[]{#_Toc138412523}[[表1-5 ]{lang="EN-US"}[display ipv6 dhcp server conflict]{lang="EN-US"}]{#_Toc54497770}[命令显示信息描述]{style="font-family:
黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1921356247}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1369797635}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x1604174558}

[[IPv6 address]{lang="EN-US"}]{#struct_0_13981_19121_x1363882483}

[[发生冲突的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x557541195}[地址]{style="font-family:宋体"}

[[Detect time]{lang="EN-US"}]{#struct_0_13981_19121_522354133}

[[检测到冲突的时间]{style="font-family:宋体"}]{#struct_0_13981_19121_77371355}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2073673106}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp server conflict]{lang="EN-US"}**]{#struct_0_13981_19121_1338154339}

::: {#-686135080 .myid}
[]{#_Toc404787169}[]{#struct_0_13981_19121_x1537802752}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server database**

------------------------------------------------------------------------

[**[display ipv6 dhcp server database]{lang="EN-US"}**]{#struct_0_13981_19121_1978719110}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的表项备份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1537999360}

[**[display ipv6 dhcp server database]{lang="EN-US"}**]{#struct_0_13981_19121_214274045}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1828571335}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1537933824}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x78380760}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1896504514}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x416658668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1509263431}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1537606144}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_649500458}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_800329116}[显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项备份信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server database]{lang="EN-US"}]{#struct_0_13981_19121_x1537540608}

[ File name               :   database.dhcp]{lang="EN-US"}

[ Username                :   ]{lang="EN-US"}

[ Password                :   ]{lang="EN-US"}

[ Update interval         :   600 seconds]{lang="EN-US"}

[ Latest write time       :   Feb  8 16:02:23 2014]{lang="EN-US"}

[ Status                  :   Last write succeeded.]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ipv6 dhcp server database]{lang="EN-US"}]{#struct_0_13981_19121_x498382425}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1319529170}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1817690992}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x1537737216}

[[File name]{lang="EN-US"}]{#struct_0_13981_19121_x1763960852}

[[存储]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1064417186}[服务器表项的文件名称]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_13981_19121_x1537671680}

[[配置远程目标文件时的用户名]{style="font-family:宋体"}]{#struct_0_13981_19121_x1732201570}

[[Password]{lang="EN-US"}]{#struct_0_13981_19121_x1992895831}

[[配置远程目标文件时的密码，有配置时显示为]{style="font-family:宋体"}["\*\*\*\*\*\*"]{lang="EN-US"}]{#struct_0_13981_19121_x1537344000}

[[Update interval]{lang="EN-US"}]{#struct_0_13981_19121_x1377196847}

[[定期刷新表项存储文件的刷新时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_1406412324}

[[Latest write time]{lang="EN-US"}]{#struct_0_13981_19121_x1537278464}

[[最近一次写文件的时间]{style="font-family:宋体"}]{#struct_0_13981_19121_1539671560}

[[Status]{lang="EN-US"}]{#struct_0_13981_19121_635740215}

[[写文件时的状态]{style="font-family:宋体"}]{#struct_0_13981_19121_x1537868289}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Writing]{lang="EN-US"}]{#struct_0_13981_19121_x712790448}[[：正在写文件]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write succeeded.]{lang="EN-US"}]{#struct_0_13981_19121_x365964605}[[：上一次写文件成功]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write failed.]{lang="EN-US"}]{#struct_0_13981_19121_x1537802753}[[：上一次写文件失败]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[ ]{lang="EN-US"}

::: {#-1292734827 .myid}
[]{#_Toc404787170}[]{#_Toc370742262}[]{#struct_0_13981_19121_x1363816947}[]{#_Toc379641077}[]{#_Toc379646164}[]{#_Toc379717220}[]{#_Toc379719066}[]{#_Toc379719147}[]{#_Toc379964789}[]{#_Toc379994499}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server expired**

------------------------------------------------------------------------

[**[display ipv6 dhcp server expired]{lang="EN-US"}**]{#struct_0_13981_19121_x2054391511}[命令用来显示租约过期的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1997737257}

[**[display ipv6 dhcp server expired ]{lang="EN-US"}**[\[ \[ **address** *ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \] \| **pool** *pool-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1051210516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2126346815}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_478940779}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_428785850}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x15811537}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1717982470}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1363751411}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x7430762}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x56330517}

[**[address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_1876781058}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的租约过期地址绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1537999361}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的租约过期的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的租约过期的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1501773808}[：显示指定地址池中租约过期的地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1731045430}

[[执行本命令时，如果不指定任何参数，则显示所有租约过期的地址绑定信息。]{style="font-family:宋体"}]{#struct_0_13981_19121_1177332949}

[[在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1639980636}[地址池的可用地址分配完后，租约过期的地址将被分配给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1827345396}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1364734451}[显示所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池中租约过期的地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server expired]{lang="EN-US"}]{#struct_0_13981_19121_x1256337959}

[IPv6 address           DUID                            Lease expiration]{lang="EN-US"}

[2001:3eff:fe80:4caa:   3030-3066-2e65-3230-302e-       Apr 25 17:10:47 2007]{lang="EN-US"}

[37ee:7::1              3130-3234-2d45-7468-6572-]{lang="EN-US"}

[                       6e65-7430-2f31]{lang="EN-US"}

[]{#struct_0_13981_19121_887113579}[]{#_Toc138412524}[[表1-7 ]{lang="EN-US"}[display dhcp server expired]{lang="EN-US"}]{#_Toc54497772}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1924697831}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1932284793}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_582774970}

[[IPv6 address]{lang="EN-US"}]{#struct_0_13981_19121_848968950}

[[租约过期的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1137352580}[地址]{style="font-family:宋体"}

[[DUID]{lang="EN-US"}]{#struct_0_13981_19121_x1364668915}

[[租约过期的客户端的]{style="font-family:宋体"}[DUID]{lang="EN-US"}]{#struct_0_13981_19121_x1262693495}

[[Lease expiration]{lang="EN-US"}]{#struct_0_13981_19121_1706252866}

[[租约过期的时间]{style="font-family:宋体"}]{#struct_0_13981_19121_1209416439}

**[ ]{lang="EN-US"}**

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1892879517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp server expired]{lang="EN-US"}**]{#struct_0_13981_19121_x1734984143}

::: {#1158686369 .myid}
[]{#_Toc404787171}[]{#_Toc370742263}[]{#struct_0_13981_19121_x1963986616}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server ip-in-use**

------------------------------------------------------------------------

[**[display ipv6 dhcp server ip-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_x1647010148}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_201873781}

[**[display ipv6 dhcp server ip-in-use]{lang="EN-US"}**[ \[ \[ **address** *ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \] \| **pool** *pool-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_2117889311}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1320167386}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1948401890}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1578490270}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x2048916232}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_1438377118}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_40875886}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_1689895485}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x551568008}

[**[address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_201939317}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1537540609}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_990288429}[：显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1558571811}

[[执行本命令时，如果不指定任何参数，则显示所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x332817089}[地址绑定信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_788825422}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1550594072}[显示所有的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server ip-in-use]{lang="EN-US"}]{#struct_0_13981_19121_1646547454}

[Pool: 1]{lang="EN-US"}

[ IPv6 address                                Type     Lease expiration]{lang="EN-US"}

[ 2:1::1                                      Auto(O)  Jul 10 19:45:01 2008]{lang="EN-US"}

[Pool: 2]{lang="EN-US"}

[ IPv6 address                                Type      Lease expiration]{lang="EN-US"}

[ 1:1::2                                      Static(F) Not available]{lang="EN-US"}

[Pool: 3]{lang="EN-US"}

[ IPv6 address                                Type      Lease expiration]{lang="EN-US"}

[ 1:2::1f1                                    Static(O) Oct  9 09:23:31 2008]{lang="EN-US"}

[Pool: 4]{lang="EN-US"}

[ IPv6 address                                Type      Lease expiration]{lang="EN-US"}

[ 1:2::2                                      Auto(Z)   Oct  11 09:23:31 2008]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x720896986}[显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server ip-in-use pool 1]{lang="EN-US"}]{#struct_0_13981_19121_202004853}

[Pool]{lang="EN-US"}[：]{style="font-family:
宋体"}[1]{lang="EN-US"}

[ IPv6 address                                Type      Lease expiration]{lang="EN-US"}

[ 2:1::1                                      Auto(O)   Jul 10 22:22:22 2008]{lang="EN-US"}

[ 3:1::2                                      Static(C) Jan  1 11:11:11 2008]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1090636858}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server ip-in-use address 2:1::3]{lang="EN-US"}]{#struct_0_13981_19121_x1355660900}

[Pool: 1]{lang="EN-US"}

[Client: FE80::C800:CFF0:FE18:0]{lang="EN-US"}

[Type: Auto(O)]{lang="PT-BR"}

[DUID: 00030001CA000C180000]{lang="PT-BR"}

[IAID: 0x00030001]{lang="PT-BR"}

[  ]{lang="PT-BR"}[IPv6 address: 2:1::3]{lang="EN-US"}

[  Preferred lifetime 400, valid lifetime 500]{lang="EN-US"}

[  Expires at Jul 10 09:45:01 2008 (288 seconds left)]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ipv6 dhcp server ip-in-use]{lang="EN-US"}]{#struct_0_13981_19121_x1718740365}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1917888251}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_2080699624}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_202070389}

[[Pool]{lang="EN-US"}]{#struct_0_13981_19121_1531413768}

[[地址绑定信息所属的地址池]{style="font-family:宋体"}]{#struct_0_13981_19121_767002927}

[[IPv6 address]{lang="EN-US"}]{#struct_0_13981_19121_312017424}

[[已分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_539842775}[地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13981_19121_x315245365}

[[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x625594426}[地址绑定的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Static(F)]{lang="EN-US"}]{#struct_0_13981_19121_202135925}[：表示尚未分配给客户端的静态绑定（]{style="font-family:
  宋体"}[Free]{lang="EN-US"}[），即静态无效绑定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Static(O)]{lang="EN-US"}]{#struct_0_13981_19121_x880918486}[：设备上配置静态绑定的地址后，如果收到对应客户端发送的]{style="font-family:
  宋体"}[Solicit]{lang="EN-US"}[消息，则产生该类型的绑定信息，即静态临时绑定（]{style="font-family:宋体"}[Offered]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Static(C)]{lang="EN-US"}]{#struct_0_13981_19121_1389535359}[：表示已经分配给客户端的静态绑定（]{lang="EN-US" style="font-family:宋体"}[Committed]{lang="EN-US"}[），即静态正式绑定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Auto(O)]{lang="EN-US"}]{#struct_0_13981_19121_x1660305965}[：表示接收到客户端发送的]{lang="EN-US" style="font-family:宋体"}[Solicit]{lang="EN-US"}[消息后，产生的动态临时绑定（]{lang="EN-US" style="font-family:宋体"}[Offered]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Auto(C)]{lang="EN-US"}]{#struct_0_13981_19121_639885458}[：表示接收到客户端发送的]{lang="EN-US" style="font-family:宋体"}[Request]{lang="EN-US"}[消息，或支持]{lang="EN-US" style="font-family:宋体"}[地址]{style="font-family:宋体"}[快速分配功能的服务器收到客户端发送的包含]{lang="EN-US" style="font-family:宋体"}[Rapid Commit]{lang="EN-US"}[选项的]{lang="EN-US" style="font-family:宋体"}[Solicit]{lang="EN-US"}[消息后，产生的动态正式绑定（]{lang="EN-US" style="font-family:宋体"}[Committed]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto(Z)]{lang="EN-US"}]{#struct_0_13981_19121_1483916092}[：表示已成功分配的租约表项在配置恢复后（如主备倒换），由于所在地址池引用的前缀不生效产生的僵死绑定]{style="font-family:宋体"}[(Zombie)]{lang="EN-US"}

[[Lease-expiration]{lang="EN-US"}]{#struct_0_13981_19121_x325382508}

[[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_202201461}[地址的租约过期时间。如果租约过期时间在]{style="font-family:宋体"}[2100]{lang="EN-US"}[年以后，则显示为]{style="font-family:宋体"}[Expires after 2100]{lang="EN-US"}[；对于静态无效绑定，显示为]{style="font-family:宋体"}[Not available]{lang="EN-US"}

[[Client]{lang="EN-US"}]{#struct_0_13981_19121_1026053364}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x2012114505}[客户端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。对于静态无效绑定，该字段显示为空]{style="font-family:宋体"}

[[DUID]{lang="EN-US"}]{#struct_0_13981_19121_x860983594}

[[客户端的]{style="font-family:宋体"}[DUID]{lang="EN-US"}]{#struct_0_13981_19121_291274627}

[[IAID]{lang="EN-US"}]{#struct_0_13981_19121_202266997}

[[客户端的]{style="font-family:宋体"}[IAID]{lang="EN-US"}]{#struct_0_13981_19121_x976666345}[。对于静态无效绑定且没有配置]{style="font-family:宋体"}[IAID]{lang="EN-US"}[，该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Preferred lifetime]{lang="EN-US"}]{#struct_0_13981_19121_x1384006041}

[[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_1508059775}[地址的首选生命期，单位为秒]{style="font-family:宋体"}

[[valid lifetime]{lang="EN-US"}]{#struct_0_13981_19121_344997219}

[[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_202332533}[地址的有效生命期，单位为秒]{style="font-family:宋体"}

[[Expires at]{lang="EN-US"}]{#struct_0_13981_19121_x2101163796}

[[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1190366658}[地址的租约过期时间。如果租约过期时间在]{style="font-family:宋体"}[2100]{lang="EN-US"}[年以后，则显示为]{style="font-family:宋体"}[Expires after 2100]{lang="EN-US"}

**[ ]{lang="EN-US"}**

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1567813274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp server ip-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_x1976292725}

::: {#797319525 .myid}
[]{#_Toc404787172}[]{#_Toc370742264}[]{#struct_0_13981_19121_737726032}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server pd-in-use**

------------------------------------------------------------------------

[**[display ipv6 dhcp server pd-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_x1573446847}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[前缀绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1255008435}

[**[display ipv6 dhcp server pd-in-use]{lang="EN-US"}**[ \[ **pool** *pool-name* \| \[ **prefix** *prefix/prefix-len* \] \[ **vpn-instance** *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_201349493}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_249613207}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1632476530}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2051828405}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_455451872}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x988891894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x616252912}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_786622661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_245626277}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_201415029}[：显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的前缀绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix/prefix-len*]{lang="EN-US"}]{#struct_0_13981_19121_902101066}[：显示指定前缀的前缀绑定信息。]{style="font-family:宋体"}*[prefix/prefix-len]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀长度，]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1941152819}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[前缀绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[前缀绑定信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x427077266}

[[执行本命令时，如果不指定任何参数，则显示所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1660259287}[前缀绑定信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_176497608}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1975258702}[显示所有的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[前缀绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server pd-in-use]{lang="EN-US"}]{#struct_0_13981_19121_x35483535}

[Pool: 1]{lang="EN-US"}

[ IPv6 prefix                                 Type      Lease expiration]{lang="EN-US"}

[ 2:1::/24                                    Auto(O)   Jul 10 19:45:01 2008]{lang="EN-US"}

[Pool: 2]{lang="EN-US"}

[ IPv6 prefix                                 Type      Lease expiration]{lang="EN-US"}

[ 1:1::/64                                    Static(F) Not available]{lang="EN-US"}

[Pool: 3]{lang="EN-US"}

[ IPv6 prefix                                 Type      Lease expiration]{lang="EN-US"}

[ 1:2::/64                                    Static(O) Oct  9 09:23:31 2008]{lang="EN-US"}

[Pool: 4]{lang="EN-US"}

[ IPv6 prefix                                 Type      Lease expiration]{lang="EN-US"}

[ 12::/80                                     Auto(Z)   Oct 17 09:34:59 2008]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1564060673}[显示指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的前缀绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server pd-in-use pool 1]{lang="EN-US"}]{#struct_0_13981_19121_201873782}

[Pool: 1]{lang="EN-US"}

[ IPv6 prefix                                 Type      Lease expiration]{lang="EN-US"}

[ 2:1::/24                                    Auto(O)   Jul 10 22:22:22 2008]{lang="EN-US"}

[ 3:1::/64                                    Static(C) Jan  1 11:11:11 2008]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_2117889314}[显示指定前缀的前缀绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server pd-in-use prefix 2:1::3/24]{lang="EN-US"}]{#struct_0_13981_19121_1320363994}

[Pool: 1]{lang="EN-US"}

[Client: FE80::C800:CFF:FE18:0]{lang="EN-US"}

[Type: Auto(O)]{lang="PT-BR"}

[DUID: 00030001CA000C180000]{lang="PT-BR"}

[IAID: 0x00030001]{lang="PT-BR"}

[  ]{lang="PT-BR"}[IPv6 prefix: 2:1::/24]{lang="EN-US"}

[  Preferred lifetime 400, valid lifetime 500]{lang="EN-US"}

[  Expires at Jul 10 09:45:01 2008 (288 seconds left)]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display ipv6 dhcp server pd-in-use]{lang="EN-US"}]{#struct_0_13981_19121_x769682995}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1919234599}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_201939318}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_990288440}

[[IPv6 prefix]{lang="EN-US"}]{#struct_0_13981_19121_1589384422}

[[已分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_941181438}[前缀]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13981_19121_1625355801}

[[前缀绑定的类型，取值包括：]{style="font-family:宋体"}]{#struct_0_13981_19121_x1055795663}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Static(F)]{lang="EN-US"}]{#struct_0_13981_19121_218899411}[：表示尚未分配给客户端的静态绑定前缀（]{style="font-family:
  宋体"}[Free]{lang="EN-US"}[），即静态无效绑定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Static(O)]{lang="EN-US"}]{#struct_0_13981_19121_202004854}[：表示静态临时绑定。设备上配置静态绑定的前缀后，如果收到对应客户端发送的]{style="font-family:
  宋体"}[Solicit]{lang="EN-US"}[消息，则产生该类型的绑定信息，即静态临时绑定（]{style="font-family:宋体"}[Offered]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Static(C)]{lang="EN-US"}]{#struct_0_13981_19121_1090636859}[：表示已经分配给客户端的静态绑定，即静态正式绑定（]{lang="EN-US" style="font-family:宋体"}[Committed]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Auto(O)]{lang="EN-US"}]{#struct_0_13981_19121_x1355595364}[：表示接收到客户端发送的]{lang="EN-US" style="font-family:宋体"}[Solicit]{lang="EN-US"}[消息后，产生的动态临时绑定（]{lang="EN-US" style="font-family:宋体"}[Offered]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Auto(C)]{lang="EN-US"}]{#struct_0_13981_19121_348833800}[：表示接收到客户端发送的]{lang="EN-US" style="font-family:宋体"}[Request]{lang="EN-US"}[消息，或支持前缀快速分配功能的服务器收到客户端发送的包含]{lang="EN-US" style="font-family:宋体"}[Rapid Commit]{lang="EN-US"}[选项的]{lang="EN-US" style="font-family:宋体"}[Solicit]{lang="EN-US"}[消息后，产生的动态正式]{lang="EN-US" style="font-family:宋体"}[绑定]{style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[Committed]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto(Z)]{lang="EN-US"}]{#struct_0_13981_19121_1484636988}[：表示已成功分配的前缀表项在配置恢复（如主备倒换）后，由于所在前缀池引用的前缀不生效产生的僵死绑定]{style="font-family:宋体"}[(Zombie)]{lang="EN-US"}

[[Pool]{lang="EN-US"}]{#struct_0_13981_19121_x1531786825}

[[前缀绑定所属的地址池]{style="font-family:宋体"}]{#struct_0_13981_19121_x2072836850}

[[Lease-expiration]{lang="EN-US"}]{#struct_0_13981_19121_202070390}

[[前缀的租约过期时间。如果租约过期时间在]{style="font-family:宋体"}[2100]{lang="EN-US"}]{#struct_0_13981_19121_x424901359}[年以后，则显示为]{style="font-family:宋体"}[Expires after 2100]{lang="EN-US"}[；对于静态无效绑定，显示为]{style="font-family:宋体"}[Not available]{lang="EN-US"}

[[Client]{lang="EN-US"}]{#struct_0_13981_19121_x187009451}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_699405252}[客户端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。对于静态无效绑定，该字段显示为空]{style="font-family:宋体"}

[[DUID]{lang="EN-US"}]{#struct_0_13981_19121_1771852276}

[[客户端的]{style="font-family:宋体"}[DUID]{lang="EN-US"}]{#struct_0_13981_19121_1589386555}

[[IAID]{lang="EN-US"}]{#struct_0_13981_19121_202135926}

[[客户端的]{style="font-family:宋体"}[IAID]{lang="EN-US"}]{#struct_0_13981_19121_x880918483}[。对于静态无效绑定且没有配置]{style="font-family:宋体"}[IAID]{lang="EN-US"}[，该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Preferred lifetime]{lang="EN-US"}]{#struct_0_13981_19121_1389863039}

[[前缀的首选生命期，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_1116668368}

[[valid lifetime]{lang="EN-US"}]{#struct_0_13981_19121_129477045}

[[前缀的有效生命期，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_202201462}

[[Expires at]{lang="EN-US"}]{#struct_0_13981_19121_1026053365}

[[前缀的租约过期时间。如果租约过期时间在]{style="font-family:宋体"}[2100]{lang="EN-US"}]{#struct_0_13981_19121_x2012048969}[年以后，则显示为]{style="font-family:宋体"}[Expires after 2100]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1505207393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp server pd-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_x2080800267}

::: {#97071579 .myid}
[]{#_Toc404787173}[]{#_Toc370742265}[]{#struct_0_13981_19121_x925286432}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- display ipv6 dhcp server statistics**

------------------------------------------------------------------------

[**[display ipv6 dhcp server statistics]{lang="EN-US"}**]{#struct_0_13981_19121_396498813}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_202266998}

[**[display ipv6 dhcp server statistics]{lang="EN-US"}**[ \[ **pool** *pool-name* \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_x976666356}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1383940506}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1648733286}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1049546465}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1108248459}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_229689607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_822883425}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_202332534}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2101163801}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1949422796}[：显示指定地址池的信息。]{style="font-family:宋体"}[pool-name]{lang="EN-US"}[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1940825139}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2057294582}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1399154517}[显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp server statistics]{lang="EN-US"}]{#struct_0_13981_19121_201349494}

[Bindings:]{lang="EN-US"}

[    Ip-in-use                 :  1]{lang="EN-US"}

[    Pd-in-use                 :  0]{lang="EN-US"}

[    Expired                   :  0]{lang="EN-US"}

[Conflict                      :  0]{lang="EN-US"}

[Packets received              :  1]{lang="EN-US"}

[    Solicit                   :  1]{lang="EN-US"}

[    Request                   :  0]{lang="EN-US"}

[    Confirm                   :  0]{lang="EN-US"}

[    Renew                     :  0]{lang="EN-US"}

[    Rebind                    :  0]{lang="EN-US"}

[    Release                   :  0]{lang="EN-US"}

[    Decline                   :  0]{lang="EN-US"}

[    Information-request       :  0]{lang="EN-US"}

[    Relay-forward             :  0]{lang="EN-US"}

[Packets dropped               :  0]{lang="EN-US"}

[Packets sent                  :  0]{lang="EN-US"}

[    Advertise                 :  0]{lang="EN-US"}

[    Reconfigure               :  0]{lang="EN-US"}

[    Reply                     :  0]{lang="EN-US"}

[    Relay-reply               :  0]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display ipv6 dhcp server statistics]{lang="EN-US"}]{#struct_0_13981_19121_249613200}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1916529357}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1632476523}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x485810000}

[[Bindings]{lang="EN-US"}]{#struct_0_13981_19121_x1254144658}

[[各种状态的地址绑定数，包括：]{style="font-family:宋体"}]{#struct_0_13981_19121_x1698650410}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ip-in-use]{lang="EN-US"}]{#struct_0_13981_19121_201415030}[：地址绑定信息总数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pd-in-use]{lang="EN-US"}]{#struct_0_13981_19121_x1054214077}[：前缀绑定信息的总数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Expired]{lang="EN-US"}]{#struct_0_13981_19121_x1095954004}[：租约过期的地址绑定信息的总数]{style="font-family:宋体"}

[[Conflict]{lang="EN-US"}]{#struct_0_13981_19121_x589709433}

[[冲突地址的总数，显示指定地址池的统计信息时无此字段]{style="font-family:宋体"}]{#struct_0_13981_19121_1011881164}

[[Packets received]{lang="EN-US"}]{#struct_0_13981_19121_752914312}

[[接收报文的数目，报文类型如下：]{style="font-family:宋体"}]{#struct_0_13981_19121_201873779}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Solicit]{lang="EN-US"}]{#struct_0_13981_19121_1780182295}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Request]{lang="EN-US"}]{#struct_0_13981_19121_x157250029}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Confirm]{lang="EN-US"}]{#struct_0_13981_19121_1556869605}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Renew]{lang="EN-US"}]{#struct_0_13981_19121_x710912955}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Rebind]{lang="EN-US"}]{#struct_0_13981_19121_201939315}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Release]{lang="EN-US"}]{#struct_0_13981_19121_990288427}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Decline]{lang="EN-US"}]{#struct_0_13981_19121_x1558571797}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Information-request]{lang="EN-US"}]{#struct_0_13981_19121_x1495092226}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Relay-forward]{lang="EN-US"}]{#struct_0_13981_19121_x1680506809}

[[显示指定地址池的统计信息时无此类字段]{style="font-family:宋体"}]{#struct_0_13981_19121_202004851}

[[Packets dropped]{lang="EN-US"}]{#struct_0_13981_19121_1090636856}

[[丢弃报文的数目，显示指定地址池的统计信息时无此字段]{style="font-family:宋体"}]{#struct_0_13981_19121_x1355005540}

[[Packets sent]{lang="EN-US"}]{#struct_0_13981_19121_1896819301}

[[发送报文的数目，报文类型如下：]{style="font-family:宋体"}]{#struct_0_13981_19121_x41140686}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Advertise]{lang="EN-US"}]{#struct_0_13981_19121_202070387}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Reconfigure]{lang="EN-US"}]{#struct_0_13981_19121_1531413782}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_13981_19121_766609721}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Relay-reply]{lang="EN-US"}]{#struct_0_13981_19121_1269066371}

[[显示指定地址池的统计信息时无此类字段]{style="font-family:宋体"}]{#struct_0_13981_19121_x2117005453}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_202135923}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp server statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x880918480}

::: {#-78714390 .myid}
[]{#_Toc404787174}[]{#_Toc370742266}[]{#struct_0_13981_19121_1389666431}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- dns-server**

------------------------------------------------------------------------

[**[dns-server]{lang="EN-US"}**]{#struct_0_13981_19121_x50765725}[命令用来配置为客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[**[undo dns-server]{lang="EN-US"}**]{#struct_0_13981_19121_x235647111}[命令用来删除指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x291076861}

[**[dns-server]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_x713814411}

[**[undo dns-server]{lang="EN-US"}[ ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x38820467}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_202201459}

[[未]{style="font-family:宋体"}]{#struct_0_13981_19121_x1312598804}[指定为客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x332054165}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_406982465}[地址池视图]{style="font-family:宋体"}[/DHCPv6]{lang="EN-US"}[选项组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1566175286}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x580305118}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_317229998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1966084824}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_510404154}[：]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_202266995}

[[可以通过多次执行本命令配置多个]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_13981_19121_x976666343}[服务器地址。一个地址池下最多可以配置]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址，且配置的先后顺序决定了]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的优先级，先配置的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器优先级大于后配置的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1384137113}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x218801863}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[为客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[2:2::3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_817716868}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] dns-server 2:2::3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x221599265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x1033037138}
:::

::: {#700735607 .myid}
[]{#_Toc404787175}[]{#_Toc370742267}[]{#struct_0_13981_19121_x1113431600}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- domain-name**

------------------------------------------------------------------------

[**[domain-name]{lang="EN-US"}**]{#struct_0_13981_19121_202332531}[命令用来配置为客户端分配的域名后缀。]{style="font-family:宋体"}

[**[undo domain-name]{lang="EN-US"}**]{#struct_0_13981_19121_x2101163798}[命令用来]{style="font-family:宋体"}[删除为客户端分配的域名后缀]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x740027964}

[**[domain-name]{lang="EN-US"}[ ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_13981_19121_x1702377120}

[**[undo domain-name]{lang="EN-US"}**]{#struct_0_13981_19121_x1093890572}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x876797036}

[[未指定为客户端分配的域名后缀。]{style="font-family:宋体"}]{#struct_0_13981_19121_1993361836}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_388031544}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1790593646}[地址池视图]{style="font-family:宋体"}[/DHCPv6]{lang="EN-US"}[选项组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_201349491}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_249613205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1632476528}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1695663581}

[*[domain-name]{lang="EN-US"}*]{#struct_0_13981_19121_1398489090}[：域名后缀，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1259224765}

[[一个地址池下只能配置一个域名后缀。重复执行本命令，新的配置会覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_13981_19121_1489457897}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_746378438}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_201415027}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[为客户端分配的域名后缀为]{style="font-family:宋体"}[aaa.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_902101052}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] domain-name aaa.com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1146900842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x2046016845}
:::

::: {#684966631 .myid}
[]{#_Toc404787176}[]{#_Toc370742268}[]{#struct_0_13981_19121_x1874136422}[]{#_Toc349031163}[]{#_Toc348965411}[]{#_Toc348956703}[]{#_Toc348890626}[]{#_Toc379964796}[]{#_Toc379994506}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp option-group**

------------------------------------------------------------------------

[**[ipv6 dhcp option-group]{lang="EN-US"}**]{#struct_0_13981_19121_811748437}[命令用来手工创建静态]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组，并进入]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组视图。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[ipv6 dhcp option-group]{lang="EN-US"}**[命令用来删除指定的静态]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1874201958}

[**[ipv6 dhcp option-group]{lang="EN-US"}**[ *option-group-number*]{lang="EN-US"}]{#struct_0_13981_19121_1342303493}

[**[undo ipv6 dhcp option-group ]{lang="EN-US"}***[option-group-number]{lang="EN-US"}*]{#struct_0_13981_19121_x393228457}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_120815782}

[[设备上不存在任何]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1874660711}[选项组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1717075188}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x633588845}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x97286321}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1874726247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x93647545}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1567005583}

[*[option-group-number]{lang="EN-US"}*]{#struct_0_13981_19121_1650760394}[：选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1735206070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1874529639}[客户端从]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或前缀时，可以同时获取其他的网络配置参数，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端可以根据获取的网络配置参数动态生成]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组。动态生成的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组不允许手工修改和删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手工配置的静态]{style="font-family:宋体"}]{#struct_0_13981_19121_x1031646807}[DHCPv6]{lang="EN-US"}[选项组与动态生成的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号允许相同，静态选项组信息优先。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x108985093}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1388329175}[创建静态]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1874595175}

[\[Sysname\] ipv6 dhcp option-group 1]{lang="EN-US"}

[\[Sysname-dhcp6-option-group1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x406459343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp option-group]{lang="EN-US"}**]{#struct_0_13981_19121_1490356953}
:::

::: {#-1045025164 .myid}
[]{#_Toc404787177}[]{#_Toc370742269}[]{#struct_0_13981_19121_x1270845497}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp pool**

------------------------------------------------------------------------

[**[ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_952470645}[命令用来创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池，并]{style="font-family:宋体"}[进入]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池视图。如果指定的地址池已存在，则直接进入地址池视图。]{style="font-family:宋体"}

[**[undo ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x1188730773}[命令用来删除指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1927128915}

[**[ipv6 dhcp pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_201873780}

[**[undo ipv6 dhcp pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_2117889312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1319970778}

[[设备上不存在任何]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x132119551}[地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x270921142}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x617247163}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1978382705}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x2017848301}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1843743242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_201939316}

[*[pool-name]{lang="EN-US"}*]{#struct_0_13981_19121_990288430}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_780080358}

[[在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1201760567}[地址池下，可以配置为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、前缀等参数。]{style="font-family:宋体"}

[[需要注意的是，删除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x433242372}[地址池时，该地址池中已经分配的地址绑定信息和前缀绑定信息也将被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x307180768}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1481896153}[创建名称为]{style="font-family:宋体"}[pool1]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池，并]{style="font-family:宋体"}[进入]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1312317347}

[\[Sysname\] ipv6 dhcp pool pool1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-pool1\]]{lang="EN-US"}[]{#_Toc230789652}[]{#_Toc228694666}[]{#_Toc229455098}[]{#_Toc228694669}[]{#_Toc229455101}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_202004852}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp poo]{lang="EN-US"}**[l]{lang="EN-US"}]{#struct_0_13981_19121_1090636857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server apply pool]{lang="EN-US"}**]{#struct_0_13981_19121_x1354940004}
:::

::: {#-427632581 .myid}
[]{#_Toc404787178}[]{#_Toc370742270}[]{#struct_0_13981_19121_513620007}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp prefix-pool**

------------------------------------------------------------------------

[**[ipv6 dhcp prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_1066599506}[命令用来创建前缀池，并指定包含的前缀和分配的前缀长度。]{style="font-family:宋体"}

[**[undo ipv6 dhcp prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_572465900}[命令用来删除指定的前缀池。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2140945684}

[**[ipv6 dhcp prefix-pool]{lang="EN-US"}**[ *prefix-pool-number* **prefix** { *prefix/prefix-len* \| *prefix-number* } **assign-len** *assign-len* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_x2072520653}

[**[undo ipv6 dhcp prefix-pool]{lang="EN-US"}**[ *prefix-pool-number* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_202070388}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1531413769}

[[设备上不存在任何]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_766937391}[前缀池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x835807308}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_738690374}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1081742794}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_639799395}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x176038399}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_202135924}

[*[prefix-pool-number]{lang="EN-US"}*]{#struct_0_13981_19121_x880918485}[：前缀池索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ {*prefix/prefix-len* \| *prefix-number* }]{lang="EN-US"}]{#struct_0_13981_19121_1389469823}[：指定前缀池包含的前缀或引用前缀编号。]{style="font-family:宋体"}*[prefix/prefix-len]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀长度，其中，]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。引用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[assign-len]{lang="EN-US"}**[ *assign-len*]{lang="EN-US"}]{#struct_0_13981_19121_x841988429}[：指定分配的前缀长度。]{style="font-family:宋体"}*[assign-len]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，]{style="font-family:宋体"}*[assign-len]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[，且与]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[之差小于或等于]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x1940628532}[：在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内创建前缀池，并指定包含的前缀和分配的前缀长度。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示配置的是公网中创建前缀池，并指定包含的前缀和分配的前缀长度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x222382455}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所有前缀池包含的前缀范围之间不能重叠，即前缀范围不能相交也不能相互包含。]{style="font-family:宋体"}]{#struct_0_13981_19121_x321721806}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[前缀池创建后不允许修改，只能删除后再重新创建。]{style="font-family:宋体"}]{#struct_0_13981_19121_798520854}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除前缀池，会清除从该前缀池中分配的所有前缀绑定信息。]{style="font-family:宋体"}]{#struct_0_13981_19121_1686943958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备上不存在本命令引用的]{style="font-family:宋体"}]{#struct_0_13981_19121_1483719486}[IPv6]{lang="EN-US"}[前缀，则本命令暂时不会生效。设备上创建引用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，本命令才生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一]{style="font-family:宋体"}]{#struct_0_13981_19121_1615808204}[VPN]{lang="EN-US"}[下的不同前缀池引用的前缀编号不能重叠。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[引用的]{style="font-family:宋体"}]{#struct_0_13981_19121_x1906792204}[IPv6]{lang="EN-US"}[前缀发生变化时，前缀池包含的前缀范围也会随之发生变化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_472449458}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_202201460}[配置前缀池]{style="font-family:宋体"}[1]{lang="EN-US"}[，包含的前缀为]{style="font-family:宋体"}[2001:0410::/32]{lang="EN-US"}[，分配的前缀长度为]{style="font-family:宋体"}[42]{lang="EN-US"}[，即前缀池]{style="font-family:宋体"}[1]{lang="EN-US"}[包含]{style="font-family:宋体"}[2001:0410::/42]{lang="EN-US"}[～]{style="font-family:宋体"}[2001:0410:FFC0::/42]{lang="EN-US"}[范围内的]{style="font-family:宋体"}[1024]{lang="EN-US"}[个前缀。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1026053363}

[\[Sysname\] ipv6 dhcp prefix-pool 1 prefix 2001:0410::/32 assign-len 42]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1739805028}[配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，前缀为]{style="font-family:宋体"}[88:99::/32]{lang="EN-US"}[，配置前缀池]{style="font-family:宋体"}[2]{lang="EN-US"}[引用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号]{style="font-family:宋体"}[3]{lang="EN-US"}[，分配的前缀长度为]{style="font-family:宋体"}[42]{lang="EN-US"}[，即前缀池]{style="font-family:宋体"}[2]{lang="EN-US"}[可以分配]{style="font-family:宋体"}[88:99::/42]{lang="EN-US"}[～]{style="font-family:宋体"}[88:99:FFC0::/42]{lang="EN-US"}[范围内的]{style="font-family:宋体"}[1024]{lang="EN-US"}[个前缀。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1483653950}

[\[Sysname\] ipv6 prefix 3 88:99::/32]{lang="EN-US"}

[\[Sysname\] ipv6 dhcp prefix-pool 2 prefix 3 assign-len 42]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2012180041}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp prefix-poo]{lang="EN-US"}**[l]{lang="EN-US"}]{#struct_0_13981_19121_223504686}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_x1050927254}
:::

::: {#-850495858 .myid}
[]{#_Toc404787179}[]{#_Toc370742271}[]{#struct_0_13981_19121_207761386}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server**

------------------------------------------------------------------------

[**[ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_1461165413}[命令用来配置全局查找地址池，并指定全局查找]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池时地址或前缀分配策略。]{style="font-family:宋体"}

[**[undo ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_x894657867}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_202266996}

[**[ipv6 dhcp server]{lang="EN-US"}[ ]{lang="EN-US"}**[{ **allow-hint** \| **preference** *preference-value* \| **rapid-commit** } \*]{lang="EN-US"}]{#struct_0_13981_19121_x976666346}

[**[undo ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_x1383940505}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1080150069}

[[接口全局查找]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1162953703}[地址池时，不支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配和地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能，服务器优先级的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1853430474}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13981_19121_565416018}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1645276171}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_834407023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1310368418}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_202332532}

[**[allow-hint]{lang="EN-US"}**]{#struct_0_13981_19121_x2101163795}[：指定服务器支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配功能。如果不指定本参数，则表示不支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配功能。]{style="font-family:宋体"}

[**[preference]{lang="EN-US"}**[ *preference-value*]{lang="EN-US"}]{#struct_0_13981_19121_375717283}[：指定发送的]{style="font-family:宋体"}[Advertise]{lang="EN-US"}[消息中的服务器优先级。]{style="font-family:宋体"}*[preference-value]{lang="EN-US"}*[为服务器优先级，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。该值越大，表示服务器的优先级越高，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端选择该服务器分配的地址或前缀的可能性越大。]{style="font-family:宋体"}

[**[rapid-commit]{lang="EN-US"}**]{#struct_0_13981_19121_1491481398}[：指定服务器支持交互两个报文的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能。如果不指定本参数，则表示服务器不支持地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x898047083}

[[如果执行本命令时，指定了]{style="font-family:宋体"}**[allow-hint]{lang="EN-US"}**]{#struct_0_13981_19121_x658204204}[参数，则服务器优先为客户端分配它期望的地址或前缀。如果客户端期望的地址或前缀不在接口可分配的地址池中，或者已经分配给其他客户端，则服务器忽略客户端的期望地址或前缀，并为客户端分配其他空闲地址或前缀。如果没有指定]{style="font-family:宋体"}**[allow-hint]{lang="EN-US"}**[参数，则服务器忽略客户端期望的地址或前缀，从地址池中选择地址或前缀分配给客户端。]{style="font-family:宋体"}

[[需要注意的是，如果在同一个接口上同时执行了]{style="font-family:宋体"}**[ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_x1541136518}[命令和]{style="font-family:宋体"}**[ipv6 dhcp server apply pool]{lang="EN-US"}**[命令，则以]{style="font-family:宋体"}**[ipv6 dhcp server apply pool]{lang="EN-US"}**[命令的配置为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_2095478715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1225742375}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_201349492}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[全局查找地址池，服务器支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配和地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能，优先级设置为最高，即]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_249613206}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp server allow-hint preference 255 rapid-commit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1632476529}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1033219774}[配置接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[全局查找地址池，服务器支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配和地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能，优先级设置为最高，即]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1491682715}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 dhcp server allow-hint preference 255 rapid-commit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x96440524}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_x190879665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp select]{lang="EN-US"}**]{#struct_0_13981_19121_x1140191948}
:::

::: {#2059639537 .myid}
[]{#_Toc404787180}[]{#_Toc370742272}[]{#struct_0_13981_19121_201415028}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server apply pool**

------------------------------------------------------------------------

[**[ipv6 dhcp server apply pool]{lang="EN-US"}**]{#struct_0_13981_19121_902101067}[命令用来指定接口引用的]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[地址池，并指定地址和前缀分配策略。]{style="font-family:
宋体"}

[**[undo ipv6 dhcp server apply pool]{lang="EN-US"}**]{#struct_0_13981_19121_x427077267}[命令用来取消接口引用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1660324823}

[**[ipv6 dhcp server apply pool]{lang="EN-US"}**[ *pool-name* \[ **allow-hint** \| **preference** *preference-value* \| **rapid-commit** \] \*]{lang="EN-US"}]{#struct_0_13981_19121_x1020254632}

[**[undo ipv6 dhcp server apply pool]{lang="EN-US"}**]{#struct_0_13981_19121_1387135774}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_506510941}

[[接口没有引用地址池，接口接收到]{style="font-family:宋体"}]{#struct_0_13981_19121_x1233644947}[DHCPv6]{lang="EN-US"}[请求报文后，]{style="font-family:宋体"}[服务器根据该接口的地址或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的地址选择匹配的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池，并从该地址池中选择]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或前缀分配给客户端。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1995375008}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13981_19121_219002529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_201873777}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1780182309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x2113827300}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_536254170}

[*[pool-name]{lang="EN-US"}*]{#struct_0_13981_19121_x1081428024}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[allow-hint]{lang="EN-US"}**]{#struct_0_13981_19121_149315718}[：指定服务器支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配功能。如果不指定本参数，则表示不支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配功能。]{style="font-family:宋体"}

[**[preference]{lang="EN-US"}**[ *preference-value*]{lang="EN-US"}]{#struct_0_13981_19121_181980449}[：指定发送的]{style="font-family:宋体"}[Advertise]{lang="EN-US"}[消息中的服务器优先级。]{style="font-family:宋体"}*[preference-value]{lang="EN-US"}*[为服务器优先级，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。该值越大，表示服务器的优先级越高，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端选择该服务器分配的地址或前缀的可能性越大。]{style="font-family:宋体"}

[**[rapid-commit]{lang="EN-US"}**]{#struct_0_13981_19121_708499088}[：指定服务器支持交互两个报文的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能。如果不指定本参数，则表示服务器不支持地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_996695757}

[[如果接口上引用了地址池，则从该接口接收到客户端发送的]{style="font-family:宋体"}]{#struct_0_13981_19121_419603197}[DHCPv6]{lang="EN-US"}[请求后，将从引用的地址池中选择]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或]{style="font-family:宋体"}[前缀，分配给客户端]{style="font-family:宋体"}[；否则，服务器将根据接口的地址或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的地址选择匹配的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池，并从该地址池中选择]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或前缀分配给客户端。]{style="font-family:宋体"}

[[如果执行本命令时，指定了]{style="font-family:宋体"}**[allow-hint]{lang="EN-US"}**]{#struct_0_13981_19121_201939313}[参数，则服务器优先为客户端分配它期望的地址或前缀。如果客户端期望的地址或前缀不在接口可分配的地址池中，或者已经分配给其他客户端，则服务器忽略客户端的期望地址或前缀，并为客户端分配其他空闲地址或前缀。如果没有指定]{style="font-family:宋体"}**[allow-hint]{lang="EN-US"}**[参数，则服务器忽略客户端期望的地址或前缀，从地址池中选择地址或前缀分配给客户端。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13981_19121_990288433}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口上最多只能引用一个地址池，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_13981_19121_780080359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口可以引用并不存在的地址池，但是，此时该接口无法为客户端分配]{style="font-family:宋体"}]{#struct_0_13981_19121_x1201760568}[IPv6]{lang="EN-US"}[地址、前缀等信息。只有创建该地址池后，才能为客户端分配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、前缀等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x480296539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_146353531}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1702074929}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[引用已存在的地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[，服务器支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配和地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能，优先级设置为最高，即]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x2093549993}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp server apply pool 1 allow-hint preference 255 rapid-commit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_7680706}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_202004849}[配置接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[引用已存在的地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[，服务器支持期望地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀分配和地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀快速分配功能，优先级设置为最高，即]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1248015312}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 dhcp server apply pool 1 allow-hint preference 255 rapid-commit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1707031105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_13981_19121_x665011416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x1304914693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp select]{lang="EN-US"}**]{#struct_0_13981_19121_x1415022882}
:::

::: {#-1589845883 .myid}
[]{#_Toc404787181}[]{#struct_0_13981_19121_x1940890677}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server database filename**

------------------------------------------------------------------------

[**[ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_1665226892}[命令用来指定存储]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项的文件名称。]{style="font-family:宋体"}

[**[undo ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_1462177704}[命令用来删除指定的存储]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项的文件名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1940825141}

[**[ipv6 dhcp server database filename ]{lang="EN-US"}**[{ *filename* \| **url** *url* \[ **username** *username* \[ **password** { **cipher** \| **simple** } *key* \] \] }]{lang="EN-US"}]{#struct_0_13981_19121_x1941021749}

[**[undo ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_1084810523}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1940956213}

[[未指定存储文件名称。]{style="font-family:宋体"}]{#struct_0_13981_19121_597555040}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1940628533}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x490507576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1260217692}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1940562997}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x968240708}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1479221410}

[*[filename]{lang="EN-US"}*]{#struct_0_13981_19121_x1941152822}[：目标文件名，该配置用于本地存储模式。文件名取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[**[url]{lang="EN-US"}***[ url]{lang="EN-US"}*]{#struct_0_13981_19121_x415470510}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[，该配置用于远程文件系统模式。此参数中不能包含用户名和密码，和参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key]{lang="EN-US"}*[配合使用。]{style="font-family:宋体"}

[**[username]{lang="EN-US"}***[ username]{lang="EN-US"}*]{#struct_0_13981_19121_220910236}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[时的用户名。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_13981_19121_x1941087286}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13981_19121_97135063}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_13981_19121_x1941283894}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[时的密码，为可显字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1799885575}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_13981_19121_x1941218358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_13981_19121_x1940890678}[存储]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项时，如果设备中还不存在对应名称的文件，则设备会自动创建该文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_13981_19121_x1940628534}[执行本命令后，会立即触发一次表项备份。之后，如果未配置]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[ **dhcp** **server** **database** **update** **interval**]{lang="EN-US"}[命令，若表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒之后刷新存储文件；若表项未发生变化，则不再刷新存储文件。如果配置了]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[ **dhcp server** **database** **update** **interval**]{lang="EN-US"}[命令，若表项发生变化，则到达刷新时间间隔后刷新存储文件；若表项未发生变化，则不再刷新存储文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_13981_19121_x1941283887}[不支持远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[，配置远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[请使用]{lang="EN-US" style="font-family:宋体"}*[url]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[username]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[key]{lang="EN-US"}*[配合使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[频繁擦写本地存储介质可能会影响存储介质寿命，建议使用远程文件系统模式存储]{style="font-family:宋体"}]{#struct_0_13981_19121_1483785021}[DHCPv6]{lang="EN-US"}[服务器表项文件。]{style="font-family:宋体"}

[[当进行远程存储时，支持]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_13981_19121_x929063316}[和]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_13981_19121_x1940956207}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议时，服务器地址支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[形式或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[形式，并且支持]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名方式。服务器地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址形式时需使用方括号]{style="font-family:宋体"}[(]{lang="EN-US"}["]{style="font-family:宋体"}[\[]{lang="EN-US"}["和"]{style="font-family:
宋体"}[\]]{lang="EN-US"}["]{style="font-family:宋体"}[)]{lang="EN-US"}[引用。配置服务器地址为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名格式时请勿使用方括号引用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_13981_19121_x1941152816}[当采用]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}*[ftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径]{style="font-family:宋体"}*["的形式，如有用户名和密码请分别使用参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和参数]{style="font-family:宋体"}*[key]{lang="EN-US"}*[进行配置，用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_13981_19121_x1941218352}[TFTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}*[tftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径]{style="font-family:宋体"}*["的形式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1907171379}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1940890672}[配置存储]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项的文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1940825136}

[\[Sysname\] ipv6 dhcp server database filename database.dhcp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1291135941}[配置远程存储]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项至]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10::1]{lang="EN-US"}[的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器工作目录下]{style="font-family:宋体"}[,]{lang="EN-US"}[用户名为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[，文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1941021744}

[\[Sysname\] ipv6 dhcp server database filename url ftp://\[10::1\]/database.dhcp username 1 password simple 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1940956208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update interval]{lang="EN-US"}**]{#struct_0_13981_19121_x1775032419}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update now]{lang="EN-US"}**]{#struct_0_13981_19121_x1940628528}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update stop]{lang="EN-US"}**]{#struct_0_13981_19121_x1940562992}
:::

::: {#339635473 .myid}
[]{#_Toc404787182}[]{#struct_0_13981_19121_x1727755595}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server database update interval**

------------------------------------------------------------------------

[**[ipv6 dhcp server database update interval]{lang="EN-US"}**]{#struct_0_13981_19121_x375068878}[命令用来配置刷新]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项存储文件的延迟时间。]{style="font-family:宋体"}

[**[undo ipv6 dhcp server database update interval]{lang="EN-US"}**]{#struct_0_13981_19121_x1003201344}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x375003342}

[**[ipv6 dhcp server database update interval ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_13981_19121_x375199950}

[**[undo ipv6 dhcp server database interval]{lang="EN-US"}**]{#struct_0_13981_19121_x1801131898}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x375134414}

[[若]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x337062807}[服务器表项不变化，则不刷新表项存储文件；若]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒后刷新表项存储文件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_112708325}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x374806734}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_2009251494}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x374741198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x287535600}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x374937806}

[*[seconds]{lang="EN-US"}*]{#struct_0_13981_19121_x686077461}[：刷新延迟时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[864000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x374872270}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若执行该命令配置之前没有使用]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_872999990}[命令配置固化文件，]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器不会在表项发生变化之后定时刷新表项数据到固化文件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若执行该命令配置之后通过]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_x374544590}[命令配置固化文件，则]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器会在表项发生变化之后刷新表项数据到固化文件，且刷新表项的延迟时间为本命令配置的时间。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当服务器表项发生变化后，]{style="font-family:宋体"}]{#struct_0_13981_19121_1994153472}[DHCPv6]{lang="EN-US"}[服务器开始计时，当本命令配置的延迟时间到达后，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器会把这个时间段内表项所有的变化信息备份到固化文件中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1237177557}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x374479054}[若]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项发生变化，在]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟后刷新表项存储文件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1302653199}

[\[Sysname\] ipv6 dhcp server database update interval 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x375068879}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_x1003135808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update now]{lang="EN-US"}**]{#struct_0_13981_19121_x375003343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 ]{lang="EN-US"}[dhcp server database update ]{lang="EN-US"}**]{#struct_0_13981_19121_1651340850}**[stop]{lang="EN-US"}**
:::

::: {#-761594988 .myid}
[]{#_Toc404787183}[]{#struct_0_13981_19121_x375199951}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server database update now**

------------------------------------------------------------------------

[**[ipv6 dhcp server database update now]{lang="EN-US"}**]{#struct_0_13981_19121_x1801197434}[命令用来将当前]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项保存到用户指定的文件中。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x375134415}

[**[ipv6 dhcp server database update now]{lang="EN-US"}**]{#struct_0_13981_19121_x374806735}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_2009317030}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x374741199}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x287470064}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x847690512}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x374937807}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x686142997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_13981_19121_x374872271}[本命令只用来触发一次]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项的备份。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未通过]{lang="EN-US" style="font-family:宋体"}[ipv6 dhcp server database filename]{lang="EN-US"}]{#struct_0_13981_19121_872934454}[命令指定存储表项的文件，则本命令的配置不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x374544591}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1237243093}[将当前的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项保存到文件中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x374479055}

[\[Sysname\] ipv6 dhcp server database update now]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1302587663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_x375068880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update interval]{lang="EN-US"}**]{#struct_0_13981_19121_x1002677061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 ]{lang="EN-US"}[dhcp server database update ]{lang="EN-US"}**]{#struct_0_13981_19121_x375003344}**[stop]{lang="EN-US"}**
:::

::: {#-114847691 .myid}
[]{#_Toc404787184}[]{#struct_0_13981_19121_1651406386}[]{#_Toc379616752}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server database update stop**

------------------------------------------------------------------------

[**[ipv6 dhcp server database update stop]{lang="EN-US"}**]{#struct_0_13981_19121_x375199952}[命令用来终止当前的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项恢复操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1801262970}

[**[ipv6 dhcp server database update stop]{lang="EN-US"}**]{#struct_0_13981_19121_x375134416}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x374806736}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_2009382566}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1651649934}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x374741200}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1286966791}

[[【使用指导】]{style="font-family:黑体"}[]{lang="EN-US"}]{#struct_0_13981_19121_x374937808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只用来触发一次终止]{style="font-family:宋体"}]{#struct_0_13981_19121_x374872272}[DHCPv6]{lang="EN-US"}[服务器表项的恢复操作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只用来停止设备重启后从固化文件中恢复表项信息的过程，不影响除此之外的其他运行过程。当中断恢复表项信息的过程后，如果]{style="font-family:宋体"}]{#struct_0_13981_19121_873131062}[DHCP]{lang="EN-US"}[服务器分配了未恢复表项中的地址信息，可能会导致局域网设备地址冲突情况发生。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从固化文件恢复表项的连接超时间隔为]{style="font-family:宋体"}]{#struct_0_13981_19121_x374544592}[60]{lang="EN-US"}[分钟，可以通过本命令立刻终止远程恢复。]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器从固化文件中恢复表项的过程中，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器不会学习新的表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1237308629}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x374479056}[终止当前的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器表项恢复操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1302784271}

[\[Sysname\] ipv6 dhcp server database update stop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x375068881}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database filename]{lang="EN-US"}**]{#struct_0_13981_19121_x1002611525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update interval]{lang="EN-US"}**]{#struct_0_13981_19121_x375003345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server database update now]{lang="EN-US"}**]{#struct_0_13981_19121_1651471922}
:::

::: {#-1927664979 .myid}
[]{#_Toc404787185}[]{#_Toc370742273}[]{#struct_0_13981_19121_1414054588}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server forbidden-address**

------------------------------------------------------------------------

[**[ipv6 dhcp server forbidden-address]{lang="DA"}**]{#struct_0_13981_19121_x2146314359}[命令用来配置不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址。]{style="font-family:宋体"}

[**[undo ipv6 dhcp server forbidden-address]{lang="DA"}**]{#struct_0_13981_19121_345634415}[命令用来取消不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_202070385}

[**[ipv6 dhcp server forbidden-address]{lang="EN-US"}**[ *start-ipv6-address* \[ *end-ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_1531413780}

[**[undo ipv6 dhcp server forbidden-address]{lang="EN-US"}**[ *start-ipv6-address* \[ *end-ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_766478649}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1347422951}

[[除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x2122564959}[服务器接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址外，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池中的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址都参与自动分配。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1666021828}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_135375544}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_901635501}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1148944674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_894988358}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_202135921}

[*[start-ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x880918482}[：不参与自动分配的起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[end-ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_1389797503}[：不参与自动分配的结束]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不能小于]{style="font-family:宋体"}*[start-ipv6-address]{lang="EN-US"}*[。如果不指定该参数，则表示只有一个不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，即]{style="font-family:宋体"}*[start-ipv6-address]{lang="EN-US"}*[；否则，表示]{style="font-family:宋体"}*[start-ipv6-address]{lang="EN-US"}*[到]{style="font-family:宋体"}*[end-ipv6-address]{lang="EN-US"}*[之间的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址均不能参与自动分配。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x374937809}[：配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示配置的是公网中不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_313316578}

[[某些服务器占用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1405106837}[地址（如网关地址、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器地址），不能分配给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端。通过本命令可以避免这些地址参与自动分配。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13981_19121_x278002961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server forbidden-address]{lang="EN-US"}**]{#struct_0_13981_19121_1905978063}[将已经静态绑定的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址配置为不参与自动分配的地址，则该地址仍然可以分配给静态绑定的用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo ipv6 dhcp server forbidden-address]{lang="EN-US"}**]{#struct_0_13981_19121_1415628701}[命令取消不参与自动分配]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的配置时，指定的地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[地址范围必须与执行]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server forbidden-address]{lang="EN-US"}**[命令时指定的地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[地址范围保持一致。]{lang="EN-US" style="font-family:宋体"}[如果配置不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为某一地址范围，则只能同时取消该地址范围内所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的配置，不能单独取消其中某个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server forbidden-address]{lang="EN-US"}**]{#struct_0_13981_19121_952805819}[命令，可以配置多个不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1518340536}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_202201457}[配置]{style="font-family:宋体"}[2001:10:110::1]{lang="EN-US"}[到]{style="font-family:宋体"}[2001:10:110::20]{lang="EN-US"}[之间的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不参与地址自动分配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1312598790}

[\[Sysname\] ipv6 dhcp server forbidden-address 2001:10:110::1 2001:10:110::20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1994003416}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol;color:windowtext"}]{.3Char}**[ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**]{#struct_0_13981_19121_1007090395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-bind]{lang="EN-US"}**]{#struct_0_13981_19121_x1698618399}
:::

::: {#-1308094282 .myid}
[]{#_Toc404787186}[]{#_Toc370742274}[]{#struct_0_13981_19121_548784568}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- ipv6 dhcp server forbidden-prefix**

------------------------------------------------------------------------

[**[ipv6 dhcp server forbidden-prefix]{lang="DA"}**]{#struct_0_13981_19121_x1366316027}[命令用来配置不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[前缀。]{style="font-family:宋体"}

[**[undo ipv6 dhcp server forbidden-prefix]{lang="DA"}**]{#struct_0_13981_19121_x2039514685}[命令用来取消不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[前缀的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1693421604}

[**[ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**[ *start-prefix/prefix-len* \[ *end-prefix/prefix-len* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_202266993}

[**[undo ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**[ *start-prefix/prefix-len* \[ *end-prefix/prefix-len* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_x976666349}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1383743897}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_229974276}[前缀池中的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀都参与自动分配。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1459839709}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1289376838}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1853202226}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1856951765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x2047496367}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_722978373}

[*[start-prefix/prefix-len]{lang="EN-US"}*]{#struct_0_13981_19121_202332529}[：不参与自动分配的起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[为前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[end-prefix/prefix-len]{lang="EN-US"}*]{#struct_0_13981_19121_237488370}[：不参与自动分配的结束]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[为前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}*[end-prefix]{lang="EN-US"}*[的取值不能小于]{style="font-family:宋体"}*[start-prefix]{lang="EN-US"}*[。如果不指定该参数，则表示只有一个不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀，即]{style="font-family:宋体"}*[start-prefix/prefix-len]{lang="EN-US"}*[；否则，表示]{style="font-family:宋体"}*[start-prefix/prefix-len]{lang="EN-US"}*[到]{style="font-family:宋体"}*[end-prefix/prefix-len]{lang="EN-US"}*[之间的前缀均不能参与自动分配。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x374479057}[：配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[前缀。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示配置的是公网中不参与自动分配的]{style="font-family:宋体"}[IPv6]{lang="DA"}[前缀。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1229036569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**]{#struct_0_13981_19121_1245596336}[将已经静态绑定的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀配置为不参与自动分配的前缀，则该前缀仍然可以分配给静态绑定的用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**]{#struct_0_13981_19121_x1102215280}[命令取消不参与自动分配]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[v6]{lang="EN-US"}[前缀的配置时，指定的前缀]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[前缀范围必须与执行]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**[命令时指定的前缀]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[前缀范围保持一致。]{lang="EN-US" style="font-family:宋体"}[如果配置不参与自动分配的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[前缀为某一前缀范围，则只能同时取消该前缀范围内所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[前缀的配置，不能单独取消其中某个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp server forbidden-prefix]{lang="EN-US"}**]{#struct_0_13981_19121_x1198406321}[命令，可以配置多个不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀段。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1792678990}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x916606053}[配置]{style="font-family:宋体"}[2001:3e11::/32]{lang="EN-US"}[到]{style="font-family:宋体"}[2001:3eff::/32]{lang="EN-US"}[之间的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀不参与前缀自动分配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1284719592}

[\[Sysname\] ipv6 dhcp server forbidden-prefix 2001:3e11::/32 2001:3eff::/32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_201349489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp server forbidden-address]{lang="EN-US"}**]{#struct_0_13981_19121_x1706701939}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-bind]{lang="EN-US"}**]{#struct_0_13981_19121_x252402852}
:::

::: {#-815886662 .myid}
[]{#_Toc404787187}[]{#_Toc370742275}[]{#struct_0_13981_19121_1921845590}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- network**

------------------------------------------------------------------------

[**[network]{lang="EN-US"}**]{#struct_0_13981_19121_1830278414}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}

[**[undo network]{lang="EN-US"}**]{#struct_0_13981_19121_558414388}[命令用来删除动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2091315643}

[**[network]{lang="EN-US"}**[ { *prefix/prefix-length* \| **prefix** *prefix-number* \[ *sub-prefix/sub-prefix-length* \] } \[ **preferred-lifetime** *preferred-lifetime* **valid-lifetime** *valid-lifetime* \] \[ **export-route** \] ]{lang="EN-US"}]{#struct_0_13981_19121_x985683626}

[**[undo network]{lang="EN-US"}**]{#struct_0_13981_19121_2049560719}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1658177673}

[[未配置动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_201415025}[地址网段，即没有可供分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_902101054}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1146900844}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2045623629}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1781219651}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x121799439}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_2043681521}

[*[prefix/prefix-length]{lang="EN-US"}*]{#struct_0_13981_19121_1079225392}[：用于动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}*[prefix/prefix-length]{lang="EN-US"}*[为地址网段的前缀和前缀长度，]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix-number*]{lang="EN-US"}]{#struct_0_13981_19121_1484112695}[：引用前缀作为动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}*[prefix-number]{lang="EN-US"}*[为前缀编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[sub-prefix/sub-prefix-length]{lang="EN-US"}*]{#struct_0_13981_19121_1476693526}[：]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[子前缀及子前缀长度。]{style="font-family:宋体"}*[sub-prefix-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子前缀及子前缀长度用来进一步划分引用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。如果被引用的前缀长度大于子前缀长度]{style="font-family:宋体"}*[sub-prefix-length]{lang="EN-US"}*[，则使用被引用的前缀长度作为动态分配地址网段的前缀长度。如果不配置此参数，则使用前缀编号对应的前缀作为动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}

[**[preferred-lifetime]{lang="EN-US"}**[ *preferred-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_x266824943}[：指定地址池中分配的地址和前缀的首选生命期。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[为地址和前缀的首选生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[604800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）。]{style="font-family:宋体"}

[**[valid-lifetime]{lang="EN-US"}**[ *valid-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_201873778}[：指定地址池中分配的地址和前缀的有效生命期。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[为地址和前缀的有效生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[2592000]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[天）。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}[-route]{lang="EN-US"}**]{#struct_0_13981_19121_x374741194}[：将网段信息下发给路由管理，由路由管理发布指定网段信息的路由。引导指定网段的下行数据流量。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1780182296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_13981_19121_x157184493}[DHCPv6]{lang="EN-US"}[地址池只能配置一个网段，如果多次执行]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改或删除]{style="font-family:宋体"}]{#struct_0_13981_19121_x1536221293}**[network]{lang="EN-US"}**[命令的配置，会导致该地址池下现有的已分配地址被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[network export-route]{lang="EN-US"}**]{#struct_0_13981_19121_x374937802}[命令可以用来发布网段路由，如果多次执行此命令，则新的配置会覆盖已有配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置]{lang="EN-US" style="font-family:宋体"}**[network prefix]{lang="EN-US"}**]{#struct_0_13981_19121_1484047159}[命令之前设备上不存在]{lang="EN-US" style="font-family:
宋体"}[前缀]{style="font-family:宋体"}[编号为]{lang="EN-US" style="font-family:宋体"}*[prefix-number]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀，则]{lang="EN-US" style="font-family:宋体"}**[network prefix]{lang="EN-US"}**[命令暂时不会生效。设备上创建]{lang="EN-US" style="font-family:宋体"}[前缀]{style="font-family:
宋体"}[编号为]{lang="EN-US" style="font-family:宋体"}*[prefix-number]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，配置的]{lang="EN-US" style="font-family:宋体"}**[network prefix]{lang="EN-US"}**[命令才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同地址池通过]{style="font-family:宋体"}]{#struct_0_13981_19121_x92678842}**[network]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}*[prefix/prefix-length]{lang="EN-US"}*[不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[地址池通过前缀编号和]{style="font-family:宋体"}*[sub-prefix/sub-prefix-length]{lang="EN-US"}*]{#struct_0_13981_19121_1402578517}[得出自身可分配的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址网段。所以不同地址池通过配置]{style="font-family:宋体"}**[network prefix]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[引用的前缀编号和]{style="font-family:宋体"}*[sub-prefix/sub-prefix-length]{lang="EN-US"}*[不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}**[network prefix]{lang="EN-US"}**]{#struct_0_13981_19121_1369557024}[命令引用的前缀发生改变，则]{lang="EN-US" style="font-family:
宋体"}**[network prefix]{lang="EN-US"}**[命令生成的地址网段也会随之]{lang="EN-US" style="font-family:宋体"}[发生]{style="font-family:
宋体"}[改变]{lang="EN-US" style="font-family:宋体"}[。已经动态分配的前缀和地址绑定信息都会被自动清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1387457867}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_625551747}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[动态分配的地址网段为]{style="font-family:宋体"}[3ffe:501:ffff:100::/64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_212063875}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] network 3ffe:501:ffff:100::/64]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1483981623}[配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀为]{style="font-family:宋体"}[88:99::/32]{lang="EN-US"}[。配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段时，指定引用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号]{style="font-family:宋体"}[3]{lang="EN-US"}[，则]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[可分配的地址网段为引用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀对应的网段，即]{style="font-family:宋体"}[88:99::/32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1567550180}

[\[Sysname\] ipv6 prefix 3 88:99::/32]{lang="EN-US"}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] network prefix 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1658278704}[配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀为]{style="font-family:宋体"}[88:99::/32]{lang="EN-US"}[。配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址网段时，指定引用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号]{style="font-family:宋体"}[3]{lang="EN-US"}[，并指定子前缀及子前缀长度为]{style="font-family:宋体"}[3ffe:501:ffff:100::/64]{lang="EN-US"}[，则]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[可分配的地址网段为]{style="font-family:宋体"}[88:99:ffff:100::/64]{lang="EN-US"}[，即前]{style="font-family:宋体"}[32]{lang="EN-US"}[位由]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号]{style="font-family:宋体"}[3]{lang="EN-US"}[决定，]{style="font-family:宋体"}[33]{lang="EN-US"}[位～]{style="font-family:宋体"}[64]{lang="EN-US"}[位由子前缀及子前缀长度决定，且动态分配地址网段的前缀长度为子前缀长度]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1483916087}

[\[Sysname\] ipv6 prefix 3 88:99::/32]{lang="EN-US"}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] network prefix 3 3ffe:501:ffff:100::/64]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_509332606}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range]{lang="EN-US"}**]{#struct_0_13981_19121_1224880392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_201939314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[temporary address range]{lang="EN-US"}**]{#struct_0_13981_19121_990288428}
:::

::: {#-1888502768 .myid}
[]{#_Toc404787188}[]{#_Toc370742276}[]{#struct_0_13981_19121_x1558571810}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- option**

------------------------------------------------------------------------

[**[option]{lang="EN-US"}**]{#struct_0_13981_19121_1233266852}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[自定义选项。]{style="font-family:宋体"}

[**[undo option]{lang="EN-US"}**]{#struct_0_13981_19121_x1311364054}[命令用来删除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[自定义选项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1861145343}

[**[option ]{lang="EN-US"}***[code]{lang="EN-US"}***[ hex]{lang="EN-US"}**[ *hex-string*]{lang="EN-US"}]{#struct_0_13981_19121_x1316513096}

[**[undo option code]{lang="EN-US"}**]{#struct_0_13981_19121_x1570105015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_2077988386}

[[未配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1595506083}[地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[自定义选项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_202004850}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1090636855}[地址池视图]{style="font-family:宋体"}[/DHCPv6]{lang="EN-US"}[选项组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1354808932}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_219812796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1782464416}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1639556578}

[*[code]{lang="EN-US"}*]{#struct_0_13981_19121_x2026624194}[：选项的数值，取值范围为]{style="font-family:宋体"}[21]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，不包括]{style="font-family:宋体"}[25]{lang="EN-US"}[～]{style="font-family:宋体"}[26]{lang="EN-US"}[，]{style="font-family:宋体"}[37]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[，]{style="font-family:宋体"}[43]{lang="EN-US"}[～]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hex]{lang="EN-US"}**[ *hex-string*]{lang="EN-US"}]{#struct_0_13981_19121_x1222483638}[：指定选项内容为配置的十六进制数串。]{style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[为偶数位的十六进制数串，位数的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1538082721}

[[通过执行本命令，可以配置编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_13981_19121_202070386}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项内容为指定的十六进制数串，即采用指定的内容来填充]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[应答报文中编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[的选项，以便将指定的选项内容分配给客户端。]{style="font-family:宋体"}

[[本命令为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1531413783}[服务器提供了灵活的选项配置方式，使得]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器可以为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端提供更加丰富的选项内容。在以下情况下，可以使用本命令配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[自定义选项：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[随着]{style="font-family:宋体"}]{#struct_0_13981_19121_766544185}[DHCPv6]{lang="EN-US"}[的不断发展，新的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项会陆续出现。通过配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[自定义选项，可以方便地添加新的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些选项的内容，]{style="font-family:宋体"}]{#struct_0_13981_19121_703966713}[RFC]{lang="EN-US"}[中没有统一规定。厂商可以根据需要定义选项的内容，如]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[。通过配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[自定义选项，可以为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端提供厂商指定的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备上只提供了有限的选项配置命令（如]{style="font-family:宋体"}]{#struct_0_13981_19121_710122655}**[dns-server]{lang="EN-US"}**[命令），对于没有专门命令来配置的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项，可以通过]{style="font-family:宋体"}**[option]{lang="EN-US"}**[命令配置选项内容。]{style="font-family:宋体"}[例如，可以通过]{lang="EN-US" style="font-family:宋体"}**[option ]{lang="EN-US"}[31]{lang="EN-US"}**[ **hex** ]{lang="EN-US"}[00c80000000000000000000000000001]{lang="EN-US"}[命令指定为]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[v6]{lang="EN-US"}[客户端分配的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器地址为]{lang="EN-US" style="font-family:宋体"}[200::1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13981_19121_x1910574245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行本命令，并指定相同的选项数值]{style="font-family:宋体"}]{#struct_0_13981_19121_x762986712}*[code]{lang="EN-US"}*[，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些]{style="font-family:宋体"}]{#struct_0_13981_19121_x595468983}[DHCPv6]{lang="EN-US"}[选项既可以通过专门的命令来配置，也可以通过]{style="font-family:宋体"}**[option]{lang="EN-US"}**[命令来配置。例如，]{style="font-family:宋体"}[Option 23]{lang="EN-US"}[（]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址选项）既可以通过]{style="font-family:宋体"}**[dns-server]{lang="EN-US"}**[命令配置，也可以通过]{style="font-family:宋体"}**[option 23]{lang="EN-US"}**[命令配置。如果同时通过上述两种方式配置了这些选项，则在填充]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[应答报文的选项时，优先选择专门命令的配置。如果没有通过专门命令来配置，则采用]{style="font-family:宋体"}**[option]{lang="EN-US"}**[命令配置的内容填充选项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x74022572}

[[\# DNS]{lang="EN-US"}]{#struct_0_13981_19121_202135922}[服务器地址选项的编号为]{style="font-family:宋体"}[23]{lang="EN-US"}[。在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[中配置为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[2001:f3e0::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x880918479}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] option 23 hex 2001f3e0000000000000000000000001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1390256242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x552123863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-server]{lang="EN-US"}**]{#struct_0_13981_19121_x1155165134}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain-name]{lang="EN-US"}**]{#struct_0_13981_19121_365362701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sip]{lang="EN-US"}[-server]{lang="EN-US"}**]{#struct_0_13981_19121_x1103696748}
:::

::: {#-1300652415 .myid}
[]{#_Toc404787189}[]{#struct_0_13981_19121_1483653943}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- option-group**

------------------------------------------------------------------------

[**[option-group]{lang="EN-US"}**]{#struct_0_13981_19121_479986321}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池引用选项组。]{style="font-family:宋体"}

[**[undo option-group]{lang="EN-US"}**]{#struct_0_13981_19121_1334699119}[命令用来删除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池引用选项组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1484636983}

[**[option-group ]{lang="EN-US"}***[option-group-number]{lang="EN-US"}*]{#struct_0_13981_19121_x70426514}

[**[undo option-group]{lang="EN-US"}**]{#struct_0_13981_19121_x1860814910}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2085719516}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_992285074}[地址池未引用任何选项组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1674334836}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_817825682}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1812007542}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1529510340}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1100270792}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1249831884}

[*[option-group-number]{lang="EN-US"}*]{#struct_0_13981_19121_1484571447}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1459940198}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x236706829}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[引用选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1555957374}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] option-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2108712322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x81971241}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp option-group]{lang="EN-US"}**]{#struct_0_13981_19121_1517218187}
:::

::: {#-1321932509 .myid}
[]{#_Toc404787190}[]{#_Toc370742277}[]{#struct_0_13981_19121_2004836505}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- prefix-pool**

------------------------------------------------------------------------

[**[prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_x44761193}[命令用来配置地址池引用前缀池，以便从前缀池中动态选择前缀分配给客户端。]{style="font-family:宋体"}

[**[undo prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_202201458}[命令用来取消地址池引用前缀池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1312598805}

[**[prefix-pool]{lang="EN-US"}**[ *prefix-pool-number* \[ **preferred-lifetime** *preferred-lifetime* **valid-lifetime** *valid-lifetime* \]]{lang="EN-US"}]{#struct_0_13981_19121_1234029776}

[**[undo prefix-pool]{lang="EN-US"}**[ *prefix-pool-number*]{lang="EN-US"}]{#struct_0_13981_19121_1221805405}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x547695353}

[[未配置地址池引用的]{style="font-family:宋体"}]{#struct_0_13981_19121_1937748931}[前缀池]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1889646997}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_741171309}[地址池]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1659342082}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_202266994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x976666344}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1384071577}

[*[prefix-pool-number]{lang="EN-US"}*]{#struct_0_13981_19121_1518495461}[：前缀池索引，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[preferred-lifetime]{lang="EN-US"}**[ *preferred-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_475095663}[：指定分配前缀的首选生命期。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[为前缀的首选生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[604800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）。]{style="font-family:宋体"}

[**[valid-lifetime]{lang="EN-US"}**[ *valid-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_x798534875}[：指定分配前缀的有效生命期。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[为前缀的有效生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[2592000]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[天）。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x669321098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址池最多只能引用一个前缀池。]{style="font-family:宋体"}]{#struct_0_13981_19121_x1196452460}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[地址池可以引用并不存在的前缀池，但是，此时设备无法从该地址池中动态选择前缀分配给客户端。只有创建该前缀池后，才能支持前缀的动态分配。]{style="font-family:宋体"}]{#struct_0_13981_19121_954328613}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许通过重复执行本命令的方式修改地址池引用的前缀池、前缀的首选生命期和有效生命期。只有取消当前地址池引用的前缀池后，才能引用其它前缀池，或修改前缀的首选生命期和有效生命期。]{style="font-family:宋体"}]{#struct_0_13981_19121_x2106087940}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_202332530}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x2101163797}[在地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[中引用前缀池]{style="font-family:宋体"}[1]{lang="EN-US"}[，首选生命期和有效生命期为缺省值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1538516697}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] prefix-pool 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x934007992}[在地址池]{style="font-family:宋体"}[2]{lang="EN-US"}[中引用前缀池]{style="font-family:宋体"}[2]{lang="EN-US"}[，并设置首选生命期为]{style="font-family:宋体"}[1]{lang="EN-US"}[天，有效生命期为]{style="font-family:宋体"}[3]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1785101355}

[\[Sysname\] ipv6 dhcp pool 2]{lang="EN-US"}

[\[Sysname-dhcp6-pool-2\] prefix-pool 2 preferred-lifetime 86400 valid-lifetime 259200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1080194399}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp poo]{lang="EN-US"}**[l]{lang="EN-US"}]{#struct_0_13981_19121_1976977848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp prefix-pool]{lang="EN-US"}**]{#struct_0_13981_19121_229997291}
:::

::: {#1144212899 .myid}
[]{#_Toc404787191}[]{#_Toc370742278}[]{#struct_0_13981_19121_201349490}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- reset ipv6 dhcp server conflict**

------------------------------------------------------------------------

[**[reset ipv6 dhcp server conflict]{lang="EN-US"}**]{#struct_0_13981_19121_249613204}[命令用来清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址冲突信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1632476527}

[**[reset ipv6 dhcp server conflict]{lang="EN-US"}**[ \[ **address** *ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_1839788828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_764459412}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1007986850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x730407274}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x141130552}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_653594824}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_201415026}

[**[address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_902101053}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址冲突信息。如果不指定本参数，则清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址冲突信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x375134411}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址冲突信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址冲突信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1146900841}

[[如果网络配置不合理，则动态分配的地址和网络中静态配置的地址可能会发生冲突。在合理调整网络配置，不再存在冲突的情况下，原来发生冲突的地址可以重新分配给客户端。此时，通过本命令清除检测到的冲突地址，则该地址可以被重新分配。]{style="font-family:宋体"}]{#struct_0_13981_19121_x2045820237}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1121320169}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x982536151}[清除全部地址冲突信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server conflict]{lang="EN-US"}]{#struct_0_13981_19121_1774988806}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2059301113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server conflict]{lang="EN-US"}**]{#struct_0_13981_19121_418356985}
:::

::: {#-1404290294 .myid}
[]{#_Toc404787192}[]{#_Toc370742279}[]{#struct_0_13981_19121_2124188082}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- reset ipv6 dhcp server expired**

------------------------------------------------------------------------

[**[reset ipv6 dhcp server expired]{lang="EN-US"}**]{#struct_0_13981_19121_x163197986}[命令用来清除租约过期的]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1775587574}

[**[reset ipv6 dhcp server expired]{lang="EN-US"}**[ \[ \[ **address** *ipv6-address* \] \[ **vpn-instance** *vpn-instance-name* \] \| **pool** *pool-name* \] ]{lang="EN-US"}]{#struct_0_13981_19121_x204309657}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x979826055}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1580187296}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_703911194}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x877558057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1636261261}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124253618}

[**[address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_x537426705}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的租约过期地址绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x374872267}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的租约过期的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的租约过期的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[**[pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}*]{#struct_0_13981_19121_1219426652}[：清除指定地址池中租约过期的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x709104174}

[[执行本命令时，如果不指定任何参数，则清除所有租约过期的地址绑定信息。]{style="font-family:宋体"}]{#struct_0_13981_19121_988660551}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1416373282}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1445092274}[清除地址]{style="font-family:宋体"}[2001:f3e0::1]{lang="EN-US"}[的租约过期地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server expired address 2001:f3e0::1]{lang="EN-US"}]{#struct_0_13981_19121_1407084925}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2046167464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server expired]{lang="EN-US"}**]{#struct_0_13981_19121_2124319154}
:::

::: {#-635212120 .myid}
[]{#_Toc404787193}[]{#_Toc370742280}[]{#struct_0_13981_19121_620707882}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- reset ipv6 dhcp server ip-in-use**

------------------------------------------------------------------------

[**[reset ipv6 dhcp server ip-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_x1515541697}[命令用来清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[的正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1726587510}

[**[reset ipv6 dhcp server ip-in-use]{lang="EN-US"}**[ \[ **address** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **pool** *pool-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_x985361475}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1486374613}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_853547245}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1059317904}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1639419925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_2124384690}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1832408151}

[**[address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_x360728214}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的正式地址绑定和临时地址绑定信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x778353405}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_1806859408}[：清除指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_306396245}

[[执行本命令时，如果不指定任何参数，则清除所有的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1570714462}[正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}

[[需要注意的是，执行本命令后，静态临时地址绑定和静态正式地址绑定信息将变为静态无效地址绑定。]{style="font-family:宋体"}]{#struct_0_13981_19121_970983179}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1000257293}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1341554188}[清除所有的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server ip-in-use]{lang="EN-US"}]{#struct_0_13981_19121_2124450226}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x899471387}[清除指定地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server ip-in-use pool 1]{lang="EN-US"}]{#struct_0_13981_19121_1303556498}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_2083064966}[清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[正式地址绑定和临时地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server ip-in-use address 2001:0:0:1::1]{lang="EN-US"}]{#struct_0_13981_19121_1505049955}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x495043231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server ip-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_846055281}
:::

::: {#2141876468 .myid}
[]{#_Toc404787194}[]{#_Toc370742281}[]{#struct_0_13981_19121_x2036771259}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- reset ipv6 dhcp server pd-in-use**

------------------------------------------------------------------------

[**[reset ipv6 dhcp server pd-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_667200839}[命令用来清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[正式前缀绑定和临时前缀绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124515762}

[**[reset ipv6 dhcp server pd-in-use]{lang="EN-US"}**[ \[ **pool** *pool-name* \| \[ **prefix** *prefix/prefix-len* \] \[ **vpn-instance** *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_x1678915149}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1280005403}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1860943481}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2071547778}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1031828038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1660564210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_135603603}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_13981_19121_1441622384}[：清除指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的前缀绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix/prefix-len*]{lang="EN-US"}]{#struct_0_13981_19121_2124581298}[：清除指定前缀的前缀绑定信息*。*]{style="font-family:宋体"}*[prefix/prefix-len]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀长度，]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x778484477}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的正式前缀绑定和临时前缀绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的正式前缀绑定和临时前缀绑定信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1827773460}

[[执行本命令时，如果不指定任何参数，则清除所有的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_82547030}[前缀绑定信息。]{style="font-family:宋体"}

[[需要注意的是，执行本命令后，静态临时前缀绑定和静态正式前缀绑定信息将变为静态无效前缀绑定。]{style="font-family:宋体"}]{#struct_0_13981_19121_725923913}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1823554439}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x843161392}[清除所有的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[前缀绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server pd-in-use]{lang="EN-US"}]{#struct_0_13981_19121_434275679}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1571386253}[清除指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池的正式前缀绑定和临时前缀绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server pd-in-use pool 1]{lang="EN-US"}]{#struct_0_13981_19121_x247598898}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_2124646834}[清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的前缀绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server pd-in-use prefix 2001:0:0:1::/64]{lang="EN-US"}]{#struct_0_13981_19121_1091911274}[]{#_Toc228694679}[]{#_Toc229455111}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1747903214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server pd-in-use]{lang="EN-US"}**]{#struct_0_13981_19121_1022742034}
:::

::: {#1678327936 .myid}
[]{#_Toc404787195}[]{#_Toc370742282}[]{#struct_0_13981_19121_593894584}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- reset ipv6 dhcp server statistics**

------------------------------------------------------------------------

[**[reset ipv6 dhcp server statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x1367360507}[命令用来清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_800582252}

[**[reset ipv6 dhcp server statistics]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1970121405}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1291928204}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_2123663794}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1945535851}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x624630433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_46727576}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778025725}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x778222333}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_141388723}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x444041031}[清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp server statistics]{lang="EN-US"}]{#struct_0_13981_19121_1877443846}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1950656794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp server statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x1822004940}
:::

::: {#-345172994 .myid}
[]{#_Toc404787196}[]{#_Toc370742283}[]{#struct_0_13981_19121_2123729330}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- sip-server**

------------------------------------------------------------------------

[**[sip-server]{lang="EN-US"}**]{#struct_0_13981_19121_382681268}[命令用来配置为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器地址或域名。]{style="font-family:宋体"}

[**[undo sip-server]{lang="EN-US"}**]{#struct_0_13981_19121_x1508830428}[命令用来删除为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器地址或域名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1858631873}

[**[sip-server]{lang="EN-US"}**[ { **address** *ipv6-address* \| **domain-name** *domain-name* }]{lang="EN-US"}]{#struct_0_13981_19121_893169709}

[**[undo sip-server]{lang="EN-US"}**[ { **address** *ipv6-address* \| **domain-name** *domain-name* }]{lang="EN-US"}]{#struct_0_13981_19121_1967444122}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_460858806}

[[未]{style="font-family:宋体"}]{#struct_0_13981_19121_763540455}[指定为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器地址和域名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1759782977}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_2124188083}[地址池视图]{style="font-family:宋体"}[/DHCPv6]{lang="EN-US"}[选项组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x163132450}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1375013364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1644538280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1026562030}

[**[address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x699224373}[：指定]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[domain-name]{lang="EN-US"}***[ domain-name]{lang="EN-US"}*]{#struct_0_13981_19121_1148385257}[：指定]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器的域名，]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[50]{lang="EN-US"}[个字节的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_85386789}

[[同一地址池下最多可以配置]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_13981_19121_1389734653}[个]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器地址和]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器域名。配置的先后顺序决定了]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器地址或域名的优先级，即先配置的地址或域名优先级高于后配置的地址或域名。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124253619}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x537492241}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[2:2::4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1967862836}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] sip-server address 2:2::4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1259810092}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[为客户端分配的]{style="font-family:宋体"}[SIP]{lang="EN-US"}[服务器域名为]{style="font-family:宋体"}[bbb.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-dhcp6-pool-1\] sip-server domain-name bbb.com]{lang="EN-US"}]{#struct_0_13981_19121_1776958010}[]{#_Toc228694683}[]{#_Toc229455115}[]{#_Toc228694684}[]{#_Toc229455116}[]{#_Toc228694685}[]{#_Toc229455117}[]{#_Toc228694686}[]{#_Toc229455118}[]{#_Toc228694687}[]{#_Toc229455119}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x292253946}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp poo]{lang="EN-US"}**[l]{lang="EN-US"}]{#struct_0_13981_19121_344311726}
:::

::: {#1012678815 .myid}
[]{#_Toc404787197}[]{#_Toc370742284}[]{#struct_0_13981_19121_x1486621644}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- static-bind**

------------------------------------------------------------------------

[**[static-bind]{lang="EN-US"}**]{#struct_0_13981_19121_2124319155}[命令用来配置静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或前缀，以便实现]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器为特定的客户端分配固定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或前缀。]{style="font-family:宋体"}

[**[undo static-bind]{lang="EN-US"}**]{#struct_0_13981_19121_620642346}[命令用来删除静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或前缀]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1847881396}

[**[static-bind ]{lang="EN-US"}**[{ **address** *ipv6-address/addr-prefix-length* \| **prefix** *prefix/prefix-len* } **duid** *duid* \[ **iaid** *iaid* \] \[ **preferred-lifetime** *preferred-lifetime* **valid-lifetime** *valid-lifetime* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1701710765}

[**[undo static-bind]{lang="EN-US"}**[ { **address** *ipv6-address/addr-prefix-length* \| **prefix** *prefix/prefix-len* }]{lang="EN-US"}]{#struct_0_13981_19121_96358238}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1714980119}

[[未配置静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_1812835562}[地址和前缀]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124384691}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1832473687}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x713848518}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x53577735}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x244874009}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1245265766}

[**[address]{lang="EN-US"}**[ *ipv6-address/addr-prefix-length*]{lang="EN-US"}]{#struct_0_13981_19121_x726342071}[：指定静态绑定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及地址前缀长度。]{style="font-family:宋体"}*[addr-prefix-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix/prefix-len*]{lang="EN-US"}]{#struct_0_13981_19121_491776581}[：指定静态绑定的前缀及前缀长度。]{style="font-family:宋体"}*[prefix-len]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[duid]{lang="EN-US"}**[ *duid*]{lang="EN-US"}]{#struct_0_13981_19121_2124450227}[：指定静态绑定的客户端]{style="font-family:宋体"}[DUID]{lang="EN-US"}[字符串。]{style="font-family:宋体"}*[duid]{lang="EN-US"}*[取值为偶数位的十六进制数，且位数的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[iaid]{lang="EN-US"}**[ *iaid*]{lang="EN-US"}]{#struct_0_13981_19121_x899536923}[：指定静态绑定的客户端]{style="font-family:宋体"}[IAID]{lang="EN-US"}[。]{style="font-family:宋体"}*[iaid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[的十六进制数。不指定该参数，则表示不需要匹配客户端的]{style="font-family:宋体"}[IAID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[preferred-lifetime]{lang="EN-US"}**[ *preferred-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_2054098746}[：指定静态绑定的地址或前缀的首选生命期。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[为地址或前缀的首选生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[604800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）。]{style="font-family:宋体"}

[**[valid-lifetime]{lang="EN-US"}**[ *valid-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_x507789972}[：指定静态绑定的地址或前缀的有效生命期。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[为地址或前缀的有效生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[2592000]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[天）。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1496249608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行]{lang="EN-US" style="font-family:宋体"}**[static-bind]{lang="EN-US"}**]{#struct_0_13981_19121_1553088815}[命令，可以配置多个静态绑定的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和前缀。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一]{style="font-family:宋体"}]{#struct_0_13981_19121_x446510615}[IPv6]{lang="EN-US"}[地址或者前缀只能绑定给一个客户端。不允许通过重复执行本命令的方式修改]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或者前缀与客户端的绑定关系。只有删除了某个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或者前缀的静态绑定关系后，才能将该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或者前缀重新与其他客户端绑定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124515763}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1678980685}[在地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[中配置静态绑定地址：将地址]{style="font-family:宋体"}[2001:0410::1/35]{lang="EN-US"}[固定分配给]{style="font-family:宋体"}[DUID]{lang="EN-US"}[为]{style="font-family:宋体"}[0003000100e0fc005552]{lang="EN-US"}[、]{style="font-family:宋体"}[IAID]{lang="EN-US"}[为]{style="font-family:宋体"}[A1A1A1A1]{lang="EN-US"}[的客户端。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1775132119}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] static-bind address 2001:0410::1/35 duid 0003000100e0fc005552 iaid A1A1A1A1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_2139178571}[在地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[中配置静态绑定前缀：将前缀]{style="font-family:宋体"}[2001:0410::/35]{lang="EN-US"}[固定分配给]{style="font-family:宋体"}[DUID]{lang="EN-US"}[为]{style="font-family:宋体"}[00030001CA0006A400]{lang="EN-US"}[、]{style="font-family:宋体"}[IAID]{lang="EN-US"}[为]{style="font-family:宋体"}[A1A1A1A1]{lang="EN-US"}[的客户端。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x306008822}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] static-bind prefix 2001:0410::/35 duid 00030001CA0006A400 iaid A1A1A1A1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1267624616}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_x1592779983}
:::

::: {#-1608111418 .myid}
[]{#_Toc404787198}[]{#_Toc370742285}[]{#struct_0_13981_19121_2124581299}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- temporary address range**

------------------------------------------------------------------------

[**[temporary address range]{lang="EN-US"}**]{#struct_0_13981_19121_1827838996}[命令用来配置地址池中动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[临时地址范围。]{style="font-family:宋体"}

[**[undo temporary address range]{lang="EN-US"}**]{#struct_0_13981_19121_804116407}[命令用来删除地址池中动态分配的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[临时地址范围。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1627163415}

[**[temporary address range]{lang="EN-US"}**[ *start-ipv6-address end-ipv6-address* \[ **preferred-lifetime** *preferred-lifetime* **valid-lifetime** *valid-lifetime* \]]{lang="EN-US"}]{#struct_0_13981_19121_x823422576}

[**[undo temporary address range]{lang="EN-US"}**]{#struct_0_13981_19121_304343699}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1169915949}

[[未配置地址池动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_526490032}[临时地址范围，不能分配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[临时地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124646835}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1091976810}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x579780419}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_812974752}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x401155895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x810338337}

[*[start-ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x726239465}[：动态分配范围的起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[临时地址。]{style="font-family:宋体"}

[*[end-ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x1118103006}[：动态分配范围的结束]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[临时地址。]{style="font-family:宋体"}

[**[preferred-lifetime]{lang="EN-US"}**[ *preferred-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_468839440}[：指定地址池分配的临时地址的首选生命期。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[为临时地址的首选生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[604800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）。]{style="font-family:宋体"}

[**[valid-lifetime]{lang="EN-US"}**[ *valid-lifetime*]{lang="EN-US"}]{#struct_0_13981_19121_2123663795}[：指定地址池分配的临时地址的有效生命期。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[为临时地址的有效生命期，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[2592000]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[天）。]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1945601387}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置]{lang="EN-US" style="font-family:宋体"}**[temporary address range]{lang="EN-US"}**]{#struct_0_13981_19121_1267906615}[命令时，地址池不会从]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**[或者]{lang="EN-US" style="font-family:宋体"}**[address range]{lang="EN-US"}**[命令配置的地址范围内分配临时地址。即此时不支持临时地址分配。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址池最多只能配置一个]{style="font-family:宋体"}]{#struct_0_13981_19121_x1901195704}[IPv6]{lang="EN-US"}[临时地址范围，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1144855473}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_367417982}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[动态分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[临时地址范围为]{style="font-family:宋体"}[3ffe:501:ffff:100::50]{lang="EN-US"}[到]{style="font-family:宋体"}[3ffe:501:ffff:100::60]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x288615696}

[\[Sysname\] ipv6 dhcp pool 1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] network 3ffe:501:ffff:100::/64]{lang="EN-US"}

[\[Sysname-dhcp6-pool-1\] temporary address range 3ffe:501:ffff:100::50 3ffe:501:ffff:100::60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1416917958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range]{lang="EN-US"}**]{#struct_0_13981_19121_2123729331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp pool]{lang="EN-US"}**]{#struct_0_13981_19121_382746804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_13981_19121_1601425598}
:::

::: {#1715388964 .myid}
[]{#_Toc404787199}[]{#struct_0_13981_19121_x778418942}

**DHCPv6 \-- DHCPv6服务器配置命令 \-- vpn-instance**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_13981_19121_x778091262}[命令用来指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器上的地址池所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_13981_19121_x778025726}[删除指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器上的地址池所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1459117933}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_13981_19121_x778156798}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_13981_19121_1046592916}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x777829118}

[[未指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x777763582}[服务器上的地址池所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_467040068}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x778353407}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1669171496}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x778287871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x778484479}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2042243855}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_13981_19121_x778418943}[：指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示地址池属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778091263}

[[当地址池绑定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_13981_19121_1869450493}[实例后，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器可以将网络划分成公网和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[私网。没有配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[属性的地址池被划分到公网，配置了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[属性的地址池被划分到相应的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[私网，这样，对于处于公网或]{style="font-family:宋体"}[VPN]{lang="EN-US"}[私网中的客户端，服务器都能够选择合适的地址池来为客户端分配租约并且记录该客户端的状态信息。]{style="font-family:宋体"}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x778025727}[客户端的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息可以从认证模块（如]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[）获取，也可以从]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器接收报文的接口配置的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息获取。如果以上两种方式都可获取]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息，以从认证模块获取的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778222335}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x504894703}[指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[编号为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x777829119}

[\[Sysname\] ipv6 dhcp pool 0]{lang="EN-US"}

[\[Sysname-dhcp6-pool-0\] vpn-instance abc]{lang="EN-US"}
:::

::: {#128801471 .myid}
[]{#_Toc404787201}[]{#_Toc370742287}[]{#struct_0_13981_19121_1459728829}[]{#_Toc267599414}[]{#_Toc189624866}[]{#_Toc177803168}

**DHCPv6 \-- DHCPv6中继配置命令 \-- display ipv6 dhcp relay server-address**

------------------------------------------------------------------------

[**[display ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_x319436406}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1316242477}

[**[display ipv6 dhcp relay server-address ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_942940579}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1248660694}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_2124188080}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x163066914}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x934093823}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1778624948}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_984396692}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_1660856099}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1673924206}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13981_19121_x1812658613}[：显示指定接口上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则显示所有接口上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_38540735}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_2124253616}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x538082065}[显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继上指定的所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay server-address]{lang="EN-US"}]{#struct_0_13981_19121_x1773614366}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Server address                             Outgoing Interface]{lang="EN-US"}

[ 2::3]{lang="EN-US"}

[ 3::4                                       GigabitEthernet1/0/3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[ Server address                             Outgoing Interface]{lang="EN-US"}

[ 2::3]{lang="EN-US"}

[ 3::4                                       GigabitEthernet1/0/3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x843678436}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay server-address interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_2124319152}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Server address                             Outgoing Interface]{lang="EN-US"}

[ 2::3]{lang="EN-US"}

[ 3::4                                       GigabitEthernet1/0/3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_620576810}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1358517706}[显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继上指定的所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay server-address]{lang="EN-US"}]{#struct_0_13981_19121_x496761497}

[Interface: Vlan-interface2]{lang="EN-US"}

[ Server address                             Outgoing Interface]{lang="EN-US"}

[ 2::3]{lang="EN-US"}

[ 3::4                                       Vlan-interface4     ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Vlan-interface3]{lang="EN-US"}

[ Server address                             Outgoing Interface]{lang="EN-US"}

[ 2::3]{lang="EN-US"}

[ 3::4                                       Vlan-interface4   ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1871032758}[显示接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay server-address interface vlan-interface 2]{lang="EN-US"}]{#struct_0_13981_19121_x364634560}

[Interface: Vlan-interface2]{lang="EN-US"}

[ Server address                             Outgoing Interface]{lang="EN-US"}

[ 2::3]{lang="EN-US"}

[ 3::4                                       Vlan-interface4     ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display ipv6 dhcp relay server-address]{lang="EN-US"}]{#struct_0_13981_19121_2124384688}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1943727007}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_1832932440}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_1639578926}

[[Interface]{lang="EN-US"}]{#struct_0_13981_19121_1791146321}

[[接口名]{style="font-family:宋体"}]{#struct_0_13981_19121_x1638317627}

[[Server address]{lang="EN-US"}]{#struct_0_13981_19121_1926595927}

[[接口上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1493489002}[服务器地址]{style="font-family:宋体"}

[[Outgoing Interface]{lang="EN-US"}]{#struct_0_13981_19121_2124450224}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x899602459}[报文的出接口，若未指定出接口，则表明报文将通过路由自动查找出接口]{style="font-family:宋体"}

[]{#_Toc267599415}[[ ]{lang="EN-US"}]{#_Toc189624867}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x228377292}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_1608420453}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp select]{lang="EN-US"}**]{#struct_0_13981_19121_x332782750}

::: {#-987753910 .myid}
[]{#_Toc404787202}[]{#_Toc370742288}[]{#struct_0_13981_19121_x801715223}

**DHCPv6 \-- DHCPv6中继配置命令 \-- display ipv6 dhcp relay statistics**

------------------------------------------------------------------------

[**[display ipv6 dhcp relay statistics]{lang="EN-US"}**]{#struct_0_13981_19121_1882405006}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124515760}

[**[display ipv6 dhcp relay statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1679046221}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x337342886}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_116706160}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1559545959}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_323411297}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1454836297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_125867624}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_1871472937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124581296}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13981_19121_1827380244}[：显示指定接口上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则显示所有接口上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_890254335}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x5388146}[显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay statistics]{lang="EN-US"}]{#struct_0_13981_19121_2124646832}

[Packets dropped               :  4]{lang="EN-US"}

[Packets received              :  14]{lang="EN-US"}

[    Solicit                   :  0]{lang="EN-US"}

[    Request                   :  0]{lang="EN-US"}

[    Confirm                   :  0]{lang="EN-US"}

[    Renew                     :  0]{lang="EN-US"}

[    Rebind                    :  0]{lang="EN-US"}

[    Release                   :  0]{lang="EN-US"}

[    Decline                   :  0]{lang="EN-US"}

[    Information-request       :  7]{lang="EN-US"}

[    Relay-forward             :  0]{lang="EN-US"}

[    Relay-reply               :  7]{lang="EN-US"}

[Packets sent                  :  14]{lang="EN-US"}

[    Advertise                 :  0]{lang="EN-US"}

[    Reconfigure               :  0]{lang="EN-US"}

[    Reply                     :  7]{lang="EN-US"}

[    Relay-forward             :  7]{lang="EN-US"}

[    Relay-reply               :  0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_1092042346}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_834695035}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[DHCPV6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_2123663792}

[Packets dropped               :  4]{lang="EN-US"}

[Packets received              :  16]{lang="EN-US"}

[    Solicit                   :  0]{lang="EN-US"}

[    Request                   :  0]{lang="EN-US"}

[    Confirm                   :  0]{lang="EN-US"}

[    Renew                     :  0]{lang="EN-US"}

[    Rebind                    :  0]{lang="EN-US"}

[    Release                   :  0]{lang="EN-US"}

[    Decline                   :  0]{lang="EN-US"}

[    Information-request       :  8]{lang="EN-US"}

[    Relay-forward             :  0]{lang="EN-US"}

[    Relay-reply               :  8]{lang="EN-US"}

[Packets sent                  :  16]{lang="EN-US"}

[    Advertise                 :  0]{lang="EN-US"}

[    Reconfigure               :  0]{lang="EN-US"}

[    Reply                     :  8]{lang="EN-US"}

[    Relay-forward             :  8]{lang="EN-US"}

[    Relay-reply               :  0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_1945404779}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1273458915}[显示接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上]{style="font-family:宋体"}[DHCPV6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp relay statistics interface vlan-interface 2]{lang="EN-US"}]{#struct_0_13981_19121_2123729328}

[Packets dropped               :  4]{lang="EN-US"}

[Packets received              :  16]{lang="EN-US"}

[    Solicit                   :  0]{lang="EN-US"}

[    Request                   :  0]{lang="EN-US"}

[    Confirm                   :  0]{lang="EN-US"}

[    Renew                     :  0]{lang="EN-US"}

[    Rebind                    :  0]{lang="EN-US"}

[    Release                   :  0]{lang="EN-US"}

[    Decline                   :  0]{lang="EN-US"}

[    Information-request       :  8]{lang="EN-US"}

[    Relay-forward             :  0]{lang="EN-US"}

[    Relay-reply               :  8]{lang="EN-US"}

[Packets sent                  :  16]{lang="EN-US"}

[    Advertise                 :  0]{lang="EN-US"}

[    Reconfigure               :  0]{lang="EN-US"}

[    Reply                     :  8]{lang="EN-US"}

[    Relay-forward             :  8]{lang="EN-US"}

[    Relay-reply               :  0]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display ipv6 dhcp relay statistics]{lang="EN-US"}]{#struct_0_13981_19121_382156981}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1945444733}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_1997620535}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_2086557800}

[[Packets dropped]{lang="EN-US"}]{#struct_0_13981_19121_868796645}

[[丢弃的报文总数]{style="font-family:宋体"}]{#struct_0_13981_19121_x719094948}

[[Packets received]{lang="EN-US"}]{#struct_0_13981_19121_x462314464}

[[接收到的报文总数]{style="font-family:宋体"}]{#struct_0_13981_19121_2124188081}

[[Solicit]{lang="EN-US"}]{#struct_0_13981_19121_x163001378}

[[接收到的]{style="font-family:宋体"}[Solicit]{lang="EN-US"}]{#struct_0_13981_19121_x543058696}[报文数目]{style="font-family:宋体"}

[[Request]{lang="EN-US"}]{#struct_0_13981_19121_187675962}

[[接收到的]{style="font-family:宋体"}[Request]{lang="EN-US"}]{#struct_0_13981_19121_x731112651}[报文数目]{style="font-family:宋体"}

[[Confirm]{lang="EN-US"}]{#struct_0_13981_19121_2124253617}

[[接收到的]{style="font-family:宋体"}[Confirm]{lang="EN-US"}]{#struct_0_13981_19121_x538147601}[报文数目]{style="font-family:宋体"}

[[Renew]{lang="EN-US"}]{#struct_0_13981_19121_647332926}

[[接收到的]{style="font-family:宋体"}[Renew]{lang="EN-US"}]{#struct_0_13981_19121_1497890162}[报文数目]{style="font-family:宋体"}

[[Rebind]{lang="EN-US"}]{#struct_0_13981_19121_x2038212693}

[[接收到的]{style="font-family:宋体"}[Rebind]{lang="EN-US"}]{#struct_0_13981_19121_286611765}[报文数目]{style="font-family:宋体"}

[[Release]{lang="EN-US"}]{#struct_0_13981_19121_2124319153}

[[接收到的]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_13981_19121_620511274}[报文数目]{style="font-family:宋体"}

[[Decline]{lang="EN-US"}]{#struct_0_13981_19121_x1724048174}

[[接收到的]{style="font-family:宋体"}[Decline]{lang="EN-US"}]{#struct_0_13981_19121_578584519}[报文数目]{style="font-family:宋体"}

[[Information-request]{lang="EN-US"}]{#struct_0_13981_19121_1099410437}

[[接收到的]{style="font-family:宋体"}[Information-request]{lang="EN-US"}]{#struct_0_13981_19121_2124384689}[报文数目]{style="font-family:宋体"}

[[Relay-forward]{lang="EN-US"}]{#struct_0_13981_19121_1832997976}

[[接收到的]{style="font-family:宋体"}[Relay-forward]{lang="EN-US"}]{#struct_0_13981_19121_x1819429338}[报文数目]{style="font-family:宋体"}

[[Relay-reply]{lang="EN-US"}]{#struct_0_13981_19121_x786405167}

[[接收到的]{style="font-family:宋体"}[Relay-reply]{lang="EN-US"}]{#struct_0_13981_19121_977243126}[报文数目]{style="font-family:宋体"}

[[Packets sent]{lang="EN-US"}]{#struct_0_13981_19121_2124450225}

[[发送的报文总数]{style="font-family:宋体"}]{#struct_0_13981_19121_x899667995}

[[Advertise]{lang="EN-US"}]{#struct_0_13981_19121_x687957239}

[[发送的]{style="font-family:宋体"}[Advertise]{lang="EN-US"}]{#struct_0_13981_19121_x1906531552}[报文数目]{style="font-family:宋体"}

[[Reconfigure]{lang="EN-US"}]{#struct_0_13981_19121_2124515761}

[[发送的]{style="font-family:宋体"}[Reconfigure]{lang="EN-US"}]{#struct_0_13981_19121_x1679111757}[报文数目]{style="font-family:宋体"}

[[Reply]{lang="EN-US"}]{#struct_0_13981_19121_x44887910}

[[发送的]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_13981_19121_1137978181}[报文数目]{style="font-family:宋体"}

[[Relay-forward]{lang="EN-US"}]{#struct_0_13981_19121_2124581297}

[[发送的]{style="font-family:宋体"}[Relay-forward]{lang="EN-US"}]{#struct_0_13981_19121_1827445780}[报文数目]{style="font-family:宋体"}

[[Relay-reply]{lang="EN-US"}]{#struct_0_13981_19121_x1833904749}

[[发送的]{style="font-family:宋体"}[Relay-reply]{lang="EN-US"}]{#struct_0_13981_19121_x1011088530}[报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x336798235}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp relay statistics]{lang="EN-US"}**]{#struct_0_13981_19121_2124646833}

::: {#-452439128 .myid}
[]{#_Toc404787203}[]{#struct_0_13981_19121_x777829120}

**DHCPv6 \-- DHCPv6中继配置命令 \-- gateway-list**

------------------------------------------------------------------------

[**[gateway-list]{lang="EN-US"}**]{#struct_0_13981_19121_x777763584}[命令用来指定匹配该地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端所在的网段的地址。]{style="font-family:宋体"}

[**[undo gateway-list]{lang="EN-US"}**]{#struct_0_13981_19121_466908996}[命令用来删除指定的匹配该地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端所在的网段的地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778353401}

[**[gateway-list ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_13981_19121_x778484473}

[**[undo gateway-list ]{lang="EN-US"}**[\[ *ipv6-address*&\<1-8\> \]]{lang="EN-US"}]{#struct_0_13981_19121_x2041588495}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778418937}

[[未指定匹配该地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x778091257}[客户端所在的网段的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1869712636}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x778025721}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778222329}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x504632560}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x778156793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x777829113}

[*[ipv6-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_13981_19121_x778353402}[：匹配该地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端所在的网段]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778287866}

[[一台]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1313978147}[中继的一个接口下可能连接不同类型的用户，当]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继转发]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端请求报文给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器时，不能再以中继接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为选择地址池的依据。为了解决这个问题，需要使用]{style="font-family:宋体"}**[gateway-list]{lang="EN-US"}**[命令指定某个类型用户所在的网段，并将该地址添加到转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文字段中，为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器选择地址池提供依据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x778484474}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x778418938}[指定匹配该地址池]{style="font-family:宋体"}[p1]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端所在的网段的地址为]{style="font-family:宋体"}[10::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x778091258}

[\[Sysname\] ipv6 dhcp pool p1]{lang="EN-US"}

[\[Sysname-dhcp6-pool-p1\] gateway-list 10::1]{lang="EN-US"}
:::

::: {#1113250697 .myid}
[]{#_Toc404787204}[]{#struct_0_13981_19121_x778222330}

**DHCPv6 \-- DHCPv6中继配置命令 \-- ipv6 dhcp relay gateway**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**[ **dhcp relay gateway**]{lang="EN-US"}]{#struct_0_13981_19121_x778156794}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端分配的网关地址。]{style="font-family:宋体"}

[**[undo ipv6 dhcp relay gateway]{lang="EN-US"}**]{#struct_0_13981_19121_1046855060}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x777829114}

[**[ipv6]{lang="EN-US"}**[ **dhcp relay gateway** *ipv6-address*]{lang="EN-US"}]{#struct_0_13981_19121_787730536}

[**[undo ipv6 dhcp relay gateway]{lang="EN-US"}**]{#struct_0_13981_19121_x1126795021}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_787796072}

[[分配接口下第一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_787599464}[地址作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的网关地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_787665000}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1206983259}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_787992680}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_788058216}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_787861608}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1007146485}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_787927144}[：指定作为客户端网关的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_788254824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口视图下配置此命令后，中继会使用此命令配置的地址作为客户端的网关地址。]{style="font-family:宋体"}]{#struct_0_13981_19121_788320360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行此命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_13981_19121_787730535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的网关地址必须属于该命令行所在的接口。]{style="font-family:宋体"}]{#struct_0_13981_19121_x1126795018}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_787796071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_787599463}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_926805721}[在接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[上配置为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端分配的网关地址为]{style="font-family:宋体"}[10::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_787664999}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp relay gateway 10::1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_787992679}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_788058215}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端分配的网关地址为]{style="font-family:宋体"}[10::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_787861607}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 dhcp relay gateway 10::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_787927143}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gateway-list]{lang="EN-US"}**]{#struct_0_13981_19121_788254823}
:::

::: {#-300080615 .myid}
[]{#_Toc404787205}[]{#struct_0_13981_19121_788320359}

**DHCPv6 \-- DHCPv6中继配置命令 \-- ipv6 dhcp relay interface-id**

------------------------------------------------------------------------

[**[ipv6 dhcp relay interface-id]{lang="EN-US"}**]{#struct_0_13981_19121_787796070}[命令用来配置]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[中继支持的]{style="font-family:宋体"}[interface-id]{lang="EN-US"}[选项填充模式。]{style="font-family:宋体"}

[**[undo ipv6 dhcp relay interface-id]{lang="EN-US"}**]{#struct_0_13981_19121_787992678}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_788058214}

[**[ipv6 dhcp relay interface-id ]{lang="EN-US"}**[{ **bas** \| **interface** }]{lang="EN-US"}]{#struct_0_13981_19121_787927142}

[**[undo ipv6 dhcp relay interface-id]{lang="EN-US"}**]{#struct_0_13981_19121_x908810586}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_788320358}

[[interface-id]{lang="EN-US"}]{#struct_0_13981_19121_787730533}[选项的填充模式为接口索引信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_787599461}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13981_19121_787664997}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_788058213}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_787861605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_788254821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x735123093}

[**[bas]{lang="EN-US"}**]{#struct_0_13981_19121_x412723551}[：表示配置]{style="font-family:宋体"}[interface-id]{lang="EN-US"}[选项填充模式为]{style="font-family:宋体"}[BAS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_13981_19121_x734926485}[：表示配置]{style="font-family:宋体"}[interface-id]{lang="EN-US"}[选项填充模式为接口名模式。填充内容为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式的接口名和接口所在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_788320357}

[[执行]{style="font-family:宋体"}**[ipv6 dhcp relay interface-id]{lang="EN-US"}**]{#struct_0_13981_19121_787796076}[命令之前，如果没有配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式，本命令不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_385035833}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_384446008}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继支持的]{style="font-family:宋体"}[interface-id]{lang="EN-US"}[选项填充模式为]{style="font-family:宋体"}[BAS]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_384314936}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp relay interface-id bas]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x734992021}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继支持的]{style="font-family:宋体"}[interface-id]{lang="EN-US"}[选项填充模式为接口名模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x734271125}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp relay interface-id interface]{lang="EN-US"}
:::

::: {#687511743 .myid}
[]{#_Toc404787206}[]{#_Toc370742289}[]{#struct_0_13981_19121_1092107882}[]{#_Toc267599416}[]{#_Toc189624868}[]{#_Toc177803167}[]{#_Toc379719101}[]{#_Toc379719182}[]{#_Toc379964825}[]{#_Toc379994536}

**DHCPv6 \-- DHCPv6中继配置命令 \-- ipv6 dhcp relay server-address**

------------------------------------------------------------------------

[**[ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_484953377}[命令用来在]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[中继上指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的地址。]{style="font-family:宋体"}

[**[undo ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_416856672}[命令用来删除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继上指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_176814736}

[**[ipv6 dhcp relay server-address ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1057127441}

[**[undo ipv6 dhcp relay server-address ]{lang="EN-US"}**[\[ *ipv6-address* \[ **interface** *interface-type interface-number* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_984643570}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x216333527}

[[未在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_632976493}[中继上指定任何]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_2123663793}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1945470315}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1461697711}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1881172310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1144093320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1580544195}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x1262270984}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。如果]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址是组播地址或者链路本地地址，则必须指定报文的出接口。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13981_19121_x1264226926}[：指定报文的出接口。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果指定了本参数，则通过指定的接口将]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端发送的请求报文转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器；如果没有指定本参数，则根据路由查找报文的出接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1851843817}

[[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_2123729329}[中继模式的接口接收到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发来的报文后，将其封装在]{style="font-family:宋体"}[Relay-forward]{lang="EN-US"}[报文中，并发送给指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器，由]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器为客户端分配地址和网络配置参数。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13981_19121_382222517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过多次执行]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_x1618752184}[命令可以指定多个]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器，一个接口下最多可以指定]{lang="EN-US" style="font-family:宋体"}[8]{lang="EN-US"}[个]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器。]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继从接口接收到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发送的报文后，将其转发给该接口上指定的所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_13981_19121_307845355}[DHCPv6]{lang="EN-US"}[服务器地址为链路本地地址或组播地址，则必须指定出接口，否则报文可能会无法到达服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_1311220135}[命令时，如果指定了]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[参数，则删除指定的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址；如果没有指定任何参数，则删除接口上的所有]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议不要在一个接口上同时配置]{style="font-family:宋体"}]{#struct_0_13981_19121_x1153170076}[DHCPv6]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_626132421}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_1957955599}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1801069332}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式，并指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[2001:1::3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_2124188078}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp select relay]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp relay server-address 2001:1::3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x162542641}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x562558369}[配置接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继模式，并指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[2001:1::3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_746552402}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 dhcp select relay]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 dhcp relay server-address 2001:1::3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1959791633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp relay server-address]{lang="EN-US"}**]{#struct_0_13981_19121_x426856424}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp selec]{lang="EN-US"}**[t]{lang="EN-US"}]{#struct_0_13981_19121_x701687640}
:::

::: {#1631374782 .myid}
[]{#_Toc404787207}[]{#struct_0_13981_19121_384577080}

**DHCPv6 \-- DHCPv6中继配置命令 \-- remote-server**

------------------------------------------------------------------------

[**[remote-server]{lang="EN-US"}**]{#struct_0_13981_19121_384970296}[命令指定中继地址池对应的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[**[undo remote-server]{lang="EN-US"}**]{#struct_0_13981_19121_384446007}[命令用来删除为中继地址池指定的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_384314935}

[**[remote-server]{lang="EN-US"}**[ *ipv6-address* \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_384642615}

[**[undo remote-server ]{lang="EN-US"}**[\[ *ipv6-address* \[ **interface** *interface-type interface-number* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_x962232263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_385035831}

[[未指定中继地址池的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_384511542}[服务器的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_384380470}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_384708150}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_384577078}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_384642614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_385035830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_384511549}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_384314941}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type inteface-number*]{lang="EN-US"}]{#struct_0_13981_19121_384446012}[：指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继将报文转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的出接口，]{style="font-family:宋体"}*[interface-type inteface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果不指定本参数，则]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继根据路由表查找报文出接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_384314940}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在一个地址池中，最多可以通过配置]{style="font-family:宋体"}]{#struct_0_13981_19121_384380476}**[remote-server]{lang="EN-US"}**[命令来指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_13981_19121_384708156}**[undo remote-server]{lang="EN-US"}**[命令时，如果没有指定任何参数，则删除所有配置的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置的目的地址是链路本地地址时，必须指定]{style="font-family:宋体"}]{#struct_0_13981_19121_384577084}[DHCPv6]{lang="EN-US"}[中继]{style="font-family:宋体"}[将报文转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器]{style="font-family:宋体"}[的出接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_384970300}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_385035836}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为中继配置的服务器地址为]{style="font-family:宋体"}[10::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1950595486}

[\[Sysname\] ipv6 dhcp pool 0]{lang="EN-US"}

[\[Sysname-dhcp6-pool-0\] remote-server 10::1]{lang="EN-US"}
:::

::: {#1201339196 .myid}
[]{#_Toc404787208}[]{#_Toc370742290}[]{#struct_0_13981_19121_2124253614}[]{#_Toc267599417}[]{#_Toc189624870}[]{#_Toc379717256}[]{#_Toc379719104}[]{#_Toc379719185}[]{#_Toc379964828}[]{#_Toc379994539}[]{#_Toc233435404}[]{#_Toc233441834}[]{#_Toc233519950}[]{#_Toc233520717}[]{#_Toc233520944}[]{#_Toc233435405}[]{#_Toc233441835}[]{#_Toc233519951}[]{#_Toc233520718}[]{#_Toc233520945}[]{#_Toc233435406}[]{#_Toc233441836}[]{#_Toc233519952}[]{#_Toc233520719}[]{#_Toc233520946}[]{#_Toc233435407}[]{#_Toc233441837}[]{#_Toc233519953}[]{#_Toc233520720}[]{#_Toc233520947}[]{#_Toc233435408}[]{#_Toc233441838}[]{#_Toc233519954}[]{#_Toc233520721}[]{#_Toc233520948}[]{#_Toc233435409}[]{#_Toc233441839}[]{#_Toc233519955}[]{#_Toc233520722}[]{#_Toc233520949}[]{#_Toc233435410}[]{#_Toc233441840}[]{#_Toc233519956}[]{#_Toc233520723}[]{#_Toc233520950}[]{#_Toc233435412}[]{#_Toc233441842}[]{#_Toc233519958}[]{#_Toc233520725}[]{#_Toc233520952}[]{#_Toc233435413}[]{#_Toc233441843}[]{#_Toc233519959}[]{#_Toc233520726}[]{#_Toc233520953}[]{#_Toc233435414}[]{#_Toc233441844}[]{#_Toc233519960}[]{#_Toc233520727}[]{#_Toc233520954}[]{#_Toc233435415}[]{#_Toc233441845}[]{#_Toc233519961}[]{#_Toc233520728}[]{#_Toc233520955}[]{#_Toc233435416}[]{#_Toc233441846}[]{#_Toc233519962}[]{#_Toc233520729}[]{#_Toc233520956}[]{#_Toc233435417}[]{#_Toc233441847}[]{#_Toc233519963}[]{#_Toc233520730}[]{#_Toc233520957}[]{#_Toc233435418}[]{#_Toc233441848}[]{#_Toc233519964}[]{#_Toc233520731}[]{#_Toc233520958}[]{#_Toc233435419}[]{#_Toc233441849}[]{#_Toc233519965}[]{#_Toc233520732}[]{#_Toc233520959}

**DHCPv6 \-- DHCPv6中继配置命令 \-- reset ipv6 dhcp relay statistics**

------------------------------------------------------------------------

[**[reset ipv6 dhcp relay statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x538213137}[命令用来清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2146609526}

[**[reset ipv6 dhcp relay statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_2000088017}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x206455742}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_54540397}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_666584333}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1439798556}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x389891689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124319150}

[**[interface]{lang="EN-US"}**[ *interface-type interfac*e-*number*]{lang="EN-US"}]{#struct_0_13981_19121_620445738}[：清除指定接口上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继相关报文统计信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则清除所有接口上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1390764986}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1804610224}[清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp relay statistics]{lang="EN-US"}]{#struct_0_13981_19121_109323174}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x325983144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp relay statistics]{lang="EN-US"}**]{#struct_0_13981_19121_1675255690}
:::

::: {#-2100120345 .myid}
[]{#_Toc404787210}[]{#_Toc370742292}[]{#struct_0_13981_19121_1675281263}[]{#_Toc349031201}[]{#_Toc348965449}[]{#_Toc348956741}[]{#_Toc348890604}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- display ipv6 dhcp client**

------------------------------------------------------------------------

[**[display ipv6 dhcp client]{lang="EN-US"}**]{#struct_0_13981_19121_x1567178577}[命令用来显示]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x404966499}

[**[display ipv6 dhcp client ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_x308380162}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1470041849}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1226123573}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1757965931}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x308183554}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x668500927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x846388954}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x308249090}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x697759190}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_13981_19121_x945287973}[：显示指定接口的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则显示所有]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_179816862}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x308052482}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1421867200}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp client interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_x308118018}

[GigabitEthernet1/0/1:]{lang="EN-US"}

[  Type: Stateful client requesting address and prefix]{lang="EN-US"}

[    State: OPEN]{lang="EN-US"}

[    Client DUID: 0003000100e002000000]{lang="EN-US"}

[    Preferred server]{lang="EN-US"}

[      Reachable via address: FE80::2E0:1FF:FE00:18]{lang="EN-US"}

[      Server DUID: 0003000100e001000000]{lang="EN-US"}

[    IA_NA: IAID 0x00000642, T1 50 sec, T2 80 sec]{lang="EN-US"}

[      Address: 1:1::2/128]{lang="EN-US"}

[        Preferred lifetime 100 sec, valid lifetime 200 sec]{lang="EN-US"}

[        Will expire on Feb 4 2014 at 15:37:20(288 seconds left]{lang="EN-US"}[）]{style="font-family:
宋体"}

[    IA_PD: IAID 0x00000642, T1 50 sec, T2 80 sec]{lang="EN-US"}

[      Prefix: 12:34::/48]{lang="EN-US"}

[        Preferred lifetime 100 sec, valid lifetime 200 sec]{lang="EN-US"}

[        Will expire on Mar 27 2014 at 08:13:24 (199 seconds left)]{lang="EN-US"}

[    DNS server addresses:]{lang="EN-US"}

[      2:2::3]{lang="EN-US"}

[    Domain name:]{lang="EN-US"}

[      aaa.com]{lang="EN-US"}

[    SIP server addresses:]{lang="EN-US"}

[      2:2::4]{lang="EN-US"}

[    SIP server domain names:]{lang="EN-US"}

[      bbb.com]{lang="EN-US"}

[    Options:]{lang="EN-US"}

[      Code: 88]{lang="EN-US"}

[        Length: 3 bytes]{lang="EN-US"}

[        Hex: AABBCC]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_853841336}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x308576771}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp client interface vlan-interface 2]{lang="EN-US"}]{#struct_0_13981_19121_x308642307}

[Vlan-interface2:]{lang="EN-US"}

[  Type: Stateful client requesting address and prefix]{lang="EN-US"}

[    State: OPEN]{lang="EN-US"}

[    Client DUID: 0003000100e002000000]{lang="EN-US"}

[    Preferred server:]{lang="EN-US"}

[      Reachable via address: FE80::2E0:1FF:FE00:18]{lang="EN-US"}

[      Server DUID: 0003000100e001000000]{lang="EN-US"}

[    IA_NA: IAID 0x00000642, T1 50 sec, T2 80 sec]{lang="EN-US"}

[      Address: 1:1::2/128]{lang="EN-US"}

[        Preferred lifetime 100 sec, valid lifetime 200 sec]{lang="EN-US"}

[        Will expire on Feb 4 2014 at 15:37:20(288 seconds left]{lang="EN-US"}[）]{style="font-family:
宋体"}

[    IA_PD: IAID 0x00000642, T1 50 sec, T2 80 sec]{lang="EN-US"}

[      Prefix: 12:34::/48]{lang="EN-US"}

[        Preferred lifetime 100 sec, valid lifetime 200 sec]{lang="EN-US"}

[        Will expire on Mar 27 2014 at 08:13:24 (199 seconds left)]{lang="EN-US"}

[    DNS server addresses:]{lang="EN-US"}

[      2:2::3]{lang="EN-US"}

[    Domain name:]{lang="EN-US"}

[      aaa.com]{lang="EN-US"}

[    SIP server addresses:]{lang="EN-US"}

[      2:2::4]{lang="EN-US"}

[    SIP server domain names:]{lang="EN-US"}

[      bbb.com]{lang="EN-US"}

[    Options:]{lang="EN-US"}

[      Code: 88]{lang="EN-US"}

[        Length: 3 bytes]{lang="EN-US"}

[        Hex: AABBCC]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display ipv6 dhcp client]{lang="EN-US"}]{#struct_0_13981_19121_1305544814}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1934347140}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_1226241460}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x308445699}

[[Type]{lang="EN-US"}]{#struct_0_13981_19121_x308511235}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1451661859}[客户端类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stateful client request]{lang="EN-US"}]{#struct_0_13981_19121_x308314627}[ing]{lang="EN-US"}[ address]{lang="EN-US"}[：表示获取]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stateful client request]{lang="EN-US"}]{#struct_0_13981_19121_1675215727}[ing]{lang="EN-US"}[ prefix]{lang="EN-US"}[：表示获取]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stateful client requesting address and prefix]{lang="EN-US"}]{#struct_0_13981_19121_x355434328}[：表示同时获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stateless client]{lang="EN-US"}]{#struct_0_13981_19121_x308380163}[：]{lang="EN-US" style="font-family:
  宋体"}[表示]{style="font-family:宋体"}[无状态]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13981_19121_x1469976313}

[[客户端的当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_13981_19121_x308183555}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_13981_19121_x668435391}[：闲置状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SOLICIT]{lang="EN-US"}]{#struct_0_13981_19121_x308249091}[：正在定位服务器]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST]{lang="EN-US"}]{#struct_0_13981_19121_x697693654}[：正在申请租约]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OPEN]{lang="EN-US"}]{#struct_0_13981_19121_x308052483}[：申请成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RENEW]{lang="EN-US"}]{#struct_0_13981_19121_x308118019}[：正在申请更新租约（租约]{style="font-family:宋体"}[T1]{lang="EN-US"}[时间之后，]{style="font-family:宋体"}[T2]{lang="EN-US"}[时间之前）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REBIND]{lang="EN-US"}]{#struct_0_13981_19121_853775800}[：正在申请更新租约（租约]{style="font-family:宋体"}[T2]{lang="EN-US"}[时间之后，过期之前）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RELEASE]{lang="EN-US"}]{#struct_0_13981_19121_1613737535}[：]{style="font-family:宋体"}[正在申请释放租约]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DECLINE]{lang="EN-US"}]{#struct_0_13981_19121_x1755350693}[：检测到地址冲突，正在申请禁用该地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INFO-REQUESTING]{lang="EN-US"}]{#struct_0_13981_19121_1613671999}[：正在无状态获取配置信息]{lang="EN-US" style="font-family:
  宋体"}

[[Client DUID]{lang="EN-US"}]{#struct_0_13981_19121_x909340592}

[[客户端的]{style="font-family:宋体"}[DUID]{lang="EN-US"}]{#struct_0_13981_19121_1613868607}

[[Preferred server]{lang="EN-US"}]{#struct_0_13981_19121_2133698804}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1613803071}[客户端选用的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的信息]{style="font-family:宋体"}

[[Reachable via address]{lang="EN-US"}]{#struct_0_13981_19121_1613999679}

[[可达地址，服务器或中继的链路本地地址]{style="font-family:宋体"}]{#struct_0_13981_19121_x625920961}

[[Server DUID]{lang="EN-US"}]{#struct_0_13981_19121_1613934143}

[[服务器的]{style="font-family:宋体"}[DUID]{lang="EN-US"}]{#struct_0_13981_19121_1371526765}

[[IA_NA]{lang="EN-US"}]{#struct_0_13981_19121_x355434329}

[[申请到的]{style="font-family:宋体"}[IA_NA]{lang="EN-US"}]{#struct_0_13981_19121_1163730975}[信息]{style="font-family:宋体"}

[[IA_PD]{lang="EN-US"}]{#struct_0_13981_19121_x355434330}

[[申请到的]{style="font-family:宋体"}[IA_PD]{lang="EN-US"}]{#struct_0_13981_19121_1163272222}[信息]{style="font-family:宋体"}

[[IAID]{lang="EN-US"}]{#struct_0_13981_19121_219233602}

[[IA]{lang="EN-US"}]{#struct_0_13981_19121_237581505}[标识符]{style="font-family:宋体"}

[[T1]{lang="EN-US"}]{#struct_0_13981_19121_469992788}

[[租约的]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_13981_19121_x355434323}[生命期，单位为秒]{style="font-family:宋体"}

[[T2]{lang="EN-US"}]{#struct_0_13981_19121_1163337759}

[[租约的]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_13981_19121_x587037655}[生命期，单位为秒]{style="font-family:宋体"}

[[Address]{lang="EN-US"}]{#struct_0_13981_19121_1614130751}

[[申请到的地址，只有客户端类型为]{style="font-family:宋体"}[Stateful client requesting address]{lang="EN-US"}]{#struct_0_13981_19121_1614065215}[时，显示该信息]{style="font-family:宋体"}

[[Prefix]{lang="EN-US"}]{#struct_0_13981_19121_93414134}

[[申请到的前缀，只有客户端类型为]{style="font-family:宋体"}[Stateful client requesting prefix]{lang="EN-US"}]{#struct_0_13981_19121_1614261823}[时，显示该信息]{style="font-family:宋体"}

[[Preferred lifetime]{lang="EN-US"}]{#struct_0_13981_19121_915378377}

[[租约的首选生命期，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_1614196287}

[[valid lifetime]{lang="EN-US"}]{#struct_0_13981_19121_1628761651}

[[租约的有效生命期，单位为秒]{style="font-family:宋体"}]{#struct_0_13981_19121_1613737534}

[[Will expire on Feb 4 2014 at 15:37:20(288 seconds left)]{lang="EN-US"}]{#struct_0_13981_19121_1613803070}

[[将在]{style="font-family:宋体"}[2014]{lang="EN-US"}]{#struct_0_13981_19121_1613999678}[年]{style="font-family:宋体"}[2]{lang="EN-US"}[月]{style="font-family:宋体"}[4]{lang="EN-US"}[日]{style="font-family:宋体"}[15]{lang="EN-US"}[点]{style="font-family:宋体"}[37]{lang="EN-US"}[分]{style="font-family:宋体"}[20]{lang="EN-US"}[秒过期（还有]{style="font-family:宋体"}[288]{lang="EN-US"}[秒）。如果租约过期时间在]{style="font-family:宋体"}[2100]{lang="EN-US"}[年以后，则显示为]{style="font-family:宋体"}[Will expire after 2100]{lang="EN-US"}

[[DNS server addresses]{lang="EN-US"}]{#struct_0_13981_19121_x625986497}

[[申请到的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_13981_19121_1613934142}[服务器地址]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_13981_19121_1371461229}

[[申请到的域名后缀]{style="font-family:宋体"}]{#struct_0_13981_19121_1614130750}

[[SIP server addresses]{lang="EN-US"}]{#struct_0_13981_19121_1614065214}

[[申请到的]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_13981_19121_93479670}[服务器地址]{style="font-family:宋体"}

[[SIP server domain names]{lang="EN-US"}]{#struct_0_13981_19121_1614261822}

[[申请到的]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_13981_19121_1614196286}[服务器域名]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_13981_19121_1628696115}

[[申请到的自定义选项]{style="font-family:宋体"}]{#struct_0_13981_19121_1613737533}

[[Code]{lang="EN-US"}]{#struct_0_13981_19121_1613671997}

[[自定义选项编码]{style="font-family:宋体"}]{#struct_0_13981_19121_x908947376}

[[Length]{lang="EN-US"}]{#struct_0_13981_19121_1613868605}

[[自定义选项长度，单位为字节]{style="font-family:宋体"}]{#struct_0_13981_19121_2133829876}

[[Hex]{lang="EN-US"}]{#struct_0_13981_19121_1613803069}

[[自定义选项内容，以十六进制字符串表示]{style="font-family:宋体"}]{#struct_0_13981_19121_1613999677}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x625789889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 address dhcp-alloc]{lang="EN-US"}**]{#struct_0_13981_19121_1595153141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 ]{lang="EN-US"}[dhcp client pd]{lang="EN-US"}**]{#struct_0_13981_19121_1613934141}

::: {#390794249 .myid}
[]{#_Toc404787211}[]{#_Toc370742293}[]{#struct_0_13981_19121_1371395693}[]{#_Toc349031202}[]{#_Toc348965450}[]{#_Toc348956742}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- display ipv6 dhcp client statistics**

------------------------------------------------------------------------

[**[display ipv6 dhcp client statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x464350476}[命令用来显示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x371187478}

[**[display ipv6 dhcp client statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_1614130749}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x706280183}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1976037559}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_575241233}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1614065213}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_93020918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_508135856}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_1614261821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_915509449}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13981_19121_x279875532}[：显示指定接口上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则显示所有]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1558617899}

[[路由应用]{style="font-family:宋体"}]{#struct_0_13981_19121_1614196285}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1628892723}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp client statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_1613737532}

[Interface                     :  GigabitEthernet1/0/1]{lang="EN-US"}

[Packets received              :  1]{lang="EN-US"}

[         Reply                :  1]{lang="EN-US"}

[         Advertise            :  0]{lang="EN-US"}

[         Reconfigure         :   0]{lang="EN-US"}

[         Invalid              :  0]{lang="EN-US"}

[Packets sent                  :  5]{lang="EN-US"}

[         Solicit              :  0]{lang="EN-US"}

[         Request              :  0]{lang="EN-US"}

[         Renew                :  0]{lang="EN-US"}

[         Rebind               :  0]{lang="EN-US"}

[         Information-request  :  5]{lang="EN-US"}

[         Release              :  0]{lang="EN-US"}

[         Decline              :  0 ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1755547301}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1141419324}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp client statistics interface vlan-interface 2]{lang="EN-US"}]{#struct_0_13981_19121_1613671996}

[Interface                    :  Vlan-interface2]{lang="EN-US"}

[Packets received             :  1]{lang="EN-US"}

[         Reply               :  1]{lang="EN-US"}

[         Advertise           :  0]{lang="EN-US"}

[         Reconfigure         :  0]{lang="EN-US"}

[         Invalid             :  0]{lang="EN-US"}

[Packets sent                 :  5]{lang="EN-US"}

[         Solicit             :  0]{lang="EN-US"}

[         Request             :  0]{lang="EN-US"}

[         Renew               :  0]{lang="EN-US"}

[         Rebind              :  0]{lang="EN-US"}

[         Information-request :  5]{lang="EN-US"}

[         Release             :  0]{lang="EN-US"}

[         Decline             :  0 ]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display ipv6 dhcp client statistics]{lang="EN-US"}]{#struct_0_13981_19121_x909012912}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x564051080}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_1613868604}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_2133895412}

[[Interface]{lang="EN-US"}]{#struct_0_13981_19121_1613803068}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1785898577}[客户端所在的接口]{style="font-family:宋体"}

[[Packets received]{lang="EN-US"}]{#struct_0_13981_19121_1613999676}

[[收到的报文数目]{style="font-family:宋体"}]{#struct_0_13981_19121_x625855425}

[[Reply]{lang="EN-US"}]{#struct_0_13981_19121_1613934140}

[[收到]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_13981_19121_1371330157}[报文的数目]{style="font-family:宋体"}

[[Advertise]{lang="EN-US"}]{#struct_0_13981_19121_1614130748}

[[收到]{style="font-family:宋体"}[Advertise]{lang="EN-US"}]{#struct_0_13981_19121_x706345719}[报文的数目]{style="font-family:宋体"}

[[Reconfigure]{lang="EN-US"}]{#struct_0_13981_19121_1614065212}

[[收到]{style="font-family:宋体"}[Reconfigure]{lang="EN-US"}]{#struct_0_13981_19121_93086454}[报文的数目]{style="font-family:宋体"}

[[Invalid]{lang="EN-US"}]{#struct_0_13981_19121_1614261820}

[[无效报文的数目]{style="font-family:宋体"}]{#struct_0_13981_19121_915574985}

[[Packets sent]{lang="EN-US"}]{#struct_0_13981_19121_1614196284}

[[已发送报文的数目]{style="font-family:宋体"}]{#struct_0_13981_19121_1613737531}

[[Solicit]{lang="EN-US"}]{#struct_0_13981_19121_x1755612837}

[[已发送]{style="font-family:宋体"}[Solicit]{lang="EN-US"}]{#struct_0_13981_19121_1613671995}[报文的数目]{style="font-family:宋体"}

[[Request]{lang="EN-US"}]{#struct_0_13981_19121_x909078448}

[[已发送]{style="font-family:宋体"}[Request]{lang="EN-US"}]{#struct_0_13981_19121_1613868603}[报文的数目]{style="font-family:宋体"}

[[Renew]{lang="EN-US"}]{#struct_0_13981_19121_2133436660}

[[已发送]{style="font-family:宋体"}[Renew]{lang="EN-US"}]{#struct_0_13981_19121_1613803067}[报文的数目]{style="font-family:宋体"}

[[Rebind]{lang="EN-US"}]{#struct_0_13981_19121_1785177681}

[[已发送]{style="font-family:宋体"}[Rebind]{lang="EN-US"}]{#struct_0_13981_19121_1613999675}[报文的数目]{style="font-family:宋体"}

[[Information-request]{lang="EN-US"}]{#struct_0_13981_19121_1613934139}

[[已发送]{style="font-family:宋体"}[Information-request]{lang="EN-US"}]{#struct_0_13981_19121_1370871402}[报文的数目]{style="font-family:宋体"}

[[Release]{lang="EN-US"}]{#struct_0_13981_19121_1614130747}

[[已发送]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_13981_19121_x705362679}[报文的数目]{style="font-family:宋体"}

[[Decline]{lang="EN-US"}]{#struct_0_13981_19121_1614065211}

[[已发送]{style="font-family:宋体"}[Decline]{lang="EN-US"}]{#struct_0_13981_19121_1614261819}[报文的数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_914985164}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp client statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x1096820987}

::: {#797856274 .myid}
[]{#_Toc404787212}[]{#_Toc370742294}[]{#struct_0_13981_19121_1718158209}[]{#_Toc349031203}[]{#_Toc348965451}[]{#_Toc348956743}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- ipv6 address dhcp-alloc**

------------------------------------------------------------------------

[**[ipv6 address dhcp-alloc]{lang="EN-US"}**]{#struct_0_13981_19121_1614196283}[命令用来配置接口作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和其他网络配置参数。]{style="font-family:宋体"}

[**[undo ipv6 address dhcp-alloc]{lang="EN-US"}**]{#struct_0_13981_19121_1629023795}[命令用来取消接口作为]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端，并删除通过]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[获取到的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址和其他网络配置参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2104136105}

[**[ipv6 address dhcp-alloc ]{lang="EN-US"}**[\[ **option-group** *option*-*group-numbe*r \| **rapid-commit** \] \*]{lang="EN-US"}]{#struct_0_13981_19121_x1015021506}

[**[undo ipv6 address dhcp-alloc]{lang="EN-US"}**]{#struct_0_13981_19121_1613737530}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1755678373}

[[接口不会作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x97874313}[客户端获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和其他网络配置参数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1613671994}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x909143984}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1619362756}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x107319111}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1613868602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_2133502196}

[**[option-group ]{lang="EN-US"}***[option]{lang="EN-US"}*[-*group-number*]{lang="EN-US"}]{#struct_0_13981_19121_142471658}[：指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号。]{style="font-family:宋体"}*[option]{lang="EN-US"}*[-*group-number*]{lang="EN-US"}[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。如果指定了本参数，则]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项后，将自动创建指定编号的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组，并将获取到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项保存在该]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组中。如果没有指定本参数，则不会自动创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组。]{style="font-family:宋体"}

[**[rapid-commit]{lang="EN-US"}**]{#struct_0_13981_19121_1361857089}[：配置客户端支持地址快速分配功能。不指定该参数时，表示该客户端不支持地址快速分配功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1613803066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_1785243217}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_335610649}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和其他网络配置参数，指定客户端支持地址快速分配功能，并指定获取到网络配置参数时，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将获取的参数保存在该选项组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1613999674}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address dhcp-alloc rapid-commit option-group 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x625724353}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_80752401}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和其他网络配置参数，指定客户端支持地址快速分配功能，并指定获取到网络配置参数时，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将获取的参数保存在该选项组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1613934138}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ipv6 address dhcp-alloc rapid-commit option-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1370805866}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp client]{lang="EN-US"}**]{#struct_0_13981_19121_1921749462}
:::

::: {#-1132199314 .myid}
[]{#_Toc404787213}[]{#_Toc370742295}[]{#struct_0_13981_19121_x1739305736}[]{#_Toc349031204}[]{#_Toc348965452}[]{#_Toc348956744}[]{#_Toc348890611}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- ipv6 dhcp client dscp**

------------------------------------------------------------------------

[**[ipv6 dhcp client dscp]{lang="EN-US"}**]{#struct_0_13981_19121_1614130746}[命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ipv6 dhcp ]{lang="EN-US"}[client dscp]{lang="EN-US"}**]{#struct_0_13981_19121_x705428215}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_870684218}

[**[ipv6 dhcp client dscp ]{lang="EN-US"}**]{#struct_0_13981_19121_783963452}*[dscp-value]{lang="EN-US"}*

[**[undo ipv6 dhcp client dscp]{lang="EN-US"}**]{#struct_0_13981_19121_1614065210}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_93217526}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_323751488}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1614261818}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_915050700}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1941368231}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_653989506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1614196282}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1628958259}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_13981_19121_125491091}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1395008491}

[[DSCP]{lang="EN-US"}]{#struct_0_13981_19121_x1115145820}[携带在]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Traffic class]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x98908413}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_192288371}[配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1115211356}

[\[Sysname\] ipv6 dhcp client dscp 30]{lang="EN-US"}
:::

::: {#-117656299 .myid}
[]{#_Toc404787214}[]{#_Toc370742296}[]{#struct_0_13981_19121_1768742045}[]{#_Toc349031205}[]{#_Toc348965453}[]{#_Toc348956745}[]{#_Toc348890612}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- ipv6 dhcp client pd**

------------------------------------------------------------------------

[**[ipv6 dhcp client pd]{lang="EN-US"}**]{#struct_0_13981_19121_525483164}[命令用来配置接口作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数。]{style="font-family:宋体"}

[**[undo ipv6 dhcp client pd]{lang="EN-US"}**]{#struct_0_13981_19121_x1756520954}[命令用来取消接口作为]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端，并删除通过]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[获取到的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1115014748}

[**[ipv6 dhcp client pd]{lang="EN-US"}**[ *prefix-number* \[ **option-group** *option*-*group-number* \| **rapid-commit** \]\*]{lang="EN-US"}]{#struct_0_13981_19121_x609391953}

[**[undo ipv6 dhcp client pd]{lang="EN-US"}**]{#struct_0_13981_19121_x1180932682}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1115080284}

[[接口不会作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_642061433}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1483521336}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x1892225015}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1114883676}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x671208598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1103256829}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x84538016}

[*[prefix-number]{lang="EN-US"}*]{#struct_0_13981_19121_x1114949212}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，将动态创建指定编号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀，该前缀编号对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到的前缀。]{style="font-family:宋体"}

[**[rapid-commit]{lang="EN-US"}**]{#struct_0_13981_19121_x743645722}[：指定客户端支持前缀快速分配功能。不指定该参数时，表示不支持前缀快速分配功能。]{style="font-family:宋体"}

[**[option-group ]{lang="EN-US"}***[option-group-number]{lang="EN-US"}*]{#struct_0_13981_19121_2037101500}[：指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号。]{style="font-family:宋体"}*[option-group-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。如果指定了本参数，则]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项后，将自动创建指定编号的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组，并将获取到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项保存在该]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组中。如果没有指定本参数，则不会自动创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1114752604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x18958255}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x302163046}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数；指定获取到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀；配置客户端支持前缀快速分配功能；指定获取到网络配置参数时，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将获取的参数保存在该选项组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1114818140}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp client pd 1 rapid-commit option-group 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x447363598}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1341678501}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数；指定获取到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀；配置客户端支持前缀快速分配功能，并指定获取到网络配置参数时，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将获取的参数保存在该选项组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1078153106}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ipv6 dhcp client pd 1 rapid-commit option-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1114621532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp client]{lang="EN-US"}**]{#struct_0_13981_19121_1377402993}
:::

::: {#889840896 .myid}
[]{#_Toc404787215}[]{#_Toc370742297}[]{#struct_0_13981_19121_1500061120}[]{#_Toc349031206}[]{#_Toc348965454}[]{#_Toc348956746}[]{#_Toc348890613}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- ipv6 dhcp client stateless enable**

------------------------------------------------------------------------

[**[ipv6 dhcp client stateless enable]{lang="EN-US"}**]{#struct_0_13981_19121_x1114687068}[命令用来使能]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[无状态配置功能。]{style="font-family:宋体"}

[**[undo ipv6 dhcp client stateless enable]{lang="EN-US"}**]{#struct_0_13981_19121_x1285275090}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1291045871}

[**[ipv6 dhcp client stateless enable]{lang="EN-US"}**]{#struct_0_13981_19121_2012657283}

[**[undo ipv6 dhcp client stateless enable]{lang="EN-US"}**]{#struct_0_13981_19121_x1115145821}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1664992354}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_2129091528}[客户端无状态配置功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_750296060}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x1115211357}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x960141310}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x723085987}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1115014749}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_956691988}

[[接口使能无状态配置功能后发送]{style="font-family:宋体"}[information request]{lang="EN-US"}]{#struct_0_13981_19121_x246332809}[报文申请配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1155147703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1115080285}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x924022508}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[无状态配置功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x30545494}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp client stateless enable]{lang="EN-US"}]{#struct_0_13981_19121_x1117469742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1114883677}

[[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_13981_19121_2057674757}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[无状态配置功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_249579115}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 dhcp client stateless enable]{lang="EN-US"}
:::

::: {#1653949660 .myid}
[]{#_Toc404787216}[]{#struct_0_13981_19121_26902693}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- ipv6 dhcp client stateful**

------------------------------------------------------------------------

[**[ipv6 dhcp client stateful]{lang="EN-US"}**]{#struct_0_13981_19121_26902692}[命令用来配置接口作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式同时获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和网络配置参数。]{style="font-family:宋体"}

[**[undo ipv6 dhcp client stateful]{lang="EN-US"}**]{#struct_0_13981_19121_x569757926}[命令用来取消接口作为]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[方式同时获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和网络配置参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1413435809}

[**[ipv6 dhcp client stateful prefix]{lang="EN-US"}**]{#struct_0_13981_19121_x413572494}[ ]{lang="EN-US"}*[prefix-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[option-group]{lang="EN-US"}**[ ]{lang="EN-US"}*[option-group-number]{lang="EN-US"}*[ \| **rapid-commit** \] \*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **ipv6 dhcp client stateful**]{lang="EN-US"}]{#struct_0_13981_19121_1129245009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1543099985}

[[接口不会作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x1358340800}[客户端同时获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和网络配置参数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1434121441}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_490878834}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x820333528}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_840916682}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x247126326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1575463641}

[**[prefix]{lang="EN-US"}***[ prefix-number]{lang="EN-US"}*]{#struct_0_13981_19121_26902691}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，将动态创建指定编号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀，该前缀编号对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到的前缀。]{style="font-family:宋体"}

[**[rapid-commit]{lang="EN-US"}**]{#struct_0_13981_19121_x2143736038}[：指定客户端支持前缀快速分配功能。不指定该参数时，表示不支持前缀快速分配功能。]{style="font-family:宋体"}

[**[option-group]{lang="EN-US"}**[ *option-group-number*]{lang="EN-US"}]{#struct_0_13981_19121_x678602124}[：指定]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号。]{style="font-family:宋体"}*[option-group-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。如果指定了本参数，则]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项后，将自动创建指定编号的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组，并将获取到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项保存在该]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组中。如果没有指定本参数，则不会自动创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_90958836}

[**[ipv6 dhcp client stateful]{lang="EN-US"}**]{#struct_0_13981_19121_1484647439}[命令优先于]{style="font-family:
宋体"}**[ipv6 address dhcp-alloc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ipv6 dhcp client pd]{lang="EN-US"}**[命令：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上同时配置以上三个命令时，接口上只会生效]{lang="EN-US" style="font-family:宋体"}**[ipv6 dhcp client stateful]{lang="EN-US"}**]{#struct_0_13981_19121_x1666657026}[命令运行状态机去同时申请]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和前缀。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上同时存在以上三个命令时，如果执行]{lang="EN-US" style="font-family:宋体"}**[undo ipv6 dhcp client stateful]{lang="EN-US"}**]{#struct_0_13981_19121_x120932741}[命令，则会生效接口上另外两条命令，分别去申请]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1314777839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_2138470754}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1446442725}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数；指定获取到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀；指定客户端支持快速分配功能；指定获取到网络配置参数时，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将获取的参数保存在该选项组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1276816049}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp client stateful prefix 1 rapid-commit option-group 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13981_19121_x1421133970}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_26902690}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端，通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀和其他网络配置参数；指定获取到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀后，创建编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀；指定客户端支持快速分配功能，并指定获取到网络配置参数时，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将获取的参数保存在该选项组中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x187420902}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ipv6 dhcp client stateful prefix 1 rapid-commit option-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1713486614}

[]{#struct_0_13981_19121_980009137}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 address dhcp-alloc]{lang="EN-US"}**]{#_Toc348964141}**[ ]{lang="EN-US"}**

[]{#struct_0_13981_19121_362853906}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp client pd]{lang="EN-US"}**]{#_Toc348964143}
:::

::: {#18822410 .myid}
[]{#_Toc404787217}[]{#_Toc370742298}[]{#struct_0_13981_19121_x1114949213}[]{#_Toc349031207}[]{#_Toc348965455}[]{#_Toc348956747}[]{#_Toc348890616}[]{#_Toc321495730}

**DHCPv6 \-- DHCPv6客户端配置命令 \-- reset ipv6 dhcp client statistics**

------------------------------------------------------------------------

[**[reset ipv6 dhcp client statistics]{lang="EN-US"}**]{#struct_0_13981_19121_1985237633}[命令用来清除]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_68932994}

[**[reset ipv6 dhcp client statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1114752605}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1547125686}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x757013027}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1114818141}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1118720343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x383974200}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_354293691}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13981_19121_x1114621533}[：清除指定接口上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则清除所有]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x188680948}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1538308816}[清除所有]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp client statistics]{lang="EN-US"}]{#struct_0_13981_19121_x1114687069}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1443608265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dhcp client statistics]{lang="EN-US"}**]{#struct_0_13981_19121_x370218906}
:::

::: {#949394437 .myid}
[]{#_Toc404787219}[]{#_Toc370742300}[]{#struct_0_13981_19121_x748600141}[]{#_Toc334776794}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- display ipv6 dhcp snooping binding**

------------------------------------------------------------------------

[**[display ipv6 dhcp snooping binding]{lang="EN-US"}**]{#struct_0_13981_19121_1992036755}[命令用来显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1598078490}

[**[display ipv6 dhcp snooping binding ]{lang="EN-US"}**[\[ **address** *ipv6-address* \[ **vlan** *vlan-id* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_117617661}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_835907723}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_485822044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1324879956}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_2124450222}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x899209243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1004336116}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x2046503903}

[[【参数】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_13981_19121_x1263201417}

[**[address ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x140619324}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_13981_19121_x579523839}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[对应的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1568831227}

[[执行本命令时，如果不指定任何参数，则显示设备上所有]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1857800032}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_2124515758}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1679570508}[显示所有]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp snooping binding ]{lang="EN-US"}]{#struct_0_13981_19121_1788391367}

[1 DHCPv6 snooping entries found.                                             ]{lang="EN-US"}

[ IPv6 address     MAC address    Lease       VLAN SVLAN Interface               ]{lang="EN-US"}

[ ================ ============== =========== ==== ===== ========================]{lang="EN-US"}

[ 2::1             00e0-fc00-0006 54          2    N/A   GigabitEthernet1/0/1  ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display ipv6 dhcp snooping binding]{lang="EN-US"}]{#struct_0_13981_19121_x1121522639}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1940748479}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1263357918}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_756798771}

[[IPv6 Address]{lang="EN-US"}]{#struct_0_13981_19121_2124581294}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1827511316}[客户端获取到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_13981_19121_1269147609}

[[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x2112912406}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Lease]{lang="EN-US"}]{#struct_0_13981_19121_1410653207}

[[IPv6]{lang="EN-US"}]{#struct_0_13981_19121_500541202}[地址租约剩余时间，单位为秒]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_13981_19121_2124646830}

[[如果]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1092173418}[功能与]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能同时使用，或接收到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文带有两层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则表示第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[；否则，表示与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端连接的设备端口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[SVLAN]{lang="EN-US"}]{#struct_0_13981_19121_x1090323778}

[[如果]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x773574002}[功能与]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能同时使用，或接收到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文带有两层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则表示第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[；否则，显示为"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_13981_19121_x1661152053}

[[连接]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x212963665}[客户端的端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2123663790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_13981_19121_1945273707}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp snooping binding]{lang="EN-US"}**]{#struct_0_13981_19121_868929405}

::: {#253007676 .myid}
[]{#_Toc202081925}[]{#_Toc404787220}[]{#_Toc370742301}[]{#struct_0_13981_19121_1778344875}[]{#_Toc334776795}[]{#_Toc318132901}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- display ipv6 dhcp snooping binding database**

------------------------------------------------------------------------

[**[display ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database**]{lang="EN-US"}]{#struct_0_13981_19121_226625430}[命令用来显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项备份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_10164597}

[**[display]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **binding** **database**]{lang="EN-US"}]{#struct_0_13981_19121_x2022759007}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1690482071}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1038019234}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_2123729326}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_382550197}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x148725667}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x657935458}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x169432095}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1744177793}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_731774118}[显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项备份信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp snooping binding database]{lang="EN-US"}]{#struct_0_13981_19121_1226274359}

[File name              :   database.dhcp]{lang="EN-US"}

[[Username               :   ]{lang="EN-US"}]{#struct_0_13981_19121_2124188079}

[[Password]{lang="EN-US"}[               :   ]{lang="EN-US"}]{#struct_0_13981_19121_x162477105}

[[Update interval        :   600 seconds]{lang="EN-US"}]{#struct_0_13981_19121_x1379446399}

[Latest write time      :   Feb 27 18:48:04 2012]{lang="EN-US"}

[Status                 :   Last write succeeded.]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display ipv6 dhcp snooping binding database]{lang="EN-US"}]{#struct_0_13981_19121_1532312372}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1936933407}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x168690060}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x224452216}

[[File name]{lang="EN-US"}]{#struct_0_13981_19121_334424717}

[[存储]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_2124253615}[表项的文件名称]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_13981_19121_x538278673}

[[配置远程目标文件时的用户名]{style="font-family:宋体"}]{#struct_0_13981_19121_597984963}

[[Password]{lang="EN-US"}]{#struct_0_13981_19121_x1090320087}

[[配置远程目标文件时的密码，有配置时显示为]{style="font-family:宋体"}["\*\*\*\*\*\*"]{lang="EN-US"}]{#struct_0_13981_19121_1732379220}

[[Update interval]{lang="EN-US"}]{#struct_0_13981_19121_x1901574792}

[[定期刷新表项存储文件的刷新时间间隔，单位：秒]{style="font-family:宋体"}]{#struct_0_13981_19121_2124319151}

[[Latest write time]{lang="EN-US"}]{#struct_0_13981_19121_620380202}

[[最近一次写文件的时间]{style="font-family:宋体"}]{#struct_0_13981_19121_x802349511}

[[Status]{lang="EN-US"}]{#struct_0_13981_19121_575277685}

[[写文件的状态，即写文件是否成功]{style="font-family:宋体"}]{#struct_0_13981_19121_x917415660}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Writing]{lang="EN-US"}]{#struct_0_13981_19121_1083256948}[：正在写文件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write succeeded]{lang="EN-US"}]{#struct_0_13981_19121_2124384687}[：写文件成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write failed]{lang="EN-US"}]{#struct_0_13981_19121_1832604760}[：写文件失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1221736017 .myid}
[]{#_Toc404787221}[]{#_Toc370742302}[]{#struct_0_13981_19121_870138471}[]{#_Toc334776796}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- display ipv6 dhcp snooping packet statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6 dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_13981_19121_x780660672}[命令用来显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_204358958}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13981_19121_1432375523}

[**[display]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_13981_19121_1275186745}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_2124450223}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **packet** **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_x899274779}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13981_19121_1298266088}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **packet** **statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_1435451933}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x784818179}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x412114796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_726115455}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1538519920}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1518083094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_2124515759}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_x1679636044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_1910418426}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_638167419}[：显示指定单板的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x1868747988}[：显示指定成员设备的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x194257822}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x1122647099}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_528194076}[：显示指定单板的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_13981_19121_x798297405}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1616923140}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x415062480}[显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp snooping packet statistics]{lang="EN-US"}]{#struct_0_13981_19121_1398794363}

[ DHCPv6 packets received                 : 100]{lang="EN-US"}

[ DHCPv6 packets sent                     : 200]{lang="EN-US"}

[ Invalid DHCPv6 packets dropped          : 0]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display ipv6 dhcp snooping packet statistics]{lang="EN-US"}]{#struct_0_13981_19121_31861438}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1931062271}[[字段]{style="font-family:黑体"}]{#struct_0_13981_19121_x1855196455}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13981_19121_x2117014505}

[[DHCPv6 packets received]{lang="EN-US"}]{#struct_0_13981_19121_2124646831}

[[接收的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_1092238954}[报文数]{style="font-family:宋体"}

[[DHCPv6 packets sent]{lang="EN-US"}]{#struct_0_13981_19121_x267471846}

[[发送的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_9475555}[报文数]{style="font-family:宋体"}

[[Invalid DHCPv6 packets dropped]{lang="EN-US"}]{#struct_0_13981_19121_x819231744}

[[丢弃的无效]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_13981_19121_x2008195748}[报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2123663791}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 dhcp snooping packet statistics]{lang="EN-US"}**]{#struct_0_13981_19121_1945339243}

::: {#90257258 .myid}
[]{#_Toc239823919}[]{#_Toc305056465}[]{#_Toc404787222}[]{#_Toc370742303}[]{#struct_0_13981_19121_x326214296}[]{#_Toc334776797}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- display ipv6 dhcp snooping trust**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_13981_19121_1967992385}[命令用来显示信任端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1058063389}

[**[display ipv6 dhcp snooping trust]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13981_19121_604894060}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x867490056}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13981_19121_713892167}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_2088077282}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_2123729327}

[[network-operator]{lang="EN-US"}]{#struct_0_13981_19121_382615733}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_459781799}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13981_19121_2024126163}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_879377858}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1778044242}[显示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[信任端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dhcp snooping trust]{lang="EN-US"}]{#struct_0_13981_19121_x1685256330}

[DHCPv6 snooping is enabled.]{lang="EN-US"}

[ Interface                                       Trusted]{lang="EN-US"}

[ =========================                       ============]{lang="EN-US"}

[ GigabitEthernet1/0/1                            Trusted]{lang="EN-US"}

[[以上显示信息表示]{style="font-family:宋体"}[DHCPv6 snooping]{lang="EN-US"}]{#struct_0_13981_19121_x2032106020}[处于启用状态，信任端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604695273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **trust**]{lang="EN-US"}]{#struct_0_13981_19121_x78235475}
:::

::: {#-2005941495 .myid}
[]{#_Toc404787223}[]{#_Toc370742304}[]{#struct_0_13981_19121_1611536143}[]{#_Toc334776798}[]{#_Toc318132889}[]{#_Toc295916602}[]{#_Toc296072713}[]{#_Toc296072751}[]{#_Toc295916603}[]{#_Toc296072714}[]{#_Toc296072752}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping binding database filename**

------------------------------------------------------------------------

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_13981_19121_x59052621}[命令用来指定存储]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项的文件名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_13981_19121_x695857350}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_688298816}

[**[ipv6 dhcp snooping binding database filename]{lang="EN-US"}**[ { *filename* \| **url** *url* \[ **username** *username* \[ **password** { **cipher** \| **simple** } *key* \] \] }]{lang="EN-US"}]{#struct_0_13981_19121_479901118}

[**[undo]{lang="EN-US"}[ ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_13981_19121_x212676842}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_510770201}

[[未指定存储文件名称。]{style="font-family:宋体"}]{#struct_0_13981_19121_x604629737}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1076890389}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x877841401}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1505849752}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1431389348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1075357109}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1110095804}

[*[filename]{lang="EN-US"}*]{#struct_0_13981_19121_8073843}[：目标文件名，该配置用于本地存储模式。文件名取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[**[url]{lang="EN-US"}***[ url]{lang="EN-US"}*]{#struct_0_13981_19121_2053216950}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[，该配置用于远程文件系统模式。此参数中不能包含用户名和密码，和参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和]{style="font-family:宋体"}*[password]{lang="EN-US"}*[配合使用。远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[是否支持大小写和是否支持路径格式遵循远程服务器端规格。]{style="font-family:宋体"}

[**[username]{lang="EN-US"}***[ username]{lang="EN-US"}*]{#struct_0_13981_19121_x604564201}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[时的用户名。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_13981_19121_1518060462}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13981_19121_913114410}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_13981_19121_669343896}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604498665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_13981_19121_283022911}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[存储]{style="font-family:宋体"}]{#struct_0_13981_19121_936458390}[DHCPv6 Snooping]{lang="EN-US"}[表项时，如果设备中还不存在对应名称的文件，则设备会自动创建该文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，会立即触发一次表项备份。之后，如果未配置]{style="font-family:宋体"}]{#struct_0_13981_19121_x823800030}**[ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}[命令，若表项发生变化，默认在]{style="font-family:
宋体"}[300]{lang="EN-US"}[秒之后刷新存储文件；若表项未发生变化，则不再刷新存储文件。如果配置了]{style="font-family:
宋体"}**[ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}[命令，若表项发生变化，则到达刷新时间间隔后刷新存储文件；若表项未发生变化，则不再刷新存储文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_13981_19121_719454685}[不支持远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[，配置远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[请使用]{lang="EN-US" style="font-family:宋体"}*[url]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[username]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[key]{lang="EN-US"}*[配合使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[频繁擦写本地存储介质可能会影响存储介质寿命，建议使用远程文件系统模式存储]{style="font-family:宋体"}]{#struct_0_13981_19121_x1648186252}[DHCPv6 Snooping]{lang="EN-US"}[表项文件。]{style="font-family:宋体"}

[[当进行远程存储时，支持]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_13981_19121_x1034803265}[和]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_13981_19121_x406759538}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议时，服务器地址支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[形式或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[形式，并且支持]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名方式。服务器地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址形式时需使用方括号]{style="font-family:宋体"}[(]{lang="EN-US"}["]{style="font-family:宋体"}[\[]{lang="EN-US"}["和"]{style="font-family:
宋体"}[\]]{lang="EN-US"}["]{style="font-family:宋体"}[)]{lang="EN-US"}[引用。配置服务器地址为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名格式时请勿使用方括号引用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_13981_19121_1871973115}[FTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[ftp://\[]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\]\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式，如有用户名和密码请分别使用参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和参数]{style="font-family:宋体"}*[key]{lang="EN-US"}*[进行配置，其中用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_13981_19121_1576511612}[TFTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[tftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1368473657}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x604433129}[配置存储]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项的文件名称为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x826508088}

[\[Sysname\] ipv6 dhcp snooping binding database filename database.dhcp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_827762201}[配置远程存储]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项至]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的]{style="font-family:宋体"}[ftp]{lang="EN-US"}[服务器工作目录下，用户名为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[，文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1774831739}

[\[Sysname\] ipv6 dhcp snooping binding database filename url ftp://\[1::1\]/database.dhcp username 1 password simple 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1994344046}[配置远程存储]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项至]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2::1]{lang="EN-US"}[的]{style="font-family:宋体"}[tftp]{lang="EN-US"}[服务器工作目录下]{style="font-family:宋体"}[,]{lang="EN-US"}[文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x2137314504}

[\[Sysname\] ipv6 dhcp snooping binding database filename tftp://\[2::1\]/database.dhcp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_248509351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_13981_19121_x1278282153}
:::

::: {#-1715205112 .myid}
[]{#_Toc404787224}[]{#_Toc370742305}[]{#struct_0_13981_19121_x604367593}[]{#_Toc334776799}[]{#_Toc318132890}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping binding database update interval**

------------------------------------------------------------------------

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_13981_19121_x2020258072}[命令用来配置刷新]{style="font-family:
宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项存储文件的延迟时间。]{style="font-family:宋体"}

[**[undo ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_13981_19121_1989608224}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_211276374}

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval** *seconds*]{lang="EN-US"}]{#struct_0_13981_19121_x1126327624}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_13981_19121_x1964653296}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1892213114}

[[若]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x1765934307}[表项不变化，则不刷新存储文件；若]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒之后刷新存储文件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1915998337}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x1956292270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604302057}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1601107995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1992828924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_28357327}

[*[seconds]{lang="EN-US"}*]{#struct_0_13981_19121_1379593780}[：刷新延迟时间，取值范围为]{style="font-family:宋体"}[60-864000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_1730783495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，当]{style="font-family:宋体"}]{#struct_0_13981_19121_1819511131}[DHCPv6 Snooping]{lang="EN-US"}[表项发生变化后，]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备开始计时，当本命令配置的延迟时间到达后，]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备会把这个时间段内表项所有的变化信息备份到固化文件中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未通过]{lang="EN-US" style="font-family:宋体"}**[ipv6 ]{lang="EN-US"}**]{#struct_0_13981_19121_x1621717018}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}[命令指定存储表项的文件，则本命令的配置不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_161043477}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x604236521}[若]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项发生变化，在]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟后刷新表项存储文件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x464594445}

[\[Sysname\] ipv6 dhcp snooping binding database update interval 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1928917909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_13981_19121_2000928286}
:::

::: {#-636133833 .myid}
[]{#_Toc404787225}[]{#_Toc370742306}[]{#struct_0_13981_19121_x575489296}[]{#_Toc334776800}[]{#_Toc318132891}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping binding database update now**

------------------------------------------------------------------------

[**[ipv6 ]{lang="EN-US"}**]{#struct_0_13981_19121_x1990924012}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **now**]{lang="EN-US"}[命令用来将当前的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项保存到用户指定的文件中。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x868483534}

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **now**]{lang="EN-US"}]{#struct_0_13981_19121_1692696342}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x605219561}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1855064620}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_819417767}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1849825547}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_807109186}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_714004983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只用来触发一次]{lang="EN-US" style="font-family:宋体"}[DHCPv6 ]{lang="EN-US"}]{#struct_0_13981_19121_224084928}[S]{lang="EN-US"}[nooping]{lang="EN-US"}[表项的备份。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未通过]{lang="EN-US" style="font-family:宋体"}**[ipv6 ]{lang="EN-US"}**]{#struct_0_13981_19121_1438142408}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}[命令]{lang="EN-US" style="font-family:宋体"}[指定存储表项的文件，则本命令的配置不会生效。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1998388786}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x605154025}[将当前的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项保存到文件中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1616526516}

[\[Sysname\] ipv6 dhcp snooping binding database update now]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_643625402}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_13981_19121_x1323883290}
:::

::: {#1264903832 .myid}
[]{#_Toc404787226}[]{#_Toc370742307}[]{#struct_0_13981_19121_1947185021}[]{#_Toc334776801}[]{#_Toc318132888}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping binding record**

------------------------------------------------------------------------

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_13981_19121_1183573476}[命令用来启用端口的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_13981_19121_875495983}[命令用来关闭端口的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_470446080}

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_13981_19121_x604695272}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_13981_19121_x78301011}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_78595078}

[[端口的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1599071310}[表项记录功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_324330514}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x2139562722}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1253810362}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1620237297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x509951619}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604629736}

[[在端口上启用端口的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1076955925}[表项记录功能后，可以在端口上监听]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文，生成]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1110544815}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1336137455}[启用端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_2083960624}

[\[Sysname\]interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping binding record]{lang="EN-US"}
:::

::: {#529233638 .myid}
[]{#_Toc404787227}[]{#_Toc370742308}[]{#struct_0_13981_19121_x865310298}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping check request-message**

------------------------------------------------------------------------

[**[ipv6 dhcp snooping check request-message]{lang="EN-US"}**]{#struct_0_13981_19121_811802860}[命令用来启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[请求方向报文检查功能。]{style="font-family:宋体"}

[**[undo ipv6 dhcp snooping check request-message]{lang="EN-US"}**]{#struct_0_13981_19121_1160561542}[命令用来关闭]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[请求方向报文检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1598502976}

[**[ipv6 dhcp snooping check request-message]{lang="EN-US"}**]{#struct_0_13981_19121_x604564200}

[**[undo ipv6 dhcp snooping check request-message]{lang="EN-US"}**]{#struct_0_13981_19121_1518125998}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_838230733}

[[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x56365270}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[请求方向报文检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1626076485}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x850993857}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x413166310}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x29050031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_828188167}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604498664}

[[本功能用来检查]{style="font-family:宋体"}[DHCPv6-Renew]{lang="EN-US"}]{#struct_0_13981_19121_282957375}[、]{style="font-family:宋体"}[DHCPv6-Decline]{lang="EN-US"}[和]{style="font-family:宋体"}[DHCPv6-Release]{lang="EN-US"}[三种]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[请求方向的报文，以防止非法客户端伪造这三种报文对]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器进行攻击。]{style="font-family:宋体"}

[[如果启用了该功能，则]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x1278835370}[设备接收到上述报文后，检查本地是否存在与接收报文匹配的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。若存在，则接收报文信息与]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项信息一致时，认为该报文为合法的请求方向报文，将其转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器；不一致时，认为该报文为伪造的请求方向报文，将其丢弃。若不存在，则认为该报文合法，将其转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1247699226}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1276879611}[启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[请求方向报文检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_1771621458}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_13981_19121_855162918}

[[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping check request-message]{lang="EN-US"}]{#struct_0_13981_19121_67464876}
:::

::: {#280329821 .myid}
[]{#_Toc318132898}[]{#_Toc313433792}[]{#_Toc404787228}[]{#_Toc370742309}[]{#struct_0_13981_19121_x340530135}[]{#_Toc334776802}[]{#_Toc239823916}[]{#_Toc305056462}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping enable**

------------------------------------------------------------------------

[**[ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_x604433128}[命令用来启用]{style="font-family:
宋体"}[DHCPv6 Snooping]{lang="EN-US"}[功能。]{style="font-family:
宋体"}

[**[undo ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_x826573624}[命令用来关闭]{style="font-family:
宋体"}[DHCPv6 Snooping]{lang="EN-US"}[功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1209949960}

[**[ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_x530564040}

[**[undo ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_1963266059}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x865267789}

[[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1141788887}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1726093243}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13981_19121_1888703660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604367592}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x2020192536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_2048938139}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1315579167}

[[启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x352753980}[功能后，如果不信任端口接收到]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器发送的报文，将丢弃该报文，以保证客户端从合法的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。此时，设备不会记录]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1323996387}[功能关闭后，所有端口都可转发]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的响应报文，并且不记录]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_260655499}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x604302056}[启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1601042459}

[\[Sysname\] ipv6 dhcp snooping enable]{lang="EN-US"}
:::

::: {#553186908 .myid}
[]{#_Toc404787229}[]{#_Toc370742310}[]{#struct_0_13981_19121_x1648045913}[]{#_Toc334776803}[]{#_Toc239823917}[]{#_Toc305056463}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping max-learning-num**

------------------------------------------------------------------------

[**[ipv6 dhcp snooping max-learning-num ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_13981_19121_1396477275}[命令用来配置接口动态学习]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项的最大数目。]{style="font-family:宋体"}

[**[undo ipv6 dhcp snooping max-learning-num]{lang="EN-US"}**]{#struct_0_13981_19121_x1716990783}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_2122601647}

[**[ipv6 dhcp snooping max-learning-num ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_13981_19121_1576967232}

[**[undo ipv6 dhcp snooping max-learning-num]{lang="EN-US"}**]{#struct_0_13981_19121_1374583527}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1614981373}

[[不限制接口动态学习]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x604236520}[表项的最大数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x464659981}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_2046292305}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1231900125}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1220996110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x462452841}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1769993602}

[*[num]{lang="EN-US"}[ber]{lang="EN-US"}*]{#struct_0_13981_19121_1551831149}[：]{style="font-family:宋体"}[接口动态学习]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x605219560}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1854999084}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[动态学习]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项的最大数目为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1124379601}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping max-learning-num 1000]{lang="EN-US"}
:::

::: {#-1098288824 .myid}
[]{#_Toc404787230}[]{#_Toc370742311}[]{#struct_0_13981_19121_861888852}[]{#_Toc334776804}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping option interface-id enable**

------------------------------------------------------------------------

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **option interface-id enable**]{lang="EN-US"}]{#struct_0_13981_19121_x653474673}[命令用来启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **option interface-id enable**]{lang="EN-US"}]{#struct_0_13981_19121_x1114693597}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1928833021}

[**[ipv6 dhcp snooping option interface-id enable]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13981_19121_462327979}

[**[undo]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **option interface-id enable**]{lang="EN-US"}]{#struct_0_13981_19121_936589464}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x605154024}

[[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x1616592052}[支持]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2036227312}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x974805594}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x861904677}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1830351888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1006608539}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x578107267}

[[只有在系统视图下全局启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_1194543360}[功能，该配置才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604695275}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x78366547}[启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x364344267}

[\[Sysname\] ipv6 dhcp snooping enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping option interface-id enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_742454101}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_x2138272173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping option interface-id string]{lang="EN-US"}**]{#struct_0_13981_19121_x794462053}
:::

::: {#2115733871 .myid}
[]{#_Toc404787231}[]{#_Toc370742312}[]{#struct_0_13981_19121_2028158195}[]{#_Toc334776806}[]{#_Toc334776805}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping option interface-id string**

------------------------------------------------------------------------

[**[ipv6 dhcp snooping option interface-id string]{lang="EN-US"}**]{#struct_0_13981_19121_x1036792867}[命令用来配置]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 dhcp snooping option interface-id string]{lang="EN-US"}**]{#struct_0_13981_19121_x604629739}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1077807893}

[**[ipv6 dhcp snooping option interface-id ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \] **string** ]{lang="EN-US"}]{#struct_0_13981_19121_x507413747}*[interface-id]{lang="EN-US"}*

[**[undo ipv6 dhcp snooping option interface-id ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1379500854}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_560332120}

[[Option 18]{lang="EN-US"}]{#struct_0_13981_19121_x1869117533}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[为当前]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2073160286}

[[二层以太网端口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x2128617881}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_406147556}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1328776790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x604564203}

[[【参数】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_13981_19121_1517929390}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_13981_19121_1056257089}[：为从指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内收到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文填充]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-id]{lang="EN-US"}*]{#struct_0_13981_19121_x936250098}[：用户自定义的]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1560142312}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1239956705}[配置]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[为]{style="font-family:宋体"}[company001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x1375786306}

[\[Sysname\] ipv6 dhcp snooping enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping option interface-id enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping option interface-id string company001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1381621753}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_x1851200570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **option** **interface-id enable**]{lang="EN-US"}]{#struct_0_13981_19121_x604498667}
:::

::: {#-42954220 .myid}
[]{#_Toc404787232}[]{#_Toc370742313}[]{#struct_0_13981_19121_282891839}[]{#_Toc334776808}[]{#_Toc334776807}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping option remote-id enable**

------------------------------------------------------------------------

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **option remote-id enable**]{lang="EN-US"}]{#struct_0_13981_19121_x908014875}[命令用来启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **option remote-id enable**]{lang="EN-US"}]{#struct_0_13981_19121_703840999}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x925160731}

[**[ipv6 dhcp snooping option remote-id enable ]{lang="EN-US"}**]{#struct_0_13981_19121_x418447148}

[**[undo ipv6 dhcp snooping option remote-id enable]{lang="EN-US"}**]{#struct_0_13981_19121_x1639823556}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_1022423511}

[[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_606310700}[支持]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604433131}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x825983799}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x590979177}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_2077691155}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_706786354}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_967153955}

[[只有在系统视图下全局启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x1622787821}[功能，该配置才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_503911832}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_1060546766}[启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x604367595}

[\[Sysname\] ipv6 dhcp snooping enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping option remote-id enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2019864856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_831189844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping option remote-id string]{lang="EN-US"}**]{#struct_0_13981_19121_758957202}
:::

::: {#1147306047 .myid}
[]{#_Toc404787233}[]{#_Toc370742314}[]{#struct_0_13981_19121_x1751157712}[]{#_Toc334776809}[]{#_Toc313433794}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping option remote-id string**

------------------------------------------------------------------------

[**[ipv6 dhcp snooping option remote-id string ]{lang="EN-US"}**]{#struct_0_13981_19121_x1961960470}[命令用来配置]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 dhcp snooping option remote-id string]{lang="EN-US"}**]{#struct_0_13981_19121_x191424896}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_392427672}

[**[ipv6 dhcp snooping option remote-id ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \] **string** *remote-id*]{lang="EN-US"}]{#struct_0_13981_19121_x604302059}

[**[undo ipv6 dhcp snooping option remote-id ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_13981_19121_x1600452635}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x823669731}

[[Option 37]{lang="EN-US"}]{#struct_0_13981_19121_1837308682}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[为当前]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1768077838}

[[二层以太网端口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x1490058229}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1737628833}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_219705046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x383300558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604236523}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_13981_19121_x464463373}[：为从指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内收到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文填充]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[remote-id]{lang="EN-US"}*]{#struct_0_13981_19121_415072026}[：用户自定义的]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x397078411}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x870416280}[配置]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[选项中的]{style="font-family:宋体"}[DUID]{lang="EN-US"}[为]{style="font-family:宋体"}[device001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x775569879}

[\[Sysname\] ipv6 dhcp snooping enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping option remote-id enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping option remote-id string device001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_253880561}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping enable]{lang="EN-US"}**]{#struct_0_13981_19121_x605219563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dhcp snooping option remote-id enable]{lang="EN-US"}**]{#struct_0_13981_19121_1854933548}
:::

::::: {#-382352012 .myid}
[]{#_Toc404787234}[]{#_Toc370742315}[]{#struct_0_13981_19121_439076381}[]{#_Toc334776810}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping rate-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DHCPv6命令.files/image001.png){#图片 14 width="62" height="25"}]{lang="EN-US"}]{#struct_0_13981_19121_1835329085}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13981_19121_x85572237}
:::

**[ ]{lang="EN-US"}**

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **rate-limit**]{lang="EN-US"}]{#struct_0_13981_19121_x1111422603}[命令用来启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的报文限速功能，即限制接口接收]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的速率。]{style="font-family:宋体"}

[**[undo ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **rate-limit**]{lang="EN-US"}]{#struct_0_13981_19121_x594873216}[命令用来关闭]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的报文限速功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x914241320}

[**[ipv6 dhcp]{lang="EN-US"}**[ **snooping** **rate-limit** *rate*]{lang="EN-US"}]{#struct_0_13981_19121_800611678}

[**[undo]{lang="EN-US"}[ ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **rate-limit**]{lang="EN-US"}]{#struct_0_13981_19121_x605154027}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1616657588}

[[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x986764519}[的报文限速功能处于关闭状态，即不限制接口接收]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的速率。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x66971782}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_x479506015}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_1004584451}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x1231948368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_1210200497}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x148568738}

[*[rate]{lang="EN-US"}*]{#struct_0_13981_19121_x604695274}[：接口接收]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的最高速率，单位为]{style="font-family:宋体"}[Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}[本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x78432083}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有启用]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_13981_19121_369509541}[v]{lang="EN-US"}[6 ]{lang="EN-US"}[S]{lang="EN-US"}[nooping]{lang="EN-US"}[功能后，本命令的配置才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口接收到的]{style="font-family:宋体"}]{#struct_0_13981_19121_252227068}[DHCPv6]{lang="EN-US"}[报文速率超过了限制，则丢弃超过速率限制的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果二层以太网接口加入了聚合组，则该接口采用对应二层聚合接口下的]{style="font-family:宋体"}]{#struct_0_13981_19121_x1429919964}[DHCPv6]{lang="EN-US"}[报文限速配置。如果二层以太网接口离开聚合组，则该接口采用二层以太网接口下的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文限速配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于某些产品来说，由于芯片的限制，限速速率的实际生效值只能是某个数值的整数倍。比如，某产品芯片支持的速率值是]{style="font-family:宋体"}]{#struct_0_13981_19121_702047521}[8]{lang="EN-US"}[的整数倍，当用户设置的速率值为]{style="font-family:宋体"}[67]{lang="EN-US"}[时，实际的生效值是]{style="font-family:宋体"}[64]{lang="EN-US"}[或]{style="font-family:宋体"}[72]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_65518996}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_2099791028}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的最高速率为]{style="font-family:宋体"}[64Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x604629738}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping rate-limit 64]{lang="EN-US"}
:::::

::: {#1148620133 .myid}
[]{#_Toc404787235}[]{#_Toc370742316}[]{#struct_0_13981_19121_1077873429}[]{#_Toc334776811}[]{#_Toc239823918}[]{#_Toc305056464}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- ipv6 dhcp snooping trust**

------------------------------------------------------------------------

[**[ipv6 dhcp snooping trust]{lang="EN-US"}**]{#struct_0_13981_19121_x846288740}[命令用来配置端口为信任端口。]{style="font-family:
宋体"}

[**[undo ipv6 dhcp snooping trust]{lang="EN-US"}**]{#struct_0_13981_19121_x247089792}[命令用来恢复端口为不信任端口。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x83220012}

[**[ipv6 dhcp snooping trust]{lang="EN-US"}**]{#struct_0_13981_19121_x713760273}

[**[undo ipv6 dhcp snooping trust]{lang="EN-US"}**]{#struct_0_13981_19121_770626240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13981_19121_x794353429}

[[在启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_69781520}[功能后，设备上所有支持]{style="font-family:宋体"}[DHCPv6 snoopnig]{lang="EN-US"}[功能的端口均为不信任端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x604564202}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_1517994926}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x949758357}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x243812794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_973023395}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_x928209020}

[[启用]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x350545369}[功能后，为了使]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端能从合法的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，必须将与合法]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器相连的接口设置为信任端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_1046326117}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1460500392}[配置以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为信任端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13981_19121_x604498666}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp snooping trust]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_282826303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_13981_19121_655983853}
:::

::: {#-1731620514 .myid}
[]{#_Toc404787236}[]{#_Toc370742317}[]{#struct_0_13981_19121_x864047768}[]{#_Toc334776812}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- reset ipv6 dhcp snooping binding**

------------------------------------------------------------------------

[**[reset ipv6 dhcp snooping binding]{lang="EN-US"}**]{#struct_0_13981_19121_x20164453}[命令用来清除]{style="font-family:宋体"}[DHCPv6 Snooping ]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_x693713907}

[**[reset ipv6 dhcp snooping binding ]{lang="EN-US"}**[{ **all** \| **address** ]{lang="EN-US"}*[ipv6-address]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] }]{lang="EN-US"}]{#struct_0_13981_19121_469223542}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_1987682746}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x604433130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x826049335}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_1975261672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x69287761}

[[【参数】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_13981_19121_1215863620}

[**[address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_13981_19121_x813652402}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_13981_19121_1905453481}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[对应的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_13981_19121_x909005101}[：清除所有]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13981_19121_346568581}

[[对于分布式设备，执行该命令后，将清除所有槽位上对应的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_13981_19121_x604367594}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_x2019799320}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x1728311926}[清除所有的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp snooping binding all]{lang="EN-US"}]{#struct_0_13981_19121_1784273878}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1925317403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[ipv6 dhcp snooping binding]{lang="EN-US"}**]{#struct_0_13981_19121_x1184645272}
:::

::: {#2143801417 .myid}
[]{#_Toc404787237}[]{#_Toc370742318}[]{#struct_0_13981_19121_1667685862}[]{#_Toc334776813}[]{#_Toc202081929}[]{#_Toc318132905}

**DHCPv6 \-- DHCPv6 Snooping配置命令 \-- reset ipv6 dhcp snooping packet statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_13981_19121_2032114314}[命令用来清除]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1137063372}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13981_19121_x604302058}

[**[reset ipv6 dhcp]{lang="EN-US"}**[ **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_13981_19121_x1600387099}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13981_19121_1157085750}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **packet** **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_1603919373}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13981_19121_440155194}[模式：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **ipv6** **dhcp** **snooping** **packet** **statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13981_19121_x1178369111}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13981_19121_x678709337}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13981_19121_x244258517}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13981_19121_x1563708029}

[[network-admin]{lang="EN-US"}]{#struct_0_13981_19121_x308994207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13981_19121_x604236522}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13981_19121_x464528909}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x693142451}[：清除指定单板的]{style="font-family:宋体"}[DHCPv6 ]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。如果未指定本参数，则清除主用主控板上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x748209050}[：清除指定成员设备的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_1774914038}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x1556534757}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13981_19121_x953969317}[：清除指定单板的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_13981_19121_768310823}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13981_19121_611282067}

[[\# ]{lang="EN-US"}]{#struct_0_13981_19121_x605219562}[清除]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 dhcp snooping packet statistics]{lang="EN-US"}]{#struct_0_13981_19121_1854868012}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13981_19121_1570359520}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_13981_19121_x2092557388}
:::
