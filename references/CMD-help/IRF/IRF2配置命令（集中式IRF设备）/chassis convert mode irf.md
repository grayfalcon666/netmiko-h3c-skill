::::: {#-1794466960 .myid}
[]{#_Toc404783267}[]{#struct_0_x2076_17954_x1121011294}[]{#_Toc375915893}[]{#_Toc262637982}[]{#_Toc216513760}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- chassis convert mode irf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1121076830}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1371679394}
:::

[ ]{lang="EN-US"}

[**[chassis convert mode irf]{lang="EN-US"}**]{#struct_0_x2076_17954_x1744214434}[命令用来将设备的运行模式切换到]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式。]{style="font-family:
宋体"}

[**[undo chassis convert mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1496071035}[命令用来将设备的运行模式切换到独立运行模式。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1362910537}

[**[chassis convert mode irf]{lang="EN-US"}**]{#struct_0_x2076_17954_90002084}

[**[undo chassis convert mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1356350993}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1153009522}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1384076624}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x559783766}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x457665316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1120618078}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_66415079}

[[设备出厂时处于独立运行模式。如果在本次运行过程中，没有修改设备的运行模式，则下次启动会延用本次启动的运行模式；如果在本次运行过程中，修改了设备的运行模式，则设备会自动重启，切换到新的模式。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1074074584}

[[请根据组网需要来配置设备的运行模式。当设备从独立运行模式切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x112188338}[模式后，即便只有一台设备也会形成]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。因为管理和维护]{style="font-family:宋体"}[IRF]{lang="EN-US"}[需要耗费一定的系统资源，所以，如果当前组网中设备不需要和别的设备组成]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，建议将运行模式配置为独立运行模式。]{style="font-family:宋体"}

[[设备从独立运行模式切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1534030064}[模式时，需要使用成员编号进行配置文件的自动转换。如果模式切换前没有配置成员编号，则系统会自动使用]{style="font-family:宋体"}[1]{lang="EN-US"}[作为成员编号。]{style="font-family:宋体"}

[[需要注意的是，确认模式切换操作后，设备会自动重启，完成运行模式的切换。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x418023695}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1126069215}

[]{#_Toc136937621}[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1065726638}[设备当前处于独立运行模式时，将设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1382307853}

[\[Sysname\] chassis convert mode irf]{lang="EN-US"}

[The device will switch to IRF mode and reboot. You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in IRF mode? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[Saving the converted configuration file to the main board succeeded.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1760095477}[设备当前处于]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式时，将设备切换到独立运行模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1120683614}

[\[Sysname\] undo chassis convert mode]{lang="EN-US"}

[The device will switch to stand-alone mode and reboot]{lang="EN-US"}[。]{style="font-family:宋体"}[ You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in stand-alone mode? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[Saving the converted configuration file to the main board succeeded.]{lang="EN-US"}
:::::

::: {#744564430 .myid}
[]{#_Toc404783268}[]{#struct_0_x2076_17954_832311637}[]{#_Toc380155625}[]{#_Toc380415183}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf**

------------------------------------------------------------------------

[**[display irf]{lang="EN-US"}**]{#struct_0_x2076_17954_277374039}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的相关信息，包括：成员编号、角色、优先级、]{style="font-family:宋体"}[CPU MAC]{lang="EN-US"}[地址以及描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1887512671}

[**[display irf]{lang="EN-US"}**]{#struct_0_x2076_17954_1788186004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x342925176}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x962397277}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1485328679}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x465186116}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_767417444}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1173819951}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x552423727}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1964206919}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1950056709}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf]{lang="EN-US"}]{#struct_0_x2076_17954_x962856032}

[MemberID  Role     Priority    CPU-Mac           Description]{lang="EN-US"}

[   1      Loading  1           00e0-fcbe-3102    F1Num001]{lang="EN-US"}

[ \*+2      Master   1           00e0-fcb1-ade2    F1Num002]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \* indicates the device is the master.]{lang="EN-US"}

[ + indicates the device through which the user logs in.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ The Bridge MAC of the IRF is: 00e0-fc00-1000]{lang="EN-US"}

[ Auto upgrade                   : yes]{lang="EN-US"}

[ Mac persistent                 : always]{lang="EN-US"}

[ Domain ID                      : 30]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display irf]{lang="EN-US"}]{#struct_0_x2076_17954_x1649943189}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1825181193}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1311780460}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2084851883}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_x2047182681}

[[成员设备的编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_881682929}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果编号前带"]{style="font-family:宋体"}]{#struct_0_x2076_17954_x962921568}[\*]{lang="EN-US"}["，表示该设备是主设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果编号前带"]{style="font-family:宋体"}]{#struct_0_x2076_17954_x826239426}[+]{lang="EN-US"}["，表示该设备是用户当前登录的、正在操作的设备]{style="font-family:宋体"}

[[Role]{lang="EN-US"}]{#struct_0_x2076_17954_27990567}

[[成员设备的角色，可能为：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x777113147}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x2076_17954_1244821138}[tandby]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[从]{style="font-family:宋体"}[设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x2076_17954_59094890}[：主设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loading]{lang="EN-US"}]{#struct_0_x2076_17954_x962724960}[：正在自动加载系统启动文件]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x2076_17954_x1994722351}

[[成员设备的优先级]{style="font-family:宋体"}]{#struct_0_x2076_17954_x93025668}

[[CPU-MAC]{lang="EN-US"}]{#struct_0_x2076_17954_x1555629901}

[[设备的]{style="font-family:宋体"}[CPU MAC]{lang="EN-US"}]{#struct_0_x2076_17954_325563534}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2076_17954_x1341794866}

[[设备的描述信息]{style="font-family:宋体"}]{#struct_0_x2076_17954_x962790496}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[没有描述信息时，]{lang="EN-US" style="font-family:宋体"}[Description]{lang="EN-US"}]{#struct_0_x2076_17954_x1583931024}[字段显示为]{lang="EN-US" style="font-family:宋体"}[\"\-\-\-\--\"]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果描述信息较多，无法在一行中完全显示，则以"]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1960902500}[...]{lang="EN-US"}["结尾，省略后面的信息。]{style="font-family:宋体"}[此时可以使用]{lang="EN-US" style="font-family:
  宋体"}**[display current-configuration]{lang="EN-US"}**[来查询完整的描述信息]{lang="EN-US" style="font-family:宋体"}

[[Bridge MAC of the IRF is]{lang="EN-US"}]{#struct_0_x2076_17954_1247713672}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_751423201}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[Auto upgrade]{lang="EN-US"}]{#struct_0_x2076_17954_x364969433}

[[是否使能自动加载系统启动文件功能]{style="font-family:宋体"}]{#struct_0_x2076_17954_x962593888}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[yes]{lang="EN-US"}]{#struct_0_x2076_17954_1542160126}[表示使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no]{lang="EN-US"}]{#struct_0_x2076_17954_1013924792}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[MAC persistent]{lang="EN-US"}]{#struct_0_x2076_17954_x2119575949}

[[是否使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_864093844}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[保留功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6 min]{lang="EN-US"}]{#struct_0_x2076_17954_x962659424}[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[保留时间为]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[always]{lang="EN-US"}]{#struct_0_x2076_17954_764211527}[表示]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[永久保留不改变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no]{lang="EN-US"}]{#struct_0_x2076_17954_x485897120}[表示立即改变]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}

[[Domain ID]{lang="EN-US"}]{#struct_0_x2076_17954_281584449}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x962462816}[的域编号]{style="font-family:宋体"}

[[当网络中存在多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1209464199}[时，用来唯一标识一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1624362486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display irf configuration]{lang="EN-US"}**]{#struct_0_x2076_17954_1220156720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display irf topology]{lang="EN-US"}**]{#struct_0_x2076_17954_x952350071}

::: {#1823087831 .myid}
[]{#_Toc404783269}[]{#struct_0_x2076_17954_742715951}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf configuration**

------------------------------------------------------------------------

[**[display irf configuration]{lang="EN-US"}**]{#struct_0_x2076_17954_463549359}[命令用来显示]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[中所有成员设备的配置信息，显示信息包括：当前成员编号、新配置的成员编号、]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的物理端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1790806739}

[**[display irf configuration]{lang="EN-US"}**]{#struct_0_x2076_17954_x752508372}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x962528352}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1530231890}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_15638714}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1559185246}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_1176968390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1429434607}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x442496160}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1998083506}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1071080279}[设备工作在独立运行模式时，显示所有成员设备上重启以后生效的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[\<Sysname\> display irf configuration]{lang="EN-US"}]{#struct_0_x2076_17954_139338308}

[ MemberID Priority IRF-Port1                   IRF-Port2]{lang="EN-US"}

[ 1        1        disable                     disable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1595409700}[设备工作在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式时，显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有成员设备的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf configuration]{lang="EN-US"}]{#struct_0_x2076_17954_x962331744}

[ MemberID  NewID    IRF-Port1                   IRF-Port2]{lang="EN-US"}

[ 2         2        Ten-GigabitEthernet2/0/25   Ten-GigabitEthernet2/0/26]{lang="EN-US"}

[ 5         5        Ten-GigabitEthernet5/0/25   Ten-GigabitEthernet5/0/26]{lang="EN-US"}

[                    Ten-GigabitEthernet5/0/27]{lang="EN-US"}

[                    Ten-GigabitEthernet5/0/28]{lang="EN-US"}

[ 10        10       Ten-GigabitEthernet10/0/25  Ten-GigabitEthernet10/0/26]{lang="EN-US"}

[                                                Ten-GigabitEthernet10/0/27]{lang="EN-US"}

[                                                Ten-GigabitEthernet10/0/28]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display irf configuration]{lang="EN-US"}]{#struct_0_x2076_17954_x442133118}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1820397685}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1523868623}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x9309650}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_x677069612}

[[设备当前的成员编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_1146349608}

[[Priority]{lang="EN-US"}]{#struct_0_x2076_17954_1207464382}

[[成员优先级。该字段只有设备处于独立运行模式时，才会显示]{style="font-family:宋体"}]{#struct_0_x2076_17954_499316186}

[[NewID]{lang="EN-US"}]{#struct_0_x2076_17954_x962397280}

[[配置的成员编号，设备重启后将会生效]{style="font-family:宋体"}]{#struct_0_x2076_17954_1485001000}

[[IRF-Port1]{lang="EN-US"}]{#struct_0_x2076_17954_1476783117}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1177921858}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[的配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示信息中包含多个物理端口则表示该]{style="font-family:宋体"}]{#struct_0_x2076_17954_93372234}[IRF]{lang="EN-US"}[端口由多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口聚合而成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_x2076_17954_x680494365}[disable]{lang="EN-US"}[则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口还没有和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定]{style="font-family:宋体"}

[[IRF-Port2]{lang="EN-US"}]{#struct_0_x2076_17954_x962856031}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1650139797}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[的配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示信息中包含多个物理端口则表示该]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1829286691}[IRF]{lang="EN-US"}[端口由多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口聚合而成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_x2076_17954_1202612519}[disable]{lang="EN-US"}[则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口还没有和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x11715983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display irf]{lang="EN-US"}**]{#struct_0_x2076_17954_1278804566}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display irf topology]{lang="EN-US"}**]{#struct_0_x2076_17954_775226993}

::: {#-173472542 .myid}
[]{#_Toc404783270}[]{#struct_0_x2076_17954_x962921567}[]{#_Toc328666672}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf link**

------------------------------------------------------------------------

[**[display irf link]{lang="EN-US"}**]{#struct_0_x2076_17954_x826829250}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x360834230}

[**[display irf link]{lang="EN-US"}**]{#struct_0_x2076_17954_187626549}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1561891601}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1221248862}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1368139524}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x182047707}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x684154409}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x962724959}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1994132528}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1587068336}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_156740520}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_73701966}

[Member 1]{lang="EN-US"}

[ IRF Port    Interface                           Status]{lang="EN-US"}

[ 1           disable                             \--]{lang="EN-US"}

[ 2           Ten-GigabitEthernet1/0/1(MDC1)      UP]{lang="EN-US"}

[             Ten-GigabitEthernet1/0/2(MDC2)      ADM]{lang="EN-US"}

[             Ten-GigabitEthernet1/0/3(MDC3)      DOWN]{lang="EN-US"}

[Member 2(IRF-Link-Down: MDC2, MDC3)]{lang="EN-US"}

[ IRF Port    Interface                           Status]{lang="EN-US"}

[ 1           Ten-GigabitEthernet2/0/1(MDC1)      UP]{lang="EN-US"}

[             Ten-GigabitEthernet2/0/2(MDC2)      DOWN]{lang="EN-US"}

[             Ten-GigabitEthernet2/0/3(MDC3)      ADM]{lang="EN-US"}

[ 2           disable                          \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x962790495}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[但不支持]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路检测功能的设备）。]{style="font-family:宋体"}

[[\<Sysname\> display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_x1584127632}

[Member 1]{lang="EN-US"}

[ IRF Port    Interface                          Status]{lang="EN-US"}

[ 1           disable                             \--]{lang="EN-US"}

[ 2           Ten-GigabitEthernet1/0/1(MDC1)      UP]{lang="EN-US"}

[             Ten-GigabitEthernet1/0/2(MDC2)      ADM]{lang="EN-US"}

[             Ten-GigabitEthernet1/0/3(MDC3)      DOWN]{lang="EN-US"}

[Member 2]{lang="EN-US"}

[ IRF Port    Interface                           Status]{lang="EN-US"}

[ 1           Ten-GigabitEthernet2/0/1(MDC1)      UP]{lang="EN-US"}

[             Ten-GigabitEthernet2/0/2(MDC2)      DOWN]{lang="EN-US"}

[             Ten-GigabitEthernet2/0/3(MDC3)      ADM]{lang="EN-US"}

[ 2           disable                          \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x642933280}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[也不支持]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路检测功能的设备）。]{style="font-family:宋体"}

[[\<Sysname\> display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_x962593887}

[Member 1]{lang="EN-US"}

[ IRF Port    Interface                           Status]{lang="EN-US"}

[ 1           disable                             \--]{lang="EN-US"}

[ 2           Ten-GigabitEthernet1//0/1           UP]{lang="EN-US"}

[             Ten-GigabitEthernet1/0/2            ADM]{lang="EN-US"}

[             Ten-GigabitEthernet1/0/3            DOWN]{lang="EN-US"}

[Member 2]{lang="EN-US"}

[ IRF Port    Interface                           Status]{lang="EN-US"}

[ 1           Ten-GigabitEthernet2/0/1            UP]{lang="EN-US"}

[             Ten-GigabitEthernet2/0/2            DOWN]{lang="EN-US"}

[             Ten-GigabitEthernet2/0/3            ADM]{lang="EN-US"}

[ 2           disable                             \--]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_1543012094}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1824384933}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1722983784}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_440385635}

[[Member *ID*]{lang="EN-US"}]{#struct_0_x2076_17954_x1329662286}

[[成员编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_36367023}

[[(IRF-Link-Down: MDC2, MDC3)]{lang="EN-US"}]{#struct_0_x2076_17954_x962659423}

[[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_764539207}[链路检测功能检测到该成员设备上]{style="font-family:宋体"}[MDC2]{lang="EN-US"}[和]{style="font-family:宋体"}[MDC3]{lang="EN-US"}[中的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路状态为]{style="font-family:宋体"}[Down]{lang="EN-US"}[，于是将该成员设备上这两个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的业务口状态也变为]{style="font-family:宋体"}[down]{lang="EN-US"}[，不能转发报文（只有支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[且支持]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路检测功能的设备支持该显示信息）]{style="font-family:宋体"}

[[IRF Port]{lang="EN-US"}]{#struct_0_x2076_17954_x1399832387}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1261644810}[端口号，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_36447733}[表示]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x2076_17954_x1762083009}[表示]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x2076_17954_x656001106}

[[对应的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x962462815}[物理端口的名称和该物理接口所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，用]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的编号表示（如果设备不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[则不显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示信息中包含多个物理端口则表示该]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1209529735}[IRF]{lang="EN-US"}[端口由多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口聚合而成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_x2076_17954_x871097488}[disable]{lang="EN-US"}[则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口还没有和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2076_17954_1208961178}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1482004321}[端口的物理接口的链路状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2076_17954_x962528351}[：链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2076_17954_1530166354}[：链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x2076_17954_787164104}[：]{lang="EN-US" style="font-family:宋体"}[用户在]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[下执行了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABSENT]{lang="EN-US"}]{#struct_0_x2076_17954_x1543395908}[：接口不]{lang="EN-US" style="font-family:宋体"}[存在，没有插入接口模块]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1887975628 .myid}
[]{#_Toc404783271}[]{#struct_0_x2076_17954_x1138346921}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf topology**

------------------------------------------------------------------------

[**[display irf topology]{lang="EN-US"}**]{#struct_0_x2076_17954_1943616576}[命令用来查看]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的拓扑信息，显示信息包含：成员编号、]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态以及]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的邻接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x537622549}

[**[display irf topology]{lang="EN-US"}**]{#struct_0_x2076_17954_x368391154}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x962331743}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x442591870}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_52397517}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1099731014}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1531780174}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x239300484}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_1754456634}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1267165421}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_42638002}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf topology]{lang="EN-US"}]{#struct_0_x2076_17954_x962397279}

[                           Topology Info]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[               IRF-Port1                  IRF-Port2]{lang="EN-US"}

[ MemberID   Link        neighbor      Link        neighbor     Belong To]{lang="EN-US"}

[ 1          DOWN        \-\--           UP          2            000f-cbb8-1a82]{lang="EN-US"}

[ 2          UP          1             UP          3            000f-cbb8-1a82]{lang="EN-US"}

[ 3          UP          2             DIS         \-\--          000f-cbb8-1a82]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display irf topology]{lang="EN-US"}]{#struct_0_x2076_17954_1484411175}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1818167341}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1265243258}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1410095441}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_1820920549}

[[成员编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_1237791421}

[[IRF-Port1]{lang="EN-US"}]{#struct_0_x2076_17954_603227913}

[[IRF-Port1]{lang="EN-US"}]{#struct_0_x2076_17954_696002448}[的信息，包括]{style="font-family:宋体"}[Link]{lang="EN-US"}[和]{style="font-family:宋体"}[neighbor]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[IRF-Port2]{lang="EN-US"}]{#struct_0_x2076_17954_461637819}

[[IRF-Port2]{lang="EN-US"}]{#struct_0_x2076_17954_x454454045}[的信息，包括]{style="font-family:宋体"}[Link]{lang="EN-US"}[和]{style="font-family:宋体"}[neighbor]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Link]{lang="EN-US"}]{#struct_0_x2076_17954_x1875238879}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1005172335}[端口的链路状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2076_17954_603162377}[：链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2076_17954_1260612358}[：链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[，可能因为物理上不连通，或者没有执行]{lang="EN-US" style="font-family:宋体"}**[irf-port-configuration active]{lang="EN-US"}**[命令激活]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DIS]{lang="EN-US"}]{#struct_0_x2076_17954_1581399227}[：表示该]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口还没有和任何]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定，请使用]{lang="EN-US" style="font-family:宋体"}**[port group interface]{lang="EN-US"}**[命令绑定]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIMEOUT]{lang="EN-US"}]{#struct_0_x2076_17954_735790933}[：]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[报文超时]{lang="EN-US" style="font-family:宋体"}

[[neighbor]{lang="EN-US"}]{#struct_0_x2076_17954_626867380}

[[与该]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_987009778}[端口直连的设备的成员编号（显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["表示该端口没有连接其它成员设备）]{style="font-family:宋体"}

[[Belong To]{lang="EN-US"}]{#struct_0_x2076_17954_603358985}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1900488457}[中当前主设备的]{style="font-family:宋体"}[CPU MAC]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x650721223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display irf]{lang="EN-US"}**]{#struct_0_x2076_17954_953515534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display irf configuration]{lang="EN-US"}**]{#struct_0_x2076_17954_x1411978240}

::::: {#-370031375 .myid}
[]{#_Toc404783272}[]{#struct_0_x2076_17954_x1423721901}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf-port load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_116078358}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x451956428}
:::

**[ ]{lang="EN-US"}**

[**[display irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_603293449}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1943348680}

[**[display irf-port load-sharing mode ]{lang="EN-US"}**[\[ **irf-port** \[ *member-id*/*port-number* \] \]]{lang="EN-US"}]{#struct_0_x2076_17954_959375561}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x443296701}

[[本命令的缺省情况与设备的型号有关，以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1512811254}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x512510681}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_142267013}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1496527771}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1450822816}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_603490057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x183044034}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_872486515}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1795616930}

[**[irf-port]{lang="EN-US"}**]{#struct_0_x2076_17954_1282752927}[：显示指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。不指定该参数时，显示全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[*[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_1769311709}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号。其中，]{style="font-family:宋体"}*[member-id]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口索引，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[。不指定该参数时，显示所有连通的]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式，如果当前没有连通的]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[链路，则显示"]{style="font-family:宋体"}[No IRF link exists.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603424521}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x141905842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1662077986}**[irf-port]{lang="EN-US"}**[参数时，则显示全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路负载分担模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定]{style="font-family:宋体"}]{#struct_0_x2076_17954_1569780504}**[irf-port]{lang="EN-US"}**[参数而未指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号，则显示所有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下分别采用的负载分担模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x2076_17954_1465537386}[IRF]{lang="EN-US"}[端口编号，则显示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下采用的负载分担模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x399080594}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_2025268536}[显示全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode]{lang="EN-US"}]{#struct_0_x2076_17954_603621129}

[irf-port Load-Sharing Mode:]{lang="EN-US"}

[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}

[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}

[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}

[MPLS traffic   : mpls-label1,             mpls-label2,]{lang="EN-US"}

[                    mpls-label3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1068006718}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode irf-port 1/1]{lang="EN-US"}]{#struct_0_x2076_17954_x1653688185}

[irf-port1/1 Load-Sharing Mode:]{lang="EN-US"}

[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}

[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}

[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}

[MPLS traffic   : mpls-label1,             mpls-label2,]{lang="EN-US"}

[                    mpls-label3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x932535993}[（配置按报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址实现]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式后）显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下采用的负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode irf 1/1]{lang="EN-US"}]{#struct_0_x2076_17954_1085578102}

[irf-port1/1 Load-Sharing Mode:]{lang="EN-US"}

[  destination-mac address]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display irf-port load-sharing mode]{lang="EN-US"}]{#struct_0_x2076_17954_618320375}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1818575341}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1837570795}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_603555593}

[[irf-port Load-Sharing Mode]{lang="EN-US"}]{#struct_0_x2076_17954_1453567943}

[[全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x530779091}[链路负载分担类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省情况下显示：二层报文、三层报文、四层报文、]{style="font-family:宋体"}]{#struct_0_x2076_17954_1909789433}[MPLS]{lang="EN-US"}[报文采用的负载分担类型（各设备支持的报文类型不同，请以设备的实际情况为准）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非缺省情况下显示：用户配置后采用的负载分担类型]{style="font-family:宋体"}]{#struct_0_x2076_17954_x31638273}

[[irf-port1/1 Load-Sharing Mode]{lang="EN-US"}]{#struct_0_x2076_17954_x783226615}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_603752201}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下采用的负载分担类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省情况下显示：全局采用的负载分担类型]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1076109306}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非缺省情况下显示：用户配置后采用的负载分担类型]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1241229365}

[[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}]{#struct_0_x2076_17954_x358344052}

[[二层报文缺省采用的负载分担类型：按照源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2076_17954_x1074061375}[地址和目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}]{#struct_0_x2076_17954_x492934612}

[[三层报文缺省采用的负载分担类型：按照源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2076_17954_603686665}[地址和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}]{#struct_0_x2076_17954_1247612773}

[[四层报文缺省采用的负载分担类型：按照源端口和目的端口进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}]{#struct_0_x2076_17954_x21079465}

[[MPLS traffic   : mpls-label1,             mpls-label2,                 mpls-label3]{lang="EN-US"}]{#struct_0_x2076_17954_1776067881}

[[MPLS]{lang="EN-US"}]{#struct_0_x2076_17954_x712147963}[报文缺省采用的负载分担类型：按照第]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[层的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[destination-mac address, source-mac address]{lang="EN-US"}]{#struct_0_x2076_17954_x376944974}

[[用户配置后采用的负载分担类型：按照源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2076_17954_603227914}[地址和目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担（此字段的显示内容与用户的配置相关）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1908609032 .myid}
[]{#_Toc404783273}[]{#struct_0_x2076_17954_696002453}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display mad**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1494677322}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1908890609}
:::

**[ ]{lang="EN-US"}**

[**[display mad]{lang="EN-US"}**]{#struct_0_x2076_17954_x1604524030}[命令用来显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1971903147}

[**[display mad ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_x2076_17954_1371646079}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x455348128}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_603162378}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1260612355}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1582251195}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1738609593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1334103648}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x638119662}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2072440246}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2076_17954_x447931476}[：显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[详细配置信息。如果不使用该参数，则显示简要配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2145745335}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_603358986}[显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[简要配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display mad]{lang="EN-US"}]{#struct_0_x2076_17954_1900488456}

[MAD ARP enabled.]{lang="EN-US"}

[MAD ND enabled.]{lang="EN-US"}

[MAD LACP disabled.]{lang="EN-US"}

[MAD BFD enabled.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x650786759}[显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[详细配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display mad verbose]{lang="EN-US"}]{#struct_0_x2076_17954_603293450}

[Current MAD status: Detect]{lang="EN-US"}

[Excluded ports(configurable):]{lang="EN-US"}

[Excluded ports(can not be configured):]{lang="EN-US"}

[MAD ARP enabled interface:]{lang="EN-US"}

[  Vlan-interface3]{lang="EN-US"}

[MAD ND enabled interface:]{lang="EN-US"}

[  Vlan-interface3]{lang="EN-US"}

[MAD LACP disabled.]{lang="EN-US"}

[MAD BFD enabled interface:]{lang="EN-US"}

[  Vlan-interface100]{lang="EN-US"}

[    mad ip address 223.255.255.202 255.255.255.0 member 2]{lang="EN-US"}

[    mad ip address 223.255.255.205 255.255.255.0 member 5]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display mad]{lang="EN-US"}]{#struct_0_x2076_17954_x12966447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1815102693}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1949880529}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1534525485}

[[MAD LACP enabled.]{lang="EN-US"}]{#struct_0_x2076_17954_x778568785}

[[是否使能]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1490902415}[检测功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x2076_17954_1099460177}[表示已经使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x2076_17954_603490058}[表示没有使能]{lang="EN-US" style="font-family:宋体"}

[[MAD ARP enabled.]{lang="EN-US"}]{#struct_0_x2076_17954_x183044043}

[[是否使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_872683118}[检测功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x2076_17954_100516611}[表示已经使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x2076_17954_x417854206}[表示没有使能]{lang="EN-US" style="font-family:宋体"}

[[MAD ND enabled.]{lang="EN-US"}]{#struct_0_x2076_17954_x284842611}

[[是否使能]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1612405815}[检测功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x2076_17954_603424522}[表示已经使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x2076_17954_x141905845}[表示没有使能]{lang="EN-US" style="font-family:宋体"}

[[Current MAD status]{lang="EN-US"}]{#struct_0_x2076_17954_x1661619234}

[[MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x2070832358}[当前的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detect]{lang="EN-US"}]{#struct_0_x2076_17954_x1734224408}[：检测状态，即]{style="font-family:宋体"}[IRF]{lang="EN-US"}[处于正常状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Recovery]{lang="EN-US"}]{#struct_0_x2076_17954_603621130}[：发生多]{style="font-family:宋体"}[Active]{lang="EN-US"}[冲突时，失败的一方进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态，该状态下设备会自动关闭所有非保留的业务接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detect to Recovery]{lang="EN-US"}]{#struct_0_x2076_17954_1270645433}[：从检测状态迁移到]{lang="EN-US" style="font-family:
  宋体"}[Recovery]{lang="EN-US"}[状态过程的中间状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Recovery to Detect]{lang="EN-US"}]{#struct_0_x2076_17954_x1407741293}[：从]{lang="EN-US" style="font-family:
  宋体"}[Recovery]{lang="EN-US"}[状态迁移到检测状态过程的中间状态]{lang="EN-US" style="font-family:宋体"}

[[Excluded ports(configurable)]{lang="EN-US"}]{#struct_0_x2076_17954_1314853075}

[[用户配置的保留接口]{style="font-family:宋体"}]{#struct_0_x2076_17954_1347331665}

[[Excluded ports(can not be configured)]{lang="EN-US"}]{#struct_0_x2076_17954_603555594}

[[系统默认保留的接口（不需要用户配置，自动保留）]{style="font-family:宋体"}]{#struct_0_x2076_17954_1453567942}

[[MAD ARP enabled interface:]{lang="EN-US"}]{#struct_0_x2076_17954_x530713555}

[[  Vlan-interface2]{lang="EN-US"}]{#struct_0_x2076_17954_x17868973}

[[使能了]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x810751669}[的接口]{style="font-family:宋体"}

[[MAD ND enabled  interface:]{lang="EN-US"}]{#struct_0_x2076_17954_603752202}

[[  Vlan-interface2]{lang="EN-US"}]{#struct_0_x2076_17954_x1076109307}

[[使能了]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1487653990}[的接口]{style="font-family:宋体"}

[[MAD LACP disabled]{lang="EN-US"}]{#struct_0_x2076_17954_x220921188}

[[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_603686666}[没有使能]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#277748717 .myid}
[]{#_Toc404783274}[]{#struct_0_x2076_17954_1657475396}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- easy-irf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x2116690546}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[只在]{lang="EN-US" style="font-family:KaiTi_GB2312"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_563879130}[模式下支持该命令]{lang="EN-US" style="font-family:KaiTi_GB2312"}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[easy-irf]{lang="EN-US"}**]{#struct_0_x2076_17954_658542626}[命令用于快速配置堆叠环境。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_84427320}

[**[easy-irf]{lang="EN-US"}**[ \[ **member** *member-id* \[ **renumber** *new-member-id* \] **domain** *domain-id* \[ **priority** *priority* \] \[ **irf-port1** *interface-list1* \] \[ **irf-port2** *interface-list2* \] \]]{lang="EN-US"}]{#struct_0_x2076_17954_1878674345}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1790641965}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_746841033}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1071407959}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1385681897}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1390288894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1813151396}

[**[member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x1304661030}[：表示设备当前的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[renumber]{lang="EN-US"}**[ *new-member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x882399762}[：表示新成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示不修改成员编号。]{style="font-family:宋体"}

[**[domain]{lang="EN-US"}**[ *domain-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x1465183150}[：表示设备所属的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。同一]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中成员设备域编号应配置为相同值。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x2076_17954_77408884}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。]{style="font-family:宋体"}

[**[irf-port1]{lang="EN-US"}**[ *interface-list1*]{lang="EN-US"}]{#struct_0_x2076_17954_x1939810253}[：表示和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。表示方式为]{style="font-family:宋体"}*[interface-list1]{lang="EN-US"}*[ = { *interface-type interface-number* }&\<1-n\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}[&\<1-n\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[n]{lang="EN-US"}[次。]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[irf-port2 ]{lang="EN-US"}***[interface-list2]{lang="EN-US"}*]{#struct_0_x2076_17954_x1577685991}[：表示和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。表示方式为]{style="font-family:宋体"}*[interface-list2]{lang="EN-US"}*[ = { *interface-type interface-number* }&\<1-n\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}[&\<1-n\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[n]{lang="EN-US"}[次。]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值与设备的型号有关，请以设备的实际情况为准。同一物理端口只能一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1395474754}

[[使用该功能，用户可以通过一条命令配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x447548885}[的基本参数，包括新成员编号、域编号、绑定物理端口，简化了配置步骤，达到快速配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的效果。]{style="font-family:宋体"}

[[在配置该功能时，有两种方式：]{style="font-family:宋体"}]{#struct_0_x2076_17954_2086188559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交互模式：用户输入]{lang="EN-US" style="font-family:宋体"}**[easy-irf]{lang="EN-US"}**]{#struct_0_x2076_17954_1247397299}[，回车，在交互过程中输入具体参数的值。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非交互模式，在输入命令行时直接指定所需参数的值。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x826082069}

[[两种方式的配置效果相同，如果用户对本功能不熟悉，建议使用交互模式。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1650518440}

[[配置时，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x644822719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果给成员设备指定新的成员编号，该成员设备会立即自动重启，以使新的成员编号生效。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_560212124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次使用该功能，修改域编号]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_17954_1207136702}[优先级]{lang="EN-US" style="font-family:宋体"}[/IRF]{lang="EN-US"}[物理端口时，域编号和优先级的新配置覆盖旧配置，]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的配置会新旧进行叠加。如需删除旧的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口配置，需要在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图下，执行]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令。一个]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口最多可绑定多少个]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在交互模式下，为]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1421275903}[IRF]{lang="EN-US"}[端口指定物理端口时，请注意：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[接口类型和接口编号间不能有空格。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_1970608159}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[不同物理接口之间用英文逗号分隔]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x2114744344}[，逗号前后不能有空格]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[有些接口板出厂时已将接口分组，]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x2134992505}[如果要将该组]{style="font-family:宋体"}[内的]{lang="EN-US" style="font-family:宋体"}[某]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定，需要将该组的所有接口都和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1467006663}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x2044326028}[通过非交互模式配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的新成员编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，域编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet2/0/21]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet2/0/22]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet2/0/23]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet2/0/24]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_552874869}

[\[Sysname\] easy-irf member 1 renumber 2 domain 10 priority 10 irf-port1 ten-gigabitethernet 2/0/21 ten-gigabitethernet 2/0/22 ten-gigabitethernet 2/0/23 ten-gigabitethernet 2/0/24]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[                  Configuration summary for member 2]{lang="EN-US"}

[IRF new member ID: 3]{lang="EN-US"}

[IRF domain ID    : 10]{lang="EN-US"}

[IRF priority     : 10]{lang="EN-US"}

[IRF-port 1       : Ten-GigabitEthernet2/0/21, Ten-GigabitEthernet2/0/22]{lang="EN-US"}

[                   Ten-GigabitEthernet2/0/23, Ten-GigabitEthernet2/0/24]{lang="EN-US"}

[IRF-port 2       : Disabled]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[Are you sure to use these settings to set up IRF? \[Y/N\] y]{lang="EN-US"}

[Starting to configure IRF\...]{lang="EN-US"}

[Configuration succeeded.]{lang="EN-US"}

[The device will reboot for the new member ID to take effect. Continue? \[Y/N\] y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x706885551}[通过交互模式配置成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[的新编号为]{style="font-family:宋体"}[5]{lang="EN-US"}[，域编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet3/0/21]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet3/0/22]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet3/0/23]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet3/0/24]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1521746653}

[\[Sysname\] easy-irf]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   ]{lang="EN-US"}

[Welcome to use easy IRF.                                                        ]{lang="EN-US"}

[To skip the current step, enter a dot sign (.).                                 ]{lang="EN-US"}

[To return to the previous step, enter a minus sign (-).                         ]{lang="EN-US"}

[To use the default value (enclosed in \[\]) for each parameter, press Enter withou]{lang="EN-US"}

[t entering a value.                                                             ]{lang="EN-US"}

[To quit the setup procedure, press CTRL+C.                                      ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   ]{lang="EN-US"}

[Select a member by its ID \<3\> \[3\]:3                                             ]{lang="EN-US"}

[Specify a new member ID \<1\~10\> \[1\]: 5                                           ]{lang="EN-US"}

[Specify a domain ID \<0\~4294967295\> \[0\]: 10                                      ]{lang="EN-US"}

[Specify a priority \<1\~32\> \[1\]: 10                                               ]{lang="EN-US"}

[Specify IRF-port 1 bindings (a physical interface or a comma-separated physical ]{lang="EN-US"}

[interface list)\[Disabled\]: ten-gigabitethernet3/0/21,ten-gigabitethernet3/0/22,ten-gigabitethernet3/0/23,ten-gigabitethernet3/0/24]{lang="EN-US"}

[Specify IRF-port 2 bindings (a physical interface or a comma-separated physical ]{lang="EN-US"}

[interface list)\[Disabled\]:                                                      ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   ]{lang="EN-US"}

[                  Configuration summary for member 3                            ]{lang="EN-US"}

[IRF new member ID: 5                                                            ]{lang="EN-US"}

[IRF domain ID    : 10                                                           ]{lang="EN-US"}

[IRF priority     : 10                                                           ]{lang="EN-US"}

[IRF-port 1       : Ten-GigabitEthernet3/0/21, Ten-GigabitEthernet3/0/22         ]{lang="EN-US"}

[                   Ten-GigabitEthernet3/0/23, Ten-GigabitEthernet3/0/24         ]{lang="EN-US"}

[IRF-port 2       : Disabled                                                     ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   ]{lang="EN-US"}

[Are you sure to use these settings to set up IRF? \[Y/N\] y                       ]{lang="EN-US"}

[Starting to configure IRF\...]{lang="EN-US"}

[Configuration succeeded.                                                        ]{lang="EN-US"}

[[The device will reboot for the new member ID to take effect. Continue? \[Y/N\] y]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2076_17954_880816010}
:::::

::::: {#-166125139 .myid}
[]{#_Toc404783275}[]{#struct_0_x2076_17954_36538721}[]{#_Toc375915901}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf auto-merge enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_1624189908}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1145090765}
:::

**[ ]{lang="EN-US"}**

[**[irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1296023208}[命令用来使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[**[undo irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_467794652}[命令用来关闭]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1461246558}

[**[irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x500691021}

[**[undo irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_37390689}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1786358260}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x2107649346}[合并自动重启功能处于使能状态。即两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并时，竞选失败方会自动重启。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1297920118}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1872472185}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1013599445}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_182793403}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1069588404}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_689537275}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_37456225}[合并时，两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[会遵照角色选举的规则进行竞选，竞选失败方]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的所有成员设备需要重启才能加入获胜方]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有使能]{style="font-family:宋体"}]{#struct_0_x2076_17954_1345735331}[IRF]{lang="EN-US"}[合并自动重启功能，则合并过程中的重启需要用户根据系统提示手工完成。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使能]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1706826329}[IRF]{lang="EN-US"}[合并自动重启功能，则合并过程中的重启由系统自动完成。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_395948872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x2076_17954_320651753}[IRF]{lang="EN-US"}[模式下，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[或]{style="font-family:宋体"}[DIS]{lang="EN-US"}[时，配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定，引起]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，从而触发]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并，此时，即便使能了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能，该功能也暂时不生效，系统会提示用户必须手工重启竞选失败方才能完成合并。此时，请使用]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令将当前配置（尤其是]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的配置）保存到下次启动配置文件后，再重启失败方。否则，失败方重启后，会因为没有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[配置信息而不能合并。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[其它情况下触发的]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1480754783}[IRF]{lang="EN-US"}[合并（比如]{style="font-family:宋体"}[IRF]{lang="EN-US"}[连接故障恢复后引起的合并；两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的启动配置文件中已经绑定了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，然后建立]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理连接引起]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，触发的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并等），如果合并时已使能了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能，则竞选失败方会自动重启加入获胜方，合并为一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要使]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1762437812}[IRF]{lang="EN-US"}[合并自动重启功能正常运行，请在即将合并的两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[上都使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1589087430}[模式下支持。配置]{lang="EN-US" style="font-family:宋体"}**[irf auto-merge enable]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_36866400}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1898027147}[使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_506626659}

[\[Sysname\] irf auto-merge enable]{lang="EN-US"}
:::::

::::: {#-1168398895 .myid}
[]{#_Toc404783276}[]{#struct_0_x2076_17954_1247612774}[]{#_Toc380415191}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf auto-update enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x20751785}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_2024230681}
:::

**[ ]{lang="EN-US"}**

[**[irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_83830565}[命令用来使能启动文件自动加载功能。]{style="font-family:宋体"}

[**[undo irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x2058530380}[命令用来关闭启动文件自动加载功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1696871032}

[**[irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_970056460}

[**[undo irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_603227911}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_696002450}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1494677325}[系统启动文件的自动加载功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1626561800}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_759867351}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1908858928}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1065863100}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1467199637}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1116218223}

[[使能启动文件自动加载功能后，当新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_603162375}[的设备和主设备的软件版本不同时，新加入的设备会自动同步主设备的软件版本，再重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，为了能够自动加载成功，请确保从设备存储介质上有足够的空闲空间用于存放新的启动文件。如果从设备存储介质上空闲空间不足，系统会自动删除从设备的当前启动文件来完成加载。如果删除从设备的当前启动文件后空间仍然不足，从设备将无法进行自动加载。此时，需要管理员重启从设备并进入从设备的]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}]{#struct_0_x2076_17954_1260612360}[菜单，删除一些不重要的文件后，再让从设备重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1581923514}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_764871086}[使能启动文件自动加载功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1391470984}

[\[Sysname\] irf auto-update enable]{lang="EN-US"}
:::::

::: {#841593833 .myid}
[]{#_Toc404783277}[]{#struct_0_x2076_17954_x125544399}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf domain**

------------------------------------------------------------------------

[**[irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_286994134}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}

[**[undo irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_2055518873}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_338476428}

[**[irf domain ]{lang="EN-US"}***[domain-id]{lang="EN-US"}*]{#struct_0_x2076_17954_603358983}

[**[undo irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_1900488459}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x651376583}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1735969123}[的域编号为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x250656615}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x300206296}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x117122579}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x2126190369}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1211372393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603293447}

[*[domain-id]{lang="EN-US"}*]{#struct_0_x2076_17954_1943348690}[：]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的域编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_959375562}

[[为了适应各种组网应用，同一个网络里可以部署多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x443296702}[。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[之间使用不同的域编号以示区别。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1512745718}[和]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测组网中，如果中间设备本身也是一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统，则必须配置该命令确保本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[和中间设备组成的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的域编号不同，否则可能造成检测异常，甚至导致业务中断。]{style="font-family:宋体"}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x71481123}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1834507912}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1575307608}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的域编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_603490055}

[\[Sysname\] irf domain 10]{lang="EN-US"}
:::

::: {#2122772173 .myid}
[]{#_Toc404783278}[]{#struct_0_x2076_17954_x183044032}[]{#_Toc300586570}[]{#_Toc300586628}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf link-delay**

------------------------------------------------------------------------

[**[irf link-delay]{lang="EN-US"}**]{#struct_0_x2076_17954_872617587}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[延迟上报时间。]{style="font-family:宋体"}

[**[undo irf link-delay]{lang="EN-US"}**]{#struct_0_x2076_17954_x1806766147}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_871497013}

[**[irf link-delay ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x2076_17954_x1318510633}

[**[undo irf link-delay]{lang="EN-US"}**]{#struct_0_x2076_17954_x1839892646}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1828586331}

[[不同型号的设备支持的缺省情况不同，以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1879853574}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603424519}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1715883946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1732684332}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_518799979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x2044250845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1207159735}

[*[interval]{lang="EN-US"}*]{#struct_0_x2076_17954_x795189655}[：表示延迟上报]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示不延迟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2073300009}

[[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_962734051}[环境中使用]{style="font-family:宋体"}[CFD]{lang="EN-US"}[、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能时，请保证]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[延迟上报时间小于]{style="font-family:宋体"}[CFD]{lang="EN-US"}[、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的超时时间，关于]{style="font-family:宋体"}[CFD]{lang="EN-US"}[、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能的介绍，请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[CFD]{lang="EN-US"}["]{style="font-family:宋体"} [、"]{style="font-family:宋体"}[BFD]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603621127}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1068006724}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[延迟上报时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x40746685}

[\[Sysname\] irf link-delay 300]{lang="EN-US"}
:::

::::: {#-1226208857 .myid}
[]{#_Toc404783279}[]{#struct_0_x2076_17954_630398309}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf isolate member**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_1699451496}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1340912222}
:::

**[ ]{lang="EN-US"}**

[**[irf isolate member]{lang="EN-US"}**]{#struct_0_x2076_17954_1539369617}[命令用来隔离某成员设备，即丢弃指定成员设备发送的所有报文。]{style="font-family:宋体"}

[**[undo irf isolate member]{lang="EN-US"}**]{#struct_0_x2076_17954_x575715975}[命令用来取消隔离。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_752836723}

[**[irf isolate member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_1271965022}

[**[undo irf isolate member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_145068463}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_710300256}

[[不隔离任何成员设备。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1851597104}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1530721329}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1387971133}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x663098651}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x759923836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x625240803}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1457061707}

[[当使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x257651649}[命令查看到物理]{style="font-family:宋体"}[IRF]{lang="EN-US"}[接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误报文较多，或者]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中出现网络风暴时，可多次使用]{style="font-family:宋体"}**[irf isolate member]{lang="EN-US"}**[命令，将所有空闲的成员编号都隔离，再进行修复。成员设备被隔离后，其它成员设备收到该成员设备发送的报文时，会直接丢弃。如果后续需要扩充]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，需先执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令取消隔离。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2047442484}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1459138917}[隔离成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_2010617556}

[\[Sysname\] irf isolate member 3]{lang="EN-US"}
:::::

::: {#-847521748 .myid}
[]{#_Toc404783280}[]{#struct_0_x2076_17954_x845227365}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf mac-address persistent**

------------------------------------------------------------------------

[**[irf mac-address persistent]{lang="EN-US"}**]{#struct_0_x2076_17954_x2015049313}[命令用来配置]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的保留时间。]{style="font-family:宋体"}

[**[undo irf mac-address persistent]{lang="EN-US"}**]{#struct_0_x2076_17954_x1137298694}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不保留，立即变化。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_660419456}

[**[irf mac-address persistent ]{lang="EN-US"}**[{ **timer** \| **always** }]{lang="EN-US"}]{#struct_0_x2076_17954_677566577}

[**[undo irf mac-address persistent]{lang="EN-US"}**]{#struct_0_x2076_17954_x1017940951}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603555591}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1453567945}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[会保留]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x530648019}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_345343917}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_538529105}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1387125574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_895204957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x56856870}

[**[timer]{lang="EN-US"}**]{#struct_0_x2076_17954_358972492}[：用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[保留时间为]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[**[always]{lang="EN-US"}**]{#struct_0_x2076_17954_603752199}[：用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[永久保留不改变。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1482128851}

[[如果配置了桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2076_17954_x2061158716}[保留时间为]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟，则当主设备离开]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[在]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟内不变化。如果主设备在]{style="font-family:
宋体"}[6]{lang="EN-US"}[分钟内重新又加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，则]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不会变化。如果]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟后主设备没有回到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，则会使用新选举的主设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[作为]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1058583933}[MAC]{lang="EN-US"}[地址永久保留，则不管主设备是否离开]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[始终保持不变。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1063067914}[MAC]{lang="EN-US"}[地址不保留，立即变化，当主设备离开]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，系统立即会使用新选举的主设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[做]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x100534984}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两个]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1917074505}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[相同，则它们不能合并为一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{lang="EN-US" style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x747716566}[和]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}[组网时，需要将]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[配置为]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址立即改变，即配置]{lang="EN-US" style="font-family:宋体"}**[undo irf mac-address persistent]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x1413685809}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中]{style="font-family:宋体"}[启用了]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议，则强烈建议用户配置]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留时间为永久保留]{lang="EN-US" style="font-family:宋体"}[，否则，可能]{style="font-family:宋体"}[会导致一系列问题。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1831228880}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_603686663}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[永久保留。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1247612779}

[\[Sysname\] irf mac-address persistent always]{lang="EN-US"}
:::

::::: {#-1860127276 .myid}
[]{#_Toc404783281}[]{#struct_0_x2076_17954_36473184}[]{#_Toc375915906}[]{#_Toc262637993}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x346564434}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_2079342274}
:::

[ ]{lang="EN-US"}

[**[irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_x661778154}[命令用来在独立运行模式下配置设备的成员编号。]{style="font-family:宋体"}

[**[undo irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_574127249}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_36538720}

[**[irf member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x332125228}

[**[undo irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_10459911}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_196782253}

[[设备处于独立运行状态时，成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_x1452459013}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2068439286}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1993086858}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x2076_17954_5456358}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_37390688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x169956876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1290853702}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_459143636}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1487983255}

[[成员编号有以下作用：]{style="font-family:宋体"}]{#struct_0_x2076_17954_20321261}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备从独立运行模式切换到]{style="font-family:宋体"}]{#struct_0_x2076_17954_1517231046}[IRF]{lang="EN-US"}[模式时，需要使用成员编号进行配置文件的自动转换。]{style="font-family:宋体"}[建议在独立运行模式下规划和修改设备的成员编号，以免成员编号冲突，设备切换到]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[，不能加入已有的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x880701233}[系统使用成员编号来唯一标识一台成员设备。如果在独立运行模式下，请使用]{style="font-family:宋体"}**[irf member]{lang="EN-US"}**[命令来配置，这种方式下配置的成员编号在设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后生效；如果在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下，请使用]{style="font-family:宋体"}**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ renumber ]{lang="EN-US"}***[new-member-id]{lang="EN-US"}*[命令来配置，这种方式下配置的成员编号需要重启设备才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_37456224}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x610579805}[在独立运行模式下配置设备的成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_734003898}

[\[sysname\] irf member 2.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x306720976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_709947780}
:::::

::: {#861064703 .myid}
[]{#_Toc404783282}[]{#struct_0_x2076_17954_x21472681}[]{#_Toc380415197}[]{#_Toc300586573}[]{#_Toc300586631}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member description**

------------------------------------------------------------------------

[**[irf member ]{lang="EN-US"}[description]{lang="EN-US"}**]{#struct_0_x2076_17954_785955831}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备的描述信息。]{style="font-family:宋体"}

[**[undo irf member ]{lang="EN-US"}[description]{lang="EN-US"}**]{#struct_0_x2076_17954_1271312321}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x242672030}

[**[irf member]{lang="EN-US"}***[ member-id ]{lang="EN-US"}***[description]{lang="EN-US"}***[ text]{lang="EN-US"}*]{#struct_0_x2076_17954_2140743767}

[**[undo irf member]{lang="EN-US"}**[ *member-id* **description**]{lang="EN-US"}]{#struct_0_x2076_17954_1428865697}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603227912}

[[成员设备没有描述信息。]{style="font-family:宋体"}]{#struct_0_x2076_17954_696002447}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_461637810}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x454454054}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1875304416}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1394420199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_160273820}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_36030560}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_1254030625}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}

[*[text]{lang="EN-US"}*]{#struct_0_x2076_17954_971121939}[：设备的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603162376}

[[当网络中存在多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1260612357}[或者同一]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中存在多台成员设备且物理位置比较分散（比如在不同楼层甚至不同建筑）时，为了确认成员设备的物理位置，在组建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时可以将物理位置设置为成员设备的描述信息，以便后期维护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1582120123}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x170494124}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[F1Num001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_47633645}

[\[Sysname\] irf member 1 description F1Num001]{lang="EN-US"}
:::

::: {#-1003199486 .myid}
[]{#_Toc404783283}[]{#struct_0_x2076_17954_x11201063}[]{#_Toc300586575}[]{#_Toc300586633}[]{#_Toc300586578}[]{#_Toc300586636}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member priority**

------------------------------------------------------------------------

[**[irf member priority]{lang="EN-US"}**]{#struct_0_x2076_17954_428855738}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备的优先级。]{style="font-family:宋体"}

[**[undo irf member priority]{lang="EN-US"}**]{#struct_0_x2076_17954_515883099}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_957551260}

[**[irf member]{lang="EN-US"}**[ *member-id* **priority** *priority*]{lang="EN-US"}]{#struct_0_x2076_17954_603358984}

[**[undo irf member]{lang="EN-US"}***[ member-id]{lang="EN-US"}*[ **priority**]{lang="EN-US"}]{#struct_0_x2076_17954_1900488458}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x651442119}

[[设备的成员优先级均为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_1351223635}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_641779583}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1126808469}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x209010457}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_730722425}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1669800815}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1294000620}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_603293448}**[：]{style="font-family:宋体"}**[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_x2076_17954_1943348681}**[：]{style="font-family:宋体"}**[表示优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_959441097}

[[优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x137923121}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2046601327}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_444612865}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[的设备的优先级为]{style="font-family:
宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_903533381}

[\[Sysname\] irf member 2 priority 32]{lang="EN-US"}[]{#_Toc171926465}[]{#_Toc171927129}[]{#_Toc171926467}[]{#_Toc171927131}[]{#_Toc171926489}[]{#_Toc171927153}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_36735327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_x245428669}
:::

::: {#430405483 .myid}
[]{#_Toc404783284}[]{#struct_0_x2076_17954_x1304975390}[]{#_Toc380415200}[]{#_Toc300586580}[]{#_Toc300586638}[]{#_Toc300586583}[]{#_Toc300586641}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member renumber**

------------------------------------------------------------------------

[**[irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_x1669872460}[命令用来配置设备的成员编号。]{style="font-family:宋体"}

[**[undo irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_603490056}[命令用来取消成员编号的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x183044033}

[**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}*[ **renumber** *new-member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_872683123}

[**[undo irf member]{lang="EN-US"}**[ *member-id* **renumber**]{lang="EN-US"}]{#struct_0_x2076_17954_x1855798516}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1318942589}

[[设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x2068178224}[模式后，使用的是独立运行模式下预配置的成员编号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_386344145}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x652099476}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1173430752}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1204931458}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_603424520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x141905843}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1662012450}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}

[*[new-member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x945787547}[：表示修改后的成员编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1820865946}

[[设备处于独立运行状态时，成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_36604255}[；切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后，使用的是独立运行模式下预配置的成员编号；如果模式切换前没有配置成员编号，则系统会自动使用]{style="font-family:宋体"}[1]{lang="EN-US"}[作为成员编号。]{style="font-family:宋体"}

[[当新加入的设备的编号和]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x855543646}[中已有成员设备的编号相同时，设备不能加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。此时，请使用该命令修改设备的成员编号后，重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置需要重启]{lang="EN-US" style="font-family:宋体"}*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x742746979}[标志的设备才能生效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2076_17954_127489487}[IRF]{lang="EN-US"}[中以设备编号标志设备，配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口和优先级也是根据设备编号来配置的，所以，修改设备成员编号可能导致设备配置发生变化或者丢失，请慎重处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1082328688}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_603621128}[将成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的成员编号修改为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> diplay irf]{lang="EN-US"}]{#struct_0_x2076_17954_x1068006719}

[\[Sysname\] irf member 1 renumber 3]{lang="EN-US"}

[Renumbering the member ID may result in configuration change or loss. Continue?\[Y/N\]Y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_525765336}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_x688867580}
:::

::::: {#-532457946 .myid}
[]{#_Toc404783285}[]{#struct_0_x2076_17954_x129326266}[]{#_Toc375915911}[]{#_Toc300586585}[]{#_Toc300586643}[]{#_Toc300586589}[]{#_Toc300586647}[]{#_Toc300586590}[]{#_Toc300586648}[]{#_Toc300586591}[]{#_Toc300586649}[]{#_Toc300586592}[]{#_Toc300586650}[]{#_Toc300586593}[]{#_Toc300586651}[]{#_Toc300586596}[]{#_Toc300586654}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf priority**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_36669791}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x587721847}
:::

[ ]{lang="EN-US"}

[**[irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_x1226065493}[命令用来在独立运行模式下配置设备的成员优先级。]{style="font-family:宋体"}

[**[undo irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_x1743515084}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1648966624}

[**[irf priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x2076_17954_x900626523}

[**[undo irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_36473183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1992087726}

[[设备的成员优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_x21115574}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1734135833}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1396410706}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1866930506}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_36538719}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1471242129}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1364208031}

[*[priority]{lang="EN-US"}*]{#struct_0_x2076_17954_x1565544653}[：表示优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2132851547}

[[成员优先级有两种配置方式：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x635923717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在独立运行模式下，使用]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1386326127}**[irf priority]{lang="EN-US"}**[命令来配置。如果在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[形成过程中，想让某台设备当选为主设备，请使用这种方式配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_37390687}[模式下，使用]{lang="EN-US" style="font-family:宋体"}**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*[命令来配置，这种方式下配置的成员优先级会影响]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[运行过程中的角色选举过程。比如当前主设备离开]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[时，优先级高的成员设备会当选为新的主设备；当发生]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[合并的时候，主设备成员优先级高的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[会竞选成功。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x125326860}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1889146823}[在独立运行模式下将本设备的成员优先级设置为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1214881657}

[\[sysname\] irf priority 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_354925802}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf member priority]{lang="EN-US"}**]{#struct_0_x2076_17954_37456223}
:::::

::: {#-1374140147 .myid}
[]{#_Toc404783286}[]{#struct_0_x2076_17954_1075195170}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port**

------------------------------------------------------------------------

[**[irf-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x1530162500}[命令用来创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口并进入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图，如果]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口已经创建，则直接进入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图。]{style="font-family:宋体"}

[**[undo irf-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x295857201}[用来删除]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x999777468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf-port ]{lang="EN-US"}***[member-id/port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x842622239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo irf-port]{lang="EN-US"}***[ member-id/port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x1131206569}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603555592}

[[设备上没有创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1453567944}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x530582483}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_355388337}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1587757744}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x862654167}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x261753868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1601011510}

[*[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x566126459}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号。其中，]{style="font-family:宋体"}*[member-id]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员]{style="font-family:宋体"}[编号；]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[索引，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时表示]{style="font-family:宋体"}[IRF-port1]{lang="EN-US"}[，为]{style="font-family:宋体"}[2]{lang="EN-US"}[时表示]{style="font-family:宋体"}[IRF-port2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603752200}

[[在组建]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1076109305}[前，必须进入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图，并绑定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口才能使能该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，从而进行]{style="font-family:宋体"}[IRF]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1644513892}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1923080878}[为成员编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[的设备创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将其与]{style="font-family:宋体"}[Ten-GigabitEthernet3/0/1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1002884123}

[\[Sysname\] interface ten-gigabitethernet 3/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet3/0/1\] shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet3/0/1\] quit]{lang="EN-US"}

[\[Sysname\] irf-port 3/1]{lang="EN-US"}

[\[Sysname-irf-port3/1\] port group interface ten-gigabitethernet 3/0/1]{lang="EN-US"}

[\[Sysname-irf-port3/1\] quit]{lang="EN-US"}

[\[Sysname\] interface ten-gigabitethernet 3/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet3/0/1\] undo shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1736725091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x122237511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_36866398}
:::

::::: {#1496518456 .myid}
[]{#_Toc404783287}[]{#struct_0_x2076_17954_603686664}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port global load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){#图片 4 width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_1247612772}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x21145001}
:::

**[ ]{lang="EN-US"}**

[**[irf-port global load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_1390138012}[命令用来配置全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[**[undo irf-port global load-sharing]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x2076_17954_x1701530697}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_617128881}

[**[irf-port global load-sharing mode]{lang="EN-US"}**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-port** \| **source-ip** \| **source-mac** \| **vlan-id** } \* \| **flexible** }]{lang="EN-US"}]{#struct_0_x2076_17954_x1420266903}

[**[undo irf-port global load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x65393313}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1114598115}

[[本命令的缺省情况则与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_603227909}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1642649702}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1432682690}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1215364630}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1108662199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1817262713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1817961424}

[**[destination-ip]{lang="EN-US"}**]{#struct_0_x2076_17954_x111387932}[：表示按报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-mac]{lang="EN-US"}**]{#struct_0_x2076_17954_176178906}[：表示按报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**]{#struct_0_x2076_17954_603162373}[：表示按报文的目的端口号进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ingress-port]{lang="EN-US"}**]{#struct_0_x2076_17954_1260612362}[：表示按报文的入端口号进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ip-protocol]{lang="EN-US"}**]{#struct_0_x2076_17954_1581792442}[：表示按报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议类型进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label1]{lang="EN-US"}**]{#struct_0_x2076_17954_348622294}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第一层（最外层）标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label2]{lang="EN-US"}**]{#struct_0_x2076_17954_x2129296012}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第二层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label3]{lang="EN-US"}**]{#struct_0_x2076_17954_x984486042}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第三层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x285004252}[：表示按报文的源端口号进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**]{#struct_0_x2076_17954_1598690925}[：表示按报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_x2076_17954_603358981}[：表示按报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan-id]{lang="EN-US"}**]{#struct_0_x2076_17954_1900488461}[：表示按报文所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[flexible]{lang="EN-US"}**]{#struct_0_x2076_17954_x650852292}[：表示系统自动根据报文的类型（]{style="font-family:宋体"}[L2]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[等）去匹配缺省负载分担模式，来灵活实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1773008417}

[[用户可以通过全局配置（系统视图下）和端口下（]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_423684541}[端口视图下）的配置方式设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在系统视图的配置对所有]{style="font-family:宋体"}]{#struct_0_x2076_17954_1130149802}[IRF]{lang="EN-US"}[链路生效；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2076_17954_650593593}[IRF]{lang="EN-US"}[端口视图下的配置只对当前]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路生效；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1464356369}[链路会优先采用端口下的配置。如果端口下没有配置，则采用全局配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_13569935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一视图下多次配置该命令，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_603293445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设备不支持的负载分担模式，系统将提示用户不支持。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1943348692}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_959244490}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1930709052}[配置全局按照报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1610922756}

[\[Sysname\] irf-port global load-sharing mode destination-mac]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_99676302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x580958987}
:::::

::::: {#-1283924903 .myid}
[]{#_Toc404783288}[]{#struct_0_x2076_17954_1969201278}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){#图片 5 width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x104544086}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_603490053}
:::

**[ ]{lang="EN-US"}**

[**[irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x183044038}[命令用来配置端口下]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[**[undo irf-port load-sharing]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x2076_17954_873272947}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1256152792}

[**[irf-port load-sharing mode]{lang="EN-US"}**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-port** \| **source-ip** \| **source-mac** \| **vlan-id** } \* \| **flexible** }]{lang="EN-US"}]{#struct_0_x2076_17954_x1128449099}

[**[undo irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1610901663}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1945015298}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x876391902}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x685470333}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_603424517}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1715883952}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x236618600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1656977491}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2073794104}

[**[destination-ip]{lang="EN-US"}**]{#struct_0_x2076_17954_930675411}[：表示按报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-mac]{lang="EN-US"}**]{#struct_0_x2076_17954_278008830}[：表示按报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x1309948392}[：设置按报文的目的端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ingress-port]{lang="EN-US"}**]{#struct_0_x2076_17954_1748664210}[：设置按报文的入端口实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ip-protocol]{lang="EN-US"}**]{#struct_0_x2076_17954_603621125}[：表示按报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议类型进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label1]{lang="EN-US"}**]{#struct_0_x2076_17954_x1068006722}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第一层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label2]{lang="EN-US"}**]{#struct_0_x2076_17954_1122052729}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第二层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label3]{lang="EN-US"}**]{#struct_0_x2076_17954_x1960174312}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第三层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**]{#struct_0_x2076_17954_2039009439}[：设置按报文的源端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**]{#struct_0_x2076_17954_x476301094}[：表示按报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_x2076_17954_1995214220}[：表示按报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan-id]{lang="EN-US"}**]{#struct_0_x2076_17954_x961991847}[：表示按报文所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[flexible]{lang="EN-US"}**]{#struct_0_x2076_17954_896439872}[：表示系统自动根据报文的类型（]{style="font-family:宋体"}[L2]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[等）去匹配缺省负载分担模式，来灵活实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603555589}

[[用户可以通过全局配置（系统视图下）和端口下（]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x502747199}[端口视图下）的配置方式设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在系统视图的配置对所有]{style="font-family:宋体"}]{#struct_0_x2076_17954_1170624348}[IRF]{lang="EN-US"}[链路生效；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2076_17954_x307493075}[IRF]{lang="EN-US"}[端口视图下的配置只对当前]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路生效；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x2061402932}[链路会优先采用端口下的配置。如果端口下没有配置，则采用全局配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_1716201838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置负载分担模式前，请先将]{style="font-family:宋体"}]{#struct_0_x2076_17954_961122506}[IRF]{lang="EN-US"}[端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定。否则，负载分担模式将配置失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一视图下多次配置该命令，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_712212673}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设备不支持的负载分担模式，系统将提示用户不支持。]{style="font-family:宋体"}]{#struct_0_x2076_17954_24916232}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603752197}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1482128849}[配置按报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址实现]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1704862820}

[\[Sysname\] irf-port 1/1]{lang="EN-US"}

[\[Sysname-irf-port1/1\] irf-port load-sharing mode destination-mac]{lang="EN-US"}
:::::

::::: {#399655551 .myid}
[]{#_Toc404783289}[]{#struct_0_x2076_17954_36473182}[]{#_Toc375915915}[]{#_Toc262638001}[]{#_Toc300586601}[]{#_Toc300586659}[]{#_Toc300586605}[]{#_Toc300586663}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port port-number**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_35772590}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x2003498093}
:::

[ ]{lang="EN-US"}

[**[irf-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x400517078}[命令用来在独立运行模式下创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口并进入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图（如果该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口已经创建，则直接进入该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **irf-port** *port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x1236775145}[用来删除指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_36538718}

[**[irf-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_867410031}

[**[undo irf-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1972063919}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x295523935}

[[设备上没有创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1029359668}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x245740172}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_37390686}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2081641996}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1474328983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_610439242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x640410482}

[*[port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_37456222}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x992916829}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x792850498}[在处于独立运行模式下创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x2130565455}

[\[Sysname\] irf-port 1]{lang="EN-US"}

[\[Sysname-irf-port1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_181009731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_1666808255}

[ ]{lang="EN-US"}
:::::

::: {#1293657116 .myid}
[]{#_Toc404783290}[]{#struct_0_x2076_17954_1197849946}[]{#_Toc300231742}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port-configuration active**

------------------------------------------------------------------------

[**[irf-port-configuration active]{lang="EN-US"}**]{#struct_0_x2076_17954_786841142}[命令用于来激活设备上所有]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[端口下的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1821004293}

[**[irf-port-configuration active]{lang="EN-US"}**]{#struct_0_x2076_17954_1499566417}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1320501569}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_603686661}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1247612777}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x20817321}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1891662917}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x449679564}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_774187781}[物理线缆连接好，并将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口添加到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口后，必须通过该命令手工激活]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的配置才能形成]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[系统启动，通过配置文件将]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1023730769}[物理端口加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，或者]{style="font-family:宋体"}[IRF]{lang="EN-US"}[形成后再加入新的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下的配置会自动激活不再需要使用该命令来激活。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1739115643}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_855479459}[激活]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_603227910}[端口]{lang="EN-US" style="font-family:宋体"}[1/2]{lang="EN-US"}[，将它和]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口]{lang="EN-US" style="font-family:宋体"}[Ten-GigabitEthernet1/0/]{lang="EN-US"}[1]{lang="EN-US"}[绑定。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_696002449}

[\[Sysname\] interface ten-gigabitEthernet 1/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/0/1\] shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] irf-port 1/2]{lang="EN-US"}

[\[Sysname-irf-port1/2\] port group interface Ten-GigabitEthernet 1/0/1]{lang="EN-US"}

[ Info : You are recommended to save the configuration now; otherwise, it will be lost after system reboot.]{lang="EN-US"}

[\[Sysname-irf-port1/2\] quit]{lang="EN-US"}

[\[Sysname\] interface ten-gigabitEthernet 1/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/0/1\] undo shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将当前配置保存到下次启动配置文件，以便]{style="font-family:宋体"}]{#struct_0_x2076_17954_461637820}[IRF]{lang="EN-US"}[端口的配置在设备重启后能继续生效。]{style="font-family:宋体"}

[[\[Sysname\] save]{lang="EN-US"}]{#struct_0_x2076_17954_603162374}

[The current configuration will be written to the device. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/startup.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[flash:/aa.cfg exists, overwrite? \[Y/N\]:y]{lang="EN-US"}

[ Validating file. Please wait\...\...\...\...\...\...\...\...\....]{lang="EN-US"}

[ Saved the current configuration to mainboard device successfully.]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[ Save next configuration file successfully.]{lang="EN-US"}

[ Configuration is saved to device successfully.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[激活]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1260612359}[端口的配置。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] irf-port-configuration active]{lang="EN-US"}]{#struct_0_x2076_17954_1581464763}
:::

::::: {#1992752252 .myid}
[]{#_Toc404783291}[]{#struct_0_x2076_17954_1915308375}[]{#_Toc300586608}[]{#_Toc300586666}[]{#_Toc342892632}[]{#_Toc342892688}[]{#_Toc342892633}[]{#_Toc342892689}[]{#_Toc342892634}[]{#_Toc342892690}[]{#_Toc342892635}[]{#_Toc342892691}[]{#_Toc342892636}[]{#_Toc342892692}[]{#_Toc342892637}[]{#_Toc342892693}[]{#_Toc342892638}[]{#_Toc342892694}[]{#_Toc342892639}[]{#_Toc342892695}[]{#_Toc342892640}[]{#_Toc342892696}[]{#_Toc342892641}[]{#_Toc342892697}[]{#_Toc342892642}[]{#_Toc342892698}[]{#_Toc342892643}[]{#_Toc342892699}[]{#_Toc342892644}[]{#_Toc342892700}[]{#_Toc342892645}[]{#_Toc342892701}[]{#_Toc342892646}[]{#_Toc342892702}[]{#_Toc342892647}[]{#_Toc342892703}[]{#_Toc342892648}[]{#_Toc342892704}[]{#_Toc342892649}[]{#_Toc342892705}[]{#_Toc342892650}[]{#_Toc342892706}[]{#_Toc342892651}[]{#_Toc342892707}[]{#_Toc342892652}[]{#_Toc342892708}[]{#_Toc342892653}[]{#_Toc342892709}[]{#_Toc342892654}[]{#_Toc342892710}[]{#_Toc342892655}[]{#_Toc342892711}[]{#_Toc342892656}[]{#_Toc342892712}[]{#_Toc342892657}[]{#_Toc342892713}[]{#_Toc342892658}[]{#_Toc342892714}[]{#_Toc342892659}[]{#_Toc342892715}[]{#_Toc342892660}[]{#_Toc342892716}[]{#_Toc300586610}[]{#_Toc300586668}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad arp enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_763996703}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1648451927}
:::

**[ ]{lang="EN-US"}**

[**[mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_431011524}[命令用来使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x384938610}[用来关闭]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2087739272}

[**[mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_603358982}

[**[undo mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1900488460}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x650917828}

[[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_607437490}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x726931125}

[[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_99645017}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x95569521}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1440197571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x600376141}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603293446}

[[为了防止]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1943348691}[级联组网时，本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测报文转发到邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中影响邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，执行]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[命令时，系统会要求用户输入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。]{style="font-family:宋体"}

[[VLAN 1]{lang="EN-US"}]{#struct_0_x2076_17954_959441098}[不能用于]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，因此，不能在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x137923128}[、]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2047191151}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_57377253}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[上启用]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_603490054}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad arp enable]{lang="EN-US"}

[You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[\[Current domain is: 0\]: 1]{lang="EN-US"}

[The assigned  domain ID is: 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x183044031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_872814195}
:::::

::::: {#-200835097 .myid}
[]{#_Toc404783292}[]{#struct_0_x2076_17954_x2069183961}[]{#_Toc300586612}[]{#_Toc300586670}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_56412175}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x309334896}
:::

**[ ]{lang="EN-US"}**

[**[mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_836617078}[命令用来使能]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x1751880324}[用来关闭]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x369085149}

[**[mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_603424518}

[**[undo mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x1715883947}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_166600391}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x614420067}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_869716642}

[[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_584866700}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_17427601}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1074148376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_2038140947}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_603621126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN 1]{lang="EN-US"}]{#struct_0_x2076_17954_x1068006725}[不能用于]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，因此，不能在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1606830626}[、]{lang="EN-US" style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{lang="EN-US" style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能]{style="font-family:宋体"}]{#struct_0_x2076_17954_654134792}[BFD]{lang="EN-US"}[检测功能的三层接口只能专用于]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测，不允许运行其它业务。如果用户配置了其它业务，可能会影响该业务以及]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测功能的运行。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1148395864}[检测功能与]{style="font-family:宋体"}[VPN]{lang="EN-US"}[功能互斥，请不要将使能了]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能的三层接口与]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例进行绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x941542421}[检测功能与生成树功能互斥，在使能了]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能的三层接口对应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的端口上，请不要使能生成树协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1974392841}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1237868415}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[上启用]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_603555590}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad bfd enable]{lang="EN-US"}
:::::

::::: {#-1753802282 .myid}
[]{#_Toc404783293}[]{#struct_0_x2076_17954_1453567946}[]{#_Toc300586614}[]{#_Toc300586672}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image004.png){#图片 9 width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x530451411}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_784559608}
:::

**[ ]{lang="EN-US"}**

[**[mad enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1534094867}[命令用来使能]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[**[undo mad enable]{lang="EN-US"}**]{#struct_0_x2076_17954_934757044}[用来关闭]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x640917161}

[**[mad enable]{lang="EN-US"}**]{#struct_0_x2076_17954_38849193}

[**[undo mad enable]{lang="EN-US"}**]{#struct_0_x2076_17954_603752198}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1482128850}

[[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_667724639}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1843581672}

[[聚合接口视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x729434167}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_340012785}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1523939615}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1101116374}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1162801923}

[[请在动态聚合接口下使能]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_603686662}[方式检测功能。聚合接口创建后，可使用]{style="font-family:宋体"}**[link-aggregation mode dynamic]{lang="EN-US"}**[命令将该接口配置为动态接口。]{style="font-family:宋体"}

[[为了防止]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1247612778}[级联组网时，本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测报文转发到邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中影响邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，执行]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[命令时，系统会要求用户输入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x21538217}[、]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1586566899}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1969663605}[在二层动态聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下启用]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1769425082}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] link-aggregation mode dynamic]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] mad enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}

[MAD LACP only enable on dynamic aggregation interface.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1133678832}[在三层动态聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下启用]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1632768934}

[\[Sysname\] interface route-aggregation 1]{lang="EN-US"}

[\[Sysname-Route-Aggregation1\] link-aggregation mode dynamic]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] mad enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}

[MAD LACP only enable on dynamic aggregation interface.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_306546296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_1500787974}
:::::

::::: {#640026197 .myid}
[]{#_Toc404783294}[]{#struct_0_x2076_17954_x658538158}[]{#_Toc300231747}[]{#_Toc237145865}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad exclude interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1769490618}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1162005519}
:::

**[ ]{lang="EN-US"}**

[**[mad exclude interface]{lang="EN-US"}**]{#struct_0_x2076_17954_998611666}[命令用来配置保留接口，当设备进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态时，该接口不会被关闭。]{style="font-family:宋体"}

[**[undo mad exclude interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x1769294010}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_283191101}

[**[mad exclude interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x967929163}

[**[undo mad exclude interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2076_17954_519106918}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1544278466}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_521247927}[物理端口是保留接口，设备进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态时会自动关闭本设备上所有的业务接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1112070937}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_588817665}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1769359546}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_2119348032}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1213358886}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2121215351}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2076_17954_682250452}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x813022424}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1903552645}[电缆断开后，网络中会存在多台全局配置完全相同的设备，这些设备连接到网络时可能会引起网络故障。为了防止这种情况发生，系统会进行多]{style="font-family:宋体"}[Active]{lang="EN-US"}[检测，最终只保留一台]{style="font-family:宋体"}[Active]{lang="EN-US"}[设备，其它设备都进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态，并且关闭]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态设备上的所有业务接口。使用该命令可以让指定的端口不被关闭，具体哪些接口需要保留由用户决定。建议除了]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录接口以及用于多]{style="font-family:宋体"}[Active]{lang="EN-US"}[检测的接口外，其他接口均关闭。]{style="font-family:宋体"}

[[当分裂的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_6699533}[恢复时，处于]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态的设备重启后重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，关闭的接口会自动恢复。也可以通过命令行]{style="font-family:宋体"}**[mad restore]{lang="EN-US"}**[对处于]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态的设备进行恢复，关闭的接口也会恢复正常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1777396277}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1769162938}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为保留接口，即当设备进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态时，该接口不会被关闭。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_204003123}

[\[Sysname\] mad exclude interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1231137779}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mad restore]{lang="EN-US"}**]{#struct_0_x2076_17954_x1198409938}
:::::

::::: {#-680367525 .myid}
[]{#_Toc404783295}[]{#struct_0_x2076_17954_x1784918895}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad ip address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1984606226}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1322161610}
:::

**[ ]{lang="EN-US"}**

[**[mad ip address]{lang="EN-US"}**]{#struct_0_x2076_17954_x637885114}[命令用来给指定成员设备配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo mad ip address]{lang="EN-US"}**]{#struct_0_x2076_17954_x1769228474}[命令用来删除相应的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x543521322}

[**[mad ip address]{lang="EN-US"}***[ ip-address ]{lang="EN-US"}*[{ *mask* \| *mask-length* } **member** *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x541227573}

[**[undo mad ip address]{lang="EN-US"}***[ ip-address ]{lang="EN-US"}*[{ *mask* \| *mask-length* } **member** *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x384710241}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1803044105}

[[没有为接口配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}]{#struct_0_x2076_17954_981857878}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x99367046}

[[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_1116546665}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x641929806}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1769031866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_75545457}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2021274236}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x2076_17954_2092341345}[：接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x2076_17954_x731326742}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相应的子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x2076_17954_1028913431}[：子网掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[member ]{lang="EN-US"}***[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x596275063}[：表示成员在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1071021235}

[[当使用]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x284777246}[检测时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备都需要配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址，这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与成员编号绑定，且必须为同一网段。但只有主设备的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址生效，从设备的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址不生效。当]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路分裂时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的原从设备变为主设备，配置的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址生效，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话被激活，设备将认为在网络中检测到存在配置冲突的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，在用于]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1769097402}[检测的接口下必须使用本命令配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址，而不要配置其它]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（包括使用]{style="font-family:宋体"}**[ip addres]{lang="EN-US"}**[s]{lang="EN-US"}[命令配置的普通]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址等），以免影响]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1039929455}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x479837130}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[在成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_225987083}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad ip address 192.168.0.1 255.255.255.0 member 1]{lang="EN-US"}

[[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_x534374517}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[在成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\[Sysname-Vlan-interface3\] mad ip address 192.168.0.2 255.255.255.0 member 2]{lang="EN-US"}]{#struct_0_x2076_17954_1300893668}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x500978099}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x678455643}
:::::

::::: {#-676151202 .myid}
[]{#_Toc404783296}[]{#struct_0_x2076_17954_x1768900794}[]{#_Toc300586617}[]{#_Toc300586675}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad nd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1359776256}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1268809231}
:::

**[ ]{lang="EN-US"}**

[**[mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1856512648}[命令用来使能]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1483750196}[用来关闭]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_442922762}

[**[mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x2046514554}

[**[undo mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_16317223}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_51375763}

[[ND MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1768966330}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x705088910}

[[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_936613206}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_211573485}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1631401228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1851729240}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x521317135}

[[为了防止]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1318286216}[级联组网时，本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测报文转发到邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中影响邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，执行]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令时，系统会要求用户输入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。]{style="font-family:宋体"}

[[VLAN 1]{lang="EN-US"}]{#struct_0_x2076_17954_1686793220}[不能用于]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，因此，不能在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1769425081}[、]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1595204523}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_593636184}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[上启用]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1600753571}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad nd enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2121879834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_1317012210}
:::::

::::: {#-196638449 .myid}
[]{#_Toc404783297}[]{#struct_0_x2076_17954_x1769490617}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad restore**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image004.png){width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1923108196}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_187394516}
:::

**[ ]{lang="EN-US"}**

[**[mad restore]{lang="EN-US"}**]{#struct_0_x2076_17954_x1288662605}[命令用来将设备从]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态恢复到正常状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1975736014}

[**[mad restore]{lang="EN-US"}**]{#struct_0_x2076_17954_716828745}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_936405572}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x2020493219}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x820454393}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1769294009}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x926728016}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_621651540}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1769359545}[链路故障会导致多]{style="font-family:宋体"}[Active]{lang="EN-US"}[冲突，原]{style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂为多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，为了防止网络中配置冲突，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统会通过多]{style="font-family:宋体"}[Active]{lang="EN-US"}[检测机制，让其中一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[继续正常工作，其它]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的状态修改为]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[（处于该状态的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[不能处理业务报文）。如果继续正常工作的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[也发生故障不能工作，此时可以通过本命令将处于]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[恢复到正常工作状态接替原]{style="font-family:宋体"}[IRF]{lang="EN-US"}[工作，以便保证业务尽量少受影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x609535323}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_17446987}[将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[从]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态恢复到正常状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_2081347823}

[\[Sysname\] mad restore]{lang="EN-US"}

[   This command will restore the device from multi-active conflict state. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Restoring from multi-active conflict state, please wait\...]{lang="EN-US"}
:::::

::: {#-1385841800 .myid}
[]{#_Toc404783298}[]{#struct_0_x2076_17954_851298337}[]{#_Toc300231750}[]{#_Toc246409983}[]{#_Toc239738063}[]{#_Toc235937657}[]{#_Toc234644239}

**IRF \-- IRF2配置命令（集中式IRF设备） \-- port group interface**

------------------------------------------------------------------------

[**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x660094454}[命令用来绑定设备的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口上第一次绑定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的同时相当于开启了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x1769162937}[命令用来取消设备的]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1718311178}

[**[port group interface]{lang="EN-US"}**[ *interface-type interface-number* \[ **mode** { **enhanced** \| **normal** } \]]{lang="EN-US"}]{#struct_0_x2076_17954_388844992}

[**[undo port group interface]{lang="EN-US"}***[ interface-name]{lang="EN-US"}*]{#struct_0_x2076_17954_1550860085}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x288611312}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x639452730}[端口没有与任何]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口进行绑定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_681823179}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1119122124}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x763225138}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1769228473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x2109605263}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1730163446}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1782745498}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的类型和编号。各型号设备上可用作]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的端口请参见产品的相关手册。]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x2076_17954_1625275934}[：]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的名称，格式为]{style="font-family:宋体"}*[interface-type+interface-number]{lang="EN-US"}*[。]{style="font-family:
宋体"}

[**[mode]{lang="EN-US"}**]{#struct_0_x2076_17954_904517199}[：设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的工作模式。该参数的支持情况以及缺省情况与设备的型号有关，请以实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enhanced]{lang="EN-US"}**]{#struct_0_x2076_17954_x943597981}[：将接口的工作模式设置为增强模式。]{lang="EN-US" style="font-family:宋体"}[本参数的支持情况与设备的]{style="font-family:宋体"}[的型号有关，请以实际情况为准。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[normal]{lang="EN-US"}**]{#struct_0_x2076_17954_x85931472}[：将接口的工作模式设置为普通模式。]{lang="EN-US" style="font-family:宋体"}[本参数的支持情况与设备的]{style="font-family:宋体"}[的型号有关，请以实际情况为准。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2128420798}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1769031865}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行该命令可以将同一]{style="font-family:宋体"}]{#struct_0_x2076_17954_x813491475}[IRF]{lang="EN-US"}[端口与多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定，最多可绑定的物理端口数与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的工作模式只在接口作为]{style="font-family:宋体"}]{#struct_0_x2076_17954_364994055}[IRF]{lang="EN-US"}[物理端口时生效，作为普通端口使用时不生效。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中直接相连的两个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的模式必须相同，否则，报文无法互通。]{style="font-family:宋体"}[当用于]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Virtual Private LAN Service]{lang="EN-US"}[，虚拟专用局域网服务）组网时，请设置为]{lang="EN-US" style="font-family:宋体"}**[enhanced]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要先使用]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_x2076_17954_1844263495}[命令关闭相应的物理端口，才能执行]{lang="EN-US" style="font-family:宋体"}**[port group interface]{lang="EN-US"}**[命令将]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[端口与该物理端口绑定。再使用]{lang="EN-US" style="font-family:
宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启该物理端口，该物理端口才能用作]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口建立]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[连接。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要先使用]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_x2076_17954_x2054500492}[命令关闭相应的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，才能执行]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令取消]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口与该]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的绑定关系。]{lang="EN-US" style="font-family:宋体"}[再使用]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，该物理端口才能用于报文的转发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些接口板出厂时已将接口分组，同一组内的接口只能都作为]{style="font-family:宋体"}]{#struct_0_x2076_17954_1697484976}[IRF]{lang="EN-US"}[物理端口，或者都不作为]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。当将某组中的一个接口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定时，系统要求先将该组中的所有接口都关闭，否则，绑定失败；当绑定后，将其中一个接口激活时，系统会判断该组中的其它接口是否已经和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定（可以绑定到同一]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，也可以绑定到不同]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口），如果没有绑定，则不允许激活。]{style="font-family:宋体"}

[[配置本命令后，即便热插拔接口板导致绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1838098940}[物理端口不存在了，但绑定关系仍然存在，使用]{style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令可以取消绑定关系。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1968981513}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1380844217}[将成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口]{style="font-family:宋体"}[Ten-GigabitEthernet3/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[IRF-port1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1769097401}

[\[Sysname\] interface ten-gigabitethernet 3/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet3/0/1\] shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet3/0/1\] quit]{lang="EN-US"}

[\[Sysname\] irf-port 3/1]{lang="EN-US"}

[\[Sysname-irf-port3/1\] port group interface ten-gigabitethernet 3/0/1]{lang="EN-US"}

[\[Sysname-irf-port3/1\] quit]{lang="EN-US"}

[\[Sysname\] interface ten-gigabitethernet 3/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet3/0/1\] undo shutdown]{lang="EN-US"}[]{#_Toc229558835}[]{#_Toc356463427}[]{#_Toc356463428}[]{#_Toc356463429}[]{#_Toc356463430}[]{#_Toc356463431}[]{#_Toc356463432}[]{#_Toc356463433}[]{#_Toc356463434}[]{#_Toc356463435}[]{#_Toc356463436}[]{#_Toc356463437}[]{#_Toc356463438}[]{#_Toc356463439}[]{#_Toc356463440}[]{#_Toc356463441}[]{#_Toc356463442}[]{#_Toc356463443}[]{#_Toc356463444}[]{#_Toc356463445}[]{#_Toc356463446}[]{#_Toc356463447}[]{#_Toc356463448}[]{#_Toc356463449}[]{#aa_57}[]{#_Toc317589907}[]{#_Toc266869840}[]{#_Toc266284581}[]{#_Toc264097537}[]{#_Ref264046745}[]{#_Toc356463450}[]{#_Toc356463451}[]{#_Toc356463452}[]{#_Toc356463453}[]{#_Toc356463454}[]{#_Toc356463455}[]{#_Toc356463456}[]{#_Toc356463457}[]{#_Toc356463458}[]{#_Toc356463459}[]{#_Toc356463460}[]{#_Toc356463461}[]{#_Toc356463462}[]{#_Toc356463463}[]{#_Toc356463464}[]{#_Toc356463465}[]{#_Toc356463466}[]{#_Toc356463467}[]{#_Toc356463468}[]{#_Toc356463469}[]{#_Toc356463470}[]{#_Toc356463471}[]{#_Toc356463472}[]{#_Toc356463473}[]{#_Toc356463474}[]{#_Toc229558850}[]{#_Toc216176722}[]{#_Toc347849254}[]{#_Toc347849255}[]{#_Toc347849256}[]{#_Toc347849257}[]{#_Toc347849258}
:::

::: {#310951257 .myid}
[]{#_Toc404783300}[]{#struct_0_x2076_17954_x1920309658}[]{#_Toc381194218}

**IRF \-- IRF2配置命令（分布式设备） \-- chassis convert mode irf**

------------------------------------------------------------------------

[**[chassis convert mode irf]{lang="EN-US"}**]{#struct_0_x2076_17954_x1104183272}[命令用来将设备的运行模式切换到]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式。]{style="font-family:
宋体"}

[**[undo chassis convert mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1247769701}[命令用来将设备的运行模式切换到独立运行模式。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2134169382}

[**[chassis convert mode irf]{lang="EN-US"}**]{#struct_0_x2076_17954_x2095669157}

[**[undo chassis convert mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x60785106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x944740738}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1869934220}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1247573093}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x232695914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_631937997}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x591521985}

[[设备出厂时处于独立运行模式。如果在本次运行过程中，没有修改设备的运行模式，则下次启动会延用本次启动的运行模式；如果在本次运行过程中，修改了设备的运行模式，则设备会自动重启，切换到新的模式。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1304211826}

[[请根据组网需要来配置设备的运行模式。当设备从独立运行模式切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_830380229}[模式后，即便只有一台设备也会形成]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。因为管理和维护]{style="font-family:宋体"}[IRF]{lang="EN-US"}[需要耗费一定的系统资源，所以，如果当前组网中设备不需要和别的设备组成]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，建议将运行模式配置为独立运行模式。]{style="font-family:宋体"}

[[设备从独立运行模式切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1194787755}[模式时，需要使用成员编号进行配置文件的自动转换。如果模式切换前没有配置成员编号，则系统会自动使用]{style="font-family:宋体"}[1]{lang="EN-US"}[作为成员编号。]{style="font-family:宋体"}

[[需要注意的是，确认模式切换操作后，设备会自动重启，完成运行模式的切换。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1247638629}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_956808158}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x498801162}[设备当前处于独立运行模式时，将设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x256658932}

[\[Sysname\] chassis convert mode irf]{lang="EN-US"}

[The device will switch to IRF mode and reboot. You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in IRF mode? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[Saving the converted configuration file to the main board succeeded.]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[ Saving the converted configuration file succeeded.]{lang="EN-US"}

[ Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_2009175968}[设备当前处于]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式时，将设备切换到独立运行模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x1248097388}

[\[Sysname\] undo chassis convert mode]{lang="EN-US"}

[The device will switch to stand-alone mode and reboot]{lang="EN-US"}[。]{style="font-family:宋体"}[ You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? \[Y/N\]:y]{lang="EN-US"}

[Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in stand-alone mode? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[Saving the converted configuration file to the main board succeeded.]{lang="EN-US"}

[Chassis 2 Slot 1:]{lang="EN-US"}

[Saving the converted configuration file succeeded.]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}
:::

::: {#-57452866 .myid}
[]{#_Toc404783301}[]{#struct_0_x2076_17954_x505664039}[]{#_Toc381194219}[]{#_Toc262637983}[]{#_Toc216513761}

**IRF \-- IRF2配置命令（分布式设备） \-- display irf**

------------------------------------------------------------------------

[**[display irf]{lang="EN-US"}**]{#struct_0_x2076_17954_x1677999090}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有成员设备的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x407032234}

[**[display irf]{lang="EN-US"}**]{#struct_0_x2076_17954_x795343031}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_94029839}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1248162924}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1899088754}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1361005608}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_1416922398}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1464198447}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_1288142956}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1247966316}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1786137533}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有成员设备的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf]{lang="EN-US"}]{#struct_0_x2076_17954_x1672251669}

[MemberID  Slot  Role   Priority  CPU-Mac         Description]{lang="EN-US"}

[ \*+1      0    Master  1         0210-fc03-0007  \-\-\-\--]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \* indicates the device is the master.]{lang="EN-US"}

[ + indicates the device through which the user logs in.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ The Bridge MAC of the IRF is: 3ce5-a6b8-3800]{lang="EN-US"}

[ Auto upgrade                : yes]{lang="EN-US"}

[ Mac persistent              : always]{lang="EN-US"}

[ Domain ID                   : 0]{lang="EN-US"}

[ Auto merge                  : no]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display irf]{lang="EN-US"}]{#struct_0_x2076_17954_x505075156}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1753170285}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1248031852}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_515834704}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_x1247835244}

[[本]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x843661685}[中成员设备的编号（如果编号前带"]{style="font-family:宋体"}[\*]{lang="EN-US"}["，表示该设备是主设备；如果编号前带"]{style="font-family:宋体"}[+]{lang="EN-US"}["，表示该设备是用户当前登录的、正在操作的设备）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_x2076_17954_x757823949}

[[成员设备上主控板所在的槽位号]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1247900780}

[[Role]{lang="EN-US"}]{#struct_0_x2076_17954_x637293205}

[[该主控板在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1247704172}[中的角色，取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby]{lang="EN-US"}]{#struct_0_x2076_17954_1971307575}[：全局备用主控板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x2076_17954_x1362265040}[：全局主用主控板]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loading]{lang="EN-US"}]{#struct_0_x2076_17954_x1247769708}[：正在自动加载系统启动文件的全局备用主控板]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x2076_17954_950944333}

[[成员设备的优先级]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1247573100}

[[CPU-MAC]{lang="EN-US"}]{#struct_0_x2076_17954_x1799238606}

[[设备的]{style="font-family:宋体"}[CPU MAC]{lang="EN-US"}]{#struct_0_x2076_17954_1398479156}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2076_17954_x1247638636}

[[设备的描述信息（没有描述信息时，]{style="font-family:宋体"}[Description]{lang="EN-US"}]{#struct_0_x2076_17954_x252979887}[字段显示为]{style="font-family:宋体"}[\"\-\-\-\--\"]{lang="EN-US"}[。如果描述信息较多，无法在一行中完全显示，则以"]{style="font-family:宋体"}[...]{lang="EN-US"}["结尾，省略后面的信息。此时可以使用]{style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**[命令来查询完整的描述信息）]{style="font-family:宋体"}

[[Bridge MAC of the IRF is]{lang="EN-US"}]{#struct_0_x2076_17954_x1248097387}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1060419902}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Auto upgrade]{lang="EN-US"}]{#struct_0_x2076_17954_x1248162923}

[[是否使能自动加载系统启动文件功能（]{style="font-family:宋体"}[yes]{lang="EN-US"}]{#struct_0_x2076_17954_x1636363655}[表示使能，]{style="font-family:宋体"}[no]{lang="EN-US"}[表示未使能）]{style="font-family:宋体"}

[[MAC persistent]{lang="EN-US"}]{#struct_0_x2076_17954_x1247966315}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1382853006}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留功能的配置信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6 min]{lang="EN-US"}]{#struct_0_x2076_17954_x1484350127}[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留时间为]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[always]{lang="EN-US"}]{#struct_0_x2076_17954_x1248031851}[表示]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址永久保留不改变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no]{lang="EN-US"}]{#struct_0_x2076_17954_112550177}[表示立即改变]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Domain ID]{lang="EN-US"}]{#struct_0_x2076_17954_x1247835243}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1603176572}[的域编号]{style="font-family:宋体"}

[[Auto merge]{lang="EN-US"}]{#struct_0_x2076_17954_x1247900779}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1284824488}[合并自动重启功能是否使能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[yes]{lang="EN-US"}]{#struct_0_x2076_17954_x1247704171}[：表示已经使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no]{lang="EN-US"}]{#struct_0_x2076_17954_405223634}[：表示没有使能]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#773439302 .myid}
[]{#_Toc404783302}[]{#struct_0_x2076_17954_x311077710}[]{#_Toc381194220}[]{#_Toc262637984}[]{#_Toc216513762}

**IRF \-- IRF2配置命令（分布式设备） \-- display irf configuration**

------------------------------------------------------------------------

[**[display irf configuration]{lang="EN-US"}**]{#struct_0_x2076_17954_1195853395}[命令用来显示所有成员设备上重启以后生效的]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1440810533}

[**[display irf configuration]{lang="EN-US"}**]{#struct_0_x2076_17954_x1247769707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_997998500}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1999811017}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1237654775}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1916314007}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_695376268}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_749673799}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1247573099}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1286333860}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1586560264}[设备工作在独立运行模式时，显示所有成员设备上重启以后生效的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[\<Sysname\> display irf configuration]{lang="EN-US"}]{#struct_0_x2076_17954_49988236}

[ MemberID Priority IRF-Port1                   IRF-Port2]{lang="EN-US"}

[ 1        1        disable                     disable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x718017932}[设备工作在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式时，显示所有成员设备上重启以后生效的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[\<Sysname\> display irf configuration]{lang="EN-US"}]{#struct_0_x2076_17954_x1247638635}

[ MemberID  NewID  IRF-Port1                     IRF-Port2]{lang="EN-US"}

[  1        1      Ten-GigabitEthernet1/1/0/1    disable]{lang="EN-US"}

[                  Ten-GigabitEthernet1/1/0/2]{lang="EN-US"}

[  2        2      disable                       Ten-GigabitEthernet2/1/0/1]{lang="EN-US"}

[                                                Ten-GigabitEthernet2/1/0/2]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display irf configuration]{lang="EN-US"}]{#struct_0_x2076_17954_x656264414}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1475545041}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x978706565}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1928610238}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_317986557}

[[设备当前的成员编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1626896153}

[[Priority]{lang="EN-US"}]{#struct_0_x2076_17954_317921021}

[[成员优先级。该字段只有设备处于独立运行模式时，才会显示]{style="font-family:宋体"}]{#struct_0_x2076_17954_x2030752702}

[[NewID]{lang="EN-US"}]{#struct_0_x2076_17954_1277952797}

[[配置的成员编号，设备重启后将会使用。该字段只有设备处于]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_318117629}[模式时，才会显示]{style="font-family:宋体"}

[[IRF-Port1]{lang="EN-US"}]{#struct_0_x2076_17954_x176465920}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_318052093}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[的配置（如果显示为多个端口，则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口由这些]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口聚合而成；如果显示为]{style="font-family:宋体"}[disable]{lang="EN-US"}[，则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口没有使能）]{style="font-family:宋体"}

[[IRF-Port2]{lang="EN-US"}]{#struct_0_x2076_17954_x1685491880}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_136886657}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[的配置（如果显示为多个端口，则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口由这些]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口聚合而成；如果显示为]{style="font-family:宋体"}[disable]{lang="EN-US"}[，则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口没有使能）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#331541433 .myid}
[]{#_Toc262637985}[]{#_Toc216513763}[]{#_Toc404783303}[]{#struct_0_x2076_17954_318248701}[]{#_Toc381194221}

**IRF \-- IRF2配置命令（分布式设备） \-- display irf link**

------------------------------------------------------------------------

[**[display irf link]{lang="EN-US"}**]{#struct_0_x2076_17954_1643040068}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x478395429}

[**[display irf link]{lang="EN-US"}**]{#struct_0_x2076_17954_x159227919}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x558251607}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1521712459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_318183165}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_633594398}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_309619920}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1395013273}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_763886305}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x106860228}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_425587176}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_318379773}

[Member 1]{lang="EN-US"}

[ IRF Port    Interface                       Status]{lang="EN-US"}

[ 1           disable                         \--]{lang="EN-US"}

[ 2           GigabitEthernet1/3/0/1(MDC1)    UP]{lang="EN-US"}

[             GigabitEthernet1/5/0/1(MDC2)    ADM]{lang="EN-US"}

[             GigabitEthernet1/6/0/1(MDC3)    DOWN]{lang="EN-US"}

[Member 2(IRF-Link-Down: MDC2, MDC3)]{lang="EN-US"}

[ IRF Port    Interface                       Status]{lang="EN-US"}

[ 1           GigabitEthernet2/3/0/1(MDC1)    UP]{lang="EN-US"}

[             GigabitEthernet2/5/0/1(MDC2)    DOWN]{lang="EN-US"}

[             GigabitEthernet2/6/0/1(MDC3)    ADM]{lang="EN-US"}

[ 2           disable                         \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_468569315}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[但不支持]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路检测功能的设备）。]{style="font-family:宋体"}

[[\<Sysname\> display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_2109271708}

[Member 1]{lang="EN-US"}

[ IRF Port    Interface                       Status]{lang="EN-US"}

[ 1           disable                         \--]{lang="EN-US"}

[ 2           GigabitEthernet1/3/0/1(MDC1)    UP]{lang="EN-US"}

[             GigabitEthernet1/5/0/1(MDC2)    ADM]{lang="EN-US"}

[             GigabitEthernet1/6/0/1(MDC3)    DOWN]{lang="EN-US"}

[Member 2]{lang="EN-US"}

[ IRF Port    Interface                       Status]{lang="EN-US"}

[ 1           GigabitEthernet2/3/0/1(MDC1)    UP]{lang="EN-US"}

[             GigabitEthernet2/5/0/1(MDC2)    DOWN]{lang="EN-US"}

[             GigabitEthernet2/6/0/1(MDC3)    ADM]{lang="EN-US"}

[ 2           disable                         \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_318314237}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路信息（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[也不支持]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路检测功能的设备）。]{style="font-family:宋体"}

[[\<Sysname\> display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_x1044806238}

[Member 1]{lang="EN-US"}

[ IRF Port    Interface                       Status]{lang="EN-US"}

[ 1           disable                         \--]{lang="EN-US"}

[ 2           GigabitEthernet1/3/0/1          UP]{lang="EN-US"}

[             GigabitEthernet1/5/0/1          ADM]{lang="EN-US"}

[             GigabitEthernet1/6/0/1          DOWN]{lang="EN-US"}

[Member 2]{lang="EN-US"}

[ IRF Port    Interface                       Status]{lang="EN-US"}

[ 1           GigabitEthernet2/3/0/1          UP]{lang="EN-US"}

[             GigabitEthernet2/5/0/1          DOWN]{lang="EN-US"}

[             GigabitEthernet2/6/0/1          ADM]{lang="EN-US"}

[ 2           disable                         \--]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display irf link]{lang="EN-US"}]{#struct_0_x2076_17954_183714669}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1458289655}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_318510845}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x771110402}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_x713620997}

[[成员编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_318445309}

[[(IRF-Link-Down: MDC2, MDC3)]{lang="EN-US"}]{#struct_0_x2076_17954_x408290608}

[[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_317986558}[链路检测功能检测到该成员设备上]{style="font-family:宋体"}[MDC2]{lang="EN-US"}[和]{style="font-family:宋体"}[MDC3]{lang="EN-US"}[中的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路状态为]{style="font-family:宋体"}[Down]{lang="EN-US"}[，于是将该成员设备上这两个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的业务口状态也变为]{style="font-family:宋体"}[down]{lang="EN-US"}[，不能转发报文（如果设备不支持]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路检测功能则不显示该信息）]{style="font-family:宋体"}

[[IRF Port]{lang="EN-US"}]{#struct_0_x2076_17954_x1626896154}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x551360659}[端口号，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_317921022}[表示]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x2076_17954_x2030752699}[表示]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x2076_17954_318117630}

[[对应的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1779849223}[物理端口的名称和该物理接口所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，用]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的编号表示（如果设备不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[则不显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示信息中包含多个物理端口则表示该]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1252255091}[IRF]{lang="EN-US"}[端口由多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口聚合而成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_x2076_17954_318052094}[disable]{lang="EN-US"}[则表示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口还没有和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2076_17954_x1685491887}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_318248702}[端口的物理接口的链路状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2076_17954_1643040067}[：链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2076_17954_x477543461}[：链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x2076_17954_318183166}[：]{lang="EN-US" style="font-family:宋体"}[用户在]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[下执行了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABSENT]{lang="EN-US"}]{#struct_0_x2076_17954_633594397}[：接口不]{lang="EN-US" style="font-family:宋体"}[存在，没有插入接口模块]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1617108997 .myid}
[]{#_Toc404783304}[]{#struct_0_x2076_17954_468569320}[]{#_Toc381194222}

**IRF \-- IRF2配置命令（分布式设备） \-- display irf topology**

------------------------------------------------------------------------

[**[display irf topology]{lang="EN-US"}**]{#struct_0_x2076_17954_535293593}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_149277694}

[**[display irf topology]{lang="EN-US"}**]{#struct_0_x2076_17954_975520134}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_482070083}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1858527425}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_318314238}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1044806253}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1738206416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_737733274}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1186134950}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1789872570}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_318510846}[显示当前]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\> display irf topology]{lang="EN-US"}]{#struct_0_x2076_17954_x771110401}

[                           Topology Info]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[               IRF-Port1                IRF-Port2]{lang="EN-US"}

[ MemberID    Link       neighbor      Link       neighbor    Belong To]{lang="EN-US"}

[ 3           DIS        \-\--           DOWN       \-\--         0210-fc03-0007]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display irf topology]{lang="EN-US"}]{#struct_0_x2076_17954_x713555461}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1435427935}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_1520709716}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_318445310}

[[MemberID]{lang="EN-US"}]{#struct_0_x2076_17954_1930361561}

[[成员编号]{style="font-family:宋体"}]{#struct_0_x2076_17954_x397303647}

[[IRF-Port1]{lang="EN-US"}]{#struct_0_x2076_17954_317986559}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1626896155}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[的信息，包括]{style="font-family:宋体"}[Link]{lang="EN-US"}[和]{style="font-family:宋体"}[neighbor]{lang="EN-US"}

[[IRF-Port2]{lang="EN-US"}]{#struct_0_x2076_17954_317921023}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x2030752700}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[的信息，包括]{style="font-family:宋体"}[Link]{lang="EN-US"}[和]{style="font-family:宋体"}[neighbor]{lang="EN-US"}

[[Link]{lang="EN-US"}]{#struct_0_x2076_17954_x1854215085}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_318117631}[端口的链路状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2076_17954_1779849224}[：]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2076_17954_318052095}[：]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DIS]{lang="EN-US"}]{#struct_0_x2076_17954_x1685491886}[：没有将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口与]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIMEOUT]{lang="EN-US"}]{#struct_0_x2076_17954_x1025912757}[：]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[报文超时]{lang="EN-US" style="font-family:宋体"}

[[neighbor]{lang="EN-US"}]{#struct_0_x2076_17954_318248703}

[[与该]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1643040066}[端口直连的设备的成员编号（显示为"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["表示该端口没有连接其它成员设备）]{style="font-family:宋体"}

[[Belong To]{lang="EN-US"}]{#struct_0_x2076_17954_318183167}

[[所属]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_633594396}[，用当前]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中主设备的]{style="font-family:宋体"}[CPU MAC]{lang="EN-US"}[地址来表示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1224569603 .myid}
[]{#_Toc216513764}[]{#_Toc216243482}[]{#_Toc216175590}[]{#_Toc214248964}[]{#_Toc213055955}[]{#_Toc404783305}[]{#struct_0_x2076_17954_309619930}[]{#_Toc381194223}[]{#_Toc262637986}

**IRF \-- IRF2配置命令（分布式设备） \-- display irf-port load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x561301863}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_318379775}
:::

[ ]{lang="EN-US"}

[**[display irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_468569321}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_535293592}

[**[display irf-port load-sharing mode ]{lang="EN-US"}**[\[ **irf-port** \[ *member-id*/*port-number* \] \]]{lang="EN-US"}]{#struct_0_x2076_17954_149277693}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_975520133}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_482070078}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_862461754}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_318314239}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x1044806252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_990676939}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_2053528333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1123369592}

[**[irf-port]{lang="EN-US"}**]{#struct_0_x2076_17954_1761976318}[：显示指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。不指定该参数时，显示全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[*[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_267914821}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号。其中，]{style="font-family:宋体"}*[member-id]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口索引，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[。不指定该参数时，显示所有连通的]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式，如果当前没有连通的]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[链路，则显示"]{style="font-family:宋体"}[No IRF link exists.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_318510847}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x771110400}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x2076_17954_x713489925}**[irf-port]{lang="EN-US"}**[参数，则显示全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路负载分担模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定]{style="font-family:宋体"}]{#struct_0_x2076_17954_x756284709}**[irf-port]{lang="EN-US"}**[参数而未指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号，则显示所有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下分别采用的负载分担模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x2076_17954_1536106362}[IRF]{lang="EN-US"}[端口编号，则显示该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下采用的负载分担模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1952633909}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1202858712}[显示缺省情况下全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode]{lang="EN-US"}]{#struct_0_x2076_17954_318445311}

[irf-port Load-Sharing Mode:]{lang="EN-US"}

[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}

[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}

[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}

[MPLS traffic   : mpls-label1,             mpls-label2,]{lang="EN-US"}

[                 mpls-label3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1930361560}[显示非缺省情况下全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode]{lang="EN-US"}]{#struct_0_x2076_17954_x397369183}

[irf-port Load-Sharing Mode:]{lang="EN-US"}

[destination-mac address, source-mac address]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x871953319}[显示缺省情况下]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode irf-port 1/1]{lang="EN-US"}]{#struct_0_x2076_17954_317986560}

[irf-port 1/1 Load-Sharing Mode:]{lang="EN-US"}

[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}

[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}

[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}

[MPLS traffic   : mpls-label1,             mpls-label2,]{lang="EN-US"}

[                 mpls-label3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1094093038}[显示非缺省情况下]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode irf-port 1/1]{lang="EN-US"}]{#struct_0_x2076_17954_x62194979}

[irf-port 1/1 Load-Sharing Mode:]{lang="EN-US"}

[destination-mac address, source-mac address]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x102360266}[显示所有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下分别采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display irf-port load-sharing mode irf-port]{lang="EN-US"}]{#struct_0_x2076_17954_x109055737}

[irf-port 1/1 Load-Sharing Mode:]{lang="EN-US"}

[  destination-ip address,  source-ip address,       mpls-label1]{lang="EN-US"}

[ ]{lang="EN-US"}

[irf-port 1/2 Load-Sharing Mode:]{lang="EN-US"}

[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}

[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}

[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}

[MPLS traffic   : mpls-label1,             mpls-label2,]{lang="EN-US"}

[                 mpls-label3]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display irf-port load-sharing mode]{lang="EN-US"}]{#struct_0_x2076_17954_317921024}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1413574857}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2030752705}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1094700198}

[[irf-port Load-Sharing Mode]{lang="EN-US"}]{#struct_0_x2076_17954_318117632}

[[全局采用的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1779849225}[链路负载分担类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省情况下显示：二层报文、三层报文、四层报文、]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1252124019}[MPLS]{lang="EN-US"}[报文采用的负载分担类型（各设备支持的报文类型不同，请以设备的实际情况为准）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非缺省情况下显示：用户配置后采用的负载分担类型]{style="font-family:宋体"}]{#struct_0_x2076_17954_318052096}

[[irf-port 1/1 Load-Sharing Mode]{lang="EN-US"}]{#struct_0_x2076_17954_x1685491885}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_318248704}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下采用的负载分担类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省情况下显示：全局采用的负载分担类型]{style="font-family:宋体"}]{#struct_0_x2076_17954_1643040073}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非缺省情况下显示：用户配置后采用的负载分担类型]{style="font-family:宋体"}]{#struct_0_x2076_17954_x477805604}

[[Layer 2 traffic: destination-mac address, source-mac address]{lang="EN-US"}]{#struct_0_x2076_17954_318183168}

[[二层报文缺省采用的负载分担类型：按照源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2076_17954_633594395}[地址和目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[Layer 3 traffic: destination-ip address,  source-ip address]{lang="EN-US"}]{#struct_0_x2076_17954_318379776}

[[三层报文缺省采用的负载分担类型：按照源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2076_17954_468569318}[地址和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[Layer 4 traffic: destination-port,        source-port]{lang="EN-US"}]{#struct_0_x2076_17954_2109271697}

[[四层报文缺省采用的负载分担类型：按照源端口和目的端口进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}]{#struct_0_x2076_17954_318314240}

[[MPLS traffic   : mpls-label1,             mpls-label2,                 mpls-label3]{lang="EN-US"}]{#struct_0_x2076_17954_x1854110309}

[[MPLS]{lang="EN-US"}]{#struct_0_x2076_17954_318510848}[报文缺省采用的负载分担类型：按照第]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[层的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[destination-mac address, source-mac address]{lang="EN-US"}]{#struct_0_x2076_17954_x771110415}

[[用户配置后采用的负载分担类型：按照源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2076_17954_x713293318}[地址和目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担（此字段的显示内容与用户的配置相关）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-68338408 .myid}
[]{#_Toc404783306}[]{#struct_0_x2076_17954_318445312}[]{#_Toc381194224}[]{#_Toc262637987}

**IRF \-- IRF2配置命令（分布式设备） \-- display mad**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_1930361559}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x396779360}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **mad**]{lang="EN-US"}]{#struct_0_x2076_17954_x897577773}[命令用来显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_339188388}

[**[display mad]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x2076_17954_x1697255190}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2064218592}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_317986553}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1626896149}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_564319052}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_x2078788940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1051284369}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_974082793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1705763999}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2076_17954_317921017}[：表示显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[详细配置信息。如果不使用该参数，则显示的是]{style="font-family:宋体"}[MAD]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x456774592}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1491607625}[显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[简要配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display mad]{lang="EN-US"}]{#struct_0_x2076_17954_1862520068}

[MAD ARP disabled.]{lang="EN-US"}

[MAD ND disabled.]{lang="EN-US"}

[MAD LACP disabled.]{lang="EN-US"}

[MAD BFD disabled.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x632990941}[显示]{style="font-family:宋体"}[MAD]{lang="EN-US"}[详细配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display mad verbose]{lang="EN-US"}]{#struct_0_x2076_17954_318117625}

[Excluded ports(configurable):]{lang="EN-US"}

[  Ten-GigabitEthernet2/1/0/2]{lang="EN-US"}

[  Ten-GigabitEthernet2/1/0/3]{lang="EN-US"}

[Excluded ports(can not be configured):]{lang="EN-US"}

[  Ten-GigabitEthernet2/2/0/25]{lang="EN-US"}

[  Ten-GigabitEthernet3/2/0/26]{lang="EN-US"}

[MAD enabled aggregation port:]{lang="EN-US"}

[  Bridge-Aggregation2]{lang="EN-US"}

[MAD BFD enabled interface:]{lang="EN-US"}

[  Vlan-interface2]{lang="EN-US"}

[    mad ip address 10.0.0.2 255.255.0.0 member 2]{lang="EN-US"}

[    mad ip address 10.0.0.3 255.255.0.0 member 3]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display mad]{lang="EN-US"}]{#struct_0_x2076_17954_x176465908}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1400696867}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_906256464}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_318052089}

[[MAD ARP disabled]{lang="EN-US"}]{#struct_0_x2076_17954_270823246}

[[没有使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_318248697}[检测功能]{style="font-family:宋体"}

[[MAD ND disabled]{lang="EN-US"}]{#struct_0_x2076_17954_x276539221}

[[没有使能]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x2128287509}[检测功能]{style="font-family:宋体"}

[[MAD LACP disabled]{lang="EN-US"}]{#struct_0_x2076_17954_318183161}

[[没有使能]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_633594402}[检测功能]{style="font-family:宋体"}

[[MAD BFD disabled]{lang="EN-US"}]{#struct_0_x2076_17954_318379769}

[[没有使能]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1487745827}[检测功能]{style="font-family:宋体"}

[[MAD ARP enabled.]{lang="EN-US"}]{#struct_0_x2076_17954_x1473495443}

[[已经使能了]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_318314233}[检测功能]{style="font-family:宋体"}

[[MAD ND enabled]{lang="EN-US"}]{#struct_0_x2076_17954_x1044806242}

[[已经使能了]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}]{#struct_0_x2076_17954_318510841}[检测功能]{style="font-family:宋体"}

[[MAD LACP enabled]{lang="EN-US"}]{#struct_0_x2076_17954_x771110406}

[[已经使能了]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x713358853}[检测功能]{style="font-family:宋体"}

[[MAD BFD enabled]{lang="EN-US"}]{#struct_0_x2076_17954_318445305}

[[已经使能了]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x408290596}[检测功能]{style="font-family:宋体"}

[[Current MAD status]{lang="EN-US"}]{#struct_0_x2076_17954_317986554}

[[MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1626896150}[当前的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detect]{lang="EN-US"}]{#struct_0_x2076_17954_317921018}[：检测状态，即]{style="font-family:宋体"}[IRF]{lang="EN-US"}[处于正常状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Recovery]{lang="EN-US"}]{#struct_0_x2076_17954_x456774581}[：发生多]{style="font-family:宋体"}[Active]{lang="EN-US"}[冲突时，失败的一方进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态，该状态下设备会自动关闭所有非保留的业务接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detect to Recovery]{lang="EN-US"}]{#struct_0_x2076_17954_1491804232}[：检测状态到]{lang="EN-US" style="font-family:
  宋体"}[Recovery]{lang="EN-US"}[状态的中间状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Recovery to Detect]{lang="EN-US"}]{#struct_0_x2076_17954_318117626}[：]{lang="EN-US" style="font-family:
  宋体"}[Recovery]{lang="EN-US"}[状态到检测状态的中间状态]{lang="EN-US" style="font-family:宋体"}

[[Excluded ports(configurable)]{lang="EN-US"}]{#struct_0_x2076_17954_x176465907}

[[用户配置的保留接口]{style="font-family:宋体"}]{#struct_0_x2076_17954_318052090}

[[Excluded ports(can not be configured)]{lang="EN-US"}]{#struct_0_x2076_17954_x1685491883}

[[系统默认保留的接口（不需要用户配置，自动保留）]{style="font-family:宋体"}]{#struct_0_x2076_17954_318248698}

[[MAD enabled aggregation port]{lang="EN-US"}]{#struct_0_x2076_17954_x276539230}

[[使能了]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_318183162}[的聚合口]{style="font-family:宋体"}

[[MAD BFD enabled interface]{lang="EN-US"}]{#struct_0_x2076_17954_633594401}

[[使能了]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_318379770}[的接口]{style="font-family:宋体"}

[[MAD BFD enabled interface:]{lang="EN-US"}]{#struct_0_x2076_17954_468569316}

[[  Vlan-interface2]{lang="EN-US"}]{#struct_0_x2076_17954_318314234}

[[    mad ip address 10.0.0.2 255.255.0.0 member 2]{lang="EN-US"}]{#struct_0_x2076_17954_x1044806241}

[[    mad ip address 10.0.0.3 255.255.0.0 member 3]{lang="EN-US"}]{#struct_0_x2076_17954_318510842}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x771110405}[中]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[的配置，包括在哪个三层接口下配置了]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[，各成员设备上的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[MAD ARP enabled interface:]{lang="EN-US"}]{#struct_0_x2076_17954_318445306}

[[使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x408290597}[的接口（该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[]{#_Toc214248965}[[ ]{lang="EN-US"}]{#_Toc213055956}

::::: {#-832819897 .myid}
[]{#_Toc216513765}[]{#_Toc262637988}[]{#_Toc261859886}[]{#_Toc404783307}[]{#struct_0_x2076_17954_2125590711}[]{#_Toc381194225}

**IRF \-- IRF2配置命令（分布式设备） \-- display port restricted**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x933353599}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1331538218}
:::

**[ ]{lang="EN-US"}**

[**[display port restricted]{lang="EN-US"}**]{#struct_0_x2076_17954_x85297970}[命令用来显示系统中被限制端口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_533078827}

[**[display port restricted]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \[ **slot** *slot-number* \] \]]{lang="EN-US"}]{#struct_0_x2076_17954_77113749}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x422131955}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1608813203}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x139372601}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x85363506}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_982559686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1682282455}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_1733814280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1824308818}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x1051625365}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上被限制端口的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定该参数时，显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有被限制端口的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x1071012637}[：表示指定接口板上被限制端口的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示接口板所在的槽位号，不指定该参数时，显示指定成员设备上的所有接口板上被限制端口的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85166898}

[[与]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x2048288853}[物理端口处于同一接口板上接口，被配置为三层聚合接口的成员端口的三层物理口时称为被限制端口。]{style="font-family:宋体"}

[[被限制端口可以正常收发单播和广播报文，但是对于组播报文，只能发送，不能接收。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1440066670}

[[该命令用于在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x761558217}[模式下帮助用户了解当前设备上哪些接口被限制了。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1233683381}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_75069480}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[4]{lang="EN-US"}[号接口板上的被限制端口的信息。]{style="font-family:
宋体"}

[[\<Sysname\> display port restricted chassis 1 slot 4]{lang="EN-US"}]{#struct_0_x2076_17954_1113832233}

[Chassis: 1]{lang="EN-US"}

[Slot: 4]{lang="EN-US"}

[Restricted ports:]{lang="EN-US"}

[  GigabitEthernet1/4/0/1 GigabitEthernet1/4/0/2]{lang="EN-US"}
:::::

::::: {#-704090095 .myid}
[]{#_Toc404783308}[]{#struct_0_x2076_17954_x842482907}

**IRF \-- IRF2配置命令（分布式设备） \-- easy-irf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x842482906}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[只在]{lang="EN-US" style="font-family:
KaiTi_GB2312"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x682940392}[模式下支持该命令]{lang="EN-US" style="font-family:KaiTi_GB2312"}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[easy-irf]{lang="EN-US"}**]{#struct_0_x2076_17954_1115994915}[命令用于快速配置堆叠环境。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1115994916}

[**[easy-irf]{lang="EN-US"}**[ \[ **member** *member-id* \[ **renumber** *new-member-id* \] **domain** *domain-id* \[ **priority** *priority* \] \[ **irf-port1** *interface-list1* \] \[ **irf-port2** *interface-list2* \] \]]{lang="EN-US"}]{#struct_0_x2076_17954_302634603}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1115994921}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1115994922}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_302372456}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1115994919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_302700139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1115994920}

[**[member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_1115994925}[：表示设备当前的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[renumber]{lang="EN-US"}**[ *new-member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x1699868348}[：表示新成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示不修改成员编号。]{style="font-family:宋体"}

[**[domain]{lang="EN-US"}**[ *domain-id*]{lang="EN-US"}]{#struct_0_x2076_17954_302437992}[：表示设备所属的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。同一]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中成员设备域编号应配置为相同值。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x2076_17954_1115994926}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。]{style="font-family:宋体"}

[**[irf-port1]{lang="EN-US"}**[ *interface-list1*]{lang="EN-US"}]{#struct_0_x2076_17954_302634600}[：表示和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。表示方式为]{style="font-family:宋体"}*[interface-list1]{lang="EN-US"}*[ = { *interface-type interface-number* }&\<1-n\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}[&\<1-n\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[n]{lang="EN-US"}[次。]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[irf-port2 ]{lang="EN-US"}***[interface-list2]{lang="EN-US"}*]{#struct_0_x2076_17954_x840320219}[：表示和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。表示方式为]{style="font-family:宋体"}*[interface-list2]{lang="EN-US"}*[ = { *interface-type interface-number* }&\<1-n\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}[&\<1-n\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[n]{lang="EN-US"}[次。]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值与设备的型号有关，请以设备的实际情况为准。同一物理端口只能一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x840320218}

[[使用该功能，用户可以通过一条命令配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1000795922}[的基本参数，包括新成员编号、域编号、绑定物理端口，简化了配置步骤，达到快速配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的效果。]{style="font-family:宋体"}

[[在配置该功能时，有两种方式：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x840320221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交互模式：用户输入]{lang="EN-US" style="font-family:宋体"}**[easy-irf]{lang="EN-US"}**]{#struct_0_x2076_17954_x1001385745}[，回车，在交互过程中输入具体参数的值。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非交互模式，在输入命令行时直接指定所需参数的值。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x840320220}

[[两种方式的配置效果相同，如果用户对本功能不熟悉，建议使用交互模式。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1001320209}

[[配置时，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x840320215}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果给成员设备指定新的成员编号，该成员设备会立即自动重启，以使新的成员编号生效。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x1001123602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次使用该功能，修改域编号]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_17954_x840320214}[优先级]{lang="EN-US" style="font-family:宋体"}[/IRF]{lang="EN-US"}[物理端口时，域编号和优先级的新配置覆盖旧配置，]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的配置会新旧进行叠加。如需删除旧的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口配置，需要在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图下，执行]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令。一个]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口最多可绑定多少个]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在交互模式下，为]{style="font-family:宋体"}]{#struct_0_x2076_17954_x760784397}[IRF]{lang="EN-US"}[端口指定物理端口时，请注意：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[接口类型和接口编号间不能有空格。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x2026245159}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[不同物理接口之间用英文逗号分隔。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_984261965}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[有些接口板出厂时已将接口分组，]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x1933739350}[如果要将该组]{style="font-family:宋体"}[内的]{lang="EN-US" style="font-family:宋体"}[某]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定，需要将该组的所有接口都和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1001058066}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x840320217}[通过非交互模式配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的新成员编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，域编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet2/1/0/21]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet2/1/0/22]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet2/1/0/23]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet2/1/0/24]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x840320211}

[\[Sysname\] easy-irf member 1 renumber 2 domain 10 priority 10 irf-port1 ten-gigabitethernet 2/1/0/21 ten-gigabitethernet 2/1/0/22 ten-gigabitethernet 2/1/0/23 ten-gigabitethernet 2/1/0/24]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[                  Configuration summary for member 2]{lang="EN-US"}

[IRF new member ID: 3]{lang="EN-US"}

[IRF domain ID    : 10]{lang="EN-US"}

[IRF priority     : 10]{lang="EN-US"}

[IRF-port 1       : Ten-GigabitEthernet2/1/0/21, Ten-GigabitEthernet2/1/0/22]{lang="EN-US"}

[                   Ten-GigabitEthernet2/1/0/23, Ten-GigabitEthernet2/1/0/24]{lang="EN-US"}

[IRF-port 2       : Disabled]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[Are you sure to use these settings to set up IRF? \[Y/N\] y]{lang="EN-US"}

[Starting to configure IRF\...]{lang="EN-US"}

[Configuration succeeded.]{lang="EN-US"}

[The device will reboot for the new member ID to take effect. Continue? \[Y/N\] y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1001385746}[通过交互模式配置成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[的新编号为]{style="font-family:宋体"}[5]{lang="EN-US"}[，域编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet3/1/0/21]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet3/1/0/22]{lang="EN-US"}[、]{style="font-family:宋体"}[Ten-GigabitEthernet3/1/0/23]{lang="EN-US"}[和]{style="font-family:宋体"}[Ten-GigabitEthernet3/1/0/24]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[]{#struct_0_x2076_17954_733657892}[]{#_Toc400991524}[]{#_Toc400991526}[]{#_Toc400991527}[]{#_Toc400991528}[]{#_Toc400991529}[]{#_Toc400991530}[]{#_Toc400991531}[]{#_Toc400991532}[]{#_Toc400991533}[]{#_Toc400991534}[]{#_Toc400991535}[]{#_Toc400991536}[]{#_Toc400991537}[]{#_Toc400991538}[]{#_Toc400991539}[]{#_Toc400991540}[]{#_Toc400991541}[]{#_Toc400991542}[]{#_Toc400991543}[]{#_Toc400991544}[]{#_Toc400991545}[]{#_Toc400991546}[]{#_Toc400991547}[]{#_Toc400991548}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] easy-irf]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[Welcome to use easy IRF.]{lang="EN-US"}

[To skip the current step, enter a dot sign (.).]{lang="EN-US"}

[To return to the previous step, enter a minus sign (-).]{lang="EN-US"}

[To use the default value (enclosed in \[\]) for each parameter, press Enter withou]{lang="EN-US"}

[t entering a value.]{lang="EN-US"}

[To quit the setup procedure, press CTRL+C.]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[Select a member by its ID \<3\> \[3\]:3]{lang="EN-US"}

[Specify a new member ID \<1\~10\> \[1\]: 5]{lang="EN-US"}

[Specify a domain ID \<0\~4294967295\> \[0\]: 10]{lang="EN-US"}

[Specify a priority \<1\~32\> \[1\]: 10]{lang="EN-US"}

[Specify IRF-port 1 bindings (a physical interface or a comma-separated physical]{lang="EN-US"}

[interface list)\[Disabled\]: ten-gigabitethernet3/1/0/21,ten-gigabitethernet3/1/0/22,ten-gigabitethernet3/1/0/23,ten-gigabitethernet3/1/0/24]{lang="EN-US"}

[Specify IRF-port 2 bindings (a physical interface or a comma-separated physical]{lang="EN-US"}

[interface list)\[Disabled\]:]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[                  Configuration summary for member 3]{lang="EN-US"}

[IRF new member ID: 5]{lang="EN-US"}

[IRF domain ID    : 10]{lang="EN-US"}

[IRF priority     : 10]{lang="EN-US"}

[IRF-port 1       : Ten-GigabitEthernet3/1/0/21, Ten-GigabitEthernet3/1/0/22]{lang="EN-US"}

[                   Ten-GigabitEthernet3/1/0/23, Ten-GigabitEthernet3/1/0/24]{lang="EN-US"}

[IRF-port 2       : Disabled]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[Are you sure to use these settings to set up IRF? \[Y/N\] y]{lang="EN-US"}

[Starting to configure IRF\...]{lang="EN-US"}

[Configuration succeeded.]{lang="EN-US"}

[The device will reboot for the new member ID to take effect. Continue? \[Y/N\] y]{lang="EN-US"}
:::::

::::: {#-1991809081 .myid}
[]{#_Toc404783309}[]{#struct_0_x2076_17954_2091556812}

**IRF \-- IRF2配置命令（分布式设备） \-- irf auto-merge enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1294970138}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1320579301}
:::

[ ]{lang="EN-US"}

[**[irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x435925840}[命令用来使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[**[undo irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x782918675}[命令用来关闭]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_893821043}

[**[irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x85035826}

[**[undo irf auto-merge enable]{lang="EN-US"}**]{#struct_0_x2076_17954_659855110}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x462961209}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1704826436}[合并自动重启功能处于使能状态。]{style="font-family:宋体"}[即]{style="font-family:宋体"}[两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并时，]{style="font-family:宋体"}[竞选失败方会自动重启。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1275399194}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x59499600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85101362}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1499567062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x643904353}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1238089919}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_527094841}[合并时，两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[会遵照角色选举的规则进行竞选，竞选失败方]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的所有成员设备需要重启才能加入获胜方]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有使能]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1363902939}[IRF]{lang="EN-US"}[合并自动重启功能，则合并过程中的重启需要用户根据系统提示手工完成。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使能]{style="font-family:宋体"}]{#struct_0_x2076_17954_x933883724}[IRF]{lang="EN-US"}[合并自动重启功能，则合并过程中的重启由系统自动完成。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x84904754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x2076_17954_1997392223}[IRF]{lang="EN-US"}[模式下，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[或]{style="font-family:宋体"}[DIS]{lang="EN-US"}[时，配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定，引起]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，从而触发]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并，此时，即便使能了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能，该功能也暂时不生效，系统会提示用户必须手工重启竞选失败方才能完成合并。此时，请使用]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令将当前配置（尤其是]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的配置）保存到下次启动配置文件后，再重启失败方。否则，失败方重启后，会因为没有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[配置信息而不能合并。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[其它情况下触发的]{style="font-family:宋体"}]{#struct_0_x2076_17954_x634949732}[IRF]{lang="EN-US"}[合并（比如]{style="font-family:宋体"}[IRF]{lang="EN-US"}[连接故障恢复后引起的合并；两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的启动配置文件中已经绑定了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，然后建立]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理连接引起]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口状态变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，触发的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并等），如果合并时已使能了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能，则竞选失败方会自动重启加入获胜方，合并为一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要使]{style="font-family:宋体"}]{#struct_0_x2076_17954_940643125}[IRF]{lang="EN-US"}[合并自动重启功能正常运行，请在即将合并的两台]{style="font-family:宋体"}[IRF]{lang="EN-US"}[上都使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1216629340}[模式下支持。配置]{lang="EN-US" style="font-family:宋体"}**[irf auto-merge enable]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x86721154}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_321230137}[使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[合并自动重启功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x84970290}

[\[Sysname\] irf auto-merge enable]{lang="EN-US"}
:::::

::::: {#-2087051999 .myid}
[]{#_Toc404783310}[]{#struct_0_x2076_17954_x398186437}[]{#_Toc381194227}[]{#_Toc262637989}

**IRF \-- IRF2配置命令（分布式设备） \-- irf auto-update enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_447942359}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1429574940}
:::

[ ]{lang="EN-US"}

[**[irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x2060427059}[命令用来使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统启动文件的自动加载功能。]{style="font-family:宋体"}

[**[undo irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1281629127}[命令用来关闭]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[系统启动文件的自动加载功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x84773682}

[**[irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x985377327}

[**[undo irf auto-update enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1253745244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x47850067}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x122682781}[系统启动文件的自动加载功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1962874152}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x84839218}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1985226687}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1633116386}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1508518845}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2055354342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有使能自动加载功能，当参与]{style="font-family:宋体"}]{#struct_0_x2076_17954_x836274049}[IRF]{lang="EN-US"}[的设备软件版本与主设备的软件版本不一致时，则新加入或者优先级低的设备不能正常启动。此时需要用户手工升级设备的软件版本后，再将设备加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能自动加载功能后，成员设备加入]{style="font-family:宋体"}]{#struct_0_x2076_17954_x555610239}[IRF]{lang="EN-US"}[时，会与主设备的软件版本号进行比较，如果不一致，则自动从主设备下载启动文件，然后使用新的系统启动文件重启，重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x85297969}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当新加入设备的型号和主设备当前运行的软件版本不配套时，自动加载功能可能不能正常工作。因此建议新设备加入]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1805573324}[IRF]{lang="EN-US"}[前，请确保新加入设备的型号和主设备当前运行的软件版本配套。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了能够自动加载成功，请确保从设备存储介质上有足够的空闲空间用于存放新的启动文件。如果从设备存储介质上空闲空间不足，系统会自动删除从设备的当前启动文件来完成加载。如果删除从设备的当前启动文件后空间仍然不足，从设备将无法进行自动加载。此时，需要管理员重启从设备并进入从设备的]{style="font-family:宋体"}]{#struct_0_x2076_17954_30100824}[Boot ROM]{lang="EN-US"}[菜单，删除一些不重要的文件后，再让从设备重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1571943440}[模式下支持。配置]{lang="EN-US" style="font-family:宋体"}**[irf auto-update enable]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1533798206}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x713602278}[使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统启动文件的自动加载功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x85363505}

[\[Sysname\] irf auto-update enable]{lang="EN-US"}
:::::

::: {#187221166 .myid}
[]{#_Toc216513766}[]{#_Toc218333697}[]{#_Toc404783311}[]{#struct_0_x2076_17954_982559687}[]{#_Toc381194228}[]{#_Toc262637990}[]{#_Toc241393551}

**IRF \-- IRF2配置命令（分布式设备） \-- irf domain**

------------------------------------------------------------------------

[**[irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_x1682282454}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}

[**[undo irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_167730339}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1075423675}

[**[irf domain]{lang="EN-US"}**[ *domain-id*]{lang="EN-US"}]{#struct_0_x2076_17954_807905563}

[**[undo irf]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_x2076_17954_x85166897}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2048288860}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_125951735}[的域编号为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1643056082}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x454136111}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x712100251}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_770691604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x85232433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1351294911}

[*[domain-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1294904602}[：]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的域编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1641006105}

[[为了适应各种组网应用，同一个网络里可以部署多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_2008254515}[。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[之间使用不同的域编号以示区别。在]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[和]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测组网中，如果中间设备本身也是一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统，则必须配置该命令确保本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[和中间设备组成的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的域编号不同，否则可能造成检测异常，甚至导致业务中断。]{style="font-family:宋体"}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_450226580}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。在缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。]{style="font-family:宋体"}

[[本命令只在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x85035825}[模式下支持。配置]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_659855109}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1493353920}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的域编号为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_620952321}

[\[Sysname\] irf domain 30]{lang="EN-US"}
:::

::: {#-1574170501 .myid}
[]{#_Toc404783312}[]{#struct_0_x2076_17954_x848129788}[]{#_Toc381194229}[]{#_Toc262637991}

**IRF \-- IRF2配置命令（分布式设备） \-- irf link-delay**

------------------------------------------------------------------------

[**[irf link-delay]{lang="EN-US"}**]{#struct_0_x2076_17954_764750390}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[延迟上报时间。]{style="font-family:宋体"}

[**[undo irf link-delay]{lang="EN-US"}**]{#struct_0_x2076_17954_802665777}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85101361}

[**[irf link-delay ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x2076_17954_1499567059}

[**[undo irf link-delay]{lang="EN-US"}**]{#struct_0_x2076_17954_x644625246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x977882174}

[[不同型号的设备支持的缺省情况不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_626256950}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1623194299}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x84904753}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1997392228}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x635539556}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1718555315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1233231279}

[*[interval]{lang="EN-US"}*]{#struct_0_x2076_17954_x116343970}[：表示延迟上报]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[的时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示不延迟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1738967950}

[[本命令只在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x84970289}[模式下支持。配置]{style="font-family:宋体"}**[irf link-delay]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1940465732}[环境中使用]{style="font-family:宋体"}[CFD]{lang="EN-US"}[、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能时，请保证]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[延迟上报时间小于]{style="font-family:宋体"}[CFD]{lang="EN-US"}[、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的超时时间，关于]{style="font-family:宋体"}[CFD]{lang="EN-US"}[、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能的介绍，请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[CFD]{lang="EN-US"}["、"]{style="font-family:宋体"}[BFD]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_766305666}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1185417751}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路]{style="font-family:宋体"}[down]{lang="EN-US"}[延迟上报时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x374910660}

[\[Sysname\] irf link-delay 300]{lang="EN-US"}
:::

::::: {#-1708032682 .myid}
[]{#_Toc404783313}[]{#struct_0_x2076_17954_x447169750}

**IRF \-- IRF2配置命令（分布式设备） \-- irf isolate member**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x204461509}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x447169753}
:::

**[ ]{lang="EN-US"}**

[**[irf isolate member]{lang="EN-US"}**]{#struct_0_x2076_17954_x447169752}[命令用来隔离某成员设备，即丢弃指定成员设备发送的所有报文。]{style="font-family:宋体"}

[**[undo irf isolate member]{lang="EN-US"}**]{#struct_0_x2076_17954_x204330437}[命令用来取消隔离。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x447169747}

[**[irf isolate member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x204133830}

[**[undo irf isolate member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_x447169746}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1126808357}

[[不隔离任何成员设备。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1451763789}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1126808358}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1126808355}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1451632717}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1126808356}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1126808361}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1451894858}

[[当使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_x2076_17954_1126808362}[命令查看到物理]{style="font-family:宋体"}[IRF]{lang="EN-US"}[接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误报文较多，或者]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中出现网络风暴时，可多次使用]{style="font-family:宋体"}**[irf isolate member]{lang="EN-US"}**[命令，将所有空闲的成员编号都隔离，再进行修复。成员设备被隔离后，其它成员设备收到该成员设备发送的报文时，会直接丢弃。如果后续需要扩充]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，需先执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令取消隔离。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1126808359}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1452419149}[隔离成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1126808360}

[\[Sysname\] irf isolate member 3]{lang="EN-US"}
:::::

::: {#212108750 .myid}
[]{#_Toc404783314}[]{#struct_0_x2076_17954_470549214}[]{#_Toc381194230}[]{#_Toc262637992}

**IRF \-- IRF2配置命令（分布式设备） \-- irf mac-address persistent**

------------------------------------------------------------------------

[**[irf ]{lang="EN-US"}[mac-address persistent]{lang="EN-US"}**]{#struct_0_x2076_17954_x84773681}[命令用来指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的保留时间。]{style="font-family:宋体"}

[**[undo irf ]{lang="EN-US"}[mac-address persistent]{lang="EN-US"}**]{#struct_0_x2076_17954_x985377328}[命令用来设置不保留]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，即主设备变更后，立即使用新主设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1253679708}

[**[irf ]{lang="EN-US"}[mac-address persistent]{lang="EN-US"}**[ { **always** \| **timer** }]{lang="EN-US"}]{#struct_0_x2076_17954_1062032652}

[**[undo irf ]{lang="EN-US"}[mac-address persistent]{lang="EN-US"}**]{#struct_0_x2076_17954_x350667515}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x502349171}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x84839217}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1985226686}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1633050850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x422963937}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x434806899}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1965426200}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1009486426}

[**[always]{lang="EN-US"}**]{#struct_0_x2076_17954_x85297968}[：指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留时间为永久保留。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x2076_17954_x1805573325}[：指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留时间为]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1535983117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2076_17954_1715870789}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留时间为]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟，当主设备离开]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟内不变化；如果主设备在]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟内重新又加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，则]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不会变化。如果]{style="font-family:宋体"}[6]{lang="EN-US"}[分钟后主设备没有回到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，则会使用新选举的主设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2076_17954_230622244}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址永久保留，则不管主设备是否离开]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址始终保持不变。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x2076_17954_x500224531}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不保留，立即变化。当主设备离开]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，系统立即使用新选举的主设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址做]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1431715030}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两个]{style="font-family:宋体"}]{#struct_0_x2076_17954_x85363504}[IRF]{lang="EN-US"}[的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址相同，则它们不能合并为一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{lang="EN-US" style="font-family:宋体"}[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_982559688}[和]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[组网时，需要将]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[配置为]{lang="EN-US" style="font-family:宋体"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址立即改变，即配置]{lang="EN-US" style="font-family:宋体"}**[undo irf ]{lang="EN-US"}[mac-address persistent]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_x1682282457}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中]{style="font-family:宋体"}[启用了]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议，则强烈建议用户配置]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址保留时间为永久保留]{lang="EN-US" style="font-family:宋体"}[，否则，可能]{style="font-family:宋体"}[会导致一系列问题。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_571014866}[模式下支持。配置]{lang="EN-US" style="font-family:宋体"}**[irf ]{lang="EN-US"}[mac-address persistent]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x682059561}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1506677702}[设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为永久保留。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x85166896}

[\[Sysname\] irf mac-address persistent always]{lang="EN-US"}
:::

::: {#-365652024 .myid}
[]{#_Toc216513767}[]{#_Toc404783315}[]{#struct_0_x2076_17954_x2048288859}[]{#_Toc381194231}

**IRF \-- IRF2配置命令（分布式设备） \-- irf member**

------------------------------------------------------------------------

[**[irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_1335870852}[命令用来在独立运行模式下配置设备的成员编号。]{style="font-family:宋体"}

[**[undo irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_x88009706}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2123538901}

[**[irf member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_795331674}

[**[undo irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_382553996}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85232432}

[[设备处于独立运行状态时，成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_1351294910}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1294839066}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_631690544}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1567573532}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_494514426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1453630460}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85035824}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_659855108}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1493353919}

[[成员编号有以下作用：]{style="font-family:宋体"}]{#struct_0_x2076_17954_620493568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备从独立运行模式切换到]{style="font-family:宋体"}]{#struct_0_x2076_17954_992562699}[IRF]{lang="EN-US"}[模式时，需要使用成员编号进行配置文件的自动转换。]{style="font-family:宋体"}[建议在独立运行模式下规划和修改设备的成员编号，以免成员编号冲突，设备切换到]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[，不能加入已有的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_49113095}[系统使用成员编号来唯一标识一台成员设备。如果在独立运行模式下，请使用]{style="font-family:宋体"}**[irf member]{lang="EN-US"}**[命令来配置，这种方式下配置的成员编号在设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后生效；如果在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下，请使用]{style="font-family:宋体"}**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ renumber ]{lang="EN-US"}***[new-member-id]{lang="EN-US"}*[命令来配置，这种方式下配置的成员编号需要重启设备才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85101360}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1499567060}[在独立运行模式下配置设备的成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x644035425}

[\[sysname\] irf member 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_167817882}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_2069860369}
:::

::: {#-1230269661 .myid}
[]{#_Toc404783316}[]{#struct_0_x2076_17954_x1175828919}[]{#_Toc381194232}[]{#_Toc262637994}

**IRF \-- IRF2配置命令（分布式设备） \-- irf member description**

------------------------------------------------------------------------

[**[irf member ]{lang="EN-US"}[description]{lang="EN-US"}**]{#struct_0_x2076_17954_93142010}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备的描述信息。]{style="font-family:宋体"}

[**[undo irf member ]{lang="EN-US"}[description]{lang="EN-US"}**]{#struct_0_x2076_17954_x84904752}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1997392229}

[**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ ]{lang="EN-US"}[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x2076_17954_x635605092}

[**[undo irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ ]{lang="EN-US"}[description]{lang="EN-US"}**]{#struct_0_x2076_17954_608148438}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1153356835}

[[成员设备没有描述信息。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1110352168}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x84970288}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1940465731}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_766240130}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x401101316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_725247355}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2004112175}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1230999684}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}

[*[text]{lang="EN-US"}*]{#struct_0_x2076_17954_x84773680}[：设备的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x985377329}

[[本命令只在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1253614172}[模式下支持。配置]{style="font-family:宋体"}**[irf member ]{lang="EN-US"}[description]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_731468380}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x204960600}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_225374663}

[\[Sysname\] irf member 1 description F1Num001]{lang="EN-US"}
:::

::: {#-1359654617 .myid}
[]{#_Toc404783317}[]{#struct_0_x2076_17954_x84839216}[]{#_Toc381194233}[]{#_Toc262637995}

**IRF \-- IRF2配置命令（分布式设备） \-- irf member priority**

------------------------------------------------------------------------

[**[irf member]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_x2076_17954_1985226685}[用来设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备的优先级。]{style="font-family:宋体"}

[**[undo irf member]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_x2076_17954_1632985314}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2041590549}

[**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_x2076_17954_x174203805}

[**[undo irf member ]{lang="EN-US"}***[member-id ]{lang="EN-US"}***[priority]{lang="EN-US"}**]{#struct_0_x2076_17954_1437169272}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x972470980}

[[设备的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_x85297967}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1805573338}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1939333180}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_686811019}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1446562323}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_162213515}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1757074930}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x85363503}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_x2076_17954_982559681}[：表示优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1682282448}

[[成员优先级有两种配置方式：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1801703665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在独立运行模式下，使用]{style="font-family:宋体"}]{#struct_0_x2076_17954_1647039915}**[irf priority]{lang="EN-US"}**[命令来配置。如果在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[形成过程中，想让某台设备当选为主设备，请使用这种方式配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1967497911}[模式下，使用]{lang="EN-US" style="font-family:宋体"}**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*[命令来配置。这种方式下配置的成员优先级会影响]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[运行过程中的角色选举过程，比如当前主设备离开]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[时，优先级高的成员设备会当选为新的主设备；当发生]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[合并的时候，主设备成员优先级高的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[会竞选成功。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85166895}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x2048288858}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下，将成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的成员设备的优先级设置为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x230213089}

[\[Sysname\] irf member 2 priority 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1235134844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_x843202993}
:::

::: {#437182802 .myid}
[]{#_Toc404783318}[]{#struct_0_x2076_17954_x298899603}[]{#_Toc381194234}[]{#_Toc262637996}[]{#_Toc216513768}

**IRF \-- IRF2配置命令（分布式设备） \-- irf member renumber**

------------------------------------------------------------------------

[**[irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_319884598}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备的成员编号。]{style="font-family:宋体"}

[**[undo irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_x85232431}[命令用来取消成员编号的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1351294909}

[**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ renumber ]{lang="EN-US"}***[new-member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1295428889}

[**[undo irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_2140185525}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_640407841}

[[设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_828877630}[模式后，使用的是独立运行模式下预配置的成员编号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85035823}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_659855107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1493353922}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_621083393}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1831701210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x590897120}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x726492347}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[new-member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x85101359}[：表示修改后的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1221422133}

[[设备处于独立运行状态时，成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_x321259945}[；切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后，使用的是独立运行模式下预配置的成员编号；如果模式切换前没有配置成员编号，则系统会自动使用]{style="font-family:宋体"}[1]{lang="EN-US"}[作为成员编号。]{style="font-family:宋体"}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1176692187}[使用成员编号来唯一标识一台成员设备。如果在独立运行模式下，请使用]{style="font-family:宋体"}**[irf member]{lang="EN-US"}**[命令来配置，这种方式下配置的成员编号在设备切换到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式后生效；如果在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下，请使用]{style="font-family:宋体"}**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ renumber ]{lang="EN-US"}***[new-member-id]{lang="EN-US"}*[命令来配置，这种方式下配置的成员编号需要重启设备才能生效。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_341980064}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要重启]{lang="EN-US" style="font-family:宋体"}*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x2021983433}[对应的设备，]{lang="EN-US" style="font-family:宋体"}*[new-member-id]{lang="EN-US"}*[才能生效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo irf member renumber]{lang="EN-US"}**]{#struct_0_x2076_17954_x84904751}[命令只能取消本次运行过程中配置的成员编号。设备重启后，设备的成员编号就变为]{lang="EN-US" style="font-family:宋体"}*[new-member-id]{lang="EN-US"}*[，不能再取消，只能重新配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2076_17954_1997392226}[IRF]{lang="EN-US"}[中以设备编号标识设备，接口的标识以及某些命令行都与成员编号有关，修改设备成员编号可能导致设备配置发生变化或者丢失，请慎重。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x634622052}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1750518799}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中设备（原成员编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）的成员编号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1097845068}

[\[Sysname\] irf member 2 renumber 4]{lang="EN-US"}

[Renumbering the member ID may result in configuration change or loss. Continue?\[Y/N\]y]{lang="EN-US"}

[[如果要取消以上配置，使设备的成员编号仍然是]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x2076_17954_193705340}[，则可以执行以下命令：]{style="font-family:宋体"}

[[\[Sysname\] undo irf member 2 renumber]{lang="EN-US"}]{#struct_0_x2076_17954_x84970287}

[Renumbering the member ID may result in configuration change or loss. Continue?\[Y/N\]y]{lang="EN-US"}

[[如果配置]{style="font-family:宋体"}[irf member 2 renumber 4]{lang="EN-US"}]{#struct_0_x2076_17954_1940465722}[后，重启设备，则设备的成员编号会变为]{style="font-family:宋体"}[4]{lang="EN-US"}[。此时，不能使用]{style="font-family:宋体"}[undo irf member 2 renumber]{lang="EN-US"}[恢复到编号]{style="font-family:宋体"}[2]{lang="EN-US"}[，只能使用]{style="font-family:宋体"}[irf member 4 renumber 2]{lang="EN-US"}[重新配置。]{style="font-family:宋体"}

[[【相关配置】]{style="font-family:黑体"}]{#struct_0_x2076_17954_766305667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf member]{lang="EN-US"}**]{#struct_0_x2076_17954_x1185417750}
:::

::::: {#330843028 .myid}
[]{#_Toc216513769}[]{#_Toc218333705}[]{#_Toc262637997}[]{#_Toc404783319}[]{#struct_0_x2076_17954_x1940994601}[]{#_Toc381194235}[]{#_Toc325728120}[]{#_Toc317589913}

**IRF \-- IRF2配置命令（分布式设备） \-- irf mode enhanced**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x2009054782}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1202324580}
:::

[ ]{lang="EN-US"}

[**[irf mode enhanced]{lang="EN-US"}**]{#struct_0_x2076_17954_x84773679}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能。]{style="font-family:宋体"}

[**[undo irf mode enhanced]{lang="EN-US"}**]{#struct_0_x2076_17954_x1705421352}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_226818544}

[**[irf mode enhanced]{lang="EN-US"}**]{#struct_0_x2076_17954_x159347219}

[**[undo irf mode enhanced]{lang="EN-US"}**]{#struct_0_x2076_17954_621461996}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x413002063}

[[设备上未配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x84839215}[增强功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1985226684}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1632919778}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x102087627}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1290187183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1960676971}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85297974}

[[未配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_533078823}[增强功能时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中最多可以支持]{style="font-family:宋体"}[2]{lang="EN-US"}[台成员设备；配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能后，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中最多可以支持]{style="font-family:宋体"}[4]{lang="EN-US"}[台成员设备，大大增强了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的吞吐量和可靠性，不过，部分功能模块的规格会低于未配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能时。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_77113753}[增强功能，需要注意以下几点：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x1239330190}[合并前，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员设备的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能的使能情况应该保持一致，即都配置或都取消]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能，否则，无法形成一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备创建了]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_x2076_17954_1665199200}[后，不能再配置]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能，即]{lang="EN-US" style="font-family:宋体"}**[irf mode enhanced]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:
宋体"}**[mdc]{lang="EN-US"}**[ *mdc-name* \[ **id** *mdc-id* \]]{lang="EN-US"}[命令互斥，不能同时配置。]{lang="EN-US" style="font-family:宋体"}[有关]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的详细描述，请参见"基础配置指导"中的"]{style="font-family:宋体"}[MDC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备运行在独立模式时，可以直接配置]{style="font-family:宋体"}]{#struct_0_x2076_17954_x2058280081}[IRF]{lang="EN-US"}[增强功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备运行在]{style="font-family:宋体"}]{#struct_0_x2076_17954_319408165}[IRF]{lang="EN-US"}[模式时，若存在]{style="font-family:宋体"}[三层以太网接口则需要切换为二层以太网接口（设备会有提示信息），才能配置]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能，]{lang="EN-US" style="font-family:宋体"}[关于三层以太网接口的详细介绍请参见"接口管理配置指导"中的"以太网接口"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备从非增强模式切换到增强模式后，某些特性的规格会发生改变，比如设备最多支持的]{style="font-family:宋体"}]{#struct_0_x2076_17954_x85363510}[VPLS]{lang="EN-US"}[实例或]{lang="EN-US" style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[实例数目等。所以，如果设备运行在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式，且当前配置了]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例或]{lang="EN-US" style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[实例]{style="font-family:宋体"}[，则需要重启设备后（设备会提示重启），才能配置]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能，否则配置失败。]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例]{lang="EN-US" style="font-family:宋体"}[的详细介绍请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[VPLS]{lang="EN-US"}["，]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[实例的详细介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换"中的"]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1356092476}[IRF]{lang="EN-US"}[增强功能后必须保存当前配置（执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了]{style="font-family:宋体"}]{#struct_0_x2076_17954_1660858788}[IRF]{lang="EN-US"}[增强功能后，不能再创建三层以太网接口]{style="font-family:宋体"}[/]{lang="EN-US"}[子接口，三层聚合接口]{style="font-family:宋体"}[/]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备运行在]{style="font-family:宋体"}]{#struct_0_x2076_17954_x979128845}[IRF]{lang="EN-US"}[模式且配置了]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能，此时用户如果想取消]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能（执行]{style="font-family:宋体"}**[undo irf mode enhanced]{lang="EN-US"}**[命令]{style="font-family:宋体"}[），必须保证成员设备小于等于两台且每台成员设备上只有一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，否则]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能无法取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x735093472}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_367154760}[在独立运行模式下，配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x85166902}

[\[Sysname\] irf mode enhanced]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x909171962}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x450075276}

[\[Sysname\] irf mode enhanced]{lang="EN-US"}
:::::

::: {#1463977157 .myid}
[]{#_Toc404783320}[]{#struct_0_x2076_17954_x1231050085}[]{#_Toc381194236}

**IRF \-- IRF2配置命令（分布式设备） \-- irf priority**

------------------------------------------------------------------------

[**[irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_x1377411644}[命令用来在独立运行模式下配置设备的成员优先级。]{style="font-family:宋体"}

[**[undo irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_x603317295}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x709734680}

[**[irf priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x2076_17954_x85232438}

[**[undo irf priority]{lang="EN-US"}**]{#struct_0_x2076_17954_1351294916}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1295232282}

[[设备的成员优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2076_17954_x1003486557}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x312508354}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x543721637}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1732540920}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x85035830}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1296460032}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x566655285}

[*[priority]{lang="EN-US"}*]{#struct_0_x2076_17954_59992212}[：表示优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1536830509}

[[成员优先级有两种配置方式：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x520879125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在独立运行模式下，使用]{style="font-family:宋体"}]{#struct_0_x2076_17954_x85101366}**[irf priority]{lang="EN-US"}**[命令来配置。如果在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[形成过程中，想让某台设备当选为主设备，请使用这种方式配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1499567058}[模式下，使用]{lang="EN-US" style="font-family:宋体"}**[irf member ]{lang="EN-US"}***[member-id]{lang="EN-US"}***[ priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*[命令来配置，这种方式下配置的成员优先级会影响]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[运行过程中的角色选举过程。比如当前主设备离开]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[时，优先级高的成员设备会当选为新的主设备；当发生]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[合并的时候，主设备成员优先级高的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[会竞选成功。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x644559710}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_514992800}[在独立运行模式下将本设备的成员优先级设置为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1222956707}

[\[sysname\] irf priority 32]{lang="EN-US"}

[]{#_Toc262637998}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_79776131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf member priority]{lang="EN-US"}**]{#struct_0_x2076_17954_1495439641}
:::

::::: {#-995261337 .myid}
[]{#_Toc404783321}[]{#struct_0_x2076_17954_x84904758}[]{#_Toc381194237}[]{#_Toc325728134}[]{#_Toc317589925}

**IRF \-- IRF2配置命令（分布式设备） \-- irf slot member**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_1997392219}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x635605093}
:::

[ ]{lang="EN-US"}

[**[irf slot member]{lang="EN-US"}**]{#struct_0_x2076_17954_608082902}[命令用来修改主控板的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员编号信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_78981818}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1167076464}

[**[irf slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}***[ member ]{lang="EN-US"}***[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x84970294}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x398186441}[模式：]{style="font-family:宋体"}

[**[irf chassi]{lang="EN-US"}[s ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}***[ member ]{lang="EN-US"}***[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_447549140}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1036866579}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1323360011}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x124111868}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_690648426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x84773686}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x985377331}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1254138461}[：表示备用主控板所在的槽位号。]{style="font-family:宋体"}

[**[chassi]{lang="EN-US"}[s ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1709951436}[：表示某个成员设备上备用主控板所在的槽位号。]{style="font-family:宋体"}

[*[member-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1342072994}[：表示目标设备的成员编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_681963932}

[[此命令用来设置指定槽位上主控板的目标设备的成员编号。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x888596811}

[[需要注意的是，本命令仅在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x84839222}[配置快速恢复时使用。其它场合下使用时会发生未知错误，请勿随意配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x735762503}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_727239659}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下，将成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位主控板的成员编号设置为]{style="font-family:
宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> irf chassis 2 slot 1 member-id 1]{lang="EN-US"}]{#struct_0_x2076_17954_785700555}
:::::

::::: {#852963714 .myid}
[]{#_Toc404783322}[]{#struct_0_x2076_17954_x1583037305}[]{#_Toc381194238}[]{#_Toc262637999}

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_432049156}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况以及支持的配置视图与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x85297973}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[不同视图下，本命令行支持的参数不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_533078826}
:::

[ ]{lang="EN-US"}

[**[irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_77113748}[命令用来配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[**[undo irf-port load-sharing]{lang="EN-US"}**[ **mode**]{lang="EN-US"}]{#struct_0_x2076_17954_1916520205}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2060974974}

[**[irf-port load-sharing mode]{lang="EN-US"}**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** ]{lang="EN-US"}]{#struct_0_x2076_17954_x1237310626}[[\|]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[ mpls-label2 ]{lang="EN-US"}**[\| **mpls-label3** \| **source-port** \| **source-ip** \| **source-mac** \| **vlan-id** } \* \| **flexible** }]{lang="EN-US"}

[**[undo irf-port load-sharing mode]{lang="EN-US"}**]{#struct_0_x2076_17954_1141413831}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x85363509}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_982559691}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_274032688}

[[系统视图]{style="font-family:宋体"}[/IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1816623895}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_927115033}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1413131537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x85166901}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x909171961}

[**[destination-ip]{lang="EN-US"}**]{#struct_0_x2076_17954_x450009740}[：表示按报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-mac]{lang="EN-US"}**]{#struct_0_x2076_17954_x1272634914}[：表示按报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x842714538}[：设置按报文的目的端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ingress-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x1091617016}[：设置按报文的入端口实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ip-protocol]{lang="EN-US"}**]{#struct_0_x2076_17954_x1658580695}[：表示按报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议类型进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label1]{lang="EN-US"}**]{#struct_0_x2076_17954_x85232437}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第一层（最外层）标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label2]{lang="EN-US"}**]{#struct_0_x2076_17954_1351294915}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第二层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label3]{lang="EN-US"}**]{#struct_0_x2076_17954_x1295166746}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第三层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**]{#struct_0_x2076_17954_1673114625}[：设置按报文的源端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**]{#struct_0_x2076_17954_x1054144683}[：表示按报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_x2076_17954_x892027259}[：表示按报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan-id]{lang="EN-US"}**]{#struct_0_x2076_17954_x85035829}[：表示按报文所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[flexible]{lang="EN-US"}**]{#struct_0_x2076_17954_659855113}[：设置按报文的不同类型]{style="font-family:宋体"}[L2]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[等分别按不同模式灵活实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x462961210}

[[用户可以通过全局配置（系统视图下）和端口下（]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1705416261}[端口视图下）的配置方式设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在系统视图下执行该命令，则该配置对所有]{style="font-family:宋体"}]{#struct_0_x2076_17954_1674841241}[IRF]{lang="EN-US"}[链路生效；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2076_17954_1211219815}[IRF]{lang="EN-US"}[端口视图下执行该命令，则该配置只对当前]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路生效；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1791047075}[链路会优先采用端口下的配置。如果端口下没有配置，则采用全局配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_x85101365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一视图下多次配置该命令，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_x2076_17954_1499567055}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设备不支持的负载分担模式，系统将提示用户不支持。]{style="font-family:宋体"}]{#struct_0_x2076_17954_x643838814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置负载分担模式前，请先将]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1657096534}[IRF]{lang="EN-US"}[端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定。否则，负载分担模式将配置失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1472551911}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x2019049526}[配置按报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址实现全局的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x84904757}

[\[Sysname\] irf-port load-sharing mode destination-mac]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1997392224}[配置按报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址实现]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/1]{lang="EN-US"}[下]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路的负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x634753124}

[\[Sysname\] irf-port 1/1]{lang="EN-US"}

[\[Sysname-irf-port 1/1\] irf-port load-sharing mode destination-mac]{lang="EN-US"}
:::::

::::: {#-963404750 .myid}
[]{#_Toc404783323}[]{#struct_0_x2076_17954_1362974542}[]{#_Toc381194239}[]{#_Toc262638000}

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port member-id/port-number**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 7 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x1874451179}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1372835879}
:::

[ ]{lang="EN-US"}

[**[irf-port ]{lang="EN-US"}***[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x84970293}[命令用来在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口并进入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图（如果该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口已经创建，则直接进入该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **irf-port** *member-id*/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x398186434}[用来删除指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_447745751}

[**[irf-port ]{lang="EN-US"}***[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x1122736240}

[**[undo irf-port ]{lang="EN-US"}***[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x817908391}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_476477411}

[[设备上没有创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x84773685}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x985377332}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1254072925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_227163101}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_2122232878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1138880434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_872027418}

[*[member-id]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x84839221}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号。其中，]{style="font-family:宋体"}*[member-id]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口索引，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x735762504}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_727043051}[端口创建后，必须在该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下绑定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，才能用于]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[相关配置可参考命令]{style="font-family:宋体"}**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_1346116252}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_523143194}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1181118460}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式下为成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的设备创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1480785971}

[\[Sysname\] irf-port 1/1]{lang="EN-US"}
:::::

::: {#-1495814558 .myid}
[]{#_Toc404783324}[]{#struct_0_x2076_17954_x1026507233}[]{#_Toc381194240}

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port port-number**

------------------------------------------------------------------------

[**[irf-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x1581313170}[命令用来在独立运行模式下创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口并进入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图（如果该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口已经创建，则直接进入该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口视图）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **irf-port** *port-number*]{lang="EN-US"}]{#struct_0_x2076_17954_371712733}[用来删除指定]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1708290331}

[**[irf-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x2109791190}

[**[undo irf-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1480720435}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_953972500}

[[设备上没有创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1408035802}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1442092303}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_647373298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2032664663}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x384020464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1480917043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1318179872}

[*[port-number]{lang="EN-US"}*]{#struct_0_x2076_17954_962213190}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口编号，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1741633949}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_2061690894}[在处于独立运行模式下创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_2137606022}

[\[Sysname\] irf-port 1]{lang="EN-US"}

[\[Sysname-irf-port1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1480851507}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_1737747205}
:::

::: {#305974533 .myid}
[]{#_Toc216513770}[]{#_Toc216243484}[]{#_Toc216175592}[]{#_Toc214248966}[]{#_Toc404783325}[]{#struct_0_x2076_17954_1438168808}[]{#_Toc381194241}[]{#_Toc262638002}

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port-configuration active**

------------------------------------------------------------------------

[**[irf-port-configuration active]{lang="EN-US"}**]{#struct_0_x2076_17954_x813450796}[命令用于来激活设备上所有]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[端口下的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_347525796}

[**[irf-port-configuration active]{lang="EN-US"}**]{#struct_0_x2076_17954_2139779912}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1481048115}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x178728295}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_368729555}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_805811633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_62227224}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x568521619}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1480982579}[物理线缆连接好，并将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口添加到]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口后，必须通过该命令手工激活]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口的配置才能形成]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[系统启动，通过配置文件将]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_2110295320}[物理端口加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，或者]{style="font-family:宋体"}[IRF]{lang="EN-US"}[形成后再加入新的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口下的配置会自动激活不再需要使用该命令来激活。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2078103089}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x253715256}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1/2]{lang="EN-US"}[状态为]{style="font-family:宋体"}[DIS]{lang="EN-US"}[的情况下，激活该]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x40850526}[端口状态为]{style="font-family:宋体"}[DIS]{lang="EN-US"}[表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口还没有与任何]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定，所以，先配置绑定关系。绑定前需要先将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口关闭，绑定后再将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口激活。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1481179187}

[\[Sysname\] interface ten-gigabitEthernet 1/1/0/27]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/27\] shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/27\] quit]{lang="EN-US"}

[\[Sysname\] irf-port 1/2]{lang="EN-US"}

[\[Sysname-irf-port1/2\] port group interface ten-gigabitethernet 1/1/0/27]{lang="EN-US"}

[ Info : You are recommended to save the configuration now; otherwise, it will be lost after system reboot.]{lang="EN-US"}

[\[Sysname-irf-port1/2\] quit]{lang="EN-US"}

[\[Sysname\] interface ten-gigabitethernet 1/1/0/27]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/27\] undo shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/27\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将当前配置保存到下次启动配置文件，以便]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1751169266}[IRF]{lang="EN-US"}[端口的配置在设备重启后能继续生效。]{style="font-family:宋体"}

[[\[Sysname\] save]{lang="EN-US"}]{#struct_0_x2076_17954_x1955652962}

[The current configuration will be written to the device. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/startup.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[flash:/aa.cfg exists, overwrite? \[Y/N\]:y]{lang="EN-US"}

[ Validating file. Please wait\...\...\...\...\...\...\...\...\....]{lang="EN-US"}

[ Saved the current configuration to mainboard device successfully.]{lang="EN-US"}

[Chassis 1 Slot 1:]{lang="EN-US"}

[ Save next configuration file successfully.]{lang="EN-US"}

[ Configuration is saved to device successfully.]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[激活]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x443019530}[端口的配置。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] irf-port-configuration active]{lang="EN-US"}]{#struct_0_x2076_17954_1165306334}
:::

::::: {#-1213632741 .myid}
[]{#_Toc404783326}[]{#struct_0_x2076_17954_1481113651}[]{#_Toc381194242}[]{#_Toc262638003}[]{#_Toc237145861}

**IRF \-- IRF2配置命令（分布式设备） \-- mad arp enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image003.png){#图片 10 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x605879619}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_293538649}
:::

[ ]{lang="EN-US"}

[**[mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1703747272}[命令用来使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x925793966}[用来关闭]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_820862794}

[**[mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1481310259}

[**[undo mad arp enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x1407813742}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x171834970}

[[ARP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1058679444}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_306914507}

[[三层接口视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1540723257}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x416821548}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1481244723}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_2120370718}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_143926971}

[[为了防止]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1578648985}[级联组网时，本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测报文转发到邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中影响邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，执行]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[命令时，系统会要求用户输入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。]{style="font-family:宋体"}

[[VLAN 1]{lang="EN-US"}]{#struct_0_x2076_17954_43487220}[不能用于]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，因此，不能在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1284748731}[、]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1480785972}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1026572769}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[上启用]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_86945098}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad arp enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}
:::::

::::: {#73545972 .myid}
[]{#_Toc404783327}[]{#struct_0_x2076_17954_x1181601727}[]{#_Toc381194243}[]{#_Toc262638004}

**IRF \-- IRF2配置命令（分布式设备） \-- mad bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 11 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_2099732383}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1480720436}
:::

[ ]{lang="EN-US"}

[**[mad]{lang="EN-US"}**[ **bfd** **enable**]{lang="EN-US"}]{#struct_0_x2076_17954_954169108}[命令用来使能]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mad** **bfd** **enable**]{lang="EN-US"}]{#struct_0_x2076_17954_1884935630}[用来关闭]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x111297199}

[**[mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1699759757}

[**[undo mad bfd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x729334061}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1616695644}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1480917044}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1318245408}

[[三层接口视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_647586616}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2096550954}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_619990098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_180960199}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x236808118}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2076_17954_1480851508}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN 1]{lang="EN-US"}]{#struct_0_x2076_17954_1737288453}[不能用于]{lang="EN-US" style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，因此，不能在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[下使能]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[ MAD]{lang="EN-US"}[检测功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1034598969}[、]{lang="EN-US" style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{lang="EN-US" style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能]{style="font-family:宋体"}]{#struct_0_x2076_17954_x2136426166}[BFD MAD]{lang="EN-US"}[检测功能的三层接口只能专用于]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测，不允许运行其它业务。如果用户配置了其它业务，可能会影响该业务以及]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能的运行。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1040667069}[检测功能与]{style="font-family:宋体"}[VPN]{lang="EN-US"}[功能互斥，请不要将使能了]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能的三层接口与]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例进行绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1347018210}[检测功能与生成树功能互斥，在使能了]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能的三层接口对应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的端口上，请不要使能生成树协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_92268717}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1481048116}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[上启用]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x178793831}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad bfd enable]{lang="EN-US"}
:::::

::::: {#1722888386 .myid}
[]{#_Toc404783328}[]{#struct_0_x2076_17954_1042708288}[]{#_Toc381194244}[]{#_Toc262638005}

**IRF \-- IRF2配置命令（分布式设备） \-- mad enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image003.png){#图片 12 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x104273851}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x193692640}
:::

[ ]{lang="EN-US"}

[**[mad]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x2076_17954_x944358091}[命令用来使能]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mad** **enable**]{lang="EN-US"}]{#struct_0_x2076_17954_1480982580}[用来关闭]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2110885149}

[**[mad enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x1827580559}

[**[undo mad enable]{lang="EN-US"}**]{#struct_0_x2076_17954_1271860672}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_166016004}

[[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x1810803792}[方式检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x896596598}

[[聚合接口视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1481179188}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1751890162}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1815613324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1026598672}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1459607568}

[[该命令可以在动态或静态聚合口下配置，但由于]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1363670156}[检测依赖于]{style="font-family:宋体"}[LACP]{lang="EN-US"}[协议，因此只在动态聚合接口下生效。]{style="font-family:宋体"}

[[为了防止]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1481113652}[级联组网时，本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测报文转发到邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中影响邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，执行]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[命令时，系统会要求用户输入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_x605814083}[、]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1625570215}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1133323048}[在二层动态聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下启用]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1087781807}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] mad enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}

[MAD LACP only enable on dynamic aggregation interface.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x752817236}[在三层动态聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下启用]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1481310260}

[\[Sysname\] interface route-aggregation 1]{lang="EN-US"}

[\[Sysname-Route-Aggregation1\] mad enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}

[MAD LACP only enable on dynamic aggregation interface.]{lang="EN-US"}
:::::

::::: {#-1586529599 .myid}
[]{#_Toc404783329}[]{#struct_0_x2076_17954_x1407354989}[]{#_Toc381194245}[]{#_Toc262638006}

**IRF \-- IRF2配置命令（分布式设备） \-- mad exclude interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 13 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_761914477}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_2125839852}
:::

[ ]{lang="EN-US"}

[**[mad]{lang="EN-US"}**[ **exclude** **interface**]{lang="EN-US"}]{#struct_0_x2076_17954_1835614159}[命令用来配置保留接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mad** **exclude** **interface**]{lang="EN-US"}]{#struct_0_x2076_17954_1481244724}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2120829470}

[**[mad]{lang="EN-US"}**[ **exclude** **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2076_17954_1287208913}

[**[undo mad]{lang="EN-US"}**[ **exclude interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x2007051557}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1293110059}

[[设备进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}]{#struct_0_x2076_17954_x75671405}[状态时会自动关闭本设备上所有的业务接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1971707838}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1480785973}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1026638305}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_31940550}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1259100545}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1324390067}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2076_17954_x842406844}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1480720437}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_954103572}[电缆断开后，网络中会存在两台（或者多台）全局配置完全相同的设备，这些设备连接到网络时可能会引起网络故障。为了防止这种情况发生，系统会进行多]{style="font-family:宋体"}[Active]{lang="EN-US"}[检测，最终只保留一台]{style="font-family:宋体"}[Active]{lang="EN-US"}[设备，其它设备都进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态，并且关闭]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态设备上的所有业务接口。使用该命令可以让指定的端口不被关闭，具体哪些接口需要保留由用户决定。建议除了对]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录接口以及用于多]{style="font-family:宋体"}[Active]{lang="EN-US"}[检测的接口外，其他接口均关闭。]{style="font-family:宋体"}

[[当分裂的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1154941838}[恢复时，处于]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态的设备重启后重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，关闭的接口会自动恢复。也可以通过命令行]{style="font-family:宋体"}**[mad restore]{lang="EN-US"}**[对处于]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态的设备进行恢复，关闭的接口恢复正常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_548253518}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_788966866}[配置]{style="font-family:宋体"}[GigabitEthernet1/1/0/1]{lang="EN-US"}[为保留接口，即当设备进入]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态时，该接口不会被关闭。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_x353716244}

[\[Sysname\] mad exclude interface gigabitethernet 1/1/0/1]{lang="EN-US"}
:::::

::::: {#-1530551689 .myid}
[]{#_Toc404783330}[]{#struct_0_x2076_17954_1480917045}[]{#_Toc381194246}[]{#_Toc262638007}

**IRF \-- IRF2配置命令（分布式设备） \-- mad ip address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 14 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_1318310944}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1373832516}
:::

[ ]{lang="EN-US"}

[**[mad ip address]{lang="EN-US"}**]{#struct_0_x2076_17954_188816692}[命令用来给指定成员设备配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mad** **ip** **address**]{lang="EN-US"}]{#struct_0_x2076_17954_336683143}[命令用来删除相应的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1752646022}

[**[mad ip address]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[ { *mask* \| *mask-length* } **member** *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_615058059}

[**[undo mad ip address ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ { *mask* \| *mask-length* } **member** *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_1480851509}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1737353989}

[[没有为接口配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}]{#struct_0_x2076_17954_x963343920}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x37847370}

[[三层接口视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_585004826}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_657701091}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1481048117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x178859367}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x40834674}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x2076_17954_x1364534725}[：接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x2076_17954_1065394246}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相应的子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x2076_17954_x1679350185}[：子网掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[member]{lang="EN-US"}**[ *member-id*]{lang="EN-US"}]{#struct_0_x2076_17954_1480982581}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2110819613}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1317742554}[检测使用]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址来进行，]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[与普通]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不同的地方在于该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与成员编号绑定，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员设备的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址必须为同一网段，只有主设备的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址生效，从设备的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址不生效。当]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路分裂时，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的原从设备变为主设备，配置的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址生效，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话被激活。]{style="font-family:宋体"}

[[需要注意的是，在用于]{style="font-family:宋体"}[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_2030574483}[检测的接口下必须使用本命令配置]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址，而不要配置其它]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（包括使用]{style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令配置的普通]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址等），以免影响]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1665807945}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1847886596}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[在成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1481179189}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad ip address 192.168.0.1 255.255.255.0 member 1]{lang="EN-US"}

[[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_x1751824626}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[在成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAD IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\[Sysname-Vlan-interface3\] mad ip address 192.168.0.2 255.255.255.0 member 2]{lang="EN-US"}]{#struct_0_x2076_17954_815897526}
:::::

::::: {#-2053403296 .myid}
[]{#_Toc262638008}[]{#_Toc404783331}[]{#struct_0_x2076_17954_234027200}[]{#_Toc381194247}[]{#_Toc328668826}[]{#_Toc300231745}

**IRF \-- IRF2配置命令（分布式设备） \-- mad nd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image001.png){#图片 8 width="63" height="26"}]{lang="EN-US"}]{#struct_0_x2076_17954_1668566493}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1481113653}
:::

**[ ]{lang="EN-US"}**

[**[mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x605748547}[命令用来使能]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x862874016}[用来关闭]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1691481139}

[**[mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_x1423187056}

[**[undo mad nd enable]{lang="EN-US"}**]{#struct_0_x2076_17954_878866744}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1588129445}

[[ND MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1481310261}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1407289453}

[[VLAN]{lang="EN-US"}]{#struct_0_x2076_17954_686172849}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1235054497}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x750106782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1554200155}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1481244725}

[[为了防止]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_2120763934}[级联组网时，本]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测报文转发到邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中影响邻居]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，执行]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令时，系统会要求用户输入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号是一个全局变量，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[都共用这个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[irf domain]{lang="EN-US"}**[命令，或者在任意]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上通过]{style="font-family:宋体"}**[mad enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad arp enable]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mad nd enable]{lang="EN-US"}**[命令均可修改全局]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号。因此，请按照网络规划来修改]{style="font-family:宋体"}[IRF]{lang="EN-US"}[域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。]{style="font-family:宋体"}

[[VLAN 1]{lang="EN-US"}]{#struct_0_x2076_17954_x635599598}[不能用于]{style="font-family:宋体"}[MAD]{lang="EN-US"}[检测，因此，不能在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[BFD MAD]{lang="EN-US"}]{#struct_0_x2076_17954_1698108087}[、]{style="font-family:宋体"}[ARP MAD]{lang="EN-US"}[、]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[这三种检测方式独立工作，可以同时配置，但不能和]{style="font-family:宋体"}[LACP MAD]{lang="EN-US"}[方式同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x365448275}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x390824847}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[3]{lang="EN-US"}[上启用]{style="font-family:宋体"}[ND MAD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1480785974}

[\[Sysname\] interface vlan-interface 3]{lang="EN-US"}

[\[Sysname-Vlan-interface3\] mad nd enable]{lang="EN-US"}

[ You need to assign a domain ID (range: 0-4294967295)]{lang="EN-US"}

[ \[Current domain is: 0\]: 1]{lang="EN-US"}

[ The assigned  domain ID is: 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1026703841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf domain]{lang="EN-US"}**]{#struct_0_x2076_17954_1019292226}
:::::

::::: {#17138067 .myid}
[]{#_Toc404783332}[]{#struct_0_x2076_17954_2144017455}[]{#_Toc381194248}

**IRF \-- IRF2配置命令（分布式设备） \-- mad restore**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 15 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_x785321901}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_1480720438}
:::

[ ]{lang="EN-US"}

[**[mad restore]{lang="EN-US"}**]{#struct_0_x2076_17954_954824468}[命令用来将设备从]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态恢复到正常状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_623939387}

[**[mad restore]{lang="EN-US"}**]{#struct_0_x2076_17954_x1831113837}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x722159900}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1611457977}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1480917046}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1318376480}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x2091454858}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1105151959}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x589326229}[链路故障会导致多]{style="font-family:宋体"}[Active]{lang="EN-US"}[冲突，原]{style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂为多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，为了防止网络中配置冲突，]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统会通过多]{style="font-family:宋体"}[Active]{lang="EN-US"}[检测机制，让其中一个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[继续正常工作，其它]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的状态修改为]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[（处于该状态的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[不能处理业务报文）。如果继续正常工作的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[也发生故障不能工作，此时可以通过本命令将处于]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[恢复到正常工作状态接替原]{style="font-family:宋体"}[IRF]{lang="EN-US"}[工作，以便保证业务尽量少受影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_952970716}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_86695173}[将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[从]{style="font-family:宋体"}[Recovery]{lang="EN-US"}[状态恢复到正常状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1480851510}

[\[Sysname\] mad restore]{lang="EN-US"}

[   This command will restore the device from multi-active conflict state. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Restoring from multi-active conflict state, please wait\...]{lang="EN-US"}
:::::

::: {#-1610967583 .myid}
[]{#_Toc404783333}[]{#struct_0_x2076_17954_1737812740}[]{#_Toc381194249}[]{#_Toc262638009}[]{#_Toc216513775}

**IRF \-- IRF2配置命令（分布式设备） \-- port group interface**

------------------------------------------------------------------------

[**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x903676596}[命令用来绑定设备的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **port group interface**]{lang="EN-US"}]{#struct_0_x2076_17954_380230369}[命令用来取消设备的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1404675701}

[**[port group ]{lang="EN-US"}**[\[ **mdc** *mdc-name* \] **interface** *interface-type* *interface-number* \[ **mode** { **enhanced** \| **extended** \| **normal** } \]]{lang="EN-US"}]{#struct_0_x2076_17954_1481048118}

[**[undo port group ]{lang="EN-US"}**[\[ **mdc** *mdc-name* \] **interface** *interface-name*]{lang="EN-US"}]{#struct_0_x2076_17954_x179449191}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_749791507}

[[设备上没有创建]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x84632096}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_996806899}

[[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x489698173}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1194696789}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1480982582}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_2110754077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1435841802}

[**[mdc]{lang="EN-US"}**[ *mdc-name*]{lang="EN-US"}]{#struct_0_x2076_17954_358712626}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x2076_17954_x412461056}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x2076_17954_x1983357435}[：接口的名称，格式为]{style="font-family:宋体"}*[interface-typeinterface-number]{lang="EN-US"}[，]{style="font-family:
宋体"}[interface-type]{lang="EN-US"}*[与]{style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[之间没有空格。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**]{#struct_0_x2076_17954_1481179190}[：设置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的工作模式。该参数以及各模式的支持情况与设备]{style="font-family:宋体"}[/]{lang="EN-US"}[接口板的型号有关，请以实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enhanced]{lang="EN-US"}**]{#struct_0_x2076_17954_x1751365873}[：将接口的工作模式设置为增强模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ex]{lang="EN-US"}**]{#struct_0_x2076_17954_1487518605}**[tended]{lang="EN-US"}**[：将接口的工作模式设置为]{lang="EN-US" style="font-family:宋体"}[扩展]{style="font-family:
宋体"}[模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[normal]{lang="EN-US"}**]{#struct_0_x2076_17954_x22883439}[：将接口的工作模式设置为普通模式。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_64958327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当需要绑定的]{style="font-family:宋体"}]{#struct_0_x2076_17954_1866686173}[IRF]{lang="EN-US"}[物理端口属于非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[时，必须指定]{style="font-family:宋体"}**[mdc]{lang="EN-US"}**[参数，否则，系统将提示该接口不存在；当需要绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口属于缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[时，可以不指定]{style="font-family:宋体"}**[mdc]{lang="EN-US"}**[参数。关于]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的详细介绍请参见"基础配置指导"中的"]{style="font-family:宋体"}[MDC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行该命令可以将同一]{style="font-family:宋体"}]{#struct_0_x2076_17954_1455558437}[IRF]{lang="EN-US"}[端口与多个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口绑定，最多可绑定的物理端口数与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的工作模式只在接口作为]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1939551931}[IRF]{lang="EN-US"}[物理端口时生效，作为普通端口使用时不生效。]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中直接相连的两个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的模式必须相同，否则，报文无法互通。]{style="font-family:宋体"}[当用于]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Virtual Private LAN Service]{lang="EN-US"}[，虚拟专用局域网服务）组网时，请设置为]{lang="EN-US" style="font-family:宋体"}**[enhanced]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1481113654}[模式下，需要先使用]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令关闭相应的物理端口，才能执行]{lang="EN-US" style="font-family:宋体"}**[port group interface]{lang="EN-US"}**[命令将]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口与该物理端口绑定。再使用]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启该物理端口，该物理端口才能用作]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口建立]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[连接**；**如果在独立运行模式下进行配置，则可以直接执行]{lang="EN-US" style="font-family:宋体"}**[port group interface]{lang="EN-US"}**[命令，不需要先使用]{lang="EN-US" style="font-family:
宋体"}**[shutdown]{lang="EN-US"}**[命令关闭相应的物理端口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x605683011}[模式下，需要先使用]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令关闭相应的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，才能执行]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令取消]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口与该]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口的绑定关系。再使用]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启该]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，该物理端口才能用于报文的转发；如果在独立运行模式下进行配置，则可以直接执行]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令，不需要先使用]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令关闭相应的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，即便热插拔接口板导致绑定的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1888320777}[物理端口不存在了，但绑定关系仍然存在，使用]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令可以取消绑定关系。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些接口板出厂时已将接口分组，同一组内的接口只能都作为]{style="font-family:宋体"}]{#struct_0_x2076_17954_798324628}[IRF]{lang="EN-US"}[物理端口，或者都不作为]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口。当将某组中的一个接口和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定时，系统要求先将该组中的所有接口都关闭，否则，绑定失败；当绑定后，将其中一个接口激活时，系统会判断该组中的其它接口是否已经和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定（可以绑定到同一]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口，也可以绑定到不同]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口），如果没有绑定，则不允许激活。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x173783320}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_744126271}[在处于独立运行模式的设备上将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口]{style="font-family:宋体"}[Ten-GigabitEthernet1/0/1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1481310262}

[\[Sysname\] irf-port 1]{lang="EN-US"}

[\[Sysname-irf-port1\] port group interface ten-gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1407223917}[将]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员设备（编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口]{style="font-family:宋体"}[Ten-GigabitEthernet1/1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[端口]{style="font-family:宋体"}[1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_958692344}

[\[Sysname\] interface ten-gigabitethernet 1/1/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/1\] shutdown]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] irf-port 1/1]{lang="EN-US"}

[\[Sysname-irf-port 1/1\] port group interface ten-gigabitethernet 1/1/0/1]{lang="EN-US"}

[\[Sysname-irf-port 1/1\] quit]{lang="EN-US"}

[\[Sysname\] interface ten-gigabitethernet 1/1/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/1/0/1\] undo shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_353837515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[irf-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x1325808341}
:::

::: {#1570950239 .myid}
[]{#_Toc404783335}[]{#struct_0_x2076_17954_2120698398}[]{#_Toc381194294}

**IRF \-- IRF3配置命令 \-- associate**

------------------------------------------------------------------------

[**[associate]{lang="EN-US"}**]{#struct_0_x2076_17954_1251855474}[命令用来给]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备分配虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号。]{style="font-family:宋体"}

[**[undo associate]{lang="EN-US"}**]{#struct_0_x2076_17954_x699998969}[命令用来取消指定]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x408256081}

[**[associate ]{lang="EN-US"}**]{#struct_0_x2076_17954_1739971054}[*[associated-id]{lang="EN-US" style="font-size:9.0pt"}*]{.TableTextChar}

[**[undo associate]{lang="EN-US"}**]{#struct_0_x2076_17954_x722755749}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1148101549}

[[没有给任何]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_88979542}[设备分配虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2134041556}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1480785967}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1026900450}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x157638951}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1116247974}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_586381827}

[[*[associated-id]{lang="EN-US" style="font-size:9.0pt"}*]{.TableTextChar}]{#struct_0_x2076_17954_x578446203}[：表示给]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备分配的虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号。该参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x362627552}

[[当父设备为分布式设备组成的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_2014663110}[时，使用该命令配置的为虚拟框号；当父设备为集中式设备组成的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[时，使用该命令配置的为虚拟槽位号。关于虚拟框号和虚拟槽位号的详细介绍请参见"虚拟化技术配置指导"中的"]{style="font-family:宋体"}[IRF3]{lang="EN-US"}["。]{style="font-family:宋体"}

[[在为]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x271934698}[设备分配虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[虚拟框号]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2076_17954_x1797139111}[虚拟槽位号可配置的值还与]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的]{lang="EN-US" style="font-family:宋体"}[型号]{style="font-family:宋体"}[有关，]{lang="EN-US" style="font-family:宋体"}[如果配置的值大于]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备允许配置的最大值，则会配置失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个虚拟框号]{style="font-family:宋体"}]{#struct_0_x2076_17954_1480720431}[/]{lang="EN-US"}[虚拟槽位号只能分配给一个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_954234644}[端口视图]{lang="EN-US" style="font-family:宋体"}[下多次执行该命令，新配置会覆盖旧配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1290164638}[PEX]{lang="EN-US"}[设备已经正常启动，修改或删除该]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号会导致该]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备自动重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2076_17954_x835239611}[PEX]{lang="EN-US"}[设备启动过程中，不允许修改虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1067651629}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1765656611}[为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[相连的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备分配虚拟框号]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1480917039}

[\[Sysname\] pex-port 2]{lang="EN-US"}

[\[Sysname-pex-port2\] associate 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1317524507}[为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口]{style="font-family:宋体"}[2]{lang="EN-US"}[相连的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备分配虚拟槽位号]{style="font-family:宋体"}[101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1210963694}

[\[Sysname\] pex-port 2]{lang="EN-US"}

[\[Sysname-pex-port2\] associate 101]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404783336}[]{#struct_0_x2076_17954_x132536778}[]{#_Toc381194295}

**IRF \-- IRF3配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x2076_17954_1325136193}[命令用来为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口配置描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2076_17954_922176132}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1480851503}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x2076_17954_1738009349}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2076_17954_823870811}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_131650424}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x380840214}[端口的描述信息为"]{style="font-family:宋体"}[pex-port *pex-number*]{lang="EN-US"}["，比如]{style="font-family:宋体"}[pex-port 0002]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1282295149}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1481048111}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x178990439}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_315294435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_635455745}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x777398651}

[*[text]{lang="EN-US"}*]{#struct_0_x2076_17954_x631480992}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[79]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1235477147}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x288246078}[配置编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的描述信息为"]{style="font-family:宋体"}[connettodep2]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1480982575}

[\[Sysname\] pex-port 2]{lang="EN-US"}

[\[Sysname-pex-port2\] description connettodep2]{lang="EN-US"}
:::

::: {#-2043961043 .myid}
[]{#_Toc404783337}[]{#struct_0_x2076_17954_2110557464}

**IRF \-- IRF3配置命令 \-- display pex working-mode (Centralized IRF devices)**

------------------------------------------------------------------------

[**[display pex working-mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1797296796}[命令用来显示设备的工作模式。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2115789931}

[**[display pex working-mode ]{lang="EN-US"}**[{ **all** \| **slot** *slot-number1* \[ **to** *slot-number2* \] }]{lang="EN-US"}]{#struct_0_x2076_17954_x1626973301}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_425790156}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_98081320}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x694146080}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_296554191}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x931808248}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1481179183}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_17954_x1751431410}[：表示所有的设备。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number1*]{lang="EN-US"}]{#struct_0_x2076_17954_x616335841}[：表示成员设备的编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number1* **to** *slot-number2*]{lang="EN-US"}]{#struct_0_x2076_17954_x796643288}[：表示多个成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[表示起始编号，]{style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[表示结束编号，]{style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[的值应大于等于]{style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x39401315}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1937426283}[显示设备的工作模式。]{style="font-family:宋体"}

[[\<Sysname\> display pex working-mode all]{lang="EN-US"}]{#struct_0_x2076_17954_808594281}

[[Parent device mode Configuration:]{lang="EN-US"}]{#struct_0_x2076_17954_624404715}

[[  Auto mode:]{lang="EN-US"}]{#struct_0_x2076_17954_850059079}

[[    Slots 1 to 3]{lang="EN-US"}]{#struct_0_x2076_17954_128335142}

[[  Switch mode:]{lang="EN-US"}]{#struct_0_x2076_17954_1481113647}

[[    None]{lang="EN-US"}]{#struct_0_x2076_17954_x605486404}

[[  PEX mode at startup:]{lang="EN-US"}]{#struct_0_x2076_17954_x2045453673}

[[    None]{lang="EN-US"}]{#struct_0_x2076_17954_x280135550}

[ ]{lang="EN-US"}

[[PEX device mode Configuration:]{lang="EN-US"}]{#struct_0_x2076_17954_x93156501}

[[  Switch mode at startup:]{lang="EN-US"}]{#struct_0_x2076_17954_785161070}

[[    None]{lang="EN-US"}]{#struct_0_x2076_17954_x1242363291}

[[  PEX mode at startup:]{lang="EN-US"}]{#struct_0_x2076_17954_1365518356}

[[    Slots 100 to 103]{lang="EN-US"}]{#struct_0_x2076_17954_1550298702}

[[表1-13 ]{lang="EN-US"}[[display pex working-mode]{lang="EN-US"}]{.FigureDescriptionChar}]{#struct_0_x2076_17954_1225050666}[[命令显示]{style="font-family:黑体"}]{.FigureDescriptionChar}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1389483931}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_1481310255}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_1481244719}

[[Parent device mode Configuration]{lang="EN-US"}]{#struct_0_x2076_17954_1480785968}

[[给非]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1480720432}[设备配置的工作模式]{style="font-family:宋体"}

[[Auto mode]{lang="EN-US"}]{#struct_0_x2076_17954_954431252}

[[表示配置的为]{style="font-family:宋体"}[auto]{lang="EN-US"}]{#struct_0_x2076_17954_1480917040}[模式]{style="font-family:宋体"}

[[Switch mode]{lang="EN-US"}]{#struct_0_x2076_17954_1480851504}

[[表示配置的为]{style="font-family:宋体"}[switch]{lang="EN-US"}]{#struct_0_x2076_17954_1481048112}[模式]{style="font-family:宋体"}

[[PEX mode at startup]{lang="EN-US"}]{#struct_0_x2076_17954_1480982576}

[[表示配置的为]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1481179184}[模式。非]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备切换到]{style="font-family:宋体"}[PEX]{lang="EN-US"}[模式需要手工重启后才能生效]{style="font-family:宋体"}

[[PEX device mode Configuration]{lang="EN-US"}]{#struct_0_x2076_17954_x1751103730}

[[给]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1481113648}[设备配置的工作模式]{style="font-family:宋体"}

[[Switch mode at startup]{lang="EN-US"}]{#struct_0_x2076_17954_1481310256}

[[表示配置的为]{style="font-family:宋体"}[switch]{lang="EN-US"}]{#struct_0_x2076_17954_1481244720}[模式。]{style="font-family:宋体"}[PEX]{lang="EN-US"}[切换到]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式需要手工重启后才能生效]{style="font-family:宋体"}

[[PEX mode at startup]{lang="EN-US"}]{#struct_0_x2076_17954_1077501444}

[[表示配置的为]{style="font-family:宋体"}[pex]{lang="EN-US"}]{#struct_0_x2076_17954_1077435908}[模式]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-847485758 .myid}
[]{#_Toc404783338}[]{#struct_0_x2076_17954_279417428}[]{#_Toc387672205}

**IRF \-- IRF3配置命令 \-- display pex working-mode (Distributed devices--In IRF mode)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_840310334}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x937178885}
:::

[ ]{lang="EN-US"}

[**[display pex working-mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x60717344}[命令用来显示]{style="font-family:
宋体"}[PEX]{lang="EN-US"}[设备的工作模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1427078207}

[**[display pex working-mode ]{lang="EN-US"}**[{ **all** \| **chassis** *chassis-number* **slot** *slot-number1* \[ **to** *slot-number2* \] }]{lang="EN-US"}]{#struct_0_x2076_17954_450484408}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1825955810}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x141110039}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1077632516}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x447865350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x2121616388}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x669816249}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_17954_x60891803}[：表示所有的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number1* \[ **to** *slot-number2* \]]{lang="EN-US"}]{#struct_0_x2076_17954_782997151}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备所在位置。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1470992351}[：表示]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的虚拟框号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slot]{lang="EN-US"}**[ *slot-number1*]{lang="EN-US"}]{#struct_0_x2076_17954_x1569055461}[：表示]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的槽位号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[to ]{lang="EN-US"}***[slot-number2]{lang="EN-US"}*]{#struct_0_x2076_17954_x1258902262}[：表示多个]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{lang="EN-US" style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[表示起始]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的槽位号，]{lang="EN-US" style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[表示结束]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的槽位号，]{lang="EN-US" style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[的值应大于等于]{lang="EN-US" style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[的值。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1206056032}

[[设备工作在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1077566980}[模式才支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x129961970}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1231849901}[显示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式。]{style="font-family:宋体"}

[[\<Sysname\> display pex working-mode all]{lang="EN-US"}]{#struct_0_x2076_17954_x1735059400}

[[PEX device mode Configuration:]{lang="EN-US"}]{#struct_0_x2076_17954_1500320230}

[[  Switch mode at startup:]{lang="EN-US"}]{#struct_0_x2076_17954_x1418714103}

[[    None]{lang="EN-US"}]{#struct_0_x2076_17954_x1227458910}

[[  PEX mode at startup:]{lang="EN-US"}]{#struct_0_x2076_17954_x820069308}

[[    Chassis 101 slots 0]{lang="EN-US"}]{#struct_0_x2076_17954_402725351}

[[表1-14 ]{lang="EN-US"}[[display pex working-mode]{lang="EN-US"}]{.FigureDescriptionChar}]{#struct_0_x2076_17954_1538292977}[[命令显示]{style="font-family:黑体"}]{.FigureDescriptionChar}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1373660165}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_1077763588}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_1077698052}

[[PEX device mode Configuration]{lang="EN-US"}]{#struct_0_x2076_17954_1077894660}

[[给]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077829124}[设备配置的工作模式]{style="font-family:宋体"}

[[Switch mode at startup]{lang="EN-US"}]{#struct_0_x2076_17954_1078025732}

[[表示配置的为]{style="font-family:宋体"}[switch]{lang="EN-US"}]{#struct_0_x2076_17954_2097124057}[模式。]{style="font-family:宋体"}[PEX]{lang="EN-US"}[切换到]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式需要手工重启后才能生效]{style="font-family:宋体"}

[[PEX mode at startup]{lang="EN-US"}]{#struct_0_x2076_17954_1077960196}

[[表示配置的为]{style="font-family:宋体"}[pex]{lang="EN-US"}]{#struct_0_x2076_17954_1077501445}[模式]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1021075225 .myid}
[]{#_Toc404783339}[]{#struct_0_x2076_17954_x1994473531}[]{#_Toc381194296}

**IRF \-- IRF3配置命令 \-- display pex-port**

------------------------------------------------------------------------

[**[display pex-port]{lang="EN-US"}**]{#struct_0_x2076_17954_1077435909}[命令用来显示已创建的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_279482964}

[**[display pex-port]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *pex-port-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x2076_17954_500052300}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1013161648}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_x548695953}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x249121853}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_899974499}

[[network-operator]{lang="EN-US"}]{#struct_0_x2076_17954_1077632517}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x447799814}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2076_17954_492186341}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x927237305}

[*[pex-port-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x103117797}[：显示指定编号的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的相关信息。不指定该参数时，显示所有已创建的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的相关信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2076_17954_x2069082455}[：显示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的详细信息。不指定该参数时，显示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1077566981}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x130027506}[显示所有]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的简要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pex-port]{lang="EN-US"}]{#struct_0_x2076_17954_1077763589}

[PEX port 2:]{lang="EN-US"}

[  Status: Online]{lang="EN-US"}

[  Associated ID: Slot 100]{lang="EN-US"}

[  Description: pex-port 0002]{lang="EN-US"}

[ ]{lang="EN-US"}

[PEX port 3:]{lang="EN-US"}

[  Status: Offline]{lang="EN-US"}

[  Associated ID: Slot 101]{lang="EN-US"}

[  Description: pex-port 0003]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1111927097}[显示所有]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display pex-port verbose]{lang="EN-US"}]{#struct_0_x2076_17954_1077698053}

[PEX port 2:]{lang="EN-US"}

[   Status: Online]{lang="EN-US"}

[   Associated ID: Slot 100]{lang="EN-US"}

[   Description: pex-port 0002]{lang="EN-US"}

[   Member port count: 3]{lang="EN-US"}

[   Member port        Status          Peer port]{lang="EN-US"}

[   XGE1/0/2           Down            \--]{lang="EN-US"}

[   XGE1/0/3           Down            \--]{lang="EN-US"}

[   XGE1/0/4           Blocked         \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1123520488}[显示所有]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的简要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pex-port]{lang="EN-US"}]{#struct_0_x2076_17954_782709573}

[PEX port 2:]{lang="EN-US"}

[  Status: Online]{lang="EN-US"}

[  Associated ID: Chassis 100]{lang="EN-US"}

[  Description: pex-port 0002]{lang="EN-US"}

[ ]{lang="EN-US"}

[PEX port 3:]{lang="EN-US"}

[  Status: Offline]{lang="EN-US"}

[  Associated ID: Chassis 101]{lang="EN-US"}

[  Description: pex-port 0003]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x1804747642}[显示所有]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display pex-port verbose]{lang="EN-US"}]{#struct_0_x2076_17954_1077894661}

[PEX port 2:]{lang="EN-US"}

[   Status: Online]{lang="EN-US"}

[   Associated ID: Chassis 100]{lang="EN-US"}

[   Description: pex-port 0002]{lang="EN-US"}

[   Member port count: 3]{lang="EN-US"}

[   Member port        Status          Peer port]{lang="EN-US"}

[   XGE1/1/0/2          Down            \--]{lang="EN-US"}

[   XGE1/1/0/3          Down            \--]{lang="EN-US"}

[   XGE1/1/0/4          Blocked         \--]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display pex-port verbose]{lang="EN-US"}]{#struct_0_x2076_17954_x1636759951}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1350072891}[[字段]{style="font-family:黑体"}]{#struct_0_x2076_17954_1077829125}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2076_17954_1078025733}

[[PEX port 2]{lang="EN-US"}]{#struct_0_x2076_17954_1077960197}

[[编号为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x2076_17954_1077501446}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的相关信息]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2076_17954_1077632518}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077566982}[设备的状态信息，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_x2076_17954_1077763590}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备在线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_x2076_17954_1077698054}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备不在线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loading]{lang="EN-US"}]{#struct_0_x2076_17954_1077894662}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备正在启动]{style="font-family:宋体"}

[[Associated ID]{lang="EN-US"}]{#struct_0_x2076_17954_1077829126}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077960198}[端口绑定的虚拟槽位号。当显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}[时，表示该]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口没有配置虚拟槽位号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077501447}[端口对应的虚拟框号。当显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}[时，表示该]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口没有配置虚拟框号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2076_17954_1077435911}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077632519}[端口的描述信息]{style="font-family:宋体"}

[[Member port]{lang="EN-US"}]{#struct_0_x2076_17954_1077566983}

[[父设备上的]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077763591}[物理接口]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2076_17954_1077894663}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077829127}[端口内的成员端口状态，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forwarding]{lang="EN-US"}]{#struct_0_x2076_17954_1078025735}[：表示物理链路可转发业务报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x2076_17954_1077960199}[：表示物理链路是断开的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blocked]{lang="EN-US"}]{#struct_0_x2076_17954_1077501440}[：表示物理链路停止转发业务报文]{style="font-family:宋体"}

[[Peer port]{lang="EN-US"}]{#struct_0_x2076_17954_1077435904}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077566976}[设备上的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口的名称，当没有获取到该接口的名称时，该字段显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[No member ports.]{lang="EN-US"}]{#struct_0_x2076_17954_1077763584}

[[表示该]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077698048}[端口没有绑定]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1357334169 .myid}
[]{#_Toc404783340}[]{#struct_0_x2076_17954_1123848169}

**IRF \-- IRF3配置命令 \-- pex working-mode (Centralized IRF devices)**

------------------------------------------------------------------------

[**[pex working-mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1976248394}[命令用来配置设备的工作模式。]{style="font-family:宋体"}

[**[undo pex working-mode]{lang="EN-US"}**]{#struct_0_x2076_17954_910358952}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1787255520}

[**[pex working-mode]{lang="EN-US"}**[ { **auto** \| **pex** \| **switch** } { **all** \| **slot** *slot-number1* \[ **to** *slot-number2* \] }]{lang="EN-US"}]{#struct_0_x2076_17954_1077894656}

[**[undo pex working-mode]{lang="EN-US"}**[ { **all** \| **slot** *slot-number1* \[ **to** *slot-number2* \] }]{lang="EN-US"}]{#struct_0_x2076_17954_x1636956562}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x621252745}

[[非]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x2023233049}[设备的缺省方式是]{style="font-family:宋体"}[auto]{lang="EN-US"}[模式，即支持自动切换为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备；]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式是]{style="font-family:宋体"}[PEX]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1316935274}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_1177444818}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_840959726}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1315281661}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_126456014}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1331581733}

[**[auto]{lang="EN-US"}**]{#struct_0_x2076_17954_x264331300}[：表示允许设备根据组网环境自动切换到]{style="font-family:宋体"}[PEX]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[pex]{lang="EN-US"}**]{#struct_0_x2076_17954_1077829120}[：表示将设备的工作模式强制设置为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[switch]{lang="EN-US"}**]{#struct_0_x2076_17954_365763214}[：表示将设备的工作模式强制设置为]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_17954_x2145111138}[：当和]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[关键字配合使用时，]{style="font-family:宋体"}**[all]{lang="EN-US"}**[表示所有非]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备；当和]{style="font-family:宋体"}**[pex]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[switch]{lang="EN-US"}**[关键字配合使用时，]{style="font-family:宋体"}**[all]{lang="EN-US"}**[表示所有成员设备以及]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number1*]{lang="EN-US"}]{#struct_0_x2076_17954_x822973779}[：当和]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[关键字配合使用时，]{style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[表示成员设备的编号；当和]{style="font-family:宋体"}**[pex]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[switch]{lang="EN-US"}**[关键字配合使用时，]{style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[表示成员设备的编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number1* **to** *slot-number2*]{lang="EN-US"}]{#struct_0_x2076_17954_1483497353}[：表示同时修改多个成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式。]{style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[表示起始成员设备的编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号，]{style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[表示结束成员设备的编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号，]{style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[的值应大于等于]{style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x368323398}

[[该命令只对当前存在的设备生效。如果指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**]{#struct_0_x2076_17954_1205698237}[上并没有接入设备，命令也可以配置成功，但是不生效。当该]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[上重新接入时，请重新配置该命令。]{style="font-family:宋体"}

[[关于各模式的详细描述请参见"虚拟化技术配置指导"中的"]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_1350813821}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1291139526}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_642634922}[所有设备当前处于]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式，将所有设备的工作模式设置为]{style="font-family:宋体"}[auto]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1078025728}

[\[Sysname\] pex working-mode auto all]{lang="EN-US"}

[[Are you sure you want to enable auto mode? In auto mode, the device will automatically reboot to enable PEX mode when the connection to the parent device goes up, but PEX device doesn\'t suppport this command. \[Y/N\]: y]{lang="EN-US"}]{#struct_0_x2076_17954_2096468698}
:::

::::: {#-726405309 .myid}
[]{#_Toc404783341}[]{#struct_0_x2076_17954_599435217}[]{#_Toc387672204}

**IRF \-- IRF3配置命令 \-- pex working-mode (Distributed devices--In IRF mode)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2076_17954_1007181469}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2076_17954_x1305700248}
:::

**[ ]{lang="EN-US"}**

[**[pex working-mode]{lang="EN-US"}**]{#struct_0_x2076_17954_x1393880853}[命令用来配置]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式。]{style="font-family:宋体"}

[**[undo pex working-mode]{lang="EN-US"}**]{#struct_0_x2076_17954_803212628}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x43956843}

[**[pex working-mode]{lang="EN-US"}**[ **switch** { **all** \| **chassis** *chassis-number* **slot** *slot-number1* \[ **to** *slot-number2* \] }]{lang="EN-US"}]{#struct_0_x2076_17954_1968867147}

[**[undo pex working-mode ]{lang="EN-US"}**[{ **all** \| **chassis** *chassis-number* **slot** *slot-number1* \[ **to** *slot-number2* \] }]{lang="EN-US"}]{#struct_0_x2076_17954_256803589}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1801621080}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077960192}[设备的工作模式是]{style="font-family:宋体"}[PEX]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x852610071}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_963506892}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2134386820}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1278286066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1315428354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_120891764}

[**[switch]{lang="EN-US"}**]{#struct_0_x2076_17954_x838041448}[：表示将]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式强制设置为]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2076_17954_x1127584496}[：表示将所有相连的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式强制设置为]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number1* \[ **to** *slot-number2* \]]{lang="EN-US"}]{#struct_0_x2076_17954_145173379}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备所在位置。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1077501441}[：表示]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的虚拟框号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slot]{lang="EN-US"}**[ *slot-number1*]{lang="EN-US"}]{#struct_0_x2076_17954_x1994735675}[：表示]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的槽位号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[to ]{lang="EN-US"}***[slot-number2]{lang="EN-US"}*]{#struct_0_x2076_17954_x701807364}[：表示多个]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备。]{lang="EN-US" style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[表示起始]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的槽位号，]{lang="EN-US" style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[表示结束]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[设备对应的槽位号，]{lang="EN-US" style="font-family:宋体"}*[slot-number2]{lang="EN-US"}*[的值应大于等于]{lang="EN-US" style="font-family:宋体"}*[slot-number1]{lang="EN-US"}*[的值。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1535659956}

[[设备工作在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2076_17954_x642497262}[模式才支持该命令。]{style="font-family:宋体"}

[[如果某]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x1665086900}[要退出]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[网络，作为一台交换机独立运行，请使用该命令，将]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的工作模式配置为]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式。配置]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式后，需要手动重启该]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备，配置才会生效。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1233911650}[设备切换到]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式，第一次重启成功后，设备会工作在]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式。此时，请保存当前配置，否则，设备再一次重启时会遵循启动配置文件中的模式。]{style="font-family:宋体"}

[[该命令只对当前存在的设备生效。如果指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**]{#struct_0_x2076_17954_x963338402}[上并没有接入设备，命令也可以配置成功，但是不生效。当该]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[上重新接入时，请重新配置该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_359693323}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_110489935}[将]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备（所在位置为]{style="font-family:宋体"}[chassis 100 slot 0]{lang="EN-US"}[）的工作模式设置为]{style="font-family:宋体"}[switch]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_504183896}

[\[Sysname\] pex working-mode switch chassis 100 slot 0]{lang="EN-US"}

[[Are you sure you want to force a change to switch mode? In forced switch mode, the device can\'t change to PEX mode automatically. \[Y/N\]: y ]{lang="EN-US"}]{#struct_0_x2076_17954_1077435905}

[[If you want to change parent device to PEX mode or change PEX device to switch mode, you must reboot the device.]{lang="EN-US"}]{#struct_0_x2076_17954_280269396}
:::::

::: {#-218683287 .myid}
[]{#_Toc404783342}[]{#struct_0_x2076_17954_x1679187182}[]{#_Toc381194297}

**IRF \-- IRF3配置命令 \-- port group interface**

------------------------------------------------------------------------

[**[port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x62133996}[用来将]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口和父设备上的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口绑定。]{style="font-family:宋体"}

[**[undo port group interface]{lang="EN-US"}**]{#struct_0_x2076_17954_x1251534205}[用来取消指定绑定。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x605307423}

[**[port group interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2076_17954_707350255}

[**[undo port group interface ]{lang="EN-US"}***[interface-name]{lang="EN-US"}*]{#struct_0_x2076_17954_548996121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1568810493}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_1077632513}[端口没有和任何]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口绑定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x448061958}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x1983412992}[端口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_80928761}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1910754569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_215790331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x749422219}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2076_17954_1077566977}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口的类型和编号。各设备型号上可用作]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口的接口请参见产品相关手册。]{style="font-family:宋体"}

[[interface-name]{lang="EN-US"}]{#struct_0_x2076_17954_x130158591}[：物理端口的名称，格式为]{style="font-family:宋体"}*[interface-typeinterface-number]{lang="EN-US"}*[。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[表示接口名称，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示接口编号，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[和]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[中间不允许有空格。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x2113435935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x2076_17954_x894495882}[PEX]{lang="EN-US"}[端口用来管理一个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备，和同一个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口绑定的多个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口只能连接到同一个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备，这些物理端口之间互为备份，自动实现流量的负载分担。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x1860074498}[物理端口和]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口绑定后，该物理端口下绑定前的所有配置将恢复到缺省情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行该命令可以将多个]{style="font-family:宋体"}]{#struct_0_x2076_17954_1077763585}[PEX]{lang="EN-US"}[物理端口绑定到一个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口中，最多可绑定的物理端口数与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x2076_17954_1111140665}[PEX]{lang="EN-US"}[物理端口只能和一个]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x2076_17954_941557000}[PEX]{lang="EN-US"}[设备已经正常启动，关闭（执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令）]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口中最后一个处于]{style="font-family:宋体"}[Forwarding]{lang="EN-US"}[状态的物理端口，会导致对应的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些接口板出厂时已将物理端口分组（包括]{style="font-family:宋体"}]{#struct_0_x2076_17954_1077698049}[40GE]{lang="EN-US"}[和]{style="font-family:宋体"}[100GE]{lang="EN-US"}[接口拆分出来的]{style="font-family:宋体"}[10GE]{lang="EN-US"}[接口）：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[同一组内的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_1123913705}[物理端口]{style="font-family:宋体"}[可以只有一个或者几个作为]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口]{lang="EN-US" style="font-family:宋体"}[，但]{style="font-family:宋体"}[建议绑定到一个]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口或者提前进行]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的规划。]{lang="EN-US" style="font-family:宋体"}[否则，绑定的时候，可能会导致该组物理接口已连接的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备重启。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果同一组内的某个]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_1943441546}[物理]{style="font-family:宋体"}[端口已经和]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[端口绑定，则其它]{lang="EN-US" style="font-family:宋体"}[物理端口]{style="font-family:宋体"}[不能和]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口绑定，反之，亦然。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当将某组中的一个]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2076_17954_1077894657}[物理端口]{style="font-family:宋体"}[和]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口]{style="font-family:宋体"}[绑定时，系统要求先将该组中的所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都关闭]{lang="EN-US" style="font-family:宋体"}[（执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令）]{style="font-family:宋体"}[，才能执行]{lang="EN-US" style="font-family:宋体"}**[port group interface]{lang="EN-US"}**[命令将]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口与该物理端口绑定。再使用]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启该物理端口，该物理端口才能用作]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口建立连接。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[取消]{style="font-family:宋体"}]{#struct_0_x2076_17954_x1636891026}[某组中]{lang="EN-US" style="font-family:宋体"}[物理端口]{style="font-family:宋体"}[和]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的]{style="font-family:宋体"}[绑定时，需要先使用]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令关闭]{lang="EN-US" style="font-family:宋体"}[该组的所有]{style="font-family:宋体"}[物理端口，才能执行]{lang="EN-US" style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令取消]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[端口与该]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[物理端口的绑定关系。再使用]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[该组的]{style="font-family:宋体"}[物理端口，]{lang="EN-US" style="font-family:宋体"}[这些]{style="font-family:宋体"}[物理端口才能用于报文的转发。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_579522724}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_1077829121}[将物理端口]{style="font-family:宋体"}[Ten-GigabitEther1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[PEX 3]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_365697678}

[\[Sysname\] pex-port 3]{lang="EN-US"}

[\[Sysname-pex-port3\] port group interface ten-gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_578248669}[将物理端口]{style="font-family:宋体"}[Ten-GigabitEther1/0/6]{lang="EN-US"}[和]{style="font-family:宋体"}[PEX 4]{lang="EN-US"}[绑定。（]{style="font-family:宋体"}[Ten-GigabitEther1/0/5]{lang="EN-US"}[～]{style="font-family:宋体"}[Ten-GigabitEther1/0/]{lang="EN-US"}[８四个接口是一组的）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1077960193}

[\[Sysname\] interface range name pex interface ten-gigabitethernet 1/0/5 to ten-gigabitethernet 1/0/8]{lang="EN-US"}

[\[Sysname-if-range-pex\] shutdown]{lang="EN-US"}

[\[Sysname-if-range-pex\] quit]{lang="EN-US"}

[\[Sysname\] pex-port 4]{lang="EN-US"}

[\[Sysname-pex-port4\] port group interface ten-gigabitethernet 1/0/6]{lang="EN-US"}

[\[Sysname-pex-port4\] quit]{lang="EN-US"}

[\[Sysname\] interface range name pex]{lang="EN-US"}

[\[Sysname-if-range-pex\] undo shutdown]{lang="EN-US"}

[\[Sysname-if-range-pex\] quit]{lang="EN-US"}
:::

::: {#1939562848 .myid}
[]{#_Toc404783343}[]{#struct_0_x2076_17954_x852675607}[]{#_Toc381194298}

**IRF \-- IRF3配置命令 \-- pex-port**

------------------------------------------------------------------------

[**[pex-port]{lang="EN-US"}**]{#struct_0_x2076_17954_x1651381911}[命令用来创建]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口并进入]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口视图。如果]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口已经创建，则直接进入]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口视图。]{style="font-family:宋体"}

[**[undo pex-port]{lang="EN-US"}**]{#struct_0_x2076_17954_458584969}[命令用来删除]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2076_17954_2063282368}

[**[pex-port ]{lang="EN-US"}***[pex-port-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1915604935}

[**[undo pex-port ]{lang="EN-US"}***[pex-port-id]{lang="EN-US"}*]{#struct_0_x2076_17954_x1651447447}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1422674194}

[[没有创建]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x829857479}[端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1642164930}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2076_17954_818197516}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2076_17954_994236719}

[[network-admin]{lang="EN-US"}]{#struct_0_x2076_17954_1021319939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2076_17954_x1651250839}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x885446071}

[*[pex-port-id]{lang="EN-US"}*]{#struct_0_x2076_17954_684994085}[：表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2076_17954_x1200347397}

[[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x1442381547}[端口用来配置和管理]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备，通过创建]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口、绑定成员端口、配置虚拟框号]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟槽位号，用户可将与本设备（作为父设备）相连的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备当成一块远程业务板来使用，从而提高了设备的可扩展性。]{style="font-family:宋体"}

[[创建]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_x2076_17954_x1651316375}[端口时，如果已创建的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口数目已经达到系统最大值，则不允许创建新的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口；删除状态为]{style="font-family:宋体"}[Online]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口，会导致该端口对应的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备重启。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2076_17954_1907435136}

[[\# ]{lang="EN-US"}]{#struct_0_x2076_17954_x245077394}[创建编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2076_17954_1639762266}

[\[Sysname\] pex-port 2]{lang="EN-US"}

[\[Sysname-pex-port2\]]{lang="EN-US"}
:::
