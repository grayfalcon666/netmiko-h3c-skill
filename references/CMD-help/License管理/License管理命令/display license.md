::: {#1230264995 .myid}
[]{#_Toc404783053}[]{#struct_0_17928_89207_1927554003}[]{#_Toc307382713}

**License管理 \-- License管理命令 \-- display license**

------------------------------------------------------------------------

[**[display license]{lang="EN-US"}**]{#struct_0_17928_89207_x1284808495}[命令用来显示]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_342124102}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_x1889820743}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[display license ]{lang="EN-US"}**[\[ **activation-file** \| **activation-key** \| **license-key** \]]{lang="EN-US"}]{#struct_0_17928_89207_1954590676}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_1417159785}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display license ]{lang="EN-US"}**[\[ **activation-file** \| **activation-key** \| **license-key** \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_17928_89207_503461179}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_1002868793}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[display license ]{lang="EN-US"}**[\[ **activation-file** \| **activation-key** \| **license-key** \] \[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_17928_89207_2021967809}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_1766223934}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[display license ]{lang="EN-US"}**[\[ **activation-file** \| **activation-key** \| **license-key** \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_17928_89207_x825118243}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_1732355497}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17928_89207_x1431581139}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x593566286}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_367595331}

[[network-operator]{lang="EN-US"}]{#struct_0_17928_89207_1583128599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_638964337}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17928_89207_x838015961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_1192991398}

[**[activation-file]{lang="EN-US"}**]{#struct_0_17928_89207_1766420542}[：显示设备上已存在的激活文件相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[activation-key]{lang="EN-US"}**]{#struct_0_17928_89207_1871795011}**[：]{style="font-family:宋体"}**[显示设备上已存在的激活码相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[license-key]{lang="EN-US"}**]{#struct_0_17928_89207_811438712}[：显示设备上已存在的授权码相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1836422056}[：显示指定主控板上安装的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，显示设备上所有主控板的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1361117752}[：显示指定成员设备上安装的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_1358049778}[：显示指定成员设备上安装的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_69883219}[：显示指定成员设备的指定主控板上安装的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，显示所有主控板上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_1023662952}

[[如果不指定]{style="font-family:宋体"}**[activation-file]{lang="EN-US"}**]{#struct_0_17928_89207_1800936655}[、]{style="font-family:宋体"}**[activation-key]{lang="EN-US"}**[和]{style="font-family:宋体"}**[license-key]{lang="EN-US"}**[参数，则显示所有类型]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_x31847426}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1766355006}[显示设备上所有]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license]{lang="EN-US"}]{#struct_0_17928_89207_x480863499}

[Feature: opt]{lang="EN-US"}

[Feature Description: opt license.]{lang="EN-US"}

[Activation Key: QvkT-%gfS-Xz/4-jR@V-9g%3-79wv-NMFG-kmJ9]{lang="EN-US"}

[Registered at: 2013-02-23 11:36:09]{lang="EN-US"}

[License Type: Days restricted]{lang="EN-US"}

[Time Left (days): 249]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CS12500F_2014072009113494375.ak]{lang="EN-US"}

[Feature: LISP EVB evi mdc SPBM TRILL FCoE]{lang="EN-US"}

[Product Description: H3C S12500-F Advanced Data Center License ]{lang="EN-US"}

[Registered at: 2014-05-07 15:07:39 ]{lang="EN-US"}

[License Type: Permanent ]{lang="EN-US"}

[Current State: In use ]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CVSR10008vCPU_2014072009113494375.ak]{lang="EN-US"}

[Feature: STANDARD]{lang="EN-US"}

[Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)]{lang="EN-US"}

[Registered at: 2014-07-20 09:13:29]{lang="EN-US"}

[License Type: Permanent]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1766534950}[显示设备上所有]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license]{lang="EN-US"}]{#struct_0_17928_89207_x1148160273}

[Slot 0:]{lang="EN-US"}

[Feature: opt]{lang="EN-US"}

[Feature Description: opt license.]{lang="EN-US"}

[Activation Key: cyKT-x3vc-W@Ca-n4gn-YB83-rVY3-C8:7-e3pg]{lang="EN-US"}

[Registered at: 2013-02-21 15:26:33]{lang="EN-US"}

[License Type: Trial (days restricted)]{lang="EN-US"}

[Trial Time Left (days): 20]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CS12500F_2014072009113494375.ak]{lang="EN-US"}

[Feature: LISP EVB evi mdc SPBM TRILL FCoE]{lang="EN-US"}

[Product Description: H3C S12500-F Advanced Data Center License ]{lang="EN-US"}

[Registered at: 2014-05-07 15:07:39 ]{lang="EN-US"}

[License Type: Permanent ]{lang="EN-US"}

[Current State: In use ]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CVSR10008vCPU_2014072009113494375.ak]{lang="EN-US"}

[Feature: STANDARD]{lang="EN-US"}

[Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)]{lang="EN-US"}

[Registered at: 2014-07-20 09:13:29]{lang="EN-US"}

[License Type: Permanent]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1766551614}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display license]{lang="EN-US"}]{#struct_0_17928_89207_x1659320382}

[Slot 1:]{lang="EN-US"}

[Feature: opt]{lang="EN-US"}

[Feature Description: opt license.]{lang="EN-US"}

[Activation Key: dyKT-x3vc-W@Ca-n4gn-Yo83-rVY3-C8:7-e3pg]{lang="EN-US"}

[Registered at: 2013-02-21 15:26:33]{lang="EN-US"}

[License Type: Trial (days restricted)]{lang="EN-US"}

[Time Left (days): 20]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CS12500F_2014072009113494375.ak]{lang="EN-US"}

[Feature: LISP EVB evi mdc SPBM TRILL FCoE]{lang="EN-US"}

[Product Description: H3C S12500-F Advanced Data Center License ]{lang="EN-US"}

[Registered at: 2014-05-07 15:07:39 ]{lang="EN-US"}

[License Type: Permanent ]{lang="EN-US"}

[Current State: In use ]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CVSR10008vCPU_2014072009113494375.ak]{lang="EN-US"}

[Feature: STANDARD]{lang="EN-US"}

[Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)]{lang="EN-US"}

[Registered at: 2014-07-20 09:13:29]{lang="EN-US"}

[License Type: Permanent]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x684104076}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license]{lang="EN-US"}]{#struct_0_17928_89207_146609871}

[Chassis 2:]{lang="EN-US"}

[Feature: opt]{lang="EN-US"}

[Feature Description: opt license.]{lang="EN-US"}

[Activation Key: cyKT-x3vc-WsCa-n4gn-YB83-rsY3-C8:7-e3pg]{lang="EN-US"}

[Registered at: 2013-02-21 15:26:33]{lang="EN-US"}

[License Type: Trial (days restricted)]{lang="EN-US"}

[Trial Time Left (days): 20]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CS12500F_2014072009113494375.ak]{lang="EN-US"}

[Feature: LISP EVB evi mdc SPBM TRILL FCoE]{lang="EN-US"}

[Product Description: H3C S12500-F Advanced Data Center License ]{lang="EN-US"}

[Registered at: 2014-05-07 15:07:39 ]{lang="EN-US"}

[License Type: Permanent ]{lang="EN-US"}

[Current State: In use ]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CVSR10008vCPU_2014072009113494375.ak]{lang="EN-US"}

[Feature: STANDARD]{lang="EN-US"}

[Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)]{lang="EN-US"}

[Registered at: 2014-07-20 09:13:29]{lang="EN-US"}

[License Type: Permanent]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x2058375437}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有]{style="font-family:宋体"}[License]{lang="EN-US"}[的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license chassis 2 slot 1]{lang="EN-US"}]{#struct_0_17928_89207_1766486078}

[Chassis 2 Slot 1]{lang="EN-US"}[：]{style="font-family:宋体"}

[Feature: opt]{lang="EN-US"}

[Feature Description: opt license.]{lang="EN-US"}

[Activation Key: cydT-x3vc-W@Ca-n4gn-YB83-rVY3-C8:7-e3pg]{lang="EN-US"}

[Registered at: 2013-02-21 15:26:33]{lang="EN-US"}

[License Type: Trial (days restricted)]{lang="EN-US"}

[Trial Time Left (days): 20]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CS12500F_2014072009113494375.ak]{lang="EN-US"}

[Feature: LISP EVB evi mdc SPBM TRILL FCoE]{lang="EN-US"}

[Product Description: H3C S12500-F Advanced Data Center License ]{lang="EN-US"}

[Registered at: 2014-05-07 15:07:39 ]{lang="EN-US"}

[License Type: Permanent ]{lang="EN-US"}

[Current State: In use ]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/license/H3CVSR10008vCPU_2014072009113494375.ak]{lang="EN-US"}

[Feature: STANDARD]{lang="EN-US"}

[Product Description: H3C VSR1000  License(Comware V7,STANDARD Edition,8vCPU,Permanent)]{lang="EN-US"}

[Registered at: 2014-07-20 09:13:29]{lang="EN-US"}

[License Type: Permanent]{lang="EN-US"}

[Current State: In use]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[[display license]{lang="EN-US"}]{.FigureDescriptionChar}]{#struct_0_17928_89207_x2016866584}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_921289753}[[字段]{style="font-family:黑体"}]{#struct_0_17928_89207_1766027323}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17928_89207_x883129334}

[[Chassis *n*]{lang="EN-US"}]{#struct_0_17928_89207_x1091365847}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_1481735617}[号成员设备上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Slot *n*]{lang="EN-US"}]{#struct_0_17928_89207_x1417167335}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_x893064684}[号主控板上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_x1033177179}[号成员设备上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis *n* slot *m*]{lang="EN-US"}]{#struct_0_17928_89207_1765961787}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_806799175}[号成员设备]{style="font-family:宋体"}*[m]{lang="EN-US"}*[号主控板上的]{style="font-family:宋体"}[License]{lang="EN-US"}[信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Feature]{lang="EN-US"}]{#struct_0_17928_89207_x580132070}

[[特性名称]{style="font-family:宋体"}]{#struct_0_17928_89207_348674861}

[[Feature Description]{lang="EN-US"}]{#struct_0_17928_89207_x972043716}

[[特性的相关描述]{style="font-family:宋体"}]{#struct_0_17928_89207_848262709}

[[Product Description]{lang="EN-US"}]{#struct_0_17928_89207_1766158395}

[[激活文件产品描述信息]{style="font-family:宋体"}]{#struct_0_17928_89207_1124445899}

[[License Key]{lang="EN-US"}]{#struct_0_17928_89207_x1636117102}

[[显示安装的授权码信息]{style="font-family:宋体"}]{#struct_0_17928_89207_1519117031}

[[Activation Key]{lang="EN-US"}]{#struct_0_17928_89207_876181921}

[[显示安装的激活码信息]{style="font-family:宋体"}]{#struct_0_17928_89207_1503280670}

[[Registered at]{lang="EN-US"}]{#struct_0_17928_89207_1766092859}

[[在设备上的安装时间]{style="font-family:宋体"}]{#struct_0_17928_89207_x1583268602}

[[License Type]{lang="EN-US"}]{#struct_0_17928_89207_x1808237165}

[[License]{lang="EN-US"}]{#struct_0_17928_89207_651989298}[的类型]{style="font-family:宋体"}[，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_17928_89207_453967721}[：无法获取]{style="font-family:宋体"}[License]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permanent]{lang="EN-US"}]{#struct_0_17928_89207_1766289467}[：]{style="font-family:宋体"}[永久类型]{lang="EN-US" style="font-family:宋体"}[，表示该]{style="font-family:宋体"}[License]{lang="EN-US"}[永远有效，不会过期]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Days restricted]{lang="EN-US"}]{#struct_0_17928_89207_1927488466}[：]{style="font-family:宋体"}[相对时间类型]{lang="EN-US" style="font-family:宋体"}[，表示该]{style="font-family:宋体"}[License]{lang="EN-US"}[是正式发布的，且有效期是一个相对时间段，比如]{style="font-family:宋体"}[30]{lang="EN-US"}[天]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Date restricted]{lang="EN-US"}]{#struct_0_17928_89207_654235698}[：]{style="font-family:宋体"}[绝对时间类型]{lang="EN-US" style="font-family:宋体"}[，表示该]{style="font-family:宋体"}[License]{lang="EN-US"}[是正式发布的，且有效期是一个绝对时间段，比如]{style="font-family:宋体"}[2013]{lang="EN-US"}[年]{style="font-family:宋体"}[5]{lang="EN-US"}[月]{style="font-family:宋体"}[1]{lang="EN-US"}[日到]{style="font-family:宋体"}[2013]{lang="EN-US"}[年]{style="font-family:宋体"}[5]{lang="EN-US"}[月]{style="font-family:宋体"}[30]{lang="EN-US"}[日]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Trial (days restricted)]{lang="EN-US"}]{#struct_0_17928_89207_281635347}[：]{style="font-family:宋体"}[相对时间类型的试用]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[，表示该]{style="font-family:宋体"}[License]{lang="EN-US"}[是]{style="font-family:宋体"}[相对时间类型]{lang="EN-US" style="font-family:宋体"}[的、非正式发布的]{style="font-family:宋体"}[License]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Trial (date restricted)]{lang="EN-US"}]{#struct_0_17928_89207_x1073046995}[：]{style="font-family:宋体"}[绝对时间类型的试用]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[，表示该]{style="font-family:宋体"}[License]{lang="EN-US"}[是绝对]{style="font-family:宋体"}[时间类型]{lang="EN-US" style="font-family:宋体"}[的、非正式发布的]{style="font-family:宋体"}[License]{lang="EN-US"}

[[Time Left (days)]{lang="EN-US"}]{#struct_0_17928_89207_1766223931}

[[正式授权相对时间类型剩余时间]{style="font-family:宋体"}]{#struct_0_17928_89207_x825314851}

[[Trial Time Left (days)]{lang="EN-US"}]{#struct_0_17928_89207_1433677456}

[[临时授权相对时间类型剩余时间]{style="font-family:宋体"}]{#struct_0_17928_89207_x1882081533}

[[Validity Period ]{lang="EN-US"}]{#struct_0_17928_89207_1766420539}

[[正式授权绝对时间类型过期日期。]{style="font-family:宋体"}[No limit]{lang="EN-US"}]{#struct_0_17928_89207_1872515914}[表示不限制时间]{style="font-family:宋体"}

[[Trial Validity Period]{lang="EN-US"}]{#struct_0_17928_89207_1086886454}

[[临时授权绝对时间类型过期日期。]{style="font-family:宋体"}[No limit]{lang="EN-US"}]{#struct_0_17928_89207_427581347}[表示不限制时间]{style="font-family:宋体"}

[[Current State]{lang="EN-US"}]{#struct_0_17928_89207_1766355003}

[[License]{lang="EN-US"}]{#struct_0_17928_89207_x480666891}[当前状态]{style="font-family:宋体"}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In use]{lang="EN-US"}]{#struct_0_17928_89207_1360997993}[：]{style="font-family:宋体"}[当前]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[正在使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Usable]{lang="EN-US"}]{#struct_0_17928_89207_964920043}[：]{style="font-family:宋体"}[当前]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[正在]{style="font-family:宋体"}[等待使用]{lang="EN-US" style="font-family:宋体"}[（当设备同时安装了多个相对时间]{style="font-family:宋体"}[License]{lang="EN-US"}[，且多个]{style="font-family:宋体"}[License]{lang="EN-US"}[均支持某一特性时，则只有一个]{style="font-family:宋体"}[License]{lang="EN-US"}[中的该特性处于]{style="font-family:宋体"}[In use]{lang="EN-US"}[状态，其它]{style="font-family:宋体"}[License]{lang="EN-US"}[中的该特性会处于]{style="font-family:宋体"}[Usable]{lang="EN-US"}[状态。绝对时间]{style="font-family:宋体"}[License]{lang="EN-US"}[，此状态表示未到启用时间）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Expired]{lang="EN-US"}]{#struct_0_17928_89207_1766551611}[：]{style="font-family:宋体"}[当前]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[已过期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Uninstalled]{lang="EN-US"}]{#struct_0_17928_89207_x1659123774}[：]{style="font-family:宋体"}[当前]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[已卸载]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unusable]{lang="EN-US"}]{#struct_0_17928_89207_x1984266950}[：]{style="font-family:宋体"}[当前]{lang="EN-US" style="font-family:宋体"}[License]{lang="EN-US"}[无法使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_17928_89207_467313267}[：不合法的数据，无法使用]{lang="EN-US" style="font-family:宋体"}

[[Uninstall Key]{lang="EN-US"}]{#struct_0_17928_89207_1766486075}

[[卸载码]{style="font-family:宋体"}]{#struct_0_17928_89207_x2016538904}

[[Uninstall Date]{lang="EN-US"}]{#struct_0_17928_89207_1514335029}

[[卸载日期]{style="font-family:宋体"}]{#struct_0_17928_89207_393962262}

[ ]{lang="EN-US"}

::: {#-2092439042 .myid}
[]{#_Toc404783054}[]{#struct_0_17928_89207_x559745517}

**License管理 \-- License管理命令 \-- display license feature**

------------------------------------------------------------------------

[**[display license feature]{lang="EN-US"}**]{#struct_0_17928_89207_1766027324}[命令用来显示特性的]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x882801654}

[**[display license feature]{lang="EN-US"}**]{#struct_0_17928_89207_823835140}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1768310166}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17928_89207_x1479639555}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x911299182}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_1431306800}

[[network-operator]{lang="EN-US"}]{#struct_0_17928_89207_x1717425144}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x30273282}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17928_89207_1765961788}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_806602567}

[[License]{lang="EN-US"}]{#struct_0_17928_89207_1309979743}[摘要信息包括哪些特性需要安装]{style="font-family:宋体"}[License]{lang="EN-US"}[，以及已安装的]{style="font-family:宋体"}[License]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_1649622074}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x511616424}[显示]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息。（集中式设备）（分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license feature]{lang="EN-US"}]{#struct_0_17928_89207_1438759954}

[Total: 50 Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1201126148}[显示]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license feature]{lang="EN-US"}]{#struct_0_17928_89207_1766158396}

[Slot 0:]{lang="EN-US"}

[Total: 50   Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Total: 50   Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1124380363}[显示]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display license feature]{lang="EN-US"}]{#struct_0_17928_89207_1766092860}

[Slot 0:]{lang="EN-US"}

[Total: 50 Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Total: 50  Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1582678777}[显示]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license feature]{lang="EN-US"}]{#struct_0_17928_89207_x1554307217}

[Chassis 1:]{lang="EN-US"}

[Total: 50 Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 2:]{lang="EN-US"}

[Total: 50  Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x666194478}[显示]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license feature]{lang="EN-US"}]{#struct_0_17928_89207_1766289468}

[Chassis 1 Slot 0:]{lang="EN-US"}

[Total: 50   Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 2 Slot 1:]{lang="EN-US"}

[Total: 50   Usage: 7]{lang="EN-US"}

[Feature       Licensed     State]{lang="EN-US"}

[OPT           Y            Formal]{lang="EN-US"}

[OSPF          N            -]{lang="EN-US"}

[MPLS          Y            Trail]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display license feature]{lang="EN-US"}]{#struct_0_17928_89207_1927029714}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_916995121}[[字段]{style="font-family:黑体"}]{#struct_0_17928_89207_648760658}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17928_89207_1366966773}

[[Slot *n*]{lang="EN-US"}]{#struct_0_17928_89207_1741753930}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_1016057558}[号主控板上的]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Slot *n*]{lang="EN-US"}]{#struct_0_17928_89207_1766223932}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_x825511459}[号成员备上的]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis *n*]{lang="EN-US"}]{#struct_0_17928_89207_192771545}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_684840371}[号成员备上的]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Chassis *n* Slot *m*]{lang="EN-US"}]{#struct_0_17928_89207_x747327181}

[*[n]{lang="EN-US"}*]{#struct_0_17928_89207_1031784957}[号成员设备的]{style="font-family:宋体"}*[m]{lang="EN-US"}*[号主控板上的]{style="font-family:宋体"}[License]{lang="EN-US"}[摘要信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_17928_89207_1766420540}

[[设备上一共可安装]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_17928_89207_1871926083}[的总数目]{style="font-family:宋体"}

[[Usage]{lang="EN-US"}]{#struct_0_17928_89207_380170122}

[[设备上已经安装的]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_17928_89207_x446590940}[总数]{style="font-family:宋体"}

[[Feature]{lang="EN-US"}]{#struct_0_17928_89207_197726515}

[[需要]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_17928_89207_x958557411}[授权才能使用的业务特性的名称]{style="font-family:宋体"}

[[Licensed]{lang="EN-US"}]{#struct_0_17928_89207_1766355004}

[[是否已经授权]{style="font-family:宋体"}]{#struct_0_17928_89207_x480732427}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_17928_89207_x210871335}[表示未授权]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_17928_89207_x162832761}[表示已授权]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_17928_89207_1782582012}

[[License]{lang="EN-US"}]{#struct_0_17928_89207_493194647}[的当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Formal]{lang="EN-US"}]{#struct_0_17928_89207_1766551612}[表示当前已经为该特性安装了正式]{style="font-family:宋体"}[License]{lang="EN-US"}[，]{style="font-family:宋体"}[License]{lang="EN-US"}[处于有效状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Trail]{lang="EN-US"}]{#struct_0_17928_89207_x1659189310}[表示当前已经为该特性安装了临时]{style="font-family:宋体"}[License]{lang="EN-US"}[，]{style="font-family:宋体"}[License]{lang="EN-US"}[处于有效状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_17928_89207_x1203503140}[表示当前无有效]{style="font-family:宋体"}[License]{lang="EN-US"}[，用户如需使用该特性，请安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1452441157 .myid}
[]{#_Toc307382710}[]{#_Toc404783055}[]{#struct_0_17928_89207_x989156119}[]{#_Toc307382706}[]{#_Toc303758679}[]{#_Toc301442627}[]{#_Toc301425703}

**License管理 \-- License管理命令 \-- display license device-id**

------------------------------------------------------------------------

[**[display license device-id]{lang="EN-US"}**]{#struct_0_17928_89207_x996069986}[命令用来显示设备的]{style="font-family:
宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_2121993158}[命令用来显示指定主控板的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1766486076}[命令用来显示指定成员设备的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[display license device-id chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x2016473368}[命令用来显示指定成员设备的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1715943595}[命令用来显示指定成员设备上指定主控板的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_261072435}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_318425845}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**]{#struct_0_17928_89207_x1565931055}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_1296338668}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_470922230}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x2124601870}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**[ **chassis** *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x124737738}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x962856028}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[display license device-id]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1650598548}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_1718669858}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17928_89207_658847004}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1372366588}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_x310591814}

[[network-operator]{lang="EN-US"}]{#struct_0_17928_89207_420896228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x839375776}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17928_89207_x328361166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962921564}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x827025858}[：表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1111121250}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_212571827}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1015270429}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1466628763}

[[生成]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_17928_89207_x1713996104}[激活码或激活文件需要使用]{style="font-family:宋体"}[DID]{lang="EN-US"}[和]{style="font-family:宋体"}[SN]{lang="EN-US"}[，用来表示激活码]{style="font-family:宋体"}[/]{lang="EN-US"}[激活文件和设备的绑定关系。]{style="font-family:宋体"}

[[DID]{lang="EN-US"}]{#struct_0_17928_89207_17204297}[在执行压缩命令的时候会发生变化。因此，请在申请激活码或激活文件前，查询设备的]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[DID]{lang="EN-US"}]{#struct_0_17928_89207_x632228416}[有两种形式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[字符串形式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17928_89207_x88766775}[。]{style="font-family:宋体"}[在申请激活码或激活文件时，直接在申请页]{lang="EN-US" style="font-family:宋体"}[面]{style="font-family:宋体"}[输入该字符串即可。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[文件形式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17928_89207_192783104}[。]{style="font-family:宋体"}[在申请激活码或激活文件时，需]{lang="EN-US" style="font-family:宋体"}[通过]{style="font-family:宋体"}[申请]{lang="EN-US" style="font-family:宋体"}[页面]{style="font-family:宋体"}[上传该文件。]{lang="EN-US" style="font-family:宋体"}

[[不同型号的产品支持的]{style="font-family:宋体"}[DID]{lang="EN-US"}]{#struct_0_17928_89207_x515528841}[形式不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1267909230}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1019796983}[显示设备的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license device-id]{lang="EN-US"}]{#struct_0_17928_89207_x962724956}

[SN: XXXXXXXXXXXXXXXXXXXX]{lang="EN-US"}

[Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1994853424}[显示主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license device-id slot 1]{lang="EN-US"}]{#struct_0_17928_89207_x1054452201}

[SN: XXXXXXXXXXXXXXXXXXXX]{lang="EN-US"}

[Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_2082663740}[显示成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display license device-id slot 2]{lang="EN-US"}]{#struct_0_17928_89207_1491007132}

[SN: XXXXXXXXXXXXXXXXXXXX]{lang="EN-US"}

[Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x93598391}[显示成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license device-id chassis 2]{lang="EN-US"}]{#struct_0_17928_89207_x962790492}

[SN: XXXXXXXXXXXXXXXXXXXX]{lang="EN-US"}

[Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1584193168}[显示成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板的]{style="font-family:
宋体"}[SN]{lang="EN-US"}[和]{style="font-family:宋体"}[DID]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> display license device-id chassis 2 slot 1]{lang="EN-US"}]{#struct_0_17928_89207_x1830275922}

[SN: XXXXXXXXXXXXXXXXXXXX]{lang="EN-US"}

[Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[[display license device-id]{lang="EN-US"}]{.FigureDescriptionChar}]{#struct_0_17928_89207_x1299684523}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_910944541}[[字段]{style="font-family:黑体"}]{#struct_0_17928_89207_2097254322}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17928_89207_199171668}

[[SN]{lang="EN-US"}]{#struct_0_17928_89207_868893050}

[[序列号信息，用于生成激活码或激活文件]{style="font-family:宋体"}]{#struct_0_17928_89207_264344097}

[[Device ID]{lang="EN-US"}]{#struct_0_17928_89207_x962593884}

[[设备编号信息，用于生成激活码或激活文件]{style="font-family:宋体"}]{#struct_0_17928_89207_1542946558}

[ ]{lang="EN-US"}

::: {#-1246506900 .myid}
[]{#_Toc404783056}[]{#struct_0_17928_89207_1051100943}

**License管理 \-- License管理命令 \-- license activation-file install**

------------------------------------------------------------------------

[**[license activation-file install]{lang="EN-US"}**]{#struct_0_17928_89207_1404642550}[命令用来安装]{style="font-family:宋体"}[License]{lang="EN-US"}[的激活文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_1653815917}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_482532610}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-file install]{lang="EN-US"}**[ *file-name*]{lang="EN-US"}]{#struct_0_17928_89207_1779578248}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_1467322247}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license activation-file install ]{lang="EN-US"}***[file-name]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x962659420}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_764473671}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-file install ]{lang="EN-US"}***[file-name]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1766822425}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x338030304}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-file install ]{lang="EN-US"}***[file-name]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x824516177}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_1385371654}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_x1739985875}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1023461868}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_x203205880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x406243393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962462812}

[*[file-name]{lang="EN-US"}*]{#struct_0_17928_89207_x1209726343}[：激活文件的全路径]{style="font-family:宋体;color:black"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个]{style="font-family:宋体"}[字符的字符串，区分大小写。]{style="font-family:宋体"}[激活文件]{style="font-family:宋体;color:black"}[必须合法、有效，并且保存在设备存储介质上。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_2131178046}[：表示给主控板安装]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，主控板安装[激活文件]{style="color:black"}后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1395567885}[：表示给成员设备安装]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，成员设备安装[激活文件]{style="color:black"}后，即便加入别的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，也具有运行相应特性的授权。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_1189006509}[：表示给成员设备安装]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，成员设备安装[激活文件]{style="color:black"}后，即便加入别的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_2043437224}[：表示给指定成员设备上的指定主控板安装]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，主控板安装[激活文件]{style="color:black"}后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1206259500}

[[激活文件是用户购买的激活受控特性的凭证。激活文件安装到设备上后，对应的特性得到授权，可以正常使用。]{style="font-family:宋体"}]{#struct_0_17928_89207_x1187857315}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_1377649622}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x962528348}[安装激活文件]{style="font-family:宋体"}[20130810.ak]{lang="EN-US"}[。（集中式设备）（分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1530625105}

[\[Sysname\] license activation-file install flash:/license/20130810.ak]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1564724689}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[安装激活文件]{style="font-family:宋体"}[20130811.ak]{lang="EN-US"}[。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1359685086}

[\[Sysname\] license activation-file install flash:/license/20130811.ak slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1250352592}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[安装激活文件]{style="font-family:宋体"}[20130812.ak]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_451492855}

[\[Sysname\] license activation-file install flash:/license/20130812.ak slot 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x35417171}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[安装激活文件]{style="font-family:宋体"}[20130813.ak]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_368016748}

[\[Sysname\] license activation-file install flash:/license/20130813.ak chassis 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x962331740}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板安装激活文件]{style="font-family:
宋体"}[20130814.ak]{lang="EN-US"}[。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x442395262}

[\[Sysname\] license activation-file install flash:/license/20130814.ak chassis 2 slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x361385182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display license activation-file]{lang="EN-US"}**]{#struct_0_17928_89207_1737713650}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[license activation-file uninstall]{lang="EN-US"}**]{#struct_0_17928_89207_x1293907633}
:::

::: {#1641166447 .myid}
[]{#_Toc404783057}[]{#struct_0_17928_89207_x1221701859}

**License管理 \-- License管理命令 \-- license activation-file uninstall**

------------------------------------------------------------------------

[**[license activation-file uninstall]{lang="EN-US"}**]{#struct_0_17928_89207_916446459}[命令用来卸载]{style="font-family:宋体"}[License]{lang="EN-US"}[的激活文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_59851603}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_978282290}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-file uninstall ]{lang="EN-US"}***[file-name]{lang="EN-US"}*]{#struct_0_17928_89207_x962397276}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_1485394215}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license activation-file uninstall ]{lang="EN-US"}***[file-name]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1436830210}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_1370035218}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-file uninstall ]{lang="EN-US"}***[file-name]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1236757801}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_804139261}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-file uninstall ]{lang="EN-US"}***[file-name]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1889504119}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1278606290}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_x1032445334}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962856027}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_x1650270868}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_1560784505}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_1988109782}

[*[file-name]{lang="EN-US"}*]{#struct_0_17928_89207_x1329903858}[：激活文件的全路径]{style="font-family:宋体;color:black"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个]{style="font-family:宋体"}[字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1561259655}[：表示给主控板卸载]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，主控板卸载[激活文件]{style="color:black"}后，将不能使用该激活文件包含的特性。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1973823052}[：表示给成员设备卸载]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，成员设备卸载[激活文件]{style="color:black"}后，将不能使用该激活文件包含的特性。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_x823561392}[：表示给成员设备卸载]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，成员设备卸载[激活文件]{style="color:black"}后，将不能使用该激活文件包含的特性。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_716600797}[：表示给指定成员设备上的指定主控板卸载]{style="font-family:宋体"}[License]{lang="EN-US"}[激活文件]{style="font-family:宋体;color:black"}[，成员设备卸载[激活文件]{style="color:black"}后，将不能使用该激活文件包含的特性。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962921563}

[[当用户购买的正式激活文件还没有到期，并且在当前上设备不需要再使用时，可以卸载该激活文件，此时设备会产生一个卸载凭证------卸载文件。用户可以将该卸载凭证和其它设备绑定，获取一个新的激活文件，并在新设备上安装，从而将]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_17928_89207_x826567106}[从当前设备迁移到其它设备。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17928_89207_69766302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[激活文件被卸载后，对应的特性将无法获得到被卸载的激活文件的信息，特性无法运行。]{style="font-family:宋体"}]{#struct_0_17928_89207_703669343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果卸载的是临时激活文件，则不会产卸载文件；如果卸载的是正式激活文件，则会产卸载文件。]{style="font-family:宋体"}]{#struct_0_17928_89207_459829003}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_x98679832}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1185849399}[卸载正式激活文件]{style="font-family:宋体"}[flash:/license/20130810.ak]{lang="EN-US"}[。（集中式设备）（分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x768129484}

[\[Sysname\] license activation-file uninstall flash:/license/20130810.ak]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall file: flash:/license/20130810.uak]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_974909563}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[卸载正式激活文件]{style="font-family:宋体"}[flash:/license/20130811.ak]{lang="EN-US"}[。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x962724955}

[\[Sysname\] license activation-file uninstall flash:/license/20130811.ak slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall file: flash:/license/20130813.uak]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1994918960}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[卸载正式激活文件]{style="font-family:宋体"}[flash:/license/20130812.ak]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1961424674}

[\[Sysname\] license activation-file uninstall flash:/license/20130812.ak slot 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall file: flash:/license/20130812.uak]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1624581553}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[卸载正式激活文件]{style="font-family:宋体"}[flash:/license/20130813.ak]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_793290706}

[\[Sysname\] license activation-file uninstall flash:/license/20130813.ak chassis 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall file: flash:/license/20130813.uak]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1436065451}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板卸载正式激活文件]{style="font-family:
宋体"}[flash:/license/20130814.ak]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1003474455}

[\[Sysname\] license activation-file uninstall flash:/license/20130814.ak chassis 2 slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall file: flash:/license/20130814.uak]{lang="EN-US"}

[]{#_Toc307382708}[]{#_Toc303758680}[]{#_Toc301442628}[]{#_Toc301425704}[]{#_Toc185927308}[]{#_Toc123026768}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962790491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display license activation-file]{lang="EN-US"}**]{#struct_0_17928_89207_x1584389776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[license activation-file install]{lang="EN-US"}**]{#struct_0_17928_89207_350070733}
:::

::: {#-1648203087 .myid}
[]{#_Toc404783058}[]{#struct_0_17928_89207_509180252}

**License管理 \-- License管理命令 \-- license activation-key install**

------------------------------------------------------------------------

[**[license activation-key install]{lang="EN-US"}**]{#struct_0_17928_89207_x172532467}[命令用来安装]{style="font-family:
宋体"}[License]{lang="EN-US"}[的激活码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_365685656}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_191586174}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-key install]{lang="EN-US"}**[ *activation-key-string*]{lang="EN-US"}]{#struct_0_17928_89207_x1557950586}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_1615559820}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license activation-key install ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_2049455296}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x962593883}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-key install ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_1542749950}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x1729471262}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-key install ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x494503888}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1857697731}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_344506048}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_689847132}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_134399499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_1962897484}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962659419}

[*[activation-key-string]{lang="EN-US"}*]{#struct_0_17928_89207_763883848}[：激活码，格式为]{style="font-family:宋体;
color:black"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[，]{style="font-family:宋体"}[区分大小写，必须是合法、有效的激活码。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1044291948}[：表示给主控板安装激活码，主控板安装激活码后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1350125385}[：表示给成员设备安装激活码，成员设备安装激活码后，即便加入别的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，也具有运行相应特性的授权。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_1204066147}[：表示给成员设备安装激活码，成员设备安装激活码后，即便加入别的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x950923996}[：表示给指定成员设备上的指定主控板安装激活码，主控板安装激活码后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_1696306470}

[[激活码是用户购买的激活受控特性的凭证。激活码安装到设备上后，对应的特性得到授权，可以正常使用。]{style="font-family:宋体"}]{#struct_0_17928_89207_1320370694}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_1965896700}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x962462811}[安装激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（集中式设备）（分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x1209791879}

[\[Sysname\] license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1986765404}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[安装激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_322944536}

[\[Sysname\] license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x349909485}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[安装激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x1251398866}

[\[Sysname\] license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1660700626}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[安装激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x962528347}

[\[Sysname\] license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1530035281}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板安装激活码]{style="font-family:
宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x1163014645}

[\[Sysname\] license activation-key install XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2 slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_1733418082}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display license activation-key]{lang="EN-US"}**]{#struct_0_17928_89207_1239726454}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[license activation-key uninstall]{lang="EN-US"}**]{#struct_0_17928_89207_595995529}
:::

::: {#358916295 .myid}
[]{#_Toc404783059}[]{#struct_0_17928_89207_x2014852104}

**License管理 \-- License管理命令 \-- license activation-key unistall**

------------------------------------------------------------------------

[**[license activation-key uninstall]{lang="EN-US"}**]{#struct_0_17928_89207_x321929307}[命令用来卸载激活码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_727849776}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_x1191878242}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-key uninstall ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}*]{#struct_0_17928_89207_x962331739}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_x441936511}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license activation-key uninstall ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1380341266}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x283644882}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-key uninstall ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x589424736}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x986704040}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license activation-key uninstall ]{lang="EN-US"}***[activation-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1128404853}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_x432447253}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_1252558021}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962397275}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_1485197607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x527248092}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_629056902}

[*[activation-key-string]{lang="EN-US"}*]{#struct_0_17928_89207_77406446}[：要卸载的激活码，格式为]{style="font-family:宋体;color:black"}[xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx]{lang="EN-US"}[，]{style="font-family:宋体"}[区分大小写。只有设备上已安装且未过期的激活码才可以卸载。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x709795615}[：表示给主控板卸载激活码。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1390295178}[：表示给成员设备卸载激活码。成员设备卸载激活码后，将失去此激活码的授权信息，特性将无法获取到卸载的激活码的授权信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_578533057}[：表示给成员设备卸载激活码。成员设备卸载激活码后，成员设备将失去此激活码的授权信息，特性模块将无法再获取到此授权码的授权信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1106732681}[：表示给指定成员设备的指定主控板卸载激活码。成员设备卸载激活码后，成员设备将失去此激活码的授权信息，特性模块将无法再获取到此授权码的授权信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962856030}

[[当用户需要将特性授权信息迁移到其它设备上使用时，可以卸载特性对应的激活码，此时设备会产生一个卸载凭证------卸载码，本设备对应的特性将无法使用。用户可以将授权信息和其他设备绑定，从而将授权信息从一个设备迁移到另一台设备。]{style="font-family:宋体"}]{#struct_0_17928_89207_x1650074261}

[[如果卸载的是正式激活码，则会产生卸载码；如果卸载的是临时激活码，则不会产生卸载码。]{style="font-family:宋体"}]{#struct_0_17928_89207_x2063952624}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1252183066}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_121231068}[卸载正式激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_500237632}

[\[Sysname\] license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x702809023}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[卸载正式激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x2125329574}

[\[Sysname\] license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x962921566}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[卸载正式激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x826894786}

[\[Sysname\] license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1654599544}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[卸载正式激活码]{style="font-family:宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1014387878}

[\[Sysname\] license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1818134046}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板卸载正式激活码]{style="font-family:
宋体"}[XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x955841074}

[\[Sysname\] license activation-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX chassis 2 slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[Uninstall key: YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY-YYYY]{lang="EN-US"}

[]{#_Toc307382712}[]{#_Toc303758683}[]{#_Toc301442630}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x936608145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display license activation-key]{lang="EN-US"}**]{#struct_0_17928_89207_x34568271}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[license activation-key install]{lang="EN-US"}**]{#struct_0_17928_89207_x962724958}
:::

::: {#-393442366 .myid}
[]{#_Toc404783060}[]{#struct_0_17928_89207_x1994198064}

**License管理 \-- License管理命令 \-- license compress**

------------------------------------------------------------------------

[**[license compress]{lang="EN-US"}**]{#struct_0_17928_89207_782427351}[命令用来压缩]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1399359512}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_x468464663}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license compress]{lang="EN-US"}**]{#struct_0_17928_89207_906490806}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_x1216229913}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license compress slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1644350941}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_1378482846}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license compress chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x962790494}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x1584062096}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license compress chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1495247746}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_1597885838}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_1211807096}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x165906241}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_x706814649}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x1208368051}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_1809918268}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x962593886}[：表示对指定主控板的]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区进行压缩，主控板将删除无效的]{style="font-family:宋体"}[License]{lang="EN-US"}[数据，对]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区空间进行释放，用于安装新的激活信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1543077630}[：表示对指定成员设备的]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区进行压缩，成员设备将删除无效的]{style="font-family:宋体"}[License]{lang="EN-US"}[数据，对]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区空间进行释放，用于安装新的激活信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_x924123951}[：表示对指定成员设备的]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区进行压缩，将删除无效的]{style="font-family:宋体"}[License]{lang="EN-US"}[数据，对]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区空间进行释放，用于安装新的激活信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_403857059}[：表示对指定成员设备上指定主控板的]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区进行压缩，将删除无效的]{style="font-family:宋体"}[License]{lang="EN-US"}[数据，对]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区空间进行释放，用于安装新的激活信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_x857341902}

[[License]{lang="EN-US"}]{#struct_0_17928_89207_x1268220531}[存储区空间是有限的。执行该命令后，系统会自动判断各]{style="font-family:宋体"}[License]{lang="EN-US"}[的状态，将过期和卸载的]{style="font-family:宋体"}[License]{lang="EN-US"}[以及相关数据删除。从而释放空间，以便用户安装新的]{style="font-family:宋体"}[License]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，请在执行该命令前，保存各卸载]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_17928_89207_517646068}[的卸载码。因为执行该命令后，卸载码会被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_1644635263}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x979311172}[压缩]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x962659422}

[\[Sysname\] license compress]{lang="EN-US"}

[This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.]{lang="EN-US"}

[Are you sure you want to continue? \[Y/N\]: Y]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_764604743}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[压缩]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x724311225}

[\[Sysname\] license compress slot 1]{lang="EN-US"}

[This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.]{lang="EN-US"}

[Are you sure you want to continue? \[Y/N\]: Y]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1410168239}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[压缩]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_450669021}

[\[Sysname\] license compress slot 2]{lang="EN-US"}

[This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.]{lang="EN-US"}

[Are you sure you want to continue? \[Y/N\]: Y]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_122359723}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[压缩]{style="font-family:宋体"}[License]{lang="EN-US"}[存储区。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x962462814}

[\[Sysname\] license compress chassis 2]{lang="EN-US"}

[This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files.Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.]{lang="EN-US"}

[Are you sure you want to continue? \[Y/N\]: Y]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1209595271}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板压缩]{style="font-family:
宋体"}[License]{lang="EN-US"}[存储区。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x2132935302}

[\[Sysname\] license compress chassis 2 slot 1]{lang="EN-US"}

[This command will delete all data relevant to uninstalled and expired keys/licenses, including Uninstall keys, and create a new device ID for activation keys/files. Make sure you have saved the Uninstall keys so you can apply for a new activation key/file for the unexpired licenses that were covered by the uninstalled activation keys/files.]{lang="EN-US"}

[Are you sure you want to continue? \[Y/N\]: Y]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}
:::

::: {#-374377674 .myid}
[]{#_Toc404783061}[]{#struct_0_17928_89207_1805896738}

**License管理 \-- License管理命令 \-- license license-key install**

------------------------------------------------------------------------

[**[license license-key install]{lang="EN-US"}**]{#struct_0_17928_89207_1263864857}[命令用来安装授权码。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_308094259}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_x1886813028}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license license-key install]{lang="EN-US"}**[ *license-key-string*]{lang="EN-US"}]{#struct_0_17928_89207_x1944757792}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_x1088918302}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license license-key install ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x962528350}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_1530100818}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license license-key install ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1547889414}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_836210973}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license license-key install ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1446298312}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1273778629}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_2000384139}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x193009357}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_x1651176503}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x962331742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_x442526334}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x820557006}[：表示给主控板安装[授权]{style="color:black"}码，主控板安装[授权]{style="color:black"}码后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1231850654}[：表示给成员设备安装[授权]{style="color:black"}码，成员设备安装[授权]{style="color:black"}码后，即便加入别的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，也具有运行相应特性的授权。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_724177942}[：表示给成员设备安装[授权]{style="color:black"}码，成员设备安装[授权]{style="color:black"}码后，即便加入别的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1846297340}[：表示给指定成员设备上的指定主控板安装[授权]{style="color:black"}码，主控板安装[授权]{style="color:black"}码后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[ ]{lang="EN-US" style="color:black"}**]{#struct_0_17928_89207_x2121138923}[【使用指导】]{style="font-family:
黑体"}

[[授权码是用户购买的激活受控特性的凭证。授权码安装到设备上后，对应的特性得到授权，可以正常使用。授权码没有绑定关系，因此一个授权码可以安装到多台设备上。]{style="font-family:宋体"}]{#struct_0_17928_89207_464541602}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962397278}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1484476711}[安装授权码]{style="font-family:宋体"}[XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1850040355}

[\[Sysname\] license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1656216300}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[安装授权码]{style="font-family:宋体"}[XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x1621725622}

[\[Sysname\] license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1043217576}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[安装授权码]{style="font-family:宋体"}[XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x1064496816}

[\[Sysname\] license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX slot 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_367380007}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[安装授权码]{style="font-family:宋体"}[XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x962856029}

[\[Sysname\] license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x1650664084}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板安装授权码]{style="font-family:
宋体"}[XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1681586906}

[\[Sysname\] license license-key install XXXXXXXX-(XXXX-)XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2 slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x364355580}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display license license-key]{lang="EN-US"}**]{#struct_0_17928_89207_x1639225358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[license license-key uninstall]{lang="EN-US"}**]{#struct_0_17928_89207_1046754871}
:::

::: {#-1428135004 .myid}
[]{#_Toc404783062}[]{#struct_0_17928_89207_122646800}[]{#_Toc317081249}

**License管理 \-- License管理命令 \-- license license-key uninstall**

------------------------------------------------------------------------

[**[license license-key uninstall]{lang="EN-US"}**]{#struct_0_17928_89207_181590068}[命令用来卸载授权码。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x571276282}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17928_89207_x962921565}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license license-key uninstall ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}*]{#struct_0_17928_89207_x826960322}

[[分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot/]{lang="EN-US"}]{#struct_0_17928_89207_x1113718341}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[license license-key uninstall ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_1124815098}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x105589490}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license license-key uninstall ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_17928_89207_101845695}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17928_89207_x1408832046}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[：]{style="font-family:宋体"}

[**[license license-key uninstall ]{lang="EN-US"}***[license-key-string]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_600610538}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17928_89207_x559723245}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17928_89207_x1620667170}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962724957}

[[network-admin]{lang="EN-US"}]{#struct_0_17928_89207_x1994787888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17928_89207_x948401442}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17928_89207_x1753905683}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_660672099}[：表示给主控板卸载[授权]{style="color:black"}码，主控板卸载[授权]{style="color:black"}码后，将失去此[授权]{style="color:black"}码的授权信息，特性将无法获取到卸载的[授权]{style="color:black"}码的授权信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_640157014}[：表示给成员设备卸载[授权]{style="color:black"}码，成员设备卸载[授权]{style="color:black"}码后，将失去此[授权]{style="color:black"}码的授权信息，特性将无法获取到卸载的[授权]{style="color:black"}码的授权信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_17928_89207_1912735132}[：表示给成员设备卸载[授权]{style="color:black"}码，成员设备卸载[授权]{style="color:black"}码后，成员设备将失去此[授权]{style="color:black"}码的授权信息，特性模块将无法再获取到此[授权]{style="color:black"}码的授权信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17928_89207_x1041407336}[：表示给指定成员设备上的指定主控板安装激活码，主控板安装激活码后，即便插入别的设备，也具有运行相应特性的授权。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17928_89207_x962790493}

[[用户确定不再使用受控特性时，可以将授权码卸载，此时对应的特性将不会得到授权，不能使用。]{style="font-family:宋体"}]{#struct_0_17928_89207_x1584258704}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17928_89207_1707012364}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_808991417}[卸载授权码]{style="font-family:宋体"}[XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x114793325}

[\[Sysname\] license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x874547983}[给主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[卸载授权码]{style="font-family:宋体"}[XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（分布式设备－独立运行模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x1790359185}

[\[Sysname\] license license-key uninstall XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1646447125}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[卸载授权码]{style="font-family:宋体"}[XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_x962593885}

[\[Sysname\] license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX slot 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_1542881022}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[卸载授权码]{style="font-family:宋体"}[XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式不支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1367586666}

[\[Sysname\] license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17928_89207_x2128081211}[给成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板卸载授权码]{style="font-family:
宋体"}[XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式支持]{style="font-family:宋体"}[slot]{lang="EN-US"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17928_89207_1479564327}

[\[Sysname\] license license-key uninstall XXXXXXXX-XXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX chassis 2 slot 1]{lang="EN-US"}

[This operation might take some time. Do not perform any other operations until the operation is completed or a failure message is displayed. Please wait\...]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17928_89207_x2109536562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display license license-key]{lang="EN-US"}**]{#struct_0_17928_89207_x1625043671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[license license-key install]{lang="EN-US"}**]{#struct_0_17928_89207_x1714588183}

[ ]{lang="EN-US"}
:::
