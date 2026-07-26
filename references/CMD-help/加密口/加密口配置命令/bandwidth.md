::: {#1742433432 .myid}
[]{#_Toc404794146}[]{#struct_0_x2878_x8506_62076976}

**加密口 \-- 加密口配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x2878_x8506_x915640045}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1937976605}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1327906773}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x2878_x8506_x585100009}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1461304218}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_740854589}

[[加密口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x2878_x8506_x1430105903}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_835530669}

[[加密口视图]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x1183612064}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x368381146}

[[network-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_412128642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_2093495787}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_1985522297}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x2878_x8506_x585034473}[：]{style="font-family:宋体"}[表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_1626150512}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x2878_x8506_x1637796929}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_137417527}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_x692022596}[配置加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2878_x8506_x727565309}

[\[Sysname\] interface encrypt 2/4/0]{lang="EN-US"}

[\[Sysname-Encrypt2/4/0\] bandwidth 50]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404794147}[]{#struct_0_x2878_x8506_2079105895}

**加密口 \-- 加密口配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1071741443}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2878_x8506_20168184}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x584968937}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x2878_x8506_x1779916681}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2878_x8506_x998384726}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x55445454}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x2878_x8506_1015226400}["，比如：]{style="font-family:宋体"}[Encrypt2/4/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x293736803}

[[加密口视图]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x437252226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1729967323}

[[network-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_x1424209637}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_x584903401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_84922547}

[*[text]{lang="EN-US"}*]{#struct_0_x2878_x8506_x1138287577}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1969119106}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_567914618}[设置加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[encrypt-intf]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2878_x8506_x1470963827}

[\[Sysname\] interface encrypt 2/4/0]{lang="EN-US"}

[\[Sysname-Encrypt2/4/0\] description encrypt-intf]{lang="EN-US"}
:::

::: {#1588189860 .myid}
[]{#_Toc404794148}[]{#struct_0_x2878_x8506_233409329}

**加密口 \-- 加密口配置命令 \-- display interface encrypt**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1311802066}[命令用来显示]{style="font-family:宋体"}[加密口]{style="font-family:宋体"}[的相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x2015792893}

[**[display interface ]{lang="EN-US"}**[\[ **encrypt** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x2878_x8506_442052255}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_1616054329}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2878_x8506_1891424146}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_280242833}

[[network-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_x1001145144}

[[network-operator]{lang="EN-US"}]{#struct_0_x2878_x8506_1775538281}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_608472979}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2878_x8506_x959436640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x585820905}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2878_x8506_x1030273683}[：显示指定加密口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1898169809}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x2878_x8506_x590149739}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x2878_x8506_314413301}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_932187183}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x2878_x8506_802277132}**[encrypt]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_580960767}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[加密口]{style="font-family:宋体"}[的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_1352954238}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_x1832365699}[显示加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface encrypt 2/4/0]{lang="EN-US"}]{#struct_0_x2878_x8506_x585362152}

[Encrypt2/4/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Encrypt2/4/0 Interface]{lang="EN-US"}

[Bandwidth: 64kbps]{lang="EN-US"}

[Maximum Transmit Unit: 64000]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Physical: Encrypt2/4/0, baudrate: 64000 bps]{lang="EN-US"}

[Last 5 seconds input: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}

[Last 5 seconds output: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_x655271059}[显示加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface encrypt 2/4/0 brief]{lang="EN-US"}]{#struct_0_x2878_x8506_x1633190584}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[En2/4/0              DOWN DOWN      \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_x585296616}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的加密口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface encrypt brief down]{lang="EN-US"}]{#struct_0_x2878_x8506_826223998}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[En2/4/0              ADM   Administratively]{lang="EN-US"}

[En2/4/1              DOWN  Not connected]{lang="EN-US"}

[En2/4/2              DOWN  Not connected]{lang="EN-US"}

[En2/4/3              DOWN  Not connected]{lang="EN-US"}

[En2/4/4              DOWN  Not connected]{lang="EN-US"}

[En2/4/5              DOWN  Not connected]{lang="EN-US"}

[En2/4/6              DOWN  Not connected]{lang="EN-US"}

[En2/4/7              DOWN  Not connected]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface encrypt]{lang="EN-US"}]{#struct_0_x2878_x8506_1917926754}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x854588723}[[字段]{style="font-family:黑体"}]{#struct_0_x2878_x8506_312732985}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2878_x8506_870466669}

[[Encrypt2/4/0 ]{lang="EN-US"}]{#struct_0_x2878_x8506_881141373}

[[Current state]{lang="EN-US"}]{#struct_0_x2878_x8506_x585231080}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x2878_x8506_1264957658}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2878_x8506_1294893799}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2878_x8506_x1778845221}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2878_x8506_x1570263582}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x2878_x8506_x61476448}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x585165544}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2878_x8506_2031324009}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2878_x8506_x1070320245}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2878_x8506_x420371323}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x2878_x8506_x720800364}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2878_x8506_490275289}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x585100008}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x2878_x8506_x1461369754}

[[接口的最大传输单元（]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x2878_x8506_1091513796}[）。缺省值为]{style="font-family:宋体"}[64000]{lang="EN-US"}[字节。表示长度大于]{style="font-family:宋体"}[MTU]{lang="EN-US"}[的报文，将会被分片后再发送。如果设置了不准分片，报文会被丢弃]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x2878_x8506_1776876098}

[[物理层链路信息]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x747442263}

[[baudrate]{lang="EN-US"}]{#struct_0_x2878_x8506_x1714345955}

[[接口的带宽]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x585034472}

[[Last 5 seconds input: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x2878_x8506_1626216048}

[[最近]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x2878_x8506_x1616950545}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的包数]{style="font-family:宋体"}

[[Last 5 seconds output:  0 bytes/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x2878_x8506_x1003696824}

[[最近]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x2878_x8506_x328058271}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的包数]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}]{#struct_0_x2878_x8506_x584968936}

[[该接口接收的数据报文个数、字节数，以及由于没有接收缓冲而被丢弃的报文个数]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x1779982217}

[[Output: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}]{#struct_0_x2878_x8506_x1426871643}

[[该接口发送的数据报文个数、字节数，以及由于没有发送缓冲而被丢弃的报文个数]{style="font-family:宋体"}]{#struct_0_x2878_x8506_1413683437}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x2878_x8506_x1626233073}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x584903400}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x2878_x8506_84857011}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x987505386}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2878_x8506_1920437210}[Link]{lang="EN-US"}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x2878_x8506_x585886440}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x2878_x8506_441986719}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2878_x8506_x1245093042}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x2878_x8506_837251475}

[[Link]{lang="EN-US"}]{#struct_0_x2878_x8506_x585820904}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x1030339219}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2878_x8506_x1342646807}[：表示]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x2878_x8506_1325539507}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x2878_x8506_x585362155}

[[接口]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x655598739}[数据链路层]{style="font-family:宋体"}[协议状态，]{style="font-family:宋体"}[取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2878_x8506_x1137426911}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2878_x8506_x1905183322}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x2878_x8506_x1835991896}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x2878_x8506_x585296619}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2878_x8506_825765246}[地址]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x2878_x8506_x298625752}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x2878_x8506_x585231083}[的原因，]{style="font-family:宋体"}[取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_1264761050}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface ]{lang="EN-US"}[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_1724958731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2878_x8506_2134038417}

::: {#1533008127 .myid}
[]{#_Toc404794149}[]{#struct_0_x2878_x8506_1920904563}

**加密口 \-- 加密口配置命令 \-- interface encrypt**

------------------------------------------------------------------------

[**[interface encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1293787057}[命令用来进入]{style="font-family:宋体"}[加密口]{style="font-family:宋体"}[视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x369050493}

[**[interface encrypt]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x2878_x8506_x322101161}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x139889302}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2878_x8506_x1894575276}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x585165547}

[[network-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_2031520617}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_873859260}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x2878_x8506_1267406740}

[*[number]{lang="EN-US"}*]{#struct_0_x2878_x8506_54922982}[：]{style="font-family:宋体"}[加密口]{style="font-family:宋体"}[的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1099914346}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_x1543826928}[进入加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[的接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2878_x8506_x1618997388}

[\[Sysname\] interface encrypt 2/4/0]{lang="EN-US"}

[\[Sysname-Encrypt2/4/0\]]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc404794150}[]{#struct_0_x2878_x8506_2113822453}

**加密口 \-- 加密口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2878_x8506_x585100011}[命令用来清除]{style="font-family:
宋体"}[加密口]{style="font-family:宋体"}[的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1461828507}

[**[reset counters interface]{lang="EN-US"}**[ \[ **encrypt** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x2878_x8506_598233179}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1337205979}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2878_x8506_1297778131}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_2056172407}

[[network-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_583741177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_644714501}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_600557598}

[**[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_x585034475}[：清除加密口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2878_x8506_1626019440}[：加密口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x899855018}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x2878_x8506_1293583481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_1077410369}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1224592255}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[加密口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_x230109307}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[加密口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1364060094}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_x584968939}[清除加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface encrypt 2/4/0]{lang="EN-US"}]{#struct_0_x2878_x8506_x1780309897}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_1175412169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[encrypt]{lang="EN-US"}**]{#struct_0_x2878_x8506_x161473097}
:::

::: {#1170655049 .myid}
[]{#_Toc404794151}[]{#struct_0_x2878_x8506_x1232634084}

**加密口 \-- 加密口配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2878_x8506_x841957948}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x2878_x8506_x164967768}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x723168800}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1606376020}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2878_x8506_x1323395532}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x584903403}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_x2878_x8506_84791475}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x657691367}

[[加密口视图]{style="font-family:宋体"}]{#struct_0_x2878_x8506_180518449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_85325360}

[[network-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_x836231956}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2878_x8506_x142447279}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2878_x8506_x1437349300}

[[\# ]{lang="EN-US"}]{#struct_0_x2878_x8506_282303545}[关闭加密口]{style="font-family:宋体"}[Encrypt2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2878_x8506_x585886443}

[\[Sysname\] interface encrypt 2/4/0]{lang="EN-US"}

[\[Sysname-Encrypt2/4/0\] shutdown]{lang="EN-US"}
:::
