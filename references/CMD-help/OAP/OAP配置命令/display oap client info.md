::::: {#1900914894 .myid}
[]{#_Toc404797519}[]{#struct_0_10411_62186_1653419529}[]{#_Toc325734364}

**OAP \-- OAP配置命令 \-- display oap client info**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OAP命令.files/image001.png){#图片 3 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10411_62186_1164334283}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_874391123}
:::

[ ]{lang="EN-US"}

[**[display oap client info]{lang="EN-US"}**]{#struct_0_10411_62186_1644942115}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[OAP client]{lang="SV"}[的信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_181950839}

[**[display oap client info]{lang="EN-US"}**[ \[ *client-id* \]]{lang="EN-US"}]{#struct_0_10411_62186_1842456931}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_1266780081}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10411_62186_x749186205}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_1643337000}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_x182077629}

[[network-operator]{lang="EN-US"}]{#struct_0_10411_62186_1270915545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_937791925}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10411_62186_1968585354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10411_62186_x1266902483}

[*[client-id]{lang="EN-US"}*]{#struct_0_10411_62186_1667334139}[：]{style="font-family:宋体;color:black"}[要显示的]{style="font-family:宋体"}[OAP client]{lang="SV"}[的]{style="font-family:宋体"}[Client ID]{lang="SV"}[，]{style="font-family:宋体"}[Client ID]{lang="SV"}[由]{style="font-family:宋体"}[OAP manager]{lang="SV"}[分配，取值范围为]{style="font-family:宋体"}[1]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="SV" style="color:black"}[。]{style="font-family:宋体;color:black"}[如果不指定参数则显示所有]{style="font-family:宋体"}[OAP client]{lang="SV"}[的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10411_62186_x244505001}

[[显示多个]{style="font-family:宋体"}]{#struct_0_10411_62186_x314068130}[OAP client]{lang="SV"}[信息的时候按照]{style="font-family:宋体"}[Client ID]{lang="SV"}[由小到大顺序排列。]{style="font-family:宋体"}[OAP client]{lang="SV"}[信息从]{style="font-family:宋体"}[OAP client]{lang="SV"}[发送的信息通告报文中获得]{style="font-family:宋体"}[，]{style="font-family:宋体"}[当]{style="font-family:宋体"}[OAP client]{lang="SV"}[字段]{style="font-family:宋体"}[信息不存在时该字段不显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_x654215534}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_x182012093}[显示]{style="font-family:宋体"}[Client ID]{lang="SV"}[为]{style="font-family:宋体"}[1]{lang="SV"}[的]{style="font-family:
宋体"}[OAP client]{lang="SV"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display oap client info 1]{lang="SV"}]{#struct_0_10411_62186_897669831}

[ Client ID: 1]{lang="SV"}

[ CPU: Intel(R) Pentium(R) M processor 1.40GHz]{lang="SV"}

[ ]{lang="SV"}[PCB Version: 3.00]{lang="EN-US"}

[ CPLD Version: 1.00]{lang="EN-US"}

[ Bootrom Version: 1.12]{lang="EN-US"}

[ Storage Card: 256 MB]{lang="EN-US"}

[ Memory: 512 MB]{lang="EN-US"}

[ Harddisk: 40.0 GB]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_x911365769}[显示所有]{style="font-family:宋体"}[OAP client]{lang="SV"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display oap client info]{lang="EN-US"}]{#struct_0_10411_62186_x181946557}

[ Client ID: 1]{lang="EN-US"}

[ CPU: Intel(R) Pentium(R) M processor 1.40GHz]{lang="EN-US"}

[ PCB Version: 3.00]{lang="EN-US"}

[ CPLD Version: 1.00]{lang="EN-US"}

[ Bootrom Version: 1.12]{lang="EN-US"}

[ Storage Card: 256 MB]{lang="EN-US"}

[ Memory: 512 MB]{lang="EN-US"}

[ Harddisk: 40.0 GB]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Client ID: 2 ]{lang="EN-US"}

[ CPU: Intel(R) Pentium(R) M processor 1.40GHz]{lang="EN-US"}

[ PCB Version: 3.00]{lang="EN-US"}

[ CPLD Version: 1.00]{lang="EN-US"}

[ Bootrom Version: 1.12]{lang="EN-US"}

[ Storage Card: 256 MB]{lang="EN-US"}

[ Memory: 512 MB]{lang="EN-US"}

[ Harddisk: 40.0 GB]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display oap client info]{lang="EN-US"}]{#struct_0_10411_62186_633482882}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_624209517}[[字段]{style="font-family:宋体"}]{#struct_0_10411_62186_x521364104}
:::::

[[描述]{style="font-family:宋体"}]{#struct_0_10411_62186_x895603030}

[[Client ID]{lang="EN-US"}]{#struct_0_10411_62186_1236060307}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_x441969381}[的]{style="font-family:宋体"}[Client ID]{lang="FR"}

[[Client Description]{lang="EN-US"}]{#struct_0_10411_62186_521481006}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_x181881021}[的描述字符串]{style="font-family:宋体"}

[[Hardware]{lang="EN-US"}]{#struct_0_10411_62186_999668235}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_1685425368}[的硬件版本]{style="font-family:宋体"}

[[System Software]{lang="EN-US"}]{#struct_0_10411_62186_1708178930}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_130009251}[的系统软件名称与版本]{style="font-family:宋体"}

[[Application Software]{lang="EN-US"}]{#struct_0_10411_62186_x509396301}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_x181815485}[的应用软件版本]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_10411_62186_x1723298691}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_232930631}[的]{style="font-family:宋体"}[CPU]{lang="FR"}[信息]{style="font-family:宋体"}

[[PCB Version]{lang="EN-US"}]{#struct_0_10411_62186_x2117124731}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_x880735243}[的]{style="font-family:宋体"}[PCB]{lang="FR"}[版本信息]{style="font-family:宋体"}

[[CPLD Version]{lang="EN-US"}]{#struct_0_10411_62186_x181749949}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_1079579852}[的]{style="font-family:宋体"}[CPLD]{lang="FR"}[版本信息]{style="font-family:宋体"}

[[Bootrom Version]{lang="EN-US"}]{#struct_0_10411_62186_526064366}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_1197711713}[的]{style="font-family:宋体"}[Boot ROM]{lang="FR"}[版本信息]{style="font-family:宋体"}

[[Storage Card]{lang="EN-US"}]{#struct_0_10411_62186_x1530534990}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_1318965884}[的存储卡的空间大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Memory]{lang="EN-US"}]{#struct_0_10411_62186_x181684413}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_x168421481}[的内存大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Harddisk]{lang="EN-US"}]{#struct_0_10411_62186_1767806439}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_x2013720984}[的硬盘大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_x1905434447}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display oap client summary]{lang="EN-US"}**]{#struct_0_10411_62186_x181618877}

::::: {#1284074075 .myid}
[]{#_Toc404797520}[]{#struct_0_10411_62186_691380309}[]{#_Toc325734365}

**OAP \-- OAP配置命令 \-- display oap client summary**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OAP命令.files/image001.png){#图片 4 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10411_62186_x1792570672}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_x1508870363}
:::

[ ]{lang="EN-US"}

[**[display oap client summary]{lang="EN-US"}**]{#struct_0_10411_62186_x1824369103}[命令用来]{style="font-family:
宋体"}[显示]{style="font-family:宋体"}[OAP client]{lang="SV"}[的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_x708260001}

[**[display oap client summary]{lang="EN-US"}**[ \[ *client-id* \]]{lang="EN-US"}]{#struct_0_10411_62186_198766783}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_711709950}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10411_62186_x182601917}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_1310177734}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_29784480}

[[network-operator]{lang="EN-US"}]{#struct_0_10411_62186_562855957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_517225656}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10411_62186_722984929}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10411_62186_375600332}

[*[client-id]{lang="SV"}*]{#struct_0_10411_62186_x814629189}[：要显示摘要信息的]{style="font-family:宋体"}[Client ID]{lang="SV"}[，]{style="font-family:宋体"}[Client ID]{lang="SV"}[由]{style="font-family:宋体"}[OAP]{lang="FR"}[ manager]{lang="SV"}[分配，取值范围为]{style="font-family:宋体"}[1]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="SV" style="color:black"}[。如果不指定参数则显示所有]{style="font-family:宋体"}[OAP client]{lang="SV"}[的摘要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10411_62186_1751647012}

[[显示多个]{style="font-family:宋体"}]{#struct_0_10411_62186_x1590954862}[OAP client]{lang="SV"}[摘要信息的时候按照]{style="font-family:宋体"}[Client ID]{lang="SV"}[由小到大顺序排列。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_x182536381}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_1653485065}[显示]{style="font-family:宋体"}[Client ID]{lang="SV"}[为]{style="font-family:宋体"}[1]{lang="SV"}[的]{style="font-family:
宋体"}[OAP client]{lang="SV"}[的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display oap client summary 1]{lang="EN-US"}]{#struct_0_10411_62186_34004355}

[ Client ID: 1]{lang="EN-US"}

[ Status: Registered]{lang="EN-US"}

[ MAC Address: 00e0-fc0a-c3ef]{lang="EN-US"}

[ Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Last registered: 02/08/2011 12:00:00]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_1376869110}[显示所有]{style="font-family:宋体"}[OAP client]{lang="SV"}[的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display oap client summary]{lang="EN-US"}]{#struct_0_10411_62186_1384006315}

[ Client ID: 1]{lang="EN-US"}

[ Status: Registered]{lang="EN-US"}

[ MAC Address: 00e0-fc0a-c3ef]{lang="EN-US"}

[ Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Last registered: 02/08/2011 12:00:00]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Client ID: 2]{lang="EN-US"}

[ Status: Registered]{lang="EN-US"}

[ MAC Address: 00e0-fa1e-03da]{lang="EN-US"}

[ Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[ Last registered: 02/08/2011 13:00:00]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display oap client summary]{lang="EN-US"}]{#struct_0_10411_62186_1016291495}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_654058925}[[字段]{style="font-family:宋体"}]{#struct_0_10411_62186_x421883709}
:::::

[[描述]{style="font-family:宋体"}]{#struct_0_10411_62186_817258413}

[[Client ID]{lang="EN-US"}]{#struct_0_10411_62186_318382264}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_2071495758}[的]{style="font-family:宋体"}[Client ID]{lang="FR"}

[[Status]{lang="EN-US"}]{#struct_0_10411_62186_1847428824}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_1384071851}[的状态，取值包括：]{style="font-family:宋体"}[Registered]{lang="EN-US"}[：已注册。]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_10411_62186_x905712624}

[[OAP client]{lang="FR"}]{#struct_0_10411_62186_1046284369}[的]{style="font-family:宋体"}[MAC]{lang="FR"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10411_62186_71791022}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_x1061679685}[的承载接口]{style="font-family:宋体"}

[[Last registered]{lang="EN-US"}]{#struct_0_10411_62186_1384137387}

[[OAP]{lang="FR"}[ client]{lang="EN-US"}]{#struct_0_10411_62186_x560999140}[的最近注册时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_x1492913817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display oap client info]{lang="EN-US"}**]{#struct_0_10411_62186_x582072351}

::::: {#1217011295 .myid}
[]{#_Toc404797521}[]{#struct_0_10411_62186_x948938036}[]{#_Toc325734366}[]{#_Toc311203775}[]{#_Toc155674816}[]{#_Toc98822460}[]{#_Toc296424451}[]{#_Toc257621822}[]{#_Toc205712796}[]{#_Toc155674926}

**OAP \-- OAP配置命令 \-- oap client close**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OAP命令.files/image001.png){#图片 5 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10411_62186_939701898}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_x918236827}
:::

[ ]{lang="EN-US"}

[**[oap client close]{lang="EN-US"}**]{#struct_0_10411_62186_849197871}[命令用来]{style="font-family:宋体"}[关闭指定的]{style="font-family:宋体"}[OAP client]{lang="SV"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_1384202923}

[**[oap client close]{lang="EN-US"}**[ *client-id*]{lang="EN-US"}]{#struct_0_10411_62186_1838517884}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_16823983}

[[系统]{style="font-family:宋体"}]{#struct_0_10411_62186_x69549344}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_1058785367}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_x1520116305}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_1342455885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10411_62186_1976558985}

[*[client-id]{lang="SV"}*]{#struct_0_10411_62186_1448775572}[：要关闭的]{style="font-family:宋体"}[OAP client]{lang="SV"}[的]{style="font-family:宋体"}[Client ID]{lang="SV"}[，取值范围为]{style="font-family:宋体"}[1]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="SV" style="color:black"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10411_62186_1384268459}

[[若指定的]{style="font-family:宋体"}]{#struct_0_10411_62186_x1690840353}[Client]{lang="SV"}[为]{style="font-family:宋体"}[Registered]{lang="EN-US"}[状态，]{style="font-family:宋体"}[OAP manager]{lang="SV"}[会发送一条关闭操作的通告报文给指定的]{style="font-family:宋体"}[OAP client]{lang="SV"}[，]{style="font-family:宋体"}[OAP client]{lang="SV"}[收到此报文后将执行关闭操作]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若指定的]{style="font-family:宋体"}[Client]{lang="SV"}[不存在，则会打印提示信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[OAP manager]{lang="EN-US"}]{#struct_0_10411_62186_659983341}[给]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[分配]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于保证各]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[的唯一性。]{style="font-family:宋体"}

[[需要注意的是]{style="font-family:宋体"}]{#struct_0_10411_62186_345562717}[，]{style="font-family:宋体"}[该命令仅对运行]{style="font-family:宋体"}[Linux]{lang="SV"}[系统的]{style="font-family:宋体"}[OAP client]{lang="SV"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_1254485145}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_x2146247294}[关闭]{style="font-family:宋体"}[Client ID]{lang="SV"}[为]{style="font-family:宋体"}[1]{lang="SV"}[的]{style="font-family:
宋体"}[OAP client]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_10411_62186_1623759302}

[\[Sysname\] oap client close 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_166415601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display oap client summary]{lang="EN-US"}**]{#struct_0_10411_62186_1384333995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oap client reboot]{lang="EN-US"}**]{#struct_0_10411_62186_261227251}
:::::

::::: {#660464565 .myid}
[]{#_Toc404797522}[]{#struct_0_10411_62186_1021251370}[]{#_Toc325734367}[]{#_Toc311203776}[]{#_Toc296424452}[]{#_Toc257621823}[]{#_Toc205712797}[]{#_Toc155674927}[]{#_Toc155674817}[]{#_Toc186935434}

**OAP \-- OAP配置命令 \-- oap client reboot**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OAP命令.files/image001.png){#图片 6 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10411_62186_718121150}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_x2091724219}
:::

[ ]{lang="EN-US"}

[**[oap client reboot]{lang="EN-US"}**]{#struct_0_10411_62186_1524678229}[命令用来重启]{style="font-family:宋体"}[OAP client]{lang="SV"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_x807544717}

[**[oap client reboot]{lang="EN-US"}**[ *client-id*]{lang="EN-US"}]{#struct_0_10411_62186_370262960}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_1779643676}

[[系统]{style="font-family:宋体"}]{#struct_0_10411_62186_x497702566}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_1384399531}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_x943765669}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_1009234846}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10411_62186_1193735836}

[*[client-id]{lang="SV"}*]{#struct_0_10411_62186_x2074757600}[：要重启的]{style="font-family:宋体"}[OAP client]{lang="SV"}[的]{style="font-family:宋体"}[Client ID]{lang="SV"}[，取值范围为]{style="font-family:宋体"}[1]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="SV" style="color:black"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10411_62186_2037735899}

[[输入该命令后，]{style="font-family:宋体"}]{#struct_0_10411_62186_x1468415637}[若指定的]{style="font-family:宋体"}[Client]{lang="SV"}[为]{style="font-family:宋体"}[Registered]{lang="EN-US"}[状态]{style="font-family:宋体"}[，]{style="font-family:宋体"}[OAP manager]{lang="SV"}[会发送一条重启的通告报文给指定的]{style="font-family:宋体"}[OAP client]{lang="SV"}[，]{style="font-family:宋体"}[OAP client]{lang="SV"}[收到此报文后将执行重启操作]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若指定的]{style="font-family:宋体"}[Client]{lang="SV"}[不存在，则会打印提示信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[OAP manager]{lang="EN-US"}]{#struct_0_10411_62186_2099172466}[给]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[分配]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于保证各]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[的唯一性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_x739679601}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_1384465067}[重启]{style="font-family:宋体"}[Client ID]{lang="SV"}[为]{style="font-family:宋体"}[1]{lang="SV"}[的]{style="font-family:
宋体"}[OAP client]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_10411_62186_x1339113997}

[\[Sysname\] oap client reboot 1]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_785949914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display oap client summary]{lang="EN-US"}**]{#struct_0_10411_62186_x1813955872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[oap client close]{lang="EN-US"}**]{#struct_0_10411_62186_1183883635}
:::::

::::: {#-375681376 .myid}
[]{#_Toc404797523}[]{#struct_0_10411_62186_487260624}[]{#_Toc325734368}[]{#_Toc311203777}[]{#_Toc296424453}[]{#_Toc257621824}[]{#_Toc205712798}[]{#_Toc155674923}[]{#_Toc155674813}[]{#_Toc186935438}[]{#_Toc186935439}[]{#_Toc186935446}[]{#_Toc186935449}[]{#_Toc186935452}[]{#_Toc186935455}[]{#_Toc296424454}[]{#_Toc257621825}[]{#_Toc205712799}[]{#_Toc155674922}[]{#_Toc155674812}[]{#_Toc186935457}[]{#_Toc186935460}[]{#_Toc186935461}[]{#_Toc186935462}[]{#_Toc186935469}[]{#_Toc186935472}[]{#_Toc186935475}[]{#_Toc186935478}

**OAP \-- OAP配置命令 \-- oap enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[**[![说明](OAP命令.files/image001.png){#图片 7 width="62" height="27"}]{lang="EN-US"}**]{#struct_0_10411_62186_253680744}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_1949083996}[型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[oap enable]{lang="EN-US"}**]{#struct_0_10411_62186_1383482027}[命令用来启用]{style="font-family:宋体"}[OAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo oap enable]{lang="EN-US"}**]{#struct_0_10411_62186_1528401338}[命令用来关闭]{style="font-family:宋体"}[OAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_469149689}

[**[oap enable]{lang="EN-US"}**]{#struct_0_10411_62186_x1011274406}

[**[undo oap enable]{lang="EN-US"}**]{#struct_0_10411_62186_1881118815}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10411_62186_1408815740}

[[接口下]{style="font-family:宋体"}[OAP]{lang="EN-US"}]{#struct_0_10411_62186_x1775343123}[协议功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_x659974540}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10411_62186_828055677}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_1383547563}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_739628186}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_x515126704}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_1558559567}

[[\# ]{lang="FR"}]{#struct_0_10411_62186_303977640}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下]{style="font-family:宋体"}[启用]{style="font-family:宋体"}[OAP]{lang="FR"}[功能]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10411_62186_720184198}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] oap enable]{lang="EN-US"}
:::::

::::: {#511845227 .myid}
[]{#_Toc404797524}[]{#struct_0_10411_62186_x1055096833}[]{#_Toc325734369}[]{#_Toc311203778}[]{#_Toc296424455}[]{#_Toc257621826}[]{#_Toc205712800}[]{#_Toc155674924}[]{#_Toc155674814}[]{#_Toc186935480}[]{#_Toc186935483}[]{#_Toc186935484}[]{#_Toc186935485}[]{#_Toc186935492}[]{#_Toc186935495}[]{#_Toc186935498}[]{#_Toc186935501}

**OAP \-- OAP配置命令 \-- oap timer clock-sync**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OAP命令.files/image001.png){#图片 8 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10411_62186_x171760679}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_98632353}
:::

[ ]{lang="EN-US"}

[**[oap timer clock-sync]{lang="EN-US"}**]{#struct_0_10411_62186_1384006316}[命令用来配置]{style="font-family:宋体"}[OAP manager]{lang="SV"}[到]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[时钟同步定时器的值。]{style="font-family:宋体"}

[**[undo oap timer clock-sync]{lang="EN-US"}**]{#struct_0_10411_62186_1016357031}[命令用来恢复]{style="font-family:
宋体"}[OAP manager]{lang="SV"}[到]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[时钟同步定时器的值为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_x14845466}

[**[oap timer clock-sync]{lang="EN-US"}**[ *minutes*]{lang="EN-US"}]{#struct_0_10411_62186_889929448}

[**[undo oap timer clock-sync]{lang="EN-US"}**]{#struct_0_10411_62186_x1012775700}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10411_62186_x1488397157}

[[OAP manager]{lang="EN-US"}]{#struct_0_10411_62186_1881470342}[到]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[的时钟同步定时器的值为]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_1327265514}

[[系统]{style="font-family:宋体"}]{#struct_0_10411_62186_2006570576}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_1384071852}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_x905516016}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_x2069964166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10411_62186_1511710508}

[*[minutes]{lang="SV"}*]{#struct_0_10411_62186_x2061892413}[：]{style="font-family:宋体"}[OAP manager]{lang="SV"}[到]{style="font-family:宋体"}[OAP client]{lang="SV"}[的时钟同步定时器的值，取值范围为]{style="font-family:宋体"}[0]{lang="SV"}[～]{style="font-family:宋体"}[1440]{lang="SV"}[，单位为分钟。]{style="font-family:
宋体"}[0]{lang="SV"}[表示]{style="font-family:宋体"}[OAP manager]{lang="SV"}[不会对]{style="font-family:宋体"}[OAP client]{lang="SV"}[进行时钟同步。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_557917033}

[[\# ]{lang="EN-US"}]{#struct_0_10411_62186_x346938396}[配置]{style="font-family:宋体"}[OAP manager]{lang="SV"}[到]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[的时钟同步定时器的值为]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10411_62186_x1887848812}

[\[Sysname\] oap timer clock-sync 20]{lang="EN-US"}
:::::

::::: {#-376997556 .myid}
[]{#_Toc404797525}[]{#struct_0_10411_62186_1384137388}[]{#_Toc325734370}[]{#_Toc311203779}[]{#_Toc296424456}[]{#_Toc257621827}[]{#_Toc205712801}[]{#_Toc155674925}[]{#_Toc155674815}[]{#_Toc186935503}[]{#_Toc186935504}[]{#_Toc186935511}[]{#_Toc186935514}[]{#_Toc186935517}[]{#_Toc186935520}

**OAP \-- OAP配置命令 \-- oap timer monitor**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OAP命令.files/image001.png){#图片 1 width="62" height="27"}]{lang="EN-US"}]{#struct_0_10411_62186_x560278244}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10411_62186_1675590597}
:::

[ ]{lang="EN-US"}

[**[oap timer monitor]{lang="EN-US"}**]{#struct_0_10411_62186_x788646806}[命令用来配置]{style="font-family:宋体"}[OAP manager]{lang="SV"}[到]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[监控定时器的值。]{style="font-family:宋体"}

[**[undo oap timer monitor]{lang="EN-US"}**]{#struct_0_10411_62186_1161113185}[命令用来恢复]{style="font-family:宋体"}[OAP manager]{lang="SV"}[到]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[监控定时器的值为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10411_62186_728674678}

[**[oap timer monitor]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_10411_62186_x1283897771}

[**[undo oap timer monitor]{lang="EN-US"}**]{#struct_0_10411_62186_1430191293}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10411_62186_1355325530}

[[OAP manager]{lang="SV"}]{#struct_0_10411_62186_x1176904144}[对]{style="font-family:宋体"}[OAP client]{lang="EN-US"}[的监控定时器的值为]{style="font-family:宋体"}[5]{lang="SV"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10411_62186_1384202924}

[[系统]{style="font-family:宋体"}]{#struct_0_10411_62186_1838583420}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10411_62186_59607313}

[[network-admin]{lang="EN-US"}]{#struct_0_10411_62186_x1395738579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10411_62186_914279186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10411_62186_124835358}

[*[seconds]{lang="SV"}*]{#struct_0_10411_62186_x1015951530}[：]{style="font-family:宋体"}[OAP manager]{lang="SV"}[对]{style="font-family:宋体"}[OAP client]{lang="SV"}[的监控定时器的值，取值范围为]{style="font-family:宋体"}[0]{lang="SV"}[～]{style="font-family:宋体"}[10]{lang="SV"}[，单位为秒。]{style="font-family:
宋体"}[0]{lang="SV"}[表示禁止]{style="font-family:宋体"}[OAP manager]{lang="SV"}[对]{style="font-family:宋体"}[OAP client]{lang="SV"}[的监控。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10411_62186_1975774496}

[[\# ]{lang="SV"}]{#struct_0_10411_62186_311494411}[配置]{style="font-family:宋体"}[OAP manager]{lang="SV"}[对]{style="font-family:宋体"}[OAP client]{lang="SV"}[的监控定时器的值为]{style="font-family:宋体"}[6]{lang="SV"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_10411_62186_1384268460}

[\[Sysname\] oap timer monitor 6]{lang="EN-US"}
:::::
