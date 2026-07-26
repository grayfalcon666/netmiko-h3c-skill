::: {#4862103 .myid}
[]{#_Toc404782800}[]{#struct_0_x5521_61440_581886556}

**应急Shell \-- 应急Shell配置命令 \-- copy**

------------------------------------------------------------------------

[**[copy]{lang="EN-US"}**]{#struct_0_x5521_61440_x478719864}[命令用来复制文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x530061011}

[**[copy ]{lang="EN-US"}***[fileurl-source fileurl-dest]{lang="EN-US"}*]{#struct_0_x5521_61440_1560046868}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_79499123}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_613844742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1294637379}

[*[fileurl-source]{lang="EN-US"}*]{#struct_0_x5521_61440_x197341953}[：源文件的名称。]{style="font-family:宋体"}

[*[fileurl-dest]{lang="EN-US"}*]{#struct_0_x5521_61440_1143386414}[：目标文件或者文件夹的名称。如果文件夹作为]{style="font-family:宋体"}*[fileurl]{lang="EN-US"}[-dest]{lang="EN-US"}*[，则系统会将文件复制到指定文件夹，使用源文件名作为目标文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1286113368}

[[执行该命令时，如果指定的目标文件不存在，则系统会先创建该文件，再复制内容；如果指定的目标文件已存在，则系统会提示是否覆盖该文件，如果选择"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_x5521_61440_x1636040006}["]{style="font-family:宋体"}[,]{lang="EN-US"}[系统会将目标文件的内容替换成源文件的内容，如果选择"]{style="font-family:宋体"}[N]{lang="EN-US"}["，则不做任何处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1970196671}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x706568301}[将文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[在当前文件夹下复制一份，并命名为]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> copy flash:/test.cfg flash:/testbackup.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_614434566}

[Copy flash:/test.cfg to flash:/testbackup.cfg?\[Y/N\]:y]{lang="EN-US"}

[Start to copy flash:/test.cfg to flash:/testbackup.cfg\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x10500125}[将文件]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[在当前文件夹下复制到已存在的文件]{style="font-family:宋体"}[testbackup.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> copy flash:/test.cfg flash:/testbackup.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_x622566124}

[Copy flash:/test.cfg to flash:/testbackup.cfg?\[Y/N\]:y]{lang="EN-US"}

[flash:/testbackup.cfg already exists. Overwrite it?\[Y/N\]:y]{lang="EN-US"}

[Start to copy flash:/test.cfg to flash:/testbackup.cfg\...Done.]{lang="EN-US"}
:::

::: {#432758916 .myid}
[]{#_Toc404782801}[]{#struct_0_x5521_61440_200873988}

**应急Shell \-- 应急Shell配置命令 \-- delete**

------------------------------------------------------------------------

[**[delete]{lang="EN-US"}**]{#struct_0_x5521_61440_1170157749}[命令用来彻底删除指定文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1638366195}

[**[delete ]{lang="EN-US"}***[file-url]{lang="EN-US"}*]{#struct_0_x5521_61440_x1656542210}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x104130148}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_2116415707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_614500102}

[*[file-url]{lang="EN-US"}*]{#struct_0_x5521_61440_x1569547538}[：要彻底删除的文件的名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1684520579}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_929265355}[彻底删除当前目录下的文件]{style="font-family:宋体"}[tt.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> delete flash:/tt.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_1110448189}

[Delete flash:/tt.cfg? \[Y/N\]:y]{lang="EN-US"}

[Deleting the file permanently will take a long time. Please wait\...]{lang="EN-US"}

[Start to delete flash:/tt.cfg\...Done.]{lang="EN-US"}
:::

::: {#1391204812 .myid}
[]{#_Toc404782802}[]{#struct_0_x5521_61440_x1059411583}

**应急Shell \-- 应急Shell配置命令 \-- dir**

------------------------------------------------------------------------

[**[dir]{lang="EN-US"}**]{#struct_0_x5521_61440_1886708858}[命令用来显示目录或文件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1422512702}

[**[dir ]{lang="EN-US"}**[\[ **/all** \] \[ *file-url* \]]{lang="EN-US"}]{#struct_0_x5521_61440_x1758742714}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1988102940}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1628776033}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1006220731}

[**[/all]{lang="EN-US"}**]{#struct_0_x5521_61440_1471945285}[：显示当前目录下所有的文件及子文件夹信息，显示内容包括隐藏文件和文件夹。不指定该参数时，显示当前目录下所有非隐藏的文件及子文件夹信息。]{style="font-family:宋体"}

[*[file]{lang="EN-US"}*[-*url*]{lang="EN-US"}]{#struct_0_x5521_61440_397971897}[：显示指定的文件或文件夹的信息。不指定该参数时，显示当前目录下的文件及子文件夹信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1218086867}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_397405793}[显示系统中所有的文件及文件夹信息。]{style="font-family:宋体"}

[[\<boot\> dir /all]{lang="EN-US"}]{#struct_0_x5521_61440_x1758677178}

[Directory of flash:]{lang="EN-US"}

[     0      drw-           -  Jan 01 2012 00:06:09     01]{lang="EN-US"}

[     1      drw-           -  Sep 15 2012 04:03:14     pki]{lang="EN-US"}

[     2      drw-           -  Jan 01 2012 00:04:07     test]{lang="EN-US"}

[     3      drw-           -  Aug 26 2012 02:48:00     license]{lang="EN-US"}

[     4      drw-           -  Nov 05 2012 06:45:07     logfile]{lang="EN-US"}

[     5      -rwh          20  Oct 20 2012 09:09:52     .snmpboots]{lang="EN-US"}

[     6      drw-           -  Nov 05 2012 05:56:22     diagfile]{lang="EN-US"}

[     7      drwh           -  Aug 20 2012 09:23:48     .trash]{lang="EN-US"}

[     8      -rw-         816  Aug 20 2012 06:15:00     ifindex.dat]{lang="EN-US"}

[     9      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg]{lang="EN-US"}

[    10      -rw-       60620  Aug 31 2012 09:01:43     startup.mdb]{lang="EN-US"}

[    11      drw-           -  Sep 30 2012 04:43:24     versionInfo]{lang="EN-US"}

[    12      drw-           -  Nov 05 2012 05:56:22     seclog]{lang="EN-US"}

[    13      -rwh          18  Aug 20 2012 09:09:34     .pathfile]{lang="EN-US"}

[    14      -rw-    11238400  Aug 30 2012 11:06:53     boot-t2301001.bin]{lang="EN-US"}

[    15      -rw-           0  Aug 31 2012 05:04:40     lauth.dat]{lang="EN-US"}

[    16      -rw-        4383  Oct 20 2012 06:15:00     test.cfg]{lang="EN-US"}

[ ]{lang="EN-US"}

[61440 KB total (11108 KB free)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1246668941}[显示系统中所有的非隐藏文件及文件夹信息。]{style="font-family:宋体"}

[[\<boot\> dir]{lang="EN-US"}]{#struct_0_x5521_61440_x1758611642}

[Directory of flash:]{lang="EN-US"}

[     0      drw-           -  Jan 01 2012 00:06:09     01]{lang="EN-US"}

[     1      drw-           -  Sep 15 2012 04:03:14     pki]{lang="EN-US"}

[     2      drw-           -  Jan 01 2012 00:04:07     test]{lang="EN-US"}

[     3      drw-           -  Aug 26 2012 02:48:00     license]{lang="EN-US"}

[     4      drw-           -  Nov 05 2012 06:45:07     logfile]{lang="EN-US"}

[     5      drw-           -  Nov 05 2012 05:56:22     diagfile]{lang="EN-US"}

[     6      -rw-         816  Aug 20 2012 06:15:00     ifindex.dat]{lang="EN-US"}

[     7      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg]{lang="EN-US"}

[     8      -rw-       60620  Aug 31 2012 09:01:43     startup.mdb]{lang="EN-US"}

[     9      drw-           -  Sep 30 2012 04:43:24     versionInfo]{lang="EN-US"}

[    10      drw-           -  Nov 05 2012 05:56:22     seclog]{lang="EN-US"}

[    11      -rw-    11238400  Aug 30 2012 11:06:53     boot-t2301001.bin]{lang="EN-US"}

[    12      -rw-           0  Aug 31 2012 05:04:40     lauth.dat]{lang="EN-US"}

[    13      -rw-        4383  Aug 20 2012 06:15:00     test.cfg]{lang="EN-US"}

[ ]{lang="EN-US"}

[61440 KB total (11108 KB free)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_833310824}[显示文件]{style="font-family:宋体"}[config.cfg]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<boot\> dir flash:/config.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_1146213279}

[Directory of flash:]{lang="EN-US"}

[     0      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg]{lang="EN-US"}

[ ]{lang="EN-US"}

[61440 KB total (11108 KB free)]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[dir]{lang="EN-US"}]{#struct_0_x5521_61440_1424936830}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_608292049}[[字段]{style="font-family:黑体"}]{#struct_0_x5521_61440_1018775938}
:::

[[说明]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758546106}

[[Directory of]{lang="EN-US"}]{#struct_0_x5521_61440_x1365123556}

[[当前显示的目录]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1379720303}

[[7      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_x1639654136}

[[文件或文件夹的信息：]{style="font-family:宋体"}]{#struct_0_x5521_61440_1455702532}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x5521_61440_x1508951171}[表示编号，由系统自动分配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-rw-]{lang="EN-US"}]{#struct_0_x5521_61440_x1083945125}[表示属性。第一个字符如果是]{style="font-family:宋体"}[d]{lang="EN-US"}[表示文件夹，如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示它是文件；第二个字符是]{style="font-family:宋体"}[r]{lang="EN-US"}[，表示本文件或文件夹是可读的；第三个字符是]{style="font-family:宋体"}[w]{lang="EN-US"}[，表示本文件或文件夹是可写的；第四个字符如果是]{style="font-family:宋体"}[h]{lang="EN-US"}[，表示本文件或文件夹是隐藏的，如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示它是可见的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3231]{lang="EN-US"}]{#struct_0_x5521_61440_x1759004858}[表示文件大小，单位为字节。如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示它是文件夹]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Aug 31 2012 09:01:41]{lang="EN-US"}]{#struct_0_x5521_61440_x46816384}[表示最近一次修改的时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[startup.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_850755214}[表示文件或文件夹]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[名称]{lang="EN-US" style="font-family:宋体"}

[[61440 KB total (11108 KB free)]{lang="EN-US"}]{#struct_0_x5521_61440_1343509491}

[[存储介质存储空间的大小，单位为千字节（存储介质中空闲存储空间的大小，单位为千字节）]{style="font-family:宋体"}]{#struct_0_x5521_61440_x855941969}

[ ]{lang="EN-US"}

::: {#1843823702 .myid}
[]{#_Toc404782803}[]{#struct_0_x5521_61440_x300188083}

**应急Shell \-- 应急Shell配置命令 \-- display copyright**

------------------------------------------------------------------------

[**[display copyright]{lang="EN-US"}**]{#struct_0_x5521_61440_x1758939322}[命令用来显示版权信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x722956811}

[**[display copyright]{lang="EN-US"}**]{#struct_0_x5521_61440_391846021}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_2062089510}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1490282737}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_911866903}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x429960507}[显示版权信息。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<boot\> display copyright]{lang="EN-US"}]{#struct_0_x5521_61440_x2026503747}

[[......略......]{style="font-family:宋体"}]{#struct_0_x5521_61440_x76463867}
:::

::: {#-690534616 .myid}
[]{#_Toc404782804}[]{#struct_0_x5521_61440_x1758873786}

**应急Shell \-- 应急Shell配置命令 \-- display install package**

------------------------------------------------------------------------

[**[display install package]{lang="EN-US"}**]{#struct_0_x5521_61440_x1719079703}[命令用来显示指定软件包的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x2019818606}

[**[display install package ]{lang="EN-US"}***[package]{lang="EN-US"}*]{#struct_0_x5521_61440_62591499}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1209711445}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x2079382676}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1089890365}

[*[package]{lang="EN-US"}*]{#struct_0_x5521_61440_586788793}[：表示软件包的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。该文件必须是存储介质根目录下，后缀名为]{style="font-family:宋体"}[.bin]{lang="EN-US"}[的文件，且文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/a.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1823830430}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1486172889}[显示软件包]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<boot\> display install package flash:/system.bin]{lang="EN-US"}]{#struct_0_x5521_61440_x1758808250}

[  flash:/system.bin]{lang="EN-US"}

[  \[Package\]]{lang="EN-US"}

[  Vendor: H3C]{lang="EN-US"}

[  Product: xxxx]{lang="EN-US"}

[  Service name: system]{lang="EN-US"}

[  Platform version: 7.1]{lang="EN-US"}

[  Product version: Alpha 0101]{lang="EN-US"}

[  Supported board: mpu]{lang="EN-US"}

[  \[Component\]]{lang="EN-US"}

[  Component: Comware system]{lang="EN-US"}

[  Description: system package]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display install package]{lang="EN-US"}]{#struct_0_x5521_61440_1898793073}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_612106892}[[字段]{style="font-family:黑体"}]{#struct_0_x5521_61440_1341782658}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5521_61440_2054445636}

[[\[Package\]]{lang="EN-US"}]{#struct_0_x5521_61440_x1758218426}

[[软件包的信息]{style="font-family:宋体"}]{#struct_0_x5521_61440_x546537990}

[[Vendor]{lang="EN-US"}]{#struct_0_x5521_61440_x754267602}

[[厂商]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1467956823}

[[Product]{lang="EN-US"}]{#struct_0_x5521_61440_189522371}

[[产品名称]{style="font-family:宋体"}]{#struct_0_x5521_61440_43252509}

[[Service name]{lang="EN-US"}]{#struct_0_x5521_61440_505815938}

[[软件包所包含的服务名称]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758152890}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_x5521_61440_1571353544}[boot]{lang="EN-US"}[，表示该软件包为]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{lang="EN-US" style="font-family:宋体"}[system]{lang="EN-US"}]{#struct_0_x5521_61440_x171595320}[，表示该软件包为]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1897504721}[patch]{lang="EN-US"}[，表示该软件包为补丁包]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为其它值，则表示该软件包为提供某项功能的]{style="font-family:宋体"}]{#struct_0_x5521_61440_x819746622}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}

[[Platform version]{lang="EN-US"}]{#struct_0_x5521_61440_x81806344}

[[平台版本号]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758742713}

[[Product version]{lang="EN-US"}]{#struct_0_x5521_61440_x1584818413}

[[产品版本号，通过该信息可以判断]{style="font-family:宋体"}[System]{lang="EN-US"}]{#struct_0_x5521_61440_1880315902}[包和]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包版本是否一致]{style="font-family:宋体"}

[[Supported board]{lang="EN-US"}]{#struct_0_x5521_61440_x215433572}

[[软件包支持的板类型（本字段的取值情况与设备的型号有关，请以设备的实际情况为准）：]{style="font-family:宋体"}]{#struct_0_x5521_61440_767063249}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[mpu]{lang="EN-US"}]{#struct_0_x5521_61440_x115211383}[表示主控板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[lc]{lang="EN-US"}]{#struct_0_x5521_61440_x1758677177}[表示业务板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sfc]{lang="EN-US"}]{#struct_0_x5521_61440_487154054}[表示网板]{lang="EN-US" style="font-family:宋体"}

[[\[Component\]]{lang="EN-US"}]{#struct_0_x5521_61440_x588078912}

[[组件信息，表示软件包的组成部分]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758611641}

[[Component]{lang="EN-US"}]{#struct_0_x5521_61440_x1895572531}

[[组件信息名称]{style="font-family:宋体"}]{#struct_0_x5521_61440_x863637619}

[[Description]{lang="EN-US"}]{#struct_0_x5521_61440_x1832889918}

[[软件包的描述信息]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758546105}

[ ]{lang="EN-US"}

::: {#-799154594 .myid}
[]{#_Toc404782805}[]{#struct_0_x5521_61440_x961839029}

**应急Shell \-- 应急Shell配置命令 \-- display interface m-eth0**

------------------------------------------------------------------------

[**[display interface m-eth0]{lang="EN-US"}**]{#struct_0_x5521_61440_2056712589}[命令用来显示管理以太网接口]{style="font-family:
宋体"}[M-Eth0]{lang="EN-US"}[的信息，包括]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[up/down]{lang="EN-US"}[状态以及报文统计息等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1359728845}

[**[display interface m-eth0]{lang="EN-US"}**]{#struct_0_x5521_61440_x1622173517}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1605825308}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x846042648}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_165816112}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_786673752}[显示管理以太网接口]{style="font-family:宋体"}[M-Eth0]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<boot\> display interface m-eth0]{lang="EN-US"}]{#struct_0_x5521_61440_x1759004857}

[m-eth0 current state: UP]{lang="EN-US"}

[Line protocol current state: UP]{lang="EN-US"}

[The Maximum Transmit Unit is 1500]{lang="EN-US"}

[Inet4 Address is 192.168.20.189/24]{lang="EN-US"}

[Inet6 Address is 1:1::1:1/64 Scope:Global]{lang="EN-US"}

[Inet6 Address is FE80::202:3FF:FE04:506/10 Scope:Link ]{lang="EN-US"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: c4ca-d94c-e201]{lang="EN-US"}

[IPV6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: c4ca-d94c-e201]{lang="EN-US"}

[Input:  8983 packets, 0 errors, 0 dropped, 0 overruns, 2 frame]{lang="EN-US"}

[Output: 431 packets, 0 errors, 0 dropped, 0 overruns, 0 carrier,]{lang="EN-US"}

[        0 collisions, 1000 txqueuelen]{lang="EN-US"}

[Input bytes:804168  ]{lang="EN-US"}

[Output bytes:30367]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display interface m-eth0]{lang="EN-US"}]{#struct_0_x5521_61440_712698503}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_607337523}[[字段]{style="font-family:黑体"}]{#struct_0_x5521_61440_148618613}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5521_61440_1712677000}

[[m-eth0 current state]{lang="EN-US"}]{#struct_0_x5521_61440_x1758939321}

[[接口的物理状态，状态可能为：]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1126241338}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_x5521_61440_x1103355263}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}[shutdown]{lang="EN-US"}[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x5521_61440_960125467}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x5521_61440_1761285154}[：该端口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol current state]{lang="EN-US"}]{#struct_0_x5521_61440_1486461721}

[[接口的链路层状态，其值直接取用接口的物理状态的当前值]{style="font-family:宋体"}]{#struct_0_x5521_61440_155511691}

[[The Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x5521_61440_x1758873785}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x5521_61440_x2122364230}

[[Inet4 Address]{lang="EN-US"}]{#struct_0_x5521_61440_269661824}

[[接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5521_61440_x581982311}[地址，给接口配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址后才显示该信息]{style="font-family:宋体"}

[[Inet6 Address]{lang="EN-US"}]{#struct_0_x5521_61440_x845128681}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_x2091207269}[地址，给接口配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址后才显示该信息。]{style="font-family:宋体"}[Scope:Global]{lang="EN-US"}[表示该地址为全球单播地址]{style="font-family:宋体"}

[[Inet6 Address is FE80::202:3FF:FE04:506/10 Scope:Link]{lang="EN-US"}]{#struct_0_x5521_61440_x1758808249}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_x1186386178}[链路本地地址，该地址在接口物理状态变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[时，由系统自动生成]{style="font-family:宋体"}

[[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address]{lang="EN-US"}]{#struct_0_x5521_61440_x1981791633}

[[IPv4]{lang="EN-US"}]{#struct_0_x5521_61440_x1923142827}[报文发送帧格式，以及硬件地址]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_x5521_61440_x55242790}[，]{style="font-family:宋体"}

[[Hardware Address]{lang="EN-US"}]{#struct_0_x5521_61440_x1758218425}

[[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_1019545951}[报文发送帧格式，以及硬件地址]{style="font-family:宋体"}

[[Input: 8983 packets, 0 errors, 0 dropped, 0 overruns, 2 frame]{lang="EN-US"}]{#struct_0_x5521_61440_1722638928}

[[接口接收的报文的统计信息：报文总数，错误报文数，丢弃报文数，队列溢出报文数]{style="font-family:宋体"}[]{lang="EN-US"}]{#struct_0_x5521_61440_x42608525}[，帧队列错误报文数]{style="font-family:宋体"}

[[Output: 431 packets, 0 errors, 0 dropped, 0 overruns, 0 carrier,  0 collisions, 1000 txqueuelen]{lang="EN-US"}]{#struct_0_x5521_61440_455254686}

[[接口发送的报文的统计信息：报文总数，错误报文数，丢弃报文数，队列溢出报文数，载波出错报文数，冲突的报文数，每个队列允许的最大帧数]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758152889}

[[Input bytes]{lang="EN-US"}]{#struct_0_x5521_61440_361565499}

[[接口接收的报文的总字节数]{style="font-family:宋体"}]{#struct_0_x5521_61440_115134281}

[[Output bytes]{lang="EN-US"}]{#struct_0_x5521_61440_x1935852545}

[[接口发送的报文的总字节数]{style="font-family:宋体"}]{#struct_0_x5521_61440_x2136743586}

[ ]{lang="EN-US"}

::: {#-935850768 .myid}
[]{#_Toc404782806}[]{#struct_0_x5521_61440_x1758742716}

**应急Shell \-- 应急Shell配置命令 \-- display ip routing-table**

------------------------------------------------------------------------

[**[display ip routing-table]{lang="EN-US"}**]{#struct_0_x5521_61440_x825303526}[命令用来显示]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[路由信息表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x989897014}

[**[display ip routing-table]{lang="EN-US"}**]{#struct_0_x5521_61440_x198794434}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1746925751}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1355029280}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1074578860}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_235885031}[显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息表。]{style="font-family:宋体"}

[[\<boot\> display ip routing-table]{lang="EN-US"}]{#struct_0_x5521_61440_x1758677180}

[Kernel IP routing table]{lang="EN-US"}

[Destination     Gateway         Genmask         Flags Metric Ref    Use Iface]{lang="EN-US"}

[192.168.116.0   \*               255.255.255.0   U     0      0        0 m-eth0]{lang="EN-US"}

[default         192.168.116.1   0.0.0.0         UG    0      0        0 m-eth0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ip routing-table]{lang="EN-US"}]{#struct_0_x5521_61440_889455541}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_636567069}[[字段]{style="font-family:黑体"}]{#struct_0_x5521_61440_406835137}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5521_61440_389591870}

[[Kernel IP routing table]{lang="EN-US"}]{#struct_0_x5521_61440_x709776852}

[[IPv4]{lang="EN-US"}]{#struct_0_x5521_61440_x617948483}[路由表信息]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_x5521_61440_1517909985}

[[目的地址（取值为]{style="font-family:宋体"}[default]{lang="EN-US"}]{#struct_0_x5521_61440_x1758611644}[时表示缺省路由）]{style="font-family:宋体"}

[[Gateway]{lang="EN-US"}]{#struct_0_x5521_61440_1639879878}

[[网关（如果不需要使用网关，则该字段显示为"]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_x5521_61440_1400521814}["）]{style="font-family:宋体"}

[[Genmask]{lang="EN-US"}]{#struct_0_x5521_61440_364025827}

[[掩码（取值为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}]{#struct_0_x5521_61440_x1556750360}[时表示缺省路由的掩码）]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x5521_61440_821049421}

[[标志位：]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758546108}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G]{lang="EN-US"}]{#struct_0_x5521_61440_x202324142}[：网关路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x5521_61440_x46939279}[：主机路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x5521_61440_x1068955102}[：通过邻居发现学习到的缺省路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x5521_61440_x918521566}[：通过路由发布学习到的路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x5521_61440_1294884325}[：缓存表项，用于快速转发去往某目的地的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x5521_61440_x1759004860}[：可用路由]{lang="EN-US" style="font-family:宋体"}

[[Metric]{lang="EN-US"}]{#struct_0_x5521_61440_309217368}

[[路由开销]{style="font-family:宋体"}]{#struct_0_x5521_61440_x707464653}

[[Ref]{lang="EN-US"}]{#struct_0_x5521_61440_1563149266}

[[表示路由表项被其它表项引用的次数，即和其它表项间的依赖关系]{style="font-family:宋体"}]{#struct_0_x5521_61440_1163207541}

[[Use]{lang="EN-US"}]{#struct_0_x5521_61440_x1758939324}

[[表示这条表项被使用过的次数，即该路由被匹配到的次数]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1885756225}

[[Iface]{lang="EN-US"}]{#struct_0_x5521_61440_x2142514712}

[[出接口]{style="font-family:宋体"}]{#struct_0_x5521_61440_x426594688}

[ ]{lang="EN-US"}

::: {#1738996239 .myid}
[]{#_Toc404782807}[]{#struct_0_x5521_61440_x1507316011}

**应急Shell \-- 应急Shell配置命令 \-- display ipv6 routing-table**

------------------------------------------------------------------------

[**[display ipv6 routing-table]{lang="EN-US"}**]{#struct_0_x5521_61440_x690131225}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[路由信息表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758873788}

[**[display ipv6 routing-table]{lang="EN-US"}**]{#struct_0_x5521_61440_1769318539}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_984526611}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x836983299}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_607934364}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_136743806}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息表。]{style="font-family:宋体"}

[[\<boot\> display ipv6 routing-table]{lang="EN-US"}]{#struct_0_x5521_61440_x1758808252}

[Kernel IPv6 routing table]{lang="EN-US"}

[Destination                                 Next Hop]{lang="EN-US"}

[    Flags Metric Ref    Use Iface]{lang="EN-US"}

[::1/128                                     ::]{lang="EN-US"}

[    U     0      0        1 lo]{lang="EN-US"}

[FE80::201:2FF:FE03:406/128                  ::]{lang="EN-US"}

[    U     0      0        1 lo]{lang="EN-US"}

[FE80::/64                                   ::]{lang="EN-US"}

[    U     256    0        0 m-eth0]{lang="EN-US"}

[FF02::1:2/128                               FF02::1:2]{lang="EN-US"}

[    UC    0      2888     0 m-eth0]{lang="EN-US"}

[FF00::/8                                    ::]{lang="EN-US"}

[    U     256    0        0 m-eth0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ipv6 routing-table]{lang="EN-US"}]{#struct_0_x5521_61440_x1233374809}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_629182113}[[字段]{style="font-family:黑体"}]{#struct_0_x5521_61440_485025064}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5521_61440_x461041580}

[[Kernel IPv6 routing table]{lang="EN-US"}]{#struct_0_x5521_61440_x1259694861}

[[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_x896759575}[路由表信息]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_x5521_61440_332795092}

[[目的地址]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758218428}

[[Next Hop]{lang="EN-US"}]{#struct_0_x5521_61440_260031064}

[[下一跳]{style="font-family:宋体"}]{#struct_0_x5521_61440_x2121656639}

[[Flags]{lang="EN-US"}]{#struct_0_x5521_61440_x381563933}

[[标志位：]{style="font-family:宋体"}]{#struct_0_x5521_61440_142594095}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G]{lang="EN-US"}]{#struct_0_x5521_61440_638792382}[：网关路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x5521_61440_x1758152892}[：主机路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x5521_61440_x1560814338}[：通过邻居发现学习到的缺省路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x5521_61440_x497307073}[：通过路由发布学习到的路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x5521_61440_x1246651802}[：缓存表项，用于快速转发去往某目的地的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x5521_61440_x611211880}[：可用路由]{lang="EN-US" style="font-family:宋体"}

[[Metric]{lang="EN-US"}]{#struct_0_x5521_61440_1149001047}

[[路由开销]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758742715}

[[Ref]{lang="EN-US"}]{#struct_0_x5521_61440_x422018999}

[[表示路由表项被其它表项引用的次数，即和其它表项间的依赖关系]{style="font-family:宋体"}]{#struct_0_x5521_61440_317564227}

[[Use]{lang="EN-US"}]{#struct_0_x5521_61440_x1740302846}

[[表示这条表项被使用过的次数，即该路由被匹配到的次数]{style="font-family:宋体"}]{#struct_0_x5521_61440_1411508526}

[[Iface]{lang="EN-US"}]{#struct_0_x5521_61440_x1758677179}

[[出接口，]{style="font-family:宋体"}[lo]{lang="EN-US"}]{#struct_0_x5521_61440_x319415000}[表示环回口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-333764678 .myid}
[]{#_Toc404782808}[]{#struct_0_x5521_61440_x2113195922}

**应急Shell \-- 应急Shell配置命令 \-- display version**

------------------------------------------------------------------------

[**[display version]{lang="EN-US"}**]{#struct_0_x5521_61440_x733614423}[命令用来显示]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的版本信息，包括当前使用的平台版本号、产品版本号等的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x677506970}

[**[display version]{lang="EN-US"}**]{#struct_0_x5521_61440_x545210874}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1821765466}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x849579768}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758611643}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x732773117}[查看]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的版本信息。（不同设备的版本信息不同，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<boot\> display version]{lang="EN-US"}]{#struct_0_x5521_61440_861099855}

[[......略......]{style="font-family:宋体"}]{#struct_0_x5521_61440_x2052733775}
:::

::: {#446157247 .myid}
[]{#_Toc404782809}[]{#struct_0_x5521_61440_807725635}

**应急Shell \-- 应急Shell配置命令 \-- format**

------------------------------------------------------------------------

[**[format]{lang="EN-US"}**]{#struct_0_x5521_61440_x2038297999}[命令用来格式化存储介质。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x437789324}

[**[format ]{lang="EN-US"}***[device]{lang="EN-US"}*]{#struct_0_x5521_61440_955519733}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1411912381}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1758546107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_200960385}

[*[device]{lang="EN-US"}*]{#struct_0_x5521_61440_437297941}[：为存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_270992711}

[[格式化操作将导致存储介质上的所有文件丢失，并且不可恢复。尤其需要注意的是，如果存储介质上有启动配置文件和启动文件，格式化该存储介质，将丢失启动配置文件和启动文件，导致设备重启后无法启动，请谨慎操作。]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1747422223}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x443912496}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x743561082}[格式化]{style="font-family:宋体"}[Flash]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> format flash:]{lang="EN-US"}]{#struct_0_x5521_61440_2013169105}

[All data on flash: will be lost, continue?\[Y/N\]:y]{lang="EN-US"}

[Formatting flash:... Done.]{lang="EN-US"}
:::

::: {#228733076 .myid}
[]{#_Toc404782810}[]{#struct_0_x5521_61440_x1759004859}

**应急Shell \-- 应急Shell配置命令 \-- ftp**

------------------------------------------------------------------------

[**[ftp]{lang="EN-US"}**]{#struct_0_x5521_61440_1519267557}[命令用来访问]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_2087156230}

[**[ftp ]{lang="EN-US"}**[{ *server-ipv4-address* \| **ipv6** *server-ipv6-address* } { **get** *remote-file* *local-file* \| **put** *local-file* *remote-file* }]{lang="EN-US"}]{#struct_0_x5521_61440_70931395}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x697094472}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1720448939}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x308291530}

[*[server-ipv4-address]{lang="EN-US"}*]{#struct_0_x5521_61440_489776472}[：]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[server-ipv6-address]{lang="EN-US"}*]{#struct_0_x5521_61440_x69331335}[：]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[get ]{lang="EN-US"}***[remote-file]{lang="EN-US"}*[ *local-file*]{lang="EN-US"}]{#struct_0_x5521_61440_358874962}[：表示从]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器上下载一个文件到本地，]{style="font-family:宋体"}*[remote-file]{lang="EN-US"}*[表示]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器上的文件的名称，]{style="font-family:宋体"}*[local-file]{lang="EN-US"}*[表示本地的文件的名称。]{style="font-family:宋体"}

[**[put ]{lang="EN-US"}***[local-file]{lang="EN-US"}*[ *remote-file*]{lang="EN-US"}]{#struct_0_x5521_61440_x148881705}[：表示从本地上传一个文件到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器，]{style="font-family:宋体"}*[local-file]{lang="EN-US"}*[表示本地的文件的名称，]{style="font-family:宋体"}*[remote-file]{lang="EN-US"}*[表示]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器上的文件的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x309885331}

[[当网络拥塞，文件传输速度很慢的时候，用户可以使用]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_x5521_61440_73414894}[组合键中断本次]{style="font-family:宋体"}[FTP]{lang="EN-US"}[操作，稍后再试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1580682434}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x437809672}[使用用户名]{style="font-family:宋体"}[test]{lang="EN-US"}[、密码]{style="font-family:宋体"}[123]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.1.100]{lang="EN-US"}[上下载文件]{style="font-family:宋体"}[111.txt]{lang="EN-US"}[，保存到本地时使用名称]{style="font-family:宋体"}[222.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> ftp 192.168.1.100 get 111.txt flash:/222.txt]{lang="EN-US"}]{#struct_0_x5521_61440_x1741745327}

[User: test]{lang="EN-US"}

[Password: \*\*\*]{lang="EN-US"}
:::

::: {#-334212409 .myid}
[]{#_Toc404782811}[]{#struct_0_x5521_61440_x1329472235}

**应急Shell \-- 应急Shell配置命令 \-- install load**

------------------------------------------------------------------------

[**[install load]{lang="EN-US"}**]{#struct_0_x5521_61440_x1758873787}[命令用来加载]{style="font-family:宋体"}[System]{lang="EN-US"}[包，并引导设备进入]{style="font-family:宋体"}[Comware]{lang="EN-US"}[系统。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1009803652}

[**[install]{lang="EN-US"}**[ **load** *system-package*]{lang="EN-US"}]{#struct_0_x5521_61440_x1471369654}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x680514109}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1948391222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1351960426}

[*[system-package]{lang="EN-US"}*]{#struct_0_x5521_61440_x931373472}[：]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。该文件必须是设备存储介质根目录下，后缀名为]{style="font-family:宋体"}[.bin]{lang="EN-US"}[的文件，且文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/startup-system.bin]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[*[system-package]{lang="EN-US"}*]{#struct_0_x5521_61440_x785230124}[：]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。该文件必须是当前主控板存储介质根目录下，后缀名为]{style="font-family:宋体"}[.bin]{lang="EN-US"}[的文件，且文件名中必须包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}[信息，形如]{style="font-family:宋体"}[flash:/startup-system.bin]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[*[system-package]{lang="EN-US"}*]{#struct_0_x5521_61440_341263429}[：]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。该文件必须是本成员设备存储介质根目录下，后缀名为]{style="font-family:宋体"}[.bin]{lang="EN-US"}[的文件，且文件名中必须包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}[信息，形如]{style="font-family:宋体"}[flash:/startup-system.bin]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[*[system-package]{lang="EN-US"}*]{#struct_0_x5521_61440_x851521720}[：]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。该文件必须是当前主控板存储介质根目录下，后缀名为]{style="font-family:宋体"}[.bin]{lang="EN-US"}[的文件，且文件名中必须包含存储介质的名称，不能包含]{style="font-family:宋体"}[chassis]{lang="EN-US"}[和]{style="font-family:宋体"}[slot]{lang="EN-US"}[信息，形如]{style="font-family:宋体"}[flash:/startup-system.bin]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758808251}

[[执行该命令，系统会同时更新主用下次启动软件包列表，新列表中只包含]{style="font-family:宋体"}[Boot]{lang="EN-US"}]{#struct_0_x5521_61440_x830090282}[包和]{style="font-family:宋体"}[System]{lang="EN-US"}[包，以保证设备下次能够正常启动。如需运行]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包和补丁包，须重新下载、安装，具体配置步骤请参见"基础配置指导"中的"软件升级"和"]{style="font-family:宋体"}[ISSU]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_613081511}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1840230808}[加载]{style="font-family:宋体"}[System]{lang="EN-US"}[包，进入]{style="font-family:宋体"}[Comware]{lang="EN-US"}[系统。]{style="font-family:宋体"}

[[\<boot\> install load flash:/system.bin]{lang="EN-US"}]{#struct_0_x5521_61440_x1758218427}

[Check package flash:/system.bin \...]{lang="EN-US"}

[Extracting package \...]{lang="EN-US"}

[ ]{lang="EN-US"}

[Loading\...]{lang="EN-US"}

[Line con1 is available.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Press ENTER to get started.]{lang="EN-US"}
:::

::: {#-574569881 .myid}
[]{#_Toc404782812}[]{#struct_0_x5521_61440_x2112621931}

**应急Shell \-- 应急Shell配置命令 \-- interface m-eth0**

------------------------------------------------------------------------

[**[interface m-eth0]{lang="EN-US"}**]{#struct_0_x5521_61440_x1284830424}[命令用来进入管理以太网接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1665941910}

[**[interface m-eth0]{lang="EN-US"}**]{#struct_0_x5521_61440_165484870}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x911030048}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1835061685}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_698130552}

[[进入管理以太网接口视图后，可以给管理以太网接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5521_61440_737779795}[地址和网关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1073963456}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x1758152891}[进入管理以太网接口视图。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_5269603}

[\[boot\] interface m-eth0]{lang="EN-US"}

[\[boot-m-eth0\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_569090402}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[quit]{lang="EN-US"}**]{#struct_0_x5521_61440_912005391}
:::

::: {#1613709608 .myid}
[]{#_Toc404782813}[]{#struct_0_x5521_61440_x645484744}

**应急Shell \-- 应急Shell配置命令 \-- ip address**

------------------------------------------------------------------------

[**[ip address]{lang="EN-US"}**]{#struct_0_x5521_61440_535117541}[命令用来配置管理以太网接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip address]{lang="EN-US"}**]{#struct_0_x5521_61440_x899822360}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1424802447}

[**[ip]{lang="EN-US"}**[ **address** *ip-address* { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_x5521_61440_x1113062646}

[**[undo ip address]{lang="EN-US"}**]{#struct_0_x5521_61440_x1758742718}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5521_61440_337495888}

[[管理以太网接口下没有配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5521_61440_x1787656562}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1415042837}

[[管理以太网接口视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1032045013}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1730884216}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x5521_61440_1442398631}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x5521_61440_x1173165868}[：子网掩码长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x5521_61440_x998209906}[：子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758677182}

[[多次使用本命令，最新配置生效。]{style="font-family:宋体"}]{#struct_0_x5521_61440_x273343873}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5521_61440_2011526848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在手工关闭的管理以太网接口下配置或删除]{style="font-family:宋体"}]{#struct_0_x5521_61440_1171120641}[IP]{lang="EN-US"}[地址时，系统会同时自动激活该接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请确保配置的]{style="font-family:宋体"}]{#struct_0_x5521_61440_107820268}[IP]{lang="EN-US"}[地址没有和网络上其它设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1325604471}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x1421582037}[将管理以太网接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置为]{style="font-family:宋体"}[192.168.1.1/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_2034498683}

[\[boot\] interface m-eth0]{lang="EN-US"}

[\[boot-m-eth0\] ip address 192.168.1.1 24]{lang="EN-US"}
:::

::: {#1534732554 .myid}
[]{#_Toc404782814}[]{#struct_0_x5521_61440_1731177966}

**应急Shell \-- 应急Shell配置命令 \-- ip gateway**

------------------------------------------------------------------------

[**[ip gateway]{lang="EN-US"}**]{#struct_0_x5521_61440_x1758611646}[命令用来给管理以太网接口配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[**[undo ip gateway]{lang="EN-US"}**]{#struct_0_x5521_61440_x1492288004}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1674414017}

[**[ip]{lang="EN-US"}**[ **gateway** *ip-address*]{lang="EN-US"}]{#struct_0_x5521_61440_x1952839953}

[**[undo ip gateway]{lang="EN-US"}**]{#struct_0_x5521_61440_x246826778}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x448440787}

[[管理以太网接口下没有配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5521_61440_1206194518}[网关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1230304824}

[[管理以太网接口视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_773735124}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758546110}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x5521_61440_x558620038}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网关的地址，为点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1103819465}

[[在]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5521_61440_x154780581}[网络中，当本设备需要和不在同一网段的远程设备通信时，需要配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网关来转发报文。]{style="font-family:宋体"}

[[多次使用本命令，最新配置生效。]{style="font-family:宋体"}]{#struct_0_x5521_61440_x689245516}

[[修改或者删除管理以太网接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5521_61440_1431210831}[地址，会导致网关配置被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x556591782}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1237286358}[将管理以太网接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网关配置为]{style="font-family:宋体"}[192.168.1.5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_x1979765718}

[\[boot\] interface m-eth0]{lang="EN-US"}

[\[boot-m-eth0\] ip gateway 192.168.1.5]{lang="EN-US"}
:::

::: {#-1250635572 .myid}
[]{#_Toc404782815}[]{#struct_0_x5521_61440_x1759004862}

**应急Shell \-- 应急Shell配置命令 \-- ipv6 address**

------------------------------------------------------------------------

[**[ipv6 address]{lang="EN-US"}**]{#struct_0_x5521_61440_1472016782}[命令用来配置管理以太网接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ipv6 address]{lang="EN-US"}**]{#struct_0_x5521_61440_1041690785}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1228358556}

[**[ipv6]{lang="EN-US"}**[ **address** *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_x5521_61440_x1944921896}

[**[undo ipv6 address]{lang="EN-US"}**]{#struct_0_x5521_61440_1820863666}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1893625681}

[[管理以太网接口下没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_x393504689}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1870464902}

[[管理以太网接口视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1542977205}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758939326}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x5521_61440_1246411657}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x5521_61440_x870402072}[：前缀的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1569647546}

[[多次使用本命令，最新配置生效。]{style="font-family:宋体"}]{#struct_0_x5521_61440_x874478654}

[[在手工关闭的管理以太网接口下配置或删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_963861930}[地址时，系统会同时自动激活该接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1032086205}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x53597211}[将管理以太网接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址配置为]{style="font-family:宋体"}[2001::1/64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_x1758873790}

[\[boot\] interface m-eth0]{lang="EN-US"}

[\[boot-m-eth0\] ipv6 address 2001::1 64]{lang="EN-US"}
:::

::: {#-1834415754 .myid}
[]{#_Toc404782816}[]{#struct_0_x5521_61440_1413153715}

**应急Shell \-- 应急Shell配置命令 \-- ipv6 gateway**

------------------------------------------------------------------------

[**[ipv6 gateway]{lang="EN-US"}**]{#struct_0_x5521_61440_x21780682}[命令用来给管理以太网接口配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[**[undo ipv6]{lang="EN-US"}**[ **gateway**]{lang="EN-US"}]{#struct_0_x5521_61440_597146713}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x599102577}

[**[ipv6]{lang="EN-US"}**[ **gateway** *link-local*]{lang="EN-US"}]{#struct_0_x5521_61440_736443496}

[**[undo ipv6]{lang="EN-US"}**[ **gateway**]{lang="EN-US"}]{#struct_0_x5521_61440_1915882440}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1982929643}

[[管理以太网接口下没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_262096402}[网关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758808254}

[[管理以太网接口视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x426805755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x716266490}

[*[link-local]{lang="EN-US"}*]{#struct_0_x5521_61440_x1462912215}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网关的链路本地地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x646333310}

[[在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_x740582288}[网络中，当本设备需要和不在同一网段的远程设备通信时，需要配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网关来转发报文。]{style="font-family:宋体"}

[[多次使用本命令，最新配置生效。]{style="font-family:宋体"}]{#struct_0_x5521_61440_1018505216}

[[修改或者删除管理以太网接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5521_61440_1374446164}[地址，会导致]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网关配置被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1635053603}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_955025845}[将管理以太网接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网关配置为]{style="font-family:宋体"}[FE80::BAAF:67FF:FE27:DCD0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_x1758218430}

[\[boot\] interface m-eth0]{lang="EN-US"}

[\[boot-m-eth0\] ipv6 gateway FE80::BAAF:67FF:FE27:DCD0]{lang="EN-US"}
:::

::: {#-1196816799 .myid}
[]{#_Toc404782817}[]{#struct_0_x5521_61440_616326960}

**应急Shell \-- 应急Shell配置命令 \-- mkdir**

------------------------------------------------------------------------

[**[mkdir]{lang="EN-US"}**]{#struct_0_x5521_61440_x2097871416}[命令用来在存储介质的指定路径下创建文件夹。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_527079685}

[**[mkdir]{lang="EN-US"}**[ *directory*]{lang="EN-US"}]{#struct_0_x5521_61440_1709563977}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1739173544}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1631685018}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_48352722}

[*[directory]{lang="EN-US"}*]{#struct_0_x5521_61440_x1758152894}[：文件夹的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x398014924}

[[在使用该命令创建文件夹之前，指定的路径必须已经存在。比如：创建文件夹]{style="font-family:宋体"}[flash:/test/mytest]{lang="EN-US"}]{#struct_0_x5521_61440_1958672303}[，这时，]{style="font-family:宋体"}[test]{lang="EN-US"}[文件夹必须已经存在，否则，创建失败。]{style="font-family:宋体"}

[[如果创建的文件夹与指定路径下的其它文件或文件夹重名，则创建操作失败。]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1620886631}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_631248220}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x127140378}[在当前路径创建文件夹]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> mkdir flash:/test]{lang="EN-US"}]{#struct_0_x5521_61440_2115633360}

[Directory flash:/test created.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_313236247}[在路径]{style="font-family:宋体"}[test/]{lang="EN-US"}[下创建文件夹]{style="font-family:宋体"}[subtest]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> mkdir flash:/test/subtest]{lang="EN-US"}]{#struct_0_x5521_61440_x1758742717}

[Directory flash:/test/subtest created.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_740780415}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dir]{lang="EN-US"}**]{#struct_0_x5521_61440_740220379}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rmdir]{lang="EN-US"}**]{#struct_0_x5521_61440_x1338862194}
:::

::: {#109910483 .myid}
[]{#_Toc404782818}[]{#struct_0_x5521_61440_1825297413}

**应急Shell \-- 应急Shell配置命令 \-- more**

------------------------------------------------------------------------

[**[more]{lang="EN-US"}**]{#struct_0_x5521_61440_x953106554}[命令用来显示指定文件的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_764163681}

[**[more ]{lang="EN-US"}***[file-url]{lang="EN-US"}*]{#struct_0_x5521_61440_x1473745528}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x978275030}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1195138987}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758677181}

[*[file-url]{lang="EN-US"}*]{#struct_0_x5521_61440_x676628400}[：要显示的文件的名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_699424232}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_627003822}[显示文件]{style="font-family:宋体"}[test.txt]{lang="EN-US"}[的内容。]{style="font-family:宋体"}

[[\<boot\> more flash:/test.txt]{lang="EN-US"}]{#struct_0_x5521_61440_x966430036}

[Have a nice day.]{lang="EN-US"}
:::

::: {#-1859457985 .myid}
[]{#_Toc404782819}[]{#struct_0_x5521_61440_x296935099}

**应急Shell \-- 应急Shell配置命令 \-- move**

------------------------------------------------------------------------

[**[move]{lang="EN-US"}**]{#struct_0_x5521_61440_x723090332}[命令用来移动文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1170800758}

[**[move ]{lang="EN-US"}***[fileurl-source fileurl-dest]{lang="EN-US"}*]{#struct_0_x5521_61440_892875778}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1758611645}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_73795937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1691130140}

[*[fileurl]{lang="EN-US"}[-source]{lang="EN-US"}*]{#struct_0_x5521_61440_1332172945}[：源文件的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[fileurl]{lang="EN-US"}[-dest]{lang="EN-US"}*]{#struct_0_x5521_61440_x1933246922}[：目标文件或文件夹的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x701642540}

[[执行该命令时，如果指定的目标文件不存在，则系统会先直接执行文件移动操作；如果指定的目标文件已存在，则系统会提示是否覆盖该文件，如果选择"]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_x5521_61440_x379254671}["]{style="font-family:宋体"}[,]{lang="EN-US"}[系统会执行文件移动操作，如果选择"]{style="font-family:宋体"}[N]{lang="EN-US"}["，则不做任何处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x605039550}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1859324397}[移动文件]{style="font-family:宋体"}[config.cfg]{lang="EN-US"}[到目录]{style="font-family:宋体"}[flash:/test]{lang="EN-US"}[下。]{style="font-family:宋体"}

[[\<boot\>move flash:/config.cfg flash:/test/]{lang="EN-US"}]{#struct_0_x5521_61440_x1758546109}

[Move flash:/config.cfg to flash:/test/config.cfg?\[Y/N\]:y]{lang="EN-US"}

[\<boot\> dir flash:/test]{lang="EN-US"}

[Directory of flash:/test]{lang="EN-US"}

[     0      -rw-       77065  Oct 20 1939 06:15:02     test.mdb]{lang="EN-US"}

[ ]{lang="EN-US"}

[61440 KB total (11108 KB free)]{lang="EN-US"}
:::

::: {#-1885171420 .myid}
[]{#_Toc404782820}[]{#struct_0_x5521_61440_1363759799}

**应急Shell \-- 应急Shell配置命令 \-- ping**

------------------------------------------------------------------------

[**[ping]{lang="EN-US"}**]{#struct_0_x5521_61440_x275111129}[命令用来检查指定目的端是否可达。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_313298271}

[**[ping]{lang="EN-US"}**[ \[ **-c** *count \|* **-s** *size* \] \* *ip-address*]{lang="EN-US"}]{#struct_0_x5521_61440_x662113111}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_380534416}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1251011949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1759004861}

[**[-c]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_x5521_61440_1875301309}[：指定发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-s]{lang="EN-US"}***[ size]{lang="EN-US"}*]{#struct_0_x5521_61440_1336787087}[：指定发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文的长度，取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[56]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x5521_61440_1313453793}[：目的端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x93149481}

[[执行]{style="font-family:宋体"}**[ping]{lang="EN-US"}**]{#struct_0_x5521_61440_2004160550}[命令后，源端会给目的端发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文。在执行命令过程中，键入]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[可终止]{style="font-family:宋体"}**[ping]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1214507261}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_947271856}[检查到目的端]{style="font-family:宋体"}[1.2.1.1]{lang="EN-US"}[是否可达。]{style="font-family:宋体"}

[[\<boot\> ping 1.2.1.1]{lang="EN-US"}]{#struct_0_x5521_61440_x1758939325}

[PING 1.2.1.1 (1.2.1.1): 56 data bytes]{lang="EN-US"}

[56 bytes from 1.2.1.1: seq=0 ttl=128 time=2.243 ms]{lang="EN-US"}

[56 bytes from 1.2.1.1: seq=1 ttl=128 time=0.717 ms]{lang="EN-US"}

[56 bytes from 1.2.1.1: seq=2 ttl=128 time=0.891 ms]{lang="EN-US"}

[56 bytes from 1.2.1.1: seq=3 ttl=128 time=0.745 ms]{lang="EN-US"}

[56 bytes from 1.2.1.1: seq=4 ttl=128 time=0.911 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- 1.2.1.1 ping statistics \-\--]{lang="EN-US"}

[5 packets transmitted, 5 packets received, 0% packet loss]{lang="EN-US"}

[round-trip min/avg/max = 0.717/1.101/2.243 ms]{lang="EN-US"}

[]{#struct_0_x5521_61440_843127130}[[表1-6 ]{lang="EN-US"}[ping]{lang="EN-US"}]{#_Ref198434076}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_632001523}[[字段]{style="font-family:黑体"}]{#struct_0_x5521_61440_587840075}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1291770742}

[[PING 1.2.1.1 (1.2.1.1)]{lang="EN-US"}]{#struct_0_x5521_61440_x185802160}

[[检查]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5521_61440_x382903242}[地址为]{style="font-family:宋体"}[1.2.1.1]{lang="EN-US"}[的设备是否可达]{style="font-family:宋体"}

[[56 data bytes]{lang="EN-US"}]{#struct_0_x5521_61440_x1758873789}

[[每个]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x5521_61440_203234598}[回显请求报文中的数据字节数]{style="font-family:宋体"}

[[56 bytes from 1.2.1.1: seq=0 ttl=128 time=2.243 ms]{lang="EN-US"}]{#struct_0_x5521_61440_781959416}

[[收到]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5521_61440_x846021266}[地址为]{style="font-family:宋体"}[1.2.1.1]{lang="EN-US"}[的设备回复的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[响应报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_x5521_61440_x998996733}[表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[响应报文中数据的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[seq]{lang="EN-US"}]{#struct_0_x5521_61440_x1216278593}[表示报文序号，用来判断报文是否有分组丢失、失序或重复]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ttl]{lang="EN-US"}]{#struct_0_x5521_61440_331765688}[表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[响应报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[time]{lang="EN-US"}]{#struct_0_x5521_61440_x1758808253}[表示响应时间]{style="font-family:宋体"}

[[\-\-- 1.2.1.1 ping statistics \-\--]{lang="EN-US"}]{#struct_0_x5521_61440_332709132}

[[Ping]{lang="EN-US"}]{#struct_0_x5521_61440_392339447}[操作中收发数据的统计结果]{style="font-family:宋体"}

[[5 packets transmitted]{lang="EN-US"}]{#struct_0_x5521_61440_x1032955764}

[[发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x5521_61440_x282018051}[回显请求报文数]{style="font-family:宋体"}

[[5 packets received]{lang="EN-US"}]{#struct_0_x5521_61440_1775607593}

[[收到的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x5521_61440_x1758218429}[响应报文数]{style="font-family:宋体"}

[[0% packet loss]{lang="EN-US"}]{#struct_0_x5521_61440_x1306052877}

[[未响应请求报文占发送的总请求报文的百分比]{style="font-family:宋体"}]{#struct_0_x5521_61440_1230842274}

[[round-trip min/avg/max = 0.717/1.101/2.243 ms]{lang="EN-US"}]{#struct_0_x5521_61440_1105001806}

[[响应时间的最小值、平均值、最大值和标准方差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_x5521_61440_1764006021}

[ ]{lang="EN-US"}

::: {#-263441897 .myid}
[]{#_Toc404782821}[]{#struct_0_x5521_61440_1993609071}[]{#_Toc303347175}

**应急Shell \-- 应急Shell配置命令 \-- ping ipv6**

------------------------------------------------------------------------

[**[ping ipv6]{lang="EN-US"}**]{#struct_0_x5521_61440_x1758152893}[命令用来检查指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址是否可达。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1168069017}

[**[ping ipv6]{lang="EN-US"}**[ \[ **-c** *count* \| **-s** *size* \] \* *ipv6-address*]{lang="EN-US"}]{#struct_0_x5521_61440_x2126961778}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x777645425}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x315400049}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1725092513}

[**[-c]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_x5521_61440_x546628330}[：指定发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[回显请求报文的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-s]{lang="EN-US"}***[ size]{lang="EN-US"}*]{#struct_0_x5521_61440_x2015447450}[：指定发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[回显请求报文的长度，取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[56]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x5521_61440_x192658773}[：目的主机的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_660898192}

[[执行]{style="font-family:宋体"}**[ping]{lang="EN-US"}[ ipv6]{lang="EN-US"}**]{#struct_0_x5521_61440_x1585742940}[命令后，源端会给目的端发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[回显请求报文。在执行命令过程中，键入]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[可终止]{style="font-family:宋体"}**[ping ipv6]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1929730920}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_174450579}[检查到目的端]{style="font-family:宋体"}[2001::2]{lang="EN-US"}[是否可达。]{style="font-family:宋体"}

[[\<boot\> ping ipv6 2001::2]{lang="EN-US"}]{#struct_0_x5521_61440_1908598120}

[ping ipv6 2001::2]{lang="EN-US"}

[PING 2001::2 (2001::2): 56 data bytes]{lang="EN-US"}

[56 bytes from 2001::2: seq=0 ttl=64 time=5.420 ms]{lang="EN-US"}

[56 bytes from 2001::2: seq=1 ttl=64 time=1.140 ms]{lang="EN-US"}

[56 bytes from 2001::2: seq=2 ttl=64 time=2.027 ms]{lang="EN-US"}

[56 bytes from 2001::2: seq=3 ttl=64 time=0.887 ms]{lang="EN-US"}

[56 bytes from 2001::2: seq=4 ttl=64 time=0.791 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- 2001::2 ping statistics \-\--]{lang="EN-US"}

[5 packets transmitted, 5 packets received, 0% packet loss]{lang="EN-US"}

[round-trip min/avg/max = 0.791/2.053/5.420 ms  ]{lang="EN-US"}

[[该命令的显示信息描述表请参见]{style="font-family:宋体"}]{#struct_0_x5521_61440_x192593237}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-6]{lang="EN-US"}](?-1885171420#_Ref198434076)[。]{style="font-family:宋体"}
:::

::: {#-1028371258 .myid}
[]{#_Toc404782822}[]{#struct_0_x5521_61440_x161953740}

**应急Shell \-- 应急Shell配置命令 \-- pwd**

------------------------------------------------------------------------

[**[pwd]{lang="EN-US"}**]{#struct_0_x5521_61440_337477494}[命令用来显示当前工作路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1066467560}

[**[pwd]{lang="EN-US"}**]{#struct_0_x5521_61440_1859724137}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1793502649}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1285971272}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x434511177}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_334458332}[显示当前工作路径。]{style="font-family:宋体"}

[[\<boot\> pwd]{lang="EN-US"}]{#struct_0_x5521_61440_x192527701}

[flash:]{lang="EN-US"}
:::

::: {#-1159706084 .myid}
[]{#_Toc404782823}[]{#struct_0_x5521_61440_x529622367}

**应急Shell \-- 应急Shell配置命令 \-- quit**

------------------------------------------------------------------------

[**[quit]{lang="EN-US"}**]{#struct_0_x5521_61440_73657041}[命令用来从当前视图退回到上一级视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x499051088}

[**[quit]{lang="EN-US"}**]{#struct_0_x5521_61440_x1805078370}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1343194388}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5521_61440_429944651}[管理以太网接口视图]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x891867803}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1485937476}[从管理以太网接口视图退回到用户视图。]{style="font-family:宋体"}

[[\[boot-m-eth0\] quit]{lang="EN-US"}]{#struct_0_x5521_61440_x192462165}

[\[boot\] quit]{lang="EN-US"}

[\<boot\>]{lang="EN-US"}
:::

::: {#772218301 .myid}
[]{#_Toc404782824}[]{#struct_0_x5521_61440_247610613}

**应急Shell \-- 应急Shell配置命令 \-- reboot**

------------------------------------------------------------------------

[**[reboot]{lang="EN-US"}**]{#struct_0_x5521_61440_1958339524}[命令用来重启设备。（集中式设备）]{style="font-family:宋体"}

[**[reboot]{lang="EN-US"}**]{#struct_0_x5521_61440_1088902515}[命令用来重启当前登录的主控板。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[reboot]{lang="EN-US"}**]{#struct_0_x5521_61440_x473395946}[命令用来重启当前登录的成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_682582003}

[**[reboot]{lang="EN-US"}**]{#struct_0_x5521_61440_986060646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1829907662}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1258242528}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x192920917}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x110680437}[重启设备。（集中式设备）]{style="font-family:宋体"}

[[\<boot\> reboot]{lang="EN-US"}]{#struct_0_x5521_61440_x233057572}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_203719643}[重启当前登录的主控板。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<boot\> reboot]{lang="EN-US"}]{#struct_0_x5521_61440_117776128}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x1829584893}[重启当前登录的成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<boot\> reboot]{lang="EN-US"}]{#struct_0_x5521_61440_x1680190869}
:::

::: {#34334169 .myid}
[]{#_Toc404782825}[]{#struct_0_x5521_61440_x936914401}

**应急Shell \-- 应急Shell配置命令 \-- reset ssh public-key**

------------------------------------------------------------------------

[**[reset ssh public-key]{lang="EN-US"}**]{#struct_0_x5521_61440_6230156}[命令用来清除保存在本设备的所有]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的公钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x192855381}

[**[reset ssh public-key]{lang="EN-US"}**]{#struct_0_x5521_61440_1378387074}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1702919216}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x1749402572}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x565068568}

[[在设备上使用]{style="font-family:宋体"}**[ssh2]{lang="EN-US"}**]{#struct_0_x5521_61440_1809087365}[命令首次登录]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器时，设备会将该服务器的公钥保存到本地，以便下次登录进行身份认证时使用。如果]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的公钥变更，因为新旧公钥不一致，会导致设备再次]{style="font-family:宋体"}[SSH]{lang="EN-US"}[登录该服务器失败。此时可使用]{style="font-family:宋体"}**[reset ssh public-key]{lang="EN-US"}**[命令来清除原公钥，重新执行]{style="font-family:宋体"}**[ssh2]{lang="EN-US"}**[命令触发新的]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x206667327}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x1866903693}[清除保存在本设备的所有]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的公钥。]{style="font-family:宋体"}

[[\<boot\> ssh2 192.168.1.59]{lang="EN-US"}]{#struct_0_x5521_61440_x192789845}

[login as:client001]{lang="EN-US"}

[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]{lang="EN-US"}

[@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @]{lang="EN-US"}

[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]{lang="EN-US"}

[IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!]{lang="EN-US"}

[Someone could be eavesdropping on you right now (man-in-the-middle attack)!]{lang="EN-US"}

[It is also possible that a host key has just been changed.]{lang="EN-US"}

[The fingerprint for the RSA key sent by the remote host is]{lang="EN-US"}

[83:2d:b6:90:4a:1b:0e:c1:ea:af:09:3a:65:09:8a:b3.]{lang="EN-US"}

[Please contact your system administrator.]{lang="EN-US"}

[RSA host key for 192.168.1.59 has changed and you have requested strict checking]{lang="EN-US"}

[.]{lang="EN-US"}

[Host key verification failed.]{lang="EN-US"}

[\<boot\> reset ssh public-key]{lang="EN-US"}

[\<boot\> ssh2 192.168.1.59]{lang="EN-US"}

[login as:client001]{lang="EN-US"}

[The authenticity of host \'192.168.1.59 (192.168.1.59)\' can\'t be established.]{lang="EN-US"}

[RSA key fingerprint is 83:2d:b6:90:4a:1b:0e:c1:ea:af:09:3a:65:09:8a:b3.]{lang="EN-US"}

[Are you sure you want to continue connecting (yes/no)? yes]{lang="EN-US"}

[Warning: Permanently added \'192.168.1.59\' (RSA) to the list of known hosts.]{lang="EN-US"}

[client001@192.168.1.59\'s password:]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  ]{lang="EN-US"}

[\* Copyright (c) 2004-2012 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*  ]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*  ]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*  ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname.59\>]{lang="EN-US"}
:::

::: {#-1201142008 .myid}
[]{#_Toc404782826}[]{#struct_0_x5521_61440_x192724309}

**应急Shell \-- 应急Shell配置命令 \-- rmdir**

------------------------------------------------------------------------

[**[rmdir]{lang="EN-US"}**]{#struct_0_x5521_61440_x168757068}[命令用来删除已有目录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1707037090}

[**[rmdir]{lang="EN-US"}**[ *directory*]{lang="EN-US"}]{#struct_0_x5521_61440_x10059341}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_23559337}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_311736089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x637010869}

[*[directory]{lang="EN-US"}*]{#struct_0_x5521_61440_x1131748948}[：待删除的目录名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_188621240}

[[被删除的目录必须为空目录。即删除目录前，必须先删除该目录下的所有文件及子目录，文件的删除请参见]{style="font-family:宋体"}**[delete]{lang="EN-US"}**]{#struct_0_x5521_61440_x192134485}[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_634845190}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x2050909592}[删除目录]{style="font-family:宋体"}[mydir]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> rmdir flash:/mydir]{lang="EN-US"}]{#struct_0_x5521_61440_x1260508913}

[Remove directory flash:/mydir?\[Y/N\]:y]{lang="EN-US"}

[Directory flash:/1 removed.  ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1280672056}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[delete]{lang="EN-US"}**]{#struct_0_x5521_61440_1955860360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dir]{lang="EN-US"}**]{#struct_0_x5521_61440_x161537009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mkdir]{lang="EN-US"}**]{#struct_0_x5521_61440_1101484386}
:::

::: {#1170655049 .myid}
[]{#_Toc404782827}[]{#struct_0_x5521_61440_380892634}

**应急Shell \-- 应急Shell配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x5521_61440_x192068949}[命令用来关闭管理以太网接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x5521_61440_x475955099}[命令用来打开管理以太网接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_548495550}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x5521_61440_1834396782}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x5521_61440_x1205785600}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1846088444}

[[管理以太网接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_x5521_61440_x192658772}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_660963728}

[[管理以太网接口视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1194156807}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1038204476}

[[当管理以太网接口异常时，可通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_x5521_61440_x1725844003}[命令关闭此接口，然后再通过]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令重新打开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1591610126}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1256347752}[关闭管理以太网接口。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_x192593236}

[\[boot\] interface m-eth0]{lang="EN-US"}

[\[boot-m-eth0\] shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x161888204}[打开管理以太网接口。]{style="font-family:宋体"}

[[\[boot-m-eth0\] undo shutdown]{lang="EN-US"}]{#struct_0_x5521_61440_x809141008}
:::

::: {#1438963071 .myid}
[]{#_Toc404782828}[]{#struct_0_x5521_61440_562259322}

**应急Shell \-- 应急Shell配置命令 \-- ssh2**

------------------------------------------------------------------------

[**[ssh2]{lang="EN-US"}**]{#struct_0_x5521_61440_x1027440365}[命令用来使用]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议登录到]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1111155594}

[**[ssh2 ]{lang="EN-US"}**[{ *server-ipv4-address \|* **ipv6** *server-ipv6-address* }]{lang="EN-US"}]{#struct_0_x5521_61440_922007493}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1802862333}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1765161389}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x192527700}

[*[server-ipv4-address]{lang="EN-US"}*]{#struct_0_x5521_61440_x529687903}[：]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *server-ipv6-address*]{lang="EN-US"}]{#struct_0_x5521_61440_1595510014}[：]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x164538360}

[[如果在登录过程中，]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_x5521_61440_531397711}[服务器长时间没有响应，用户可以使用]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}[组合键中断本次]{style="font-family:宋体"}[SSH]{lang="EN-US"}[登录，稍后再试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1847027638}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x937624368}[使用]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议第一次登录到]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.1.59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> ssh2 192.168.1.59]{lang="EN-US"}]{#struct_0_x5521_61440_x192462164}

[login as:client001]{lang="EN-US"}

[The authenticity of host \'192.168.1.59 (192.168.1.59)\' can\'t be established.]{lang="EN-US"}

[RSA key fingerprint is 3d:ee:1f:f9:81:be:4f:aa:42:88:1c:ab:81:4e:95:6f.]{lang="EN-US"}

[Are you sure you want to continue connecting (yes/no)? yes]{lang="EN-US"}

[Warning: Permanently added \'192.168.1.59\' (RSA) to the list of known hosts.]{lang="EN-US"}

[client001@192.168.1.59\'s password:]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  ]{lang="EN-US"}

[\* Copyright (c) 2004-2012 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*  ]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*  ]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*  ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  ]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[\<Syaname.59\>]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_247545077}[使用]{style="font-family:宋体"}[SSH]{lang="EN-US"}[协议再次登录到]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.1.59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> ssh2 192.168.1.59]{lang="EN-US"}]{#struct_0_x5521_61440_x238343927}

[login as:client001]{lang="EN-US"}

[client001@192.168.1.59\'s password:]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  ]{lang="EN-US"}

[\* Copyright (c) 2004-2012 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*  ]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*  ]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*  ]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  ]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[\<Syaname.59\>]{lang="EN-US"}
:::

::: {#1057508062 .myid}
[]{#_Toc404782829}[]{#struct_0_x5521_61440_x192920916}

**应急Shell \-- 应急Shell配置命令 \-- system-view**

------------------------------------------------------------------------

[**[system-view]{lang="EN-US"}**]{#struct_0_x5521_61440_x110745973}[命令用来从用户视图进入系统视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_946024592}

[[system-view]{lang="EN-US"}]{#struct_0_x5521_61440_x103565157}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1286457265}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_x192855380}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1378452610}

[[应急]{style="font-family:宋体"}[Shell]{lang="EN-US"}]{#struct_0_x5521_61440_978525624}[启动后直接进入用户视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x73433483}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_804130786}[从用户视图进入系统视图。]{style="font-family:宋体"}

[[\<boot\> system-view]{lang="EN-US"}]{#struct_0_x5521_61440_1676875451}

[\[boot\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_659067348}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[quit]{lang="EN-US"}**]{#struct_0_x5521_61440_x1831216088}
:::

::: {#-377527709 .myid}
[]{#_Toc404782830}[]{#struct_0_x5521_61440_x192789844}

**应急Shell \-- 应急Shell配置命令 \-- telnet**

------------------------------------------------------------------------

[**[telnet]{lang="EN-US"}**]{#struct_0_x5521_61440_x1260778287}[命令用来使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[协议登录到]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_196218762}

[**[telnet]{lang="EN-US"}**[ { *server-ipv4-address \|* **ipv6** *server-ipv6-address* }]{lang="EN-US"}]{#struct_0_x5521_61440_721454056}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x52106494}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_1867132419}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1091124452}

[*[server-ipv4-address]{lang="EN-US"}*]{#struct_0_x5521_61440_1358506751}[：]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[*[server-ipv6-address]{lang="EN-US"}*]{#struct_0_x5521_61440_x1053923127}[：]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x192724308}

[[如果在登录过程中，]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_x5521_61440_x168822604}[服务器长时间没有响应，用户可以使用]{style="font-family:宋体"}[\<Ctrl+K\>]{lang="EN-US"}[组合键中断本次]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录，稍后再试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x180942082}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_627399713}[使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[协议登录到]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.100.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> telnet 192.168.100.1]{lang="EN-US"}]{#struct_0_x5521_61440_x776839379}
:::

::: {#-1155661038 .myid}
[]{#_Toc404782831}[]{#struct_0_x5521_61440_x297473650}

**应急Shell \-- 应急Shell配置命令 \-- tftp**

------------------------------------------------------------------------

[**[tftp]{lang="EN-US"}**]{#struct_0_x5521_61440_x287717289}[命令用来访问]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1629707546}

[**[tftp]{lang="EN-US"}**[ *server-ipv4-address* { **get** *remote-file local-file* \| **put** *local-file* *remote-file* }]{lang="EN-US"}]{#struct_0_x5521_61440_x1028803507}

[**[tftp ipv6]{lang="EN-US"}**[ *server-ipv6-address* { **get** *remote-file local-file* \| **put** *local-file* *remote-file* }]{lang="EN-US"}]{#struct_0_x5521_61440_x192134484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5521_61440_634910726}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5521_61440_342482667}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x1365622599}

[*[server-ipv4-address]{lang="EN-US"}*]{#struct_0_x5521_61440_x1197399832}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，点分十进制格式。]{style="font-family:宋体"}

[*[server-ipv6-address]{lang="EN-US"}*]{#struct_0_x5521_61440_889843500}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[get ]{lang="EN-US"}***[remote-file]{lang="EN-US"}*[ *local-file*]{lang="EN-US"}]{#struct_0_x5521_61440_512348067}[：表示从]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上下载一个文件到本地，]{style="font-family:宋体"}*[remote-file]{lang="EN-US"}*[表示]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上的文件的名称，]{style="font-family:宋体"}*[local-file]{lang="EN-US"}*[表示本地的文件的名称。]{style="font-family:宋体"}

[**[put ]{lang="EN-US"}***[local-file]{lang="EN-US"}*[ *remote-file*]{lang="EN-US"}]{#struct_0_x5521_61440_376120165}[：表示从本地上传一个文件到]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器，]{style="font-family:宋体"}*[local-file]{lang="EN-US"}*[表示本地的文件的名称，]{style="font-family:宋体"}*[remote-file]{lang="EN-US"}*[表示]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上的文件的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5521_61440_1096990623}

[[当网络拥塞，文件传输速度很慢的时候，用户可以使用]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_x5521_61440_x192068948}[组合键中断本次]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[操作，稍后再试。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5521_61440_x476020635}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_1571750300}[从]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.1.100]{lang="EN-US"}[上下载文件]{style="font-family:宋体"}[111.txt]{lang="EN-US"}[，保存到本地时使用的文件名为]{style="font-family:宋体"}[222.txt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> tftp 192.168.1.100 get 111.txt flash:/222.txt]{lang="EN-US"}]{#struct_0_x5521_61440_x1753729883}

[[\# ]{lang="EN-US"}]{#struct_0_x5521_61440_x2134509129}[将设备的启动配置文件]{style="font-family:宋体"}[startup.cfg]{lang="EN-US"}[上传到]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.1.100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<boot\> tftp 192.168.1.100 put flash:/startup.cfg startup.cfg]{lang="EN-US"}]{#struct_0_x5521_61440_100712608}
:::
