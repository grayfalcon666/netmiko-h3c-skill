::: {#-1479207546 .myid}
[]{#_Toc404784176}[]{#struct_0_x2137_27564_2135233816}[]{#_Toc309290864}

**MVRP \-- MVRP配置命令 \-- display mvrp running-status**

------------------------------------------------------------------------

[**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_x1511359244}[命令用来显示]{style="font-family:
宋体"}[MVRP]{lang="EN-US"}[运行状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_782233730}

[**[display mvrp running-status ]{lang="EN-US"}**[\[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x2137_27564_x71457442}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x566909717}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2137_27564_478671210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x950306403}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_521352838}

[[network-operator]{lang="EN-US"}]{#struct_0_x2137_27564_x696018602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_181502056}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2137_27564_2135168280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1974751975}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x2137_27564_2120564560}[：显示指定端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[运行状态信息。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为以太网端口列表，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}[ ]{lang="EN-US"}*[= *interface-type interface-number* \[ **to** *interface-type interface-number* \]]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果指定该参数，但端口未使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能，则只显示]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[全局信息。如果未指定该参数，则显示]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[全局信息和所有使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[运行状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1793501928}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_682176032}[显示所有端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[运行状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display mvrp running-status]{lang="EN-US"}]{#struct_0_x2137_27564_2135102744}

[ \-\-\-\-\-\--\[MVRP Global Info\]\-\-\-\-\-\--]{lang="EN-US"}

[ Global Status     : Enabled]{lang="EN-US"}

[ Compliance-GVRP   : False]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-\--\[GigabitEthernet1/0/1\]\-\-\--]{lang="EN-US"}

[ Config Status                  : Enabled]{lang="EN-US"}

[ Running Status                 : Enabled]{lang="EN-US"}

[ Join Timer                     : 20 (centiseconds)]{lang="EN-US"}

[ Leave Timer                    : 60 (centiseconds)]{lang="EN-US"}

[ Periodic Timer                 : 100 (centiseconds)]{lang="EN-US"}

[ LeaveAll Timer                 : 1000 (centiseconds)]{lang="EN-US"}

[ Registration Type              : Normal]{lang="EN-US"}

[ Registered VLANs :]{lang="EN-US"}

[  1(default), 2-10]{lang="EN-US"}

[ Declared VLANs :]{lang="EN-US"}

[  1(default), 2-10]{lang="EN-US"}

[ Propagated VLANs :]{lang="EN-US"}

[  1(default), 2-10]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-\--\[GigabitEthernet1/0/2\]\-\-\--]{lang="EN-US"}

[ Config Status                  : Enabled]{lang="EN-US"}

[ Running Status                 : Disabled]{lang="EN-US"}

[ Join Timer                     : 20 (centiseconds)]{lang="EN-US"}

[ Leave Timer                    : 60 (centiseconds)]{lang="EN-US"}

[ Periodic Timer                 : 100 (centiseconds)]{lang="EN-US"}

[ LeaveAll Timer                 : 1000 (centiseconds)]{lang="EN-US"}

[ Registration Type              : Normal]{lang="EN-US"}

[ Registered VLANs :]{lang="EN-US"}

[  None]{lang="EN-US"}

[ Declared  VLANs :]{lang="EN-US"}

[  None]{lang="EN-US"}

[ Propagated VLANs :]{lang="EN-US"}

[  None]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mvrp running-status]{lang="EN-US"}]{#struct_0_x2137_27564_1557393771}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_272489674}[[字段]{style="font-family:黑体"}]{#struct_0_x2137_27564_2135037208}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1925928247}

[[MVRP Global Info]{lang="EN-US"}]{#struct_0_x2137_27564_1212784932}

[[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x293677261}[全局信息]{style="font-family:宋体"}

[[Global Status]{lang="EN-US"}]{#struct_0_x2137_27564_x2027906300}

[[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_181313209}[全局状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x2137_27564_1143937993}[：使能状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x2137_27564_2134971672}[：未使能状态]{lang="EN-US" style="font-family:宋体"}

[[Compliance-GVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1555393873}

[[是否兼容]{style="font-family:宋体"}[GVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x856518720}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[True]{lang="EN-US"}]{#struct_0_x2137_27564_1045927744}[：兼容]{lang="EN-US" style="font-family:宋体"}[GVRP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_x2137_27564_x1745749076}[：不兼容]{lang="EN-US" style="font-family:宋体"}[GVRP]{lang="EN-US"}

[[\-\-\--\[GigabitEthernet1/0/1\]\-\-\--]{lang="EN-US"}]{#struct_0_x2137_27564_1842964703}

[[接口提示符，到下一提示符开始前均为该接口的运行状态信息]{style="font-family:宋体"}]{#struct_0_x2137_27564_2134906136}

[[Config Status]{lang="EN-US"}]{#struct_0_x2137_27564_1977949720}

[[接口上]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x497804693}[功能的使能状态，取值为]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[，表示使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}

[[Running Status]{lang="EN-US"}]{#struct_0_x2137_27564_1498020124}

[[接口上]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1827186513}[功能的运行状态（由接口的链路状态、链路类型、接口是否为聚合成员口及接口上]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能的使能状态决定）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x2137_27564_x1939844578}[：使能状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x2137_27564_2134840600}[：未使能状态]{lang="EN-US" style="font-family:宋体"}

[[Join Timer]{lang="EN-US"}]{#struct_0_x2137_27564_1175652242}

[[Join]{lang="EN-US"}]{#struct_0_x2137_27564_x1743381001}[定时器的值，单位是厘秒]{style="font-family:宋体"}

[[Leave Timer]{lang="EN-US"}]{#struct_0_x2137_27564_1735591858}

[[Leave]{lang="EN-US"}]{#struct_0_x2137_27564_1204920279}[定时器的值，单位是厘秒]{style="font-family:宋体"}

[[Periodic Timer]{lang="EN-US"}]{#struct_0_x2137_27564_2134775064}

[[Periodic]{lang="EN-US"}]{#struct_0_x2137_27564_31506810}[定时器的值，单位是厘秒]{style="font-family:宋体"}

[[LeaveAll Timer]{lang="EN-US"}]{#struct_0_x2137_27564_1350606969}

[[LeaveAll]{lang="EN-US"}]{#struct_0_x2137_27564_1456761127}[定时器的值，单位是厘秒]{style="font-family:宋体"}

[[Registration Type]{lang="EN-US"}]{#struct_0_x2137_27564_326152215}

[[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_2135758104}[的注册模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x2137_27564_x411718317}[：表示]{lang="EN-US" style="font-family:宋体"}[Normal]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fixed]{lang="EN-US"}]{#struct_0_x2137_27564_x344623207}[：表示]{lang="EN-US" style="font-family:宋体"}[Fixed]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forbidden]{lang="EN-US"}]{#struct_0_x2137_27564_252026101}[：表示]{lang="EN-US" style="font-family:宋体"}[Forbidden]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Registered VLANs]{lang="EN-US"}]{#struct_0_x2137_27564_2135692568}

[[接口注册的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2137_27564_1151660564}

[[Declared VLANs]{lang="EN-US"}]{#struct_0_x2137_27564_1955669193}

[[接口声明的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2137_27564_1378637075}[，即通知对端接口学习的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Propagated VLANs]{lang="EN-US"}]{#struct_0_x2137_27564_2135233813}

[[接口传播的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2137_27564_x1511686924}[，即接口学习并通知本设备其他接口向外声明的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-734441619 .myid}
[]{#_Toc404784177}[]{#struct_0_x2137_27564_x211382156}[]{#_Toc309290863}

**MVRP \-- MVRP配置命令 \-- display mvrp state**

------------------------------------------------------------------------

[**[display mvrp state]{lang="EN-US"}**]{#struct_0_x2137_27564_x2118588149}[命令用来显示指定端口在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[接口状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x2121877684}

[**[display mvrp state interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x2137_27564_514130676}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1841526617}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2137_27564_589596562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2135168277}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1974293238}

[[network-operator]{lang="EN-US"}]{#struct_0_x2137_27564_824627384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x418060030}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2137_27564_1878774202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x547944686}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2137_27564_813121358}[：显示指定端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[接口状态信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:
宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x2137_27564_670671753}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[接口状态信息。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1980341455}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_2135102741}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[接口状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display mvrp state interface gigabitethernet 1/0/1 vlan 2]{lang="EN-US"}]{#struct_0_x2137_27564_1557197163}

[ MVRP state of VLAN 2 on port GE1/0/1:]{lang="EN-US"}

[ Port                      VLAN   App-state   Reg-state]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ GE1/0/1                      2       VP          IN]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mvrp state]{lang="EN-US"}]{#struct_0_x2137_27564_1298461882}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_299932918}[[字段]{style="font-family:黑体"}]{#struct_0_x2137_27564_x927538282}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2137_27564_1025353241}

[[MVRP state of VLAN 2 on port GE1/0/1]{lang="EN-US"}]{#struct_0_x2137_27564_460231120}

[[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x2137_27564_x1890614430}[上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[接口状态信息]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x2137_27564_2135037205}

[[端口简单名称，显示使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1925207351}[的端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[状态信息]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x2137_27564_1183554129}

[[指定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x2137_27564_x1471788743}

[[App-state]{lang="EN-US"}]{#struct_0_x2137_27564_1071691119}

[[属性声明状态，用来记录本端向对端实体声明的属性的状态。其状态包括：]{style="font-family:宋体"}[VO]{lang="EN-US"}]{#struct_0_x2137_27564_x95764439}[、]{style="font-family:宋体"}[VP]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[、]{style="font-family:宋体"}[AN]{lang="EN-US"}[、]{style="font-family:宋体"}[AA]{lang="EN-US"}[、]{style="font-family:宋体"}[QA]{lang="EN-US"}[、]{style="font-family:宋体"}[LA]{lang="EN-US"}[、]{style="font-family:宋体"}[AO]{lang="EN-US"}[、]{style="font-family:宋体"}[QO]{lang="EN-US"}[、]{style="font-family:宋体"}[AP]{lang="EN-US"}[、]{style="font-family:宋体"}[QP]{lang="EN-US"}[和]{style="font-family:宋体"}[LO]{lang="EN-US"}[，每个状态都由]{style="font-family:宋体"}[2]{lang="EN-US"}[个字母组成，各字母含义如下：]{style="font-family:宋体"}

[[第一个字母表示状态：]{style="font-family:宋体"}]{#struct_0_x2137_27564_2134971669}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_x2137_27564_x1554804048}[代表]{lang="EN-US" style="font-family:宋体"}[Very anxious]{lang="EN-US"}[（非常迫切的），表示该属性未曾声明过且没有收到过]{lang="EN-US" style="font-family:宋体"}[Join]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x2137_27564_662606941}[代表]{style="font-family:宋体"}[Anxious]{lang="EN-US"}[（迫切的），表示该属性声明过一次或收到过一个]{style="font-family:宋体"}[Join]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q]{lang="EN-US"}]{#struct_0_x2137_27564_x888000564}[代表]{style="font-family:宋体"}[Quiet]{lang="EN-US"}[（安静的），表示该属性声明过两次，或声明过一次且收到过一个]{style="font-family:宋体"}[Join]{lang="EN-US"}[消息，或收到过两个]{style="font-family:宋体"}[Join]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x2137_27564_1184908292}[代表]{lang="EN-US" style="font-family:宋体"}[Leaving]{lang="EN-US"}[（离开），表示该属性正在注销]{lang="EN-US" style="font-family:宋体"}

[[第二个字母表示成员类型：]{style="font-family:宋体"}]{#struct_0_x2137_27564_1595855228}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x2137_27564_2134906133}[代表]{lang="EN-US" style="font-family:宋体"}[Active member]{lang="EN-US"}[（主动成员），表示正在声明该属性，至少已有一次发送，可以有接收]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x2137_27564_1977753112}[代表]{lang="EN-US" style="font-family:宋体"}[Passive member]{lang="EN-US"}[（被动成员），表示正在声明该属性，但是只有接收，没有发送]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x2137_27564_x2124568254}[代表]{lang="EN-US" style="font-family:宋体"}[Observer]{lang="EN-US"}[（观察者），表示未在声明该属性，只是在侦听]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x2137_27564_x1177515630}[代表]{style="font-family:宋体"}[New]{lang="EN-US"}[（新属性被动端），表示正在声明该属性，但是只有接收，没有发送]{style="font-family:宋体"}

[[譬如，]{style="font-family:宋体"}[VP]{lang="EN-US"}]{#struct_0_x2137_27564_x1672594769}[代表"]{style="font-family:宋体"}[Very anxious]{lang="EN-US"}[，]{style="font-family:宋体"}[Passive member]{lang="EN-US"}["，表示]{style="font-family:宋体"}[Very anxious]{lang="EN-US"}[状态下的被动成员]{style="font-family:宋体"}

[[Reg-state]{lang="EN-US"}]{#struct_0_x2137_27564_2134840597}

[[属性注册状态，用来记录对端实体声明的属性在本端的注册情况。其状态包括：]{style="font-family:宋体"}[IN]{lang="EN-US"}]{#struct_0_x2137_27564_x398653541}[、]{style="font-family:宋体"}[LV]{lang="EN-US"}[和]{style="font-family:宋体"}[MT]{lang="EN-US"}[，各状态含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN]{lang="EN-US"}]{#struct_0_x2137_27564_2046150810}[：注册状态，端口已经注册了该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LV]{lang="EN-US"}]{#struct_0_x2137_27564_x1846790413}[：离开状态，端口正在注销该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MT]{lang="EN-US"}]{#struct_0_x2137_27564_x1823978935}[：注销状态，端口未注册该属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-420310084 .myid}
[]{#_Toc404784178}[]{#struct_0_x2137_27564_x360660549}[]{#_Toc309290865}

**MVRP \-- MVRP配置命令 \-- display mvrp statistics**

------------------------------------------------------------------------

[**[display mvrp statistics]{lang="EN-US"}**]{#struct_0_x2137_27564_2134775061}[命令用来显示]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_31703418}

[**[display mvrp statistics]{lang="EN-US"}**[ \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x2137_27564_x460803988}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1271365727}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2137_27564_x1640904097}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_102383212}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x957146096}

[[network-operator]{lang="EN-US"}]{#struct_0_x2137_27564_x1428474275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1397203571}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2137_27564_677259935}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2135758101}

[**[interface]{lang="EN-US"}***[ interface-list]{lang="EN-US"}*]{#struct_0_x2137_27564_x411521709}[：显示指定端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为以太网端口列表，表示方式为]{style="font-family:宋体"}*[interface-list ]{lang="EN-US"}*[= *interface-type interface-number* \[ **to** *interface-type interface-number* \]]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为端口类型和端口编号。如果未指定该参数，则显示所有使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能的端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_27564_98262499}

[[如果指定的端口上没有使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x812499328}[功能，则不显示任何信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1893204700}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_934292315}[显示所有使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能的端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display mvrp statistics]{lang="EN-US"}]{#struct_0_x2137_27564_2135233814}

[ ]{lang="EN-US"}

[ \-\-\--\[GigabitEthernet1/0/1\]\-\-\--]{lang="EN-US"}

[ Failed Registrations        : 1]{lang="EN-US"}

[ Last PDU Origin             : 000f-e200-0010]{lang="EN-US"}

[ Frames Received             : 201]{lang="EN-US"}

[  New Event Received          : 0]{lang="EN-US"}

[  JoinIn Event Received       : 1167]{lang="EN-US"}

[  In Event Received           : 0]{lang="EN-US"}

[  JoinMt Event Received       : 22387]{lang="EN-US"}

[  Mt Event Received           : 31]{lang="EN-US"}

[  Leave Event Received        : 210]{lang="EN-US"}

[  LeaveAll Event Received     : 63]{lang="EN-US"}

[ Frames Transmitted          : 120]{lang="EN-US"}

[  New Event Transmitted       : 0]{lang="EN-US"}

[  JoinIn Event Transmitted    : 311]{lang="EN-US"}

[  In Event Transmitted        : 0]{lang="EN-US"}

[  JoinMt Event Transmitted    : 873]{lang="EN-US"}

[  Mt Event Transmitted        : 11065]{lang="EN-US"}

[  Leave Event Transmitted     : 167]{lang="EN-US"}

[  LeaveAll Event Transmitted  : 4]{lang="EN-US"}

[ Frames Discarded            : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-\--\[GigabitEthernet1/0/2\]\-\-\--]{lang="EN-US"}

[ Failed Registrations        : 0]{lang="EN-US"}

[ Last PDU Origin             : 0000-0000-0000]{lang="EN-US"}

[ Frames Received             : 0]{lang="EN-US"}

[  New Event Received          : 0]{lang="EN-US"}

[  JoinIn Event Received       : 0]{lang="EN-US"}

[  In Event Received           : 0]{lang="EN-US"}

[  JoinMt Event Received       : 0]{lang="EN-US"}

[  Mt Event Received           : 0]{lang="EN-US"}

[  Leave Event Received        : 0]{lang="EN-US"}

[  LeaveAll Event Received     : 0]{lang="EN-US"}

[ Frames Transmitted          : 0]{lang="EN-US"}

[  New Event Transmitted       : 0]{lang="EN-US"}

[  JoinIn Event Transmitted    : 0]{lang="EN-US"}

[  In Event Transmitted        : 0]{lang="EN-US"}

[  JoinMt Event Transmitted    : 0]{lang="EN-US"}

[  Mt Event Transmitted        : 0]{lang="EN-US"}

[  Leave Event Transmitted     : 0]{lang="EN-US"}

[  LeaveAll Event Transmitted  : 0]{lang="EN-US"}

[ Frames Discarded            : 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mvrp statistics]{lang="EN-US"}]{#struct_0_x2137_27564_x1511228172}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_295673543}[[字段]{style="font-family:黑体"}]{#struct_0_x2137_27564_869440856}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2137_27564_1869073655}

[[\-\-\--\[GigabitEthernet1/0/1\]\-\-\--]{lang="EN-US"}]{#struct_0_x2137_27564_498119072}

[[接口提示符，到下一提示符开始前均为该接口的统计信息]{style="font-family:宋体"}]{#struct_0_x2137_27564_2135168278}

[[Failed Registrations]{lang="EN-US"}]{#struct_0_x2137_27564_x1975276278}

[[本实体上通过]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1610511101}[注册]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[失败的次数]{style="font-family:宋体"}

[[Last PDU Origin]{lang="EN-US"}]{#struct_0_x2137_27564_x1197445850}

[[上一个]{style="font-family:宋体"}[MVRP PDU]{lang="EN-US"}]{#struct_0_x2137_27564_x1099249851}[的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Frames Received]{lang="EN-US"}]{#struct_0_x2137_27564_x1207940527}

[[收到的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x2132737512}[协议帧数]{style="font-family:宋体"}

[[New Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_2135102742}

[[收到的]{style="font-family:宋体"}[New]{lang="EN-US"}]{#struct_0_x2137_27564_1557000555}[属性事件数]{style="font-family:宋体"}

[[JoinIn Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_x1817565931}

[[收到的]{style="font-family:宋体"}[JoinIn]{lang="EN-US"}]{#struct_0_x2137_27564_29472962}[属性事件数]{style="font-family:宋体"}

[[In Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_508327956}

[[收到的]{style="font-family:宋体"}[In]{lang="EN-US"}]{#struct_0_x2137_27564_2135037206}[属性事件数]{style="font-family:宋体"}

[[JoinMt Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_x1925272887}

[[收到的]{style="font-family:宋体"}[JoinMt]{lang="EN-US"}]{#struct_0_x2137_27564_1729287869}[属性事件数]{style="font-family:宋体"}

[[Mt Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_x463028344}

[[收到的]{style="font-family:宋体"}[Mt]{lang="EN-US"}]{#struct_0_x2137_27564_587037572}[属性事件数]{style="font-family:宋体"}

[[Leave Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_1187676665}

[[收到的]{style="font-family:宋体"}[Leave]{lang="EN-US"}]{#struct_0_x2137_27564_2134971670}[属性事件数]{style="font-family:宋体"}

[[LeaveAll Event Received]{lang="EN-US"}]{#struct_0_x2137_27564_x1555262801}

[[收到的]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}]{#struct_0_x2137_27564_x573926239}[属性事件数]{style="font-family:宋体"}

[[Frames Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_x716980602}

[[发送的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_2088293121}[协议帧数]{style="font-family:宋体"}

[[New Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_2134906134}

[[发送的]{style="font-family:宋体"}[New]{lang="EN-US"}]{#struct_0_x2137_27564_1978080792}[属性事件数]{style="font-family:宋体"}

[[JoinIn Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_x1487522562}

[[发送的]{style="font-family:宋体"}[JoinIn]{lang="EN-US"}]{#struct_0_x2137_27564_834847475}[属性事件数]{style="font-family:宋体"}

[[In Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_2134840598}

[[发送的]{style="font-family:宋体"}[In]{lang="EN-US"}]{#struct_0_x2137_27564_x397801573}[属性事件数]{style="font-family:宋体"}

[[JoinMt Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_x1284460021}

[[发送的]{style="font-family:宋体"}[JoinMt]{lang="EN-US"}]{#struct_0_x2137_27564_x265869128}[属性事件数]{style="font-family:宋体"}

[[Mt Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_x185405043}

[[发送的]{style="font-family:宋体"}[Mt]{lang="EN-US"}]{#struct_0_x2137_27564_2134775062}[属性事件数]{style="font-family:宋体"}

[[Leave Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_31637882}

[[发送的]{style="font-family:宋体"}[Leave]{lang="EN-US"}]{#struct_0_x2137_27564_x1488544008}[属性事件数]{style="font-family:宋体"}

[[LeaveAll Event Transmitted]{lang="EN-US"}]{#struct_0_x2137_27564_x1390853777}

[[发送的]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}]{#struct_0_x2137_27564_2135758102}[个数]{style="font-family:宋体"}

[[Frames Discarded]{lang="EN-US"}]{#struct_0_x2137_27564_x411325101}

[[丢弃的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1489293299}[协议帧数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1067923334 .myid}
[]{#_Toc404784179}[]{#struct_0_x2137_27564_545042696}[]{#_Toc309290866}

**MVRP \-- MVRP配置命令 \-- mrp timer join**

------------------------------------------------------------------------

[**[mrp timer join]{lang="EN-US"}**]{#struct_0_x2137_27564_1516787957}[命令用来配置]{style="font-family:宋体"}[Join]{lang="EN-US"}[定时器的值。]{style="font-family:宋体"}

[**[undo mrp timer join]{lang="EN-US"}**]{#struct_0_x2137_27564_2135692566}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1151529492}

[**[mrp timer join ]{lang="EN-US"}***[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_1930187956}

[**[undo mrp timer join]{lang="EN-US"}**]{#struct_0_x2137_27564_1991882544}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_133852787}

[[Join]{lang="EN-US"}]{#struct_0_x2137_27564_x844712286}[定时器的值为]{style="font-family:宋体"}[20]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1618007997}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_27564_671170523}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_880428140}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x295390640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_2135233811}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1511555852}

[*[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_x573461474}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}[定时器的值，单位为厘秒（]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒＝]{style="font-family:宋体"}[1]{lang="EN-US"}[秒）。其取值应大于等于]{style="font-family:宋体"}[20]{lang="EN-US"}[厘秒，小于]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器值的一半，且必须是]{style="font-family:宋体"}[20]{lang="EN-US"}[厘秒的倍数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1483436566}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_146445834}[配置]{style="font-family:宋体"}[Join]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[40]{lang="EN-US"}[厘秒（假设此时]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_465415788}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mrp timer join 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1152180087}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **mvrp running-status**]{lang="EN-US"}]{#struct_0_x2137_27564_234759402}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mrp timer leave]{lang="EN-US"}**]{#struct_0_x2137_27564_2071487754}
:::

::: {#-283884608 .myid}
[]{#_Toc404784180}[]{#struct_0_x2137_27564_2135168275}[]{#_Toc309290867}

**MVRP \-- MVRP配置命令 \-- mrp timer leave**

------------------------------------------------------------------------

[**[mrp timer leave]{lang="EN-US"}**]{#struct_0_x2137_27564_x1974424310}[命令用来配置]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器的值。]{style="font-family:宋体"}

[**[undo mrp timer leave]{lang="EN-US"}**]{#struct_0_x2137_27564_x1844082052}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1042597529}

[**[mrp timer leave ]{lang="EN-US"}***[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_x46597078}

[**[undo mrp timer leave]{lang="EN-US"}**]{#struct_0_x2137_27564_x1546640975}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x295811290}

[[Leave]{lang="EN-US"}]{#struct_0_x2137_27564_2140975637}[定时器的值为]{style="font-family:宋体"}[60]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x2074748872}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_27564_2135102739}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1556672876}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_2111519635}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1428412159}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1078019328}

[*[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_1023338310}[：]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器的值，单位为厘秒（]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒＝]{style="font-family:宋体"}[1]{lang="EN-US"}[秒）。其取值应大于]{style="font-family:宋体"}[Join]{lang="EN-US"}[定时器值的两倍、小于]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的值，且必须是]{style="font-family:宋体"}[20]{lang="EN-US"}[厘秒的倍数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x2147100452}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_x903758313}[配置]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒（假设此时]{style="font-family:宋体"}[Join]{lang="EN-US"}[和]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器均为缺省值）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_2135037203}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mrp timer leave 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1925600567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_1848172213}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mrp timer join]{lang="EN-US"}**]{#struct_0_x2137_27564_x762946942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mrp timer leaveall]{lang="EN-US"}**]{#struct_0_x2137_27564_x1768432314}
:::

::: {#-1421294556 .myid}
[]{#_Toc404784181}[]{#struct_0_x2137_27564_1095738559}[]{#_Toc309290868}

**MVRP \-- MVRP配置命令 \-- mrp timer leaveall**

------------------------------------------------------------------------

[**[mrp timer leaveall]{lang="EN-US"}**]{#struct_0_x2137_27564_x1599687815}[命令用来配置]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的值。]{style="font-family:宋体"}

[**[undo mrp timer leaveall]{lang="EN-US"}**]{#struct_0_x2137_27564_1653605894}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1471685168}

[**[mrp timer leaveall ]{lang="EN-US"}***[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_1609420520}

[**[undo mrp timer leaveall]{lang="EN-US"}**]{#struct_0_x2137_27564_2134971667}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1555721552}

[[LeaveAll]{lang="EN-US"}]{#struct_0_x2137_27564_x1155526053}[定时器的值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_922583119}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_27564_742639362}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_415528904}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1089453935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_1650013359}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2123810628}

[*[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_389686873}[：]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的值，单位为厘秒（]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒＝]{style="font-family:宋体"}[1]{lang="EN-US"}[秒）。其取值应大于所有端口上]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器的值、小于等于]{style="font-family:宋体"}[32760]{lang="EN-US"}[厘秒，且必须是]{style="font-family:宋体"}[20]{lang="EN-US"}[厘秒的倍数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2134906131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每一次]{style="font-family:宋体"}]{#struct_0_x2137_27564_1977884184}[LeaveAll]{lang="EN-US"}[定时器超时，都会引起全网当前端口对应]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的所有属性的注销。由于其影响范围很广，所以]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的值不能太小。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[过小的]{style="font-family:宋体"}]{#struct_0_x2137_27564_1789068915}[LeaveAll]{lang="EN-US"}[定时器值可能会影响通过]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[学习到的动态]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的稳定性，建议]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的取值不要小于其缺省值（即]{style="font-family:宋体"}[1000]{lang="EN-US"}[厘秒）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了防止每次都是同一实体的]{style="font-family:宋体"}]{#struct_0_x2137_27564_x1923755366}[LeaveAll]{lang="EN-US"}[定时器先超时，每次重启时，]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的值都将在一定范围内随机变动。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1792360171}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_967006416}[配置]{style="font-family:宋体"}[LeaveAll]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[厘秒（假设此时所有端口的]{style="font-family:宋体"}[Leave]{lang="EN-US"}[定时器都为缺省值）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_x137550592}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mrp timer leaveall 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1264459139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mrp timer leave]{lang="EN-US"}**]{#struct_0_x2137_27564_2134840595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_x398522469}
:::

::: {#809359928 .myid}
[]{#_Toc404784182}[]{#struct_0_x2137_27564_x1864549166}[]{#_Toc309290869}

**MVRP \-- MVRP配置命令 \-- mrp timer periodic**

------------------------------------------------------------------------

[**[mrp timer periodic]{lang="EN-US"}**]{#struct_0_x2137_27564_1553401751}[命令用来配置]{style="font-family:宋体"}[Periodic]{lang="EN-US"}[定时器的值。]{style="font-family:宋体"}

[**[undo mrp timer periodic]{lang="EN-US"}**]{#struct_0_x2137_27564_360230894}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_456507354}

[**[mrp timer periodic ]{lang="EN-US"}***[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_1757256853}

[**[undo mrp timer periodic]{lang="EN-US"}**]{#struct_0_x2137_27564_x828937803}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x128479966}

[[Periodic]{lang="EN-US"}]{#struct_0_x2137_27564_x1284039983}[定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2134775059}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_27564_32227703}[二层聚合接口视图]{style="font-family:宋体"}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1754145764}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_2044517872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_1429663858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x2092920470}

[*[timer-value]{lang="EN-US"}*]{#struct_0_x2137_27564_x946041353}*[：]{style="font-family:宋体"}*[Periodic]{lang="EN-US"}[定时器的值，单位为厘秒（]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒＝]{style="font-family:宋体"}[1]{lang="EN-US"}[秒），取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1127187712}

[[当]{style="font-family:宋体"}[Periodic]{lang="EN-US"}]{#struct_0_x2137_27564_x1387217113}[定时器的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[厘秒时，定时器关闭；当]{style="font-family:宋体"}[Periodic]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒时，定时器开启，这时以]{style="font-family:宋体"}[100]{lang="EN-US"}[厘秒为周期发送]{style="font-family:宋体"}[MRP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2135758099}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_1927654730}[关闭]{style="font-family:宋体"}[Periodic]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_x475569873}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mrp timer periodic 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_630515952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_1936072565}
:::

::: {#-1637283398 .myid}
[]{#_Toc309290870}[]{#_Toc404784183}[]{#struct_0_x2137_27564_1535835735}

**MVRP \-- MVRP配置命令 \-- mvrp enable**

------------------------------------------------------------------------

[**[mvrp enable]{lang="EN-US"}**]{#struct_0_x2137_27564_x653013746}[命令用来使能当前端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo mvrp enable]{lang="EN-US"}**]{#struct_0_x2137_27564_x738028593}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1129544065}

[**[mvrp enable]{lang="EN-US"}**]{#struct_0_x2137_27564_2135692563}

[**[undo mvrp enable]{lang="EN-US"}**]{#struct_0_x2137_27564_1151201812}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_804696247}

[[端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x720997035}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_111447330}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_27564_x860707120}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x930983514}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_787306388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1646489564}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2135233812}

[[只有全局和端口上都使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1511621388}[功能，同时端口链路]{style="font-family:宋体"}[Up]{lang="EN-US"}[、链路类型为]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型，且端口不为聚合成员端口时，该端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1595928760}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_834122888}[使能端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_x1859190143}

[\[Sysname\] mvrp global enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port link-type trunk]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mvrp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x150809138}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_x50453685}
:::

::: {#-1585321262 .myid}
[]{#_Toc404784184}[]{#struct_0_x2137_27564_x872686981}

**MVRP \-- MVRP配置命令 \-- mvrp global enable**

------------------------------------------------------------------------

[**[mvrp global enable]{lang="EN-US"}**]{#struct_0_x2137_27564_2135168276}[命令用来全局使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo mvrp global enable]{lang="EN-US"}**]{#struct_0_x2137_27564_x1974358774}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1804154189}

[**[mvrp global enable]{lang="EN-US"}**]{#struct_0_x2137_27564_916956276}

[**[undo mvrp global enable]{lang="EN-US"}**]{#struct_0_x2137_27564_x982427007}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x2131778885}

[[全局的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1165193641}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1237717276}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2137_27564_998545355}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x696508426}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_2135102740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_1557131627}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1702539352}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要使端口上的]{style="font-family:宋体"}]{#struct_0_x2137_27564_584924340}[MVRP]{lang="EN-US"}[功能生效，必须全局使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭全局的]{style="font-family:宋体"}]{#struct_0_x2137_27564_x1928282503}[MVRP]{lang="EN-US"}[功能的同时会关闭所有端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_748581346}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_1077668443}[全局使能]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_2135037204}

[\[Sysname\] mvrp global enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1925141815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_1241250130}
:::

::: {#1209347716 .myid}
[]{#_Toc404784185}[]{#struct_0_x2137_27564_1476805653}[]{#_Toc309290872}[]{#_Toc324171859}[]{#_Toc324509997}[]{#_Toc325373410}[]{#_Toc324171860}[]{#_Toc324509998}[]{#_Toc325373411}[]{#_Toc324171861}[]{#_Toc324509999}[]{#_Toc325373412}[]{#_Toc324171862}[]{#_Toc324510000}[]{#_Toc325373413}[]{#_Toc324171863}[]{#_Toc324510001}[]{#_Toc325373414}[]{#_Toc324171864}[]{#_Toc324510002}[]{#_Toc325373415}[]{#_Toc324171865}[]{#_Toc324510003}[]{#_Toc325373416}[]{#_Toc324171866}[]{#_Toc324510004}[]{#_Toc325373417}[]{#_Toc324171867}[]{#_Toc324510005}[]{#_Toc325373418}[]{#_Toc324171868}[]{#_Toc324510006}[]{#_Toc325373419}[]{#_Toc324171869}[]{#_Toc324510007}[]{#_Toc325373420}[]{#_Toc324171870}[]{#_Toc324510008}[]{#_Toc325373421}[]{#_Toc324171871}[]{#_Toc324510009}[]{#_Toc325373422}[]{#_Toc324171872}[]{#_Toc324510010}[]{#_Toc325373423}[]{#_Toc324171873}[]{#_Toc324510011}[]{#_Toc325373424}[]{#_Toc324171874}[]{#_Toc324510012}[]{#_Toc325373425}[]{#_Toc324171875}[]{#_Toc324510013}[]{#_Toc325373426}[]{#_Toc324171876}[]{#_Toc324510014}[]{#_Toc325373427}[]{#_Toc324171877}[]{#_Toc324510015}[]{#_Toc325373428}[]{#_Toc324171878}[]{#_Toc324510016}[]{#_Toc325373429}[]{#_Toc324171879}[]{#_Toc324510017}[]{#_Toc325373430}[]{#_Toc324171880}[]{#_Toc324510018}[]{#_Toc325373431}

**MVRP \-- MVRP配置命令 \-- mvrp gvrp-compliance enable**

------------------------------------------------------------------------

[**[mvrp gvrp-compliance enable]{lang="EN-US"}**]{#struct_0_x2137_27564_1172935123}[命令用来配置]{style="font-family:
宋体"}[MVRP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[，此时既可以处理]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[报文，也可以处理]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo mvrp gvrp-compliance enable]{lang="EN-US"}**]{#struct_0_x2137_27564_1902678447}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x401094532}

[**[mvrp gvrp-compliance enable]{lang="EN-US"}**]{#struct_0_x2137_27564_x843857173}

[**[undo mvrp gvrp-compliance enable]{lang="EN-US"}**]{#struct_0_x2137_27564_1631832776}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2134971668}

[[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x1554738512}[不兼容]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x1521995459}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2137_27564_1230618509}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x2033796687}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_580502980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1470813095}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_132561986}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_1689734411}[配置]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_2134906132}

[\[Sysname\] mvrp gvrp-compliance enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1977687576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_x541819963}
:::

::: {#972291904 .myid}
[]{#_Toc404784186}[]{#struct_0_x2137_27564_x1610536126}[]{#_Toc309290873}[]{#_Toc300133533}

**MVRP \-- MVRP配置命令 \-- mvrp registration**

------------------------------------------------------------------------

[**[mvrp registration]{lang="EN-US"}**]{#struct_0_x2137_27564_1026903263}[命令用来配置端口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[注册模式。]{style="font-family:宋体"}

[**[undo mvrp registration]{lang="EN-US"}**]{#struct_0_x2137_27564_x45576052}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x344853842}

[**[mvrp registration]{lang="EN-US"}**[ { **fixed** \| **forbidden** \| **normal** }]{lang="EN-US"}]{#struct_0_x2137_27564_x888169165}

[**[undo]{lang="EN-US"}**[ **mvrp registration**]{lang="EN-US"}]{#struct_0_x2137_27564_15799332}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2134840596}

[[接口的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}]{#struct_0_x2137_27564_x398719077}[注册模式为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1269697748}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_27564_x167214141}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x34344182}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_794199531}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x1575170711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x211247977}

[**[fixed]{lang="EN-US"}**]{#struct_0_x2137_27564_251807375}[：表示]{style="font-family:宋体"}[Fixed]{lang="EN-US"}[注册模式。]{style="font-family:宋体"}

[**[forbidden]{lang="EN-US"}**]{#struct_0_x2137_27564_x1027695923}[：表示]{style="font-family:宋体"}[Forbidden]{lang="EN-US"}[注册模式。]{style="font-family:宋体"}

[**[normal]{lang="EN-US"}**]{#struct_0_x2137_27564_2134775060}[：表示]{style="font-family:宋体"}[Normal]{lang="EN-US"}[注册模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_31768954}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_666862289}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[注册模式为]{style="font-family:宋体"}[Fixed]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_27564_x2020860339}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mvrp registration fixed]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1555619299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp running-status]{lang="EN-US"}**]{#struct_0_x2137_27564_x978037484}
:::

::: {#-1614100115 .myid}
[]{#_Toc404784187}[]{#struct_0_x2137_27564_1600080026}[]{#_Toc309290874}

**MVRP \-- MVRP配置命令 \-- reset mvrp statistics**

------------------------------------------------------------------------

[**[reset mvrp statistics]{lang="EN-US"}**]{#struct_0_x2137_27564_x997383189}[命令用来清除端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_2135758100}

[**[reset mvrp statistics]{lang="EN-US"}**[ \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x2137_27564_x411456173}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_27564_87997400}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2137_27564_781142454}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1259060515}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x871422704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_27564_x371266635}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x841237124}

[**[interface]{lang="EN-US"}***[ interface-list]{lang="EN-US"}*]{#struct_0_x2137_27564_2135692564}[：清除指定端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为以太网端口列表，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[＝]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[ \[ **to** *interface-type interface-number* \]]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定该参数，则清除所有端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_27564_1151398420}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_27564_335989262}[清除所有端口上的]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset mvrp statistics]{lang="EN-US"}]{#struct_0_x2137_27564_459026927}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_27564_x640144783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mvrp statistics]{lang="EN-US"}**]{#struct_0_x2137_27564_1631403606}
:::
