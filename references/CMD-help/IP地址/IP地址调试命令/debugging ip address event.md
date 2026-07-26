::: {#-1012726041 .myid}
[]{#_Toc404786044}[]{#struct_0_x1352_x1901_380340208}[]{#_Toc205700592}[]{#_Toc205697805}

**IP地址 \-- IP地址调试命令 \-- debugging ip address event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1352_x1901_x157863250}

[**[debugging ip address event]{lang="EN-US"}**]{#struct_0_x1352_x1901_1588041015}

[**[undo debugging ip address event]{lang="EN-US"}**]{#struct_0_x1352_x1901_1351697068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1352_x1901_x1319046004}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1352_x1901_1877525489}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1352_x1901_822514237}

[[network-admin]{lang="EN-US"}]{#struct_0_x1352_x1901_x456247613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1352_x1901_x55131735}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1352_x1901_893633029}

[**[debugging ip address event]{lang="EN-US"}**]{#struct_0_x1352_x1901_1952853772}[命令用来打开]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址事件的调试开关。]{style="font-family:宋体"}**[undo debugging ip address event]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址事件的调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1352_x1901_x1192442307}[地址事件的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ip address event]{lang="EN-US"}]{#struct_0_x1352_x1901_1351762604}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1901389661}[[字段]{style="font-family:黑体"}]{#struct_0_x1352_x1901_x915195014}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1352_x1901_1980051436}

[[module]{lang="EN-US"}]{#struct_0_x1352_x1901_x40965106}

[[被通知的模块]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1352_x1901_x203921855}

[[IP]{lang="EN-US"}]{#struct_0_x1352_x1901_1567647327}

[[IP]{lang="EN-US"}]{#struct_0_x1352_x1901_x1090157628}[地址]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_x1352_x1901_1351565996}

[[掩码]{style="font-family:宋体"}]{#struct_0_x1352_x1901_297262448}

[[Type]{lang="EN-US"}]{#struct_0_x1352_x1901_2033384236}

[[地址类型，取值如下：]{style="font-family:宋体"}]{#struct_0_x1352_x1901_x1197132404}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0]{lang="EN-US"}]{#struct_0_x1352_x1901_x165377912}[：]{style="font-family:宋体"}[无]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_x1352_x1901_2055819553}[：]{style="font-family:宋体"}[手动配置的主地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x8]{lang="EN-US"}]{#struct_0_x1352_x1901_1859930058}[：]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[分配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x10]{lang="EN-US"}]{#struct_0_x1352_x1901_1351631532}[：]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}[BOOTP]{lang="EN-US"}[分配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x20]{lang="EN-US"}]{#struct_0_x1352_x1901_x922439631}[：]{style="font-family:宋体"}[通过协商得到]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x80]{lang="EN-US"}]{#struct_0_x1352_x1901_x1860232500}[：]{style="font-family:宋体"}[手动配置的从地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x200]{lang="EN-US"}]{#struct_0_x1352_x1901_x1514053070}[：]{style="font-family:宋体"}[借用其他接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x800]{lang="EN-US"}]{#struct_0_x1352_x1901_1770898291}[：]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1000]{lang="EN-US"}]{#struct_0_x1352_x1901_1351959212}[：]{style="font-family:宋体"}[MAD]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2000]{lang="EN-US"}]{#struct_0_x1352_x1901_x1362799576}[：]{style="font-family:宋体"}[SSLVPN]{lang="EN-US"}[虚接口的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4000]{lang="EN-US"}]{#struct_0_x1352_x1901_x1296060233}[：]{style="font-family:宋体"}[集群地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x40000]{lang="EN-US"}]{#struct_0_x1352_x1901_1008079406}[：]{style="font-family:宋体"}[内部环回地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x100000]{lang="EN-US"}]{#struct_0_x1352_x1901_x1133953699}[：]{style="font-family:宋体"}[mtunnel]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x200000]{lang="EN-US"}]{#struct_0_x1352_x1901_1352024748}[：]{style="font-family:宋体"}[本地]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x400000]{lang="EN-US"}]{#struct_0_x1352_x1901_x263957847}[：]{style="font-family:宋体"}[本地]{lang="EN-US" style="font-family:宋体"}[NATPT]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x800000]{lang="EN-US"}]{#struct_0_x1352_x1901_x101428766}[：]{style="font-family:宋体"}[本地]{lang="EN-US" style="font-family:宋体"}[LB]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x10000000]{lang="EN-US"}]{#struct_0_x1352_x1901_1963169344}[：]{style="font-family:宋体"}[引入的主机地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x20000000]{lang="EN-US"}]{#struct_0_x1352_x1901_x407362700}[：]{style="font-family:宋体"}[引入的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[主机地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x40000000]{lang="EN-US"}]{#struct_0_x1352_x1901_1351828140}[：]{style="font-family:宋体"}[引入的]{lang="EN-US" style="font-family:宋体"}[LB]{lang="EN-US"}[主机地址]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1352_x1901_x1361393435}

[[地址状态，取值如下：]{style="font-family:宋体"}]{#struct_0_x1352_x1901_x1059963844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_x1352_x1901_534967805}[：可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_x1352_x1901_1078057075}[：不可用]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1352_x1901_1351893676}

[[\# ]{lang="EN-US"}]{#struct_0_x1352_x1901_624346685}[在设备上配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址事件的调试信息开关，配置接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[，掩码为]{style="font-family:宋体"}[24]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[[[\<Sysname\> ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[debugging ip address event]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}]{#struct_0_x1352_x1901_x931304912}

[[[\<Sysname\> system-view]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\[Sysname\]]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[ ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[interface ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[gigabite]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[thernet]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[0/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\[Sysname-]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Gigabit]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Ethernet]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[0/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[\]ip address 2.1.1.1 24]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\[Sysname-]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Gigabit]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Ethernet]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[0/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[\]]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\*]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Dec]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[ ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[3]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[ 15:13:01:182 2012 Sysname ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[IPADDR]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[/7/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[EVENT]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[: -MDC=1;]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[IP address add event notified to module 0x04030000,]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[IP: 2.1.1.1, Mask: 255.255.255.0, Type: 0x1, State: 0x1, ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[V]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[PN Index: 0, Interface: ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Gigabit]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[Ethernet]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[0/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[1]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[ ]{lang="EN-US"}
