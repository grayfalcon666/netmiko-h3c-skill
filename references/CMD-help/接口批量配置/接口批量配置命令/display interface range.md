::: {#-16371987 .myid}
[]{#_Toc404783361}[]{#struct_0_x1084_x1389_x623515606}[]{#_Toc329784476}[]{#_Toc320284586}[]{#_Toc250564049}

**接口批量配置 \-- 接口批量配置命令 \-- display interface range**

------------------------------------------------------------------------

[**[display interface range]{lang="EN-US"}**]{#struct_0_x1084_x1389_578986855}[命令用来]{style="font-family:宋体"}[显示通过]{style="font-family:宋体"}**[interface range name]{lang="EN-US"}**[命令]{style="font-family:宋体"}[创建的批量接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_80527402}

[**[display interface range ]{lang="EN-US"}**[\[ **name** ]{lang="EN-US"}*[name]{lang="EN-US" style="color:black"}[ ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_x1084_x1389_441259546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x445428196}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1084_x1389_x1768900796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x196976842}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1389_x766046276}

[[network-operator]{lang="EN-US"}]{#struct_0_x1084_x1389_x1659577344}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1389_x1453728419}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1084_x1389_910749706}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_406232797}

[**[name ]{lang="EN-US"}***[name]{lang="EN-US" style="color:black"}*]{#struct_0_x1084_x1389_1599500000}[：设备上已创建的批量接口的别名，]{style="font-family:
宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，显示当前设备中所有]{style="font-family:宋体"}[已创建的批量接口的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_707942409}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1389_120122624}[显示当前设备中所有通过]{style="font-family:宋体"}**[interface range name]{lang="EN-US"}**[命令]{style="font-family:宋体"}[创建的批量接口的信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display interface range]{lang="EN-US"}]{#struct_0_x1084_x1389_x1529414151}

[Interface range name t2 gigabitethernet 1/0/1 gigabitethernet 1/0/2]{lang="EN-US"}

[Interface range name test gigabitethernet 1/0/11 gigabitethernet 1/0/12]{lang="EN-US"}

[[以上显示信息表明：批量接口]{style="font-family:宋体"}[t2]{lang="EN-US"}]{#struct_0_x1084_x1389_x623538162}[下绑定了接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，批量接口]{style="font-family:宋体"}[test]{lang="EN-US"}[下绑定了接口]{style="font-family:宋体"}[GigabitEthernet1/0/11]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_2110760470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface range name]{lang="EN-US"}**]{#struct_0_x1084_x1389_x220268406}
:::

::: {#-1610097578 .myid}
[]{#_Toc404783362}[]{#struct_0_x1084_x1389_x1383684722}

**接口批量配置 \-- 接口批量配置命令 \-- interface range**

------------------------------------------------------------------------

[**[interface range]{lang="EN-US"}**]{#struct_0_x1084_x1389_x1479763784}[命令用来]{style="font-family:宋体;color:black"}[绑定一组接口，并进入接口批量配置视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_650063532}

[**[interface range]{lang="EN-US"}***[ interface-list]{lang="EN-US"}*]{#struct_0_x1084_x1389_x1769425083}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_432405109}

[[系统视图]{style="font-family:宋体;color:black"}]{#struct_0_x1084_x1389_2087490433}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x1482658952}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1389_x1796874003}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1389_590676852}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x293029785}

[*[interface-list]{lang="EN-US"}*]{#struct_0_x1084_x1389_x815133754}[：接口列表，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ ]{lang="EN-US"}[＝]{style="font-family:宋体"}[ { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-5\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}[&\<1-5\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}[当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字指定接口范围时（形如]{style="font-family:宋体"}*[interface-type interface-number1]{lang="EN-US"}*[ **to** *interface-type interface-number2*]{lang="EN-US"}[），则]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字左边[的接口（起始接口）和]{style="color:black"}]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字右边的接口（结束接口）必须位于同一接口卡或子卡上，并且起始接口编号中最后一维的值必须小于等于结束接口的编号中最后一维的值，其它维的值必须相等。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_1787458630}

[[当多个接口需要配置某功能（比如]{style="font-family:宋体;color:black"}[shutdown]{lang="EN-US" style="color:black"}]{#struct_0_x1084_x1389_1441976856}[）时，需要逐个进入接口视图，在每个接口执行一遍命令，比较繁琐。]{style="font-family:
宋体;color:black"}**[interface range]{lang="EN-US"}**[命令提供了一种批量配置方式。使用该命令可以将不同类型的接口进行绑定，]{style="font-family:宋体;color:black"}[并进入接口批量配置视图。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口批量配置视图下，只能执行接口列表中第一个接口支持]{style="font-family:宋体"}]{#struct_0_x1084_x1389_x1769490619}[的命令，不能执行第一个接口不支持但其它成员接口支持的命令。（接口列表中]{style="font-family:宋体"}[的第一个接口指的是执行]{style="font-family:宋体"}**[interf[ace range]{style="color:black"}]{lang="EN-US"}**[命令]{style="font-family:宋体;
color:black"}[时]{style="font-family:宋体;color:black"}[指定的第一个接口]{style="font-family:宋体;color:black"}[）。在]{style="font-family:
宋体"}[接口批量配置视图下，输入问号并回车，将]{style="font-family:宋体"}[显示该视图下支持的所有命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口批量配置视图下执行命令，会在绑定的所有接口下执行该命令：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1084_x1389_2145231455}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当命令执行完成后，系统提示配置失败并保持在接口批量配置视图，如果配置失败的接口是接口列表的第一个接口，则表示列表中的所有接口都没有配置该命令；如果配置失败的接口是其它接口，则表示除了提示失败的接口外，其它接口都已经配置成功。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1084_x1389_x803558485}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果命令执行完成后，退回到系统视图，则表示这条命令在接口视图和系统视图下都支持，并且在列表中的某个接口上配置失败，在系统视图下配置成功，列表中位于这个接口后面的接口不再执行该命令。此时，可到列表中各接口的视图下使用]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**]{#struct_0_x1084_x1389_2120717859}[命令验证配置效果，同时如果不需要在系统视图下配置该命令的话，请使用相应的]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令取消该配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1084_x1389_827692376}[接口批量配置视图下，执]{style="font-family:
宋体"}[行]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令，]{lang="EN-US" style="font-family:宋体"}[将显示接口列表中第一个接口当前生效的配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1084_x1389_x1802058664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无法通过]{lang="EN-US" style="font-family:宋体"}**[interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_x1084_x1389_700013766}[命令进入接口视图的接口（比如]{lang="EN-US" style="font-family:宋体"}[BRI1/1/1:1]{lang="EN-US"}[等]{lang="EN-US" style="font-family:宋体"}[），不能被设置为接口列表的第一个接口。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合口加入[批量接口时]{style="color:black"}，建议不要将该聚合口的成员接口也加入，否则在[批量接口配置视图下]{style="color:black"}执行某些配置命令时，可能会导致聚合分裂]{style="font-family:宋体"}]{#struct_0_x1084_x1389_x2101057516}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[批量接口包含的接口数量]{style="font-family:宋体;color:black"}]{#struct_0_x1084_x1389_2056298747}[没有上限，仅受系统资源限制。[接口数量较多时，]{style="color:black"}在[批量接口配置视图下执行命令等待的时间将较长。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_524729634}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1389_x1598195858}[关闭接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"}[GigabitEthernet1/0/24]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[Serial2/1/1]{lang="EN-US"}[到]{style="font-family:宋体"}[Serial2/1/7]{lang="EN-US"}[。]{style="font-family:宋体;color:black"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1389_x1529545223}

[\[Sysname\] interface range gigabitethernet 1/0/1 to gigabitethernet 1/0/24 vlan-interafce 2 serial 2/1/1 to serial 2/1/7]{lang="EN-US"}

[\[Sysname-if-range\] shutdown]{lang="EN-US"}
:::

::: {#209070664 .myid}
[]{#_Toc404783363}[]{#struct_0_x1084_x1389_x1847479978}

**接口批量配置 \-- 接口批量配置命令 \-- interface range name**

------------------------------------------------------------------------

[**[interface range]{lang="EN-US" style="color:black"}**[ **name** *name* **interface** ]{lang="EN-US" style="color:black"}*[interface-list]{lang="EN-US"}*]{#struct_0_x1084_x1389_x636411888}[命令用来绑定一组接口，为这组接口指定一个别名，并使用该别名进入接口批量配置视图。]{style="font-family:宋体"}

[**[interface range name ]{lang="EN-US"}***[name]{lang="EN-US" style="color:black"}*]{#struct_0_x1084_x1389_886533631}[（不带]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[参数时）命令用来使用别名进入接口批量配置视图。]{style="font-family:宋体"}

[**[undo interface range name]{lang="EN-US"}**]{#struct_0_x1084_x1389_1955670359}[命令用来取消接口绑定，删除接口别名。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x157997878}

[**[interface range]{lang="EN-US" style="color:black"}**[ **name** *name* ]{lang="EN-US" style="color:black"}[\[ **[interface]{style="color:black"}**[ ]{style="color:black"}*interface-list* \]]{lang="EN-US"}]{#struct_0_x1084_x1389_1155318444}

[**[undo ]{lang="EN-US" style="color:black"}[interface range name]{lang="EN-US" style="color:black"}**[ *name*]{lang="EN-US" style="color:black"}]{#struct_0_x1084_x1389_x1876506104}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x1769359547}

[[系统视图]{style="font-family:宋体;color:black"}]{#struct_0_x1084_x1389_553264091}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_1063519453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1389_x1500110103}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1389_x334932203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_1429064750}

[*[name]{lang="EN-US" style="color:black"}*]{#struct_0_x1084_x1389_324886903}[：批量接口的别名，]{style="font-family:
宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[interface-list]{lang="EN-US"}*]{#struct_0_x1084_x1389_x1068739748}[：接口列表，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-5\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}[&\<1-5\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}[当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字指定接口范围时（形如]{style="font-family:宋体"}*[interface-type interface-number1]{lang="EN-US"}*[ **to** *interface-type interface-number2*]{lang="EN-US"}[），则]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字左边[的接口（起始接口）和]{style="color:black"}]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字右边的接口（结束接口）必须位于同一接口卡或子卡上，并且起始接口编号中最后一维的值必须小于等于结束接口的编号中最后一维的值，其它维的值必须相等。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x1228089524}

[[当多个接口需要配置某功能（比如]{style="font-family:宋体;color:black"}[shutdown]{lang="EN-US" style="color:black"}]{#struct_0_x1084_x1389_916200244}[）时，需要逐个进入接口视图，在每个接口执行一遍命令，比较繁琐。]{style="font-family:宋体;color:black"}**[interface range name]{lang="EN-US"}**[命令提供了一种批量配置方式。使用该命令可以将不同类型的接口进行绑定，并进入接口批量配置视图。在接口批量配置视图下执行的配置命令，对绑定的所有成员接口生效。]{style="font-family:宋体"}

[**[interface range]{lang="EN-US" style="color:black"}**[ **name**]{lang="EN-US" style="color:black"}]{#struct_0_x1084_x1389_x1769162939}[和]{style="font-family:宋体"}**[interface range]{lang="EN-US"}**[命令都能提供接口[批量配置功能，它们的差别在于：]{style="color:black"}]{style="font-family:宋体"}**[interface range]{lang="EN-US" style="color:black"}**[ **name**]{lang="EN-US" style="color:black"}[命令在绑定接口的时候可以定义一个别名，可以进行多次绑定，给不同的绑定定义不同的别名，以示区别，方便记忆。并且，后续可以使用别名直接进入接口批量配置视图，不再需要输出一长串的接口列表，配置起来更简便。用户可以使用]{style="font-family:宋体"}**[display [interface range]{style="color:black"}]{lang="EN-US"}**[命令来查看绑定了哪些接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口批量配置视图下，只能执行接口列表中第一个接口支持]{style="font-family:宋体"}]{#struct_0_x1084_x1389_1770087064}[的命令，不能执行第一个接口不支持但其它成员接口支持的命令。（接口列表中]{style="font-family:宋体"}[的第一个接口指的是执行]{style="font-family:宋体"}**[interf[ace range]{style="color:black"}]{lang="EN-US"}**[命令]{style="font-family:宋体;
color:black"}[时]{style="font-family:宋体;color:black"}[指定的第一个接口]{style="font-family:宋体;color:black"}[）。在]{style="font-family:
宋体"}[接口批量配置视图下，输入问号并回车，将]{style="font-family:宋体"}[显示该视图下支持的所有命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口批量配置视图下执行命令，会在绑定的所有接口下执行该命令：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1084_x1389_2145100383}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当命令执行完成后，系统提示配置失败并保持在接口批量配置视图，如果配置失败的接口是接口列表的第一个接口，则表示列表中的所有接口都没有配置该命令；如果配置失败的接口是其它接口，则表示除了提示失败的接口外，其它接口都已经配置成功。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1084_x1389_x1956694276}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果命令执行完成后，退回到系统视图，则表示这条命令在接口视图和系统视图下都支持，并且在列表中的某个接口上配置失败，在系统视图下配置成功，列表中位于这个接口后面的接口不再执行该命令。此时，可到列表中各接口的视图下使用]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**]{#struct_0_x1084_x1389_82538620}[命令验证配置效果，同时如果不需要在系统视图下配置该命令的话，请使用相应的]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令取消该配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1084_x1389_x1584603621}[接口批量配置视图下，执行]{lang="EN-US" style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令，将]{lang="EN-US" style="font-family:宋体"}[显示接口列表中第一个接口当前生效的配置。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1084_x1389_107362619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无法通过]{lang="EN-US" style="font-family:宋体"}**[interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_x1084_x1389_2105602158}[命令进入接口视图的接口（比如]{lang="EN-US" style="font-family:宋体"}[BRI1/1/1:1]{lang="EN-US"}[等]{lang="EN-US" style="font-family:宋体"}[），不能被设置为接口列表的第一个接口。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合口加入[批量接口时]{style="color:black"}，建议不要将该聚合口的成员接口也加入，否则在[批量接口配置视图下]{style="color:black"}执行某些配置命令时，可能会导致聚合分裂]{style="font-family:宋体"}]{#struct_0_x1084_x1389_1357327994}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[批量接口包含的接口数量]{style="font-family:宋体;color:black"}]{#struct_0_x1084_x1389_x1307511568}[没有上限，仅受系统资源限制。[接口数量较多时，]{style="color:black"}在[批量接口配置视图下执行命令等待的时间将较长。]{style="color:black"}]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统中支持的批量接口别名的个数没有上限，仅受系统资源限制。推荐用户配置]{style="font-family:宋体"}]{#struct_0_x1084_x1389_x2123466335}[1000]{lang="EN-US"}[个以下，配置数量过多，可能引起该特性执行效率降低。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x1769228475}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1389_1022562619}[将]{style="font-family:宋体"}[12]{lang="EN-US"}[个以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/12]{lang="EN-US"}[定义为]{style="font-family:宋体"}[myEthPort]{lang="EN-US"}[，并进入批量接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1389_1277920488}

[\[Sysname\] interface range name myEthPort interface gigabitethernet 1/0/1 to gigabitethernet 1/0/12]{lang="EN-US"}

[\[Sysname-if-range-myEthPort\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1389_19535775}[进入]{style="font-family:宋体"}[myEthPort]{lang="EN-US"}[别名对应的批量接口配置视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1389_x1529217536}

[\[Sysname\] interface range name myEthPort]{lang="EN-US"}

[\[Sysname-if-range-myEthPort\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1389_x595677360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[interface range]{lang="EN-US"}**]{#struct_0_x1084_x1389_x1769031867}

[ ]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}
:::
