::::: {#1456515988 .myid}
[]{#_Toc404796762}[]{#struct_0_x4606_33440_317037197}

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock self-test-result**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_2067511172}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_583253002}
:::

**[ ]{lang="EN-US"}**

[**[display network-clock self-test-result]{lang="EN-US"}**]{#struct_0_x4606_33440_1240401018}[命令用来查看时钟监控的自检结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1475524588}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1693451992}

[**[display network-clock self-test-result]{lang="EN-US"}**]{#struct_0_x4606_33440_1640883094}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_3919419}[模式：]{style="font-family:宋体"}

[**[display network-clock self-test-result]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x4606_33440_763766119}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_872580556}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x549895104}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1377127424}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1224346880}

[[network-operator]{lang="EN-US"}]{#struct_0_x4606_33440_1159219909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1019390576}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4606_33440_2105430502}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1011804179}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x2132750770}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控自检结果。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1758141130}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_387392122}[查看时钟监控的自检结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock self-test-result]{lang="EN-US"}]{#struct_0_x4606_33440_x549960640}

[Clock module work mode: Normal]{lang="EN-US"}

[  SRAM                : Normal]{lang="EN-US"}

[  CPLD                : Normal]{lang="EN-US"}

[  E1A                 : Normal]{lang="EN-US"}

[  E1B                 : Normal]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_210702766}[查看所有成员设备的时钟监控自检结果。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock self-test-result]{lang="EN-US"}]{#struct_0_x4606_33440_x716999360}

[Chassis 0]{lang="EN-US"}[：]{style="font-family:宋体"}

[Clock module state: Normal]{lang="EN-US"}

[  SRAM                : Normal]{lang="EN-US"}

[  CPLD                : Normal]{lang="EN-US"}

[  E1A                 : Normal]{lang="EN-US"}

[  E1B                 : Normal]{lang="EN-US"}

[Chassis 1]{lang="EN-US"}[：]{style="font-family:宋体"}

[Clock module state: Normal]{lang="EN-US"}

[  SRAM                : Normal]{lang="EN-US"}

[  CPLD                : Normal]{lang="EN-US"}

[  E1A                 : Normal]{lang="EN-US"}

[  E1B                 : Normal]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display network-clock self-test-result]{lang="EN-US"}]{#struct_0_x4606_33440_1283130172}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_320394765}[[字段]{style="font-family:黑体"}]{#struct_0_x4606_33440_581597014}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4606_33440_227210006}

[[Clock module work mode]{lang="EN-US"}]{#struct_0_x4606_33440_x549370817}

[[时钟芯片状态，包括：]{style="font-family:宋体"}]{#struct_0_x4606_33440_2116096267}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4606_33440_x1421090336}[：工作正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x4606_33440_x270565404}[：工作故障（如果以下任意一项故障，则显示工作故障）]{style="font-family:宋体"}

[[SRAM]{lang="EN-US"}]{#struct_0_x4606_33440_x1403756495}

[[SRAM]{lang="EN-US"}]{#struct_0_x4606_33440_x1659802464}[（]{style="font-family:宋体"}[Static Random Access Memory]{lang="EN-US"}[，静态随机存储器）状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4606_33440_x1846973115}[：工作正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x4606_33440_x1051213228}[：工作故障]{lang="EN-US" style="font-family:宋体"}

[[CPLD]{lang="EN-US"}]{#struct_0_x4606_33440_x549436353}

[[CPLD]{lang="EN-US"}]{#struct_0_x4606_33440_x571910736}[（]{style="font-family:宋体"}[Complex Programmable Logical Device]{lang="EN-US"}[，复杂可编程逻辑器件）状态，包括：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4606_33440_1767768804}[：工作正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x4606_33440_710520466}[：工作故障]{lang="EN-US" style="font-family:宋体"}

[[E1A]{lang="EN-US"}]{#struct_0_x4606_33440_x261170028}

[[芯片]{style="font-family:宋体"}[E1A]{lang="EN-US"}]{#struct_0_x4606_33440_x758046529}[状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4606_33440_x549501889}[：工作正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x4606_33440_543917521}[：工作故障]{lang="EN-US" style="font-family:宋体"}

[[E1B]{lang="EN-US"}]{#struct_0_x4606_33440_2002304242}

[[芯片]{style="font-family:宋体"}[E1B]{lang="EN-US"}]{#struct_0_x4606_33440_x1864832722}[状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4606_33440_x373011370}[：工作正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x4606_33440_x550466307}[：工作故障]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1191085820 .myid}
[]{#_Toc404796763}[]{#struct_0_x4606_33440_x549567425}

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock source**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x931345879}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_x750019790}
:::

**[ ]{lang="EN-US"}**

[**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_x1631510054}[命令用来查看所有参考源的状态。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1844369791}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_700758171}

[**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_264666717}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_853995668}[模式：]{style="font-family:宋体"}

[**[display network-clock source]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x4606_33440_624576140}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x742155803}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_1675473657}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549108673}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_553891231}

[[network-operator]{lang="EN-US"}]{#struct_0_x4606_33440_201190468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x812332609}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4606_33440_x20780794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x316584013}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x777149205}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控参考源的状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1680074888}

[[本命令用来查看当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x4606_33440_x1907734059}[的所有参考源的状态。]{style="font-family:宋体"}

[[在任何]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x4606_33440_1478433625}[上都能执行本命令查看到]{style="font-family:宋体"}[BITS]{lang="EN-US"}[时钟源。线路时钟源只能在它对应的接口所在的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中查看，当线路时钟源的所有参数均为默认值时该时钟源不显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1672859093}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x549174209}[查看所有时钟监控参考源的状态。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock source]{lang="EN-US"}]{#struct_0_x4606_33440_x1357169058}

[Traced reference: Pos3/1/1]{lang="EN-US"}

[BITS   State  Priority  SSM level  Force SSM  Sa bit  Direction  Frequency]{lang="EN-US"}

[BITS0  Lost   255       Unknown    ON         4       In         2 Mbps]{lang="EN-US"}

[BITS1  Lost   255       Unknown    ON         4       Out        2 MHz]{lang="EN-US"}

[Port       State  Priority  SSM level  Force SSM  LPU port]{lang="EN-US"}

[Pos3/1/1   Normal 10        Unknown    OFF        Yes ]{lang="EN-US"}

[Cpos4/1/9  Normal 15        Unknown    ON         No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x159334524}[查看所有成员设备的时钟监控参考源的状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock source]{lang="EN-US"}]{#struct_0_x4606_33440_1033772990}

[Chassis 1:]{lang="EN-US"}

[Traced reference: Pos1/3/1/1]{lang="EN-US"}

[BITS   State  Priority  SSM level  Force SSM  Sa bit  Direction  Frequency]{lang="EN-US"}

[BITS0  Lost   255       Unknown    ON         4       In         2 Mbps]{lang="EN-US"}

[BITS1  Lost   255       Unknown    ON         4       Out        2 MHz]{lang="EN-US"}

[Port        State  Priority  SSM level  Force SSM  LPU port]{lang="EN-US"}

[Pos1/3/1/1  Normal 1         PRC        OFF        Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 2:]{lang="EN-US"}

[Traced reference: Pos2/2/1/8]{lang="EN-US"}

[BITS   State  Priority  SSM level  Force SSM  Sa bit  Direction  Frequency]{lang="EN-US"}

[BITS0  Lost   10        Unknown    ON         4       In         2 Mbps]{lang="EN-US"}

[BITS1  Lost   255       Unknown    ON         4       Out        2 MHz]{lang="EN-US"}

[Port        State  Priority  SSM level  Force SSM  LPU port]{lang="EN-US"}

[Pos2/2/1/8  Normal 1         PRC        OFF        Yes]{lang="EN-US"}

[Cpos2/4/2/2 Normal 15        Unknown    ON         No]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display network-clock source]{lang="EN-US"}]{#struct_0_x4606_33440_x1192231447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_322532967}[[字段]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549239745}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4606_33440_941828634}

[[Traced reference]{lang="EN-US"}]{#struct_0_x4606_33440_678169641}

[[已选中的参考源，没有跟踪时显示]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x4606_33440_x1730067973}

[[当参考源被选中时，系统将同步时钟信号到所有接口板]{style="font-family:宋体"}]{#struct_0_x4606_33440_x806450844}

[[Reference]{lang="EN-US"}]{#struct_0_x4606_33440_x1565833270}

[[参考源]{style="font-family:宋体"}]{#struct_0_x4606_33440_275400675}

[[State]{lang="EN-US"}]{#struct_0_x4606_33440_x679125784}

[[参考源的状态：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1451466812}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4606_33440_x549305281}[：正常工作的时钟源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lost]{lang="EN-US"}]{#struct_0_x4606_33440_1365750579}[：未工作或异常的时钟源]{lang="EN-US" style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x4606_33440_x1997646990}

[[参考源的优先级]{style="font-family:宋体"}]{#struct_0_x4606_33440_x257052018}

[[SSM level]{lang="EN-US"}]{#struct_0_x4606_33440_465504366}

[[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_x1653951942}[级别，按照其同步质量由高到低依次为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRC]{lang="EN-US"}]{#struct_0_x4606_33440_x1538989195}[：]{lang="EN-US" style="font-family:宋体"}[G.811]{lang="EN-US"}[时钟信号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-A]{lang="EN-US"}]{#struct_0_x4606_33440_x549895105}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[转接节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-B]{lang="EN-US"}]{#struct_0_x4606_33440_x1377192960}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[本地节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SEC]{lang="EN-US"}]{#struct_0_x4606_33440_x1051331096}[：]{style="font-family:宋体"}[SDH]{lang="EN-US"}[设备时钟源信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNU]{lang="EN-US"}]{#struct_0_x4606_33440_608454714}[：不]{style="font-family:宋体"}[应]{lang="EN-US" style="font-family:宋体"}[用作同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x4606_33440_172930805}[：时钟源的同步质量未知]{lang="EN-US" style="font-family:宋体"}

[[Force SSM]{lang="EN-US"}]{#struct_0_x4606_33440_x549960641}

[[是否从时钟源提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_210768302}[级别：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ON]{lang="EN-US"}]{#struct_0_x4606_33440_x1917213938}[：不从时钟源提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OFF]{lang="EN-US"}]{#struct_0_x4606_33440_x727035281}[：从时钟源提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别]{style="font-family:宋体"}

[[Sa bit]{lang="EN-US"}]{#struct_0_x4606_33440_131768986}

[[传输]{style="font-family:宋体"}[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_1129592090}[时钟源承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sa4]{lang="EN-US"}]{#struct_0_x4606_33440_x549370818}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的]{style="font-family:宋体"}[sa]{lang="EN-US"}[时隙为]{style="font-family:宋体"}[sa4]{lang="EN-US"}[比特]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sa5]{lang="EN-US"}]{#struct_0_x4606_33440_2115506443}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的]{style="font-family:宋体"}[sa]{lang="EN-US"}[时隙为]{style="font-family:宋体"}[sa5]{lang="EN-US"}[比特]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sa6]{lang="EN-US"}]{#struct_0_x4606_33440_x499260927}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的]{style="font-family:宋体"}[sa]{lang="EN-US"}[时隙为]{style="font-family:宋体"}[sa6]{lang="EN-US"}[比特]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sa7]{lang="EN-US"}]{#struct_0_x4606_33440_113059201}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的]{style="font-family:宋体"}[sa]{lang="EN-US"}[时隙为]{style="font-family:宋体"}[sa7]{lang="EN-US"}[比特]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sa8]{lang="EN-US"}]{#struct_0_x4606_33440_1406598575}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的]{style="font-family:宋体"}[sa]{lang="EN-US"}[时隙为]{style="font-family:宋体"}[sa8]{lang="EN-US"}[比特]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4606_33440_x549436354}[：线路时钟源不支持配置]{lang="EN-US" style="font-family:宋体"}[Sa-bit]{lang="EN-US"}

[[Direction]{lang="EN-US"}]{#struct_0_x4606_33440_x996832363}

[[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_1671118193}[时钟源方向：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In]{lang="EN-US"}]{#struct_0_x4606_33440_1865322502}[：接收外部时钟信息号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Out]{lang="EN-US"}]{#struct_0_x4606_33440_7224613}[：向外提供时钟信号]{style="font-family:宋体"}

[[Frequency]{lang="EN-US"}]{#struct_0_x4606_33440_x996766827}

[[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_x263647360}[时钟源频率：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2 Mbps]{lang="EN-US"}]{#struct_0_x4606_33440_x1290710587}[：频率为]{style="font-family:宋体"}[2 Mbps]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2 MHz]{lang="EN-US"}]{#struct_0_x4606_33440_x1677194408}[：频率为]{style="font-family:宋体"}[2 MHz]{lang="EN-US"}

[[LPU port]{lang="EN-US"}]{#struct_0_x4606_33440_x571976272}

[[端口是否使能]{style="font-family:宋体"}[LPU port]{lang="EN-US"}]{#struct_0_x4606_33440_x217465214}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x4606_33440_1412903021}[：使能]{lang="EN-US" style="font-family:宋体"}[LPU port]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x4606_33440_x549501890}[：未使能]{lang="EN-US" style="font-family:宋体"}[LPU port]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4606_33440_543327696}[：]{lang="EN-US" style="font-family:宋体"}[BITS0]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[BITS1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[PTP]{lang="EN-US"}[等显示为]{lang="EN-US" style="font-family:宋体"}[N/A]{lang="EN-US"}

[\
]{lang="EN-US"}

::::: {#1076461974 .myid}
[]{#_Toc404796764}[]{#struct_0_x4606_33440_510008093}[]{#_Toc369767202}[]{#_Toc369767855}[]{#_Toc369767879}[]{#_Toc369767965}[]{#_Toc369767203}[]{#_Toc369767856}[]{#_Toc369767880}[]{#_Toc369767966}

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock status**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_33624807}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_418005969}
:::

**[ ]{lang="EN-US"}**

[**[display network-clock status]{lang="EN-US"}**]{#struct_0_x4606_33440_x1284296133}[命令用来查看时钟监控的工作状态。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1546459572}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_91860206}

[**[display network-clock status]{lang="EN-US"}**]{#struct_0_x4606_33440_x744527715}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x549567426}[模式：]{style="font-family:宋体"}

[**[display network-clock status]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x4606_33440_x931280343}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x393223699}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_498911145}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2144872796}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x268035508}

[[network-operator]{lang="EN-US"}]{#struct_0_x4606_33440_x2093455513}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1133348797}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4606_33440_149890193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1269687018}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x1739160634}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控工作状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549108674}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_553694623}[查看时钟监控的工作状态。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock status]{lang="EN-US"}]{#struct_0_x4606_33440_9312730}

[Mode              : Auto]{lang="EN-US"}

[Traced reference  : N/A]{lang="EN-US"}

[Lock mode         : Unknown]{lang="EN-US"}

[SSM output level  : SSUB]{lang="EN-US"}

[SSM control enable: On]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_26801743}[查看所有成员设备的时钟监控工作状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock status]{lang="EN-US"}]{#struct_0_x4606_33440_x549174210}

[Chassis 0:]{lang="EN-US"}

[Mode              : Auto]{lang="EN-US"}

[Reference         : N/A]{lang="EN-US"}

[Traced reference  : N/A]{lang="EN-US"}

[Lock mode         : Unknown]{lang="EN-US"}

[SSM output level  : SSUB]{lang="EN-US"}

[SSM control enable: On]{lang="EN-US"}

[Chassis 1:]{lang="EN-US"}

[Mode              : Auto]{lang="EN-US"}

[Reference         : N/A]{lang="EN-US"}

[Traced reference  : N/A]{lang="EN-US"}

[Lock mode         : Unknown]{lang="EN-US"}

[SSM output level  : SSUB]{lang="EN-US"}

[SSM control enable: On]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display network-clock status]{lang="EN-US"}]{#struct_0_x4606_33440_x1356579235}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_348396717}[[字段]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1425024067}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4606_33440_1602911149}

[[Mode]{lang="EN-US"}]{#struct_0_x4606_33440_65247073}

[[工作模式，包括：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1482248548}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x4606_33440_1316503620}[：自动模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x4606_33440_x1535334737}[：手动模式]{lang="EN-US" style="font-family:宋体"}

[[Traced reference]{lang="EN-US"}]{#struct_0_x4606_33440_x591027440}

[[已选中的参考源，没有时钟源选中时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x4606_33440_x549239746}

[[Lock mode]{lang="EN-US"}]{#struct_0_x4606_33440_941763098}

[[时钟监控的锁相状态，包括：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1245782659}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Freerun]{lang="EN-US"}]{#struct_0_x4606_33440_34101828}[：自由振荡状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Locked]{lang="EN-US"}]{#struct_0_x4606_33440_1949699057}[：锁定（跟踪）状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Holdover]{lang="EN-US"}]{#struct_0_x4606_33440_170810626}[：保持状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pre-locked]{lang="EN-US"}]{#struct_0_x4606_33440_995298566}[：预锁状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lost]{lang="EN-US"}]{#struct_0_x4606_33440_x549305282}[：信号丢失状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x4606_33440_1365553971}[：信号未知]{lang="EN-US" style="font-family:宋体"}

[[SSM output level]{lang="EN-US"}]{#struct_0_x4606_33440_x399462155}

[[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_1648835826}[级别，由高到低依次为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRC]{lang="EN-US"}]{#struct_0_x4606_33440_1798431998}[：]{lang="EN-US" style="font-family:宋体"}[G.811]{lang="EN-US"}[时钟信号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-A]{lang="EN-US"}]{#struct_0_x4606_33440_910156694}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[转接节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-B]{lang="EN-US"}]{#struct_0_x4606_33440_x549895106}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[本地节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SEC]{lang="EN-US"}]{#struct_0_x4606_33440_x1376996352}[：]{style="font-family:宋体"}[SDH]{lang="EN-US"}[设备时钟源信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNU]{lang="EN-US"}]{#struct_0_x4606_33440_629530417}[：不]{style="font-family:宋体"}[应]{lang="EN-US" style="font-family:宋体"}[用作同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x4606_33440_178392310}[：时钟源的同步质量未知]{lang="EN-US" style="font-family:宋体"}

[[SSM control enable]{lang="EN-US"}]{#struct_0_x4606_33440_1642529199}

[[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_x549960642}[级别是否参与控制时钟源的选举：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x4606_33440_210833838}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别参与控制]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x4606_33440_x1337214042}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别不参与控制]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::::: {#1369175030 .myid}
[]{#_Toc404796765}[]{#struct_0_x4606_33440_619244438}[]{#_Toc369767205}[]{#_Toc369767858}[]{#_Toc369767882}[]{#_Toc369767968}[]{#_Toc369767206}[]{#_Toc369767859}[]{#_Toc369767883}[]{#_Toc369767969}[]{#_Toc369767208}[]{#_Toc369767861}[]{#_Toc369767885}[]{#_Toc369767970}[]{#_Toc369767209}[]{#_Toc369767862}[]{#_Toc369767886}[]{#_Toc369767971}

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock version**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x184414952}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_1168250713}
:::

**[ ]{lang="EN-US"}**

[**[display network-clock]{lang="EN-US"}**[ **version**]{lang="EN-US"}]{#struct_0_x4606_33440_975918093}[令用来查看时钟监控的版本信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_946160378}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x549370819}

[**[display network-clock]{lang="EN-US"}**[ **version**]{lang="EN-US"}]{#struct_0_x4606_33440_2115440907}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x2008680152}[模式：]{style="font-family:宋体"}

[**[display network-clock]{lang="EN-US"}**[ **version** \[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x4606_33440_x285095900}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_57772813}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x77287379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x86739034}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x2008014617}

[[network-operator]{lang="EN-US"}]{#struct_0_x4606_33440_x2124249399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1532061986}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4606_33440_x1586713897}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549436355}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x572041808}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控版本信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x271086337}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_2067905854}[查看时钟监控的版本信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock version]{lang="EN-US"}]{#struct_0_x4606_33440_x1810920188}

[Clock card]{lang="EN-US"}

[  Type      : SR01CK3A]{lang="EN-US"}

[  Software  : 106]{lang="EN-US"}

[  PCB       : A]{lang="EN-US"}

[  Number of Cpld: 1]{lang="EN-US"}

[  Cpld 0:]{lang="EN-US"}

[    Software  : 001]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x2005833848}[查看成员设备]{style="font-family:宋体"}[0]{lang="EN-US"}[的时钟监控版本信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display network-clock version chassis 0:]{lang="EN-US"}]{#struct_0_x4606_33440_x549501891}

[Clock card]{lang="EN-US"}

[  Type      : SR01CK3A]{lang="EN-US"}

[  Software  : 106]{lang="EN-US"}

[  PCB       : A]{lang="EN-US"}

[  Number of Cpld: 1]{lang="EN-US"}

[  Cpld 0:]{lang="EN-US"}

[    Software  : 001]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_543393232}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的具体显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_x321000380}
:::

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display network-clock version]{lang="EN-US"}]{#struct_0_x4606_33440_1942356076}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_350351657}[[字段]{style="font-family:黑体"}]{#struct_0_x4606_33440_245270614}
:::::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4606_33440_x976724781}

[[Type]{lang="EN-US"}]{#struct_0_x4606_33440_x1773742826}

[[时钟扣板类型，当前有]{style="font-family:宋体"}[SR01CK3A]{lang="EN-US"}]{#struct_0_x4606_33440_x43000512}[和]{style="font-family:宋体"}[SR07CK3C]{lang="EN-US"}[两种类型]{style="font-family:宋体"}

[[Software]{lang="EN-US"}]{#struct_0_x4606_33440_1766693546}

[[时钟扣板软件版本]{style="font-family:宋体"}]{#struct_0_x4606_33440_x549567427}

[[PCB]{lang="EN-US"}]{#struct_0_x4606_33440_x931214807}

[[时钟扣板]{style="font-family:宋体"}[PCB]{lang="EN-US"}]{#struct_0_x4606_33440_1988235141}[（]{style="font-family:宋体"}[Printed Circuit Board]{lang="EN-US"}[，印制电路板）版本]{style="font-family:宋体"}

[[Number of Cpld]{lang="EN-US"}]{#struct_0_x4606_33440_x1789608257}

[[时钟扣板]{style="font-family:宋体"}[CPLD]{lang="EN-US"}]{#struct_0_x4606_33440_1307926296}[个数]{style="font-family:宋体"}

[[Cpld 0]{lang="EN-US"}]{#struct_0_x4606_33440_1465125890}

[[时钟扣板的]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4606_33440_x1132488019}[号]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[，即第一个]{style="font-family:宋体"}[CPLD]{lang="EN-US"}

[[Software]{lang="EN-US"}]{#struct_0_x4606_33440_x549108675}

[[时钟扣板]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4606_33440_553760159}[号]{style="font-family:宋体"}[CPLD]{lang="EN-US"}[的软件版本]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1336883564 .myid}
[]{#_Toc404796766}[]{#struct_0_x4606_33440_27889722}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock lpuport**

------------------------------------------------------------------------

[**[network-clock lpuport]{lang="EN-US"}**]{#struct_0_x4606_33440_1442807317}[命令用来配置线路时钟源的输入端口。]{style="font-family:宋体"}

[**[undo network-clock lpuport]{lang="EN-US"}**]{#struct_0_x4606_33440_833223622}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x398637646}

[**[network-clock lpuport]{lang="EN-US"}**[ *port-type port-number*]{lang="EN-US"}]{#struct_0_x4606_33440_x1496139368}

[**[undo network-clock lpuport]{lang="EN-US"}**[ *port-type port-number*]{lang="EN-US"}]{#struct_0_x4606_33440_x1038272981}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1100108394}

[[未配置线路时钟源的输入端口。]{style="font-family:宋体"}]{#struct_0_x4606_33440_1557579932}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549174211}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1356644771}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x405432773}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1872230351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_422047195}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1732602879}

[*[port-type port-number]{lang="EN-US"}*]{#struct_0_x4606_33440_505520745}[：端口类型及端口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_352642061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只允许将主接口指定为线路时钟源的输入端口。]{style="font-family:宋体"}]{#struct_0_x4606_33440_628501474}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备允许配置多个线路时钟源的输入端口。在自动模式下，设备上最终生效的线路时钟源输入端口为配置的所有输入端口中的最优端口；在手动模式下，设备上最终生效的线路时钟源输入端口为该模式下通过]{style="font-family:宋体"}]{#struct_0_x4606_33440_23604309}**[network-clock work-mode manual mdc]{lang="EN-US"}**[命令指定的]{style="font-family:
宋体"}[MDC]{lang="EN-US"}[的时钟源。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不建议将主时钟模式的端口配置为线路时钟源的输入端口。]{style="font-family:宋体"}]{#struct_0_x4606_33440_x996457550}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549239747}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_941697562}[配置线路时钟源的输入端口为]{style="font-family:宋体"}[POS2/2/0]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_2023457253}

[\[Sysname\] network-clock lpuport pos 2/2/0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1397273413}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_x110757091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network-clock work-mode manual mdc]{lang="EN-US"}**]{#struct_0_x4606_33440_1609241798}
:::

::::: {#645730468 .myid}
[]{#_Toc404796767}[]{#struct_0_x4606_33440_569317117}[]{#_Toc375382804}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source direction**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x1119235349}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_1376708254}
:::

[ ]{lang="EN-US"}

[**[network-clock source ]{lang="FR"}[direction]{lang="EN-US"}**]{#struct_0_x4606_33440_388730835}[命令用来配置传输]{style="font-family:
宋体"}[BITS]{lang="FR"}[时钟源]{style="font-family:宋体"}[方向]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo network-clock source ]{lang="FR"}[direction]{lang="EN-US"}**]{#struct_0_x4606_33440_1017498036}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1612338822}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x126410874}

[**[network-clock source ]{lang="FR"}**]{#struct_0_x4606_33440_x1769668259}[{ **bits0** \| **bits1** } **direction** { **in** \| **out** }]{lang="FR"}

[**[undo network-clock source ]{lang="FR"}**]{#struct_0_x4606_33440_x1183686003}[{ **bits0** \| **bits1** } **direction**]{lang="FR"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_568727294}[模式：]{style="font-family:宋体"}

[**[network-clock]{lang="EN-US"}**]{#struct_0_x4606_33440_1207795061}**[ ]{lang="EN-US"}[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}[ ]{lang="EN-US"}**[source ]{lang="FR"}**[{ **bits0** \| **bits1** } ]{lang="FR"}[{ ]{lang="SV"}**[in]{lang="FR"}**[ \| ]{lang="SV"}**[out]{lang="FR"}**[ }]{lang="SV"}

[**[undo ]{lang="FR"}[network-clock]{lang="EN-US"}**]{#struct_0_x4606_33440_1639410326}[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}**[source ]{lang="FR"}**[{ **bits0** \| **bits1** } ]{lang="FR"}**[direction]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_274666648}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4606_33440_610368492}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1266296919}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x655610467}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1847521996}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1406617641}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x26583143}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1013672348}

[**[chassis ]{lang="SV"}**]{#struct_0_x4606_33440_568792830}*[chassis-number]{lang="SV"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="SV"}[模式]{style="font-family:宋体"}[）]{style="font-family:
宋体"}

[**[bits0]{lang="SV"}**]{#struct_0_x4606_33440_91865230}[：]{style="font-family:宋体"}[BITS0]{lang="SV"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="SV"}**]{#struct_0_x4606_33440_x325454849}[：]{style="font-family:宋体"}[BITS1]{lang="SV"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[in]{lang="SV"}**]{#struct_0_x4606_33440_580988656}[：时钟源方向为入方向，即此时时钟源接收外部时钟信号]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[**[out]{lang="FR"}**]{#struct_0_x4606_33440_215349938}[：]{style="font-family:宋体"}[时钟源方向为出方向，即此时时钟源向外提供时钟信号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_214583625}

[[该命令只支持在管理]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x4606_33440_1187609264}[中配置，但配置对所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1081951981}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_1643047662}[配置]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源方向为出方向。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_568858366}

[\[Sysname\] network-clock source bits0 direction out]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x914361795}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源的方向为出方向。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_1567841706}

[\[Sysname\] network-clock chassis 1 source bits0 direction out]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1048328354}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_x505126514}
:::::

::: {#-1165739823 .myid}
[]{#_Toc404796768}[]{#struct_0_x4606_33440_x1032435868}[]{#_Toc356330121}[]{#_Toc356831261}[]{#_Toc356330122}[]{#_Toc356831262}[]{#_Toc356330123}[]{#_Toc356831263}[]{#_Toc356330124}[]{#_Toc356831264}[]{#_Toc356330125}[]{#_Toc356831265}[]{#_Toc356330126}[]{#_Toc356831266}[]{#_Toc356330127}[]{#_Toc356831267}[]{#_Toc356330128}[]{#_Toc356831268}[]{#_Toc356330129}[]{#_Toc356831269}[]{#_Toc356330130}[]{#_Toc356831270}[]{#_Toc356330131}[]{#_Toc356831271}[]{#_Toc356330132}[]{#_Toc356831272}[]{#_Toc356330133}[]{#_Toc356831273}[]{#_Toc356330134}[]{#_Toc356831274}[]{#_Toc356330135}[]{#_Toc356831275}[]{#_Toc356330136}[]{#_Toc356831276}[]{#_Toc356330137}[]{#_Toc356831277}[]{#_Toc356330138}[]{#_Toc356831278}[]{#_Toc356330139}[]{#_Toc356831279}[]{#_Toc356330140}[]{#_Toc356831280}[]{#_Toc356330141}[]{#_Toc356831281}[]{#_Toc356330142}[]{#_Toc356831282}[]{#_Toc356330143}[]{#_Toc356831283}[]{#_Toc356330144}[]{#_Toc356831284}[]{#_Toc356330145}[]{#_Toc356831285}[]{#_Toc356330146}[]{#_Toc356831286}[]{#_Toc356330147}[]{#_Toc356831287}[]{#_Toc356330148}[]{#_Toc356831288}[]{#_Toc356330149}[]{#_Toc356831289}[]{#_Toc356330150}[]{#_Toc356831290}[]{#_Toc356330151}[]{#_Toc356831291}[]{#_Toc356330152}[]{#_Toc356831292}[]{#_Toc356330153}[]{#_Toc356831293}[]{#_Toc356330154}[]{#_Toc356831294}[]{#_Toc356330155}[]{#_Toc356831295}[]{#_Toc356330156}[]{#_Toc356831296}[]{#_Toc356330157}[]{#_Toc356831297}[]{#_Toc356330158}[]{#_Toc356831298}[]{#_Toc356330159}[]{#_Toc356831299}[]{#_Toc356330160}[]{#_Toc356831300}[]{#_Toc356330161}[]{#_Toc356831301}[]{#_Toc356330162}[]{#_Toc356831302}[]{#_Toc356330163}[]{#_Toc356831303}[]{#_Toc356330164}[]{#_Toc356831304}[]{#_Toc356330165}[]{#_Toc356831305}[]{#_Toc356330166}[]{#_Toc356831306}[]{#_Toc356330167}[]{#_Toc356831307}[]{#_Toc356330168}[]{#_Toc356831308}[]{#_Toc356330169}[]{#_Toc356831309}[]{#_Toc356330170}[]{#_Toc356831310}[]{#_Toc356330171}[]{#_Toc356831311}[]{#_Toc356330172}[]{#_Toc356831312}[]{#_Toc356330173}[]{#_Toc356831313}[]{#_Toc356330174}[]{#_Toc356831314}[]{#_Toc356330175}[]{#_Toc356831315}[]{#_Toc356330176}[]{#_Toc356831316}[]{#_Toc356330177}[]{#_Toc356831317}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source forcessm**

------------------------------------------------------------------------

[**[network-clock source forcessm]{lang="EN-US"}**]{#struct_0_x4606_33440_x1390190202}[命令用来配置]{style="font-family:
宋体"}[SSM]{lang="EN-US"}[级别的提取方式。]{style="font-family:宋体"}

[**[undo network-clock source forcessm]{lang="EN-US"}**]{#struct_0_x4606_33440_x1229444503}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_633876462}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1946344411}

[**[network-clock source]{lang="EN-US"}**[ { **bits0** \| **bits1** \| **lpuport** *port-type port-number* \| **ptp** } **forcessm** { **on** \| **off** }]{lang="EN-US"}]{#struct_0_x4606_33440_x1234884797}

[**[undo network-clock source]{lang="EN-US"}**[ { **bits0** \| **bits1** \| **lpuport** *port-type port-number* \| **ptp** } **forcessm**]{lang="EN-US"}]{#struct_0_x4606_33440_x67453719}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x549305283}[模式：]{style="font-family:宋体"}

[**[network-clock chassis]{lang="EN-US"}**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **forcessm** { **on** \| **off** }]{lang="EN-US"}]{#struct_0_x4606_33440_1365619507}

[**[network-clock source lpuport]{lang="EN-US"}**[ *port-type port-number* **forcessm** { **on** \| **off** }]{lang="EN-US"}]{#struct_0_x4606_33440_366486349}

[**[undo network-clock chassis]{lang="EN-US"}**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **forcessm**]{lang="EN-US"}]{#struct_0_x4606_33440_x913856597}

[**[undo network-clock source lpuport]{lang="EN-US"}**[ *port-type port-number* **forcessm**]{lang="EN-US"}]{#struct_0_x4606_33440_1680063582}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_438502094}

[[不从时钟源中提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_x899653013}[级别，使用用户自行配置的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_2099824789}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_802889112}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1327940362}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1989817019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x549895107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1377061888}

[**[on]{lang="EN-US"}**]{#struct_0_x4606_33440_x978010228}[：不从时钟源中提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别，使用用户自行配置的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别。]{style="font-family:宋体"}

[**[off]{lang="EN-US"}**]{#struct_0_x4606_33440_1218838941}[：从时钟源中提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别，用户配置的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别无效。]{style="font-family:宋体"}

[**[bits0]{lang="EN-US"}**]{#struct_0_x4606_33440_1948821753}[：]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="EN-US"}**]{#struct_0_x4606_33440_207075180}[：]{style="font-family:宋体"}[BITS1]{lang="EN-US"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[lpuport]{lang="EN-US"}**[ *port-type port-number*]{lang="EN-US"}]{#struct_0_x4606_33440_x61361204}[：指定的线路时钟源，]{style="font-family:宋体"}*[port-type port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[端口类型及端口编号。]{style="font-family:宋体"}

[**[ptp]{lang="EN-US"}**]{#struct_0_x4606_33440_218294700}[：]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议时钟源。]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_1651689337}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_491869450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_2068497236}[时钟源和]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议时钟源只支持在缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中配置，线路时钟源只能在接口对应的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时钟源配置为从时钟源中提取]{style="font-family:宋体"}]{#struct_0_x4606_33440_1529509903}[SSM]{lang="EN-US"}[级别时，用户自行配置的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别将失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x549960643}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_210899374}[配置]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源从该时钟源接收的信号中提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x913661567}

[\[Sysname\] network-clock source bits0 forcessm off]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_2084200006}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源从该时钟源接收的信号中提取]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1750504785}

[\[Sysname\] network-clock chassis 1 source bits0 forcessm off]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x464912387}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_1975192295}
:::

::::: {#1587221138 .myid}
[]{#_Toc404796769}[]{#struct_0_x4606_33440_568530686}[]{#_Toc375382805}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source frequency**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x1764536384}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_554279995}
:::

**[ ]{lang="FR"}**

[**[network-clock source frequency]{lang="FR"}**]{#struct_0_x4606_33440_x1760736018}[命令用来配置传输]{style="font-family:宋体"}[BITS]{lang="FR"}[时钟频率。]{style="font-family:宋体"}

[**[undo network-clock source frequency]{lang="FR"}**]{#struct_0_x4606_33440_x1767583510}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_568596222}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_2129493042}

[**[network-clock source ]{lang="FR"}**]{#struct_0_x4606_33440_721061296}[{ **bits0** \| **bits1** } **frequency** { **bps-2m** \| **hz-2m** }]{lang="FR"}

[**[undo network-clock source ]{lang="FR"}**]{#struct_0_x4606_33440_261292353}[{ **bits0** \| **bits1** } **frequency**]{lang="FR"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x1718445688}[模式：]{style="font-family:宋体"}

[**[network-clock]{lang="EN-US"}**]{#struct_0_x4606_33440_x1945152842}**[ ]{lang="EN-US"}[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}**[ source ]{lang="FR"}**[{ **bits0** \| **bits1** } **frequency** ]{lang="FR"}[{ ]{lang="SV"}**[bps-2m]{lang="EN-US"}**[ \| ]{lang="SV"}**[hz-2m]{lang="EN-US"}**[ ]{lang="EN-US"}[}]{lang="SV"}

[**[undo ]{lang="FR"}[network-clock]{lang="EN-US"}**]{#struct_0_x4606_33440_x415339322}**[ ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[source ]{lang="FR"}**[{ **bits0** \| **bits1** } **frequency**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1752105595}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4606_33440_568661758}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_787989756}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_271213458}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x16725322}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x814449039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x590282021}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1631140938}

[**[chassis ]{lang="SV"}**]{#struct_0_x4606_33440_1267078396}*[chassis-number]{lang="SV"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="SV"}[模式]{style="font-family:宋体"}[）]{style="font-family:
宋体"}

[**[bits0]{lang="SV"}**]{#struct_0_x4606_33440_1263972075}[：]{style="font-family:宋体"}[BITS0]{lang="SV"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="SV"}**]{#struct_0_x4606_33440_673397726}[：]{style="font-family:宋体"}[BITS1]{lang="SV"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[bps-2m]{lang="SV"}**]{#struct_0_x4606_33440_569251582}[：]{style="font-family:宋体"}[BITS]{lang="SV"}[时钟源的频率为]{style="font-family:
宋体"}[2 Mbps]{lang="SV"}[。]{style="font-family:宋体"}

[**[h]{lang="SV"}**]{#struct_0_x4606_33440_1218684384}**[z-2m]{lang="FR"}**[：]{style="font-family:宋体"}[BITS]{lang="SV"}[时钟源的频率为]{style="font-family:宋体"}[2 MHz]{lang="SV"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1987106647}

[[该命令只支持在管理]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x4606_33440_x397188979}[中配置，但配置对所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x929660731}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x1081933417}[配置]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源频率为]{style="font-family:宋体"}[2 MHz]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1006417866}

[\[Sysname\] network-clock source bits0 frequency hz-2m]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x500297226}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源频率为]{style="font-family:宋体"}[2 MHz]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1848029554}

[\[Sysname\] network-clock chassis 1 source bits0 frequency hz-2m]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_2027872304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_x813887603}
:::::

::::: {#-104667694 .myid}
[]{#_Toc404796770}[]{#struct_0_x4606_33440_x1213522409}[]{#_Toc369767192}[]{#_Toc369767866}[]{#_Toc369767890}[]{#_Toc369767975}[]{#_Toc356831319}[]{#_Toc356831320}[]{#_Toc356831321}[]{#_Toc356831322}[]{#_Toc356831323}[]{#_Toc356831324}[]{#_Toc356831325}[]{#_Toc356831326}[]{#_Toc356831327}[]{#_Toc356831328}[]{#_Toc356831329}[]{#_Toc356831330}[]{#_Toc356831331}[]{#_Toc356831332}[]{#_Toc356831333}[]{#_Toc356831334}[]{#_Toc356831335}[]{#_Toc356831336}[]{#_Toc356831337}[]{#_Toc356831338}[]{#_Toc356831339}[]{#_Toc356831340}[]{#_Toc356831341}[]{#_Toc356831342}[]{#_Toc356831343}[]{#_Toc356831344}[]{#_Toc356831345}[]{#_Toc356831346}[]{#_Toc356831347}[]{#_Toc356831348}[]{#_Toc356831349}[]{#_Toc356831350}[]{#_Toc356831351}[]{#_Toc356831352}[]{#_Toc356831353}[]{#_Toc356831354}[]{#_Toc356831355}[]{#_Toc356831356}[]{#_Toc356831357}[]{#_Toc356831358}[]{#_Toc356831359}[]{#_Toc356831360}[]{#_Toc356831361}[]{#_Toc356831362}[]{#_Toc356831363}[]{#_Toc356831364}[]{#_Toc356831365}[]{#_Toc356831366}[]{#_Toc356831367}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source priority**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x360602769}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_609028798}
:::

**[ ]{lang="EN-US"}**

[**[network-clock source priority]{lang="EN-US"}**]{#struct_0_x4606_33440_x2115454755}[命令用来配置参考源的优先级。]{style="font-family:
宋体"}

[**[undo network-clock source priority]{lang="EN-US"}**]{#struct_0_x4606_33440_x1875754092}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_237442632}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1236853934}

[**[network-clock]{lang="EN-US"}**[ **source** { **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **priority** *value*]{lang="EN-US"}]{#struct_0_x4606_33440_369068207}

[**[undo]{lang="EN-US"}**[ **network-clock** **source** { **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **priority**]{lang="EN-US"}]{#struct_0_x4606_33440_1701275453}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x421762249}[模式：]{style="font-family:宋体"}

[**[network-clock chassis]{lang="EN-US"}**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **priority** *value*]{lang="EN-US"}]{#struct_0_x4606_33440_1219619501}

[**[network-clock source lpuport]{lang="EN-US"}**[ *port-type port-number* **priority** *value*]{lang="EN-US"}]{#struct_0_x4606_33440_1618228512}

[**[undo network-clock chassis]{lang="EN-US"}**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **priority**]{lang="EN-US"}]{#struct_0_x4606_33440_x628839873}

[**[undo network-clock source lpuport ]{lang="EN-US"}***[port-type port-number]{lang="EN-US"}***[ priority]{lang="EN-US"}**]{#struct_0_x4606_33440_467409741}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2115520291}

[[所有参考源的优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}]{#struct_0_x4606_33440_x1424290894}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_896166310}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_1229114084}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1112448691}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1265157363}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1169382098}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1413461806}

[**[priority]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x4606_33440_1566281734}[：参考源的优先级，数值越小优先级越高。]{style="font-family:宋体"}

[**[bits0]{lang="EN-US"}**]{#struct_0_x4606_33440_811387047}[：]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="EN-US"}**]{#struct_0_x4606_33440_x1939398727}[：]{style="font-family:宋体"}[BITS1]{lang="EN-US"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ptp]{lang="EN-US"}**]{#struct_0_x4606_33440_x2115585827}[：]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议时钟源。]{style="font-family:宋体"}

[**[lpuport ]{lang="EN-US"}***[port-type port-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x1360617496}[：指定的线路时钟源，]{style="font-family:宋体"}*[port-type port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[端口类型及端口编号。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x609942530}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1249249425}

[[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_x1050911351}[时钟源和]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议时钟源只能在缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中配置，线路时钟源只能在接口对应的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1260794773}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_403206347}[配置]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1602915154}

[\[Sysname\] network-clock source bits0 priority 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x1800067487}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_748026892}

[\[Sysname\] network-clock chassis 1 source bits0 priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2117420844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_x2115651363}
:::::

::: {#560490556 .myid}
[]{#_Toc404796771}[]{#struct_0_x4606_33440_859003482}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source sa-bit**

------------------------------------------------------------------------

[**[network-clock source sa-bit]{lang="EN-US"}**]{#struct_0_x4606_33440_x682212189}[命令用来配置传输]{style="font-family:
宋体"}[BITS]{lang="EN-US"}[时钟源承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位。]{style="font-family:宋体"}

[**[undo network-clock source sa-bit]{lang="EN-US"}**]{#struct_0_x4606_33440_x1272227063}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_394181789}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1966666460}

[**[network-clock source ]{lang="EN-US"}**[{ **bits0** \| **bits1** } **sa-bit** { **sa4** \| **sa5** \| **sa6** \| **sa7** \| **sa8** }]{lang="EN-US"}]{#struct_0_x4606_33440_x349630682}

[**[undo network-clock source ]{lang="EN-US"}**[{ **bits0** \| **bits1** } **sa-bit**]{lang="EN-US"}]{#struct_0_x4606_33440_329912728}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x122108769}[模式：]{style="font-family:宋体"}

[**[network-clock chassis]{lang="EN-US"}**[ *chassis-number* **source** { **bits0** \| **bits1** } **sa-bit** { **sa4** \| **sa5** \| **sa6** \| **sa7** \| **sa8** }]{lang="EN-US"}]{#struct_0_x4606_33440_1542301095}

[**[undo network-clock chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[source ]{lang="EN-US"}**[{ **bits0** \| **bits1** } **sa-bit**]{lang="EN-US"}]{#struct_0_x4606_33440_1391114378}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2115192611}

[[传输]{style="font-family:宋体"}[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_x1267363565}[时钟源承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1651395523}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1663327672}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1476368971}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x55020132}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1077117623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1356209095}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x1191147374}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[sa4]{lang="EN-US"}**]{#struct_0_x4606_33440_961386754}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa4]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[sa5]{lang="EN-US"}**]{#struct_0_x4606_33440_x1748133805}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa5]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[sa6]{lang="EN-US"}**]{#struct_0_x4606_33440_x2115258147}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa6]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[sa7]{lang="EN-US"}**]{#struct_0_x4606_33440_x163828536}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa7]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[sa8]{lang="EN-US"}**]{#struct_0_x4606_33440_1818524913}[：承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的]{style="font-family:宋体"}[s]{lang="EN-US"}[时隙比特位为]{style="font-family:宋体"}[sa8]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[bits0]{lang="EN-US"}**]{#struct_0_x4606_33440_254793455}[：]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="EN-US"}**]{#struct_0_x4606_33440_x1152949348}[：]{style="font-family:宋体"}[BITS1]{lang="EN-US"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1009215944}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只支持在缺省]{style="font-family:宋体"}]{#struct_0_x4606_33440_407829328}[MDC]{lang="EN-US"}[中配置，但配置对所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议本配置在网络中各设备上保持一致。]{style="font-family:宋体"}]{#struct_0_x4606_33440_759370950}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x653749031}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x1546640667}[配置传输]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa5]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1458676245}

[\[Sysname\] network-clock source bits0 sa-bit sa5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x815863566}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上传输]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[承载]{style="font-family:宋体"}[SSM]{lang="EN-US"}[的时隙比特位为]{style="font-family:宋体"}[sa5]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x2115323683}

[\[Sysname\] network-clock chassis 1 source bits0 sa-bit sa5]{lang="EN-US"}
:::

::::: {#-109419755 .myid}
[]{#_Toc404796772}[]{#struct_0_x4606_33440_x383519508}[]{#_Toc369767195}[]{#_Toc369767869}[]{#_Toc369767893}[]{#_Toc369767978}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source ssm**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x794094450}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_2016540585}
:::

**[ ]{lang="EN-US"}**

[**[network-clock source ssm]{lang="EN-US"}**]{#struct_0_x4606_33440_361232575}[命令用来配置各参考源的]{style="font-family:
宋体"}[SSM]{lang="EN-US"}[级别。]{style="font-family:宋体"}

[**[undo network-clock source ssm]{lang="EN-US"}**]{#struct_0_x4606_33440_x2142676467}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_774612230}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_605962490}

[**[network-clock source ]{lang="EN-US"}**[{ **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **ssm** { **dnu** \| **prc** \| **sec** \| **ssua** \| **ssub** \| **unknown** }]{lang="EN-US"}]{#struct_0_x4606_33440_x763087878}

[**[undo]{lang="EN-US"}**[ **network-clock source** { **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **ssm**]{lang="EN-US"}]{#struct_0_x4606_33440_x568897381}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x924233204}[模式：]{style="font-family:宋体"}

[**[network-clock chassis]{lang="EN-US"}**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **ssm** { **dnu** \| **prc** \| **sec** \| **ssua** \| **ssub** \| **unknown** }]{lang="EN-US"}]{#struct_0_x4606_33440_x2115389219}

[**[network-clock source lpuport]{lang="EN-US"}***[ port-type port-number]{lang="EN-US"}***[ ssm]{lang="EN-US"}**[ { **dnu** \| **prc** \| **sec** \| **ssua** \| **ssub** \| **unknown** }]{lang="EN-US"}]{#struct_0_x4606_33440_x1974683992}

[**[undo network-clock chassis]{lang="EN-US"}**[ *chassis-numb*er **source** { **bits0** \| **bits1** \| **ptp** } **ssm**]{lang="EN-US"}]{#struct_0_x4606_33440_2004971882}

[**[undo network-clock source lpuport]{lang="EN-US"}**[ *port-type port-number* **ssm**]{lang="EN-US"}]{#struct_0_x4606_33440_1174506163}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1769336832}

[[所有参考源的]{style="font-family:宋体"}[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_867241869}[级别为]{style="font-family:宋体"}**[unknown]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x988436150}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1386271197}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1522165539}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_934532592}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_679740466}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2115979043}

[**[dnu]{lang="EN-US"}**]{#struct_0_x4606_33440_x127502343}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[DNU]{lang="EN-US"}[（不应用作同步）。]{style="font-family:宋体"}

[**[ssub]{lang="EN-US"}**]{#struct_0_x4606_33440_x1008473485}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[SSU-B]{lang="EN-US"}[（]{style="font-family:宋体"}[G.812]{lang="EN-US"}[本地节点时钟信号）。]{style="font-family:宋体"}

[**[prc]{lang="EN-US"}**]{#struct_0_x4606_33440_x1364319029}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[PRC]{lang="EN-US"}[（]{style="font-family:宋体"}[G.811]{lang="EN-US"}[时钟信号）。]{style="font-family:宋体"}

[**[sec]{lang="EN-US"}**]{#struct_0_x4606_33440_151394567}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[SEC]{lang="EN-US"}[（]{style="font-family:宋体"}[SDH]{lang="EN-US"}[设备时钟源信号）。]{style="font-family:宋体"}

[**[ssua]{lang="EN-US"}**]{#struct_0_x4606_33440_1299603923}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[SSU-A]{lang="EN-US"}[（]{style="font-family:宋体"}[G.812]{lang="EN-US"}[转接节点时钟信号）。]{style="font-family:宋体"}

[**[unknown]{lang="EN-US"}**]{#struct_0_x4606_33440_654506648}[：]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[（时钟源的同步质量未知）。]{style="font-family:宋体"}

[**[bits0]{lang="EN-US"}**]{#struct_0_x4606_33440_1295280822}[：]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="EN-US"}**]{#struct_0_x4606_33440_x1351919379}[：]{style="font-family:宋体"}[BITS1]{lang="EN-US"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ptp]{lang="EN-US"}**]{#struct_0_x4606_33440_253630595}[：]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议时钟源。]{style="font-family:宋体"}

[**[lpuport ]{lang="EN-US"}***[port-type port-number]{lang="EN-US"}*]{#struct_0_x4606_33440_830914796}[：指定的线路时钟源，]{style="font-family:宋体"}*[port-type port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[端口类型及端口编号。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_80386921}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2116044579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于线路时钟源，配置的]{style="font-family:宋体"}]{#struct_0_x4606_33440_x2081515742}[SSM]{lang="EN-US"}[级别为该时钟源的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BITS]{lang="EN-US"}]{#struct_0_x4606_33440_624944016}[时钟源和]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议时钟源只能在缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中配置，线路时钟源只能在接口对应的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[时钟源已配置从时钟源中提取]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1417861677}[SSM]{lang="EN-US"}[级别时，用户自行配置的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置参考源的]{lang="EN-US" style="font-family:宋体"}[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_1960509657}[级别后设备响应需要一定时间，可通过]{lang="EN-US" style="font-family:宋体"}**[display network-clock source]{lang="EN-US"}**[命令和日志信息查看配置是否生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_119087849}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_1972417236}[配置]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[DNU]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_1609268107}

[\[Sysname\] network-clock source bits0 ssm dnu]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x757610237}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别为]{style="font-family:宋体"}[DNU]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_754578121}

[\[Sysname\] network-clock chassis 1 source bits0 ssm dnu]{lang="EN-US"}
:::::

::: {#1546376457 .myid}
[]{#_Toc404796773}[]{#struct_0_x4606_33440_x2115454756}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock ssmcontrol**

------------------------------------------------------------------------

[**[network-clock ssmcontrol]{lang="EN-US"}**]{#struct_0_x4606_33440_2015928677}[命令用来配置]{style="font-family:
宋体"}[SSM]{lang="EN-US"}[级别是否参与控制。]{style="font-family:宋体"}

[**[undo network-clock ssmcontrol]{lang="EN-US"}**]{#struct_0_x4606_33440_x717644756}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_539534671}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x38522621}

[**[network-clock ssmcontrol]{lang="EN-US"}**[ { **on** \| **off** }]{lang="EN-US"}]{#struct_0_x4606_33440_218508669}

[**[undo network-clock ssmcontrol]{lang="EN-US"}**]{#struct_0_x4606_33440_1112953888}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x324032971}[模式：]{style="font-family:宋体"}

[**[network-clock chassis]{lang="EN-US"}**[ *chassis-number* **ssmcontrol** { **on** \| **off** }]{lang="EN-US"}]{#struct_0_x4606_33440_1316612519}

[**[undo network-clock chassis]{lang="EN-US"}**[ *chassis-number* **ssmcontrol**]{lang="EN-US"}]{#struct_0_x4606_33440_x1151001684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_832784596}

[[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_6549666}[级别不参与控制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2115520292}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_1304592461}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x782157301}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x351690185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1735200045}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1723697824}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_47154256}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[on]{lang="EN-US"}**]{#struct_0_x4606_33440_x1895083366}[：配置]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别参与控制。]{style="font-family:宋体"}

[**[off]{lang="EN-US"}**]{#struct_0_x4606_33440_1221194765}[：配置]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别不参与控制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x957128361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_x293497128}[级别参与控制：时钟源在自动工作模式时，将首先按照参考源的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别确定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSM]{lang="EN-US"}]{#struct_0_x4606_33440_x2115585828}[级别不参与控制：用户可以配置和查看]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别，但是在自动切换时钟源时，参考源的]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别被忽略，直接按照参考源的优先级来确定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只支持在缺省]{style="font-family:宋体"}]{#struct_0_x4606_33440_x957332969}[MDC]{lang="EN-US"}[中配置，但配置对所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_101583096}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x1795226589}[配置时钟监控]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别参与控制。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1013665041}

[\[Sysname\] network-clock ssmcontrol on]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_1670592909}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的时钟监控]{style="font-family:宋体"}[SSM]{lang="EN-US"}[级别参与控制。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_1437736345}

[\[Sysname\] network-clock chassis 1 ssmcontrol on]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2112279672}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_x1670124533}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network-clock ssm]{lang="EN-US"}**]{#struct_0_x4606_33440_x1471555134}
:::

::: {#-194576823 .myid}
[]{#_Toc404796774}[]{#struct_0_x4606_33440_x2115651364}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock work-mode**

------------------------------------------------------------------------

[**[network-clock work-mode]{lang="EN-US"}**]{#struct_0_x4606_33440_455718955}[命令用来配置时钟监控的工作模式，即时钟源的选择模式。]{style="font-family:宋体"}

[**[undo network-clock work-mode]{lang="EN-US"}**]{#struct_0_x4606_33440_84492262}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1852995906}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1030413539}

[**[network-clock work-mode ]{lang="EN-US"}**[{ **auto** \| **manual source** { **bits0** \| **bits1** \| **lpuport** *port-type port-number* } }]{lang="EN-US"}]{#struct_0_x4606_33440_481593651}

[**[undo network-clock work-mode]{lang="EN-US"}**]{#struct_0_x4606_33440_x2131634162}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_1686621253}[模式：]{style="font-family:宋体"}

[**[network-clock chassis]{lang="EN-US"}**[ *chassis-number* **work-mode** { **auto** \| **manual source** { **bits0** \| **bits1** } }]{lang="EN-US"}]{#struct_0_x4606_33440_1204284359}

[**[network-clock work-mode manual source lpuport ]{lang="EN-US"}***[port-type port-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x182520165}

[**[undo network-clock chassis]{lang="EN-US"}**[ *chassis-number* **work-mode**]{lang="EN-US"}]{#struct_0_x4606_33440_114574541}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1155851685}

[[时钟监控的工作模式为自动模式。]{style="font-family:宋体"}]{#struct_0_x4606_33440_x2115192612}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1670648092}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_512426414}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x496414546}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_667941013}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x670886246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1729315168}

[**[auto]{lang="EN-US"}**]{#struct_0_x4606_33440_801066403}[：配置时钟监控的工作模式为自动模式。]{style="font-family:宋体"}

[**[manual source]{lang="EN-US"}**]{#struct_0_x4606_33440_x1226968869}[：配置时钟监控手动模式的时钟源。]{style="font-family:宋体"}

[**[bits0]{lang="EN-US"}**]{#struct_0_x4606_33440_x1903440422}[：配置手动模式下参考时钟为]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源。]{style="font-family:宋体"}

[**[bits1]{lang="EN-US"}**]{#struct_0_x4606_33440_x796342065}[：配置手动模式下参考时钟为]{style="font-family:宋体"}[BITS1]{lang="EN-US"}[时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[lpuport]{lang="EN-US"}**[ *port-type port-number*]{lang="EN-US"}]{#struct_0_x4606_33440_x2115258148}[：配置手动模式下主用时钟源为线路时钟源，]{style="font-family:宋体"}*[port-type port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[端口类型及端口编号。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_x1279573783}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1950475064}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手动模式指定线路时钟源时，只能在接口对应的]{style="font-family:宋体"}]{#struct_0_x4606_33440_x280437372}[MDC]{lang="EN-US"}[中配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若配置手动模式下主用时钟源为线路时钟源，该线路时钟源的输入端口必须同时为]{style="font-family:宋体"}]{#struct_0_x4606_33440_x873487680}**[network-clock lpuport]{lang="EN-US"}**[命令指定的线路时钟源输入端口，配置才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置时钟监控的工作模式后设备响应需要一定时间，可通过]{lang="EN-US" style="font-family:宋体"}**[display network-clock status]{lang="EN-US"}**]{#struct_0_x4606_33440_x1677047410}[命令和日志信息查看配置是否生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1362827643}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_58426117}[配置时钟监控的工作模式为手动模式，主用时钟源为]{style="font-family:宋体"}[BITS0]{lang="EN-US"}[时钟源。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x839276490}

[\[Sysname\] network-clock work-mode manual source bits0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_1225062578}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的时钟监控的工作模式为自动模式。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x65921765}

[\[Sysname\] network-clock chassis 1 work-mode auto]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2115323684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock source]{lang="EN-US"}**]{#struct_0_x4606_33440_1989133487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock status]{lang="EN-US"}**]{#struct_0_x4606_33440_992740016}
:::

::::: {#1550834690 .myid}
[]{#_Toc404796775}[]{#struct_0_x4606_33440_x1290252030}

**时钟监控 \-- 时钟监控配置命令 \-- network-clock work-mode manual mdc**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_1007008564}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_x1704933176}
:::

[ ]{lang="EN-US"}

[**[network-clock work-mode manual mdc]{lang="EN-US"}**]{#struct_0_x4606_33440_x823846700}[命令用来配置手动模式下指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的时钟源有效。]{style="font-family:宋体"}

[**[undo network-clock work-mode manual mdc]{lang="EN-US"}**]{#struct_0_x4606_33440_1888753830}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1591147911}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1039997119}

[**[network-clock work-mode manual mdc ]{lang="EN-US"}***[mdc-id]{lang="EN-US"}*]{#struct_0_x4606_33440_707507748}

[**[undo network-clock work-mode manual mdc]{lang="EN-US"}**]{#struct_0_x4606_33440_x1553636720}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4606_33440_x2115389220}[模式：]{style="font-family:宋体"}

[**[network-clock chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ work-mode manual mdc ]{lang="EN-US"}***[mdc-id]{lang="EN-US"}*]{#struct_0_x4606_33440_x52304155}

[**[undo network-clock chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ work-mode manual mdc]{lang="EN-US"}**]{#struct_0_x4606_33440_889156875}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1505152276}

[[缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x4606_33440_x498910567}[下配置的手动配置生效。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1706108548}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1214986074}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_79174325}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1981156200}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_324100233}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_703877659}

[**[mdc]{lang="EN-US"}***[ mdc-id]{lang="EN-US"}*]{#struct_0_x4606_33440_x2115979044}[：表示手动模式下指定的非缺省]{style="font-family:宋体"}[MDC ID]{lang="EN-US"}[号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x4606_33440_1438581598}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_413114342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只支持在缺省]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1292143532}[MDC]{lang="EN-US"}[中配置，但配置对所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在手工指定非缺省]{style="font-family:宋体"}]{#struct_0_x4606_33440_1553572736}[MDC]{lang="EN-US"}[时钟源时，请使用]{style="font-family:宋体"}**[display network-clock source]{lang="EN-US"}**[命令查看时钟源的状态，只有该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[内的所有框上有可以正常工作的参考源，该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[才能配置为主用时钟源。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置主控板时钟监控的工作模式后设备响应需要一定时间。]{style="font-family:宋体"}]{#struct_0_x4606_33440_1932999480}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x2088352711}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x463576490}[配置手动模式下]{style="font-family:宋体"}[MDC 2]{lang="EN-US"}[的时钟源有效。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x665723696}

[\[Sysname\] network-clock work-mode manual mdc 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_246579006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display network-clock status]{lang="EN-US"}**]{#struct_0_x4606_33440_x376617166}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network-clock work-mode]{lang="EN-US"}**]{#struct_0_x4606_33440_x2116044580}[]{#_Toc355809802}[]{#_Toc356062933}[]{#_Toc356330186}[]{#_Toc356831374}[]{#_Toc355809803}[]{#_Toc356062934}[]{#_Toc356330187}[]{#_Toc356831375}[]{#_Toc355809804}[]{#_Toc356062935}[]{#_Toc356330188}[]{#_Toc356831376}[]{#_Toc355809805}[]{#_Toc356062936}[]{#_Toc356330189}[]{#_Toc356831377}[]{#_Toc355809806}[]{#_Toc356062937}[]{#_Toc356330190}[]{#_Toc356831378}[]{#_Toc355809807}[]{#_Toc356062938}[]{#_Toc356330191}[]{#_Toc356831379}[]{#_Toc355809808}[]{#_Toc356062939}[]{#_Toc356330192}[]{#_Toc356831380}[]{#_Toc355809809}[]{#_Toc356062940}[]{#_Toc356330193}[]{#_Toc356831381}[]{#_Toc355809810}[]{#_Toc356062941}[]{#_Toc356330194}[]{#_Toc356831382}[]{#_Toc355809811}[]{#_Toc356062942}[]{#_Toc356330195}[]{#_Toc356831383}[]{#_Toc355809812}[]{#_Toc356062943}[]{#_Toc356330196}[]{#_Toc356831384}[]{#_Toc355809813}[]{#_Toc356062944}[]{#_Toc356330197}[]{#_Toc356831385}[]{#_Toc355809814}[]{#_Toc356062945}[]{#_Toc356330198}[]{#_Toc356831386}[]{#_Toc355809815}[]{#_Toc356062946}[]{#_Toc356330199}[]{#_Toc356831387}[]{#_Toc355809816}[]{#_Toc356062947}[]{#_Toc356330200}[]{#_Toc356831388}[]{#_Toc355809817}[]{#_Toc356062948}[]{#_Toc356330201}[]{#_Toc356831389}[]{#_Toc355809818}[]{#_Toc356062949}[]{#_Toc356330202}[]{#_Toc356831390}[]{#_Toc355809819}[]{#_Toc356062950}[]{#_Toc356330203}[]{#_Toc356831391}[]{#_Toc355809820}[]{#_Toc356062951}[]{#_Toc356330204}[]{#_Toc356831392}[]{#_Toc355809821}[]{#_Toc356062952}[]{#_Toc356330205}[]{#_Toc356831393}[]{#_Toc355809822}[]{#_Toc356062953}[]{#_Toc356330206}[]{#_Toc356831394}[]{#_Toc355809823}[]{#_Toc356062954}[]{#_Toc356330207}[]{#_Toc356831395}[]{#_Toc355809824}[]{#_Toc356062955}[]{#_Toc356330208}[]{#_Toc356831396}[]{#_Toc355809825}[]{#_Toc356062956}[]{#_Toc356330209}[]{#_Toc356831397}[]{#_Toc355809826}[]{#_Toc356062957}[]{#_Toc356330210}[]{#_Toc356831398}[]{#_Toc355809827}[]{#_Toc356062958}[]{#_Toc356330211}[]{#_Toc356831399}[]{#_Toc355809828}[]{#_Toc356062959}[]{#_Toc356330212}[]{#_Toc356831400}[]{#_Toc355809829}[]{#_Toc356062960}[]{#_Toc356330213}[]{#_Toc356831401}[]{#_Toc355809830}[]{#_Toc356062961}[]{#_Toc356330214}[]{#_Toc356831402}[]{#_Toc355809831}[]{#_Toc356062962}[]{#_Toc356330215}[]{#_Toc356831403}[]{#_Toc355809832}[]{#_Toc356062963}[]{#_Toc356330216}[]{#_Toc356831404}[]{#_Toc355809833}[]{#_Toc356062964}[]{#_Toc356330217}[]{#_Toc356831405}[]{#_Toc355809834}[]{#_Toc356062965}[]{#_Toc356330218}[]{#_Toc356831406}[]{#_Toc355809835}[]{#_Toc356062966}[]{#_Toc356330219}[]{#_Toc356831407}[]{#_Toc355809836}[]{#_Toc356062967}[]{#_Toc356330220}[]{#_Toc356831408}[]{#_Toc355809837}[]{#_Toc356062968}[]{#_Toc356330221}[]{#_Toc356831409}[]{#_Toc355809838}[]{#_Toc356062969}[]{#_Toc356330222}[]{#_Toc356831410}[]{#_Toc355809839}[]{#_Toc356062970}[]{#_Toc356330223}[]{#_Toc356831411}[]{#_Toc355809840}[]{#_Toc356062971}[]{#_Toc356330224}[]{#_Toc356831412}[]{#_Toc355809841}[]{#_Toc356062972}[]{#_Toc356330225}[]{#_Toc356831413}[]{#_Toc355809842}[]{#_Toc356062973}[]{#_Toc356330226}[]{#_Toc356831414}[]{#_Toc355809843}[]{#_Toc356062974}[]{#_Toc356330227}[]{#_Toc356831415}[]{#_Toc355809844}[]{#_Toc356062975}[]{#_Toc356330228}[]{#_Toc356831416}[]{#_Toc355809845}[]{#_Toc356062976}[]{#_Toc356330229}[]{#_Toc356831417}[]{#_Toc355809846}[]{#_Toc356062977}[]{#_Toc356330230}[]{#_Toc356831418}[]{#_Toc355809847}[]{#_Toc356062978}[]{#_Toc356330231}[]{#_Toc356831419}[]{#_Toc355809848}[]{#_Toc356062979}[]{#_Toc356330232}[]{#_Toc356831420}[]{#_Toc355809849}[]{#_Toc356062980}[]{#_Toc356330233}[]{#_Toc356831421}[]{#_Toc355809850}[]{#_Toc356062981}[]{#_Toc356330234}[]{#_Toc356831422}[]{#_Toc355809851}[]{#_Toc356062982}[]{#_Toc356330235}[]{#_Toc356831423}[]{#_Toc355809852}[]{#_Toc356062983}[]{#_Toc356330236}[]{#_Toc356831424}[]{#_Toc355809853}[]{#_Toc356062984}[]{#_Toc356330237}[]{#_Toc356831425}[]{#_Toc355809854}[]{#_Toc356062985}[]{#_Toc356330238}[]{#_Toc356831426}[]{#_Toc355809855}[]{#_Toc356062986}[]{#_Toc356330239}[]{#_Toc356831427}[]{#_Toc355809856}[]{#_Toc356062987}[]{#_Toc356330240}[]{#_Toc356831428}[]{#_Toc355809857}[]{#_Toc356062988}[]{#_Toc356330241}[]{#_Toc356831429}[]{#_Toc355809858}[]{#_Toc356062989}[]{#_Toc356330242}[]{#_Toc356831430}[]{#_Toc355809859}[]{#_Toc356062990}[]{#_Toc356330243}[]{#_Toc356831431}[]{#_Toc348872399}[]{#_Toc349133060}[]{#_Toc348872400}[]{#_Toc349133061}[]{#_Toc348872401}[]{#_Toc349133062}[]{#_Toc348872402}[]{#_Toc349133063}[]{#_Toc348872403}[]{#_Toc349133064}[]{#_Toc348872404}[]{#_Toc349133065}[]{#_Toc348872405}[]{#_Toc349133066}[]{#_Toc348872406}[]{#_Toc349133067}[]{#_Toc348872407}[]{#_Toc349133068}[]{#_Toc348872408}[]{#_Toc349133069}[]{#_Toc348872409}[]{#_Toc349133070}[]{#_Toc348872410}[]{#_Toc349133071}[]{#_Toc348872411}[]{#_Toc349133072}[]{#_Toc348872412}[]{#_Toc349133073}[]{#_Toc348872413}[]{#_Toc349133074}[]{#_Toc348872414}[]{#_Toc349133075}[]{#_Toc348872415}[]{#_Toc349133076}[]{#_Toc348872416}[]{#_Toc349133077}[]{#_Toc348872417}[]{#_Toc349133078}[]{#_Toc348872418}[]{#_Toc349133079}[]{#_Toc348872419}[]{#_Toc349133080}[]{#_Toc348872420}[]{#_Toc349133081}[]{#_Toc348872421}[]{#_Toc349133082}[]{#_Toc348872422}[]{#_Toc349133083}[]{#_Toc348872423}[]{#_Toc349133084}[]{#_Toc348872424}[]{#_Toc349133085}[]{#_Toc348872425}[]{#_Toc349133086}[]{#_Toc348872426}[]{#_Toc349133087}[]{#_Toc348872427}[]{#_Toc349133088}[]{#_Toc348872428}[]{#_Toc349133089}[]{#_Toc348872429}[]{#_Toc349133090}[]{#_Toc348872430}[]{#_Toc349133091}[]{#_Toc348872431}[]{#_Toc349133092}[]{#_Toc348872432}[]{#_Toc349133093}[]{#_Toc348872433}[]{#_Toc349133094}[]{#_Toc348872434}[]{#_Toc349133095}[]{#_Toc348872435}[]{#_Toc349133096}[]{#_Toc348872436}[]{#_Toc349133097}[]{#_Toc348872437}[]{#_Toc349133098}[]{#_Toc348872438}[]{#_Toc349133099}[]{#_Toc348872439}[]{#_Toc349133100}[]{#_Toc348872440}[]{#_Toc349133101}[]{#_Toc348872441}[]{#_Toc349133102}[]{#_Toc348872442}[]{#_Toc349133103}[]{#_Toc348872447}[]{#_Toc349133108}
:::::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#233562051 .myid}
[]{#_Toc404796778}[]{#struct_0_x4606_33440_1609307332}[]{#_Toc378496430}

**同步以太网 \-- 同步以太网配置命令 \-- display esmc**

------------------------------------------------------------------------

[**[display esmc]{lang="EN-US"}**]{#struct_0_x4606_33440_x1147698726}[命令用来显示接口上的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1959533751}

[**[display esmc ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x4606_33440_353552026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1684016383}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4606_33440_938172575}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_471325733}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1166238971}

[[network-operator]{lang="EN-US"}]{#struct_0_x4606_33440_x347885769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1320596479}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4606_33440_1165052418}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1630354689}

[**[interface]{lang="EN-US"}***[ interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x4606_33440_1609241796}[：显示指定接口上的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。如未指定本参数，将显示所有接口的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1228708031}

[[如果接口工作在非同步模式，则该接口的]{style="font-family:宋体"}]{#struct_0_x4606_33440_787077210}[ESMC]{lang="EN-US"}[信息显示为空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x394198030}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x1176993591}[显示所有接口的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display esmc]{lang="EN-US"}]{#struct_0_x4606_33440_x349049018}

[Interface   : GigabitEthernet1/0/1]{lang="EN-US"}

[Mode        : Synchronous]{lang="EN-US"}

[ESMC status : Enable]{lang="EN-US"}

[Port status : Up]{lang="EN-US"}

[Duplex mode : Full]{lang="EN-US"}

[QL received : QL-SEC]{lang="EN-US"}

[QL sent     : QL-PRC]{lang="EN-US"}

[ESMC information packets received : 2195]{lang="EN-US"}

[ESMC information packets sent     : 6034]{lang="EN-US"}

[ESMC event packets received       : 1]{lang="EN-US"}

[ESMC event packets sent           : 16]{lang="EN-US"}

[ESMC information rate             : 1 packets/sec]{lang="EN-US"}

[ESMC expiration                   : 5 seconds]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display esmc]{lang="EN-US"}]{#struct_0_x4606_33440_x478926372}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_811016448}[[字段]{style="font-family:黑体"}]{#struct_0_x4606_33440_1609176260}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1527116538}

[[Mode]{lang="EN-US"}]{#struct_0_x4606_33440_1609110724}

[[以太网接口工作模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x1511513140}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Synchronous]{lang="EN-US"}]{#struct_0_x4606_33440_1609045188}[：同步模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-Synchronous]{lang="EN-US"}]{#struct_0_x4606_33440_x359240984}[：非同步模式（]{lang="EN-US" style="font-family:
  宋体"}[不显示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[ESMC]{lang="EN-US"}[信息）]{lang="EN-US" style="font-family:宋体"}

[[ESMC status]{lang="EN-US"}]{#struct_0_x4606_33440_1225847263}

[[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1608979652}[报文收发处理是否使能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x4606_33440_x1918026696}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x4606_33440_1608914116}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Port status]{lang="EN-US"}]{#struct_0_x4606_33440_794621229}

[[接口状态：]{style="font-family:宋体"}]{#struct_0_x4606_33440_1608848580}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x4606_33440_x1928345663}[：表示接口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4606_33440_x1707065783}[：表示接口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[Duplex mode]{lang="EN-US"}]{#struct_0_x4606_33440_1609831620}

[[以太网接口的双工模式：]{style="font-family:宋体"}]{#struct_0_x4606_33440_x734357634}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Full]{lang="EN-US"}]{#struct_0_x4606_33440_1609766084}[：接口处于全双工状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Half]{lang="EN-US"}]{#struct_0_x4606_33440_x1907159866}[：接口处于半双工状态]{style="font-family:宋体"}

[[QL received]{lang="EN-US"}]{#struct_0_x4606_33440_1609307331}

[[接收到的]{style="font-family:宋体"}[QL]{lang="EN-US"}]{#struct_0_x4606_33440_x1147895334}[值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRC]{lang="EN-US"}]{#struct_0_x4606_33440_1609241795}[：]{style="font-family:宋体"}[G.811]{lang="EN-US"}[时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-A]{lang="EN-US"}]{#struct_0_x4606_33440_1228511423}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[转接节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-B]{lang="EN-US"}]{#struct_0_x4606_33440_x1901942826}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[本地节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SEC]{lang="EN-US"}]{#struct_0_x4606_33440_1609176259}[：]{style="font-family:宋体"}[SDH]{lang="EN-US"}[设备时钟源信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNU]{lang="EN-US"}]{#struct_0_x4606_33440_x1527575293}[：不应用作同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNK]{lang="EN-US"}]{#struct_0_x4606_33440_1609110723}[：同步质量未知]{style="font-family:宋体"}

[[QL sent]{lang="EN-US"}]{#struct_0_x4606_33440_x1511316532}

[[发送的]{style="font-family:宋体"}[QL]{lang="EN-US"}]{#struct_0_x4606_33440_1609045187}[值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRC]{lang="EN-US"}]{#struct_0_x4606_33440_x358389016}[：]{style="font-family:宋体"}[G.811]{lang="EN-US"}[时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-A]{lang="EN-US"}]{#struct_0_x4606_33440_1608979651}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[转接节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSU-B]{lang="EN-US"}]{#struct_0_x4606_33440_x1918092232}[：]{style="font-family:宋体"}[G.812]{lang="EN-US"}[本地节点时钟信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SEC]{lang="EN-US"}]{#struct_0_x4606_33440_1608914115}[：]{style="font-family:宋体"}[SDH]{lang="EN-US"}[设备时钟源信号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNU]{lang="EN-US"}]{#struct_0_x4606_33440_794817837}[：不应用作同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNK]{lang="EN-US"}]{#struct_0_x4606_33440_1608848579}[：同步质量未知]{style="font-family:宋体"}

[[ESMC information packets received]{lang="EN-US"}]{#struct_0_x4606_33440_x1928935488}

[[接收的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1609831619}[信息报文数目]{style="font-family:宋体"}

[[ESMC information packets sent]{lang="EN-US"}]{#struct_0_x4606_33440_x734816387}

[[发送的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1609766083}[信息报文数目]{style="font-family:宋体"}

[[ESMC event packets received]{lang="EN-US"}]{#struct_0_x4606_33440_x1907618618}

[[接收的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1609307338}[事件报文数目]{style="font-family:宋体"}

[[ESMC event packets sent]{lang="EN-US"}]{#struct_0_x4606_33440_x1147305510}

[[发送的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1609241802}[事件报文数目]{style="font-family:宋体"}

[[ESMC information rate]{lang="EN-US"}]{#struct_0_x4606_33440_1183815878}

[[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1609176266}[信息报文发包频率，固定为]{style="font-family:宋体"}[1 packets/sec]{lang="EN-US"}

[[ESMC expiration]{lang="EN-US"}]{#struct_0_x4606_33440_x1527247610}

[[接收]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1609110730}[报文的超时时间，固定为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1511250997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[esmc enable]{lang="EN-US"}**]{#struct_0_x4606_33440_x1983224552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[synchronous mode]{lang="EN-US"}**]{#struct_0_x4606_33440_x943063366}

::: {#-645986150 .myid}
[]{#_Toc404796779}[]{#struct_0_x4606_33440_x931488819}[]{#_Toc378496431}[]{#_Toc350843567}[]{#_Toc339901008}[]{#_Toc374609496}

**同步以太网 \-- 同步以太网配置命令 \-- esmc enable**

------------------------------------------------------------------------

[**[esmc enable]{lang="EN-US"}**]{#struct_0_x4606_33440_389580650}[命令用来使能当前接口的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo esmc enable]{lang="EN-US"}**]{#struct_0_x4606_33440_424753145}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1609045194}

[**[esmc enable]{lang="EN-US"}**]{#struct_0_x4606_33440_x358454551}

[**[undo esmc enable]{lang="EN-US"}**]{#struct_0_x4606_33440_493363232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_260762134}

[[接口上]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_622758985}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_915877636}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4606_33440_x156203236}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1573164051}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1488255146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1653346223}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1250388367}

[[必须先配置以太网接口的工作模式为同步模式后，才能使能]{style="font-family:宋体"}[ESMC]{lang="EN-US"}]{#struct_0_x4606_33440_1608979658}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1918682056}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x163632416}[使能接口]{style="font-family:宋体"}[GigabitEthernet1/01]{lang="EN-US"}[的]{style="font-family:宋体"}[ESMC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_1375144635}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] esmc enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_64685907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display esmc]{lang="EN-US"}**]{#struct_0_x4606_33440_789070629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[synchronous mode]{lang="EN-US"}**]{#struct_0_x4606_33440_296822673}
:::

::::: {#58811080 .myid}
[]{#_Toc404796780}[]{#struct_0_x4606_33440_568727289}[]{#_Toc385838832}[]{#_Toc383522352}

**同步以太网 \-- 同步以太网配置命令 \-- synce state**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](时钟同步命令.files/image001.png){#图片 36 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4606_33440_x748520062}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4606_33440_x351137484}
:::

[ ]{lang="EN-US"}

[**[synce state]{lang="EN-US"}**]{#struct_0_x4606_33440_x2072591935}[命令用来配置]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口的端口模式为]{style="font-family:宋体"}[Master]{lang="EN-US"}[或者]{style="font-family:宋体"}[Slave]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo synce state]{lang="EN-US"}**]{#struct_0_x4606_33440_x94160369}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1146461436}

[**[synce state ]{lang="EN-US"}**[{ **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x4606_33440_568792825}

[**[undo synce state]{lang="EN-US"}**]{#struct_0_x4606_33440_x1864449911}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1168927996}

[[GE]{lang="EN-US"}]{#struct_0_x4606_33440_1328489256}[电口将采用自动协商的方式决定其端口模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1387967286}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4606_33440_x289215887}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_2043513671}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_1888142046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x1559065055}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1257554609}

[**[master]{lang="EN-US"}**]{#struct_0_x4606_33440_568858361}[：]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口的端口模式为]{style="font-family:宋体"}[Master]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x4606_33440_x914361802}[：]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口的端口模式为]{style="font-family:宋体"}[Slave]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1612275105}

[[在同步以太网中，]{style="font-family:宋体"}[GE]{lang="EN-US"}]{#struct_0_x4606_33440_x1750768841}[电口的端口模式与其同步时钟的方向关联。如果]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口需要向下游同步时钟，则其端口模式需要配置成]{style="font-family:宋体"}[Master]{lang="EN-US"}[；如果]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口需要从上游同步时钟，则其端口模式需要配置成]{style="font-family:宋体"}[Slave]{lang="EN-US"}[。如果未配置端口模式，]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口将采用自动协商的方式决定其端口模式（]{style="font-family:宋体"}[Master]{lang="EN-US"}[端口使用本设备的时钟，]{style="font-family:宋体"}[Slave]{lang="EN-US"}[端口从线路上提取时钟），此时协商出的主从关系和网络管理员规划的主从关系可能会相互冲突，造成设备间时钟同步错误。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1691239322}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_1169104812}[配置]{style="font-family:宋体"}[GE]{lang="EN-US"}[电口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的端口模式为]{style="font-family:宋体"}[Master]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_143074842}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] synce state master]{lang="EN-US"}
:::::

::: {#-1471398839 .myid}
[]{#_Toc404796781}[]{#struct_0_x4606_33440_687211178}[]{#_Toc378496432}

**同步以太网 \-- 同步以太网配置命令 \-- synchronous mode**

------------------------------------------------------------------------

[**[synchronous mode]{lang="EN-US"}**]{#struct_0_x4606_33440_x92495218}[命令用来配置当前接口的工作模式为同步模式。]{style="font-family:宋体"}

[**[undo synchronous mode]{lang="EN-US"}**]{#struct_0_x4606_33440_x807736581}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x401089853}

[**[synchronous mode]{lang="EN-US"}**]{#struct_0_x4606_33440_1608914122}

[**[undo synchronous mode]{lang="EN-US"}**]{#struct_0_x4606_33440_794883376}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x954943809}

[[接口的工作模式为非同步模式。]{style="font-family:宋体"}]{#struct_0_x4606_33440_x117992163}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1388975674}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4606_33440_x698354999}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1895757894}

[[network-admin]{lang="EN-US"}]{#struct_0_x4606_33440_2030292192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4606_33440_x336531049}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x1812107811}

[[只有当接口的工作模式为同步模式时，该接口才能有可能作为本设备的线路时钟源参与时钟源选择。]{style="font-family:宋体"}]{#struct_0_x4606_33440_52537334}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4606_33440_1608848586}

[[\# ]{lang="EN-US"}]{#struct_0_x4606_33440_x1927952447}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/01]{lang="EN-US"}[的工作模式为同步模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4606_33440_x1618294067}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] synchronous mode]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4606_33440_x810072703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display esmc]{lang="EN-US"}**]{#struct_0_x4606_33440_1278208131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[esmc enable]{lang="EN-US"}**]{#struct_0_x4606_33440_x1142386578}

[ ]{lang="EN-US"}
:::
