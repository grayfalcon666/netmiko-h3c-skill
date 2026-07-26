::::: {#853638386 .myid}
[]{#_Toc379547053}[]{#_Toc375835809}[]{#_Toc404798630}[]{#struct_0_10286_17180_x69427510}[]{#_Toc384042036}[]{#_Toc383786740}[]{#_Toc383097749}[]{#_Toc376856930}[]{#_Toc371411810}

**NVGRE \-- NVGRE配置命令 \-- arp suppression enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_10286_17180_1072464723}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_153356017}
:::

[ ]{lang="EN-US"}

[**[arp suppression enable]{lang="EN-US"}**]{#struct_0_10286_17180_x1296100236}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[**[undo arp suppression enable]{lang="EN-US"}**]{#struct_0_10286_17180_x1202785817}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_526498874}

[]{#_Toc178914661}[**[arp suppression enable]{lang="EN-US"}**]{#struct_0_10286_17180_1344707813}

[**[undo arp suppression enable]{lang="EN-US"}**]{#struct_0_10286_17180_1079245935}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_875402007}

[[ARP]{lang="EN-US"}]{#struct_0_10286_17180_x1388931791}[泛洪抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_2093248645}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_86681358}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1882622942}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1880650250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_596412960}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2103700884}

[[为了避免广播发送的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_10286_17180_1729614953}[请求报文占用核心网络带宽，]{style="font-family:宋体"}[NVE]{lang="EN-US"}[从本地站点、]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道接收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求和]{style="font-family:宋体"}[ARP]{lang="EN-US"}[应答报文后，根据该报文在本地建立]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。后续当]{style="font-family:宋体"}[NVE]{lang="EN-US"}[收到本站点内虚拟机请求其它虚拟机]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求时，优先根据]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项进行代答。如果没有对应的表项，则将]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求泛洪到核心网。]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能可以大大减少]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪的次数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1873174830}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x2044459181}[在]{style="font-family:宋体"}[VSI vsi1]{lang="EN-US"}[下开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_1686725076}

[\[Sysname\] vsi vsi1]{lang="EN-US"}

[\[Sysname-vsi-vsi1\] arp suppression enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_177152150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp suppression]{lang="EN-US"}**]{#struct_0_10286_17180_x1487159352}**[ vsi]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset arp suppression]{lang="EN-US"}**]{#struct_0_10286_17180_x1932926530}**[ vsi]{lang="EN-US"}**
:::::

::::: {#1742433432 .myid}
[]{#_Toc404798631}[]{#struct_0_10286_17180_x1589963463}[]{#_Toc375835896}[]{#_Toc290542288}

**NVGRE \-- NVGRE配置命令 \-- bandwidth**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_10286_17180_2098066154}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_x387566233}
:::

[ ]{lang="EN-US"}

[**[bandwidth]{lang="DA"}**]{#struct_0_10286_17180_x266654208}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="DA"}**]{#struct_0_10286_17180_1965945842}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x563701328}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_10286_17180_x827484673}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_10286_17180_2094477041}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_1743236091}

[[接口的期望带宽＝接口的最大速率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_10286_17180_99518574}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2103056889}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x88814573}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1556319085}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1877387928}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x313854206}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x891509363}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_10286_17180_x449442667}[：]{style="font-family:宋体"}[接口的期望带宽]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x746575842}

[[接口的期望带宽会对下列内容有影响：]{style="font-family:宋体"}]{#struct_0_10286_17180_x2087931039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBQ]{lang="EN-US"}]{#struct_0_10286_17180_316200686}[队列带宽。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路开销值。具体介绍请参见"三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_10286_17180_x629416904}[路由配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1044965343}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x459255623}[配置接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的]{style="font-family:宋体"}[期望带宽]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_958769886}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] bandwidth 10000]{lang="EN-US"}
:::::

::: {#1948332219 .myid}
[]{#_Toc404798632}[]{#struct_0_10286_17180_x43585543}[]{#_Toc375835897}[]{#_Toc290542290}

**NVGRE \-- NVGRE配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_10286_17180_1523096593}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1265453730}

[**[default]{lang="EN-US"}**]{#struct_0_10286_17180_x1821200102}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x597293585}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1682884521}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1429293271}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_936667037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1778413867}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_631941403}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_10286_17180_616741259}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_10286_17180_x1960698110}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1026632441}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1896750288}[将接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_697129028}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] default]{lang="EN-US"}

[This command will restore the default settings. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#-1798254511 .myid}
[]{#_Toc404798633}[]{#struct_0_10286_17180_1381832520}

**NVGRE \-- NVGRE配置命令 \-- description (VSI view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_10286_17180_x1792216318}[命令用来设置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_10286_17180_x468628328}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1319795884}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_10286_17180_x599301491}

[**[undo description]{lang="EN-US"}**]{#struct_0_10286_17180_1509404991}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1633880614}

[[未配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1225546990}[的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x395425264}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x40729604}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1900927474}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1423671145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x2061738841}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x226132377}

[*[text]{lang="EN-US"}*]{#struct_0_10286_17180_x576132602}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1767707855}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x718733041}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[vsi for vpn1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_1914467570}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] description vsi for vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1182303943}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10286_17180_400568808}
:::

::: {#-2134435914 .myid}
[]{#_Toc404798634}[]{#struct_0_10286_17180_1109898365}[]{#_Toc375835898}

**NVGRE \-- NVGRE配置命令 \-- description (VSI interface view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_10286_17180_x193345600}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_10286_17180_983721204}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x567862241}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_10286_17180_493161209}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_10286_17180_x1585321459}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_x231963572}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_10286_17180_738547598}["，例如：]{style="font-family:宋体"}[Vsi-interface100 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x133651449}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x660574658}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x631639149}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_417469205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1377503741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1745162151}

[*[text]{lang="EN-US"}*]{#struct_0_10286_17180_136655311}[：接口的描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_997110011}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_10286_17180_x1354280207}

[[本命令仅用于标识某接口，并无特别的功能。使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_10286_17180_1912564608}[等命令可以看到设置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1043540242}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_695510870}[配置接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[gateway for NVGRE 5000]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_966831107}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] description gateway for NVGRE 5000]{lang="EN-US"}
:::

::::: {#-530734358 .myid}
[]{#_Toc404798635}[]{#struct_0_10286_17180_x1986271598}[]{#_Toc384042038}[]{#_Toc383786741}[]{#_Toc383097750}[]{#_Toc376856931}[]{#_Toc371411811}

**NVGRE \-- NVGRE配置命令 \-- display arp suppression vsi**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_10286_17180_x2110168450}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_1340017100}
:::

[ ]{lang="EN-US"}

[**[display arp suppression vsi]{lang="EN-US"}**]{#struct_0_10286_17180_110165199}[命令用来显示]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1124296630}

[]{#_Toc178914662}[[集中式设备：]{style="font-family:宋体"}]{#struct_0_10286_17180_2080900561}

[**[display arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_10286_17180_x712283742}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10286_17180_x1529646043}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_10286_17180_887763064}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_10286_17180_848318034}[模式：]{style="font-family:宋体"}

[**[display arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_10286_17180_33657118}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_713472107}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x1388866255}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x552449885}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_368321229}

[[network-operator]{lang="EN-US"}]{#struct_0_10286_17180_1086227840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_875156873}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10286_17180_x2040995025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_1473425009}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_270701140}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_10286_17180_x1932162045}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_10286_17180_2028005585}[：显示指定成员设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_10286_17180_x1743861370}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_10286_17180_1290124532}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_10286_17180_177217686}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_10286_17180_1482092687}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_10286_17180_427068980}[：显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项的个数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x571144361}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_578278501}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_10286_17180_x1882739174}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x669443215}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_10286_17180_1743301627}

[Total entries: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1880115055}[显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_10286_17180_x906190911}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1372123360}[显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_10286_17180_977381765}

[Total entries: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1461885602}[显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_10286_17180_x629351368}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1708094891}[显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_10286_17180_x211159474}

[Total entries: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1748499886}[显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_10286_17180_x69428225}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1854487625}[显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_10286_17180_x297601966}

[Total entries: 3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display arp suppression vsi]{lang="EN-US"}]{#struct_0_10286_17180_1219539406}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1744358475}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_x333957953}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_936732573}

[[IP Address]{lang="EN-US"}]{#struct_0_10286_17180_1403762945}

[[ARP]{lang="EN-US"}]{#struct_0_10286_17180_x510444969}[泛洪抑制表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_10286_17180_x888625906}

[[ARP]{lang="EN-US"}]{#struct_0_10286_17180_x60715981}[泛洪抑制表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Vsi Name]{lang="EN-US"}]{#struct_0_10286_17180_940837456}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_178459775}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10286_17180_x58927974}

[[MAC]{lang="EN-US"}]{#struct_0_10286_17180_x936700922}[表项的出链路标识符，用来在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内唯一标识一条]{style="font-family:宋体"}[AC]{lang="EN-US"}[或一条]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_10286_17180_x1792150782}

[[ARP]{lang="EN-US"}]{#struct_0_10286_17180_x2118899678}[泛洪抑制表项的老化时间，单位为分钟]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_10286_17180_x1731894923}

[[ARP]{lang="EN-US"}]{#struct_0_10286_17180_1839551458}[泛洪抑制表项的数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x338255910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp suppression enable]{lang="EN-US"}**]{#struct_0_10286_17180_340892393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset arp suppression]{lang="EN-US"}**]{#struct_0_10286_17180_1702143401}**[ vsi]{lang="EN-US"}**

::: {#429599933 .myid}
[]{#_Toc404798636}[]{#struct_0_10286_17180_x122835153}[]{#_Toc375835899}

**NVGRE \-- NVGRE配置命令 \-- display interface vsi-interface**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}**]{#struct_0_10286_17180_x226066841}**[vsi-interface]{lang="DE"}**[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1431246650}

[**[display interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_10286_17180_x561763286}**[vsi-interface]{lang="DE"}**[ \[ *vsi-interface-id* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1111785665}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x265123668}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_531922572}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x540323278}

[[network-operator]{lang="EN-US"}]{#struct_0_10286_17180_x417817494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x272152637}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10286_17180_806021937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_983786740}

[*[vsi-nterface-id]{lang="EN-US"}*]{#struct_0_10286_17180_x2107189798}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_10286_17180_x783662512}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_10286_17180_x333620234}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_10286_17180_788521682}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x832420126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型（]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10286_17180_x720837995}**[vsi-interface]{lang="DE"}**[），将显示设备支持的所有接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型，不指定接口编号（]{lang="EN-US" style="font-family:宋体"}*[vsi-interface-id]{lang="EN-US"}*]{#struct_0_10286_17180_899124553}[）]{lang="EN-US" style="font-family:
宋体"}[，则显示所有]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[虚]{style="font-family:宋体"}[接口的信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则显示指定]{style="font-family:宋体"}]{#struct_0_10286_17180_870305868}[VSI]{lang="EN-US"}[虚接口的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_592962130}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1745096615}[显示接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_10286_17180_1462636529}[display interface vsi-interface 100]{lang="NL-BE"}

[Vsi-interface100]{lang="IT"}

[Current state: UP]{lang="IT"}

[Line protocol state: UP]{lang="IT"}

[Description: Vsi-interface100 Interface]{lang="IT"}

[Bandwidth: 1000000kbps]{lang="IT"}

[Maximum Transmit Unit: 1500]{lang="IT"}

[Internet Address is 10.1.1.1/24 Primary]{lang="IT"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102]{lang="IT"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102]{lang="IT"}

[Physical: Unknown, baudrate: 1000000 kbps]{lang="IT"}

[Last clearing of counters: Never]{lang="IT"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="IT"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="IT"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="IT"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="IT"}

[[表1-2 ]{lang="EN-US"}[display interface vsi-interface]{lang="EN-US"}]{#struct_0_10286_17180_x648474838}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1736946169}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_x922730780}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_1340082636}

[[Vsi-interface100]{lang="NL-BE"}]{#struct_0_10286_17180_505633441}

[[接口]{style="font-family:宋体"}]{#struct_0_10286_17180_x569032251}[VSI-interface100]{lang="NL-BE"}[的相关信息]{style="font-family:宋体"}

[[C]{lang="NL-BE"}[urrent state]{lang="EN-US"}]{#struct_0_10286_17180_1840777618}

[[接口的物理状态和管理状态，取值包括：]{style="font-family:宋体"}]{#struct_0_10286_17180_1768750191}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administr]{lang="EN-US"}]{#struct_0_10286_17180_1696682865}[a]{lang="EN-US"}[t]{lang="EN-US"}[ive]{lang="EN-US"}[ly DOWN]{lang="EN-US"}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_10286_17180_971796270}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_10286_17180_1338260191}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_10286_17180_x1388800719}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：]{style="font-family:宋体"}]{#struct_0_10286_17180_330991144}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_10286_17180_x1048604960}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_10286_17180_x426860770}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_10286_17180_x1114897959}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_10286_17180_x1036194721}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_10286_17180_177283222}

[[Bandwidth]{lang="NL-BE"}]{#struct_0_10286_17180_1076829494}

[[接口的期望带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_10286_17180_x1609622893}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_10286_17180_148197299}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_10286_17180_1774816542}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_10286_17180_2099376036}

[[Tunnel]{lang="NO-BOK"}]{#struct_0_10286_17180_1743367163}[接口的]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址。如果没有为]{style="font-family:宋体"}[Tunnel]{lang="NO-BOK"}[接口配置]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_10286_17180_481164531}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_10286_17180_x327135558}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IP]{lang="EN-US"}]{#struct_0_10286_17180_1991811841}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_10286_17180_126149390}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IPv6]{lang="EN-US"}]{#struct_0_10286_17180_x629285832}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_10286_17180_x1456364829}

[[接口的物理类型，取值为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_10286_17180_589765237}

[[baudrate]{lang="IT"}]{#struct_0_10286_17180_1508400954}

[[接口的波特率，单位为]{style="font-family:宋体"}]{#struct_0_10286_17180_x66509982}[kbps]{lang="IT"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_10286_17180_323940388}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_10286_17180_936798109}[命令清除接口下的统计信息的时间（如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_10286_17180_x1744115887}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_10286_17180_x1238079816}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的包数]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_10286_17180_x50851592}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_10286_17180_x1792085246}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的包数]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_10286_17180_1555605918}

[[总计输入的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_10286_17180_686153160}[总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}

[[Output: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_10286_17180_x2060408291}

[[总计输出的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_10286_17180_x1642756377}[总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x226001305}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vsi-interface brief]{lang="EN-US"}]{#struct_0_10286_17180_987919631}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Vsi100               DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x147845485}[显示接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vsi-interface 100 brief description]{lang="EN-US"}]{#struct_0_10286_17180_x102779895}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Vsi100               UP    UP      1.1.1.1         VSI-interface100]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1057295105}[显示当前状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface brief down]{lang="EN-US"}]{#struct_0_10286_17180_983852276}

[Brief information of interface(s) under route mode:]{lang="NL-BE"}

[Link: ADM - administratively down; Stby - standby]{lang="NL-BE"}

[Interface            Link Cause]{lang="NL-BE"}

[Vsi100]{lang="EN-US"}[               DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[Vsi200]{lang="EN-US"}[               DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[]{#struct_0_10286_17180_431365072}[[表1-3 ]{lang="EN-US"}[display interface vsi-interface brief]{lang="EN-US"}]{#_Ref129008332}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1734611849}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_x495193878}

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_x1093023796}

[[Brief information of interface(s) under route mode:]{lang="EN-US"}]{#struct_0_10286_17180_34502521}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_10286_17180_958933978}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_10286_17180_x1745031079}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_10286_17180_1798170745}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_10286_17180_955275409}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_10286_17180_1939107938}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_10286_17180_x1753172182}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的网络层协议状态显示是]{style="font-family:宋体"}[UP]{lang="EN-US"}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10286_17180_126294428}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_10286_17180_1339623884}

[[Link]{lang="EN-US"}]{#struct_0_10286_17180_x2027189892}

[[接口物理连接状态，取值包括：]{style="font-family:宋体"}]{#struct_0_10286_17180_901105612}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_10286_17180_357043173}[：表示本链路物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_10286_17180_x2121942932}[：表示本链路物理上]{lang="EN-US" style="font-family:宋体"}[是]{style="font-family:宋体"}[不通的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_10286_17180_x2000691878}[：表示本链路被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_10286_17180_x1389259471}[：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_10286_17180_1896562819}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：]{style="font-family:宋体"}]{#struct_0_10286_17180_1907912405}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_10286_17180_x597673587}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (s)]{lang="EN-US"}]{#struct_0_10286_17180_1711458461}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_10286_17180_483109238}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_10286_17180_984738134}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_10286_17180_176824470}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_10286_17180_x1418516871}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_10286_17180_x336961567}

[[Cause]{lang="EN-US"}]{#struct_0_10286_17180_1305964119}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_10286_17180_412415280}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_10286_17180_1742908411}[：表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_10286_17180_x1888688251}[：表示没有]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[关联该]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[或者]{lang="EN-US" style="font-family:宋体"}[关联该接口]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[没有]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PW.]{lang="EN-US"}

[ ]{lang="NL-BE"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1388680882}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_10286_17180_x2015979106}

::: {#356357916 .myid}
[]{#_Toc404798637}[]{#struct_0_10286_17180_x1701013304}

**NVGRE \-- NVGRE配置命令 \-- display l2vpn mac-address**

------------------------------------------------------------------------

[**[display l2vpn mac-address]{lang="EN-US"}**]{#struct_0_10286_17180_x1324760067}[命令用来显示]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1268162841}

[**[display l2vpn mac-address ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **dynamic** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_10286_17180_803899157}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_704428853}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x629744584}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x195612906}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x614253263}

[[network-operator]{lang="EN-US"}]{#struct_0_10286_17180_893350947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_208821913}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10286_17180_x469419407}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_2113925383}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_10286_17180_x1519233756}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_10286_17180_x1995892697}[：显示通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。如果不指定本参数，则显示所有类型的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，包括通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的本地和远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项、静态配置的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[不支持静态配置本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_10286_17180_8935765}[：显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数目。如果不指定本参数，则显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_936339357}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1601949639}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn mac-address]{lang="EN-US"}]{#struct_0_10286_17180_x1773781962}

[MAC Address      State    VSI Name                        Link ID/Name  Aging]{lang="EN-US"}

[0000-0000-000a   dynamic  vpn1                            1             Aging]{lang="EN-US"}

[0000-0000-000b   static   vpn1                            Tunnel10      NotAging]{lang="EN-US"}

[0000-0000-000c   dynamic  vpn1                            Tunnel65535   Aging]{lang="EN-US"}

[0000-0000-000d   dynamic  vpn1                            Tunnel9999999 Aging]{lang="EN-US"}

[\-\-- 4 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x788598543}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项总数。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn mac-address count]{lang="EN-US"}]{#struct_0_10286_17180_x294281226}

[4 mac address(es) found]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display l2vpn mac-address]{lang="EN-US"}]{#struct_0_10286_17180_577417446}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1730197187}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_x1413876147}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_x654621219}

[[MAC Address]{lang="EN-US"}]{#struct_0_10286_17180_x1792543998}

[[MAC]{lang="EN-US"}]{#struct_0_10286_17180_542331273}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10286_17180_x855962568}

[[MAC]{lang="EN-US"}]{#struct_0_10286_17180_x739309134}[地址的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_10286_17180_1607013003}[：表示]{style="font-family:宋体"}[通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的本地或远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="EN-US"}]{#struct_0_10286_17180_x2117292210}[：表示静态配置的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10286_17180_1467745776}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1487051385}[名称]{style="font-family:宋体"}

[[Link ID/Name]{lang="EN-US"}]{#struct_0_10286_17180_x970003451}

[[对于本端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_10286_17180_x226460057}[地址，为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的出链路标识符，即]{style="font-family:宋体"}[AC]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符；对于远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的隧道名称]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_10286_17180_x171966117}

[[MAC]{lang="EN-US"}]{#struct_0_10286_17180_1631633031}[地址表项是否老化，取值包括]{style="font-family:宋体"}[Aging]{lang="EN-US"}[和]{style="font-family:宋体"}[NotAging]{lang="EN-US"}

[[XX mac address(es) found]{lang="EN-US"}]{#struct_0_10286_17180_x731739790}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x187165959}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x963212437}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn mac-address]{lang="EN-US"}**]{#struct_0_10286_17180_1874856405}

::: {#-1122099741 .myid}
[]{#_Toc404798638}[]{#struct_0_10286_17180_983393524}[]{#_Toc379547057}[]{#_Toc375835820}

**NVGRE \-- NVGRE配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

[**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_882568457}[命令用来显示以太网服务实例的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1403091650}

[**[display l2vpn service-instance ]{lang="EN-US"}**[\[ **interface**]{lang="EN-US"}*[ interface-type interface-number]{lang="EN-US"}*[ \[ **service-instance** *instance-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10286_17180_x982214520}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2126113102}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x530927766}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1580565796}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x817447460}

[[network-operator]{lang="EN-US"}]{#struct_0_10286_17180_503990078}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x62520568}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10286_17180_1610719964}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1745489831}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_10286_17180_x1494939652}[：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。]{style="font-family:
宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_10286_17180_463258624}[：显示指定以太网服务实例的信息。]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。如果指定了]{style="font-family:宋体"}**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*[参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。]{style="font-family:
宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10286_17180_x485157112}[：显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_307667513}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1658680679}[显示所有以太网服务实例的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance]{lang="EN-US"}]{#struct_0_10286_17180_679156077}

[Total number of service-instances: 4, 4 up, 0 down]{lang="EN-US"}

[Total number of ACs: 4, 4 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                SrvID Owner                           LinkID State Type]{lang="EN-US"}

[GE1/0/3                  1     vsi10                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  2     vsi11                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  3     vsi12                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  4     vsi13                           1      Up    VSI]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display l2vpn service-instance]{lang="EN-US"}]{#struct_0_10286_17180_721631837}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2029050331}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_1339689420}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_x845527788}

[[Total number of service-instances]{lang="EN-US"}]{#struct_0_10286_17180_x1250047440}

[[以太网服务实例的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_10286_17180_2112618768}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的以太网服务实例数目]{style="font-family:宋体"}

[[Total number of ACs]{lang="EN-US"}]{#struct_0_10286_17180_x1172791872}

[[AC]{lang="EN-US"}]{#struct_0_10286_17180_x201486202}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[AC]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10286_17180_1623775896}

[[二层以太网接口或二层聚合接口名称]{style="font-family:宋体"}]{#struct_0_10286_17180_x1389193935}

[[SrvID ]{lang="EN-US"}]{#struct_0_10286_17180_x794636824}

[[以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_10286_17180_x1461645414}

[[Owner]{lang="EN-US"}]{#struct_0_10286_17180_x799916613}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1339101118}[名称，如果以太网服务实例上尚未关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，则本字段显示为空]{style="font-family:宋体"}

[[LinkID]{lang="EN-US"}]{#struct_0_10286_17180_1536008290}

[[以太网服务实例在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1522842091}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10286_17180_176890006}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10286_17180_x632139094}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_10286_17180_x2054352317}

[[以太网服务实例所属的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10286_17180_x971450767}[类型，取值包括]{style="font-family:宋体"}[VSI]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1744502139}[显示二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[上所有以太网服务实例的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/3 verbose]{lang="EN-US"}]{#struct_0_10286_17180_1742973947}

[Interface: GE1/0/3]{lang="EN-US"}

[  Service Instance: 1]{lang="EN-US"}

[    Encapsulation : s-vid 1 to 16]{lang="EN-US"}

[    VSI Name      : vsi10]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 2]{lang="EN-US"}

[    Encapsulation : s-vid 1001 to 1016]{lang="EN-US"}

[                    only-tagged]{lang="EN-US"}

[    VSI Name      : vsi11]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 3]{lang="EN-US"}

[    Encapsulation : s-vid 2000]{lang="EN-US"}

[                    c-vid 1001 to 1002 1015 to 1016]{lang="EN-US"}

[    VSI Name      : vsi12]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display l2vpn service-instance verbose]{lang="EN-US"}]{#struct_0_10286_17180_877645335}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2023999943}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_1217839809}

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_x629679048}

[[Interface]{lang="EN-US"}]{#struct_0_10286_17180_x270001392}

[[二层以太网接口或二层聚合接口]{style="font-family:宋体"}]{#struct_0_10286_17180_x1003647753}

[[Service Instance]{lang="EN-US"}]{#struct_0_10286_17180_x1846267200}

[[以太网服务实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_10286_17180_2097687921}

[[Encapsulation]{lang="EN-US"}]{#struct_0_10286_17180_x1787641593}

[[以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则不显示本字段]{style="font-family:宋体"}]{#struct_0_10286_17180_x309851315}

[[VSI Name]{lang="EN-US"}]{#struct_0_10286_17180_2062509696}

[[与以太网服务实例关联的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_936404893}[的名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10286_17180_x750793603}

[[以太网服务实例在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1177119526}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10286_17180_1830977292}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10286_17180_987936300}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1016514509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_x1601644818}[]{#_Toc389834784}

::: {#-1007637280 .myid}
[]{#_Toc404798639}[]{#struct_0_10286_17180_1344030014}[]{#_Toc386982100}[]{#_Toc374372819}[]{#_Toc334795167}[]{#_Toc391301810}[]{#_Toc391301849}

**NVGRE \-- NVGRE配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

[**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10286_17180_x1792478462}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1721136935}

[**[display]{lang="EN-US"}**[ **l2vpn** **vsi** \[ **name** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10286_17180_x1428075893}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1965824309}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10286_17180_587015472}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x374081970}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1842311939}

[[network-operator]{lang="EN-US"}]{#struct_0_10286_17180_2022886798}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_216743210}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10286_17180_x1191694075}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x226394521}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_591277709}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10286_17180_x257463972}[：显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1227986109}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1393510787}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi]{lang="EN-US"}]{#struct_0_10286_17180_2048874514}

[Total number of VSIs: 1, 1 up, 0 down, 0 admin down]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name                        VSI Index       MTU    State]{lang="EN-US"}

[vpna                            0               1500   Up]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x475569182}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi verbose]{lang="EN-US"}]{#struct_0_10286_17180_670435788}

[VSI Name: 0]{lang="EN-US"}

[  VSI Index               : 0]{lang="EN-US"}

[  VSI State               : Down]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : Unlimited]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  Flooding                : Enabled]{lang="EN-US"}

[  Statistics              : Enabled]{lang="EN-US"}

[  Input statistics:]{lang="EN-US"}

[    Octets   : 0]{lang="EN-US"}

[    Packets  : 0]{lang="EN-US"}

[    Errors   : 0]{lang="EN-US"}

[    Discards : 0]{lang="EN-US"}

[  Output statistics:]{lang="EN-US"}

[    Octets   : 0]{lang="EN-US"}

[    Packets  : 0]{lang="EN-US"}

[    Errors   : 0]{lang="EN-US"}

[    Discards : 0]{lang="EN-US"}

[  Gateway Interface       : VSI-interface 100]{lang="EN-US"}

[  NVGRE VSID              : 4096]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: 1]{lang="EN-US"}

[  VSI Index               : 1]{lang="EN-US"}

[  VSI State               : Down]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : Unlimited]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  Flooding                : Enabled]{lang="EN-US"}

[  Statistics              : Enabled]{lang="EN-US"}

[  Input Statistics:]{lang="EN-US"}

[    Octets   : 0]{lang="EN-US"}

[    Packets  : 0]{lang="EN-US"}

[    Errors   : 0]{lang="EN-US"}

[    Drops : 0]{lang="EN-US"}

[  Output Statistics:]{lang="EN-US"}

[    Octets   : 0]{lang="EN-US"}

[    Packets  : 0]{lang="EN-US"}

[    Errors   : 0]{lang="EN-US"}

[    Discards : 0]{lang="EN-US"}

[  Gateway Interface       : VSI-interface 101]{lang="EN-US"}

[  NVGRE VSID              : 4097]{lang="EN-US"}

[  Tunnels:]{lang="EN-US"}

[    Tunnel Name          Link ID    State  Type]{lang="EN-US"}

[Tunnel1              0x7000001  Up     Manual]{lang="EN-US"}

[Tunnel2              0x7000002  Up     Manual]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    BAGG1 srv1                       0          Down]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display l2vpn vsi]{lang="EN-US"}]{#struct_0_10286_17180_1700488090}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2019898927}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_x809908154}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_153261724}

[[VSI Name]{lang="EN-US"}]{#struct_0_10286_17180_1029027587}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x183582915}[名称]{style="font-family:宋体"}

[[VSI Index]{lang="EN-US"}]{#struct_0_10286_17180_2097961878}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x606874047}[索引]{style="font-family:宋体"}

[[VSI Description]{lang="EN-US"}]{#struct_0_10286_17180_x2128821171}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x2058447567}[的描述信息，如果不配置，则此行不显示]{style="font-family:宋体"}

[[VSI State]{lang="EN-US"}]{#struct_0_10286_17180_1364824426}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1876174130}[的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_10286_17180_1575094099}[：]{style="font-family:宋体"}[up]{lang="EN-US"}[状态。只有]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[关联了处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的隧道和]{style="font-family:宋体"}[AC]{lang="EN-US"}[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[才会处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_10286_17180_x1255667861}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_10286_17180_260015730}[：通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_10286_17180_587035864}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1099595950}[上配置的最大传输单元]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_10286_17180_957222292}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x492363626}[的带宽限制值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}

[[Broadcast Restrain]{lang="EN-US"}]{#struct_0_10286_17180_x974272523}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_703523601}[的广播抑制百分比]{style="font-family:宋体"}

[[Multicast Restrain]{lang="EN-US"}]{#struct_0_10286_17180_627642908}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1783168403}[的组播抑制百分比]{style="font-family:宋体"}

[[Unknown Unicast Restrain]{lang="EN-US"}]{#struct_0_10286_17180_x1483287942}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x2145476907}[的未知单播抑制百分比]{style="font-family:宋体"}

[[MAC Learning]{lang="EN-US"}]{#struct_0_10286_17180_1073720315}

[[是否使能了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_10286_17180_x1761790809}[地址学习功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10286_17180_x406175808}[：使能了]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10286_17180_x795658266}[：未使能]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[MAC Table Limit]{lang="EN-US"}]{#struct_0_10286_17180_x287866480}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1298932680}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}]{#struct_0_10286_17180_132377724}[，表示不限制]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[Drop Unknown]{lang="EN-US"}]{#struct_0_10286_17180_1054260968}

[[当]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1526277461}[内学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，是否禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10286_17180_1817624456}[：表示禁止转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10286_17180_267151261}[：表示允许转发]{lang="EN-US" style="font-family:宋体"}

[[Hub-Spoke]{lang="EN-US"}]{#struct_0_10286_17180_1046811103}

[[是否使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}]{#struct_0_10286_17180_463976297}[能力。未使能]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力，则不显示此字段]{style="font-family:宋体"}

[[Flooding]{lang="EN-US"}]{#struct_0_10286_17180_x1698240075}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x481582050}[是否使能泛洪功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10286_17180_1833235202}[：表示使能了]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能，即]{style="font-family:宋体"}[NVE]{lang="EN-US"}[会将目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的单播数据帧发送给所有本地和远端站点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10286_17180_883478102}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[禁止]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能]{lang="EN-US" style="font-family:宋体"}[，即]{style="font-family:宋体"}[NVE]{lang="EN-US"}[只将目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的单播数据帧发送给所有本地站点]{style="font-family:宋体"}

[[Statistics]{lang="EN-US"}]{#struct_0_10286_17180_x1201227260}

[[是否使能]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x716456774}[的统计功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10286_17180_x895648153}[：使能了]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[的统计功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10286_17180_x1868856942}[：禁止]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[的统计功能]{lang="EN-US" style="font-family:宋体"}

[[Input statistics]{lang="EN-US"}]{#struct_0_10286_17180_x1210706190}

[[入方向的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x747787164}[报文统计信息，包括入方向接收的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、接收的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、接收的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Output statistics]{lang="EN-US"}]{#struct_0_10286_17180_314205428}

[[出方向的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1285646576}[报文统计信息，包括出方向发送的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、发送的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Gateway Interface]{lang="EN-US"}]{#struct_0_10286_17180_x1529323425}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x868680692}[网关虚接口编号]{style="font-family:宋体"}

[[NVGRE VSID]{lang="EN-US"}]{#struct_0_10286_17180_x625401459}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_1880289369}[虚拟子网编号]{style="font-family:宋体"}

[[Tunnels]{lang="EN-US"}]{#struct_0_10286_17180_x1740028039}

[[与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_1174712869}[网络关联的隧道信息]{style="font-family:宋体"}

[[Tunnel Name]{lang="EN-US"}]{#struct_0_10286_17180_x136176158}

[[隧道名字]{style="font-family:宋体"}]{#struct_0_10286_17180_670501324}

[[Link ID]{lang="EN-US"}]{#struct_0_10286_17180_2079232461}

[[隧道在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1806167692}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10286_17180_1501119551}

[[隧道状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10286_17180_x2058382031}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_10286_17180_50317349}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x1040960907}[和]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道的关联方式，取值为]{style="font-family:宋体"}[Manual]{lang="EN-US"}[，表示手动关联]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[和]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[ACs]{lang="EN-US"}]{#struct_0_10286_17180_x492298090}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1375502174}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_10286_17180_828243149}

[[接入电路]{style="font-family:宋体"}]{#struct_0_10286_17180_x193592021}

[[Link ID]{lang="EN-US"}]{#struct_0_10286_17180_1073785851}

[[AC]{lang="EN-US"}]{#struct_0_10286_17180_x986672516}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10286_17180_742743029}

[[AC]{lang="EN-US"}]{#struct_0_10286_17180_x1298867144}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1771550832 .myid}
[]{#_Toc404798640}[]{#struct_0_10286_17180_633260906}

**NVGRE \-- NVGRE配置命令 \-- display nvgre tunnel**

------------------------------------------------------------------------

[**[display nvgre tunnel]{lang="EN-US"}**]{#struct_0_10286_17180_x1984354649}[命令用来显示与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络关联的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x875056150}

[**[display]{lang="EN-US"}**[ **nvgre tunnel** \[ **vsid** *vsid* \]]{lang="EN-US"}]{#struct_0_10286_17180_x1420968648}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_663171087}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x698354035}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1971455924}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_267216797}

[[network-operator]{lang="EN-US"}]{#struct_0_10286_17180_1329753894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_2133758281}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10286_17180_1277013323}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_1361947044}

[*[vsid]{lang="EN-US"}*]{#struct_0_10286_17180_969769702}[：显示与指定]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络关联的隧道的信息。]{style="font-family:宋体"}*[vsid]{lang="EN-US"}*[为]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[虚拟子网标识符，取值范围为]{style="font-family:宋体"}[4096]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。不指定此参数，则显示所有与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络关联的隧道的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1407456597}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1474528231}[显示所有与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络关联的隧道的信息。]{style="font-family:宋体"}

[[\<Sysname\> display nvgre tunnel]{lang="EN-US"}]{#struct_0_10286_17180_1833300738}

[Total number of NVGREs: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[NVGRE VSID: 4096; VSI name: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[NVGRE VSID: 4097; VSI name: 2; Total tunnels: 2 (1 up, 1 down)]{lang="EN-US"}

[Tunnel name          Link ID    State  Type]{lang="EN-US"}

[Tunnel1              0x7000001  Up     Manual]{lang="EN-US"}

[Tunnel3              0x7000002  Down   Manual]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display nvgre tunnel]{lang="EN-US"}]{#struct_0_10286_17180_67638593}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2040801681}[[字段]{style="font-family:黑体"}]{#struct_0_10286_17180_x1111092491}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10286_17180_x1332899671}

[[Total number of NVGREs]{lang="EN-US"}]{#struct_0_10286_17180_x356737218}

[[已创建的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x905461136}[网络的总数]{style="font-family:宋体"}

[[NVGRE VSID]{lang="EN-US"}]{#struct_0_10286_17180_1446077950}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x540148526}[虚拟子网编号]{style="font-family:宋体"}

[[VSI name]{lang="EN-US"}]{#struct_0_10286_17180_x895582617}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_834354385}[网络所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Total tunnels]{lang="EN-US"}]{#struct_0_10286_17180_x368580486}

[[与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x1125113555}[网络关联的隧道的总数，包括处于]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态的隧道总数]{style="font-family:宋体"}

[[Tunnel name]{lang="EN-US"}]{#struct_0_10286_17180_1770553042}

[[隧道名称]{style="font-family:宋体"}]{#struct_0_10286_17180_1989388538}

[[Link ID]{lang="EN-US"}]{#struct_0_10286_17180_1037095616}

[[隧道在]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_314270964}[网络内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10286_17180_1647531246}

[[隧道的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10286_17180_x1896695863}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_10286_17180_1758349901}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x1850911376}[和]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道的关联方式，取值为]{style="font-family:宋体"}[Manual]{lang="EN-US"}[，表示手动关联]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[和]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x760170868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nvgre]{lang="EN-US"}**]{#struct_0_10286_17180_1880354905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel]{lang="EN-US"}**]{#struct_0_10286_17180_1342196225}

::: {#-900899430 .myid}
[]{#_Toc404798641}[]{#struct_0_10286_17180_x27817965}[]{#_Toc379547060}[]{#_Toc375835822}[]{#_Toc288911611}[]{#_Toc203551099}

**NVGRE \-- NVGRE配置命令 \-- encapsulation**

------------------------------------------------------------------------

[**[encapsulation]{lang="EN-US"}**]{#struct_0_10286_17180_1227745414}[命令用来配置以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_10286_17180_246535599}[命令用来删除以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_835816886}

[**[encapsulation]{lang="EN-US"}**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_10286_17180_x1165433961}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** { *vlan-id* \| *vlan-id-list* } \[ **only-tagged** \]]{lang="EN-US"}]{#struct_0_10286_17180_170958621}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_10286_17180_x1733686149}

[**[encapsulation]{lang="EN-US"}**[ { **default** \| **tagged** \| **untagged** }]{lang="EN-US"}]{#struct_0_10286_17180_670566860}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_10286_17180_1623239190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_544558477}

[[未配置任何报文匹配规则。]{style="font-family:宋体"}]{#struct_0_10286_17180_681271502}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1123763308}

[[以太网服务实例视图]{style="font-family:宋体"}]{#struct_0_10286_17180_1180078416}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_667013785}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1283170772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x283319682}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2058316495}

[**[c-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_10286_17180_x136316062}[：匹配内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Customer VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_10286_17180_x99288830}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_10286_17180_1956413905}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ to *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_10286_17180_x1797273924}[：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Service VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_10286_17180_x460299985}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_10286_17180_1485041757}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[only-tagged]{lang="EN-US"}**]{#struct_0_10286_17180_293858320}[：表示只匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。当匹配的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，如果未指定本关键字，则会同时匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文和未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文；如果指定了本参数，则只匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_10286_17180_235306328}[：匹配指定外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签和内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_10286_17180_915258039}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_10286_17180_x1342553457}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[al]{lang="EN-US"}**]{#struct_0_10286_17180_x492232554}**[l]{lang="EN-US"}**[表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_10286_17180_x595379128}[：表示缺省的报文匹配规则。]{style="font-family:宋体"}

[**[tagged]{lang="EN-US"}**]{#struct_0_10286_17180_x1280635794}[：表示匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[untagged]{lang="EN-US"}**]{#struct_0_10286_17180_x1251623553}[：表示匹配未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x931939143}

[[当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_10286_17180_1135678257}

[[同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（]{style="font-family:宋体"}**[encapsulation default]{lang="EN-US"}**]{#struct_0_10286_17180_x1981564500}[）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10286_17180_180396518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个以太网服务实例视图下，不能重复执行本命令。]{style="font-family:宋体"}]{#struct_0_10286_17180_x587175470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例]{style="font-family:宋体"}]{#struct_0_10286_17180_x1192653974}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的关联。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[内层]{style="font-family:宋体"}]{#struct_0_10286_17180_x875972704}[VLAN]{lang="EN-US"}[标签和外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[QinQ]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1692920858}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1627805576}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置如下报文匹配规则：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[111]{lang="EN-US"}[，内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[20]{lang="EN-US"}[、]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_1073851387}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\] encapsulation s-vid 111 c-vid 20 30 to 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x201801876}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_1295738494}
:::

::: {#-2005881093 .myid}
[]{#_Toc404798642}[]{#struct_0_10286_17180_605074285}[]{#_Toc384042060}[]{#_Toc371411812}

**NVGRE \-- NVGRE配置命令 \-- flooding disable**

------------------------------------------------------------------------

[**[flooding disable]{lang="EN-US"}**]{#struct_0_10286_17180_1784880458}[命令用来关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能。]{style="font-family:宋体"}

[**[undo flooding disable]{lang="EN-US"}**]{#struct_0_10286_17180_x1607174546}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x432308408}

[**[flooding disable]{lang="EN-US"}**]{#struct_0_10286_17180_50562826}

[**[undo flooding disable]{lang="EN-US"}**]{#struct_0_10286_17180_578431900}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_x21285293}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_520415724}[的泛洪功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x947883884}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1298801608}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1530244445}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x967817739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1080274426}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_781096958}

[[缺省情况下，]{style="font-family:宋体"}[NVE]{lang="EN-US"}]{#struct_0_10286_17180_445455549}[从本地站点内接收到目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的单播数据帧后，会在该]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络内除接收接口外的所有本地接口和]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道上泛洪该数据帧，将该数据帧发送给]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络内的所有站点。如果用户希望把该类数据帧限制在本地站点内，不通过]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道将其转发到远端站点，则可以通过本命令手工禁止]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络对应]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_456771873}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_147429972}[关闭名称为]{style="font-family:宋体"}[vsi1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_267282333}

[\[Sysname\] vsi vsi1]{lang="EN-US"}

[\[Sysname-vsi-vsi1\] flooding disable]{lang="EN-US"}
:::

::: {#17596291 .myid}
[]{#_Toc404798643}[]{#struct_0_10286_17180_907189173}

**NVGRE \-- NVGRE配置命令 \-- gateway vsi-interface**

------------------------------------------------------------------------

[**[gateway vsi-interface]{lang="EN-US"}**]{#struct_0_10286_17180_x477634819}[命令用来为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定网关接口。]{style="font-family:宋体"}

[**[undo gateway vsi-interface ]{lang="EN-US"}**]{#struct_0_10286_17180_767612204}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1450640539}

[**[gateway vsi-interface ]{lang="EN-US"}***[vsi-interface-id]{lang="EN-US"}*]{#struct_0_10286_17180_1490429132}

[**[undo gateway vsi-interface]{lang="EN-US"}**]{#struct_0_10286_17180_x2018361673}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_45568314}

[[没有为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1384407026}[指定网关接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_2124640646}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x128702555}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1833366274}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_467151879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1484094279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x111588893}

[*[vsi-interface-id]{lang="EN-US"}*]{#struct_0_10286_17180_142243679}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[网关虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x57259475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_10286_17180_x351611698}[VSI]{lang="EN-US"}[只能指定一个网关接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的]{style="font-family:宋体"}]{#struct_0_10286_17180_1803255351}[VSI]{lang="EN-US"}[可以指定相同的网关接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x961909962}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1818234522}[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定网关接口为]{style="font-family:宋体"}[Vsi-interface100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_10286_17180_1380309045}

[\[Sysname\] vsi vpna]{lang="EN-US"}

[\[Sysname-vsi-vpna\] gateway vsi-interface 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x265730220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface vsi-interface]{lang="EN-US"}**]{#struct_0_10286_17180_x895517081}
:::

::: {#-256627221 .myid}
[]{#_Toc404798644}[]{#struct_0_10286_17180_x726885719}[]{#_Toc381105348}

**NVGRE \-- NVGRE配置命令 \-- interface vsi-interface**

------------------------------------------------------------------------

[**[interface vsi-interface]{lang="EN-US"}**]{#struct_0_10286_17180_x1051614197}[命令用来创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口视图。]{style="font-family:宋体"}

[**[undo interface vsi-interface]{lang="EN-US"}**]{#struct_0_10286_17180_x1104998102}[命令用来删除]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[虚接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x522916096}

[**[interface vsi-interface ]{lang="EN-US"}***[vsi-interface-id]{lang="EN-US"}*]{#struct_0_10286_17180_2070419597}

[**[undo interface vsi-interface ]{lang="EN-US"}***[vsi-interface-id]{lang="EN-US"}*]{#struct_0_10286_17180_x1601695856}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_511496151}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1451261568}[虚接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x841043782}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10286_17180_314336500}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_127720738}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x608469944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1195832616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1339056362}

[*[vsi-nterface-id]{lang="EN-US"}*]{#struct_0_10286_17180_1447742443}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1727243709}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x130562319}[创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口]{style="font-family:宋体"}[100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_10286_17180_x914240597}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_381211122}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gateway vsi-interface]{lang="EN-US"}**]{#struct_0_10286_17180_x819492885}
:::

::: {#2070950537 .myid}
[]{#_Toc404798645}[]{#struct_0_10286_17180_1880420441}[]{#_Toc379547066}[]{#_Toc375835823}

**NVGRE \-- NVGRE配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_10286_17180_1735161578}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_10286_17180_1130078309}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1726236173}

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_10286_17180_x818841881}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_10286_17180_1449221774}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_793163956}

[[L2VPN]{lang="EN-US"}]{#struct_0_10286_17180_370158250}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x356437354}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10286_17180_1432404559}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x292666842}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_670632396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1987809580}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1143847371}

[[只有使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10286_17180_1939159895}[功能后，才能进行]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_2099135794}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1927173725}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_x1546797012}

[\[Sysname\] l2vpn enable]{lang="EN-US"}
:::

::: {#-1775240408 .myid}
[]{#_Toc404798646}[]{#struct_0_10286_17180_x72713905}[]{#_Toc384042067}

**NVGRE \-- NVGRE配置命令 \-- mac-address static**

------------------------------------------------------------------------

[**[mac-address static]{lang="EN-US"}**]{#struct_0_10286_17180_x1097917886}[命令用来添加静态远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[undo mac-address static]{lang="EN-US"}**]{#struct_0_10286_17180_x1677454889}[命令用来删除指定的静态远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2058250959}

[**[mac-address static]{lang="EN-US"}**[ *mac-address* **interface tunnel** *tunnel-number* **vsi** *vsi-name*]{lang="EN-US"}]{#struct_0_10286_17180_2074429677}

[**[undo mac-address static]{lang="EN-US"}**[ \[ *mac-address* \] \[ **interface tunnel** *tunnel-number* \] **vsi** *vsi-name*]{lang="EN-US"}]{#struct_0_10286_17180_2035290006}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_1776289880}

[[设备上不存在任何静态的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_10286_17180_x225305651}[地址表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1899275051}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10286_17180_1290909379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_2040610326}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_844052373}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1354688640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_1098172835}

[*[mac]{lang="EN-US"}*[-]{lang="EN-US"}]{#struct_0_10286_17180_770535255}*[address]{lang="EN-US"}*[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，不支持组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[interface tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_10286_17180_x492167018}[：指定远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道接口。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_1732745790}[：指定远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_1294126521}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_10286_17180_x613989950}[地址是指]{style="font-family:宋体"}[NVE]{lang="EN-US"}[连接的远端站点内虚拟机的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址既可以通过本命令静态配置，也可以通过报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习。静态配置的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项优先级高于源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x587201735}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1951090463}[添加一条静态远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[，]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[为]{style="font-family:宋体"}[vsi1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_1381611196}

[\[Sysname\] mac-address static 000f-e201-0101 interface tunnel 1 vsi vsi1]{lang="EN-US"}
:::

::: {#988247972 .myid}
[]{#_Toc404798647}[]{#struct_0_10286_17180_x1471222830}[]{#_Toc375835902}

**NVGRE \-- NVGRE配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_10286_17180_x2003165159}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_10286_17180_1073916923}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_581889920}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_10286_17180_x76995850}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_10286_17180_976452816}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_480103542}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_10286_17180_729830892}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x509896212}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1626547428}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1178551823}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x111296569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x630998229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1298736072}

[*[size]{lang="EN-US"}*]{#struct_0_10286_17180_x482868408}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[46]{lang="EN-US"}[～]{style="font-family:宋体"}[1560]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_873963670}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1869789877}[配置接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_x1541010588}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] mtu 1430]{lang="EN-US"}
:::

::: {#1896375162 .myid}
[]{#_Toc404798648}[]{#struct_0_10286_17180_1374371329}[]{#_Toc386982098}

**NVGRE \-- NVGRE配置命令 \-- nvgre**

------------------------------------------------------------------------

[**[nvgre]{lang="EN-US"}**]{#struct_0_10286_17180_x680607599}[命令用来创建]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络，并进入]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络视图。]{style="font-family:宋体"}

[**[undo nvgre]{lang="EN-US"}**]{#struct_0_10286_17180_x1543265531}[命令用来删除指定的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1651050743}

[**[nvgre ]{lang="EN-US"}***[vsid]{lang="EN-US"}*]{#struct_0_10286_17180_267347869}

[**[undo nvgre]{lang="EN-US"}**]{#struct_0_10286_17180_573211688}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_1703484105}

[[设备上不存在任何]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x127601199}[网络。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_939554364}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1540626525}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_779847663}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x221304969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x2085736815}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1415291024}

[*[vsid]{lang="EN-US"}*]{#struct_0_10286_17180_1833431810}[：]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[虚拟子网标识符，取值范围为]{style="font-family:宋体"}[4096]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_2062196731}

[[在一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_5833353}[下只能创建一个]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络。不同]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下创建的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络，其]{style="font-family:宋体"}[VSID]{lang="EN-US"}[不能相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1661830792}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x2140171197}[在名称为]{style="font-family:宋体"}[vpna]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下创建编号为]{style="font-family:宋体"}[10000]{lang="EN-US"}[的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络，并进入]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络视图。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_10286_17180_910730439}

[\[Sysname\] vsi vpna]{lang="EN-US"}

[\[Sysname-vsi-vpna\] nvgre 10000]{lang="EN-US"}

[\[Sysname-vsi-vpna-nvgre-10000\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_433591434}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_10286_17180_1450978399}
:::

::::: {#-1851718045 .myid}
[]{#_Toc404798649}[]{#struct_0_10286_17180_x2072196917}[]{#_Toc384042077}[]{#_Toc383786769}[]{#_Toc383097751}[]{#_Toc376856932}[]{#_Toc371411817}

**NVGRE \-- NVGRE配置命令 \-- reset arp suppression vsi**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_10286_17180_x895451545}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_822915470}
:::

[ ]{lang="EN-US"}

[**[reset arp suppression vsi]{lang="EN-US"}**]{#struct_0_10286_17180_453671708}[命令用来清除]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1182245539}

[**[reset arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \]]{lang="EN-US"}]{#struct_0_10286_17180_97238712}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2146657874}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10286_17180_311277717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1579446628}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_420933670}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x57608194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1720414981}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_314402036}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1173175118}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1998548294}[清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> reset arp suppression vsi]{lang="EN-US"}]{#struct_0_10286_17180_719881556}

[This command will delete all entries. Continue? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1374789122}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp suppression]{lang="EN-US"}**]{#struct_0_10286_17180_x669050059}**[ vsi]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp suppression enable]{lang="EN-US"}**]{#struct_0_10286_17180_370942044}
:::::

::: {#877252436 .myid}
[]{#_Toc404798650}[]{#struct_0_10286_17180_229841903}[]{#_Toc375835903}[]{#_Toc290542313}[]{#_Toc263067840}

**NVGRE \-- NVGRE配置命令 \-- reset counters interface vsi-interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="DE"}**]{#struct_0_10286_17180_1485321024}[命令用来清除接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1472195634}

[**[reset counters interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_10286_17180_x910847304}**[vsi-interface]{lang="DE"}**[ \[ *vsi-interface-id* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1427589052}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10286_17180_1880485977}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x204554766}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_587908017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_274211840}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1894065205}

[*[vsi-nterface-id]{lang="EN-US"}*]{#struct_0_10286_17180_1016063532}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_760653653}

[[在某些情况下]{style="font-family:宋体"}]{#struct_0_10286_17180_x195824877}[，]{style="font-family:宋体"}[需要统计一定时间内某接口的流量]{style="font-family:宋体"}[，]{style="font-family:宋体"}[这就需要在统计开始前清除该接口原有的统计信息]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型（]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10286_17180_928053522}**[vsi-interface]{lang="DE"}**[），则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10286_17180_x2048402436}[，]{lang="EN-US" style="font-family:宋体"}[不指定接口编号（]{lang="EN-US" style="font-family:
宋体"}*[vsi-interface-id]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}[，则清除所有]{lang="EN-US" style="font-family:
宋体"}[VSI]{lang="EN-US"}[虚]{style="font-family:宋体"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则清除指定]{style="font-family:宋体"}]{#struct_0_10286_17180_x723929635}[VSI]{lang="EN-US"}[虚接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1245504720}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_670173644}[清除接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface vsi-interface 100]{lang="EN-US"}]{#struct_0_10286_17180_x10948977}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1773865690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface]{lang="EN-US"}**]{#struct_0_10286_17180_285118936}
:::

::::: {#816869194 .myid}
[]{#_Toc404798651}[]{#struct_0_10286_17180_1459767398}

**NVGRE \-- NVGRE配置命令 \-- reset l2vpn mac-address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image002.png){#图片 1 width="61" height="26"}]{lang="EN-US"}]{#struct_0_10286_17180_x1781009300}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_x388050228}
:::

**[ ]{lang="EN-US"}**

[**[reset l2vpn mac-address]{lang="EN-US"}**]{#struct_0_10286_17180_x1617869816}[命令用来清除通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1350070404}

[**[reset ]{lang="EN-US"}[l2vpn mac-address ]{lang="EN-US"}**[\[ **vsi**]{lang="EN-US"}*[ vsi-name ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_10286_17180_x925096687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_781326134}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x2058709711}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1651341238}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_666615215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1803149536}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_418538765}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_x453132260}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x591329078}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_520162409}[通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习到错误的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，或学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项数目达到最大值时，可以执行本命令，以便重新学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1872370161}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1573553559}[清除名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn mac-address vsi vpn1]{lang="EN-US"}]{#struct_0_10286_17180_255414565}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x492625770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn mac-address vsi]{lang="EN-US"}**]{#struct_0_10286_17180_548766777}
:::::

::::: {#1068872014 .myid}
[]{#_Toc404798652}[]{#struct_0_10286_17180_x577125114}[]{#_Toc387305729}[]{#_Toc381105349}

**NVGRE \-- NVGRE配置命令 \-- reset l2vpn statistics vsi**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_10286_17180_x1733730357}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_969909212}
:::

[ ]{lang="EN-US"}

[**[reset l2vpn statistics vsi]{lang="EN-US"}**]{#struct_0_10286_17180_1550224640}[命令用来清除]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_525292266}

[**[reset l2vpn statistics vsi ]{lang="EN-US"}**[\[ **name** *vsi-name* \]]{lang="EN-US"}]{#struct_0_10286_17180_x1225053750}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_2011020284}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10286_17180_1920792732}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1831804088}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_1073458171}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1742172248}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x649645365}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_x897076288}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1875971695}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_139968334}[清除本设备上所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn statistics vsi]{lang="EN-US"}]{#struct_0_10286_17180_x722797930}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1188334812}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics enable]{lang="EN-US"}**]{#struct_0_10286_17180_x1536734718}
:::::

::: {#-26059450 .myid}
[]{#_Toc404798653}[]{#struct_0_10286_17180_1678997636}[]{#_Toc371411814}

**NVGRE \-- NVGRE配置命令 \-- selective-flooding mac-address**

------------------------------------------------------------------------

[**[selective-flooding mac-addres]{lang="EN-US"}**]{#struct_0_10286_17180_x1299194824}[命令用来配置]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo selective-flooding mac-addres]{lang="EN-US"}**]{#struct_0_10286_17180_1006328661}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的选择性泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1756743907}

[]{#_Toc178914659}[**[selective-flooding mac-addres]{lang="EN-US"}**[ *mac-addres*]{lang="EN-US"}]{#struct_0_10286_17180_1563608798}

[**[undo selective-flooding mac-addres]{lang="EN-US"}**[ *mac-addres*]{lang="EN-US"}]{#struct_0_10286_17180_1147055802}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2109741563}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_628708065}[选择性泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2009048598}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x164292087}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_72813008}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_266889117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_335067766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_1066003610}

[*[mac-address]{lang="EN-US"}*]{#struct_0_10286_17180_154644892}[：选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[F]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_369027115}

[[通过]{style="font-family:宋体"}**[flooding disable]{lang="EN-US"}**]{#struct_0_10286_17180_x1788683446}[命令关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能后，为了将某些]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数据帧泛洪到远端站点以保证某些业务的流量在站点间互通，可以配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。当数据帧的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址匹配选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时，该数据帧可以泛洪到远端站点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_913287874}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1457858425}[在]{style="font-family:宋体"}[VSI vsi1]{lang="EN-US"}[下配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_762902657}

[\[Sysname\] VSI vsi1]{lang="EN-US"}

[\[Sysname-vsi-vsi1\] selective-flooding mac-address 000f-e201-0101]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_959459622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flooding disable]{lang="EN-US"}**]{#struct_0_10286_17180_1832973058}
:::

::: {#-1902885513 .myid}
[]{#_Toc290542294}[]{#_Toc263067821}[]{#_Toc207010297}[]{#_Toc207010030}[]{#_Toc139515319}[]{#_Toc137103152}[]{#_Toc404798654}[]{#struct_0_10286_17180_x331708268}

**NVGRE \-- NVGRE配置命令 \-- service-instance**

------------------------------------------------------------------------

[**[service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_1645709196}[命令用来创建以太网服务实例，并进入以太网服务实例视图。]{style="font-family:宋体"}

[**[undo service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_527588590}[命令用来删除指定的以太网服务实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1091600492}

[**[service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_10286_17180_x963028878}

[**[undo service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_10286_17180_x1935705211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_735550032}

[[接口上不存在任何以太网服务实例。]{style="font-family:宋体"}]{#struct_0_10286_17180_x798553366}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x895910297}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10286_17180_1221404307}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x173121296}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_1941474650}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1546416353}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1575712852}

[*[instance-id]{lang="EN-US"}*]{#struct_0_10286_17180_x391745875}[：以太网服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1820034072}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1638949241}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上创建以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_313943284}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_848033367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_2137070786}
:::

::: {#1602442547 .myid}
[]{#_Toc404798655}[]{#struct_0_10286_17180_x1642985326}[]{#_Toc379547070}[]{#_Toc375835843}

**NVGRE \-- NVGRE配置命令 \-- shutdown (VSI view)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_x468618386}[命令用来关闭当前的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_1321958582}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1153750937}

[**[shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_1447634099}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_x2139590353}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_401111754}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1167090776}[处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1880027225}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1714476357}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x537203245}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x380348793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1794465862}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_x450178012}

[[关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_266770143}[后，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[将不能提供二层交换服务。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1727773641}[功能通常用于暂时禁用二层交换服务，但还需要再次启用该服务的场景。关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[所有已存在的配置保持不变。在关闭状态下还可以对]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[再次被开启后，基于最新的配置提供二层交换服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1446014645}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1591947781}[关闭名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_670239180}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_295860828}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10286_17180_1857994146}
:::

::: {#-1527177385 .myid}
[]{#_Toc404798656}[]{#struct_0_10286_17180_1930908034}[]{#_Toc375835904}

**NVGRE \-- NVGRE配置命令 \-- shutdown (VSI interface view)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_1118353611}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_10286_17180_1191356280}[命令用来开启当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_1122124286}

[**[shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_1586127181}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_10286_17180_x38349541}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2058644175}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1629455708}[虚接口均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x846189772}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1813304775}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2134714918}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1373213998}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_1290380308}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_814569680}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x745692805}[关闭接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_x492560234}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] shutdown]{lang="EN-US"}
:::

::::: {#-655052582 .myid}
[]{#_Toc404798657}[]{#struct_0_10286_17180_x613014011}[]{#_Toc387305730}[]{#_Toc381105350}[]{#_Toc376783185}

**NVGRE \-- NVGRE配置命令 \-- statistics enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NVGRE命令.files/image001.png){#图片 2 width="63" height="25"}]{lang="EN-US"}]{#struct_0_10286_17180_x589257691}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_10286_17180_x1379425775}
:::

[ ]{lang="EN-US"}

[**[statistics enable]{lang="EN-US"}**]{#struct_0_10286_17180_x1775069018}[命令用来开启指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[报文统计功能。]{style="font-family:宋体"}

[**[undo statistics enable]{lang="EN-US"}**]{#struct_0_10286_17180_x356657498}[命令用来关闭指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[报文统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x511196523}

[**[statistics enable]{lang="EN-US"}**]{#struct_0_10286_17180_x914769071}

[**[undo statistics enable]{lang="EN-US"}**]{#struct_0_10286_17180_x797179140}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1178923990}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x362345378}[的报文统计功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1073523707}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_1731897599}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2067483062}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_452815347}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x1086227381}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1142954561}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1818791867}[开启名为]{style="font-family:宋体"}[vpls1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的报文统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_x112232413}

[\[Sysname\] vsi vpls1]{lang="EN-US"}

[\[Sysname-vsi-vpls1\] statistics enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1113200444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn statistics vsi]{lang="EN-US"}**]{#struct_0_10286_17180_1775948901}
:::::

::: {#816204697 .myid}
[]{#_Toc404798658}[]{#struct_0_10286_17180_x1299129288}[]{#_Toc386982097}[]{#_Toc374372823}[]{#_Toc371058550}

**NVGRE \-- NVGRE配置命令 \-- tunnel**

------------------------------------------------------------------------

[**[tunnel]{lang="EN-US"}**]{#struct_0_10286_17180_709236938}[命令用来配置]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络与指定的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道关联。]{style="font-family:宋体"}

[**[undo tunnel]{lang="EN-US"}**]{#struct_0_10286_17180_x1094703781}[命令用来取消]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_145762813}

[**[tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_10286_17180_x494155356}

[**[undo tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_10286_17180_827360112}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_44882357}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_655207963}[网络没有与任何]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_1514026949}

[[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x1520177570}[网络视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1835814252}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_x2073357025}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_266954653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_755368718}

[*[tunnel-numb]{lang="FR"}*[er]{lang="EN-US"}]{#struct_0_10286_17180_763943455}[：隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_1102784577}

[[在]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}]{#struct_0_10286_17180_x899942916}[组网中，用户需要手工将]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道关联。]{style="font-family:宋体"}[NVE]{lang="EN-US"}[接收到某个]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络的泛洪流量后，将在与该]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络关联的所有]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道上发送该流量，以便将流量转发给所有的远端]{style="font-family:宋体"}[NVE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[执行本命令时，需要注意的是：]{style="font-family:宋体"}]{#struct_0_10286_17180_x280412843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令指定的隧道必须是]{style="font-family:宋体"}]{#struct_0_10286_17180_x828220488}[NVGRE]{lang="EN-US"}[模式的隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_10286_17180_300613806}[NVGRE]{lang="EN-US"}[网络可以关联多条]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道；一条]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道可以关联多个]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_608813095}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_x1317054065}[配置]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道]{style="font-family:宋体"}[Tunne0]{lang="EN-US"}[和]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[与]{style="font-family:宋体"}[NVGRE 10000]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_10286_17180_1833038594}

[\[Sysname\] vsi vpna]{lang="EN-US"}

[\[Sysname-vsi-vpna\] nvgre 10000]{lang="EN-US"}

[\[Sysname-vsi-vpna-nvgre-10000\] tunnel 0]{lang="EN-US"}

[\[Sysname-vsi-vpna-nvgre-10000\] tunnel 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_807975402}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display nvgre tunnel]{lang="EN-US"}**]{#struct_0_10286_17180_117973239}
:::

::: {#-981054953 .myid}
[]{#_Toc404798659}[]{#struct_0_10286_17180_1092689365}[]{#_Toc379547097}[]{#_Toc375835849}

**NVGRE \-- NVGRE配置命令 \-- vsi**

------------------------------------------------------------------------

[**[vsi]{lang="EN-US"}**]{#struct_0_10286_17180_x1095680270}[命令用来创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Switching Instance]{lang="EN-US"}[，虚拟交换实例），并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vsi**]{lang="EN-US"}]{#struct_0_10286_17180_1885527626}[命令用来删除指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_268620958}

[**[vsi]{lang="IT"}**]{#struct_0_10286_17180_x733201799}[ *vsi-name*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_10286_17180_500329806}[ ]{lang="IT"}**[vsi]{lang="IT"}**[ *vsi-name*]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_844281850}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_801440575}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x686326760}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10286_17180_x895844761}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_1960114451}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_456140318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_446209301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1831691109}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_x309012593}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_1309738815}

[[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x1132935070}[是]{style="font-family:宋体"}[NVE]{lang="EN-US"}[上为一个]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络提供二层交换服务的虚拟交换实例。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[可以看做是]{style="font-family:宋体"}[NVE]{lang="EN-US"}[上的一台基于]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络进行二层转发的虚拟交换机，它具有传统以太网交换机的所有功能，包括源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址老化、泛洪等。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[与]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络一一对应。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1397312165}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_39816646}[创建名为]{style="font-family:宋体"}[nvgre5000]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_314008820}

[\[Sysname\] vsi nvgre5000]{lang="EN-US"}

[\[Sysname-vsi-nvgre5000\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1366433748}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10286_17180_89502885}
:::

::: {#-216238939 .myid}
[]{#_Toc404798660}[]{#struct_0_10286_17180_1730984695}[]{#_Toc379547105}[]{#_Toc375835850}

**NVGRE \-- NVGRE配置命令 \-- xconnect vsi**

------------------------------------------------------------------------

[**[xconnect vsi]{lang="EN-US"}**]{#struct_0_10286_17180_677659022}[命令用来将]{style="font-family:宋体"}[AC]{lang="NL-BE"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **xconnect vsi**]{lang="EN-US"}]{#struct_0_10286_17180_471209658}[命令用来取消]{style="font-family:宋体"}[AC]{lang="EN-US"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1157899937}

[**[xconnect vsi ]{lang="EN-US"}***[vsi-name ]{lang="EN-US"}*[\[ **access-mode** { **ethernet** \| **vlan** } \]]{lang="EN-US"}]{#struct_0_10286_17180_1019884427}

[**[undo xconnect vsi]{lang="EN-US"}**]{#struct_0_10286_17180_192665227}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10286_17180_1880092761}

[[AC]{lang="EN-US"}]{#struct_0_10286_17180_x1738174910}[没有]{style="font-family:宋体"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10286_17180_x1953919198}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10286_17180_x488323458}[以太网服务实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10286_17180_x372649997}

[[network-admin]{lang="EN-US"}]{#struct_0_10286_17180_1854531925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10286_17180_x692342831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10286_17180_468729002}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_10286_17180_x1145347410}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[access-mode]{lang="EN-US"}**]{#struct_0_10286_17180_x774715649}[：指定]{style="font-family:宋体"}[接入]{style="font-family:宋体"}[模式。当关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[为三层以太网子接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、以太网服务实例时，接入模式缺省为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[；其他情况下，接入模式缺省为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ethernet]{lang="EN-US"}**]{#struct_0_10286_17180_536545740}[：指定]{style="font-family:宋体"}[接入模式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_10286_17180_x2030013559}[：指定]{style="font-family:宋体"}[接入模式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10286_17180_1935992280}

[[在接口视图下执行本命令后，从接口接收到的报文将通过查找关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10286_17180_x649069262}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表进行转发；在某个接口的以太网服务实例视图下执行本命令后，从该接口接收到的、符合以太网服务实例报文匹配规则的报文，将通过查找关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表进行转发。]{style="font-family:宋体"}

[[接入模式分为以下两种：]{style="font-family:宋体"}]{#struct_0_10286_17180_x167564838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_10286_17180_x459738224}[接入模式：从本地站点接收到的、发送给本地站点的以太网帧必须带有]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。]{style="font-family:宋体"}[NVE]{lang="EN-US"}[从本地站点接收到以太网帧后，删除该帧的所有]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[，再转发该数据帧；]{style="font-family:宋体"}[NVE]{lang="EN-US"}[发送以太网帧到本地站点时，为其添加]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。采用该模式时，]{style="font-family:宋体"}[NVE]{lang="EN-US"}[不会传递]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[信息，不同站点可以独立地规划自己的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，不同站点的不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[之间可以互通。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_10286_17180_x1469212794}[接入模式：]{lang="EN-US" style="font-family:宋体"}[从本地站点接收到的、发送给本地站点的以太网帧可以携带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[，也可以不携带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。]{style="font-family:宋体"}[NVE]{lang="EN-US"}[从本地站点接收到以太网帧后，保持该帧的]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[信息不变，转发该数据帧；]{style="font-family:宋体"}[NVE]{lang="EN-US"}[发送以太网帧到本地站点时，不会为其添加]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。采用该模式时，]{style="font-family:宋体"}[NVE]{lang="EN-US"}[会在不同站点间传递]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[信息，不同站点的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[需要统一规划，否则无法互通。]{style="font-family:宋体"}

[[需要注意的是，在以太网服务实例下配置该命令前，必须先配置]{style="font-family:宋体"}**[encapsulation]{lang="EN-US"}**]{#struct_0_10286_17180_2110140961}[命令]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10286_17180_1349449789}

[[\# ]{lang="EN-US"}]{#struct_0_10286_17180_1095130317}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下采用以太网服务实例]{style="font-family:宋体"}[200]{lang="EN-US"}[来匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文，将该以太网服务实例与名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10286_17180_2102629681}

[\[Sysname\] vsi vpn1 hub-spoke]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] encapsulation s-vid 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] xconnect vsi vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10286_17180_x2075250410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn interface]{lang="EN-US"}**]{#struct_0_10286_17180_1111122362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10286_17180_x1781916718}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_10286_17180_x63615819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_10286_17180_x741112098}
:::
