::: {#-454064564 .myid}
[]{#_Toc404784749}[]{#struct_0_x1401_20040_x1895901445}[]{#_Toc174449605}

**业务环回组 \-- 业务环回组配置命令 \-- display service-loopback group**

------------------------------------------------------------------------

[**[display service-loopback group]{lang="EN-US"}**]{#struct_0_x1401_20040_2141656344}[命令用来显示业务环回组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x1700889607}

[**[display service-loopback group ]{lang="EN-US"}**[\[ *number* \]]{lang="EN-US"}]{#struct_0_x1401_20040_1135025655}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1401_20040_1977601559}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1401_20040_247906341}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x518087390}

[[network-admin]{lang="EN-US"}]{#struct_0_x1401_20040_2031306316}

[[network-operator]{lang="EN-US"}]{#struct_0_x1401_20040_x1858789696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1401_20040_149395166}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1401_20040_1740169965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1401_20040_2141721880}

[*[number]{lang="EN-US"}*]{#struct_0_x1401_20040_667986889}[：显示指定业务环回组的信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为业务环回组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有业务环回组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x1443269720}

[[\# ]{lang="EN-US"}]{#struct_0_x1401_20040_447712195}[显示业务环回组]{style="font-family:宋体"}[5]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display service-loopback group 5]{lang="EN-US"}]{#struct_0_x1401_20040_1962715907}

[ ]{lang="EN-US"}

[Service Group ID: 5       Service Type: Tunnel]{lang="EN-US"}

[Member:]{lang="EN-US"}

[ GigabitEthernet1/0/1]{lang="EN-US"}

[ GigabitEthernet1/0/2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display service-loopback group]{lang="EN-US"}]{#struct_0_x1401_20040_732207730}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1997701999}[[字段]{style="font-family:黑体"}]{#struct_0_x1401_20040_x921393729}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1401_20040_1431330506}

[[Service Group ID]{lang="EN-US"}]{#struct_0_x1401_20040_x2135354050}

[[业务环回组的编号]{style="font-family:宋体"}]{#struct_0_x1401_20040_2141787416}

[[Service Type]{lang="EN-US"}]{#struct_0_x1401_20040_x2077233106}

[[业务环回组的业务类型：]{style="font-family:宋体"}]{#struct_0_x1401_20040_1197033697}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multicast-tunnel]{lang="EN-US"}]{#struct_0_x1401_20040_x350356781}[：表示组播隧道业务类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tunnel]{lang="EN-US"}]{#struct_0_x1401_20040_1841772174}[：表示单播隧道业务类型]{style="font-family:宋体"}

[[Member]{lang="EN-US"}]{#struct_0_x1401_20040_958093894}

[[业务环回组的成员端口]{style="font-family:宋体"}]{#struct_0_x1401_20040_1965617550}

[ ]{lang="EN-US"}

::: {#-950987923 .myid}
[]{#_Toc404784750}[]{#struct_0_x1401_20040_2141852952}[]{#_Toc174449607}

**业务环回组 \-- 业务环回组配置命令 \-- port service-loopback group**

------------------------------------------------------------------------

[**[port service-loopback group]{lang="EN-US"}**]{#struct_0_x1401_20040_x1286583012}[命令用来将端口加入指定的业务环回组。]{style="font-family:
宋体"}

[**[undo port service-loopback group]{lang="EN-US"}**]{#struct_0_x1401_20040_16188461}[命令用来将端口从业务环回组中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1401_20040_951246486}

[**[port service-loopback group]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x1401_20040_1337128114}

[**[undo]{lang="EN-US"}**[ **port** **service-loopback group**]{lang="EN-US"}]{#struct_0_x1401_20040_x275990059}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1401_20040_1069613793}

[[端口不属于任何业务环回组。]{style="font-family:宋体"}]{#struct_0_x1401_20040_1961865570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1401_20040_1624086992}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1401_20040_2141918488}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x951199012}

[[network-admin]{lang="EN-US"}]{#struct_0_x1401_20040_x1089658300}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1401_20040_x310121058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1401_20040_1968266620}

[*[number]{lang="EN-US"}*]{#struct_0_x1401_20040_x1663234130}[：指定业务环回组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x1491698271}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在将端口加入业务环回组时，该端口上已存在的所有配置都将被清除。]{style="font-family:宋体"}]{#struct_0_x1401_20040_x921498808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个端口只允许加入一个业务环回组，且必须支持该业务环回组的业务类型。]{style="font-family:宋体"}]{#struct_0_x1401_20040_x912415184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过在不同端口上执行本命令，可以将多个端口加入到业务环回组中。]{style="font-family:宋体"}]{#struct_0_x1401_20040_x1045352330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果端口是一个已被引用的业务环回组中唯一的成员端口，那么该端口退出该业务环回组将导致单播隧道或组播隧道尚未]{style="font-family:宋体"}]{#struct_0_x1401_20040_x1772753638}[down]{lang="EN-US"}[时就发生流量中断。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1401_20040_2141984024}[端口不属于任何业务环回组]{lang="EN-US" style="font-family:宋体"}[，则在该端口上不能执行]{style="font-family:宋体"}**[undo port service-loopback group]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1401_20040_1416455070}

[[\# ]{lang="EN-US"}]{#struct_0_x1401_20040_879714927}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[加入业务环回组]{style="font-family:宋体"}[5]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1401_20040_782850280}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port service-loopback group 5]{lang="EN-US"}
:::

::: {#-2127202607 .myid}
[]{#_Toc404784751}[]{#struct_0_x1401_20040_x530578707}[]{#_Toc174449606}

**业务环回组 \-- 业务环回组配置命令 \-- service-loopback group**

------------------------------------------------------------------------

[**[service-loopback group]{lang="EN-US"}**]{#struct_0_x1401_20040_1535477579}[命令用来创建业务环回组，并指定其业务类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **service-loopback group**]{lang="EN-US"}]{#struct_0_x1401_20040_135837380}[命令用来删除业务环回组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x1120549021}

[**[service-loopback group]{lang="EN-US"}**[ *number* **type** { **multicast-tunnel** \| **tunnel** } \*]{lang="EN-US"}]{#struct_0_x1401_20040_x1261487407}

[**[undo service-loopback group ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1401_20040_2142049560}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x696626994}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1401_20040_1369051045}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1401_20040_x1123104661}

[[network-admin]{lang="EN-US"}]{#struct_0_x1401_20040_x1089594514}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1401_20040_x1604437220}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1401_20040_525666664}

[*[number]{lang="EN-US"}*]{#struct_0_x1401_20040_x1494394571}[：指定业务环回组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**]{#struct_0_x1401_20040_687082448}[：指定业务环回组的业务类型。]{style="font-family:宋体"}

[**[multicast-tunnel]{lang="EN-US"}**]{#struct_0_x1401_20040_1966729966}[：指定业务类型为]{style="font-family:宋体"}[Multicast tunnel]{lang="EN-US"}[（组播隧道）类型。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}**]{#struct_0_x1401_20040_2141066520}[：指定业务类型为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[（单播隧道）类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1401_20040_1458011061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[业务环回组只有在被其他特性引用后才能处理业务。业务环回组一旦创建即可被引用，且一个业务环回组可以同时被多个特性引用。]{style="font-family:宋体"}]{#struct_0_x1401_20040_x1421037444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每种业务类型的业务环回组在全局只能有一个。]{style="font-family:宋体"}]{#struct_0_x1401_20040_x431969111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[业务环回组创建后不允许再更改其业务类型。]{style="font-family:宋体"}]{#struct_0_x1401_20040_562631478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不建议删除已被其他特性引用的业务环回组。]{style="font-family:宋体"}]{#struct_0_x1401_20040_706433178}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1401_20040_292728456}

[[\# ]{lang="EN-US"}]{#struct_0_x1401_20040_x68266837}[创建业务环回组]{style="font-family:宋体"}[5]{lang="EN-US"}[，并指定其业务类型为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1401_20040_x72048554}

[\[Sysname\] service-loopback group 5 type tunnel]{lang="EN-US"}
:::
