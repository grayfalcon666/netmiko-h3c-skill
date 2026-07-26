::: {#-1506715290 .myid}
[]{#_Toc361382004}[]{#_Toc345167280}[]{#_Toc404782969}[]{#struct_0_21314_23244_x1227908547}[]{#_Toc361382006}[]{#_Toc345167282}

**安全域 \-- 安全域配置命令 \-- display security-zone**

------------------------------------------------------------------------

[**[display ]{lang="EN-US"}[security-zone]{lang="EN-US"}**]{#struct_0_21314_23244_x896285436}[命令用]{style="font-family:宋体"}[来显示]{style="font-family:宋体"}[安全域信息，包括]{style="font-family:宋体"}[缺省安全域和自定义的]{style="font-family:宋体"}[安全域信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_695370577}

[**[display ]{lang="EN-US" style="color:black"}[security-zone]{lang="EN-US"}**]{#struct_0_21314_23244_x1181368453}[ \[ **name**]{lang="EN-US" style="color:black"}**[ ]{lang="EN-US" style="color:black"}***[zone-name ]{lang="EN-US" style="color:black"}*[\]]{lang="EN-US" style="color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_1238766702}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21314_23244_1759259524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_x896219900}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x1952904176}

[[network-operator]{lang="EN-US"}]{#struct_0_21314_23244_1642454572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_x2015661852}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21314_23244_x1527397060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_669274222}

[**[name ]{lang="EN-US"}**]{#struct_0_21314_23244_x1917628180}*[zone-name]{lang="EN-US"}*[：安全域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。若不指定本参数，则显示所有安全域的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_x479128060}

[[安全域的显示顺序是先显示缺省安全域信息，再按照安全域名称的字母排序显示自定义的安全域信息。]{style="font-family:宋体"}]{#struct_0_21314_23244_1450925342}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_1100995815}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x1548523061}[显示安全域]{style="font-family:宋体;color:black"}[myZone]{lang="EN-US"}[的信息]{style="font-family:宋体;color:black"}[。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display security-zone name myZone]{lang="EN-US"}]{#struct_0_21314_23244_1870080451}

[[Name: myZone]{lang="EN-US"}]{#struct_0_21314_23244_669339758}

[Members:]{lang="EN-US"}

[  GigabitEthernet1/0/3]{lang="EN-US"}

[  GigabitEthernet1/0/4]{lang="EN-US"}

[  GigabitEthernet1/1/1 in VLAN 3]{lang="EN-US"}

[  GigabitEthernet1/1/5 in VLAN 7]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x377586308}[显示安全区域]{style="font-family:宋体;color:black"}[myZone]{lang="EN-US"}[信息]{style="font-family:宋体;color:black"}[。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display security-zone name myZone]{lang="EN-US"}]{#struct_0_21314_23244_669208686}

[Name: myZone]{lang="EN-US"}

[Members:]{lang="EN-US"}

[  GigabitEthernet1/1/1]{lang="EN-US"}

[  GigabitEthernet1/1/2]{lang="EN-US"}

[  VLAN 150-200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x1608626782}[显示安全域]{style="font-family:宋体"}[IPZone]{lang="EN-US"}[的信息。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display security-zone name IPZone]{lang="EN-US"}]{#struct_0_21314_23244_x882391966}

[Name: IPZone]{lang="EN-US"}

[Members:]{lang="EN-US"}

[  192.168.1.0 255.255.255.0]{lang="EN-US"}

[  192.168.0.0 255.255.0.0 vpn-instance abc]{lang="EN-US"}

[  1001:1002::0 32]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}**[display]{lang="EN-US"}**]{#struct_0_21314_23244_x1176111971}[ ]{lang="EN-US"}**[security-zone]{lang="EN-US"}**[命令输出信息描述]{style="font-family:黑体"}

[]{#table_struct_0_218935573}[[字段]{style="font-family:黑体"}]{#struct_0_21314_23244_669012078}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21314_23244_x217630002}

[[Name]{lang="EN-US"}]{#struct_0_21314_23244_x2089430305}

[[安全域名称]{style="font-family:宋体"}]{#struct_0_21314_23244_2073976811}

[[Members]{lang="EN-US"}]{#struct_0_21314_23244_x1387535650}

[[安全域成员，包括以下几种取值：]{style="font-family:宋体"}]{#struct_0_21314_23244_1070589120}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层接口名称]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21314_23244_x852223249}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口名称]{style="font-family:宋体"}]{#struct_0_21314_23244_669077614}[和所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_21314_23244_2102993746}[编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网中]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21314_23244_1120256573}[的]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[子网]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网中]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21314_23244_x641316115}[的]{style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[子网]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPN]{lang="EN-US"}]{#struct_0_21314_23244_2006340969}[中]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[子网]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPN]{lang="EN-US"}]{#struct_0_21314_23244_x445827368}[中]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_21314_23244_x1283284607}[，该安全域中没有任何成员]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#2090415285 .myid}
[]{#_Toc404782970}[]{#struct_0_21314_23244_678754492}[]{#_Toc361382009}[]{#_Toc345167285}[]{#_Toc361932898}[]{#_Toc361932913}[]{#_Toc361932899}[]{#_Toc361932914}

**安全域 \-- 安全域配置命令 \-- display zone-pair security**

------------------------------------------------------------------------

[**[display zone-pair security]{lang="EN-US"}**]{#struct_0_21314_23244_167652241}[命令用]{style="font-family:
宋体"}[来显示已创建的所有]{style="font-family:宋体"}[域间实例的]{style="font-family:宋体;color:black"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_x2079646312}

[**[display ]{lang="EN-US" style="color:black"}[zone-pair security]{lang="EN-US"}**]{#struct_0_21314_23244_x896940796}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_x499702125}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21314_23244_1710898452}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_x277108487}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x896875260}

[[network-operator]{lang="EN-US"}]{#struct_0_21314_23244_291079288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_x1629679801}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21314_23244_1784023802}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_1938621142}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x897071868}[显示所有安全域间实例的信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> display **zone-pair security**]{lang="EN-US"}]{#struct_0_21314_23244_x897006332}

[ Source zone   Destination zone]{lang="EN-US"}

[ DMZ           Local]{lang="EN-US"}

[ Trust         Local]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}**[display]{lang="EN-US"}**]{#struct_0_21314_23244_x457765256}[ ]{lang="EN-US"}**[zone-pair security]{lang="EN-US"}**[命令输出信息描述]{style="font-family:黑体"}

[]{#table_struct_0_225605141}[[字段]{style="font-family:黑体"}]{#struct_0_21314_23244_358591394}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21314_23244_525859145}

[[Source zone]{lang="EN-US"}]{#struct_0_21314_23244_x897202940}

[[源安全域名称]{style="font-family:宋体"}]{#struct_0_21314_23244_x871547831}

[[Destination zone]{lang="EN-US"}]{#struct_0_21314_23244_414533990}

[[目的安全域名称]{style="font-family:宋体"}]{#struct_0_21314_23244_x897137404}

[ ]{lang="EN-US"}

::: {#1592927346 .myid}
[]{#_Toc404782971}[]{#struct_0_21314_23244_x322257783}[]{#_Toc339630669}[]{#_Toc361382005}[]{#_Toc322446699}[]{#_Toc322446704}

**安全域 \-- 安全域配置命令 \-- import interface**

------------------------------------------------------------------------

[**[import ]{lang="EN-US" style="color:black"}**]{#struct_0_21314_23244_x1682994157}**[interface]{lang="EN-US"}**[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[向安全域中添加三层接口成员，包括三层以太网接口、三层以太网子接口和其它三层逻辑接口。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21314_23244_x1937882022}**[import ]{lang="EN-US" style="color:black"}[interface]{lang="EN-US"}**[命令用来从安全域中移除]{style="font-family:宋体"}[三层接口成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1364067093}

[**[import]{lang="EN-US"}**]{#struct_0_21314_23244_1725433899}[ **interface ** ]{lang="EN-US"}*[lay3-]{lang="EN-US"}[interface-type ]{lang="EN-US"}[lay3-]{lang="EN-US"}[interface-number]{lang="EN-US"}*

[**[undo import]{lang="EN-US"}**]{#struct_0_21314_23244_1444517723}[ **interface ** ]{lang="EN-US"}*[lay3-]{lang="EN-US"}[interface-type ]{lang="EN-US"}[lay3-]{lang="EN-US"}[interface-number]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_x2089053899}

[[安全域中不存在任何成员。]{style="font-family:宋体"}]{#struct_0_21314_23244_668946542}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_x524312563}

[[安全域视图]{style="font-family:宋体"}]{#struct_0_21314_23244_x822613434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1226416280}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_2107366468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_1225392122}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_x846258885}

[*[lay3-]{lang="EN-US"}*]{#struct_0_21314_23244_1491571890}*[interface-type ]{lang="EN-US"}[lay3-]{lang="EN-US"}[interface-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[指定添加到安全域的三层接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_x727933213}

[[可以通过多次执行本命令向同一个安全域添加多个三层接口成员。]{style="font-family:宋体"}]{#struct_0_21314_23244_669798510}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21314_23244_1526403892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个三层接口只允许加入一个安全域。]{style="font-family:宋体"}]{#struct_0_21314_23244_1842516277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要修改接口所属安全域，需要首先在相应安全域中使用]{lang="EN-US" style="font-family:宋体"}**[undo import]{lang="EN-US"}**]{#struct_0_21314_23244_x1786718965}[命令将相应接口从原安全域中删除，再使用]{lang="EN-US" style="font-family:宋体"}**[import]{lang="EN-US"}**[命令将其加入其它安全域。其中，缺省的安全域]{lang="EN-US" style="font-family:宋体"}[Local]{lang="EN-US"}[中不允许添加任何接口，其它缺省的安全域中允许添加接口。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1972482001}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_669864046}[向安全域]{style="font-family:宋体"}[Trust]{lang="EN-US"}[中添加三层以太网接口]{style="font-family:宋体"}[Ethernet1/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_x768198145}

[\[Sysname\] security-zone name trust]{lang="EN-US"}

[\[Sysname-security-zone-trust\] import interface ethernet 1/1]{lang="EN-US"}
:::

::::: {#1475135274 .myid}
[]{#_Toc404782972}[]{#struct_0_21314_23244_x74512051}[]{#_Toc401928843}[]{#_Toc401928844}

**安全域 \-- 安全域配置命令 \-- import interface vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](安全域命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_21314_23244_1847736714}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21314_23244_x1704097836}
:::

[ ]{lang="EN-US"}

[**[import ]{lang="EN-US" style="color:black"}[interface vlan]{lang="EN-US"}**]{#struct_0_21314_23244_x822764677}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[向安全域中添加二层接口和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21314_23244_1511403278}**[import ]{lang="EN-US" style="color:black"}[interface vlan]{lang="EN-US"}**[命令用来从安全域中移除]{style="font-family:宋体"}[二层接口和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_1833412302}

[**[import interface ]{lang="EN-US"}***[lay2-]{lang="EN-US"}*]{#struct_0_21314_23244_471727565}*[interface-type ]{lang="EN-US"}[lay2-]{lang="EN-US"}[interface-number]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*

[**[undo import interface ]{lang="EN-US"}***[lay2-]{lang="EN-US"}*]{#struct_0_21314_23244_139284015}*[interface-type ]{lang="EN-US"}[lay2-]{lang="EN-US"}[interface-number]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_1277188008}

[[安全域中不存在任何成员。]{style="font-family:宋体"}]{#struct_0_21314_23244_983142416}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_1385193425}

[[安全域视图]{style="font-family:宋体"}]{#struct_0_21314_23244_989725366}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_281652773}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x319263393}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_1042641953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1607944150}

[*[lay2-]{lang="EN-US"}*]{#struct_0_21314_23244_1681058501}*[interface-type ]{lang="EN-US"}[lay2-]{lang="EN-US"}[interface-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[指定添加到安全域的二层接口的接口类型和接口编号。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US" style="color:black"}**]{#struct_0_21314_23244_x1088302439}**[ ]{lang="EN-US" style="color:black"}***[vlan-list]{lang="EN-US"}*[：指定接口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}[vlan-list ]{lang="EN-US"}[＝]{style="font-family:宋体"} [{ *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为已创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[必须大于]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[。]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_809160528}

[[可以通过多次执行本命令]{style="font-family:宋体"}]{#struct_0_21314_23244_x222310451}[，向安全域中添加多个二层接口和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21314_23244_x1469382404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个二层接口和所属的]{style="font-family:宋体"}]{#struct_0_21314_23244_x1753940641}[VLAN]{lang="EN-US"}[只允许加入一个安全域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要修改接口或者]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_21314_23244_1802480897}[所属安全域，需要首先在相应安全域中使用]{lang="EN-US" style="font-family:宋体"}**[undo import]{lang="EN-US"}**[命令将相应接口或者]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[从原安全域中删除，再使用]{lang="EN-US" style="font-family:宋体"}**[import]{lang="EN-US"}**[命令将其加入其它安全域。其中，缺省的安全域]{lang="EN-US" style="font-family:宋体"}[Local]{lang="EN-US"}[中不允许添加任何接口或者]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，其它缺省的安全域中允许添加接口和]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1294195859}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_1899799031}[向安全域]{style="font-family:宋体;color:black"}[Untrust]{lang="EN-US" style="color:black"}[中添加二层以太网接口]{style="font-family:宋体;
color:black"}[Ethernet1/1]{lang="EN-US" style="color:black"}[和对应的]{style="font-family:宋体;color:black"}[VLAN 10]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_684937300}

[\[Sysname\] security-zone name untrust]{lang="EN-US"}

[\[Sysname-security-zone-untrust\] import interface ethernet1/1 vlan 10]{lang="EN-US"}
:::::

::::: {#9594196 .myid}
[]{#_Toc404782973}[]{#struct_0_21314_23244_633120827}[]{#_Toc401928846}

**安全域 \-- 安全域配置命令 \-- import ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](安全域命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_21314_23244_1523541100}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21314_23244_127641559}
:::

[ ]{lang="EN-US"}

[**[import ip]{lang="EN-US"}**]{#struct_0_21314_23244_x1023765925}[命令用来向安全域中添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网成员。]{style="font-family:宋体"}

[**[undo import ip]{lang="EN-US"}**]{#struct_0_21314_23244_x42542841}[命令用来从安全域中删除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_1319740975}

[**[import ip]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21314_23244_1790575819}

[**[undo import ip]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21314_23244_724284889}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_2124992551}

[[安全域中不存在任何]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_21314_23244_x554561721}[子网成员。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_239304144}

[[安全域视图]{style="font-family:宋体"}]{#struct_0_21314_23244_2053298069}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_1583136032}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x569024375}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_x1964857142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_x981201141}

[*[ip-address]{lang="EN-US"}*]{#struct_0_21314_23244_x826230561}[：指定子网]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_21314_23244_x718536528}[：表示子网的掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_21314_23244_x46416971}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网相应的子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_21314_23244_x342495099}[：指定子网所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示设备中存在的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，表示子网位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_x813714556}

[[可以通过多次执行本命令，向安全域中添加多个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_21314_23244_x1231379159}[子网成员。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21314_23244_x2069175041}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[完全相同的子网不能添加到不同的安全域中，例如]{style="font-family:宋体"}]{#struct_0_21314_23244_x2113348183}[1.1.1.1/24]{lang="EN-US"}[与]{style="font-family:宋体"}[1.1.1.2/24]{lang="EN-US"}[相同，均对应]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[，不能分别添加到不同安全域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两个子网的网段有包含关系，例如]{style="font-family:宋体"}]{#struct_0_21314_23244_1943884319}[1.1.1.1/24]{lang="EN-US"}[与]{style="font-family:宋体"}[1.1.2.2/16]{lang="EN-US"}[，后者包含前者，但系统认为是两个不同子网，可以分别配置到同一安全域或者不同安全域。当配置到不同安全域时，报文最终将匹配掩码最长的子网所在的安全域。]{style="font-family:宋体"}[如]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[的报文]{style="font-family:宋体"}[会匹配到]{lang="EN-US" style="font-family:宋体"}[1.1.1.1/24]{lang="EN-US"}[所在的安全域。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_764026213}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x352632614}[添加地址为]{style="font-family:宋体"}[192.168.1.0]{lang="EN-US"}[、掩码长度为]{style="font-family:宋体"}[24]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网到安全域]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_x1446966892}

[\[Sysname\] security-zone name a]{lang="EN-US"}

[\[Sysname-security-zone-a\] import ip 192.168.1.0 24]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x1947753679}[添加地址为]{style="font-family:宋体"}[192.168.2.1]{lang="EN-US"}[、掩码为]{style="font-family:宋体"}[255.255.255.0]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网到安全域]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_205239301}

[\[Sysname\] security-zone name a]{lang="EN-US"}

[\[Sysname-security-zone-a\] import ip 192.168.2.1 255.255.255.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_846641691}[添加地址为]{style="font-family:宋体"}[192.168.2.1]{lang="EN-US"}[、掩码为]{style="font-family:宋体"}[255.255.255.0]{lang="EN-US"}[、]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网到安全域]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_x872798060}

[\[Sysname\] security-zone name a]{lang="EN-US"}

[\[Sysname-security-zone-a\] import ip 192.168.2.1 255.255.255.0 vpn-instance abc]{lang="EN-US"}
:::::

::::: {#-898023057 .myid}
[]{#_Toc404782974}[]{#struct_0_21314_23244_342187464}

**安全域 \-- 安全域配置命令 \-- import ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](安全域命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_21314_23244_1261131654}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21314_23244_1597425741}
:::

[ ]{lang="EN-US"}

[**[import ipv6]{lang="EN-US"}**]{#struct_0_21314_23244_x1608561246}[命令用来向安全域中添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网成员。]{style="font-family:宋体"}

[**[undo import ipv6]{lang="EN-US"}**]{#struct_0_21314_23244_x89296673}[命令用来从安全域中删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1404694593}

[**[import ipv6]{lang="EN-US"}**[ *ipv6-address prefix-length* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21314_23244_416752282}

[**[undo import ipv6]{lang="EN-US"}**[ *ipv6-address prefix-length* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21314_23244_x1616500700}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_1821035256}

[[安全域中不存在任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_21314_23244_1239471634}[子网成员。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_x598433795}

[[安全域视图]{style="font-family:宋体"}]{#struct_0_21314_23244_1516488796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_589539713}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_1245625450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_1239016894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_1120322109}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_21314_23244_x1827201735}[：指定子网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_21314_23244_1641666134}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_21314_23244_2021820400}[：指定子网所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示设备中存在的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，表示子网位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_x812767657}

[[可以通过多次执行本命令，向安全域中添加多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_21314_23244_x437762216}[子网成员。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21314_23244_x1731736595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[完全相同的]{style="font-family:宋体"}]{#struct_0_21314_23244_x459883906}[IPv6]{lang="EN-US"}[子网不能添加到不同的安全域中，例如]{style="font-family:宋体"}[1:1:1::1/32]{lang="EN-US"}[与]{style="font-family:宋体"}[1:1:1::2/32]{lang="EN-US"}[相同，均对应]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网]{style="font-family:宋体"}[1:1::0/32]{lang="EN-US"}[，不能分别添加到不同安全域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两个子网的网段有包含关系，例如]{style="font-family:宋体"}]{#struct_0_21314_23244_1663800636}[1:1:1::0/48]{lang="EN-US"}[与]{style="font-family:宋体"}[1:1:1::0/32]{lang="EN-US"}[，后者包含前者，但系统会认为是两个不同子网，可以分别配置到同一安全域或者不同安全域。当配置到不同安全域时，报文最终将匹配前缀最长的子网所在的安全域。]{style="font-family:宋体"}[如]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1:1:1::2]{lang="EN-US"}[的报文]{style="font-family:宋体"}[会匹配到]{lang="EN-US" style="font-family:宋体"}[1:1:1::0/48]{lang="EN-US"}[所在的安全域。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_x386641210}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_1284487622}[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网]{style="font-family:宋体"}[1001:1002::0/32]{lang="EN-US"}[添加到安全域]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_x445761832}

[\[Sysname\] security-zone name a]{lang="EN-US"}

[\[Sysname-security-zone-a\] import ipv6 1001:1002::1 32]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_1127974415}[将]{style="font-family:宋体"}[VPN abc]{lang="EN-US"}[中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网]{style="font-family:宋体"}[1001:1002::0/32]{lang="EN-US"}[添加到安全域]{style="font-family:宋体"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_1743478862}

[\[Sysname\] security-zone name a]{lang="EN-US"}

[\[Sysname-security-zone-a\] import ipv6 1001:1002::1 32 vpn-instance abc]{lang="EN-US"}
:::::

::::: {#1930196435 .myid}
[]{#_Toc404782975}[]{#struct_0_21314_23244_1643093039}[]{#_Toc401928849}

**安全域 \-- 安全域配置命令 \-- import vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](安全域命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_21314_23244_1061867325}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21314_23244_x655719677}
:::

[ ]{lang="EN-US"}

[**[import vlan]{lang="EN-US" style="color:black"}**]{#struct_0_21314_23244_x142794007}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[向安全域中添加]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21314_23244_893927173}**[import vlan]{lang="EN-US" style="color:black"}**[命令用来从安全域中移除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_1789049422}

[**[import ]{lang="EN-US"}**]{#struct_0_21314_23244_860702518}**[vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}

[**[undo import ]{lang="EN-US"}**]{#struct_0_21314_23244_x964262783}**[vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_x986510896}

[[安全域中不存在任何成员。]{style="font-family:宋体"}]{#struct_0_21314_23244_x881146641}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_x232903271}

[[安全域视图]{style="font-family:宋体"}]{#struct_0_21314_23244_x582592626}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_214457238}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x438726}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_1539840675}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_1793004569}

[**[vlan]{lang="EN-US" style="color:black"}**]{#struct_0_21314_23244_183773982}**[ ]{lang="EN-US" style="color:black"}***[vlan-list]{lang="EN-US"}*[：指定要加入安全区域的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}[vlan-list ]{lang="EN-US"}[＝]{style="font-family:宋体"} [{ *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为已创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[必须大于]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[。]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。属于这些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的所有二层以太网接口均属于该安全域。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_1716667641}

[[可以通过多次执行本命令，向安全域中添加多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_21314_23244_485587321}[成员。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21314_23244_x1508134698}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_21314_23244_x1890289469}[VLAN]{lang="EN-US"}[只允许加入一个安全域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要修改]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_21314_23244_x121631754}[所属安全域，需要首先在相应安全域中使用]{lang="EN-US" style="font-family:宋体"}**[undo import]{lang="EN-US"}**[命令将相应]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[从原安全域中删除，再使用]{lang="EN-US" style="font-family:宋体"}**[import]{lang="EN-US"}**[命令将其加入其它安全域。其中，缺省的安全域]{lang="EN-US" style="font-family:宋体"}[Local]{lang="EN-US"}[中不允许添加任何]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，其它缺省的安全域中允许添加]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_x247433672}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_755997880}[向安全域]{style="font-family:宋体;color:black"}[Trust]{lang="EN-US" style="color:black"}[中添加]{style="font-family:宋体;color:black"}[VLAN 3]{lang="EN-US" style="color:black"}[、]{style="font-family:宋体;
color:black"}[VLAN 5]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[VLAN 7]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_x517689013}

[\[Sysname\] security-zone name trust]{lang="EN-US"}

[\[Sysname-security-zone-trust\] import vlan 3 5 to 7]{lang="EN-US"}
:::::

::: {#1321736809 .myid}
[]{#_Toc404782976}[]{#struct_0_21314_23244_x217630007}[]{#_Toc401928851}[]{#_Toc401928852}[]{#_Toc398557330}[]{#_Toc398557677}[]{#_Toc400991444}[]{#_Toc322446705}[]{#_Toc257634904}[]{#_Toc139168962}[]{#_Toc322446706}[]{#_Toc361932895}[]{#_Toc361932910}[]{#_Toc361932931}[]{#_Toc361933237}

**安全域 \-- 安全域配置命令 \-- security-zone**

------------------------------------------------------------------------

[**[security-zone]{lang="EN-US"}**]{#struct_0_21314_23244_x2089626913}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[创建并且进入安全域视图。]{style="font-family:宋体"}

[**[undo security-zone]{lang="EN-US"}**]{#struct_0_21314_23244_172896570}[命令用来删除]{style="font-family:宋体"}[安全域]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_1514460391}

[**[security-zone name]{lang="EN-US" style="color:black"}**]{#struct_0_21314_23244_x1526790999}**[ ]{lang="EN-US" style="color:black"}***[zone-name]{lang="EN-US" style="color:black"}*

[**[undo security-zone]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_669077613}[ ]{lang="FR" style="color:black"}**[name]{lang="FR" style="color:black"}[ ]{lang="FR" style="color:black"}***[zone-name]{lang="FR" style="color:black"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_2102993753}

[[缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_21314_23244_x1283612288}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_509884109}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21314_23244_1973473693}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_668881005}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x1313973513}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_625359090}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_1511589575}

[**[name]{lang="EN-US"}**]{#struct_0_21314_23244_668946541}*[zone-name]{lang="EN-US" style="color:black"}*[：安全域的名称，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[31]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包含字符["-"]{lang="EN-US"}。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_x524312562}

[[当首次执行创建安全域或者创建域间策略的命令时，系统会自动创建]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_21314_23244_x822547898}[个缺省安全域：]{style="font-family:宋体"}[Local]{lang="EN-US"}[、]{style="font-family:宋体"}[Trust]{lang="EN-US"}[、]{style="font-family:宋体"}[DMZ]{lang="EN-US"}[和]{style="font-family:宋体"}[Untrust]{lang="EN-US"}[。该描述的适用情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[同一个]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_21314_23244_x34894681}[内不同安全域的名称不允许相同，属于不同]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的安全域的名称可以相同。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[可通过多次执行本命令，创建多个安全域。]{style="font-family:宋体"}]{#struct_0_21314_23244_x246834792}

[[删除一个安全域时，以此安全域为源域或目的域的域间实例也会被删除，而且在该域间实例上已经应用的安全策略会被自动解除应用。缺省安全域不能被删除。]{style="font-family:宋体"}]{#struct_0_21314_23244_712982381}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_x2019854030}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_x1844122209}[创建安全域]{style="font-family:宋体;color:black"}[zonetest]{lang="EN-US" style="color:black"}[，并进入该安全域视图]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_669864045}

[\[Sysname\] security-zone name zonetest]{lang="EN-US"}

[\[Sysname-security-zone-zonetest\]]{lang="EN-US"}

[[【相关配置】]{style="font-family:黑体"}]{#struct_0_21314_23244_x768198148}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display security-zone]{lang="EN-US"}**]{#struct_0_21314_23244_1363835876}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import]{lang="EN-US"}**]{#struct_0_21314_23244_669274220}

[ ]{lang="EN-US"}
:::

::: {#-94386934 .myid}
[]{#struct_0_21314_23244_609829384}[]{#_Toc361382008}[]{#_Toc345167284}[]{#_Toc404782977}[]{#_Toc375667191}[]{#_Toc374116058}

**安全域 \-- 安全域配置命令 \-- zone-pair security**

------------------------------------------------------------------------

[**[zone-pair security]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_x1961435879}[命令用]{style="font-family:
宋体"}[来]{style="font-family:宋体"}[创建安全域间实例并进入安全域间实例视图]{style="font-family:
宋体;color:black"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21314_23244_669339757}**[zone-pair security]{lang="FR" style="color:black"}**[命令用来]{style="font-family:宋体"}[删除指定的域间实例]{style="font-family:宋体;color:black"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_777957158}

[**[zone-pair security source]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_x96557478}**[ ]{lang="FR" style="color:black"}**[{ ]{lang="FR" style="color:black"}*[source-zone-name]{lang="FR" style="color:black"}***[ ]{lang="FR" style="color:black"}**[\| **any** } ]{lang="FR" style="color:black"}**[destination]{lang="FR" style="color:black"}[ ]{lang="FR" style="color:black"}**[{ ]{lang="FR" style="color:black"}*[destination-zone-name ]{lang="FR" style="color:black"}*[\| **any** }]{lang="FR" style="color:black"}

[**[undo zone-pair security source]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_1343419289}**[ ]{lang="FR" style="color:black"}**[{ ]{lang="FR" style="color:black"}*[source-zone-name]{lang="FR" style="color:black"}***[ ]{lang="FR" style="color:black"}**[\| **any** } ]{lang="FR" style="color:black"}**[destination]{lang="FR" style="color:black"}[ ]{lang="FR" style="color:black"}**[{ ]{lang="FR" style="color:black"}*[destination-zone-name]{lang="FR" style="color:black"}***[ ]{lang="FR" style="color:black"}**[\| **any** }]{lang="FR" style="color:black"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_x2008916787}

[[无任何安全域间实例存在]{style="font-family:宋体;color:black"}]{#struct_0_21314_23244_x1875212600}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1158384908}

[[系统]{style="font-family:宋体"}]{#struct_0_21314_23244_1001895764}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_669143149}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_178308511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21314_23244_x440220623}

[**[source]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_1748111530}**[ ]{lang="FR" style="color:black"}***[source-zone-name]{lang="FR" style="color:black"}*[：源安全域的名称，为]{style="font-family:
宋体;color:black"}[1]{lang="FR" style="color:black"}[～]{style="font-family:宋体;color:black"}[31]{lang="FR" style="color:black"}[个字符的字符串，不区分大小写。]{style="font-family:宋体;color:black"}

[**[destination]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_x345130926}**[ ]{lang="FR" style="color:black"}***[destination-zone-name]{lang="FR" style="color:black"}*[：目的安全域的名称，为]{style="font-family:宋体;color:black"}[1]{lang="FR" style="color:black"}[～]{style="font-family:宋体;color:black"}[31]{lang="FR" style="color:black"}[个字符的字符串，不区分大小写。]{style="font-family:宋体;color:black"}

[**[any]{lang="FR" style="color:black"}**]{#struct_0_21314_23244_x455904050}[：表示任意安全域。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_273092809}

[[安全域间实例用于指定安全策略（如]{style="font-family:宋体;color:black"}]{#struct_0_21314_23244_669208685}[ASPF]{lang="EN-US" style="color:black"}[策略、对象策略等）需要检测的业务流的源安全域和目的安全域，它们分别描述了经过网络设备的业务流的首包要进入的安全域和要离开的安全域。在安全域间实例上应用安全策略可实现对指定业务流进行安全策略检查。]{style="font-family:宋体;color:black"}

[[需要注意的是：]{style="font-family:宋体;color:black"}]{#struct_0_21314_23244_x1529666464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_21314_23244_1573503661}[安全]{style="font-family:
宋体;color:black"}[域间实例时指定的源安全域和目的安全域必须是已存在的安全域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_21314_23244_x715609860}[安全]{style="font-family:
宋体;color:black"}[域间实例后，在域间实例上已经应用的安全策略将不生效，对应的引用关系同时被取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_1833042717}

[]{#struct_0_21314_23244_1222901328}[]{#_Toc322446707}[]{#_Toc322446708}[\# ]{lang="EN-US"}[创建源安全域]{style="font-family:宋体;color:black"}[Trust]{lang="EN-US" style="color:black"}[到目的安全域]{style="font-family:宋体;color:black"}[Untrust]{lang="EN-US" style="color:black"}[的安全域间实例。]{style="font-family:宋体;
color:black"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_451651410}

[\[Sysname\] [zone-pair security]{style="color:black"} source trust destination untrust]{lang="EN-US"}

[\[Sysname-[zone-pair-security]{style="color:black"}-Trust-Untrust\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_1430569648}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone-pair security]{lang="EN-US"}**]{#struct_0_21314_23244_669012077}
:::

::::: {#1320008151 .myid}
[]{#_Toc404782978}[]{#struct_0_21314_23244_x1668260916}[]{#_Toc383018332}

**安全域 \-- 安全域配置命令 \-- security-zone intra-zone default permit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](安全域命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_21314_23244_1207964435}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21314_23244_x1839532754}
:::

[ ]{lang="EN-US"}

[**[security-zone intra-zone default permit]{lang="EN-US"}**]{#struct_0_21314_23244_2146114676}[命令用来配置同一安全域内接口间报文处理的缺省动作为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **security-zone intra-zone default permit**]{lang="EN-US"}]{#struct_0_21314_23244_x1701092223}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1984015385}

[**[security-zone intra-zone default permit]{lang="EN-US"}**]{#struct_0_21314_23244_x1699958763}

[**[undo]{lang="EN-US"}**[ **security-zone intra-zone default permit**]{lang="EN-US"}]{#struct_0_21314_23244_x1668326452}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1342347632}

[[同一安全域内报文过滤的缺省动作为]{style="font-family:宋体"}[deny]{lang="EN-US"}]{#struct_0_21314_23244_790462086}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1246099140}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21314_23244_477792445}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21314_23244_x1880624861}

[[network-admin]{lang="EN-US"}]{#struct_0_21314_23244_x628910146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21314_23244_x1813315144}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21314_23244_2032217002}

[[对于同一安全域内接口间的报文，若设备上不存在当前域到当前域的域间实例，设备缺省会将其丢弃，可以通过配置安全域内接口间报文处理的缺省动作为]{style="font-family:宋体"}[permit]{lang="EN-US"}]{#struct_0_21314_23244_x1668785203}[来允许其通过。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21314_23244_953834959}

[[\# ]{lang="EN-US"}]{#struct_0_21314_23244_589194121}[配置同一安全域内接口间报文处理的缺省动作为]{style="font-family:宋体"}[pemit]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21314_23244_x2054827512}

[\[Sysname\] security-zone intra-zone default permit]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
