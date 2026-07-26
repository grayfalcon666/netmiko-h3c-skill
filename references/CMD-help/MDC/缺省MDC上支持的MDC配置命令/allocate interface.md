::: {#1546310888 .myid}
[]{#_Toc404783229}[]{#struct_0_11418_x2016_x1367067517}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- allocate interface**

------------------------------------------------------------------------

[**[allocate interface]{lang="EN-US"}**]{#struct_0_11418_x2016_x134550932}[命令用来为]{style="font-family:宋体"}[MDC]{lang="EN-US"}[分配物理接口。]{style="font-family:宋体"}

[**[undo allocate interface]{lang="EN-US"}**]{#struct_0_11418_x2016_1596383859}[命令用来将接口从]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1824261375}

[**[allocate interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-list]{lang="EN-US"}*]{#struct_0_11418_x2016_1359078955}

[**[undo allocate interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_11418_x2016_1571867116}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1373556236}

[[物理设备上的所有接口都属于缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x575672315}[，不属于任何非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x50861065}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x791613016}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x439170922}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_1568989710}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x1240522138}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x999876734}

[*[interface-list]{lang="EN-US"}*]{#struct_0_11418_x2016_x580871390}[：接口列表，表示给]{style="font-family:宋体"}[MDC]{lang="EN-US"}[分配接口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ ]{lang="EN-US"}[＝]{style="font-family:宋体"}[ { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-24\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}[&\<1-24\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[24]{lang="EN-US"}[次。]{style="font-family:宋体"}[当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字指定接口范围时（形如]{style="font-family:宋体"}*[interface-type interface-number1]{lang="EN-US"}*[ **to** *interface-type interface-number2*]{lang="EN-US"}[），则]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字左边[的接口（起始接口）和]{style="color:black"}]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字右边的接口（结束接口）]{style="font-family:宋体;color:black"}[类型必须相同，并且处于同一接口板上，否则将配置失败]{style="font-family:
宋体"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1373621772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将]{style="font-family:宋体"}]{#struct_0_11418_x2016_216121379}[IRF]{lang="EN-US"}[中某成员设备上的接口分配给]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的时候，请确保该成员设备上缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中至少要保留一个处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口，否则，会导致]{style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[物理设备的]{style="font-family:宋体"}]{#struct_0_11418_x2016_347186403}[Console]{lang="EN-US"}[口和]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口被缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[独享，不能分配给非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[物理设备的管理以太网口不能分配。缺省]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1558119034}[MDC]{lang="EN-US"}[上始终有管理以太网口，非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的管理以太网口在]{style="font-family:宋体"}[MDC]{lang="EN-US"}[创建时由系统自动创建。不同]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的管理以太网口名称和编号相同，共用物理设备上的同一个物理接口和物理链路，可以配置同网段或者不同网段的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，以便不同]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的管理员登录自己的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个物理接口只能属于一台]{style="font-family:宋体"}]{#struct_0_11418_x2016_x503174422}[MDC]{lang="EN-US"}[。物理接口分配给]{style="font-family:宋体"}[MDC]{lang="EN-US"}[后，需要登录该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[后，才能对接口下的参数进行配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次使用]{lang="EN-US" style="font-family:宋体"}**[allocate interface]{lang="EN-US"}**]{#struct_0_11418_x2016_x1187134644}[命令]{lang="EN-US" style="font-family:
宋体"}[可以]{style="font-family:宋体"}[给同一]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[分配]{lang="EN-US" style="font-family:宋体"}[多个]{style="font-family:宋体"}[接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于硬件限制，某些接口板上的接口是按组划分的，每个组里包含几个接口。此时，请一次性将这组接口分配给某一]{style="font-family:宋体"}]{#struct_0_11418_x2016_535791754}[MDC]{lang="EN-US"}[，而不能只分配这组接口中的部分接口。接口是否按组划分以及哪些接口分为一组与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[物理接口只能从缺省]{style="font-family:宋体"}]{#struct_0_11418_x2016_692708037}[MDC]{lang="EN-US"}[分配到非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。当某接口属于]{style="font-family:宋体"}[MDC A]{lang="EN-US"}[，要分配到]{style="font-family:宋体"}[MDC B]{lang="EN-US"}[时，需要先使用]{style="font-family:宋体"}**[undo allocate interface]{lang="EN-US"}**[命令，将该接口归还给缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，再使用]{style="font-family:宋体"}**[allocate interface]{lang="EN-US"}**[命令分配给]{style="font-family:宋体"}[MDC B]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将物理接口分配给]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1655302566}[MDC]{lang="EN-US"}[或者从]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中删除时，该接口下的所有配置都会恢复到缺省情况。]{style="font-family:宋体"}

[[请确保缺省]{style="font-family:宋体"}]{#struct_0_11418_x2016_x668903936}[MDC]{lang="EN-US"}[和非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[用户对同一个接口的操作时序，在缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[用户分配或删除接口时及时通知非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[用户，让其停止配置该接口，否则可能导致接口达不到非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[用户预期的配置效果。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将]{style="font-family:宋体"}]{#struct_0_11418_x2016_1373163020}[IRF]{lang="EN-US"}[物理端口分配给其]{style="font-family:宋体"}[它]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[或者从当前]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[中删]{lang="EN-US" style="font-family:宋体"}[除时，必须先执行]{style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令恢复到缺省情况，再执行分配或者删除操作，最后执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令保存当前配置文件。有关]{style="font-family:宋体"}**[undo port group interface]{lang="EN-US"}**[命令的详细使用，请参见"]{style="font-family:宋体"}[IRF]{lang="EN-US"}[命令参考"中的"]{style="font-family:宋体"}[IRF]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x950949503}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x325770453}[将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[分配给]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_901972344}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] allocate interface gigabitethernet 1/0/1 gigabitethernet1/0/3]{lang="EN-US"}

[[Configuration of the interfaces will be lost. Continue? \[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1719876353}[将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/8]{lang="EN-US"}[分配给]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_1320944534}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] allocate interface gigabitethernet 1/0/1 to gigabitethernet 1/0/8]{lang="EN-US"}

[Configuration of the interfaces will be lost. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1923522484}[将接口]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[分配给]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_1373228556}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] allocate interface gigabitethernet 1/0/4]{lang="EN-US"}

[Configuration of the interfaces will be lost. Continue? \[Y/N\]:y]{lang="EN-US"}

[Group error: all interfaces of one group must be allocated to the same mdc.]{lang="EN-US"}

[  GigabitEthernet1/0/4]{lang="EN-US"}

[ ]{lang="EN-US"}

[Port list of group 2:]{lang="EN-US"}

[  GigabitEthernet1/0/3               GigabitEthernet1/0/4]{lang="EN-US"}

[[以上提示信息表明]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}]{#struct_0_11418_x2016_x1324117900}[必须和]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[一起分配给同一个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。执行如下命令，将]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[一起分配给]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[：]{style="font-family:宋体"}

[[\[Sysname-mdc-2-sub1\] allocate interface gigabitethernet 1/0/3 gigabitethernet 1/0/4]{lang="EN-US"}]{#struct_0_11418_x2016_x1956326224}

[Configuration of the interfaces will be lost. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#1505521113 .myid}
[]{#_Toc404783230}[]{#struct_0_11418_x2016_x1454000049}[]{#_Toc315942677}[]{#_Toc315942678}[]{#_Toc315942679}[]{#_Toc315942680}[]{#_Toc315942681}[]{#_Toc315942682}[]{#_Toc315942683}[]{#_Toc315942684}[]{#_Toc315942685}[]{#_Toc315942686}[]{#_Toc315942687}[]{#_Toc315942688}[]{#_Toc315942689}[]{#_Toc315942690}[]{#_Toc315942691}[]{#_Toc315942692}[]{#_Toc315942693}[]{#_Toc315942694}[]{#_Toc315942695}[]{#_Toc315942696}[]{#_Toc315942697}[]{#_Toc315942698}[]{#_Toc315942699}[]{#_Toc315942700}[]{#_Toc315942701}[]{#_Toc315942702}[]{#_Toc315942703}[]{#_Toc315942704}[]{#_Toc315942705}[]{#_Toc315942706}[]{#_Toc315942707}[]{#_Toc315942708}[]{#_Toc315942709}[]{#_Toc315942710}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- display mdc**

------------------------------------------------------------------------

[**[display mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x431685539}[命令用来显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关信息，包括]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的编号、名称和状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1382652875}

[**[display mdc ]{lang="EN-US"}**[\[ **name** ]{lang="EN-US"}*[mdc-name ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_11418_x2016_x765620749}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1906237047}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_1373294092}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1380251732}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_239061664}

[[network-operator]{lang="EN-US"}]{#struct_0_11418_x2016_x1324272216}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_1067244415}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_1746871929}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1719355542}

[**[name]{lang="EN-US"}***[ mdc-name]{lang="EN-US"}*]{#struct_0_11418_x2016_x446617299}[：显示指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}*[mdc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。不指定该参数时，显示所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x971912560}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x957289452}[显示所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display mdc]{lang="EN-US"}]{#struct_0_11418_x2016_1373359628}

[ID         Name            Status]{lang="EN-US"}

[1          Admin           active]{lang="EN-US"}

[2          sub1            inactive]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mdc]{lang="EN-US"}]{#struct_0_11418_x2016_x2090198087}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2014513540}[[字段]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1463040709}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11418_x2016_989538759}

[[ID]{lang="EN-US"}]{#struct_0_11418_x2016_2008148860}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1562068006}[的编号]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_11418_x2016_x1823858821}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1373949452}[的名称]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_11418_x2016_x1700849038}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1789046448}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_11418_x2016_1391940245}[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于未启动状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starting]{lang="EN-US"}]{#struct_0_11418_x2016_x159950966}[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[正在启动中，即对]{style="font-family:宋体"}[MDC]{lang="EN-US"}[正在执行]{style="font-family:宋体"}**[mdc start]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_11418_x2016_1345057512}[表示]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[正常运行]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[updating]{lang="EN-US"}]{#struct_0_11418_x2016_1820589262}[表示正在给]{style="font-family:宋体"}[MDC]{lang="EN-US"}[分配接口板，即对]{style="font-family:宋体"}[MDC]{lang="EN-US"}[执行]{style="font-family:宋体"}**[location]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stopping]{lang="EN-US"}]{#struct_0_11418_x2016_1374014988}[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[正在停止，即]{style="font-family:宋体"}[MDC]{lang="EN-US"}[正在执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **mdc start**]{lang="EN-US"}[命令]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1071315093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x1620384875}

::: {#-1896667081 .myid}
[]{#_Toc404783231}[]{#struct_0_11418_x2016_x1054939198}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- display mdc interface**

------------------------------------------------------------------------

[**[display mdc interface]{lang="EN-US"}**]{#struct_0_11418_x2016_x1116940598}[命令用来显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1141562745}

[**[display mdc ]{lang="EN-US"}**[\[ **name** *mdc-name* \] **interface**]{lang="EN-US"}]{#struct_0_11418_x2016_923401635}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1661553008}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_1373425165}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x2135649710}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_752338686}

[[network-operator]{lang="EN-US"}]{#struct_0_11418_x2016_1311125704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x1938857257}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_x1375548620}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_2023688822}

[**[name]{lang="EN-US"}***[ mdc-name]{lang="EN-US"}*]{#struct_0_11418_x2016_x966538121}[：显示指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}*[mdc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。不指定该参数时，显示所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1685290059}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1412532296}[显示所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[\<Sysname\> display mdc interface]{lang="EN-US"}]{#struct_0_11418_x2016_1373490701}

[ MDC Admin\'s interface(s):]{lang="EN-US"}

[  M-Ethernet1/0/1                    Fc0/2/7]{lang="EN-US"}

[  FortyGigE0/1/8                     GigabitEthernet1/0/2]{lang="EN-US"}

[  GigabitEthernet1/0/3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ MDC sub1\'s interface(s):]{lang="EN-US"}

[  GigabitEthernet1/0/4                Ten-GigabitEthernet1/1/5]{lang="EN-US"}

[  Ten-GigabitEthernet1/1/6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1367133053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[allocate interface]{lang="EN-US"}**]{#struct_0_11418_x2016_2014569666}
:::

::: {#-163657031 .myid}
[]{#_Toc404783232}[]{#struct_0_11418_x2016_x709351162}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- display mdc resource**

------------------------------------------------------------------------

[**[display mdc resource]{lang="EN-US"}**]{#struct_0_11418_x2016_1379165621}[命令用来显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_963220151}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11418_x2016_x842285494}

[**[display mdc ]{lang="EN-US"}**[\[ **name** *mdc-name* \] **resource** \[ **cpu** \| **disk** \| **memory[ ]{style="color:red"}**\]]{lang="EN-US"}]{#struct_0_11418_x2016_1373556237}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11418_x2016_x575737851}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mdc ]{lang="EN-US"}**[\[ **name** *mdc-name* \] **resource** \[ **cpu** \| **disk** \| **memory[ ]{style="color:red"}**\] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11418_x2016_x36091477}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11418_x2016_1766978576}[模式：]{style="font-family:宋体"}

[**[display mdc ]{lang="EN-US"}**[\[ **name** *mdc-name* \] **resource** \[ **cpu** \| **disk** \| **memory** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11418_x2016_1502653905}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1604955916}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_1137469896}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1006519515}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x2145829701}

[[network-operator]{lang="EN-US"}]{#struct_0_11418_x2016_1373621773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_216186915}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_x791669237}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_736365810}

[**[name]{lang="EN-US"}***[ mdc-name]{lang="EN-US"}*]{#struct_0_11418_x2016_910267464}[：显示指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。]{style="font-family:宋体"}*[mdc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。不指定该参数时，显示所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_11418_x2016_1446187960}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用情况。]{style="font-family:宋体"}

[**[disk]{lang="EN-US"}**]{#struct_0_11418_x2016_x566035278}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的磁盘使用情况。]{style="font-family:宋体"}

[**[memory]{lang="EN-US"}**]{#struct_0_11418_x2016_55994213}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的内存使用情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_395629525}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定单板上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_1373163021}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定成员设备上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x950883967}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定成员设备指定单板上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x2064864322}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1709610298}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_1378493360}[显示所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display mdc resource]{lang="EN-US"}]{#struct_0_11418_x2016_1373228557}

[Memory usage:]{lang="EN-US"}

[Slot 0 CPU 0:]{lang="EN-US"}

[Used 207.2MB, Free 288.7MB, Total 495.9MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Available(MB)]{lang="EN-US"}

[  1     Admin            495.9        172.1        288.7]{lang="EN-US"}

[  2     sub1             495.9        17.9         288.7]{lang="EN-US"}

[  3     sub2             495.9        17.2         288.7]{lang="EN-US"}

[CPU usage:]{lang="EN-US"}

[Slot 0 CPU 0:]{lang="EN-US"}

[  ID    Name             Weight       Usage(%)]{lang="EN-US"}

[  1     Admin            10           1]{lang="EN-US"}

[  2     sub1             10           0]{lang="EN-US"}

[  3     sub2             10           0]{lang="EN-US"}

[Disk usage:]{lang="EN-US"}

[Slot 0 CPU 0:]{lang="EN-US"}

[flash: Used 0.7MB, Free 461.2MB, Total 461.9MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)     Available(MB)]{lang="EN-US"}

[  1     Admin            461.9        0.5          461.2]{lang="EN-US"}

[  2     sub1             461.9        0.1          461.2]{lang="EN-US"}

[  3     sub2             461.9        0.1          461.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x2064995394}[显示所有单板上]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display mdc resource]{lang="EN-US"}]{#struct_0_11418_x2016_x2064929858}

[Memory usage:]{lang="EN-US"}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[Used 238.1MB, Free 249.3MB, Total 487.4MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  1     Admin            487.4        206.0       249.3]{lang="EN-US"}

[  2     MyDevice         487.4        32.1        249.3]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[Used 218.3MB, Free 270.1MB, Total 487.4MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  1     Admin            487.4        188.2       270.1]{lang="EN-US"}

[  2     MyDevice         487.4        30.1        270.1]{lang="EN-US"}

[CPU usage:]{lang="EN-US"}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[  ID    Name             Weight       Usage(%)]{lang="EN-US"}

[  1     Admin            10           24]{lang="EN-US"}

[  2     MyDevice         10           0   ]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[  ID    Name             Weight       Usage(%)]{lang="EN-US"}

[  1     Admin            10           24]{lang="EN-US"}

[  2     MyDevice         10           0]{lang="EN-US"}

[Disk usage:]{lang="EN-US"}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[cfa0: Used 83.4MB, Free 163.1MB, Total 246.5MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  1     Admin            221.9        83.4        138.5]{lang="EN-US"}

[  2     MyDevice         46.3         0.1         46.2]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[cfa0: Used 44.8MB, Free 201.7MB, Total 246.5MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  1     Admin            410.5        44.8        201.7]{lang="EN-US"}

[  2     MyDevice         40           0.0         40]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mdc resource]{lang="EN-US"}]{#struct_0_11418_x2016_x1071380629}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2021492504}[[字段]{style="font-family:黑体"}]{#struct_0_11418_x2016_136979008}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355458187}

[[Memory usage]{lang="EN-US"}]{#struct_0_11418_x2016_x106974049}

[[表示下面显示的是内存的使用情况]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1931492305}

[[CPU usage]{lang="EN-US"}]{#struct_0_11418_x2016_634286008}

[[表示下面显示的是]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_11418_x2016_x1193662639}[的使用情况]{style="font-family:宋体"}

[[Disk usage]{lang="EN-US"}]{#struct_0_11418_x2016_623216268}

[[表示下面显示的是磁盘的使用情况]{style="font-family:宋体"}]{#struct_0_11418_x2016_1374216307}

[[Slot 0 CPU 0]{lang="EN-US"}]{#struct_0_11418_x2016_x1355392651}

[[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_899312186}[在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上资源的使用情况（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis 1 slot 0 CPU 0]{lang="EN-US"}]{#struct_0_11418_x2016_x2065192002}

[[表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x992831380}[在指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上资源的使用情况（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Used 238.1MB, Free 249.3MB, Total 487.4MB]{lang="EN-US"}]{#struct_0_11418_x2016_2064827649}

[[内存的使用情况，]{style="font-family:宋体"}[Used]{lang="EN-US"}]{#struct_0_11418_x2016_1442870916}[表示内存已使用空间的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Free]{lang="EN-US"}[表示当前空闲内存的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Total]{lang="EN-US"}[表示整个内存大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Cfa0:: Used 0,  Free 61, Total 61]{lang="EN-US"}]{#struct_0_11418_x2016_x316063027}

[[Cfa0]{lang="EN-US"}]{#struct_0_11418_x2016_x1355261579}[表示磁盘的名称，]{style="font-family:宋体"}[Used]{lang="EN-US"}[表示整个磁盘已使用空间的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Free]{lang="EN-US"}[表示整个磁盘当前空闲空间的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Total]{lang="EN-US"}[表示整个磁盘空间大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ID]{lang="EN-US"}]{#struct_0_11418_x2016_346049196}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1842004075}[的编号]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_11418_x2016_1622700399}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1733243781}[的名称]{style="font-family:宋体"}

[[Weight]{lang="EN-US"}]{#struct_0_11418_x2016_x1355720331}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x723860038}[使用]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的权重值]{style="font-family:宋体"}

[[Usage(%)]{lang="EN-US"}]{#struct_0_11418_x2016_x433782306}

[[指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x339686420}[对指定单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的实际占用率（用百分比表示）]{style="font-family:宋体"}

[[Quota(MB)]{lang="EN-US"}]{#struct_0_11418_x2016_364312989}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1355654795}[使用磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存的限制值，单位]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Used(MB)]{lang="EN-US"}]{#struct_0_11418_x2016_1421855595}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1272108302}[当前已使用的磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存空间的大小，单位]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Available(MB)]{lang="EN-US"}]{#struct_0_11418_x2016_x1893494768}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_409494300}[还可以使用的磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存空间的大小，单位]{style="font-family:宋体"}[MB]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#305021740 .myid}
[]{#_Toc404783233}[]{#struct_0_11418_x2016_x55188336}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- limit-resource cpu**

------------------------------------------------------------------------

[**[limit-resource cpu]{lang="EN-US"}**]{#struct_0_11418_x2016_x1355589259}[命令用来配置]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重。]{style="font-family:宋体"}

[**[undo limit-resource cpu]{lang="EN-US"}**]{#struct_0_11418_x2016_x34253677}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1558402448}

[**[limit-resource cpu]{lang="EN-US"}**[ **weight** *weight-value*]{lang="EN-US"}]{#struct_0_11418_x2016_x826918062}

[**[undo]{lang="EN-US"}**[ **limit-resource cpu**]{lang="EN-US"}]{#struct_0_11418_x2016_833726095}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11418_x2016_902901475}

[[各]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_605060863}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重均为]{style="font-family:宋体"}[10]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[各]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x600069315}[在所有成员设备上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重均为]{style="font-family:宋体"}[10]{lang="EN-US"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x214038031}[在所有单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重均为]{style="font-family:宋体"}[10]{lang="EN-US"}[（不能修改）。非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在所有具有使用权限的单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重均为]{style="font-family:宋体"}[10]{lang="EN-US"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1509914258}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1355523723}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x2024547192}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_654813108}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x1771005294}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x565152518}

[**[weight ]{lang="EN-US"}***[weight-value]{lang="EN-US"}*]{#struct_0_11418_x2016_x977532427}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在指定单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x2105873516}

[[系统根据]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x896067027}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重为]{style="font-family:宋体"}[MDC]{lang="EN-US"}[分配]{style="font-family:宋体"}[CPU]{lang="EN-US"}[资源。比如当系统]{style="font-family:宋体"}[CPU]{lang="EN-US"}[较忙时，]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[运行都需要占用较多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，且其权重分别为]{style="font-family:宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[，则系统为第一个]{style="font-family:
宋体"}[MDC]{lang="EN-US"}[分配的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时间和为第二个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[分配的时间近似都是为第三个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[分配的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时间的]{style="font-family:宋体"}[2]{lang="EN-US"}[倍，此时和配置权重值分别为]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[1]{lang="EN-US"}[效果一致。]{style="font-family:宋体"}

[[配置本命令后，]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1260611106}[在主控板和自己拥有的接口板上都将获得相同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重。]{style="font-family:宋体"}[MDC]{lang="EN-US"}[拥有的接口板需要通过]{style="font-family:宋体"}**[location]{lang="EN-US"}**[命令来分配。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[配置本命令后，]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1354933899}[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[所有成员设备上都将获得相同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1367463675}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_1554764707}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_642470467}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] limit-resource cpu weight 2]{lang="EN-US"}
:::

::: {#-1683769703 .myid}
[]{#_Toc404783234}[]{#struct_0_11418_x2016_1770865381}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- limit-resource disk**

------------------------------------------------------------------------

[**[limit-resource disk]{lang="EN-US"}**]{#struct_0_11418_x2016_807375319}[命令用来配置]{style="font-family:宋体"}[MDC]{lang="EN-US"}[可使用的磁盘空间上限（用百分比表示）。]{style="font-family:宋体"}

[**[undo limit-resource disk]{lang="EN-US"}**]{#struct_0_11418_x2016_1343931167}[命令用来恢复到缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x31475892}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1354868363}

[**[limit-resource disk ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_x257180487}

[**[undo limit-resource disk]{lang="EN-US"}**]{#struct_0_11418_x2016_856814078}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11418_x2016_710897019}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[limit-resource disk slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] **ratio** *limit-ratio*]{lang="EN-US"}]{#struct_0_11418_x2016_x1319761082}

[**[undo limit-resource disk]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_11418_x2016_x1681015523}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11418_x2016_x852142405}[模式：]{style="font-family:宋体"}

[**[limit-resource disk chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **ratio** *limit-ratio*]{lang="EN-US"}]{#struct_0_11418_x2016_x977270576}

[**[undo limit-resource disk]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_11418_x2016_x1319370282}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x785666484}

[[所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1355458186}[共享物理设备上的所有磁盘空间，每个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[可使用的磁盘空间上限为空闲磁盘空间值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1459109892}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1250383144}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1518942369}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_1707654822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x49154543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1646165034}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1285060763}[：表示主控板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_905843154}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1355392650}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_11418_x2016_x2064798789}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_x1829571169}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[最多可使用的磁盘空间大小与设备整个磁盘空间大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_768382181}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在指定单板上最多可使用的磁盘空间大小与该单板整个磁盘空间大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_x461909105}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在指定成员设备上最多可使用的磁盘空间大小与该成员设备整个磁盘空间大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x860229268}

[[执行]{style="font-family:宋体"}**[limit-resource disk]{lang="EN-US"}**]{#struct_0_11418_x2016_1089531999}[命令前，请使用]{style="font-family:宋体"}**[display mdc resource]{lang="EN-US"}**[命令可查看]{style="font-family:宋体"}[MDC]{lang="EN-US"}[当前实际已经使用的磁盘空间大小。配置值应大于]{style="font-family:宋体"}[MDC]{lang="EN-US"}[当前实际已经使用的磁盘空间大小，否则，会导致]{style="font-family:宋体"}[MDC]{lang="EN-US"}[申请新的磁盘空间失败，从而无法进行文件夹创建、文件拷贝和保存等操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1811999603}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x693160901}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用设备磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1355327114}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] limit-resource disk ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x625013565}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1915920830}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] limit-resource disk slot 1 ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1568991799}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_785653350}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] limit-resource disk slot 2 ratio 30]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_11418_x2016_705277207}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[号主控板磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x715120245}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] limit-resource disk chassis 2 slot 1 ratio 30]{lang="EN-US"}
:::

::: {#2136473035 .myid}
[]{#_Toc404783235}[]{#struct_0_11418_x2016_1818415637}[]{#_Toc327431986}[]{#_Toc326304849}[]{#_Toc293500509}[]{#_Toc279410439}[]{#_Toc279417230}[]{#_Toc279652057}[]{#_Toc279410440}[]{#_Toc279417231}[]{#_Toc279652058}[]{#_Toc279410441}[]{#_Toc279417232}[]{#_Toc279652059}[]{#_Toc279410443}[]{#_Toc279417234}[]{#_Toc279652061}[]{#_Toc279410444}[]{#_Toc279417235}[]{#_Toc279652062}[]{#_Toc279410445}[]{#_Toc279417236}[]{#_Toc279652063}[]{#_Toc279410446}[]{#_Toc279417237}[]{#_Toc279652064}[]{#_Toc279410447}[]{#_Toc279417238}[]{#_Toc279652065}[]{#_Toc279410448}[]{#_Toc279417239}[]{#_Toc279652066}[]{#_Toc279410449}[]{#_Toc279417240}[]{#_Toc279652067}[]{#_Toc279410450}[]{#_Toc279417241}[]{#_Toc279652068}[]{#_Toc279410451}[]{#_Toc279417242}[]{#_Toc279652069}[]{#_Toc279410452}[]{#_Toc279417243}[]{#_Toc279652070}[]{#_Toc279410453}[]{#_Toc279417244}[]{#_Toc279652071}[]{#_Toc279410454}[]{#_Toc279417245}[]{#_Toc279652072}[]{#_Toc279410455}[]{#_Toc279417246}[]{#_Toc279652073}[]{#_Toc279410456}[]{#_Toc279417247}[]{#_Toc279652074}[]{#_Toc279410457}[]{#_Toc279417248}[]{#_Toc279652075}[]{#_Toc279410458}[]{#_Toc279417249}[]{#_Toc279652076}[]{#_Toc279410459}[]{#_Toc279417250}[]{#_Toc279652077}[]{#_Toc279410460}[]{#_Toc279417251}[]{#_Toc279652078}[]{#_Toc279410461}[]{#_Toc279417252}[]{#_Toc279652079}[]{#_Toc279410462}[]{#_Toc279417253}[]{#_Toc279652080}[]{#_Toc279410463}[]{#_Toc279417254}[]{#_Toc279652081}[]{#_Toc279410464}[]{#_Toc279417255}[]{#_Toc279652082}[]{#_Toc279410465}[]{#_Toc279417256}[]{#_Toc279652083}[]{#_Toc279410466}[]{#_Toc279417257}[]{#_Toc279652084}[]{#_Toc279410467}[]{#_Toc279417258}[]{#_Toc279652085}[]{#_Toc279410468}[]{#_Toc279417259}[]{#_Toc279652086}[]{#_Toc279410469}[]{#_Toc279417260}[]{#_Toc279652087}[]{#_Toc279410470}[]{#_Toc279417261}[]{#_Toc279652088}[]{#_Toc279410471}[]{#_Toc279417262}[]{#_Toc279652089}[]{#_Toc279410472}[]{#_Toc279417263}[]{#_Toc279652090}[]{#_Toc279410473}[]{#_Toc279417264}[]{#_Toc279652091}[]{#_Toc279410474}[]{#_Toc279417265}[]{#_Toc279652092}[]{#_Toc279410475}[]{#_Toc279417266}[]{#_Toc279652093}[]{#_Toc279410476}[]{#_Toc279417267}[]{#_Toc279652094}[]{#_Toc279410477}[]{#_Toc279417268}[]{#_Toc279652095}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- limit-resource memory**

------------------------------------------------------------------------

[**[limit-resource memory]{lang="EN-US"}**]{#struct_0_11418_x2016_x1355261578}[命令用来配置]{style="font-family:宋体"}[MDC]{lang="EN-US"}[可使用的内存上限（用百分比表示）。]{style="font-family:宋体"}

[**[undo limit-resource ]{lang="EN-US"}[memory]{lang="EN-US"}**]{#struct_0_11418_x2016_x1220034745}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1434242534}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11418_x2016_1320995242}

[**[limit-resource memory ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_x1181035284}

[**[undo limit-resource memory]{lang="EN-US"}**]{#struct_0_11418_x2016_407472100}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11418_x2016_2005707726}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[limit-resource memory]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \] **ratio** *limit-ratio*]{lang="EN-US"}]{#struct_0_11418_x2016_x820677347}

[**[undo limit-resource memory]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_11418_x2016_x1109750525}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11418_x2016_x1355720330}[模式：]{style="font-family:宋体"}

[**[limit-resource memory]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] **ratio** *limit-ratio*]{lang="EN-US"}]{#struct_0_11418_x2016_2005023317}

[**[undo limit-resource memory]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_11418_x2016_379888335}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x2140016402}

[[所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x148197823}[共享物理设备上的内存，每个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[可使用的内存上限为空闲内存大小。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_827771330}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1363067688}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1615299585}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_1980773787}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355654794}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1307027760}[：表示单板所在的槽位号。分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x639449604}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x512683313}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_11418_x2016_x2064929861}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_x663325426}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在指定单板上最多可使用的内存大小与该设备整个内存大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_759261191}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在指定单板上最多可使用的内存大小与该单板整个内存大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*]{#struct_0_11418_x2016_1160366438}[：表示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[在指定单板上最多可使用的内存大小与该成员设备整个内存大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1116671892}

[[使用本命令相当于给一台]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1377996879}[分配内存，如果内存分配过小，会影响]{style="font-family:宋体"}[MDC]{lang="EN-US"}[启动，请保证所配置内存限制大于]{style="font-family:宋体"}[MDC]{lang="EN-US"}[启动所需内存。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355589258}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1600337618}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用设备内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_176120744}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-MDC-2-sub1\] limit-resource memory ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x91913138}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1450287753}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-MDC-2-sub1\] limit-resource memory slot 1 ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_1241625872}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1590696516}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-MDC-2-sub1\] limit-resource memory slot 2 ratio 30]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_11418_x2016_1539918480}[配置]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1355523722}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[[\[Sysname-MDC-2-sub1\] limit-resource memory chassis 2 slot 1 ratio 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_11418_x2016_704336163}
:::

::::: {#803282398 .myid}
[]{#_Toc404783236}[]{#struct_0_11418_x2016_x1258185079}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- location**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MDC命令.files/image001.png){#图片 7 width="62" height="25"}]{lang="EN-US"}]{#struct_0_11418_x2016_x1505331237}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11418_x2016_x2065126469}
:::

[ ]{lang="EN-US"}

[**[location]{lang="EN-US"}**]{#struct_0_11418_x2016_x549898797}[命令用来将接口板的使用权限分配给]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **location**]{lang="EN-US"}]{#struct_0_11418_x2016_x1806453070}[命令用来取消分配。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1723042628}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_11418_x2016_1123032343}

[**[location slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1546183398}

[**[undo]{lang="EN-US"}**[ **location slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1926208599}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11418_x2016_x1354933898}[模式：]{style="font-family:宋体"}

[**[location chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_198620266}

[**[undo]{lang="EN-US"}**[ **location chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1209823616}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x2080016064}

[[缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x124847618}[可以使用物理设备上的所有接口板，非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[不能使用。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1438289216}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1186839143}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1156929645}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x434088917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x1354868362}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1823264428}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x1862957060}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x188023045}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_475647847}

[[只有将接口板的使用权限分配给]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_1461826926}[后，才能将接口板上的接口分配给]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在不同]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1277948312}[视图下执行该命令可以将同一接口板的使用权限分配给多个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1198396588}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_575496562}[将]{style="font-family:宋体"}[3]{lang="EN-US"}[号接口板的使用权限分配给]{style="font-family:
宋体"}[MDC sub1]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1355458189}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] location slot 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_1412055725}[将]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[3]{lang="EN-US"}[号接口板的使用权限分配给]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1994693896}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] location chassis 2 slot 3]{lang="EN-US"}
:::::

::: {#-719433416 .myid}
[]{#_Toc404783237}[]{#struct_0_11418_x2016_x1411330539}[]{#_Toc315942717}[]{#_Toc315942718}[]{#_Toc315942719}[]{#_Toc315942720}[]{#_Toc315942721}[]{#_Toc315942722}[]{#_Toc315942723}[]{#_Toc315942724}[]{#_Toc315942725}[]{#_Toc315942726}[]{#_Toc315942727}[]{#_Toc315942728}[]{#_Toc315942729}[]{#_Toc315942730}[]{#_Toc315942731}[]{#_Toc315942732}[]{#_Toc315942733}[]{#_Toc315942734}[]{#_Toc315942735}[]{#_Toc315942736}[]{#_Toc315942737}[]{#_Toc315942738}[]{#_Toc315942739}[]{#_Toc315942740}[]{#_Toc315942741}[]{#_Toc315942742}[]{#_Toc315942743}[]{#_Toc315942744}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- switchto mdc**

------------------------------------------------------------------------

[**[switchto mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x665671167}[命令用来登录指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，命令行视图将从缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的系统视图切换到指定]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的用户视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x99969502}

[**[switchto mdc ]{lang="EN-US"}**]{#struct_0_11418_x2016_1103856694}[*[mdc-name]{lang="EN-US"}*]{.ItemListChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1826425887}

[[系统视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_x659040877}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355392653}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_2062111600}

[[network-operator]{lang="EN-US"}]{#struct_0_11418_x2016_1219869573}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1615672415}

[[*[mdc-name]{lang="EN-US"}*]{.ItemListChar}]{#struct_0_11418_x2016_1262492589}[：]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。必须是当前设备上已经启动的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1450654854}

[[只有]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_354767454}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态时，才允许使用该命令来登录]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1144297171}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1070886609}[切换到]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1355327117}

[\[Sysname\] switchto mdc sub1]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\* Copyright (c) 2004-2011 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\<Sysname\> display mdc]{lang="EN-US"}

[ID         Name            Status]{lang="EN-US"}

[2          sub1            active ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x221729038}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[switchback]{lang="EN-US"}**]{#struct_0_11418_x2016_x1392567567}
:::

::: {#536860702 .myid}
[]{#_Toc404783238}[]{#struct_0_11418_x2016_x2012651968}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- mdc**

------------------------------------------------------------------------

[**[mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_1705461687}[命令用来创建]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[MDC]{lang="EN-US"}[视图（如果指定的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[已经存在，则直接进入]{style="font-family:宋体"}[MDC]{lang="EN-US"}[视图）。]{style="font-family:宋体"}

[**[undo mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x302540792}[命令用来删除一个已经存在的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355261581}

[**[mdc ]{lang="EN-US"}**]{#struct_0_11418_x2016_x10639916}[*[mdc-name]{lang="EN-US"}*]{.ItemListChar}[ \[ **id** *mdc-id* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **mdc** ]{lang="EN-US"}]{#struct_0_11418_x2016_1154288250}[*[mdc-name]{lang="EN-US"}*]{.ItemListChar}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11418_x2016_476236334}

[[设备上有一个]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_538942582}[（缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[），该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称为]{style="font-family:宋体"}[Admin]{lang="EN-US"}[，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1828105723}

[[系统视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1631136274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1909798517}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x801781662}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355720333}

[[*[mdc-name]{lang="EN-US"}*]{.ItemListChar}]{#struct_0_11418_x2016_x1886659452}[：]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[**[id]{lang="EN-US"}***[ mdc-id]{lang="EN-US"}*]{.ItemListChar}]{#struct_0_11418_x2016_x1771396590}[[：]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{.ItemListChar}[[的编号，取值范围与设备的型号有关，请以设备的实际情况为准。不指定该参数时，系统会给]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{.ItemListChar}[[自动分配一个目前可用的最小的编号。]{style="font-family:
宋体"}]{.ItemListChar}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1717511762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省]{style="font-family:宋体"}]{#struct_0_11418_x2016_x218198044}[MDC]{lang="EN-US"}[不需要创建，不能删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行该命令可以创建多个]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1940621586}[MDC]{lang="EN-US"}[，不同型号的设备支持的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[总个数不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进入指定]{style="font-family:宋体"}]{#struct_0_11418_x2016_1839213505}[MDC]{lang="EN-US"}[视图时，可以不输入]{style="font-family:宋体"}[*[mdc-id]{lang="EN-US"}*]{.ItemListChar}[。但如果输入，则必须和]{style="font-family:宋体"}[MDC]{lang="EN-US"}[当前的编号一致，否则会提示错误信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1506178568}[MDC]{lang="EN-US"}[后，该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[下的磁盘文件以及配置都会丢失，并且不能恢复，请谨慎使用删除]{style="font-family:宋体"}[MDC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x789096294}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_817573172}[创建]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，名称为]{style="font-family:宋体"}[sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_x1355654797}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[It will take some time to create MDC\...]{lang="EN-US"}

[MDC created successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1710312287}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x1223268914}
:::

::: {#959926395 .myid}
[]{#_Toc404783239}[]{#struct_0_11418_x2016_x1828730225}

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- mdc start**

------------------------------------------------------------------------

[**[mdc ]{lang="EN-US"}**]{#struct_0_11418_x2016_214339893}[**[start]{lang="EN-US"}**]{.ItemListChar}[命令用来启动当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo mdc ]{lang="EN-US"}**]{#struct_0_11418_x2016_492493707}[**[start]{lang="EN-US"}**]{.ItemListChar}[命令用来停止当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1564846326}

[**[mdc ]{lang="EN-US"}**]{#struct_0_11418_x2016_x193589657}[**[start]{lang="EN-US"}**]{.ItemListChar}

[**[undo]{lang="EN-US"}**[ **mdc** ]{lang="EN-US"}]{#struct_0_11418_x2016_x1355589261}[**[start]{lang="EN-US"}**]{.ItemListChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x390287429}

[[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_612735516}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1399539731}

[[network-admin]{lang="EN-US"}]{#struct_0_11418_x2016_1400598628}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1640511459}

[[创建]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_11418_x2016_x1430599605}[相当于构造了一台新的物理设备。创建后需要执行]{style="font-family:宋体"}**[mdc ]{lang="EN-US"}**[**[start]{lang="EN-US"}**]{.ItemListChar}[命令，才能完成新]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的初始化，相当于上电启动。启动后，用户可以登录到该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[执行配置以及查看操作。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_11418_x2016_618650963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[停止]{style="font-family:宋体"}]{#struct_0_11418_x2016_1823877352}[MDC]{lang="EN-US"}[会导致该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的业务中断，登录该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的用户自动退出，请谨慎使用该功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[停止]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1355523725}[MDC]{lang="EN-US"}[前请保存]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的配置，否则，直接停止]{style="font-family:宋体"}[MDC]{lang="EN-US"}[可能导致]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的当前配置丢失。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1463851050}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_2109392738}[启动]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11418_x2016_1818242449}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] mdc start]{lang="EN-US"}

[It will take some time to start MDC\...]{lang="EN-US"}

[MDC started successfully.]{lang="EN-US"}
:::

::: {#673617888 .myid}
[]{#_Toc404783241}[]{#struct_0_11418_x2016_x1837669355}

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- display mdc**

------------------------------------------------------------------------

[**[display mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x1502812592}[命令用来显示本]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关信息，包括本]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的编号、名称和状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1354933901}

[**[display mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x1011692068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_672884683}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_290401833}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1705657276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_1418221118}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_1480429771}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_988235438}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x774674415}[显示本]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<sub1\> display mdc]{lang="EN-US"}]{#struct_0_11418_x2016_x1354868365}

[ID      Name         Status]{lang="EN-US"}

[2       sub1         active]{lang="EN-US"}

[[显示信息描述请参见]{style="font-family:宋体"}]{#struct_0_11418_x2016_x2065388613}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](#_0_11418_x2016_x2090198087)[。]{style="font-family:宋体"}
:::

::: {#-1225934632 .myid}
[]{#_Toc404783242}[]{#struct_0_11418_x2016_913020420}

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- display mdc interface**

------------------------------------------------------------------------

[**[display mdc interface]{lang="EN-US"}**]{#struct_0_11418_x2016_1850302585}[命令用来显示本]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1100692470}

[**[display mdc interface]{lang="EN-US"}**]{#struct_0_11418_x2016_1588607595}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x209529591}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_1483279039}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_854607732}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x1355327116}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_x1787812979}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_973527246}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1228006372}[显示本]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[\<sub1\> display mdc interface]{lang="EN-US"}]{#struct_0_11418_x2016_x1755790184}

[ MDC sub1\'s interface(s):]{lang="EN-US"}

[  M-Ethernet1/0/1                    GigabitEthernet1/0/2]{lang="EN-US"}

[  Ten-GigabitEthernet1/1/5           Ten-GigabitEthernet1/1/6]{lang="EN-US"}
:::

::: {#1356812736 .myid}
[]{#_Toc404783243}[]{#struct_0_11418_x2016_x1665772466}

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- display mdc resource**

------------------------------------------------------------------------

[**[display mdc resource]{lang="EN-US"}**]{#struct_0_11418_x2016_x2066287704}[命令用来显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1232437027}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11418_x2016_x1355261580}

[**[display mdc]{lang="EN-US"}**[ **resource** \[ **cpu** \| **disk** \| **memory[ ]{style="color:red"}**\]]{lang="EN-US"}]{#struct_0_11418_x2016_x1576723857}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11418_x2016_x1044221808}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mdc resource ]{lang="EN-US"}**[\[ **cpu** ]{lang="EN-US"}[\| **disk** \| **memory** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11418_x2016_621622141}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11418_x2016_x543919420}[模式：]{style="font-family:宋体"}

[**[display mdc resource ]{lang="EN-US"}**[\[ **cpu** ]{lang="EN-US"}[\| **disk** \| **memory** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11418_x2016_x1005114585}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1035309213}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_x394915059}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1208384424}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x1355720332}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_842223903}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x2060622047}

[**[cpu]{lang="EN-US"}**]{#struct_0_11418_x2016_436440505}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[使用情况。]{style="font-family:宋体"}

[**[disk]{lang="EN-US"}**]{#struct_0_11418_x2016_x453015975}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的磁盘使用情况。]{style="font-family:宋体"}

[**[memory]{lang="EN-US"}**]{#struct_0_11418_x2016_625912475}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的内存使用情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_1486107842}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定单板上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对所有单板上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_593876264}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定成员设备上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对所有成员设备上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x2117079568}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定成员设备指定单板上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有单板上]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_11418_x2016_x2065388612}[：显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x155092255}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1355654796}[显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sub1\> display mdc resource]{lang="EN-US"}]{#struct_0_11418_x2016_x144228346}

[Memory usage:]{lang="EN-US"}

[Slot 0 CPU 0:]{lang="EN-US"}

[Used 232.3MB, Free 263.6MB, Total 495.9MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Available(MB)]{lang="EN-US"}

[  2     sub1             495.9        42.7         263.6]{lang="EN-US"}

[CPU usage:]{lang="EN-US"}

[Slot 0 CPU 0:]{lang="EN-US"}

[  ID    Name             Weight       Usage(%)]{lang="EN-US"}

[  2     sub1             10           0]{lang="EN-US"}

[Disk usage:]{lang="EN-US"}

[Slot 0 CPU 0:]{lang="EN-US"}

[flash: Used 0.7MB, Free 461.2MB, Total 461.9MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)     Available(MB)]{lang="EN-US"}

[  2     sub1             461.9        0.1          461.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_554391873}[显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sub1\> display mdc resource]{lang="EN-US"}]{#struct_0_11418_x2016_x1354868364}

[Memory usage:]{lang="EN-US"}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[Used 238.1MB, Free 249.3MB, Total 487.4MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  2     sub1             487.4        32.1        249.3]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[Used 218.3MB, Free 270.1MB, Total 487.4MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  2     sub1             487.4        30.1        270.1]{lang="EN-US"}

[CPU usage:]{lang="EN-US"}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[  ID    Name             Weight       Usage(%)]{lang="EN-US"}

[  2     MyDevice         10           0   ]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[  ID    Name             Weight       Usage(%)]{lang="EN-US"}

[  2     sub1             10           0]{lang="EN-US"}

[Disk usage:]{lang="EN-US"}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[cfa0: Used 83.4MB, Free 163.1MB, Total 246.5MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  2     sub1             46.3         0.1         46.2]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[cfa0: Used 44.8MB, Free 201.7MB, Total 246.5MB]{lang="EN-US"}

[  ID    Name             Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  2     sub1             40           0.0         40]{lang="EN-US"}

[[显示信息描述请参见]{style="font-family:宋体"}]{#struct_0_11418_x2016_x498845916}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](#_0_11418_x2016_x1071380629)[。]{style="font-family:宋体"}
:::

::: {#1024163059 .myid}
[]{#_Toc404783244}[]{#struct_0_11418_x2016_x876266288}

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- switchback**

------------------------------------------------------------------------

[**[switchback]{lang="EN-US"}**]{#struct_0_11418_x2016_774684023}[命令用来从当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[切换回缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，命令行视图将从当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的用户视图返回到缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的系统视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x574215338}

[**[switchback]{lang="EN-US"}**]{#struct_0_11418_x2016_1499029420}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x1355589263}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11418_x2016_772511985}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1404253104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11418_x2016_x679235695}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11418_x2016_885743526}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1135802153}

[[network-admin/network-operator]{lang="EN-US"}]{#struct_0_11418_x2016_410058060}[使用]{style="font-family:宋体"}**[switchto]{lang="EN-US"}**[命令登录]{style="font-family:宋体"}[MDC]{lang="EN-US"}[后角色变为]{style="font-family:宋体"}[mdc-admin/mdc-operator]{lang="EN-US"}[。]{style="font-family:宋体"}

[[只有通过执行]{style="font-family:宋体"}**[switchto]{lang="EN-US"}**]{#struct_0_11418_x2016_x1922691318}[命令登录]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的情况下可以使用]{style="font-family:宋体"}**[switchback]{lang="EN-US"}**[命令切换回缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。使用其它方式（比如通过]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的以太网口直接]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[）登录的情况不能使用该命令切换回缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11418_x2016_1250319222}

[[\# ]{lang="EN-US"}]{#struct_0_11418_x2016_x1355523727}[由本]{style="font-family:宋体"}[MDC]{lang="EN-US"}[返回缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sub1\> switchback]{lang="EN-US"}]{#struct_0_11418_x2016_301051636}

[\[Sysname\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11418_x2016_x418322884}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[switchto mdc]{lang="EN-US"}**]{#struct_0_11418_x2016_x2058557170}
:::
