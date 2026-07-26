::: {#372542212 .myid}
[]{#_Toc404798921}[]{#struct_0_x1598_x1733_x792392975}

**HTTPD \-- HTTPD Probe命令 \-- display system internal httpd service**

------------------------------------------------------------------------

[**[display system internal httpd service]{lang="EN-US"}**]{#struct_0_x1598_x1733_x1694810970}[命令用来显示]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[服务相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x1399015613}

[**[display system internal httpd service]{lang="EN-US"}**]{#struct_0_x1598_x1733_2141812535}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x513192678}

[[Probe]{lang="EN-US"}]{#struct_0_x1598_x1733_512485600}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x1678755778}

[[network-admin]{lang="EN-US"}]{#struct_0_x1598_x1733_x1550934032}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1598_x1733_1153445974}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_694410627}

[[通过本命令可以查看]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}]{#struct_0_x1598_x1733_138504783}[服务信息，包括打开的服务端口，注册的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，内部]{style="font-family:宋体"}[LIPC]{lang="EN-US"}[端口号等。]{style="font-family:宋体"}

[[本命令仅在]{style="font-family:宋体"}[Debug]{lang="EN-US"}]{#struct_0_x1598_x1733_x1398950077}[版本支持，]{style="font-family:宋体"}[Release]{lang="EN-US"}[版本不提供。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_44247516}

[[\# ]{lang="EN-US"}]{#struct_0_x1598_x1733_x1886742496}[显示]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[服务信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1598_x1733_x1252563537}

[\[Sysname\] probe]{lang="EN-US"}

[\[Sysname-probe\] display system internal httpd service]{lang="EN-US"}

[Address family: IPv4]{lang="EN-US"}

[Port: 80]{lang="EN-US"}

[URL: /wnm/]{lang="EN-US"}

[Application family: LIPC]{lang="EN-US"}

[Application address: 0x0]{lang="EN-US"}

[Application port: 10529]{lang="EN-US"}

[ ]{lang="EN-US"}

[Address family: IPv6]{lang="EN-US"}

[Port: 80]{lang="EN-US"}

[URL: /wnm/]{lang="EN-US"}

[Application family: LIPC]{lang="EN-US"}

[Application address: 0x0]{lang="EN-US"}

[Application port: 10529]{lang="EN-US"}

[]{#struct_0_x1598_x1733_1591134784}[[表1-1 ]{lang="EN-US"}[display ]{lang="EN-US"}]{#_Toc94583061}[system internal httpd service]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1733813147}[[字段]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x1398884541}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1598_x1733_175908086}

[[Address family]{lang="EN-US"}]{#struct_0_x1598_x1733_x1010162410}

[[HTTPD]{lang="PT-BR"}]{#struct_0_x1598_x1733_x835080799}[服务的协议族类型，]{style="font-family:宋体"}[IPv4]{lang="PT-BR"}[或者]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}

[[Port]{lang="EN-US"}]{#struct_0_x1598_x1733_1116266918}

[[HTT]{lang="EN-US"}]{#struct_0_x1598_x1733_x975638884}[PD]{lang="PT-BR"}[服务打开的端口号]{style="font-family:
  宋体"}

[[URL]{lang="EN-US"}]{#struct_0_x1598_x1733_x362193423}

[[HTTPD]{lang="PT-BR"}]{#struct_0_x1598_x1733_1628077712}[服务访问的目标资源地址]{style="font-family:宋体"}

[[Application family]{lang="EN-US"}]{#struct_0_x1598_x1733_x1398819005}

[[后台服务的协议族类型，]{style="font-family:宋体"}]{#struct_0_x1598_x1733_x645034458}[LIPC]{lang="PT-BR"}[或者]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[，目前仅支持]{style="font-family:宋体"}[LIPC]{lang="PT-BR"}

[[Application address]{lang="EN-US"}]{#struct_0_x1598_x1733_x1777910278}

[[后台服务的地址，]{style="font-family:宋体"}]{#struct_0_x1598_x1733_x592068099}[LIPC]{lang="PT-BR"}[类型为]{style="font-family:宋体"}[LIPC]{lang="PT-BR"}[地址，]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[类型为]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址]{style="font-family:宋体"}

[[Application port]{lang="EN-US"}]{#struct_0_x1598_x1733_x1553432479}

[[后台服务打开的端口号]{style="font-family:宋体"}]{#struct_0_x1598_x1733_x1649272982}

[ ]{lang="EN-US"}

::: {#358293646 .myid}
[]{#_Toc404798922}[]{#struct_0_x1598_x1733_x1398753469}

**HTTPD \-- HTTPD Probe命令 \-- debugging system internal httpd**

------------------------------------------------------------------------

[**[debugging system internal httpd]{lang="EN-US"}**]{#struct_0_x1598_x1733_x883956358}[命令用来打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging system internal httpd]{lang="EN-US"}**]{#struct_0_x1598_x1733_1996041858}[命令用来关闭]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_136438805}

[**[debugging system internal httpd ]{lang="EN-US"}**[{ **all** \| **event** \| **process** \| **error** }]{lang="EN-US"}]{#struct_0_x1598_x1733_x1586057452}

[**[undo debugging system internal httpd ]{lang="EN-US"}**[{ **all** \| **event** \| **process** \| **error** }]{lang="EN-US"}]{#struct_0_x1598_x1733_x1657950993}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x106598562}

[[Probe]{lang="EN-US"}]{#struct_0_x1598_x1733_x810838499}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_848132096}

[[network-admin]{lang="EN-US"}]{#struct_0_x1598_x1733_x1398687933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1598_x1733_1217728056}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x1731155551}

[**[all]{lang="EN-US"}**]{#struct_0_x1598_x1733_1453563104}**[：]{style="font-family:宋体"}**[打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[模块全部调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1598_x1733_x970602851}**[：]{style="font-family:宋体"}**[打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[模块的事件调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_x1598_x1733_x169284614}**[：]{style="font-family:宋体"}**[打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[模块的处理调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1598_x1733_x1785531635}**[：]{style="font-family:宋体"}**[打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[模块的错误调试信息开关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1598_x1733_x1677673753}

[[\# ]{lang="EN-US"}]{#struct_0_x1598_x1733_x2046841634}[打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1598_x1733_x1398622397}

[\[Sysname\] probe]{lang="EN-US"}

[\[Sysname-probe\] debugging system internal httpd all]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1598_x1733_1414800432}[打开]{style="font-family:宋体"}[HTTPD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1598_x1733_1773143070}

[\[Sysname\] probe]{lang="EN-US"}

[\[Sysname-probe\] debugging system internal httpd event]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
