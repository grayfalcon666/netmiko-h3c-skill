::: {#1039611657 .myid}
[]{#_Toc404785375}[]{#struct_0_x1087_11486_x1731230197}[]{#_Toc327887955}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- controller cellular**

------------------------------------------------------------------------

[**[controller cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_984785848}[命令用来进入]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_560924470}

[**[controller cellular]{lang="EN-US"}**[ *cellular-number*]{lang="EN-US"}]{#struct_0_x1087_11486_821880211}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1105054079}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x422917043}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1364214443}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1874339454}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1375593548}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x570516870}

[*[cellular-number]{lang="EN-US"}*]{#struct_0_x1087_11486_1368964614}[：]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_839656722}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1713969522}[进入接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_1068618688}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular 2/4/0\]]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785376}[]{#struct_0_x1087_11486_x1496797510}[]{#_Toc327887956}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1087_11486_1364673196}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1087_11486_724349282}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1383481396}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1087_11486_x1595937904}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1087_11486_x1323040537}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1350770945}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x1087_11486_648815796}["，比如：]{style="font-family:宋体"}[Cellular2/4/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1992837281}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_994144742}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1364738732}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1144827542}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1563950027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x833269082}

[*[text]{lang="EN-US"}*]{#struct_0_x1087_11486_x359984602}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x698343294}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_20826121}[设置接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Cellular-intf]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x1244955104}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] description Cellular-intf]{lang="EN-US"}
:::

::: {#1326301942 .myid}
[]{#_Toc404785377}[]{#struct_0_x1087_11486_1364804268}[]{#_Toc324238747}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- display cellular**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **cellular**]{lang="EN-US"}]{#struct_0_x1087_11486_733357366}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的呼叫连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x9277549}

[**[display cellular]{lang="EN-US"}**[ \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_x1087_11486_1525698610}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1478219894}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x530048051}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_345867907}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1059500781}

[[network-operator]{lang="EN-US"}]{#struct_0_x1087_11486_1364869804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x361487737}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1087_11486_x1776463486}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1780620137}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1087_11486_x589662418}[：显示指定]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[呼叫连接信息。如果不指定本参数，则显示所有在位]{style="font-family:宋体"}[Modem]{lang="EN-US"}[对应]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[呼叫连接信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1783913462}

[[对于不同厂家生产的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_451871157}[，此命令显示的内容和格式可能略有区别。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_504462318}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_1364935340}[显示]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}[的呼叫连接信息（]{style="font-family:宋体"}[WCDMA]{lang="EN-US"}[网络）。]{style="font-family:宋体"}

[[\<Sysname\> display cellular 2/4/0]{lang="EN-US"}]{#struct_0_x1087_11486_1364673194}

[Cellular2/4/0:]{lang="EN-US"}

[  Hardware Information:]{lang="EN-US"}

[    Model: E176G]{lang="EN-US"}

[    Modem Firmware Version: 11.604.09.00.00]{lang="EN-US"}

[    Hardware Version: CD25TCPU]{lang="EN-US"}

[    International Mobile Subscriber Identity (IMSI): 460029010431055]{lang="EN-US"}

[    International Mobile Equipment Identity (IMEI): 353871020138548]{lang="EN-US"}

[    Factory Serial Number (FSN):  DK9RAA1871500602]{lang="EN-US"}

[    Modem Status: Online]{lang="EN-US"}

[  Profile Information:]{lang="EN-US"}

[    Profile 1: Active]{lang="EN-US"}

[      PDP Type: IPv4, Header Compression: Off]{lang="EN-US"}

[      Data Compression: Off]{lang="EN-US"}

[      Access Point Name (APN): 001]{lang="EN-US"}

[      Packet Session Status: Inactive]{lang="EN-US"}

[  Modem Setup Information:]{lang="EN-US"}

[    Diagnostics Monitor: Close]{lang="EN-US"}

[  Network Information:]{lang="EN-US"}

[    Current Service Status: Service available]{lang="EN-US"}

[    Current Service: Combined]{lang="EN-US"}

[    Packet Service: Attached]{lang="EN-US"}

[    Packet Session Status: Inactive]{lang="EN-US"}

[    Current Roaming Status: Roaming]{lang="EN-US"}

[    Network Selection Mode: Manual]{lang="EN-US"}

[    Network Connection Mode: WCDMA precedence]{lang="EN-US"}

[    Current Network Connection: HSDPA and HSUPA]{lang="EN-US"}

[    Mobile Country Code (MCC): 460]{lang="EN-US"}

[    Mobile Network Code (MNC): 00]{lang="EN-US"}

[    Location Area Code (LAC): 4318]{lang="EN-US"}

[    Cell ID: 25381]{lang="EN-US"}

[  Radio Information:]{lang="EN-US"}

[    Current Band: ANY]{lang="EN-US"}

[    Current RSSI: -51 dBm]{lang="EN-US"}

[  Modem Security Information:]{lang="EN-US"}

[    PIN Verification: Disabled]{lang="EN-US"}

[    PIN Status: Ready]{lang="EN-US"}

[    Number of Retries remaining: 3]{lang="EN-US"}

[    SIM Status: OK]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display cellular]{lang="EN-US"}]{#struct_0_x1087_11486_724218210}[命令显示信息描述表（]{style="font-family:黑体"}[WCDMA]{lang="EN-US"}[网络）]{style="font-family:黑体"}

[]{#table_struct_0_1171621453}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_170344699}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_1446317220}

[[Hardware Information]{lang="EN-US"}]{#struct_0_x1087_11486_1364738730}

[[硬件信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_1144696470}

[[Model]{lang="EN-US"}]{#struct_0_x1087_11486_763267051}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1901722223}[名称]{style="font-family:宋体"}

[[Modem Firmware Version]{lang="EN-US"}]{#struct_0_x1087_11486_x251708843}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x337930368}[的软件版本号]{style="font-family:宋体"}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1087_11486_1364804266}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_734274870}[的硬件版本号]{style="font-family:宋体"}

[[International Mobile Subscriber Identity (IMSI)]{lang="EN-US"}]{#struct_0_x1087_11486_1123208803}

[[SIM]{lang="EN-US"}]{#struct_0_x1087_11486_x1158948614}[卡的]{style="font-family:宋体"}[IMSI]{lang="EN-US"}[号码串]{style="font-family:宋体"}

[[International Mobile Equipment Identity (IMEI)]{lang="EN-US"}]{#struct_0_x1087_11486_1538395811}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2130562613}[的]{style="font-family:宋体"}[IMEI]{lang="EN-US"}[串号]{style="font-family:宋体"}

[[Factory Serial Number (FSN)]{lang="EN-US"}]{#struct_0_x1087_11486_1364869802}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x361880953}[的产品序列号]{style="font-family:宋体"}

[[Modem Status]{lang="EN-US"}]{#struct_0_x1087_11486_x551083581}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2054001611}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[nline]{lang="EN-US"}]{#struct_0_x1087_11486_x1617189898}[：]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[处于上电状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[ffline]{lang="EN-US"}]{#struct_0_x1087_11486_1364935338}[：]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[处于下电状态或省电模式，]{lang="EN-US" style="font-family:宋体"}[cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Profile Information]{lang="EN-US"}]{#struct_0_x1087_11486_1496291755}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_273409111}[的参数模板信息]{style="font-family:宋体"}

[[Profile 1]{lang="EN-US"}]{#struct_0_x1087_11486_x4484099}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1756607484}[的]{style="font-family:宋体"}[PDP]{lang="EN-US"}[设置状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1087_11486_1365000874}[：已经配置参数模板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x1087_11486_1365066410}[ndefined]{lang="EN-US"}[：还未配置参数模板]{lang="EN-US" style="font-family:宋体"}

[[PDP Type]{lang="EN-US"}]{#struct_0_x1087_11486_1365131946}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_1364214442}[类型，只有]{style="font-family:宋体"}[Profile 1: Active]{lang="EN-US"}[时，才显示该信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_x1087_11486_1874404990}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_x1087_11486_x217512202}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x1087_11486_655812936}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[透传]{style="font-family:宋体"}

[[Header Compression]{lang="EN-US"}]{#struct_0_x1087_11486_684865385}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_1364673191}[头压缩模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x1087_11486_1364738727}[：使能]{style="font-family:宋体"}[PDP]{lang="EN-US"}[头压缩]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1087_11486_1364804263}[：禁止]{style="font-family:宋体"}[PDP]{lang="EN-US"}[头压缩]{style="font-family:宋体"}

[[Data Compression]{lang="EN-US"}]{#struct_0_x1087_11486_734078262}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_502087763}[数据压缩模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x1087_11486_1364935335}[：使能]{style="font-family:宋体"}[PDP]{lang="EN-US"}[数据压缩]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1087_11486_1365000871}[：禁止]{style="font-family:宋体"}[PDP]{lang="EN-US"}[数据压缩]{style="font-family:宋体"}

[[Access Point Name (APN)]{lang="EN-US"}]{#struct_0_x1087_11486_x1954655279}

[[接入点名称]{style="font-family:宋体"}]{#struct_0_x1087_11486_x623898185}

[[Packet Session Status]{lang="EN-US"}]{#struct_0_x1087_11486_1365066407}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_x462745746}[的激活状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1087_11486_1314482282}[：处于激活状态，]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[正在进行]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[传输]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x1087_11486_1365131943}[：处于非激活状态，]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[接口的物理状态为]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}

[[Modem Setup Information]{lang="EN-US"}]{#struct_0_x1087_11486_x1575106484}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_645335942}[安装状态]{style="font-family:宋体"}

[[Diagnostics Monitor]{lang="EN-US"}]{#struct_0_x1087_11486_x640141528}

[[诊断口监控状态]{style="font-family:宋体"}]{#struct_0_x1087_11486_1364148903}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Open]{lang="EN-US"}]{#struct_0_x1087_11486_x747458859}[：诊断监控打开]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Close]{lang="EN-US"}]{#struct_0_x1087_11486_1711322666}[：诊断监控关闭]{style="font-family:宋体"}

[[Network Information]{lang="EN-US"}]{#struct_0_x1087_11486_1364214439}

[[网络信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_1874994807}

[[Current Service Status]{lang="EN-US"}]{#struct_0_x1087_11486_1762395724}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_964401907}[的服务状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service available]{lang="EN-US"}]{#struct_0_x1087_11486_1364673192}[：提供有效服务]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Emergency]{lang="EN-US"}]{#struct_0_x1087_11486_724087138}[：提供有限制服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No service]{lang="EN-US"}]{#struct_0_x1087_11486_x867917845}[：无法提供服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low power]{lang="EN-US"}]{#struct_0_x1087_11486_1364738728}[：处于省电模式，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Current Service]{lang="EN-US"}]{#struct_0_x1087_11486_1145220757}

[[当前服务类型：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1187691493}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Circuit-switched]{lang="EN-US"}]{#struct_0_x1087_11486_1364804264}[：仅]{lang="EN-US" style="font-family:
  宋体"}[CS]{lang="EN-US"}[域服务]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet-switched]{lang="EN-US"}]{#struct_0_x1087_11486_734143798}[：仅]{lang="EN-US" style="font-family:
  宋体"}[PS]{lang="EN-US"}[域服务]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Combined]{lang="EN-US"}]{#struct_0_x1087_11486_x1020796323}[：]{lang="EN-US" style="font-family:宋体"}[CS]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PS]{lang="EN-US"}[域服务都有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x1087_11486_1364869800}[：服务无效]{lang="EN-US" style="font-family:宋体"}

[[Packet Service]{lang="EN-US"}]{#struct_0_x1087_11486_x361749881}

[[3G Modem PS]{lang="EN-US"}]{#struct_0_x1087_11486_x108924622}[域附着状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detached]{lang="EN-US"}]{#struct_0_x1087_11486_1364935336}[：分离状态，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attached]{lang="EN-US"}]{#struct_0_x1087_11486_1495636395}[：连接状态]{lang="EN-US" style="font-family:宋体"}

[[Current Roaming Status]{lang="EN-US"}]{#struct_0_x1087_11486_x748207704}

[[漫游状态：]{style="font-family:宋体"}]{#struct_0_x1087_11486_1365000872}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Roaming]{lang="EN-US"}]{#struct_0_x1087_11486_x1954589743}[：漫游状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Home]{lang="EN-US"}]{#struct_0_x1087_11486_x177865523}[：本地状态]{lang="EN-US" style="font-family:宋体"}

[[Network Selection Mode]{lang="EN-US"}]{#struct_0_x1087_11486_1365066408}

[[网络选择模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x463466642}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1087_11486_x1045898006}[：手动选择]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Automatic]{lang="EN-US"}]{#struct_0_x1087_11486_1365131944}[：自动选择]{lang="EN-US" style="font-family:宋体"}

[[Network Connection Mode]{lang="EN-US"}]{#struct_0_x1087_11486_x1575434164}

[[网络连接模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_1364148904}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA only]{lang="EN-US"}]{#struct_0_x1087_11486_x747917611}[：仅连接]{lang="EN-US" style="font-family:宋体"}[WCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA precedence]{lang="EN-US"}]{#struct_0_x1087_11486_x2073703766}[：优先连接]{lang="EN-US" style="font-family:
  宋体"}[WCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM only]{lang="EN-US"}]{#struct_0_x1087_11486_1364214440}[：仅连接]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM precedence]{lang="EN-US"}]{#struct_0_x1087_11486_1874536062}[：优先连接]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[Current Network Connection]{lang="EN-US"}]{#struct_0_x1087_11486_x1364210160}

[[当前网络连接：]{style="font-family:宋体"}]{#struct_0_x1087_11486_1142835523}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No Service]{lang="EN-US"}]{#struct_0_x1087_11486_922936575}[：无服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_x1364144624}[：]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GPRS]{lang="EN-US"}]{#struct_0_x1087_11486_139868205}[：]{lang="EN-US" style="font-family:宋体"}[GPRS]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EDGE]{lang="EN-US"}]{#struct_0_x1087_11486_x1364079088}[：]{lang="EN-US" style="font-family:宋体"}[EDGE]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_x1581064666}[：]{lang="EN-US" style="font-family:宋体"}[WCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA]{lang="EN-US"}]{#struct_0_x1087_11486_1763617529}[：]{lang="EN-US" style="font-family:宋体"}[HSDPA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_x1364013552}[：]{lang="EN-US" style="font-family:宋体"}[HSUPA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA and HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_1900098173}[：]{lang="EN-US" style="font-family:
  宋体"}[HSDPA]{lang="EN-US"}[和]{lang="EN-US" style="font-family:
  宋体"}[HSUPA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSPA+]{lang="EN-US"}]{#struct_0_x1087_11486_x1363948016}[：]{lang="EN-US" style="font-family:宋体"}[HSPA+]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_x1403117316}[：未知网络]{lang="EN-US" style="font-family:宋体"}

[[Mobile Country Code (MCC)]{lang="EN-US"}]{#struct_0_x1087_11486_x1595026542}

[[移动国家码，搜索到网络后才能显示该信息。例如：中国大陆的国家码为]{style="font-family:宋体"}[460]{lang="EN-US"}]{#struct_0_x1087_11486_x1363882480}

[[Mobile Network Code (MNC)]{lang="EN-US"}]{#struct_0_x1087_11486_1008542746}

[[运营商网络代码，成功注册到网络后才能显示该信息。例如：中国移动]{style="font-family:宋体"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_x1363816944}[网络代码为]{style="font-family:宋体"}[00]{lang="EN-US"}

[[Location Area Code (LAC)]{lang="EN-US"}]{#struct_0_x1087_11486_x1651106984}

[[位置码信息，成功注册到网络后才能显示该信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1363751408}

[[Cell ID]{lang="EN-US"}]{#struct_0_x1087_11486_1914949075}

[[小区信息，成功注册到网络后才能显示该信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_x799656898}

[[Current Band]{lang="EN-US"}]{#struct_0_x1087_11486_x1364734448}

[[当前频带选择模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x46418842}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_x1364668912}[：选择]{style="font-family:宋体"}[GSM]{lang="EN-US"}[网络频带]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_x1665978022}[：选择]{style="font-family:宋体"}[WCDMA]{lang="EN-US"}[网络频带]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANY]{lang="EN-US"}]{#struct_0_x1087_11486_x1364210159}[：选择任意频带]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTO]{lang="EN-US"}]{#struct_0_x1087_11486_x779544314}[：自动选择频带]{style="font-family:宋体"}

[[Current RSSI]{lang="EN-US"}]{#struct_0_x1087_11486_x1364144623}

[[当前信号质量：]{style="font-family:宋体"}]{#struct_0_x1087_11486_899383092}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信号质量的取值范围为]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1364079087}[-110dBm ]{lang="EN-US"}[～]{style="font-family:宋体"}[ -51dBm]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_1598157383}[：无信号，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Modem Security Information]{lang="EN-US"}]{#struct_0_x1087_11486_316525856}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1364013551}[安全信息]{style="font-family:宋体"}

[[PIN Verification]{lang="EN-US"}]{#struct_0_x1087_11486_x828785182}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_x1363948015}[认证状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1087_11486_x999832789}[：未使能]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1087_11486_x1363882479}[：使能了]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[PIN Status]{lang="EN-US"}]{#struct_0_x1087_11486_x1364437929}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_x1087_11486_x1363816943}[：]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIN Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_x85023043}[：]{lang="EN-US" style="font-family:
  宋体"}[SIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PIN]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin verify]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PUK Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_x74386972}[：]{lang="EN-US" style="font-family:
  宋体"}[SIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PUK]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin unlock]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[Number of Retries remaining]{lang="EN-US"}]{#struct_0_x1087_11486_x1364734447}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_x1364668911}[或]{style="font-family:宋体"}[PUK]{lang="EN-US"}[剩余尝试次数]{style="font-family:宋体"}

[[SIM Status]{lang="EN-US"}]{#struct_0_x1087_11486_1062905333}

[[SIM]{lang="EN-US"}]{#struct_0_x1087_11486_x1364210162}[卡状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OK]{lang="EN-US"}]{#struct_0_x1087_11486_x1989332359}[：]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network Reject]{lang="EN-US"}]{#struct_0_x1087_11486_x1364144626}[：]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡被拒绝接入网络，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not Insert]{lang="EN-US"}]{#struct_0_x1087_11486_1302667619}[：未插入]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1364079090}[显示]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}[的呼叫连接信息（]{style="font-family:宋体"}[TD-SCDMA]{lang="EN-US"}[网络）。]{style="font-family:宋体"}

[[\<Sysname\> display cellular 2/4/0]{lang="EN-US"}]{#struct_0_x1087_11486_x1364079091}

[Cellular2/4/0:]{lang="EN-US"}

[  Hardware Information:]{lang="EN-US"}

[    Model: ET128]{lang="EN-US"}

[    Modem Firmware Version: 11.101.01.08.00]{lang="EN-US"}

[    Hardware Version:  CS31TCPU]{lang="EN-US"}

[    International Mobile Subscriber Identity (IMSI): 460079011105842]{lang="EN-US"}

[    International Mobile Equipment Identity (IMEI): 860039002369111]{lang="EN-US"}

[    Factory Serial Number (FSN):  GQ4CAB1942911350]{lang="EN-US"}

[    Modem Status: Online]{lang="EN-US"}

[  Profile Information:]{lang="EN-US"}

[    Profile 1: Active]{lang="EN-US"}

[      PDP Type: IPv4]{lang="EN-US"}

[      Header Compression: Off]{lang="EN-US"}

[      Data Compression: Off]{lang="EN-US"}

[      Access Point Name (APN): cmnet]{lang="EN-US"}

[      Packet Session Status: Active]{lang="EN-US"}

[  Network Information:]{lang="EN-US"}

[    Current Service Status: Service available]{lang="EN-US"}

[    Network Selection Mode: Automatic]{lang="EN-US"}

[    Network Connection Mode: TD-SCDMA precedence]{lang="EN-US"}

[    Current Network Connection: HSDPA]{lang="EN-US"}

[    Mobile Network Name: CHINA MOBILE]{lang="EN-US"}

[    Downstream Bandwidth: 2800000 bps]{lang="EN-US"}

[  Radio Information:]{lang="EN-US"}

[    Current RSSI: -75 dBm]{lang="EN-US"}

[  Modem Security Information:]{lang="EN-US"}

[    PIN Verification: Disabled]{lang="EN-US"}

[    PIN Status: Ready]{lang="EN-US"}

[    Number of Retries remaining: 3]{lang="EN-US"}

[    SIM Status: OK]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x1364013555}[命令显示信息描述表（]{style="font-family:黑体"}[TD-SCDMA]{lang="EN-US"}[网络）]{style="font-family:黑体"}

[]{#table_struct_0_1174525783}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_1496813646}

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1363948019}

[[Hardware Information]{lang="EN-US"}]{#struct_0_x1087_11486_x847066615}

[[硬件信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_621040839}

[[Model]{lang="EN-US"}]{#struct_0_x1087_11486_x1369797635}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1363882483}[名称]{style="font-family:宋体"}

[[Modem Firmware Version]{lang="EN-US"}]{#struct_0_x1087_11486_x557541195}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_522354133}[的软件版本号]{style="font-family:宋体"}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1087_11486_77371355}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2073673106}[的硬件版本号]{style="font-family:宋体"}

[[International Mobile Subscriber Identity (IMSI)]{lang="EN-US"}]{#struct_0_x1087_11486_1338154339}

[[SIM]{lang="EN-US"}]{#struct_0_x1087_11486_x1363816947}[卡的]{style="font-family:宋体"}[IMSI]{lang="EN-US"}[号码串]{style="font-family:宋体"}

[[International Mobile Equipment Identity (IMEI)]{lang="EN-US"}]{#struct_0_x1087_11486_x2054391511}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1997737257}[的]{style="font-family:宋体"}[IMEI]{lang="EN-US"}[串号]{style="font-family:宋体"}

[[Factory Serial Number (FSN)]{lang="EN-US"}]{#struct_0_x1087_11486_x1051210516}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x2126346815}[的产品序列号]{style="font-family:宋体"}

[[Modem Status]{lang="EN-US"}]{#struct_0_x1087_11486_x1363751411}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x7430762}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_x1087_11486_x56330517}[：]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[处于上电状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_x1087_11486_1876781058}[：]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[处于下电状态或省电模式，]{lang="EN-US" style="font-family:宋体"}[cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Profile Information]{lang="EN-US"}]{#struct_0_x1087_11486_x1501773808}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1364734451}[的参数模板信息]{style="font-family:宋体"}

[[Profile 1]{lang="EN-US"}]{#struct_0_x1087_11486_x1256337959}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_887113579}[的]{style="font-family:宋体"}[PDP]{lang="EN-US"}[设置状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1087_11486_201873781}[：已经配置参数模板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x1087_11486_202004853}[ndefined]{lang="EN-US"}[：还未配置参数模板]{lang="EN-US" style="font-family:宋体"}

[[PDP Type]{lang="EN-US"}]{#struct_0_x1087_11486_1090636858}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_202201461}[类型，只有]{style="font-family:宋体"}[Profile 1: Active]{lang="EN-US"}[时，才显示该信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_x1087_11486_1026053364}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_x1087_11486_x2012114505}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x1087_11486_202266997}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[透传]{style="font-family:宋体"}

[[Header Compression]{lang="EN-US"}]{#struct_0_x1087_11486_x976666345}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_x1384006041}[头压缩模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x1087_11486_201349493}[：使能]{style="font-family:宋体"}[PDP]{lang="EN-US"}[头压缩]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1087_11486_201873782}[：禁止]{style="font-family:宋体"}[PDP]{lang="EN-US"}[头压缩]{style="font-family:宋体"}

[[Data Compression]{lang="EN-US"}]{#struct_0_x1087_11486_2117889314}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_1320363994}[数据压缩模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x1087_11486_202004854}[：使能]{style="font-family:宋体"}[PDP]{lang="EN-US"}[数据压缩]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1087_11486_202135926}[：禁止]{style="font-family:宋体"}[PDP]{lang="EN-US"}[数据压缩]{style="font-family:宋体"}

[[Access Point Name (APN)]{lang="EN-US"}]{#struct_0_x1087_11486_x880918483}

[[接入点名称]{style="font-family:宋体"}]{#struct_0_x1087_11486_1389863039}

[[Packet Session Status]{lang="EN-US"}]{#struct_0_x1087_11486_202201462}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_1026053365}[的激活状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1087_11486_x2012048969}[：处于激活状态，]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[正在进行]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[传输]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x1087_11486_1505207393}[：处于非激活状态，]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[接口的物理状态为]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}

[[Network Information]{lang="EN-US"}]{#struct_0_x1087_11486_202266998}

[[网络信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_x976666356}

[[Current Service Status]{lang="EN-US"}]{#struct_0_x1087_11486_x1383940506}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_202332534}[的服务状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service available]{lang="EN-US"}]{#struct_0_x1087_11486_x2101163801}[：提供有效服务]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Emergency]{lang="EN-US"}]{#struct_0_x1087_11486_x1949422796}[：提供有限制服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No service]{lang="EN-US"}]{#struct_0_x1087_11486_x2057294582}[：无法提供服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low power]{lang="EN-US"}]{#struct_0_x1087_11486_201349494}[：处于省电模式，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Network Selection Mode]{lang="EN-US"}]{#struct_0_x1087_11486_249613200}

[[网络选择模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1632476523}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1087_11486_201415030}[：手动选择]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Automatic]{lang="EN-US"}]{#struct_0_x1087_11486_x1054214077}[：自动选择]{lang="EN-US" style="font-family:宋体"}

[[Network Connection Mode]{lang="EN-US"}]{#struct_0_x1087_11486_x1095954004}

[[网络连接模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_201873779}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TD-SCDMA only]{lang="EN-US"}]{#struct_0_x1087_11486_1780182295}[：仅连接]{lang="EN-US" style="font-family:宋体"}[TD-SCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TD-SCDMA precedence]{lang="EN-US"}]{#struct_0_x1087_11486_x157250029}[：优先连接]{lang="EN-US" style="font-family:
  宋体"}[TD-SCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM only]{lang="EN-US"}]{#struct_0_x1087_11486_201939315}[：仅连接]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM precedence]{lang="EN-US"}]{#struct_0_x1087_11486_990288427}[：优先连接]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[Current Network Connection]{lang="EN-US"}]{#struct_0_x1087_11486_x1558571797}

[[当前网络连接：]{style="font-family:宋体"}]{#struct_0_x1087_11486_202004851}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No Service]{lang="EN-US"}]{#struct_0_x1087_11486_1090636856}[：无服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_x1355005540}[：]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GPRS]{lang="EN-US"}]{#struct_0_x1087_11486_202070387}[：]{lang="EN-US" style="font-family:宋体"}[GPRS]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EDGE]{lang="EN-US"}]{#struct_0_x1087_11486_1531413782}[：]{lang="EN-US" style="font-family:宋体"}[EDGE]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TD-SCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_766609721}[：]{lang="EN-US" style="font-family:宋体"}[TD-SCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA]{lang="EN-US"}]{#struct_0_x1087_11486_202135923}[：]{lang="EN-US" style="font-family:宋体"}[HSDPA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_x880918480}[：未知网络]{lang="EN-US" style="font-family:宋体"}

[[Mobile Network Name]{lang="EN-US"}]{#struct_0_x1087_11486_202201459}

[[移动网络名称]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1312598804}

[[Downstream Bandwidth]{lang="EN-US"}]{#struct_0_x1087_11486_x332054165}

[[下行理论带宽，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}]{#struct_0_x1087_11486_202266995}

[[Radio Information]{lang="EN-US"}]{#struct_0_x1087_11486_x976666343}

[[无线电通信信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1384137113}

[[Current RSSI]{lang="EN-US"}]{#struct_0_x1087_11486_202332531}

[[当前信号质量：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x2101163798}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信号质量的取值范围为]{style="font-family:宋体"}]{#struct_0_x1087_11486_201349491}[-110dBm ]{lang="EN-US"}[～]{style="font-family:宋体"}[ -51dBm]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_249613205}[：无信号，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Modem Security Information]{lang="EN-US"}]{#struct_0_x1087_11486_x1632476528}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_201415027}[安全信息]{style="font-family:宋体"}

[[PIN Verification]{lang="EN-US"}]{#struct_0_x1087_11486_902101052}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_201873780}[认证状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1087_11486_2117889312}[：未使能]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1087_11486_1319970778}[：使能了]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[PIN Status]{lang="EN-US"}]{#struct_0_x1087_11486_201939316}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_990288430}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_x1087_11486_202004852}[：]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIN Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_1090636857}[：]{lang="EN-US" style="font-family:
  宋体"}[SIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PIN]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin verify]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PUK Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_x1354940004}[：]{lang="EN-US" style="font-family:
  宋体"}[SIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PUK]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin unlock]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[Number of Retries remaining]{lang="EN-US"}]{#struct_0_x1087_11486_202070388}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_1531413769}[或]{style="font-family:宋体"}[PUK]{lang="EN-US"}[剩余尝试次数]{style="font-family:宋体"}

[[SIM Status]{lang="EN-US"}]{#struct_0_x1087_11486_202135924}

[[SIM]{lang="EN-US"}]{#struct_0_x1087_11486_x880918485}[卡状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OK]{lang="EN-US"}]{#struct_0_x1087_11486_202201460}[：]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network Reject]{lang="EN-US"}]{#struct_0_x1087_11486_1026053363}[：]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡被拒绝接入网络，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not Insert]{lang="EN-US"}]{#struct_0_x1087_11486_x2012180041}[：未插入]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_202266996}[显示]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}[的呼叫连接信息（]{style="font-family:宋体"}[CDMA]{lang="EN-US"}[网络）。]{style="font-family:宋体"}

[[\<Sysname\> display cellular 2/4/0]{lang="EN-US"}]{#struct_0_x1087_11486_2124253619}

[Cellular2/4/0:]{lang="EN-US"}

[  Hardware Information:]{lang="EN-US"}

[    Model: EC169]{lang="EN-US"}

[    Manufacturer: HUAWEI TECHNOLOGIES CO.]{lang="EN-US"}

[    Modem Firmware Version: 11.002.03.01.45]{lang="EN-US"}

[    Hardware Version:  CE62TCPUVer A]{lang="EN-US"}

[    Electronic Serial Number (ESN): c1836f2d]{lang="EN-US"}

[    Preferred Roaming List (PRL) Version: 0]{lang="EN-US"}

[    International Mobile Subscriber Identity (IMSI): 460036101433925]{lang="EN-US"}

[    Modem Status: Online]{lang="EN-US"}

[  Network Information:]{lang="EN-US"}

[    Current Service Status: Service available]{lang="EN-US"}

[    Current Roaming Status: Home]{lang="EN-US"}

[    Network Connection Mode: Manual]{lang="EN-US"}

[    Current Network Connection: 1xRTT/EVDO HYBRID]{lang="EN-US"}

[    Downstream Bandwidth: 3100000 bps]{lang="EN-US"}

[  Radio Information:]{lang="EN-US"}

[    Current RSSI(1xRTT): -93 dBm]{lang="EN-US"}

[    Current RSSI(EVDO): -75 dBm]{lang="EN-US"}

[    Current Voltage: 3336 mV]{lang="EN-US"}

[  Modem Security Information:]{lang="EN-US"}

[    PIN Verification: Disabled]{lang="EN-US"}

[    PIN Status: Ready]{lang="EN-US"}

[    Number of Retries remaining: 3]{lang="EN-US"}

[    UIM Status: OK]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display cellular]{lang="EN-US"}]{#struct_0_x1087_11486_2124319155}[命令显示信息描述表（]{style="font-family:黑体"}[CDMA]{lang="EN-US"}[网络）]{style="font-family:黑体"}

[]{#table_struct_0_1492264313}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_620642346}

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1847881396}

[[Hardware Information]{lang="EN-US"}]{#struct_0_x1087_11486_2124384691}

[[硬件信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_1832473687}

[[Model]{lang="EN-US"}]{#struct_0_x1087_11486_x713848518}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x53577735}[名称]{style="font-family:宋体"}

[[Manufacturer]{lang="EN-US"}]{#struct_0_x1087_11486_x244874009}

[[设备生产商]{style="font-family:宋体"}]{#struct_0_x1087_11486_2124450227}

[[Modem Firmware Version]{lang="EN-US"}]{#struct_0_x1087_11486_x899536923}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2054098746}[的软件版本号]{style="font-family:宋体"}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1087_11486_x507789972}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1496249608}[的硬件版本号]{style="font-family:宋体"}

[[Electronic Serial Number (ESN)]{lang="EN-US"}]{#struct_0_x1087_11486_2124515763}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1678980685}[的产品序列号]{style="font-family:宋体"}

[[Preferred Roaming List (PRL) Version]{lang="EN-US"}]{#struct_0_x1087_11486_x1775132119}

[[首选漫游列表版本]{style="font-family:宋体"}]{#struct_0_x1087_11486_2139178571}

[[International Mobile Subscriber Identity (IMSI)]{lang="EN-US"}]{#struct_0_x1087_11486_x306008822}

[[UIM]{lang="EN-US"}]{#struct_0_x1087_11486_2124581299}[卡的]{style="font-family:宋体"}[IMSI]{lang="EN-US"}[号码串]{style="font-family:宋体"}

[[Modem Status]{lang="EN-US"}]{#struct_0_x1087_11486_1827838996}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_804116407}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_x1087_11486_1627163415}[：]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[处于上电状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_x1087_11486_x823422576}[：]{lang="EN-US" style="font-family:宋体"}[3G Modem]{lang="EN-US"}[处于下电状态或省电模式，]{lang="EN-US" style="font-family:宋体"}[cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Network Information]{lang="EN-US"}]{#struct_0_x1087_11486_2124646835}

[[网络信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_1091976810}

[[Current Service Status]{lang="EN-US"}]{#struct_0_x1087_11486_x579780419}

[[3G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_812974752}[的服务状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service available]{lang="EN-US"}]{#struct_0_x1087_11486_2123663795}[：提供有效服务]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Emergency]{lang="EN-US"}]{#struct_0_x1087_11486_1945601387}[：提供有限制服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No service]{lang="EN-US"}]{#struct_0_x1087_11486_1267906615}[：无法提供服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low power]{lang="EN-US"}]{#struct_0_x1087_11486_x1901195704}[：处于省电模式，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Current Roaming Status]{lang="EN-US"}]{#struct_0_x1087_11486_2123729331}

[[漫游状态：]{style="font-family:宋体"}]{#struct_0_x1087_11486_382746804}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Roaming]{lang="EN-US"}]{#struct_0_x1087_11486_1601425598}[：漫游状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Home]{lang="EN-US"}]{#struct_0_x1087_11486_1766353525}[：本地状态]{lang="EN-US" style="font-family:宋体"}

[[Network Selection Mode]{lang="EN-US"}]{#struct_0_x1087_11486_2124188080}

[[网络选择模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x163066914}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1087_11486_x934093823}[：手动选择]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Automatic]{lang="EN-US"}]{#struct_0_x1087_11486_x1778624948}[：自动选择]{lang="EN-US" style="font-family:宋体"}

[[Current Network Connection]{lang="EN-US"}]{#struct_0_x1087_11486_2124253616}

[[当前网络连接：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x538082065}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No Service]{lang="EN-US"}]{#struct_0_x1087_11486_x1773614366}[：无服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1xRTT/EVDO HYBRID]{lang="EN-US"}]{#struct_0_x1087_11486_x843678436}[：]{lang="EN-US" style="font-family:
  宋体"}[1xRTT]{lang="EN-US"}[和]{lang="EN-US" style="font-family:
  宋体"}[EVDO]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVDO]{lang="EN-US"}]{#struct_0_x1087_11486_2124319152}[：]{lang="EN-US" style="font-family:宋体"}[EVDO]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1xRTT]{lang="EN-US"}]{#struct_0_x1087_11486_620576810}[：]{lang="EN-US" style="font-family:宋体"}[1xRTT]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_x1358517706}[：未知网络]{lang="EN-US" style="font-family:宋体"}

[[Downstream Bandwidth]{lang="EN-US"}]{#struct_0_x1087_11486_2124384688}

[[下行理论带宽，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}]{#struct_0_x1087_11486_1832932440}

[[Radio Information]{lang="EN-US"}]{#struct_0_x1087_11486_1639578926}

[[无线电通信信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_2124450224}

[[Current RSSI (1xRTT)]{lang="EN-US"}]{#struct_0_x1087_11486_x899602459}

[[当前]{style="font-family:宋体"}[1xRTT]{lang="EN-US"}]{#struct_0_x1087_11486_x228377292}[网络信号质量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信号质量的取值范围为]{style="font-family:宋体"}]{#struct_0_x1087_11486_1608420453}[-125dBm ]{lang="EN-US"}[～]{style="font-family:宋体"}[ -75dBm]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_2124515760}[：无信号]{lang="EN-US" style="font-family:宋体"}

[[Current RSSI (EVDO)]{lang="EN-US"}]{#struct_0_x1087_11486_x1679046221}

[[当前]{style="font-family:宋体"}[EVDO]{lang="EN-US"}]{#struct_0_x1087_11486_x337342886}[网络信号质量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信号质量的取值范围为]{style="font-family:宋体"}]{#struct_0_x1087_11486_2124581296}[-120dBm ]{lang="EN-US"}[～]{style="font-family:宋体"}[ -60dBm]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_1827380244}[：无信号]{lang="EN-US" style="font-family:宋体"}

[[Current Voltage]{lang="EN-US"}]{#struct_0_x1087_11486_890254335}

[[UIM]{lang="EN-US"}]{#struct_0_x1087_11486_2124646832}[卡电压值，单位为]{style="font-family:宋体"}[mV]{lang="EN-US"}

[[Modem Security Information]{lang="EN-US"}]{#struct_0_x1087_11486_1092042346}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_834695035}[安全信息]{style="font-family:宋体"}

[[PIN Verification]{lang="EN-US"}]{#struct_0_x1087_11486_2123663792}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_1945404779}[认证状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1087_11486_1273458915}[：未使能]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1087_11486_2123729328}[：使能了]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[PIN Status]{lang="EN-US"}]{#struct_0_x1087_11486_382156981}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_x1087_11486_1997620535}[：]{lang="EN-US" style="font-family:宋体"}[UIM]{lang="EN-US"}[卡状态正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIN Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_2124188081}[：]{lang="EN-US" style="font-family:
  宋体"}[UIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PIN]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin verify]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PUK Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_x163001378}[：]{lang="EN-US" style="font-family:
  宋体"}[UIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PUK]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin unlock]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[Number of Retries remaining]{lang="EN-US"}]{#struct_0_x1087_11486_x543058696}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_2124253617}[或]{style="font-family:宋体"}[PUK]{lang="EN-US"}[剩余尝试次数]{style="font-family:宋体"}

[[UIM Status]{lang="EN-US"}]{#struct_0_x1087_11486_x538147601}

[[UIM]{lang="EN-US"}]{#struct_0_x1087_11486_647332926}[卡状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OK]{lang="EN-US"}]{#struct_0_x1087_11486_2124319153}[：]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network Reject]{lang="EN-US"}]{#struct_0_x1087_11486_620511274}[：]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡被拒绝接入网络，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not Insert]{lang="EN-US"}]{#struct_0_x1087_11486_x1724048174}[：未插入]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1262881277}[显示]{style="font-family:宋体"}[4G Modem]{lang="EN-US"}[的呼叫连接信息（]{style="font-family:宋体"}[LTE]{lang="EN-US"}[网络）。]{style="font-family:宋体"}

[[\<Sysname\> display cellular 0/0]{lang="EN-US"}]{#struct_0_x1087_11486_x1311618187}

[Cellular0/0:]{lang="EN-US"}

[  Hardware Information:]{lang="EN-US"}

[    Model: MC7750]{lang="EN-US"}

[    Manufacturer: Sierra Wireless, Incorporated]{lang="EN-US"}

[    Modem Firmware Version: SWI9600M_03.05.10.06]{lang="EN-US"}

[    Hardware Version: 10]{lang="EN-US"}

[    International Mobile Equipment Identity (IMEI): 990000560327506]{lang="EN-US"}

[    Modem Status: Online]{lang="EN-US"}

[  Profile Information:]{lang="EN-US"}

[    Profile index: 1]{lang="EN-US"}

[      PDP Type: IPv4]{lang="EN-US"}

[      Header Compression: Off]{lang="EN-US"}

[      Data Compression: Off]{lang="EN-US"}

[      Access Point Name (APN): vzwinternet]{lang="EN-US"}

[  Network Information:]{lang="EN-US"}

[    Current Service Status: Service available]{lang="EN-US"}

[    Current Roaming Status: Roaming]{lang="EN-US"}

[    Current Data Bearer Technology: Unknown]{lang="EN-US"}

[    Network Selection Mode: Manual]{lang="EN-US"}

[    Mobile Country Code (MCC): 460]{lang="EN-US"}

[    Mobile Network Code (MNC): 00]{lang="EN-US"}

[    Location Area Code (LAC): 4318]{lang="EN-US"}

[    Cell ID: 25381]{lang="EN-US"}

[  Radio Information:]{lang="EN-US"}

[    Technology Preference: LTE only]{lang="EN-US"}

[    Technology Selected: LTE]{lang="EN-US"}

[  LTE related info:]{lang="EN-US"}

[    Current RSSI: -79 dBm]{lang="EN-US"}

[    Current RSRQ: -9 dB]{lang="EN-US"}

[    Current RSRP: -106 dBm]{lang="EN-US"}

[    Current SNR: 5 dB]{lang="EN-US"}

[    Tx Power: -3276 dBm]{lang="EN-US"}

[  Modem Security Information:]{lang="EN-US"}

[    PIN Verification: Disabled]{lang="EN-US"}

[    PIN Status: Ready]{lang="EN-US"}

[    SIM Status: OK]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display cellular]{lang="EN-US"}]{#struct_0_x1087_11486_1210688490}[命令显示信息描述表（]{style="font-family:黑体"}[LTE]{lang="EN-US"}[网络）]{style="font-family:黑体"}

[]{#table_struct_0_x614360826}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_190032322}

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_931442548}

[[Hardware Information]{lang="EN-US"}]{#struct_0_x1087_11486_1295482898}

[[硬件信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1666165804}

[[Model]{lang="EN-US"}]{#struct_0_x1087_11486_1690565640}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1347204566}[名称]{style="font-family:宋体"}

[[Manufacturer]{lang="EN-US"}]{#struct_0_x1087_11486_x1008832082}

[[设备生产商]{style="font-family:宋体"}]{#struct_0_x1087_11486_x271145198}

[[Modem Firmware Version]{lang="EN-US"}]{#struct_0_x1087_11486_2097700806}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2134592525}[的软件版本号]{style="font-family:宋体"}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1087_11486_x100081863}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_426927383}[的硬件版本号]{style="font-family:宋体"}

[[International Mobile Equipment Identity (IMEI)]{lang="EN-US"}]{#struct_0_x1087_11486_1771019487}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_496442251}[的]{style="font-family:宋体"}[IMEI]{lang="EN-US"}[串号]{style="font-family:宋体"}

[[Modem Status]{lang="EN-US"}]{#struct_0_x1087_11486_x592566140}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1990258881}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[nline]{lang="EN-US"}]{#struct_0_x1087_11486_x859596750}[：]{lang="EN-US" style="font-family:宋体"}[Modem]{lang="EN-US"}[处于上电状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[ffline]{lang="EN-US"}]{#struct_0_x1087_11486_983971533}[：]{lang="EN-US" style="font-family:宋体"}[Modem]{lang="EN-US"}[处于下电状态或省电模式，]{lang="EN-US" style="font-family:宋体"}[C]{lang="EN-US"}[ellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Profile Information]{lang="EN-US"}]{#struct_0_x1087_11486_446557118}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_35238783}[的参数模板信息]{style="font-family:宋体"}

[[Profile index]{lang="EN-US"}]{#struct_0_x1087_11486_1737083057}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x123303494}[的参数模板索引]{style="font-family:宋体"}

[[PDP Type]{lang="EN-US"}]{#struct_0_x1087_11486_706487191}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_x1627607064}[类型，只有]{style="font-family:宋体"}[Profile 1 = Active]{lang="EN-US"}[时，才显示该信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_x1087_11486_141008196}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_x1087_11486_x1466986352}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x1087_11486_x1504362085}[：]{style="font-family:宋体"}[PDP]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[透传]{style="font-family:宋体"}

[[Header Compression]{lang="EN-US"}]{#struct_0_x1087_11486_x238012697}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_1748814556}[头压缩模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x1087_11486_303202664}[：使能]{style="font-family:宋体"}[PDP]{lang="EN-US"}[头压缩]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1087_11486_x808639649}[：禁止]{style="font-family:宋体"}[PDP]{lang="EN-US"}[头压缩]{style="font-family:宋体"}

[[Data Compression]{lang="EN-US"}]{#struct_0_x1087_11486_x1002829029}

[[PDP]{lang="EN-US"}]{#struct_0_x1087_11486_x1551516104}[数据压缩模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x1087_11486_1774725604}[：使能]{style="font-family:宋体"}[PDP]{lang="EN-US"}[数据压缩]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x1087_11486_x215903626}[：禁止]{style="font-family:宋体"}[PDP]{lang="EN-US"}[数据压缩]{style="font-family:宋体"}

[[Access Point Name]{lang="EN-US"}]{#struct_0_x1087_11486_1869286605}

[[接入点名称]{style="font-family:宋体"}]{#struct_0_x1087_11486_117051312}

[[Network Information]{lang="EN-US"}]{#struct_0_x1087_11486_469018877}

[[网络信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_x595485073}

[[Current Service Status]{lang="EN-US"}]{#struct_0_x1087_11486_x584875012}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1479897995}[的服务状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Limited]{lang="EN-US"}]{#struct_0_x1087_11486_1822232438}[：服务受限，]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service available]{lang="EN-US"}]{#struct_0_x1087_11486_336141653}[：提供有效服务]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Emergency]{lang="EN-US"}]{#struct_0_x1087_11486_x581171347}[：提供有限制服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No service]{lang="EN-US"}]{#struct_0_x1087_11486_x1218201347}[：无法提供服务，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low power]{lang="EN-US"}]{#struct_0_x1087_11486_1505262993}[：处于省电模式，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Current Roaming Status]{lang="EN-US"}]{#struct_0_x1087_11486_x443794706}

[[漫游状态：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x906650917}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Roaming]{lang="EN-US"}]{#struct_0_x1087_11486_1348137379}[：漫游状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Home]{lang="EN-US"}]{#struct_0_x1087_11486_1125383347}[：本地状态]{lang="EN-US" style="font-family:宋体"}

[[Current Data Bearer Technology]{lang="EN-US"}]{#struct_0_x1087_11486_x2094689840}

[[当前载波制式，包括：]{style="font-family:宋体"}]{#struct_0_x1087_11486_1014619763}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CDMA2000 1X]{lang="EN-US"}]{#struct_0_x1087_11486_1640576282}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CDMA2000 HRPD (1xEV-DO)]{lang="EN-US"}]{#struct_0_x1087_11486_1599564446}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_x2013255055}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UMTS]{lang="EN-US"}]{#struct_0_x1087_11486_x928959520}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CDMA2000 HRPD (1xEV-DO RevA)]{lang="EN-US"}]{#struct_0_x1087_11486_1218911022}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EDGE]{lang="EN-US"}]{#struct_0_x1087_11486_x713846943}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA and WCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_x1129318909}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA and HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_1634334366}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA and HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_216941267}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LTE]{lang="EN-US"}]{#struct_0_x1087_11486_1358377220}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CDMA2000 EHRPD]{lang="EN-US"}]{#struct_0_x1087_11486_x1532603436}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA+ and WCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_156085546}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA+ and HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_x1889494576}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DC_HSDPA+ and WCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_757465950}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DC_HSDPA+ and HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_x26607385}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA+ and 64QAM]{lang="EN-US"}]{#struct_0_x1087_11486_1625194028}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSDPA+, 64QAM and HSUPA]{lang="EN-US"}]{#struct_0_x1087_11486_33480505}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TDSCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_1452356567}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TDSCDMA and HSDPA]{lang="EN-US"}]{#struct_0_x1087_11486_x1731696240}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_1717416376}

[[Network Selection Mode]{lang="EN-US"}]{#struct_0_x1087_11486_143453653}

[[网络选择模式：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x726034382}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1087_11486_x277598721}[：手动选择]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Automatic]{lang="EN-US"}]{#struct_0_x1087_11486_1789943174}[：自动选择]{lang="EN-US" style="font-family:宋体"}

[[Mobile Country Code]{lang="EN-US"}]{#struct_0_x1087_11486_x1519713868}

[[移动国家码，搜索到网络后才能显示该信息。例如：中国大陆的国家码为]{style="font-family:宋体"}[460]{lang="EN-US"}]{#struct_0_x1087_11486_838745844}

[[Mobile Network Code]{lang="EN-US"}]{#struct_0_x1087_11486_2126048187}

[[运营商网络代码，成功注册到网络后才能显示该信息。例如：中国移动]{style="font-family:宋体"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_840049559}[网络代码为]{style="font-family:宋体"}[00]{lang="EN-US"}

[[Location Area Code]{lang="EN-US"}]{#struct_0_x1087_11486_1484293135}

[[位置码信息，成功注册到网络后才能显示该信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_436765032}

[[Cell ID]{lang="EN-US"}]{#struct_0_x1087_11486_1419722641}

[[小区信息，成功注册到网络后才能显示该信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_1108941714}

[[Radio Information]{lang="EN-US"}]{#struct_0_x1087_11486_262838111}

[[无线电通信信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_2002848973}

[[Technology Preference]{lang="EN-US"}]{#struct_0_x1087_11486_879016768}

[[网络优先连接选择：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x54466825}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTO]{lang="EN-US"}]{#struct_0_x1087_11486_x1086081428}[：自动选择连接网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM only]{lang="EN-US"}]{#struct_0_x1087_11486_1955794806}[：仅连接]{style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM precedence]{lang="EN-US"}]{#struct_0_x1087_11486_x2036116924}[：优先连接]{lang="EN-US" style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA only]{lang="EN-US"}]{#struct_0_x1087_11486_148437803}[：仅连接]{style="font-family:宋体"}[WCDMA]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA precedence]{lang="EN-US"}]{#struct_0_x1087_11486_1905971904}[：优先连接]{lang="EN-US" style="font-family:
  宋体"}[WCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TD-SCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_x773088549}[ only]{lang="EN-US"}[：仅连接]{lang="EN-US" style="font-family:宋体"}[TD-SCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TD-SCDMA precedence]{lang="EN-US"}]{#struct_0_x1087_11486_x1588044610}[：优先连接]{lang="EN-US" style="font-family:
  宋体"}[TD-SCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVDO]{lang="EN-US"}]{#struct_0_x1087_11486_x1650940624}[：仅连接]{style="font-family:宋体"}[CDMA-EVDO]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1x RTT]{lang="EN-US"}]{#struct_0_x1087_11486_x1814172958}[：仅连接]{lang="EN-US" style="font-family:宋体"}[CDMA-1x RTT]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1xRTT/EVDO HYBRID]{lang="EN-US"}]{#struct_0_x1087_11486_1599629982}[：]{lang="EN-US" style="font-family:
  宋体"}[同时]{style="font-family:宋体"}[连接]{lang="EN-US" style="font-family:宋体"}[CDMA-EVDO]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[CDMA-1x RTT]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LTE only]{lang="EN-US"}]{#struct_0_x1087_11486_1112948479}[：仅连接]{lang="EN-US" style="font-family:宋体"}[LTE]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[Technology Selected]{lang="EN-US"}]{#struct_0_x1087_11486_400009433}

[[当前选择的网络：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x576790190}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GSM]{lang="EN-US"}]{#struct_0_x1087_11486_x1129253373}[：连接]{style="font-family:宋体"}[GSM]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_409754334}[：连接]{style="font-family:宋体"}[WCDMA]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TD-SCDMA]{lang="EN-US"}]{#struct_0_x1087_11486_x1724389888}[：连接]{lang="EN-US" style="font-family:宋体"}[TD-SCDMA]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVDO]{lang="EN-US"}]{#struct_0_x1087_11486_186726488}[：连接]{style="font-family:宋体"}[CDMA-EVDO]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1x RTT]{lang="EN-US"}]{#struct_0_x1087_11486_240526962}[：连接]{lang="EN-US" style="font-family:宋体"}[CDMA-1x RTT]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1xRTT/EVDO HYBRID]{lang="EN-US"}]{#struct_0_x1087_11486_x1532537900}[：]{lang="EN-US" style="font-family:
  宋体"}[同时]{style="font-family:宋体"}[连接]{lang="EN-US" style="font-family:宋体"}[CDMA-EVDO]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[CDMA-1x RTT]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LTE]{lang="EN-US"}]{#struct_0_x1087_11486_1720177342}[：连接]{style="font-family:宋体"}[LTE]{lang="EN-US"}[网络]{style="font-family:宋体"}

[[LTE related info]{lang="EN-US"}]{#struct_0_x1087_11486_2039529257}

[[LTE]{lang="EN-US"}]{#struct_0_x1087_11486_667302141}[网络相关信息]{style="font-family:宋体"}

[[Current RSSI]{lang="EN-US"}]{#struct_0_x1087_11486_33546041}

[[当前信号质量：]{style="font-family:宋体"}]{#struct_0_x1087_11486_329335464}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[信号质量的取值范围为]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1669848526}[-110dBm]{lang="EN-US"}[～]{style="font-family:宋体"}[-51dBm]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_570217824}[：无信号，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[Current RSRQ]{lang="EN-US"}]{#struct_0_x1087_11486_x725968846}

[[当前参考信号接收质量]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1338988912}

[[Current RSRP]{lang="EN-US"}]{#struct_0_x1087_11486_383228317}

[[当前参考信号接收功率]{style="font-family:宋体"}]{#struct_0_x1087_11486_2032435439}

[[Current SNR]{lang="EN-US"}]{#struct_0_x1087_11486_840115095}

[[当前信噪比]{style="font-family:宋体"}]{#struct_0_x1087_11486_387726741}

[[Tx Power]{lang="EN-US"}]{#struct_0_x1087_11486_1979347785}

[[发送功率]{style="font-family:宋体"}]{#struct_0_x1087_11486_414415913}

[[Modem Security Information]{lang="EN-US"}]{#struct_0_x1087_11486_436830568}

[[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x734165575}[安全信息]{style="font-family:宋体"}

[[PIN Verification]{lang="EN-US"}]{#struct_0_x1087_11486_x1596876027}

[[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_x126539686}[认证状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1087_11486_2002914509}[：未使能]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1087_11486_x675551092}[：使能了]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1087_11486_x1919513141}[：当前]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码状态未知]{style="font-family:宋体"}

[[PIN Status]{lang="EN-US"}]{#struct_0_x1087_11486_1955860342}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_x1087_11486_x161405939}[：]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIN Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_367814732}[：]{lang="EN-US" style="font-family:
  宋体"}[SIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PIN]{lang="EN-US"}[认证请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin verify]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PUK Requirement]{lang="EN-US"}]{#struct_0_x1087_11486_x688884886}[：]{lang="EN-US" style="font-family:
  宋体"}[SIM]{lang="EN-US"}[卡有]{lang="EN-US" style="font-family:
  宋体"}[PUK]{lang="EN-US"}[认真请求]{lang="EN-US" style="font-family:
  宋体"}[，需要用户配置]{style="font-family:宋体"}**[pin unlock]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[SIM Status]{lang="EN-US"}]{#struct_0_x1087_11486_x773023013}

[[SIM]{lang="EN-US"}]{#struct_0_x1087_11486_x1245153738}[卡状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OK]{lang="EN-US"}]{#struct_0_x1087_11486_x1151967020}[：]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network Reject]{lang="EN-US"}]{#struct_0_x1087_11486_2049715004}[：]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡被拒绝接入网络，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not Insert]{lang="EN-US"}]{#struct_0_x1087_11486_1599695518}[ed]{lang="EN-US"}[：未插入]{lang="EN-US" style="font-family:宋体"}[SIM]{lang="EN-US"}[卡，]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口功能不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not Initialized]{lang="EN-US"}]{#struct_0_x1087_11486_1474213436}[：当前]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡状态未知]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2124384689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode cdma]{lang="EN-US"}**]{#struct_0_x1087_11486_1832997976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode td-scdma]{lang="EN-US"}**]{#struct_0_x1087_11486_x1819429338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode wcdma]{lang="EN-US"}**]{#struct_0_x1087_11486_x786405167}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin modify]{lang="EN-US"}**]{#struct_0_x1087_11486_977243126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin unlock]{lang="EN-US"}**]{#struct_0_x1087_11486_1480121741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verification]{lang="EN-US"}**]{#struct_0_x1087_11486_1344465906}**[ enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verify]{lang="EN-US"}**]{#struct_0_x1087_11486_289990017}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[plmn select]{lang="EN-US"}**]{#struct_0_x1087_11486_x636859684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[profile create]{lang="EN-US"}**]{#struct_0_x1087_11486_2124450225}

::: {#-782832203 .myid}
[]{#_Toc404785378}[]{#struct_0_x1087_11486_x899667995}[]{#_Toc327887957}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- display controller cellular**

------------------------------------------------------------------------

[**[display controller cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_x687957239}[命令用来显示]{style="font-family:
宋体"}[Cellular]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1906531552}

[**[display controller]{lang="EN-US"}**[ \[ **cellular** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x1087_11486_x1373569484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x449951808}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_759203406}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1114902932}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_730667719}

[[network-operator]{lang="EN-US"}]{#struct_0_x1087_11486_2124515761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1679111757}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1087_11486_x44887910}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1137978181}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1087_11486_x139413292}[：]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1261852469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x1087_11486_x363119616}**[cellular]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_2055073925}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口]{style="font-family:宋体"}[的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[USB 3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2124581297}[模块热插拔后，相关统计信息会被清零。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1827445780}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1833904749}[显示接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller cellular 2/4/0]{lang="EN-US"}]{#struct_0_x1087_11486_x1011088530}

[Cellular2/4/0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Description: Cellular2/4/0 Interface]{lang="EN-US"}

[Modem status: Present]{lang="EN-US"}

[DM port status: Disabled]{lang="EN-US"}

[Capability:]{lang="EN-US"}

[  1 Control channel, 1 PPP channel]{lang="EN-US"}

[Control channel 0 traffic statistics:]{lang="EN-US"}

[  TX: 0 packets, 0 errors]{lang="EN-US"}

[  RX: 0 packets, 0 errors]{lang="EN-US"}

[PPP channel 0 traffic statistics:]{lang="EN-US"}

[  TX: 0 packets, 0 errors]{lang="EN-US"}

[  RX: 0 packets, 0 errors]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display controller cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x336798235}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1481211213}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_2124646833}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_1092107882}

[[Cellular2/4/0]{lang="EN-US"}]{#struct_0_x1087_11486_484953377}

[[Current state]{lang="EN-US"}]{#struct_0_x1087_11486_416856672}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x1087_11486_176814736}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_x1087_11486_x1057127441}[ ]{lang="EN-US"}[DOWN]{lang="EN-US"}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1087_11486_2123663793}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1087_11486_1945470315}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1087_11486_x1461697711}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x1881172310}[接口的描述信息]{style="font-family:宋体"}

[[Modem status]{lang="EN-US"}]{#struct_0_x1087_11486_1144093320}

[[USB 3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1580544195}[模块的在位状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Present]{lang="EN-US"}]{#struct_0_x1087_11486_2123729329}[：表示在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_x1087_11486_382222517}[：表示不在位]{lang="EN-US" style="font-family:宋体"}

[[DM port status]{lang="EN-US"}]{#struct_0_x1087_11486_x1618752184}

[[DM]{lang="EN-US"}]{#struct_0_x1087_11486_307845355}[功能的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1087_11486_1311220135}[：表示]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能处于打开状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1087_11486_x1153170076}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能处于]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[Capability:]{lang="EN-US"}]{#struct_0_x1087_11486_2124188078}

[[  1 Control channel, 1 PPP channel]{lang="EN-US"}]{#struct_0_x1087_11486_x162542641}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x562558369}[接口支持的通道类型及数量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1 Control channel]{lang="EN-US"}]{#struct_0_x1087_11486_746552402}[：支持]{lang="EN-US" style="font-family:
  宋体"}[1]{lang="EN-US"}[个控制通道]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1 PPP channel]{lang="EN-US"}]{#struct_0_x1087_11486_1959791633}[：支持]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[个异步串口子通道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1 ETH channel]{lang="EN-US"}]{#struct_0_x1087_11486_2124253614}[：支持]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[个以太]{lang="EN-US" style="font-family:宋体"}[网]{style="font-family:宋体"}[子通道]{lang="EN-US" style="font-family:宋体"}

[[Control channel 0 traffic statistics:]{lang="EN-US"}]{#struct_0_x1087_11486_x538213137}

[[  TX: 0 packets, 0 errors]{lang="EN-US"}]{#struct_0_x1087_11486_x2146609526}

[[  RX: 0 packets, 0 errors]{lang="EN-US"}]{#struct_0_x1087_11486_2000088017}

[[Control channel]{lang="EN-US"}]{#struct_0_x1087_11486_2124319150}[的报文收发统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送完成的报文数量，发送错误的报文数量]{style="font-family:宋体"}]{#struct_0_x1087_11486_620445738}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收的报文数量，接收错误的报文数量]{style="font-family:宋体"}]{#struct_0_x1087_11486_1390764986}

[[PPP channel 0 traffic statistics]{lang="EN-US"}]{#struct_0_x1087_11486_1804610224}

[[  TX: 0 packets, 0 errors]{lang="EN-US"}]{#struct_0_x1087_11486_109323174}

[[  RX: 0 packets, 0 errors]{lang="EN-US"}]{#struct_0_x1087_11486_2124384686}

[[PPP channel]{lang="EN-US"}]{#struct_0_x1087_11486_1832539224}[的报文收发统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送完成的报文数量，发送错误的报文数量]{style="font-family:宋体"}]{#struct_0_x1087_11486_x748600141}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收的报文数量，接收错误的报文数量]{style="font-family:宋体"}]{#struct_0_x1087_11486_1992036755}

[[ETH channel 0 traffic statistics]{lang="EN-US"}]{#struct_0_x1087_11486_2124450222}

[[  TX: 0 packets, 0 errors]{lang="EN-US"}]{#struct_0_x1087_11486_x899209243}

[[  RX: 0 packets, 0 errors]{lang="EN-US"}]{#struct_0_x1087_11486_x1004336116}

[[ETH channel]{lang="EN-US"}]{#struct_0_x1087_11486_x2046503903}[的报文收发统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送完成的报文数量，发送错误的报文数量]{style="font-family:宋体"}]{#struct_0_x1087_11486_2124515758}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收的报文数量，接收错误的报文数量]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1679570508}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1788391367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters controller]{lang="EN-US"}**]{#struct_0_x1087_11486_x1121522639}**[ ]{lang="EN-US"}[cellular]{lang="EN-US"}**

::: {#-1402041713 .myid}
[]{#_Toc404785379}[]{#struct_0_x1087_11486_x1263357918}[]{#_Toc324238749}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- dm-port open**

------------------------------------------------------------------------

[**[dm-port open]{lang="EN-US"}**]{#struct_0_x1087_11486_756798771}[命令用来打开]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dm-port open**]{lang="EN-US"}]{#struct_0_x1087_11486_x1884132502}[命令用来关闭]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2124581294}

[**[dm-port open]{lang="EN-US"}**]{#struct_0_x1087_11486_1827511316}

[**[undo dm-port open]{lang="EN-US"}**]{#struct_0_x1087_11486_1269147609}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2112912406}

[[本命令的缺省情况与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1410653207}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_500541202}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x389666250}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1096167013}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1757885142}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1576930963}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2124646830}

[[本命令用于在]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1092173418}[上打开或关闭]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[DM]{lang="EN-US"}]{#struct_0_x1087_11486_x1090323778}[（]{style="font-family:宋体"}[Diagnostic and Monitoring]{lang="EN-US"}[，诊断和监控），指某些类型的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[支持通过]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[上的调试信息输出接口输出调试信息功能，用于连接第三方的调试工具（如高通]{style="font-family:宋体"}[QXDM]{lang="EN-US"}[软件）进行诊断和监控。]{style="font-family:宋体"}

[[不同型号的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x773574002}[对于]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能的支持情况不同，具体使用请参考相应的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[用户手册。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1661152053}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x212963665}[打开]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[DM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_899839275}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] dm-port open]{lang="EN-US"}
:::

::: {#1985170617 .myid}
[]{#_Toc404785380}[]{#struct_0_x1087_11486_436896104}[]{#_Toc369265220}[]{#_Toc362278593}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- mode**

------------------------------------------------------------------------

[**[mode]{lang="EN-US"}**]{#struct_0_x1087_11486_x1908428265}[命令用来选择网络连接方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x182470507}

[**[mode]{lang="EN-US"}**[ { **1xrtt** \| **auto** \| **evdo** \| **gsm** \| **gsm-precedence** \| **hybrid** \| **lte** \| **td** \| **td-precedence** \| **wcdma** \| **wcdma-precedence** }]{lang="EN-US"}]{#struct_0_x1087_11486_x665369366}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x71634753}

[[本命令的缺省情况与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1845672205}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x897924622}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x2020017932}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1612702507}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1009064845}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1186657882}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_654824713}

[**[1xrtt]{lang="EN-US"}**]{#struct_0_x1087_11486_1380704008}[：设置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[只选择]{style="font-family:宋体"}[CDMA-1x RTT]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1087_11486_x313636483}[：设置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[自动选择网络。]{style="font-family:宋体"}

[**[evdo]{lang="NO-BOK"}**]{#struct_0_x1087_11486_x920339427}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[只选择]{style="font-family:宋体"}[CDMA-EVDO]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[gsm]{lang="NO-BOK"}**]{#struct_0_x1087_11486_1784748652}[：设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[只选择]{style="font-family:宋体"}[GSM]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[gsm-preference]{lang="NO-BOK"}**]{#struct_0_x1087_11486_2002980045}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[优先选择]{style="font-family:宋体"}[GSM]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[hybrid]{lang="NO-BOK"}**]{#struct_0_x1087_11486_x294775268}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[同时]{style="font-family:宋体"}[选择]{style="font-family:宋体"}[CDMA-EVDO]{lang="NO-BOK"}[和]{style="font-family:宋体"}[CDMA-1x RTT]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[lte]{lang="EN-US"}**]{#struct_0_x1087_11486_x1381923817}[：设置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[只选择]{style="font-family:宋体"}[LTE]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[**[td]{lang="NO-BOK"}**]{#struct_0_x1087_11486_1695097632}[：设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[只选择]{style="font-family:宋体"}[TD-SCDMA]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[td-preference]{lang="NO-BOK"}**]{#struct_0_x1087_11486_x527315638}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[优先选择]{style="font-family:宋体"}[TD-SCDMA]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[wcdma]{lang="NO-BOK"}**]{#struct_0_x1087_11486_x485252286}[：设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[只选择]{style="font-family:宋体"}[WCDMA]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[**[wcdma-preference]{lang="NO-BOK"}**]{#struct_0_x1087_11486_x2026087670}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[3G/4G Modem]{lang="NO-BOK"}[优先选择]{style="font-family:宋体"}[WCDMA]{lang="NO-BOK"}[网络。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1062216017}

[[本命令用于在]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1219227382}[3G/]{lang="NO-BOK"}[4G Modem]{lang="SV"}[上选择网络连接方式。]{style="font-family:宋体"}

[[本命令中各参数的支持情况与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_280602329}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1594383673}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_1926908413}[设置]{style="font-family:宋体"}[4G Modem]{lang="EN-US"}[只选择]{style="font-family:宋体"}[LTE]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_1382078354}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] mode lte]{lang="EN-US"}
:::

::: {#-2103162453 .myid}
[]{#_Toc404785381}[]{#struct_0_x1087_11486_1398794363}[]{#_Toc324238754}[]{#_Toc374543482}[]{#_Toc374543483}[]{#_Toc374543484}[]{#_Toc374543485}[]{#_Toc374543486}[]{#_Toc374543487}[]{#_Toc374543488}[]{#_Toc374543489}[]{#_Toc374543490}[]{#_Toc374543491}[]{#_Toc374543492}[]{#_Toc374543493}[]{#_Toc374543494}[]{#_Toc374543495}[]{#_Toc374543496}[]{#_Toc374543497}[]{#_Toc374543498}[]{#_Toc374543499}[]{#_Toc374543500}[]{#_Toc374543501}[]{#_Toc374543502}[]{#_Toc374543503}[]{#_Toc374543504}[]{#_Toc374543505}[]{#_Toc374543506}[]{#_Toc374543507}[]{#_Toc374543508}[]{#_Toc374543509}[]{#_Toc374543510}[]{#_Toc374543511}[]{#_Toc374543512}[]{#_Toc374543513}[]{#_Toc374543514}[]{#_Toc374543515}[]{#_Toc374543516}[]{#_Toc374543517}[]{#_Toc374543518}[]{#_Toc374543519}[]{#_Toc374543520}[]{#_Toc374543521}[]{#_Toc374543522}[]{#_Toc374543523}[]{#_Toc374543524}[]{#_Toc374543525}[]{#_Toc374543526}[]{#_Toc374543527}[]{#_Toc374543528}[]{#_Toc374543529}[]{#_Toc374543530}[]{#_Toc374543531}[]{#_Toc374543532}[]{#_Toc374543533}[]{#_Toc374543534}[]{#_Toc374543535}[]{#_Toc314226268}[]{#_Toc374543536}[]{#_Toc374543537}[]{#_Toc374543538}[]{#_Toc374543539}[]{#_Toc374543540}[]{#_Toc374543541}[]{#_Toc374543542}[]{#_Toc374543543}[]{#_Toc374543544}[]{#_Toc374543545}[]{#_Toc374543546}[]{#_Toc374543547}[]{#_Toc374543548}[]{#_Toc374543549}[]{#_Toc374543550}[]{#_Toc374543551}[]{#_Toc374543552}[]{#_Toc374543553}[]{#_Toc374543554}[]{#_Toc374543555}[]{#_Toc374543556}[]{#_Toc374543557}[]{#_Toc374543558}[]{#_Toc374543559}[]{#_Toc374543560}[]{#_Toc374543561}[]{#_Toc340569951}[]{#_Toc340569952}[]{#_Toc340569953}[]{#_Toc340569954}[]{#_Toc340569955}[]{#_Toc340569956}[]{#_Toc340569957}[]{#_Toc340569958}[]{#_Toc340569959}[]{#_Toc340569960}[]{#_Toc340569961}[]{#_Toc340569962}[]{#_Toc340569963}[]{#_Toc340569964}[]{#_Toc340569965}[]{#_Toc340569966}[]{#_Toc340569967}[]{#_Toc340569968}[]{#_Toc340569969}[]{#_Toc340569970}[]{#_Toc340569971}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- modem reboot**

------------------------------------------------------------------------

[**[modem reboot]{lang="EN-US"}**]{#struct_0_x1087_11486_31861438}[命令用来手动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1855196455}

[**[modem reboot]{lang="EN-US"}**]{#struct_0_x1087_11486_x2117014505}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1658355956}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_2124646831}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1092238954}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x267471846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_9475555}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x819231744}

[[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x2008195748}[在运行过程中能够自动检测异常，并实施自动重启。如果无法自动重启，用户可以通过本命令手动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1309108431}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_879085730}[手动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_2123663791}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] modem reboot]{lang="EN-US"}
:::

::: {#772536084 .myid}
[]{#_Toc404785382}[]{#struct_0_x1087_11486_1945339243}[]{#_Toc324238762}[]{#_Toc329768479}[]{#_Toc329768759}[]{#_Toc329790640}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- modem response**

------------------------------------------------------------------------

[**[modem response]{lang="EN-US"}**]{#struct_0_x1087_11486_x326214296}[命令用来配置系统向]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[下发配置指令后，等待其回复的时间间隔，以及]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[连续不响应系统配置指令（配置指令失败或配置指令响应超时）次数的阈值，达到系统配置的阈值后，自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo modem response]{lang="EN-US"}**]{#struct_0_x1087_11486_1967992385}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1058063389}

[**[modem response timer]{lang="EN-US"}**[ *time* **auto-recovery** *threshold*]{lang="EN-US"}]{#struct_0_x1087_11486_604894060}

[**[undo modem response]{lang="EN-US"}**]{#struct_0_x1087_11486_x867490056}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_713892167}

[[系统等待]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_2088077282}[回复的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[连续不响应系统配置指令次数的阈值为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2123729327}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_382615733}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_459781799}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_2024126163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_879377858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1778044242}

[**[timer]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1087_11486_x604695273}[：系统向]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[下发配置指令后，等待其回复的时间间隔。若在该时间内系统没收到]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的回复，则认为]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[不响应系统配置指令。]{style="font-family:宋体"}*[time]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[auto-recovery]{lang="EN-US"}**[ *threshold*]{lang="EN-US"}]{#struct_0_x1087_11486_x78235475}[：]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[连续不响应系统配置指令次数的阈值，达到阈值后系统自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。当]{style="font-family:宋体"}*[threshold]{lang="EN-US"}*[配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，关闭自动重启功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1611536143}

[[3G/4G]{lang="EN-US"}]{#struct_0_x1087_11486_x604498665}[无线网络的不稳定运行或应用环境变化可能导致]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[功能故障，无法自动拨号并连接网络。设备提供自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[功能，尽可能减少需要用户手工重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的情况。]{style="font-family:宋体"}

[[开启自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x604302057}[功能后，如果连续多次下发配置指令失败或配置指令响应超时，系统将自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。为避免因配置错误引起的多次拨号失败，而导致的反复自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的情况，系统仅在上次自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[后有过至少一次拨号成功记录，并且多次发配置指令失败或配置指令响应超时的情况下才会自动重启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1601107995}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_1992828924}[配置系统向]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[下发配置指令时，等待其回复的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[模块连续]{style="font-family:宋体"}[4]{lang="EN-US"}[次不响应系统配置指令，则自动重启。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x604236521}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] modem response timer 20 auto-recovery 4]{lang="EN-US"}
:::

::: {#1762115954 .myid}
[]{#_Toc404785383}[]{#struct_0_x1087_11486_x464594445}[]{#_Toc324238758}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin modify**

------------------------------------------------------------------------

[**[pin modify]{lang="EN-US"}**]{#struct_0_x1087_11486_1928917909}[命令用来修改]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，修改后的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码保存在]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡上。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2000928286}

[**[pin modify]{lang="EN-US"}**[ *current-pin new-pin*]{lang="EN-US"}]{#struct_0_x1087_11486_x575489296}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1990924012}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x868483534}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1692696342}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1571208804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x605219561}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1855064620}

[*[current-pin]{lang="EN-US"}*]{#struct_0_x1087_11486_819417767}[：插在]{style="font-family:宋体"}[3G/4G ]{lang="SV"}[Modem]{lang="EN-US"}[上的]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，由]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[位数字组成。]{style="font-family:
宋体"}

[*[new-pin]{lang="EN-US"}*]{#struct_0_x1087_11486_x1849825547}[：用户重新设置的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，由]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[位数字组成。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_807109186}

[[本命令用于在]{style="font-family:宋体"}]{#struct_0_x1087_11486_714004983}[3G/4G Modem]{lang="SV"}[上修改]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1087_11486_224084928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果开启了]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1438142408}[的]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能，]{lang="EN-US" style="font-family:宋体"}[修改]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码后，需要配置]{style="font-family:宋体"}**[pin verify]{lang="EN-US"}**[命令以保持和修改后的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果连续多次修改]{style="font-family:宋体"}]{#struct_0_x1087_11486_1998388786}[PIN]{lang="EN-US"}[码失败，会导致]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡被锁。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1087_11486_x605154025}[SIM/UIM]{lang="EN-US"}[卡被锁，必须先通过]{style="font-family:宋体"}**[pin unlock]{lang="EN-US"}**[命令来解锁。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[部分]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1616526516}[3G/4G Modem]{lang="EN-US"}[必须在启用]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证，并且]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证通过后才可以修改]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_643625402}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1323883290}[修改]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_1947185021}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] pin modify 1234 4321]{lang="EN-US"}

[PIN will be changed to "4321". Continue? \[Y/N\]:y]{lang="EN-US"}

[PIN has been changed successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1183573476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin unlock]{lang="EN-US"}**]{#struct_0_x1087_11486_875495983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verification]{lang="EN-US"}**]{#struct_0_x1087_11486_470446080}**[ enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verify]{lang="EN-US"}**]{#struct_0_x1087_11486_x604695272}
:::

::: {#970352933 .myid}
[]{#_Toc404785384}[]{#struct_0_x1087_11486_x78301011}[]{#_Toc324238759}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin unlock**

------------------------------------------------------------------------

[**[pin unlock]{lang="EN-US"}**]{#struct_0_x1087_11486_78595078}[命令用来对]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[上的]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡进行]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码解锁。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1599071310}

[**[pin unlock]{lang="EN-US"}**[ *puk new-pin*]{lang="EN-US"}]{#struct_0_x1087_11486_324330514}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2139562722}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_1253810362}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1620237297}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x509951619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x604629736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1076955925}

[*[puk]{lang="EN-US"}*]{#struct_0_x1087_11486_1110544815}[：插在]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[上的]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PUK]{lang="EN-US"}[码，由网络提供商提供，由]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[位数字组成。]{style="font-family:
宋体"}

[*[new-pin]{lang="EN-US"}*]{#struct_0_x1087_11486_x604564200}[：用户重新设置的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，由]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[位数字组成。重新设置的]{style="font-family:
宋体"}[PIN]{lang="EN-US"}[码保存在]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡上。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1518125998}

[[本命令用于在]{style="font-family:宋体"}]{#struct_0_x1087_11486_838230733}[3G/4G Modem]{lang="SV"}[上对]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡进行]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码解锁。下列情况可能导致]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码被锁住：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[连续多次修改]{style="font-family:宋体"}]{#struct_0_x1087_11486_x56365270}[PIN]{lang="EN-US"}[码失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[连续多次开启或关闭]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1626076485}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[连续多次]{style="font-family:宋体"}]{#struct_0_x1087_11486_x604498664}[PIN]{lang="EN-US"}[码认证失败。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_282957375}[码被锁住，需要用户使用]{style="font-family:宋体"}[PUK]{lang="EN-US"}[码将]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码解锁，否则]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的数据通信功能不可用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1278835370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果开启了]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x2021922454}[的]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能，解锁]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[码后，需要配置]{lang="EN-US" style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令以保持和重新设置的]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[码一致]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果连续多次解锁失败，可能会导致]{style="font-family:宋体"}]{#struct_0_x1087_11486_1247699226}[SIM/UIM]{lang="EN-US"}[卡被永久锁定，无法使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1276879611}[SIM/UIM]{lang="EN-US"}[卡被永久锁定，请联系]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的运营商为]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡解锁。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1771621458}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_855162918}[使用]{style="font-family:宋体"}[PUK]{lang="EN-US"}[码解锁]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_67464876}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] pin unlock 87654321 1234]{lang="EN-US"}

[PIN will be unlocked and changed to "1234". Continue? \[Y/N\]:y]{lang="EN-US"}

[PIN has been unlocked and changed successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x604433128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin modify]{lang="EN-US"}**]{#struct_0_x1087_11486_x826573624}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verification]{lang="EN-US"}**]{#struct_0_x1087_11486_1209949960}**[ enable]{lang="EN-US"}**
:::

::: {#-651948497 .myid}
[]{#_Toc404785385}[]{#struct_0_x1087_11486_x530564040}[]{#_Toc324238760}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin verification enable**

------------------------------------------------------------------------

[**[pin verification enable]{lang="EN-US"}**]{#struct_0_x1087_11486_1963266059}[命令用来开启]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能。]{style="font-family:宋体"}

[**[undo pin verification enable]{lang="EN-US"}**]{#struct_0_x1087_11486_x865267789}[命令用来关闭]{style="font-family:
宋体"}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:
宋体"}[PIN]{lang="EN-US"}[码认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1141788887}

[**[pin verification enable]{lang="EN-US"}**[ \[ *pin* \]]{lang="EN-US"}]{#struct_0_x1087_11486_x1726093243}

[**[undo pin verification enable]{lang="EN-US"}**[ \[ *pin* \]]{lang="EN-US"}]{#struct_0_x1087_11486_1888703660}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x604367592}

[[本命令的缺省情况与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x2020192536}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2048938139}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x1315579167}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x352753980}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1323996387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_260655499}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1322718736}

[*[pin]{lang="EN-US"}*]{#struct_0_x1087_11486_x217048994}[：插在]{style="font-family:宋体"}[3G/4G ]{lang="SV"}[Modem]{lang="EN-US"}[上的]{style="font-family:
宋体"}[SIM/UIM]{lang="EN-US"}[卡的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，由]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[位数字组成。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x604302056}

[[本命令用于在]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1601042459}[3G/4G Modem]{lang="SV"}[上]{style="font-family:宋体"}[[开启或关闭]{style="font-family:宋体"}]{.MsoCommentReference}[PIN]{lang="EN-US"}[码认证功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果开启了]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1648045913}[的]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能，当]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[插入或]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[重启时，会使用]{lang="EN-US" style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令配置的]{lang="EN-US" style="font-family:宋体"}[PIN]{lang="EN-US"}[码进行认证，否则]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[数据通信功能不可用。重启]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的途径包括：重启设备、使用]{lang="EN-US" style="font-family:宋体"}**[modem reboot]{lang="EN-US"}**[命令重启]{lang="EN-US" style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[、热拔插]{lang="EN-US" style="font-family:宋体"}[USB 3G/4G Modem]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[对于]{style="font-family:宋体"}[SIC-3G/4G-CDMA]{lang="EN-US"}[模块，只有设备冷启动后，才需要重新进行]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果关闭了]{style="font-family:宋体"}]{#struct_0_x1087_11486_1396477275}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能，不需要进行]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证就可以进行]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[数据通信。]{style="font-family:宋体"}

[[如果开启了]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x1716990783}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能，需要通过]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令将]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码保存在设备上，在需要认证时，自动完成]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1087_11486_2122601647}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启或关闭]{style="font-family:宋体"}]{#struct_0_x1087_11486_1576967232}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能时，可能要求输入当前的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。该要求与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[设备的型号有关，请以设备的实际情况为准。如果连续多次]{style="font-family:宋体"}[[开启或关闭]{style="font-family:宋体"}]{.MsoCommentReference}[3G/4G Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能失败，可能会导致]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡被锁。如果]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡被锁，可以通过]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **unlock**]{lang="EN-US"}[命令来解锁。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[部分]{style="font-family:宋体"}]{#struct_0_x1087_11486_1374583527}[3G/4G Modem]{lang="EN-US"}[在启用]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能后，必须]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证通过后才可以关闭]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1614981373}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x604236520}[开启]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x464659981}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] pin verification enable 1234]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2046292305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin unlock]{lang="EN-US"}**]{#struct_0_x1087_11486_1231900125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verify]{lang="EN-US"}**]{#struct_0_x1087_11486_x1220996110}
:::

::: {#1283859823 .myid}
[]{#_Toc404785386}[]{#struct_0_x1087_11486_x462452841}[]{#_Toc324238761}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- pin verify**

------------------------------------------------------------------------

[**[pin verify]{lang="EN-US"}**]{#struct_0_x1087_11486_x1769993602}[命令用来配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[进行认证的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[**[undo pin verify]{lang="EN-US"}**]{#struct_0_x1087_11486_1551831149}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x605219560}

[**[pin verify]{lang="EN-US"}**[ { **cipher** *ciphered-pin* \| **simple** *pin* }]{lang="EN-US"}]{#struct_0_x1087_11486_x605154024}

[**[undo pin verify]{lang="EN-US"}**]{#struct_0_x1087_11486_x1616592052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2036227312}

[[未配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x974805594}[进行认证的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x861904677}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_1830351888}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1006608539}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x578107267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x604695275}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x78366547}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1087_11486_x604629739}[：表示以密文形式输入密码。]{style="font-family:宋体"}

[*[ciphered-pin]{lang="EN-US"}*]{#struct_0_x1087_11486_x604498667}[：插在]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[上的]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的密文]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，由]{style="font-family:宋体"}[37]{lang="EN-US"}[～]{style="font-family:宋体"}[41]{lang="EN-US"}[个字符的字符串组成。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1087_11486_x604433131}[：表示以明文形式输入密码。]{style="font-family:宋体"}

[*[pin]{lang="EN-US"}*]{#struct_0_x1087_11486_x825983799}[：插在]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[上的]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡的明文]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码，由]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[位数字组成。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x590979177}

[[开启了]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x604367595}[的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能后，当]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[插入或重启时，需要通过]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令输入]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码进行认证，如果输入的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码正确，则]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证通过，否则，]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证失败。如果连续多次]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证失败，可能会导致]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡被锁。如果]{style="font-family:宋体"}[SIM/UIM]{lang="EN-US"}[卡被锁，可以通过]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **unlock**]{lang="EN-US"}[命令来解锁。]{style="font-family:宋体"}

[[用户可以在需要]{style="font-family:宋体"}[PIN]{lang="EN-US"}]{#struct_0_x1087_11486_x2019864856}[码认证时配置]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令，也可以提前配置]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令，只要配置一次]{style="font-family:宋体"}**[pin]{lang="EN-US"}**[ **verify**]{lang="EN-US"}[命令，]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码就会保存在设备上，在需要认证时，自动完成]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_831189844}

[[#  ]{lang="EN-US"}]{#struct_0_x1087_11486_758957202}[配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[进行认证的]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x1751157712}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] pin verify simple 1234]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1961960470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin unlock]{lang="EN-US"}**]{#struct_0_x1087_11486_x191424896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pin verification]{lang="EN-US"}**]{#struct_0_x1087_11486_392427672}**[ ]{lang="EN-US"}[enable]{lang="EN-US"}**
:::

::: {#1743928426 .myid}
[]{#_Toc404785387}[]{#struct_0_x1087_11486_x604302059}[]{#_Toc324238750}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- plmn search**

------------------------------------------------------------------------

[**[plmn search]{lang="EN-US"}**]{#struct_0_x1087_11486_x1600452635}[命令用来搜索移动网络。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x823669731}

[**[plmn search]{lang="EN-US"}**]{#struct_0_x1087_11486_1837308682}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1768077838}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x1490058229}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1737628833}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_219705046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x383300558}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x604236523}

[[本命令用于触发]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x464463373}[搜索移动网络。]{style="font-family:宋体"}

[[搜索移动网络需要等待几分钟，完成搜索后，命令行会给出提示，显示搜索到的移动网络。]{style="font-family:宋体"}]{#struct_0_x1087_11486_415072026}

[[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x397078411}[使用时，需要在]{style="font-family:宋体"}[PLMN]{lang="EN-US"}[（]{style="font-family:宋体"}[Public Land Mobile Network]{lang="EN-US"}[，公共陆地移动网络）进行选择接入的移动网络。如果用户需要手工指定接入的移动网络，则需要先搜索移动网络，获取当前区域内有信号的移动网络列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x870416280}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x775569879}[搜索移动网络。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x605219563}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] plmn search]{lang="EN-US"}

[PLMN search done.]{lang="EN-US"}

[Available PLMNs:]{lang="EN-US"}

[PLMN No.     MCC    MNC    Status     Type]{lang="EN-US"}

[01           460    00     Current    GSM]{lang="EN-US"}

[02           460    00     Available  UTRAN]{lang="EN-US"}

[03           460    01     Forbidden  GSM]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[plmn search]{lang="EN-US"}]{#struct_0_x1087_11486_1854933548}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1477706257}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_439076381}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_1835329085}

[[PLMN No]{lang="EN-US"}]{#struct_0_x1087_11486_x85572237}

[[序号]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1111422603}

[[MCC]{lang="EN-US"}]{#struct_0_x1087_11486_x594873216}

[[移动国家编码]{style="font-family:宋体"}]{#struct_0_x1087_11486_x605154027}

[[MNC]{lang="EN-US"}]{#struct_0_x1087_11486_x1616657588}

[[移动网络编码，表示运营商，比如：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x986764519}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[00]{lang="EN-US"}]{#struct_0_x1087_11486_x1129056765}[、]{lang="EN-US" style="font-family:宋体"}[02]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[07]{lang="EN-US"}[：]{style="font-family:宋体"}[表示移动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[01]{lang="EN-US"}]{#struct_0_x1087_11486_x1532341292}[：]{style="font-family:宋体"}[表示联通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[03]{lang="EN-US"}]{#struct_0_x1087_11486_x1871136044}[：]{style="font-family:宋体"}[表示电信]{lang="EN-US" style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x1087_11486_x66971782}

[[移动网络的状态，其取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x479506015}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}[urrent]{lang="EN-US"}]{#struct_0_x1087_11486_1004584451}[：]{style="font-family:
  宋体"}[表示当前正在使用的网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}[vailable]{lang="EN-US"}]{#struct_0_x1087_11486_x604695274}[：]{style="font-family:宋体"}[表示网络可达]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}[orbidden]{lang="EN-US"}]{#struct_0_x1087_11486_x78432083}[：]{style="font-family:宋体"}[表示网络被禁止使用]{lang="EN-US" style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1087_11486_369509541}

[[搜索到的移动网络类型]{style="font-family:宋体"}]{#struct_0_x1087_11486_252227068}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1429919964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_65518996}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[plmn select]{lang="EN-US"}**]{#struct_0_x1087_11486_2099791028}

::: {#-985769827 .myid}
[]{#_Toc404785388}[]{#struct_0_x1087_11486_x604629738}[]{#_Toc324238751}[]{#_Toc311559476}[]{#_Toc311559909}[]{#_Toc311559477}[]{#_Toc311559910}[]{#_Toc311559478}[]{#_Toc311559911}[]{#_Toc311559479}[]{#_Toc311559912}[]{#_Toc311559480}[]{#_Toc311559913}[]{#_Toc311559481}[]{#_Toc311559914}[]{#_Toc311559482}[]{#_Toc311559915}[]{#_Toc311559483}[]{#_Toc311559916}[]{#_Toc311559484}[]{#_Toc311559917}[]{#_Toc311559485}[]{#_Toc311559918}[]{#_Toc311559486}[]{#_Toc311559919}[]{#_Toc311559487}[]{#_Toc311559920}[]{#_Toc311559488}[]{#_Toc311559921}[]{#_Toc311559489}[]{#_Toc311559922}[]{#_Toc311559490}[]{#_Toc311559923}[]{#_Toc311559491}[]{#_Toc311559924}[]{#_Toc311559492}[]{#_Toc311559925}[]{#_Toc311559493}[]{#_Toc311559926}[]{#_Toc311559494}[]{#_Toc311559927}[]{#_Toc311559495}[]{#_Toc311559928}[]{#_Toc311559496}[]{#_Toc311559929}[]{#_Toc311559497}[]{#_Toc311559930}[]{#_Toc311559498}[]{#_Toc311559931}[]{#_Toc311559499}[]{#_Toc311559932}[]{#_Toc311559500}[]{#_Toc311559933}[]{#_Toc311559501}[]{#_Toc311559934}[]{#_Toc311559502}[]{#_Toc311559935}[]{#_Toc311559503}[]{#_Toc311559936}[]{#_Toc311559504}[]{#_Toc311559937}[]{#_Toc311559505}[]{#_Toc311559938}[]{#_Toc311559506}[]{#_Toc311559939}[]{#_Toc311559507}[]{#_Toc311559940}[]{#_Toc311559508}[]{#_Toc311559941}[]{#_Toc311559509}[]{#_Toc311559942}[]{#_Toc311559510}[]{#_Toc311559943}[]{#_Toc311559511}[]{#_Toc311559944}[]{#_Toc311559512}[]{#_Toc311559945}[]{#_Toc311559513}[]{#_Toc311559946}[]{#_Toc311559514}[]{#_Toc311559947}[]{#_Toc311559515}[]{#_Toc311559948}[]{#_Toc311559516}[]{#_Toc311559949}[]{#_Toc311559517}[]{#_Toc311559950}[]{#_Toc311559518}[]{#_Toc311559951}[]{#_Toc311559519}[]{#_Toc311559952}[]{#_Toc311559520}[]{#_Toc311559953}[]{#_Toc311559521}[]{#_Toc311559954}[]{#_Toc311559522}[]{#_Toc311559955}[]{#_Toc311559523}[]{#_Toc311559956}[]{#_Toc311559524}[]{#_Toc311559957}[]{#_Toc311559525}[]{#_Toc311559958}[]{#_Toc311559526}[]{#_Toc311559959}[]{#_Toc311559527}[]{#_Toc311559960}[]{#_Toc311559528}[]{#_Toc311559961}[]{#_Toc311559529}[]{#_Toc311559962}[]{#_Toc311559530}[]{#_Toc311559963}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- plmn select**

------------------------------------------------------------------------

[**[plmn select]{lang="EN-US"}**]{#struct_0_x1087_11486_1077873429}[命令用来配置选择移动网络的方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x846288740}

[**[plmn select]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_x1087_11486_x247089792}**[auto]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| **manual** *mcc mnc* }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x83220012}

[[本命令的缺省情况与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x713760273}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_770626240}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x794353429}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x604564202}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1517994926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x949758357}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x243812794}

[**[auto]{lang="EN-US"}**]{#struct_0_x1087_11486_973023395}[：表示自动选择]{style="font-family:宋体"}[PLMN]{lang="EN-US"}[（]{style="font-family:宋体"}[Public Land Mobile Network]{lang="EN-US"}[，公共地带移动网络）。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_x1087_11486_x928209020}[：表示人工指定]{style="font-family:宋体"}[PLMN]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mcc]{lang="EN-US"}*]{#struct_0_x1087_11486_x350545369}[：]{style="font-family:宋体"}[MCC]{lang="EN-US"}[（]{style="font-family:宋体"}[Mobile Country Code]{lang="EN-US"}[，移动国家编码），取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mnc]{lang="EN-US"}*]{#struct_0_x1087_11486_1046326117}[：]{style="font-family:宋体"}[MNC]{lang="EN-US"}[（]{style="font-family:宋体"}[Mobile Network Code]{lang="EN-US"}[，移动网络编码），取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1460500392}

[[本命令用于在]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x604498666}[上配置选择移动网络的方式。]{style="font-family:宋体"}

[[当配置选择移动网络的方式为人工指定时，需要先通过]{style="font-family:宋体"}**[plmn search]{lang="EN-US"}**]{#struct_0_x1087_11486_282826303}[命令搜索移动网络。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_655983853}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x864047768}[配置选择移动网络的方式为人工指定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x20164453}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] plmn select manual 65524 65524]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x693713907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_469223542}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[plmn search]{lang="EN-US"}**]{#struct_0_x1087_11486_1987682746}
:::

::: {#1801937399 .myid}
[]{#_Toc404785389}[]{#struct_0_x1087_11486_x604433130}[]{#_Toc324238752}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- profile create**

------------------------------------------------------------------------

[**[profile create]{lang="EN-US"}**]{#struct_0_x1087_11486_x826049335}[命令用来创建]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的参数模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1975261672}

[**[profile create]{lang="EN-US"}***[ profile-number ]{lang="EN-US"}*[{ **dynamic** \| **static** *apn* } **authentication-mode** { **none** \| { **chap** \| **pap** } **user** *username* \[ **password** *password* \] }]{lang="EN-US"}]{#struct_0_x1087_11486_x69287761}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1215863620}

[[本命令的缺省情况与]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x813652402}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1905453481}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x909005101}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_346568581}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x604367594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x2019799320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1728311926}

[*[profile-number]{lang="EN-US"}*]{#struct_0_x1087_11486_1784273878}[：]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的参数模板编号。不同型号的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_x1087_11486_x604302058}[：由运营商根据接入用户动态分配接入点。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}***[ apn]{lang="EN-US"}*]{#struct_0_x1087_11486_x604236522}[：指定的由运营商提供的接入点名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[个字符的字符串，是否大小写敏感和运营商有关。]{style="font-family:宋体"}

[**[authentication-mode]{lang="EN-US"}**]{#struct_0_x1087_11486_x605219562}[：认证方式。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1087_11486_x605154026}[：不认证。]{style="font-family:宋体"}

[**[chap]{lang="EN-US"}**]{#struct_0_x1087_11486_x604695277}[：认证方式为]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pap]{lang="EN-US"}**]{#struct_0_x1087_11486_x604629741}[：认证方式为]{style="font-family:宋体"}[PAP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user]{lang="EN-US"}***[ username]{lang="EN-US"}*]{#struct_0_x1087_11486_1077283610}[：认证用户名，由运营商提供。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[password]{lang="EN-US"}***[ password]{lang="EN-US"}*]{#struct_0_x1087_11486_x604564205}[：认证密码，由运营商提供。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1518322606}

[[本命令用于在]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_x640410607}[上创建参数模板。]{style="font-family:宋体"}

[[参数模板可以配置接入点和认证方式，]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1607274829}[会根据配置的接入点和认证方式，来和对应的服务商进行认证：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当选用]{style="font-family:宋体"}]{#struct_0_x1087_11486_184153749}[None]{lang="EN-US"}[方式时，不需要输入用户名和密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当选用]{style="font-family:宋体"}]{#struct_0_x1087_11486_x604498669}[CHAP]{lang="EN-US"}[或]{style="font-family:宋体"}[PAP]{lang="EN-US"}[方式时，需要根据运营商的要求，选择配置用户名和密码，其中]{style="font-family:宋体"}*[username]{lang="EN-US"}*[字段是必选的，而]{style="font-family:宋体"}*[password]{lang="EN-US"}*[字段是可选的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_282760767}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_1677243145}[创建]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的参数模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，指定的接入点名称为]{style="font-family:宋体"}[cmnet]{lang="EN-US"}[，认证方式采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_1469753831}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] profile create 1 static cmnet authentication-mode pap user abc password abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1640280383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_394478607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[profile delete]{lang="EN-US"}**]{#struct_0_x1087_11486_538148824}
:::

::: {#-217613369 .myid}
[]{#_Toc404785390}[]{#struct_0_x1087_11486_x1849048546}[]{#_Toc324238753}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- profile delete**

------------------------------------------------------------------------

[**[profile delete]{lang="EN-US"}**]{#struct_0_x1087_11486_x604433133}[命令用来删除]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的参数模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x825852727}

[**[profile delete]{lang="EN-US"}**[ *profile-number*]{lang="EN-US"}]{#struct_0_x1087_11486_956558100}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2140333547}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_1818214931}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_265476048}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1075714152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1216153367}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_237414199}

[*[profile-number]{lang="EN-US"}*]{#struct_0_x1087_11486_x604367597}[：]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的参数模板编号。不同型号的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x647622872}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_419768412}[删除]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的参数模板]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_361830110}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] profile delete 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1338345382}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_x1564291537}

[]{#struct_0_x1087_11486_1619944006}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[profile]{lang="EN-US"}**]{#OLE_LINK3}**[ create]{lang="EN-US"}**
:::

::: {#49066820 .myid}
[]{#_Toc404785391}[]{#struct_0_x1087_11486_x2022184599}[]{#_Toc331148424}[]{#_Toc195409925}[]{#_Toc149979604}[]{#_Toc144810340}[]{#_Toc144782901}[]{#_Toc375318009}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- profile main**

------------------------------------------------------------------------

[**[profile main]{lang="EN-US"}**]{#struct_0_x1087_11486_546489425}[命令用来配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[拨号使用的主备参数模板。]{style="font-family:宋体"}

[**[undo profile main]{lang="EN-US"}**]{#struct_0_x1087_11486_782635975}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2022119063}

[**[profile main ]{lang="EN-US"}**]{#struct_0_x1087_11486_847992849}*[main-profile-number ]{lang="EN-US"}***[backup]{lang="EN-US"}**[ ]{lang="EN-US"}*[backup-profile-number]{lang="EN-US"}*

[**[undo profile main]{lang="EN-US"}**]{#struct_0_x1087_11486_683125462}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x955636506}

[[3G/4G Modem]{lang="EN-US"}]{#struct_0_x1087_11486_1038169897}[使用参数模板]{style="font-family:宋体"}[1]{lang="EN-US"}[进行拨号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1021134130}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x419405484}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1490235510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x103369025}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x917304714}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2021529239}

[*[main-profile-numbe]{lang="EN-US"}*]{#struct_0_x1087_11486_x1230979499}[：主参数模板索引。不同型号的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[backup]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1087_11486_x2090539879}*[backup-profile-number]{lang="EN-US"}*[：备份参数模板索引。不同型号的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x376318497}

[[配置]{style="font-family:宋体"}**[profile main]{lang="EN-US"}**]{#struct_0_x1087_11486_763977039}[命令后，]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[每次拨号都优先选择主参数模板，如果主参数模板拨号失败，将使用备份参数模板进行拨号。无论备份参数模板拨号是否成功，下次拨号时都使用主参数模板拨号。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1087_11486_289077958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用的主备参数模板的用户名和密码必须配成一样的。]{style="font-family:宋体"}]{#struct_0_x1087_11486_x2005585262}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令的配置会在下次拨号时生效，不会影响当前的拨号结果。]{style="font-family:宋体"}]{#struct_0_x1087_11486_110151552}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1974626892}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1598689170}[配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[拨号使用主参数模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，备份参数模板]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x2021463703}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] profile main 1 backup 2]{lang="EN-US"}
:::

::: {#-1519550549 .myid}
[]{#_Toc404785392}[]{#struct_0_x1087_11486_x604302061}[]{#_Toc327887958}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- reset counters controller cellular**

------------------------------------------------------------------------

[**[reset counters controller cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_x1600976924}[命令用来清除]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_980838257}

[**[reset counters controller]{lang="EN-US"}**[ **cellular** \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_x1087_11486_1783060702}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_446855025}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x651149585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x622517702}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1762947939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x604236525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x464332301}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1087_11486_1970473497}[：]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2134202075}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x1087_11486_791824733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*]{#struct_0_x1087_11486_x1464639495}[，则清除所有]{lang="EN-US" style="font-family:
宋体"}[Cellular]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*]{#struct_0_x1087_11486_859942196}[，则清除指定]{lang="EN-US" style="font-family:
宋体"}[Cellular]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1465908532}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_2006298060}[清除接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters controller cellular 2/4/0]{lang="EN-US"}]{#struct_0_x1087_11486_x605219565}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1854802476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cellular]{lang="EN-US"}**]{#struct_0_x1087_11486_826882776}
:::

::: {#-361739400 .myid}
[]{#_Toc404785393}[]{#struct_0_x1087_11486_x1313562980}[]{#_Toc324238748}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- sendat**

------------------------------------------------------------------------

[**[sendat]{lang="EN-US"}**]{#struct_0_x1087_11486_x924211818}[命令用来手工向]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[发送配置指令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1195537744}

[**[sendat]{lang="EN-US"}**[ *at-string*]{lang="EN-US"}]{#struct_0_x1087_11486_1663028385}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_452898539}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x1877426245}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x605154029}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1617312948}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x376023868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1558083124}

[*[at-string]{lang="SV"}*]{#struct_0_x1087_11486_x604629740}[：配置]{style="font-family:宋体"}[指令字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[300]{lang="SV"}[个字符的字符串。该字符串的内容格式不同产品有所区别，可能是]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令（]{style="font-family:宋体"}["]{style="font-family:宋体"}[+++]{lang="SV"}["]{style="font-family:宋体"}[和]{style="font-family:
宋体"}["]{style="font-family:宋体"}[A/]{lang="SV"}["]{style="font-family:宋体"}[以及任意以]{style="font-family:宋体"}[AT]{lang="SV"}[开头的字符串，]{style="font-family:宋体"}[AT]{lang="SV"}[指令的详细解释请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入命令参考]{style="font-family:宋体"}[/Modem]{lang="EN-US"}[管理"中的命令]{style="font-family:宋体"}**[sendat]{lang="EN-US"}**[），也可能是]{style="font-family:宋体"}[CNS]{lang="EN-US"}[格式的报文（样例请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-7]{lang="EN-US"}](?-361739400#_Ref329768282)[）]{style="font-family:宋体"}[[\_Ref310583627]{lang="EN-US"}](#_Ref310583627)[。本参数的具体格式与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[]{#struct_0_x1087_11486_1077349146}[[表1-7 ]{lang="EN-US"}[CNS]{lang="EN-US"}]{#_Ref329768282}[格式报文举例]{style="font-family:黑体"}

[]{#table_struct_0_1479909517}[[指令]{style="font-family:黑体"}]{#struct_0_x1087_11486_361044915}
:::

[[说明]{style="font-family:黑体"}]{#struct_0_x1087_11486_301804904}

[**[CNS]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1087_11486_x224514852}

[[控制]{style="font-family:宋体"}[CNS]{lang="EN-US"}]{#struct_0_x1087_11486_2895570}[心跳检测开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n = ]{lang="EN-US"}*]{#struct_0_x1087_11486_x604564204}[00000500000000000000]{lang="EN-US"}[，打开]{style="font-family:宋体"}[CNS]{lang="EN-US"}[心跳检测开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n = ]{lang="EN-US"}*]{#struct_0_x1087_11486_1518388142}[00000800000000000000]{lang="EN-US"}[，关闭]{style="font-family:宋体"}[CNS]{lang="EN-US"}[心跳检测开关]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_40872483}

[**[sendat]{lang="EN-US"}**]{#struct_0_x1087_11486_116179516}[命令不检查配置指令的合法性，直接将用户输入的字符串送至]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[（遇到小写字母自动转化为大写字母）。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1087_11486_1875024504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sendat]{lang="EN-US"}**]{#struct_0_x1087_11486_x604498668}[命令]{lang="EN-US" style="font-family:宋体"}[一次只能配置一条]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[指令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1087_11486_282695231}[配置]{style="font-family:
宋体"}[指令配置]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[后，]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的工作状态会被改变，有可能导致]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[的状态混乱从而影响到拨号等基本功能。]{style="font-family:宋体"}[请在专业人员的指导下慎重使用此功能。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_56495947}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x92184274}[向]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[发送拨号指令，呼叫号码]{style="font-family:宋体"}[169]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x1321800946}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] sendat ATD169]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1603505924}[向]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[发送打开]{style="font-family:宋体"}[CNS]{lang="EN-US"}[心跳检测开关的指令。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x604433132}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] sendat cns00000500000000000000]{lang="EN-US"}

::: {#1170655049 .myid}
[]{#_Toc404785394}[]{#struct_0_x1087_11486_1956056950}

**3G/4G Modem管理 \-- 3G/4G Modem管理公共配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1087_11486_x1400739470}[命令用来关闭]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x1087_11486_2082527708}[命令用来打开]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x772826405}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1087_11486_x2033926492}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1087_11486_x1131698934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_652423893}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_377076465}[接口处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_436010774}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_1365864097}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1904747831}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1663336099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x556768211}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1253545858}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1194074780}[关闭接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_2048513518}

[\[Sysname\] interface cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] shutdown]{lang="EN-US"}
:::

::: {#-772291685 .myid}
[]{#_Toc404785396}[]{#struct_0_x1087_11486_x825918263}[]{#_Toc327887959}

**3G/4G Modem管理 \-- 3G Modem管理专用配置命令 \-- serial-set**

------------------------------------------------------------------------

[**[serial-set]{lang="EN-US"}**]{#struct_0_x1087_11486_1732355727}[命令用来将]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口通道化出同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口。]{style="font-family:宋体"}

[**[undo serial-set]{lang="EN-US"}**]{#struct_0_x1087_11486_1289408052}[命令用来将]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口通道化出的同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x599600623}

[**[serial-set]{lang="EN-US"}**[ *set-number*]{lang="EN-US"}]{#struct_0_x1087_11486_325527140}

[**[undo serial-set]{lang="EN-US"}**[ *set-number*]{lang="EN-US"}]{#struct_0_x1087_11486_x598825038}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x475560836}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x604367596}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2019930392}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x371415310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x2022940593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2078356083}

[*[set-number]{lang="EN-US"}*]{#struct_0_x1087_11486_495903629}[：通道化出的串口的编号。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x435792779}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_1462684651}[接口在配置该命令后通道化出一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，接口名是]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *cellular-number*:*set-number*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_509486577}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x604302060}[将接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[通道化出一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x1600911388}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] serial-set 0]{lang="EN-US"}
:::

::: {#1742433432 .myid}
[]{#_Toc404785398}[]{#struct_0_x1087_11486_1479765616}[]{#_Toc369265317}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x1087_11486_1030591096}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x1087_11486_2022809574}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x195608623}

[**[bandwidth]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1087_11486_x1128991229}*[bandwidth-value]{lang="EN-US"}*

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x1087_11486_x1433932578}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1393898896}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x1087_11486_2104472276}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1775882570}

[[以太网通道接口视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1823537159}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1981891101}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1202602534}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x8963473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_588495874}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x1087_11486_1106231435}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbi]{lang="EN-US"}[t/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x755132220}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x1087_11486_84281553}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1532275756}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1095984118}[设置以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0]{lang="EN-US"}[:0]{lang="NO-BOK"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_2045000053}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] bandwidth 1000]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404785399}[]{#struct_0_x1087_11486_209270618}[]{#_Toc369265318}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x1087_11486_x1511115461}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x725455299}

[**[default]{lang="EN-US"}**]{#struct_0_x1087_11486_625910671}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_318983048}

[[以太网通道接口视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1076204160}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x564456593}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_946986222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_2053856148}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x297640982}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x1087_11486_33808185}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x1087_11486_x1481653613}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2136757674}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_x1690195281}[将]{style="font-family:宋体"}[以太网通道]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[Eth-channel2/4/0]{lang="EN-US"}[:0]{lang="NO-BOK"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x522179247}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2]{lang="DE"}[/4/0]{lang="EN-US"}[:0\] ]{lang="DE"}[default]{lang="EN-US"}
:::

::: {#437833442 .myid}
[]{#_Toc404785400}[]{#struct_0_x1087_11486_x1876092349}[]{#_Toc369265320}[]{#_Toc366948471}[]{#_Toc369252083}[]{#_Toc369265204}[]{#_Toc369265319}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1087_11486_1889166261}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1087_11486_1928880267}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_494482142}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1087_11486_x1082809852}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1087_11486_x1437890785}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x588128677}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_x1087_11486_1416470411}["，比如"]{style="font-family:宋体"}[Echannel2/4/0:0 Interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2043413664}

[[以太网通道接口视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x725706702}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1794447428}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1894200123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x173174315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_347133033}

[*[text]{lang="EN-US"}*]{#struct_0_x1087_11486_x1551553501}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x882856925}

[[可以根据需要修改接口的描述。]{style="font-family:宋体"}]{#struct_0_x1087_11486_447164070}

[[修改后的描述信息会在]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_x1087_11486_1989550282}[显示的接口信息中体现。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_562853591}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_125093230}[设置以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Echannel-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_847985332}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] description Echannel-interface]{lang="EN-US"}
:::

::: {#-1654107231 .myid}
[]{#_Toc404785401}[]{#struct_0_x1087_11486_x1703230415}[]{#_Toc369265321}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- display interface eth-channel**

------------------------------------------------------------------------

[**[display interface eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_840377239}[命令用来显示以太网通道接口的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_635393073}

[**[display interface]{lang="EN-US"}**[ \[ **eth-channel** \[ *channel-id* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x1087_11486_x1072822224}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1397829672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_310984247}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x509071165}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1541760278}

[[network-operator]{lang="EN-US"}]{#struct_0_x1087_11486_x426556563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1637423109}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1087_11486_2030340401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x297203721}

[*[channel-id]{lang="DE"}*]{#struct_0_x1087_11486_1674889136}[：以太网通道接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1087_11486_x751297906}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x1087_11486_x1144405591}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x1087_11486_437092712}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1645255228}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_x1657394509}[参数，将显示设备支持的所有接口的相关信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_1691311760}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[channel-id]{lang="EN-US"}*[参数，将显示所有已通道化的以太网通道接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1783372746}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_995510751}[显示以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface eth-channel 2/4/0:0]{lang="EN-US"}]{#struct_0_x1087_11486_x1694035266}

[Echannel2/4/0:0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Echannel2/4/0:0 Interface]{lang="EN-US"}

[Bandwidth: 100000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 000c-2963-b75d]{lang="EN-US"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 000c-2963-b75d]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: Never]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 buffers]{lang="EN-US"}

[Output:0 packets, 0 bytes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_445861318}[显示以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface eth-channel 2/4/0:0 brief]{lang="EN-US"}]{#struct_0_x1087_11486_x244206853}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Echannel2/4/0:0      UP   UP(s)    192.168.80.239]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_2003176653}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的以太网通道接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface eth-channel brief down]{lang="EN-US"}]{#struct_0_x1087_11486_2036400185}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Echannel2/4/0:0      ADM  Administratively]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display interface eth-channel]{lang="EN-US"}]{#struct_0_x1087_11486_x676591338}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x603441366}[[字段]{style="font-family:黑体"}]{#struct_0_x1087_11486_261000645}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1087_11486_1956122486}

[[Current state]{lang="EN-US"}]{#struct_0_x1087_11486_x772760869}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x2007760221}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_x1087_11486_1197894302}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1087_11486_x1530989053}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1087_11486_193874195}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x1087_11486_x1934273580}

[[接口的链路层协议状态，由链路层经过参数协商决定，取值为：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x368189639}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1087_11486_865398915}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1087_11486_x1127704526}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(spoofing)]{lang="EN-US"}]{#struct_0_x1087_11486_438379415}[：表示该接口的数据链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1087_11486_x1622592189}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1087_11486_35094888}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x1087_11486_1601178829}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1352283996}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x1087_11486_1554124662}

[[接口允许通过的最大传输单元]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1174758693}

[[Internet protocol processing: disabled]{lang="EN-US"}]{#struct_0_x1087_11486_1887954405}

[[接口当前不能处理]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1087_11486_1197959838}[报文]{style="font-family:宋体"}

[[Internet Address is 192.168.1.200/24 Primary]{lang="EN-US"}]{#struct_0_x1087_11486_x1530923517}

[[接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1087_11486_1178330104}[地址，此]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址由运营商自动分配]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_x1087_11486_x1934208044}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IP]{lang="EN-US"}]{#struct_0_x1087_11486_x368124103}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_x1087_11486_21361453}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IPv6]{lang="EN-US"}]{#struct_0_x1087_11486_x1127638990}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_x1087_11486_438444951}

[[输出队列的紧急队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1087_11486_x916639049}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Output queue - Protocol queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_x1087_11486_35160424}

[[输出队列的协议队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1087_11486_1601244365}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Output queue - FIFO queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_x1087_11486_1554190198}

[[输出队列的先进先出队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1087_11486_x1744231192}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数。该显示信息与用户的配置有关，当配置为]{style="font-family:宋体"}[CBQ]{lang="EN-US"}[、]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[等队列时则显示为]{style="font-family:宋体"}[CBQ/WFQ]{lang="EN-US"}[等队列的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x1087_11486_1003603233}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x1087_11486_x1717385956}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x1087_11486_x1174693157}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1087_11486_1198025374}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_x1087_11486_1766504067}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1087_11486_x1530857981}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的包数]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_x1087_11486_x1934142508}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1087_11486_1342134077}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的包数]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 buffers]{lang="EN-US"}]{#struct_0_x1087_11486_x368058567}

[[输入报文：报文数，字节数，缓存单元的个数]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1127573454}

[[Output:0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_x1087_11486_x87030884}

[[输出报文：报文数，字节数]{style="font-family:宋体"}]{#struct_0_x1087_11486_438510487}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x1087_11486_35225960}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x1087_11486_x2140849488}[）接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x1087_11486_1601309901}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x1087_11486_1554255734}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1087_11486_x2096767414}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x1087_11486_x1174627621}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x1087_11486_1198090910}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1087_11486_x241215316}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1530792445}

[[Iink]{lang="EN-US"}]{#struct_0_x1087_11486_x1934076972}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1087_11486_x367993031}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1087_11486_x582516871}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1087_11486_x1127507918}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x1087_11486_438576023}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x1087_11486_x935632175}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1087_11486_35291496}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1087_11486_1601375437}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1087_11486_x183932144}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1087_11486_1554321270}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x1087_11486_x1174562085}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x1087_11486_x1455453808}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1087_11486_1198156446}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1087_11486_x1530726909}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x1087_11486_972260218}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x1087_11486_x1934011436}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1087_11486_x367927495}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1976030483 .myid}
[]{#_Toc404785402}[]{#struct_0_x1087_11486_995512815}[]{#_Toc369265322}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- eth-channel**

------------------------------------------------------------------------

[**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_x175839273}[命令用来将]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口通道化出以太网通道接口。]{style="font-family:宋体"}

[**[undo eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_x1683691123}[命令用来将]{style="font-family:宋体"}[Cellular]{lang="EN-US"}[接口通道化出的以太网通道接口删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x262465783}

[**[eth-channel ]{lang="EN-US"}***[channel-number]{lang="EN-US"}*]{#struct_0_x1087_11486_1443915859}

[**[undo eth-channel ]{lang="EN-US"}***[channel-number]{lang="EN-US"}*]{#struct_0_x1087_11486_x1472338717}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_119510461}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_x697947397}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_193764139}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x1127442382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x2056462838}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2096070294}

[*[channel-number]{lang="DE"}*]{#struct_0_x1087_11486_188173349}[：]{style="font-family:宋体"}[通道化出的以太网通道接口]{style="font-family:宋体"}[编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x204340625}

[[Cellular]{lang="EN-US"}]{#struct_0_x1087_11486_220721411}[接口在配置该命令后通道化出一个以太网通道接口，接口名是]{style="font-family:宋体"}**[eth-channel]{lang="EN-US"}**[ *cellular-number*:*channel-number*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_885123476}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_722693230}[将接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[通道化出一个以太网通道接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x575011719}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] eth-channel 0]{lang="EN-US"}
:::

::: {#-983049293 .myid}
[]{#_Toc404785403}[]{#struct_0_x1087_11486_1104383232}[]{#_Toc369265323}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- interface eth-channel**

------------------------------------------------------------------------

[**[interface eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_946646901}[命令用来进入以太网通道接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1499283634}

[**[interface eth-channel]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1087_11486_914815771}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_499718841}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_438641559}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2022156787}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_223296976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_177420168}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1754382501}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1087_11486_2049326077}[：以太网通道接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1877900045}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_1994535908}[进入以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0]{lang="EN-US"}[:0]{lang="NO-BOK"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_251901403}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\]]{lang="EN-US"}
:::

::: {#1933878005 .myid}
[]{#_Toc404785404}[]{#struct_0_x1087_11486_474008332}[]{#_Toc369265324}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- ip address cellular-alloc**

------------------------------------------------------------------------

[**[ip address cellular-alloc]{lang="EN-US"}**]{#struct_0_x1087_11486_1788459577}[命令用来配置接口通过]{style="font-family:
宋体"}[Modem]{lang="EN-US"}[私有协议获取]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip address cellular-alloc]{lang="EN-US"}**]{#struct_0_x1087_11486_x1884469585}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x968956371}

[**[ip address cellular-alloc]{lang="EN-US"}**]{#struct_0_x1087_11486_1439817030}

[**[undo ip address cellular-alloc]{lang="EN-US"}**]{#struct_0_x1087_11486_x1517570493}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_35357032}

[[接口不通过]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1087_11486_194542010}[私有协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1836039342}

[[以太网通道接口视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x2002593803}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1340237855}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1374765444}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_460558971}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x2076039043}

[**[ip address cellular-alloc]{lang="EN-US"}**]{#struct_0_x1087_11486_x549214512}[与]{style="font-family:
宋体"}**[ip address dhcp-alloc]{lang="EN-US"}**[命令用于设置接口以何种方式从]{style="font-family:宋体"}[Modem]{lang="EN-US"}[获取接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址由运营商自动分配。]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}**[ip address cellular-alloc]{lang="EN-US"}**]{#struct_0_x1087_11486_x560120256}[命令是配置接口采用]{style="font-family:宋体"}[Modem]{lang="EN-US"}[私有协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，而]{style="font-family:宋体"}**[ip address dhcp-alloc]{lang="EN-US"}**[命令是配置接口采用标准]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_2029658299}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_2085080178}[为接口]{style="font-family:宋体"}[Cellular2/4/0]{lang="EN-US"}[创建以太网通道接口，并采用]{style="font-family:宋体"}[Modem]{lang="EN-US"}[私有协议获取运营商自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_972909304}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] eth-channel 0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] quit]{lang="EN-US"}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] ip address cellular-alloc]{lang="EN-US"}
:::

::: {#988247972 .myid}
[]{#_Toc404785405}[]{#struct_0_x1087_11486_328380220}[]{#_Toc369265325}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x1087_11486_1601440973}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1087_11486_246031204}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x516083750}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x1087_11486_636974052}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1087_11486_1637627202}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1660466951}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x1087_11486_x1804988698}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_522224193}

[[以太网通道接口视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1471309898}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_441092919}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_431562509}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1314803378}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x994335151}

[*[size]{lang="EN-US"}*]{#struct_0_x1087_11486_1780646810}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_995582054}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_1554386806}[配置以太网通道接口]{style="font-family:宋体"}[E]{lang="EN-US"}[th-channel]{lang="NO-BOK"}[2/4/0:0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x512595567}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] mtu 1430]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc404785406}[]{#struct_0_x1087_11486_1679962196}[]{#_Toc369265326}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1087_11486_506010908}[命令用来清除以太网通道接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_977080948}

[**[reset counters interface ]{lang="EN-US"}**[\[ **eth-channel** \[ *channel-id* \] \]]{lang="EN-US"}]{#struct_0_x1087_11486_x284411365}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x1504855669}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x185994314}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x830531652}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1392602590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x655790276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1449915052}

[**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_1191240931}[：清除]{style="font-family:宋体"}[以太网通道接口的统计信息。]{style="font-family:宋体"}

[*[channel-id]{lang="EN-US"}*]{#struct_0_x1087_11486_10377452}[：]{style="font-family:宋体"}[以太网通道接口]{style="font-family:宋体"}[的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1087_11486_518962774}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x1087_11486_861324553}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_x1174496549}[和]{lang="EN-US" style="font-family:宋体"}*[channel-id]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_x289322452}[而不指定]{lang="EN-US" style="font-family:宋体"}*[channel-id]{lang="EN-US"}*[，则清除所有以太网通道接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[eth-channel]{lang="EN-US"}**]{#struct_0_x1087_11486_2128173912}[和]{lang="EN-US" style="font-family:宋体"}*[channel-id]{lang="EN-US"}*[，则清除指定以太网通道接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x477199154}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_65529990}[清除以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface eth-channel 2/4/0:0]{lang="EN-US"}]{#struct_0_x1087_11486_1965900979}
:::

::: {#-716074350 .myid}
[]{#_Toc404785407}[]{#struct_0_x1087_11486_x365931595}[]{#_Toc327887960}[]{#_Toc374543587}

**3G/4G Modem管理 \-- 4G Modem管理专用配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1087_11486_718509645}[命令用来关闭以太网通道接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x1087_11486_728450853}[命令用来打开以太网通道接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1087_11486_850573428}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1087_11486_x1309143085}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1087_11486_68237452}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x604236524}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1087_11486_x464397837}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x768257757}

[[以太网通道接口视图]{style="font-family:宋体"}]{#struct_0_x1087_11486_x1823387429}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1087_11486_1418923331}

[[network-admin]{lang="EN-US"}]{#struct_0_x1087_11486_x65296852}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1087_11486_1973458887}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1087_11486_x641298509}

[[\# ]{lang="EN-US"}]{#struct_0_x1087_11486_775861635}[关闭以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1087_11486_x605219564}

[\[Sysname\] interface eth-channel 2/4/0:0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] shutdown]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
