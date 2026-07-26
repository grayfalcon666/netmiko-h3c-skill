::: {#1882814787 .myid}
[]{#_Toc404792843}[]{#struct_0_x2060_63618_135631139}[]{#_Toc257729101}[]{#_Toc131563064}

**端口安全 \-- 端口安全配置命令 \-- display port-security**

------------------------------------------------------------------------

[**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_631484562}[命令用来显示端口安全的配置信息、运行情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x197281982}

[**[display port-security]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \] ]{lang="EN-US"}]{#struct_0_x2060_63618_1134670048}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_791811285}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1481833913}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x127911925}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1831766442}

[[network-operator]{lang="EN-US"}]{#struct_0_x2060_63618_909132660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_574775310}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2060_63618_x947274019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x196823230}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2060_63618_401262809}[：显示指定端口的端口安全相关信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1375049145}

[[如果不指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_x2060_63618_x241755240}[参数，则显示所有端口的端口安全信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_306099100}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1318174398}[显示所有端口的端口安全相关状态。]{style="font-family:宋体"}

[[\<Sysname\> display port-security]{lang="EN-US"}]{#struct_0_x2060_63618_x196888766}

[Port security parameters:]{lang="EN-US"}

[   Port security           : Enabled]{lang="EN-US"}

[   AutoLearn aging time   : 30 min]{lang="EN-US"}

[   Disableport timeout    : 30 s]{lang="EN-US"}

[   MAC move                 : Denied]{lang="EN-US"}

[   Authorization fail     : Offline]{lang="EN-US"}

[   NAS-ID profile          : globalnasidprofile]{lang="EN-US"}

[   OUI value list          :]{lang="EN-US"}

[       Index :  1       Value : 123401]{lang="EN-US"}

[ ]{lang="EN-US"}

[ GigabitEthernet1/0/1 is link-up]{lang="EN-US"}

[   Port mode                      : userLoginWithOUI]{lang="EN-US"}

[   NeedToKnow mode               : Disabled]{lang="EN-US"}

[   Intrusion protection mode   : NoAction]{lang="EN-US"}

[   Security MAC address attribute ]{lang="EN-US"}

[        Learning mode             ]{lang="EN-US"}[：]{style="font-family:宋体"}[ Dynamic]{lang="EN-US"}

[        Aging type                 : ]{lang="EN-US"}[Periodical]{lang="EN-US"}

[   Max secure MAC addresses      : 64]{lang="EN-US"}

[   Current secure MAC addresses   : 1]{lang="EN-US"}

[   Authorization                   ]{lang="EN-US"}[：]{style="font-family:宋体"}[ Permitted]{lang="EN-US"}

[NAS-ID profile                : portnasidprofile]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display port-security]{lang="EN-US"}]{#struct_0_x2060_63618_x1571388977}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_632169390}[[字段]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1970428098}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2060_63618_488498367}

[[Port security]{lang="EN-US"}]{#struct_0_x2060_63618_x196954302}

[[端口安全的开启状态]{style="font-family:宋体"}]{#struct_0_x2060_63618_348059894}

[[AutoLearn aging time]{lang="EN-US"}]{#struct_0_x2060_63618_x2136880519}

[[Sticky MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1342355214}[地址的老化时间，单位为分钟]{style="font-family:宋体"}

[[Disableport timeout]{lang="EN-US"}]{#struct_0_x2060_63618_x406657495}

[[收到非法报文的端口暂时被关闭的时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x2060_63618_340217724}

[[MAC move]{lang="EN-US"}]{#struct_0_x2060_63618_x197019838}

[[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x1167324209}[迁移功能的开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_541473845}[迁移功能处于开启状态，则显示]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermitted]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x2060_63618_2124192157}[MAC]{lang="EN-US"}[迁移功能处于]{style="font-family:宋体"}[关闭状态，则显示]{style="font-family:宋体"}[Denied]{lang="EN-US"}

[[Authorization fail]{lang="EN-US"}]{#struct_0_x2060_63618_x629920196}

[[授权失败后用户的状态，包括下线（]{style="font-family:宋体"}[Offline]{lang="EN-US"}]{#struct_0_x2060_63618_x1405287997}[）和保持在线（]{style="font-family:宋体"}[Online]{lang="EN-US"}[）两种类型]{style="font-family:宋体"}

[[NAS-ID profile]{lang="EN-US"}]{#struct_0_x2060_63618_x1643693686}

[[全局引用的]{style="font-family:宋体"}[ NAS-ID Profile]{lang="EN-US"}]{#struct_0_x2060_63618_736481287}

[[OUI value list]{lang="EN-US"}]{#struct_0_x2060_63618_x1318842321}

[[允许通过认证的用户的]{style="font-family:宋体"}[24]{lang="EN-US"}]{#struct_0_x2060_63618_2084047640}[位]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_x2060_63618_x196561086}

[[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_1173467507}[的索引]{style="font-family:宋体"}

[[Value]{lang="EN-US"}]{#struct_0_x2060_63618_x1892860511}

[[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_x1639991313}[值]{style="font-family:宋体"}

[[Port mode]{lang="EN-US"}]{#struct_0_x2060_63618_x64783478}

[[端口安全模式，包括以下几种：]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1463926931}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[noRestriction]{lang="EN-US"}]{#struct_0_x2060_63618_x475949849}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[autoLearn]{lang="FR"}]{#struct_0_x2060_63618_x196626622}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[macAddressWithRadius]{lang="EN-US"}]{#struct_0_x2060_63618_1925582747}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[macAddressElseUserLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_766123119}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[macAddressElseUserLoginSecureExt]{lang="EN-US"}]{#struct_0_x2060_63618_x643060057}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[secure]{lang="EN-US"}]{#struct_0_x2060_63618_x197085373}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[userLogin]{lang="EN-US"}]{#struct_0_x2060_63618_1548649231}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[userLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_x1787405051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[userLoginSecureExt]{lang="EN-US"}]{#struct_0_x2060_63618_x356300786}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[macAddressOrUserLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_x164236752}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[macAddressOrUserLoginSecureExt]{lang="EN-US"}]{#struct_0_x2060_63618_x197150909}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[userLoginWithOUI]{lang="EN-US"}]{#struct_0_x2060_63618_x428530270}

[[以上各模式的支持情况以及生效情况与设备的型号有关，请以设备的实际情况为准。关于各模式的具体涵义，请参考端口安全配置手册]{style="font-family:宋体"}]{#struct_0_x2060_63618_x100531908}

[[NeedToKnow mode]{lang="EN-US"}]{#struct_0_x2060_63618_x1514576418}

[[Need To Know]{lang="EN-US"}]{#struct_0_x2060_63618_x197216445}[模式，包括以下四种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NeedToKnowOnly]{lang="EN-US"}]{#struct_0_x2060_63618_787287733}[：表示仅允许目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为已通过认证的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的单播报文通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NeedToKnowWithBroadcast]{lang="EN-US"}]{#struct_0_x2060_63618_x147364979}[：允许目的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为已通过认证的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的单播报文或广播地址的报文通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NeedToKnowWithMulticast]{lang="EN-US"}]{#struct_0_x2060_63618_1422737032}[：允许目的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为已通过认证的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的单播报文，广播地址或组播地址的报文通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x2060_63618_x197281981}[：表示不进行]{style="font-family:宋体"}[NTK]{lang="EN-US"}[处理]{style="font-family:宋体"}

[[该模式的生效情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x2060_63618_1134866656}

[[Intrusion protection mode]{lang="EN-US"}]{#struct_0_x2060_63618_17574624}

[[入侵检测特性模式，包括以下四种：]{style="font-family:宋体"}]{#struct_0_x2060_63618_x568447974}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BlockMacAddress]{lang="EN-US"}]{#struct_0_x2060_63618_x196823229}[：表示将非法报文的源]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址加入阻塞]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DisablePort]{lang="EN-US"}]{#struct_0_x2060_63618_400804058}[：表示将收到非法报文的端口永久关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DisablePortTemporarily]{lang="EN-US"}]{#struct_0_x2060_63618_x1876816145}[：表示将收到非法报文的端口暂时关闭一段时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NoAction]{lang="EN-US"}]{#struct_0_x2060_63618_x196888765}[：表示不进行入侵检测处理]{lang="EN-US" style="font-family:宋体"}

[[Security MAC address attribute]{lang="EN-US"}]{#struct_0_x2060_63618_x630378947}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x630313411}[地址的相关属性]{style="font-family:宋体"}

[[Security MAC address learning mode]{lang="EN-US"}]{#struct_0_x2060_63618_2010207979}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x630247875}[地址的学习方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_x2060_63618_x1069251558}[：动态类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sticky]{lang="EN-US"}]{#struct_0_x2060_63618_x630182339}[：]{lang="EN-US" style="font-family:宋体"}[Sticky]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[Security MAC address aging type]{lang="EN-US"}]{#struct_0_x2060_63618_x1152070842}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x1693175024}[地址的老化方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Periodical]{lang="EN-US"}]{#struct_0_x2060_63618_x630116803}[：按照配置的老化时间间隔进行老化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactivity]{lang="EN-US"}]{#struct_0_x2060_63618_1648687321}[：无流量命中时老化]{lang="EN-US" style="font-family:宋体"}

[[Max secure MAC addresses]{lang="EN-US"}]{#struct_0_x2060_63618_x1571192369}

[[端口安全允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1306991969}[地址数目或上线用户数]{style="font-family:宋体"}

[[Current secure MAC addresses]{lang="EN-US"}]{#struct_0_x2060_63618_x873556128}

[[端口下保存的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x196954301}[地址数目]{style="font-family:宋体"}

[[Authorization]{lang="EN-US"}]{#struct_0_x2060_63618_347863286}

[[服务器的授权信息是否被忽略]{style="font-family:宋体"}]{#struct_0_x2060_63618_x580643325}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}[ermitted]{lang="EN-US"}]{#struct_0_x2060_63618_x197019837}[：表示当前端口应用]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[或本地设备]{style="font-family:宋体"}[下发的授权信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ignored]{lang="EN-US"}]{#struct_0_x2060_63618_x1166472241}[：表示当前端口不应用]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[或本地设备]{style="font-family:宋体"}[下发的授权信息]{lang="EN-US" style="font-family:宋体"}

[[NAS-ID profile]{lang="EN-US"}]{#struct_0_x2060_63618_681905142}

[[端口下引用的]{style="font-family:宋体"}[ NAS-ID Profile]{lang="EN-US"}]{#struct_0_x2060_63618_x57511161}

[ ]{lang="EN-US"}

::: {#-1282111703 .myid}
[]{#_Toc404792844}[]{#struct_0_x2060_63618_x259670177}[]{#_Toc257729102}[]{#_Toc161544324}

**端口安全 \-- 端口安全配置命令 \-- display port-security mac-address block**

------------------------------------------------------------------------

[**[display port-security mac-address block]{lang="EN-US"}**]{#struct_0_x2060_63618_x108006708}[命令用来显示阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1294870092}

[**[display port-security mac-address block]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \] \[ **vlan** *vlan-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x2060_63618_x191569192}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x196561085}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_1173401971}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1548304411}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_931346869}

[[network-operator]{lang="EN-US"}]{#struct_0_x2060_63618_x2097428712}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1125426569}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2060_63618_1844070948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_725173210}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2060_63618_1631986064}[：显示指定端口的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。]{style="font-family:
宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x2060_63618_x196626621}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x2060_63618_1925517211}[：显示阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1567113565}

[[如果不指定任何参数，则显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_763731745}[地址的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1272946021}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x778702976}[显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block]{lang="EN-US"}]{#struct_0_x2060_63618_1410657240}

[ MAC ADDR             Port                         VLAN ID]{lang="EN-US"}

[ 0002-0002-0002      GE1/0/1                     1]{lang="EN-US"}

[ 000d-88f8-0577      GE1/0/1                     1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  2 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x1468761734}[显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block]{lang="EN-US"}]{#struct_0_x2060_63618_1368998571}

[ MAC ADDR             Port                         VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 0, no MAC address found \-\--]{lang="EN-US"}

[ MAC ADDR              Port                        VLAN ID]{lang="EN-US"}

[ 000f-3d80-0d2d       GE1/0/1                    30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_852602320}[显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block]{lang="EN-US"}]{#struct_0_x2060_63618_x539448519}

[ MAC ADDR             Port                         VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 0 in chassis 1, no MAC address found \-\--]{lang="EN-US"}

[ MAC ADDR              Port                        VLAN ID]{lang="EN-US"}

[ 000f-3d80-0d2d       GE1/0/1                    30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  1 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1368933035}[显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址计数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block count]{lang="EN-US"}]{#struct_0_x2060_63618_x757813131}

[ ]{lang="EN-US"}

[\-\-- 2 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x798583490}[显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址计数。（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block count]{lang="EN-US"}]{#struct_0_x2060_63618_x562902981}

[ ]{lang="EN-US"}

[\-\-- On slot 0, no MAC address found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- On slot 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_352258790}[显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址计数。（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block count]{lang="EN-US"}]{#struct_0_x2060_63618_1368867499}

[ ]{lang="EN-US"}

[ \-\-- On slot 0 in chassis 1, no MAC address found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  1 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_817988360}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block vlan 1]{lang="EN-US"}]{#struct_0_x2060_63618_x81673165}

[ MAC ADDR             Port                         VLAN ID]{lang="EN-US"}

[ 0002-0002-0002      GE1/0/1                     1]{lang="EN-US"}

[ 000d-88f8-0577      GE1/0/1                     1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  2 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_476405282}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block vlan 30]{lang="EN-US"}]{#struct_0_x2060_63618_x1875367936}

[ MAC ADDR               Port                        VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 0, no MAC address found \-\--]{lang="EN-US"}

[ MAC ADDR               Port                        VLAN ID]{lang="EN-US"}

[ 000f-3d80-0d2d        GE1/0/1                    30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1368801963}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block vlan 30]{lang="EN-US"}]{#struct_0_x2060_63618_1958594405}

[ MAC ADDR               Port                        VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 0 in chassis 1, no MAC address found \-\--]{lang="EN-US"}

[ MAC ADDR               Port                       VLAN ID]{lang="EN-US"}

[ 000f-3d80-0d2d        GE1/0/1                   30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x1189785086}[显示指定端口下的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block interface GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x2060_63618_x1228854327}

[ MAC ADDR             Port                        VLAN ID]{lang="EN-US"}

[ 000d-88f8-0577      GE1/0/1                    1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  1 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_201607170}[显示指定端口下的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block interface GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x2060_63618_1369260715}

[ MAC ADDR             Port                        VLAN ID]{lang="EN-US"}

[ 000f-3d80-0d2d      GE1/0/1                    30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_2019120141}[显示指定端口下的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block interface GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x2060_63618_600897599}

[ MAC ADDR             Port                        VLAN ID]{lang="EN-US"}

[ 000f-3d80-0d2d      GE1/0/1                    30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1174556170}[显示指定端口下的在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block interface ethernet 1/1 vlan 1]{lang="EN-US"}]{#struct_0_x2060_63618_1754394625}

[ MAC ADDR             Port                        VLAN ID]{lang="EN-US"}

[ 000d-88f8-0577      GE1/0/1                    1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  1 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1369195179}[显示指定端口下的在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block interface ethernet 1/1 vlan 30]{lang="EN-US"}]{#struct_0_x2060_63618_x1160799561}

[ MAC ADDR             Port                        VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[ 000f-3d80-0d2d      GE1/0/1                    30]{lang="EN-US"}

[ \-\-- On slot 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_96202264}[显示指定端口下的在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address block interface ethernet 1/1 vlan 30]{lang="EN-US"}]{#struct_0_x2060_63618_1124416471}

[ MAC ADDR             Port                        VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[ 000f-3d80-0d2d      GE1/0/1                    30]{lang="EN-US"}

[ \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-- 1 mac address(es) found \-\--]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display port-security mac-address block]{lang="EN-US"}]{#struct_0_x2060_63618_x906540509}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_622177682}[[字段]{style="font-family:黑体"}]{#struct_0_x2060_63618_x655101629}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369129643}

[[MAC ADDR]{lang="EN-US"}]{#struct_0_x2060_63618_x1868553356}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1518266712}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x2060_63618_x262738275}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x1239188338}[地址所在端口]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x2060_63618_x1179236179}

[[端口所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2060_63618_1369064107}

[*[number]{lang="EN-US"}*[ mac address(es) found]{lang="EN-US"}]{#struct_0_x2060_63618_431957560}

[[当前阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1804815894}[地址数目为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[个]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x278173200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security intrusion-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x784566633}

::: {#-1901710462 .myid}
[]{#_Toc404792845}[]{#struct_0_x2060_63618_x862835199}[]{#_Toc257729103}

**端口安全 \-- 端口安全配置命令 \-- display port-security mac-address security**

------------------------------------------------------------------------

[**[display port-security mac-address security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1823381290}[命令用来显示安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x771629820}

[**[display port-security mac-address security]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \] \[ **vlan** *vlan-id* \] \[ **count** \] ]{lang="EN-US"}]{#struct_0_x2060_63618_1369522859}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1166066596}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_1276700582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x619367266}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1345079024}

[[network-operator]{lang="EN-US"}]{#struct_0_x2060_63618_x1354670773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1456159560}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2060_63618_1667776430}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1793585399}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2060_63618_1369457323}[：显示指定端口的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。]{style="font-family:
宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x2060_63618_408585095}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x2060_63618_x549297916}[：统计符合条件的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1010447963}

[[当端口工作于]{style="font-family:宋体"}[autoLearn]{lang="EN-US"}]{#struct_0_x2060_63618_x2016660947}[模式时，端口上通过自动学习或者静态配置的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址可通过该命令查看。]{style="font-family:宋体"}

[[如果不指定任何参数，则显示所有安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1874230933}[地址的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1753822534}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x2133181739}[显示所有安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address security]{lang="EN-US"}]{#struct_0_x2060_63618_1368998572}

[ MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME]{lang="EN-US"}

[ 0002-0002-0002  1         Security       GE1/0/1                         NOAGED]{lang="EN-US"}

[ 000d-88f8-0577  1         Security       GE1/0/1                         28]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  2 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_852536784}[显示所有安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址计数。]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address security count]{lang="EN-US"}]{#struct_0_x2060_63618_43112754}

[ ]{lang="EN-US"}

[ \-\--  2 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x38514024}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address security vlan 1]{lang="EN-US"}]{#struct_0_x2060_63618_x931314589}

[ MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME]{lang="EN-US"}

[ 0002-0002-0002  1         Security       GE1/0/1                         NOAGED]{lang="EN-US"}

[ 000d-88f8-0577  1         Security       GE1/0/1                         28]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  2 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_414388174}[显示指定端口下的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address security interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x2060_63618_1368933036}

[ MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME]{lang="EN-US"}

[ 000d-88f8-0577  1         Security       GE/0/1                          NOAGED]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\--  1 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x757616523}[显示指定端口下的在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> display port-security mac-address security interface gigabitethernet 1/0/1 vlan 1]{lang="EN-US"}]{#struct_0_x2060_63618_x1160104154}

[ MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME]{lang="EN-US"}

[ 000d-88f8-0577  1         Security       GE1/0/1                         NOAGED]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\--  1 mac address(es) found  \-\--]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display port-security mac-address security]{lang="EN-US"}]{#struct_0_x2060_63618_302073976}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_624519820}[[字段]{style="font-family:黑体"}]{#struct_0_x2060_63618_x851294986}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2060_63618_x401793165}

[[MAC ADDR]{lang="EN-US"}]{#struct_0_x2060_63618_1368867500}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x1137868031}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x2060_63618_x745329694}

[[端口所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2060_63618_x495441290}

[[STATE]{lang="EN-US"}]{#struct_0_x2060_63618_2008920465}

[[添加的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_87168538}[地址类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Security]{lang="EN-US"}]{#struct_0_x2060_63618_1368801964}[：表示该项是安全]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[PORT INDEX]{lang="EN-US"}]{#struct_0_x2060_63618_1958659941}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x923249400}[地址所在端口]{style="font-family:宋体"}

[[AGING TIME]{lang="EN-US"}]{#struct_0_x2060_63618_57940521}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_307060534}[地址的剩余存活时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于静态]{style="font-family:宋体"}]{#struct_0_x2060_63618_1461422748}[MAC]{lang="EN-US"}[地址，显示为]{style="font-family:宋体"}[NOAGED]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x2060_63618_1369260716}[Sticky MAC]{lang="EN-US"}[地址，显示为具体的剩余存活时间，单位为分钟。缺省情况下为不进行老化，显示为]{style="font-family:宋体"}[NOAGED]{lang="EN-US"}

[*[number]{lang="EN-US"}*[ mac address(es) found]{lang="EN-US"}]{#struct_0_x2060_63618_2018923533}

[[当前保存的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x162031225}[地址数目为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[个]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1774949629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security mac-address security]{lang="EN-US"}**]{#struct_0_x2060_63618_1393236590}

::: {#-1962576612 .myid}
[]{#_Toc404792846}[]{#struct_0_x2060_63618_x704822756}[]{#_Toc257729105}

**端口安全 \-- 端口安全配置命令 \-- port-security authorization ignore**

------------------------------------------------------------------------

[**[port-security authorization ignore]{lang="EN-US"}**]{#struct_0_x2060_63618_906102956}[命令用来配置端口不应用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或设备本地下发的授权信息。]{style="font-family:宋体"}

[**[undo port-security authorization ignore]{lang="EN-US"}**]{#struct_0_x2060_63618_1369195180}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1160209748}

[**[port-security authorization ignore]{lang="EN-US"}**]{#struct_0_x2060_63618_171950010}

[**[undo port-security authorization ignore]{lang="EN-US"}**]{#struct_0_x2060_63618_x35847039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1096879472}

[[端口应用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x2060_63618_1358546624}[服务器或设备本地下发的授权信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_910715082}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1947450927}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369129644}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1868749964}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1574702759}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1010098233}

[[当用户通过]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x2060_63618_x357001303}[认证或本地认证后，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或设备会根据用户帐号配置的相关属性进行授权，比如动态下发]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[等。若不希望接受这类动态下发的属性，则可通过配置本命令来忽略。]{style="font-family:宋体"}

[[需要注意的是，该命令在三层以太网接口视图下的支持情况与产品型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2060_63618_273972490}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1118751218}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1995784589}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[不应用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或设备本地下发的授权信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_1391471280}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security authorization ignore]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369064108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_431236664}
:::

::: {#-1542001396 .myid}
[]{#_Toc404792847}[]{#struct_0_x2060_63618_936229277}[]{#_Toc373237207}

**端口安全 \-- 端口安全配置命令 \-- port-security authorization-fail offline**

------------------------------------------------------------------------

[**[port-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2060_63618_1619352269}[命令用来开启授权失败用户下线功能。]{style="font-family:宋体"}

[**[undo port-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2060_63618_1741429779}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_935639454}

[**[port-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2060_63618_1399812300}

[**[undo port-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2060_63618_2020175471}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1204106970}

[[授权失败用户下线功能处于关闭状态，即授权失败后用户保持在线。]{style="font-family:宋体"}]{#struct_0_x2060_63618_x310465200}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_935704990}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1747750186}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1236096643}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1101605865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x740726103}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_935770526}

[[如果配置为授权失败用户下线，当下发的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x2060_63618_283704247}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[不存在或者]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发失败时，将强制用户下线；]{style="font-family:宋体"}

[[如果配置为授权失败用户保持在线，当下发的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x2060_63618_x1343360553}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[不存在或者]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发失败时，用户保持在线，授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Porfile]{lang="EN-US"}[不生效，设备打印]{style="font-family:宋体"}[LOG]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1313485047}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1037656686}[开启授权失败用户下线功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_935836062}

[\[Sysname\] port-security authorization-fail offline]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_96944958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_1499768741}
:::

::: {#-743452660 .myid}
[]{#_Toc404792848}[]{#struct_0_x2060_63618_1455413557}[]{#_Toc257729106}[]{#_Toc131563063}

**端口安全 \-- 端口安全配置命令 \-- port-security enable**

------------------------------------------------------------------------

[**[port-security enable]{lang="EN-US"}**]{#struct_0_x2060_63618_55690935}[命令用来使能端口安全。]{style="font-family:宋体"}

[**[undo port-security enable]{lang="EN-US"}**]{#struct_0_x2060_63618_1163305308}[命令用来关闭端口安全。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1782553334}

[**[port-security enable]{lang="EN-US"}**]{#struct_0_x2060_63618_1617494580}

[**[undo port-security enable]{lang="EN-US"}**]{#struct_0_x2060_63618_1122686740}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_x2060_63618_6441572}

[[端口安全的使能情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2060_63618_1369522860}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1166656423}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_2059331109}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1599906642}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1488273599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1971651344}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_586203174}

[[如果已全局开启了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_x237979809}[或]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，则无法使能端口安全。]{style="font-family:宋体"}

[[执行使能或关闭端口安全的命令后，端口上的相关配置将会恢复为如下情况：]{style="font-family:宋体"}]{#struct_0_x2060_63618_1070666549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_1369457324}[端口接入控制方式恢复为]{style="font-family:宋体"}**[macbased]{lang="EN-US"}**[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_409043847}[端口的授权状态恢复为]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[端口上有用户在线的情况下，若关闭端口安全，则在线用户将会下线。]{style="font-family:宋体"}]{#struct_0_x2060_63618_1024528044}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_59955217}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_318297046}[使能端口安全。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_1292463567}

[\[Sysname\] port-security enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1115290198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_1368998569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x]{lang="EN-US"}**]{#struct_0_x2060_63618_852078031}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/802.1X]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x port-control]{lang="EN-US"}**]{#struct_0_x2060_63618_612846950}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/802.1X]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x port-method]{lang="EN-US"}**]{#struct_0_x2060_63618_720514890}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/802.1X]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-authentication]{lang="EN-US"}**]{#struct_0_x2060_63618_1402777373}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/MAC]{lang="EN-US"}[地址认证）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#430310708 .myid}
[]{#_Toc404792849}[]{#struct_0_x2060_63618_1756791137}[]{#_Toc257729107}

**端口安全 \-- 端口安全配置命令 \-- port-security intrusion-mode**

------------------------------------------------------------------------

[**[port-security intrusion-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x20008943}[命令用来配置入侵检测特性，对接收到非法报文的端口采取相应的安全策略。]{style="font-family:
宋体"}

[**[undo port-security intrusion-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_1611794930}[命令用来缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x445327572}

[**[port-security intrusion-mode ]{lang="EN-US"}**[{ **blockmac** \| **disableport** \| **disableport-temporarily** }]{lang="EN-US"}]{#struct_0_x2060_63618_1368933033}

[**[undo port-security intrusion-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x757419915}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x2044910906}

[[对接收到非法报文的端口不进行入侵检测处理。]{style="font-family:宋体"}]{#struct_0_x2060_63618_x619376205}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x223364207}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_1663512203}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x2060_63618_9518174}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1009699005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_410598683}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_177338069}

[**[blockmac]{lang="EN-US"}**]{#struct_0_x2060_63618_1368867497}[：表示将非法报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址加入阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表中，源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文将被丢弃，实现在端口上过滤非法流量的作用。此]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在被阻塞]{style="font-family:宋体"}[3]{lang="EN-US"}[分钟（系统默认，不可配）后恢复正常。阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表可以通过]{style="font-family:宋体"}**[display port-security mac-address block]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[**[disableport]{lang="EN-US"}**]{#struct_0_x2060_63618_818643720}[：表示将收到非法报文的端口永久关闭。]{style="font-family:宋体"}

[**[disableport-temporarily]{lang="EN-US"}**]{#struct_0_x2060_63618_x1714557336}[：表示将收到非法报文的端口暂时关闭一段时间。关闭时长可通过]{style="font-family:宋体"}**[port-security timer disableport]{lang="EN-US"}**[命令配置。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1241798240}

[[可以通过执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2060_63618_250406993}[命令重新开启被入侵检测特性临时或永久断开的端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x895864616}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x591596}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的入侵检测特性检测到非法报文后，将非法报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址置为阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_x689753953}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security intrusion-mode blockmac]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1368801961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_1958463333}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security mac-address block]{lang="EN-US"}**]{#struct_0_x2060_63618_x58538307}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security timer disableport]{lang="EN-US"}**]{#struct_0_x2060_63618_83742726}
:::

::: {#599970268 .myid}
[]{#_Toc404792850}[]{#struct_0_x2060_63618_936163742}[]{#_Toc373237210}

**端口安全 \-- 端口安全配置命令 \-- port-security mac-address aging-type inactivity**

------------------------------------------------------------------------

[**[port-security mac-address aging-type inactivity]{lang="EN-US"}**]{#struct_0_x2060_63618_187081069}[命令用来配置安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的老化方式为无流量老化。]{style="font-family:宋体"}

[**[undo port-security mac-address aging-type inactivity]{lang="EN-US"}**]{#struct_0_x2060_63618_x734710778}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1206066506}

[**[port-security mac-address aging-type inactivity]{lang="EN-US"}**]{#struct_0_x2060_63618_x1184910238}

[**[undo port-security mac-address aging-type inactivity]{lang="EN-US"}**]{#struct_0_x2060_63618_936229278}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1619352276}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1742019602}[地址按照配置的老化时间进行老化，即在安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的老化时间到达后立即老化，不论该安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是否还有流量产生。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1215978824}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_935639451}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1399812305}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_2019847791}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1351848896}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1540480814}

[[无流量老化方式下，设备会定期检测（检测周期不可配）端口上的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_935704987}[地址是否有流量产生，若某安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在配置的老化时间内没有任何流量产生，则才会被老化，否则该安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不会被老化，并在下一个老化周期内重复该检测过程。下一个周期内若还有流量产生则继续保持该安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的学习状态，该方式可有效避免非法用户通过仿冒合法用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址乘机在合法用户的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址老化时间到达之后占用端口资源。]{style="font-family:宋体"}

[[此命令仅对于]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}]{#struct_0_x2060_63618_590901979}[地址以及动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x2004210592}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1235674139}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的老化方式为无流量老化。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_935770523}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security mac-address aging-type inactivity]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_283704244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1343360556}
:::

::: {#-1162733567 .myid}
[]{#_Toc404792851}[]{#struct_0_x2060_63618_553970160}[]{#_Toc373237211}[]{#_Toc361662989}[]{#_Toc296589716}

**端口安全 \-- 端口安全配置命令 \-- port-security mac-address dynamic**

------------------------------------------------------------------------

[**[port-security mac-address dynamic]{lang="EN-US"}**]{#struct_0_x2060_63618_x948006878}[命令用来将]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址设置为动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo port-security mac-address dynamic]{lang="EN-US"}**]{#struct_0_x2060_63618_935836059}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1477033147}

[**[port-security mac-address dynamic]{lang="EN-US"}**]{#struct_0_x2060_63618_1594660490}

[**[undo port-security mac-address dynamic]{lang="EN-US"}**]{#struct_0_x2060_63618_x164276109}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_935901595}

[[端口学习到的是]{style="font-family:宋体"}[Sticky]{lang="EN-US"}]{#struct_0_x2060_63618_452656021}[类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，它能够被保存在配置文件中，设备重启后也不会丢失。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x127525120}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1381260442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_935967131}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1635569115}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_964379827}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x530905491}

[[动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_936032667}[地址不会被保存在配置文件中，可通过执行]{style="font-family:宋体"}**[display port-security mac-address security]{lang="EN-US"}**[命令查看到，设备重启之后会丢失。在不希望设备上保存重启之前端口上已有的]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址的情况下，可将其设置为动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[本命令成功执行后，指定端口上的]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}]{#struct_0_x2060_63618_588983704}[地址会立即被转换为动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，且将不能手工添加]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址。之后，若成功执行对应的]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令，该端口上的动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址会立即转换为]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址，且用户可以手工添加]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x7617837}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_141008987}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址设置为动态类型的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_936098203}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security mac-address dynamic]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x602579982}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1095365955}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security mac-address security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1650497684}
:::

::: {#-1620667945 .myid}
[]{#_Toc404792852}[]{#struct_0_x2060_63618_1579159371}[]{#_Toc257729108}

**端口安全 \-- 端口安全配置命令 \-- port-security mac-address security**

------------------------------------------------------------------------

[**[port-security mac-address security]{lang="EN-US"}**]{#struct_0_x2060_63618_857480057}[命令用来添加安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo port-security mac-address security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1242935396}[命令用来删除指定的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x2012621685}

[[在二层以太网接口视图下：]{style="font-family:宋体"}]{#struct_0_x2060_63618_x202380346}

[**[port-security mac-address security ]{lang="EN-US"}**[\[ **sticky** \] *mac-address* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x2060_63618_1369260713}

[**[undo port-security mac-address security ]{lang="EN-US"}**[\[ **sticky** \] *mac-address* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x2060_63618_2018726925}

[[在系统视图下：]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1403330115}

[**[port-security]{lang="EN-US"}**[ **mac-address** **security** \[ **sticky** \] *mac-address* **interface** *interface-type interface-number* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x2060_63618_1913856363}

[**[undo port-security mac-address security ]{lang="EN-US"}**[\[ \[ *mac-address* \[ **interface** *interface-type interface-number* \] \] **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x2060_63618_533327193}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1127444549}

[[未配置安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x2013423875}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x475206635}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2060_63618_1285733756}[系统视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369195177}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1160668489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_868225380}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1892752545}

[**[sticky]{lang="EN-US"}**]{#struct_0_x2060_63618_190213914}[：表示要添加一个可老化的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址（]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址）。]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址的老化时间可通过]{style="font-family:宋体"}**[port-security timer autolearn aging]{lang="EN-US"}**[命令]{style="font-family:宋体"}[配置。当]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址的老化时间到达时，]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址即被删除。若不指定本参数，则表示添加的是一个不老化的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x2060_63618_1142111554}[：安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2060_63618_x1050298281}[：指定添加安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的接口。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x2060_63618_x1425601468}[：指定安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x2081810676}

[[手工配置添加的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1369129641}[地址在保存配置并设备重启后，不会被删除。因此，可以将网络中一些已知的、固定要接入某端口的主机或设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址添加为安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，这样在端口处于]{style="font-family:宋体"}[autoLearn]{lang="EN-US"}[安全模式时，此类源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的主机或设备的报文将被允许通过指定端口，而且还可避免与其它通过自动方式学习到端口上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文争夺资源而被拒绝接收。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1868422284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成功添加安全]{style="font-family:宋体"}]{#struct_0_x2060_63618_x861097990}[MAC]{lang="EN-US"}[地址的前提为：端口安全处于开启状态；端口的端口安全模式为]{style="font-family:宋体"}[autoLearn]{lang="EN-US"}[；当前的接口允许指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[通过或已加入该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，且该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[已添加的安全]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x2035003244}[地址，除非首先将其删除，否则不能重复添加或者修改其地址类型，例如已经在某端口上添加了一条安全]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}**[port-security mac-address security]{lang="EN-US"}**[ 1-1-1 **vlan** 10]{lang="EN-US"}[，则不能再添加一条安全]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}**[port-security mac-address security sticky]{lang="EN-US"}**[ 1-1-1 **vlan** 10]{lang="EN-US"}[。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1888367610}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1671048627}[使能端口安全，配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的安全模式为]{style="font-family:宋体"}[autoLearn]{lang="EN-US"}[，并指定端口安全允许的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_x462254032}

[\[Sysname\] port-security enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security max-mac-count 100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security port-mode autolearn]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_922219275}[为该端口添加一条]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[0001-0002-0003]{lang="EN-US"}[，该安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址属于]{style="font-family:宋体"}[VLAN 4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/1\] port-security mac-address security sticky ]{lang="EN-US"}]{#struct_0_x2060_63618_1369064105}[0001-0002-0003]{lang="EN-US"}[ vlan 4]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_432088632}[在系统视图下为端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[添加一条安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[0001-0001-0002]{lang="EN-US"}[，该安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址属于]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] port-security mac-address security ]{lang="EN-US"}]{#struct_0_x2060_63618_x407227331}[0001-0001-0002]{lang="EN-US"}[ interface gigabitethernet 1/0/1 vlan 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1922715278}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_513856949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security timer autolearn aging]{lang="EN-US"}**]{#struct_0_x2060_63618_x1476971342}
:::

::: {#-1661734453 .myid}
[]{#_Toc404792853}[]{#struct_0_x2060_63618_x2023810840}[]{#_Toc334531737}[]{#_Toc331088875}

**端口安全 \-- 端口安全配置命令 \-- port-security mac-move permit**

------------------------------------------------------------------------

[**[port-security mac-move permit]{lang="EN-US"}**]{#struct_0_x2060_63618_x1670460171}[命令用来开启允许]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[迁移功能。]{style="font-family:宋体"}

[**[undo port-security mac-move permit]{lang="EN-US"}**]{#struct_0_x2060_63618_1369522857}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1166984100}

[**[port-security mac-move permit]{lang="EN-US"}**]{#struct_0_x2060_63618_1480874978}

[**[undo port-security mac-move permit]{lang="EN-US"}**]{#struct_0_x2060_63618_565004507}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x988361468}

[[允许]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1361295658}[迁移功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x605840616}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_1501950438}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1019600189}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1369457321}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_408716167}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_866899622}

[[该功能对系统中的所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_x1626396129}[认证用户和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户生效。]{style="font-family:宋体"}

[[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_579195724}[迁移功能处于关闭状态时，如果用户从某一端口上线成功，则该用户在未从当前端口下线的情况下无法在设备的其它端口上（无论该端口是否与当前端口属于同一]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）发起认证，也无法上线。]{style="font-family:宋体"}

[[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x2033927368}[迁移功能处于开启状态时，如果用户从某一端口上线成功，则允许该在线用户在设备的其它端口上（无论该端口是否与当前端口属于同一]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）发起认证。如果该用户在后接入的端口上认证成功，则当前端口会将该用户立即进行下线处理，保证该用户仅在一个端口上处于上线状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_520762135}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_908232778}[开启允许]{style="font-family:宋体"}[MAC]{lang="EN-US"}[迁移功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_x472845450}

[\[Sysname\] port-security mac-move permit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1368998570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_852667856}
:::

::: {#1948322621 .myid}
[]{#_Toc404792854}[]{#struct_0_x2060_63618_x1347423720}[]{#_Toc257729109}[]{#_Toc131563069}

**端口安全 \-- 端口安全配置命令 \-- port-security max-mac-count**

------------------------------------------------------------------------

[**[port-security max-mac-count]{lang="EN-US"}**]{#struct_0_x2060_63618_x690305540}[命令用来设置端口安全允许的最大安全]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址数。]{style="font-family:
宋体"}

[**[undo port-security max-mac-count]{lang="EN-US"}**]{#struct_0_x2060_63618_x239762512}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_573885421}

[**[port-security max-mac-count ]{lang="EN-US"}***[count-value]{lang="EN-US"}*]{#struct_0_x2060_63618_x1482280893}

[**[undo port-security max-mac-count]{lang="EN-US"}**]{#struct_0_x2060_63618_x1249039896}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x383199843}

[[端口安全不限制本端口可保存的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1368933034}[地址数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x757747595}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_404210293}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1198963395}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x875102544}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1315629870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_2114204953}

[*[count-value]{lang="EN-US"}*]{#struct_0_x2060_63618_x75838773}[：端口允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_240763399}

[[对于]{style="font-family:宋体"}[autoLearn]{lang="EN-US"}]{#struct_0_x2060_63618_1368867498}[安全模式，端口允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数由本命令配置，包括端口上学习到的以及手工配置的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数；对于采用]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证或者两者组合形式的认证类安全模式，端口允许的最大用户数取本命令配置的值与相应模式下允许认证用户数的最小值。例如，]{style="font-family:宋体"}[userLoginSecureExt]{lang="EN-US"}[模式下，端口下所允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数为配置的端口安全允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数与]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证所允许的最大用户数的最小值。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2060_63618_817922824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当端口工作于]{style="font-family:宋体"}]{#struct_0_x2060_63618_1914481142}[autoLearn]{lang="EN-US"}[模式时，无法更改端口安全允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无线端口上有用户在线时，无法更改端口安全允许的最大安全]{style="font-family:宋体"}]{#struct_0_x2060_63618_1206685698}[MAC]{lang="EN-US"}[地址数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口安全允许的最大安全]{style="font-family:宋体"}]{#struct_0_x2060_63618_2004904630}[MAC]{lang="EN-US"}[地址数不能小于当前端口下已保存的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令在三层以太网接口视图下的支持情况与产品型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1596921719}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_116360362}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x574508711}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置端口安全允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_1368801962}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security max-mac-count 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1958528869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_x523515584}
:::

::: {#-499997729 .myid}
[]{#_Toc404792855}[]{#struct_0_x2060_63618_728828237}[]{#_Toc396314065}[]{#_Toc372540907}[]{#_Toc373314567}

**端口安全 \-- 端口安全配置命令 \-- port-security nas-id-profile**

------------------------------------------------------------------------

[**[port-security nas-id-profile]{lang="EN-US"}**]{#struct_0_x2060_63618_x1643890294}[命令用来指定全局]{style="font-family:
宋体"}[/]{lang="EN-US"}[端口引用的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo port-security nas-id-profile]{lang="EN-US"}**]{#struct_0_x2060_63618_x572070195}[命令用来删除全局]{style="font-family:宋体"}[/]{lang="EN-US"}[端口引用的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_2029519251}

[**[port-security nas-id-profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x2060_63618_528171256}

[**[undo port-security nas-id-profile]{lang="EN-US"}**]{#struct_0_x2060_63618_x1617068579}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x332471020}

[[未指定引用的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}]{#struct_0_x2060_63618_1955491322}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1428336628}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2060_63618_x2027468081}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1084993061}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x203816526}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x49489122}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_433304080}

[*[profile-name]{lang="SV"}*]{#struct_0_x2060_63618_x348389352}[：标识指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[绑定关系的]{style="font-family:宋体"}[Profile]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_668084837}

[[本命令引用的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}]{#struct_0_x2060_63618_x1108822499}[由命令]{style="font-family:宋体"}**[aaa nas-id profile]{lang="EN-US"}**[配置，具体情况请参考"安全命令参考"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[NAS-ID Profile]{lang="EN-US"}]{#struct_0_x2060_63618_x976375509}[可以在系统视图下或者接口视图下进行配置引用，接口上的配置优先，若接口上没有配置，则使用系统视图下的全局配置。]{style="font-family:宋体"}

[[需要注意的是，如果指定了]{style="font-family:宋体"}]{#struct_0_x2060_63618_x595173393}[NAS-ID Profile]{lang="PT-BR"}[，]{style="font-family:宋体"}[则此]{style="font-family:宋体"}[Profile]{lang="PT-BR"}[中定义的绑定关系优先使用]{style="font-family:宋体"}[；]{style="font-family:宋体"}[如果未指定]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[或指定的]{style="font-family:宋体"}[Profile]{lang="EN-US"}[中没有找到匹配的绑定关系，则使用设备名作为]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1704540217}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1488277588}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上指定名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_2217341}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-secutiry nas-id-profile aaa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x2026340247}[在系统视图下指定名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_129762758}

[\[Sysname\] port-secutiry nas-id-profile aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_89115918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aaa nas-id profile]{lang="EN-US"}**]{#struct_0_x2060_63618_1186103697}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1876013693 .myid}
[]{#_Toc404792856}[]{#struct_0_x2060_63618_x1448565905}[]{#_Toc257729110}[]{#_Toc131563070}

**端口安全 \-- 端口安全配置命令 \-- port-security ntk-mode**

------------------------------------------------------------------------

[**[port-security ntk-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x1581716871}[命令用来配置端口]{style="font-family:宋体"}[Need To Know]{lang="EN-US"}[特性。]{style="font-family:宋体"}

[**[undo port-security ntk-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x1696895431}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x532664711}

[**[port-security ntk-mode ]{lang="EN-US"}**[{ **ntk-withbroadcasts** \| **ntk-withmulticasts** \| **ntkonly** }]{lang="EN-US"}]{#struct_0_x2060_63618_x107540375}

[**[undo port-security ntk-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x1897729722}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369260714}

[[端口没有配置]{style="font-family:宋体"}[Need To Know]{lang="EN-US"}]{#struct_0_x2060_63618_2019054605}[特性，即所有报文都可成功发送。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_581880592}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_1828278412}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_656005369}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_860328990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x725199065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1344923067}

[**[ntk-withbroadcasts]{lang="EN-US"}**]{#struct_0_x2060_63618_x1108073557}[：允许目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为已通过认证的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的单播报文或广播地址的报文通过。]{style="font-family:宋体"}

[**[ntk-withmulticasts]{lang="EN-US"}**]{#struct_0_x2060_63618_1369195178}[：允许目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为已通过认证的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的单播报文，广播地址或组播地址的报文通过。]{style="font-family:宋体"}

[**[ntkonly]{lang="EN-US"}**]{#struct_0_x2060_63618_x1160734025}[：仅允许目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为已通过认证的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的单播报文通过。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_2004667363}

[[Need To Know]{lang="EN-US"}]{#struct_0_x2060_63618_1530230142}[特性通过检测从端口发出的数据帧的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，保证数据帧只能被发送到已经通过认证的设备上，从而防止非法设备窃听网络数据。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1977543328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无线端口上有用户在线的情况下，无法更改]{lang="EN-US" style="font-family:宋体"}[Need To Know]{lang="EN-US"}]{#struct_0_x2060_63618_395037691}[特性的配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Need To Know]{lang="EN-US"}]{#struct_0_x2060_63618_2092064909}[特性的配置生效情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1887035752}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_142137304}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Need To Know]{lang="EN-US"}[特性为]{style="font-family:宋体"}**[ntkonly]{lang="EN-US"}**[，即仅发送目的地址为已认证的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_1369129642}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security ntk-mode ntkonly]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1868618892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1629386137}
:::

::: {#-81690441 .myid}
[]{#_Toc404792857}[]{#struct_0_x2060_63618_1809186782}[]{#_Toc257729111}[]{#_Toc131563065}

**端口安全 \-- 端口安全配置命令 \-- port-security oui**

------------------------------------------------------------------------

[**[port-security oui]{lang="EN-US"}**]{#struct_0_x2060_63618_594414841}[命令用来配置允许通过认证的用户的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo port-security oui]{lang="EN-US"}**]{#struct_0_x2060_63618_826529676}[命令用来删除指定索引的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_2062887223}

[**[port-security oui index ]{lang="EN-US"}***[index-value ]{lang="EN-US"}***[mac-address ]{lang="EN-US"}***[oui-value]{lang="EN-US"}*]{#struct_0_x2060_63618_1162507906}

[**[undo port-security oui index ]{lang="EN-US"}***[index-value]{lang="EN-US"}*]{#struct_0_x2060_63618_1369064106}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_431892024}

[[不存在允许通过认证的用户]{style="font-family:宋体"}[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_1417604821}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1620301645}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_325560481}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1807567460}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_358514962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_2063285905}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_828739088}

[*[index-value]{lang="EN-US"}*]{#struct_0_x2060_63618_1369522858}[：标识此]{style="font-family:宋体"}[OUI]{lang="EN-US"}[的索引值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[oui-value]{lang="EN-US"}*]{#struct_0_x2060_63618_x1166132132}[：]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值，输入格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[的]{style="font-family:宋体"}[48]{lang="EN-US"}[位]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。系统会自动取输入的前]{style="font-family:宋体"}[24]{lang="EN-US"}[位做为]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值，忽略后]{style="font-family:宋体"}[24]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1258482673}

[[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_387611183}[是]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的前]{style="font-family:宋体"}[24]{lang="EN-US"}[位（二进制），是]{style="font-family:宋体"}[IEEE]{lang="EN-US"}[为不同设备供应商分配的一个全球唯一的标识符。当需要允许某些特殊设备的（有线接入）报文总是可以通过认证，或仅允许这些设备的（无线接入）报文可以进行认证的情况下，就可以通过本命令来指定这些设备的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值，例如，某公司仅允许]{style="font-family:宋体"}[A]{lang="EN-US"}[厂商的]{style="font-family:宋体"}[IP]{lang="EN-US"}[电话在本企业网内使用，则可以通过本命令将]{style="font-family:宋体"}[A]{lang="EN-US"}[厂商设备的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值设置为认证的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[可通过多次执行本命令，配置多个]{style="font-family:宋体"}[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_1252374478}[值。]{style="font-family:宋体"}

[[配置的]{style="font-family:宋体"}[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_1516720839}[值只在端口安全模式为]{style="font-family:宋体"}[userLoginWithOUI]{lang="EN-US"}[时生效。在]{style="font-family:宋体"}[userLoginWithOUI]{lang="EN-US"}[模式下，端口上除了允许一个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证用户接入之外，还额外允许一个特殊用户接入，该用户报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[与设备上配置的某个]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值相符。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x458881856}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_86277741}[配置一个允许通过认证的用户]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值为]{style="font-family:宋体"}[000d2a]{lang="EN-US"}[，索引为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_x24685955}

[\[Sysname\] port-security oui index 4 mac-address 000d-2a10-0033]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369457322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_408650631}
:::

::: {#-1993206321 .myid}
[]{#_Toc404792858}[]{#struct_0_x2060_63618_x1897182265}[]{#_Toc257729112}[]{#_Toc131563071}

**端口安全 \-- 端口安全配置命令 \-- port-security port-mode**

------------------------------------------------------------------------

[**[port-security port-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_1484494465}[命令用来配置端口安全模式。]{style="font-family:宋体"}

[**[undo port-security port-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_1035159896}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x2116532942}

[**[port-security port-mode ]{lang="EN-US"}**[{ **autolearn** \| **mac-authentication** \| **mac-else-userlogin-secure** \| **mac-else-userlogin-secure-ext** \| **secure** \| **userlogin** \| **userlogin-secure** \| **userlogin-secure-ext** \| **userlogin-secure-or-mac** \| **userlogin-secure-or-mac-ext** \| **userlogin-withoui** }]{lang="EN-US"}]{#struct_0_x2060_63618_1701367056}

[**[undo port-security port-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x822378016}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_286762448}

[[端口处于]{style="font-family:宋体"}[noRestrictions]{lang="EN-US"}]{#struct_0_x2060_63618_1368998567}[模式，此时该端口的安全功能关闭，端口处于不受端口安全限制的状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_852209103}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_1651032580}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_580795346}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x1959551682}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x51900565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1659907974}

[[表1-4 ]{lang="EN-US"}[安全模式的参数解释表]{style="font-family:黑体"}]{#struct_0_x2060_63618_x780799055}

[]{#table_struct_0_650236626}[[参数]{style="font-family:黑体"}]{#struct_0_x2060_63618_1368933031}
:::

[[安全模式]{style="font-family:黑体"}]{#struct_0_x2060_63618_x757550987}

[[说明]{style="font-family:黑体"}]{#struct_0_x2060_63618_320533105}

[**[autolearn]{lang="EN-US"}**]{#struct_0_x2060_63618_x931360865}

[[autoLearn]{lang="EN-US"}]{#struct_0_x2060_63618_12509752}

[[端口可通过手工配置或自动学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x1354838458}[地址。手工配置或自动学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址被称为安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，并被添加到安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中]{style="font-family:宋体"}

[[当端口下的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1409856614}[地址数超过端口安全允许的最大安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数后，端口模式会自动转变为]{style="font-family:宋体"}[secure]{lang="EN-US"}[模式。之后，该端口停止添加新的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，只有源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、通过命令]{style="font-family:宋体"}**[mac-address dynamic]{lang="EN-US"}**[或]{style="font-family:宋体"}**[mac-address static]{lang="EN-US"}**[手工配置的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文，才能通过该端口]{style="font-family:宋体"}

[**[mac-authentication]{lang="EN-US"}**]{#struct_0_x2060_63618_1368867495}

[[macAddressWithRadius]{lang="EN-US"}]{#struct_0_x2060_63618_818774792}

[[对接入用户采用]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x2133004601}[地址认证]{style="font-family:宋体"}

[[此模式下，端口允许多个用户接入]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1985275026}

[**[mac-else-userlogin-secure]{lang="EN-US"}**]{#struct_0_x2060_63618_x411219120}

[[macAddressElseUserLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_1368801959}

[[端口同时处于]{style="font-family:宋体"}[macAddressWithRadius]{lang="EN-US"}]{#struct_0_x2060_63618_1957939042}[模式和]{style="font-family:宋体"}[userLoginSecure]{lang="EN-US"}[模式，但]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证优先级大于]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。允许端口下一个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证用户及多个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户接入]{style="font-family:宋体"}

[[非]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_x299543509}[报文直接进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[报文先进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，如果]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证失败再进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{style="font-family:宋体"}

[**[mac-else-userlogin-secure-ext]{lang="EN-US"}**]{#struct_0_x2060_63618_x1647785931}

[[macAddressElseUserLoginSecureExt]{lang="EN-US"}]{#struct_0_x2060_63618_x52685202}

[[与]{style="font-family:宋体"}[macAddressElseUserLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_1369260711}[类似，但允许端口下有多个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户]{style="font-family:宋体"}

[**[secure]{lang="EN-US"}**]{#struct_0_x2060_63618_2018857997}

[[secure]{lang="EN-US"}]{#struct_0_x2060_63618_156658752}

[[禁止端口学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x374111385}[地址，只有源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为端口上的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、手工配置的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文，才能通过该端口]{style="font-family:宋体"}

[**[userlogin]{lang="EN-US"}**]{#struct_0_x2060_63618_x684683943}

[[userLogin]{lang="EN-US"}]{#struct_0_x2060_63618_173002900}

[[对接入用户采用基于端口的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_1369195175}[认证]{style="font-family:宋体"}

[[此模式下，端口下的第一个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_x1160537417}[用户认证成功后，其它用户无须认证就可接入]{style="font-family:宋体"}

[**[userlogin-secure]{lang="EN-US"}**]{#struct_0_x2060_63618_x1533430507}

[[userLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_x61889840}

[[对接入用户采用基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1369129639}[地址的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[此模式下，端口最多只允许一个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_x1867898001}[认证用户接入]{style="font-family:宋体"}

[**[userlogin-secure-ext]{lang="EN-US"}**]{#struct_0_x2060_63618_x2078687551}

[[userLoginSecureExt]{lang="EN-US"}]{#struct_0_x2060_63618_1494992928}

[[对接入用户采用基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_1369064103}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证，且允许端口下有多个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户]{style="font-family:宋体"}

[**[userlogin-secure-or-mac]{lang="EN-US"}**]{#struct_0_x2060_63618_431695416}

[[macAddressOrUserLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_1581957443}

[[端口同时处于]{style="font-family:宋体"}[userLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_1131926559}[模式和]{style="font-family:宋体"}[macAddressWithRadius]{lang="EN-US"}[模式，且允许一个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证用户及多个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户接入]{style="font-family:宋体"}

[[此模式下，]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2060_63618_1369522855}[认证优先级大于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证：报文首先进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证，如果]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证失败再进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证]{style="font-family:宋体"}

[**[userlogin-secure-or-mac-ext]{lang="EN-US"}**]{#struct_0_x2060_63618_x1166853028}

[[macAddressOrUserLoginSecureExt]{lang="EN-US"}]{#struct_0_x2060_63618_525448676}

[[与]{style="font-family:宋体"}[macAddressOrUserLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_1369457319}[类似，但允许端口下有多个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户]{style="font-family:宋体"}

[**[userlogin-withoui]{lang="EN-US"}**]{#struct_0_x2060_63618_408191876}

[[userLoginWithOUI]{lang="EN-US"}]{#struct_0_x2060_63618_x285426612}

[[与]{style="font-family:宋体"}[userLoginSecure]{lang="EN-US"}]{#struct_0_x2060_63618_1204629023}[模式类似，但端口上除了允许一个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证用户接入之外，还额外允许一个特殊用户接入，该用户报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[与设备上配置的]{style="font-family:宋体"}[OUI]{lang="EN-US"}[值相符]{style="font-family:宋体"}

[[此模式下，报文首先进行]{style="font-family:宋体"}[OUI]{lang="EN-US"}]{#struct_0_x2060_63618_852143567}[匹配，]{style="font-family:宋体"}[OUI]{lang="EN-US"}[匹配失败的报文再进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证，]{style="font-family:宋体"}[OUI]{lang="EN-US"}[匹配成功和]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证成功的报文都允许通过端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x519049424}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[各端口安全模式的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2060_63618_x679738889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口安全模式与端口下的]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1451270703}[802.1X]{lang="EN-US"}[认证使能、端口接入控制方式、端口授权状态以及端口下的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证使能配置互斥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当端口安全已经使能且当前端口安全模式不是]{lang="EN-US" style="font-family:宋体"}[noRestrictions]{lang="EN-US"}]{#struct_0_x2060_63618_x810703994}[时，若要改变端口安全模式，必须首先执行]{lang="EN-US" style="font-family:宋体"}**[undo port-security port-mode]{lang="EN-US"}**[命令恢复端口安全模式为]{lang="EN-US" style="font-family:宋体"}[noRestrictions]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置端口安全]{lang="EN-US" style="font-family:宋体"}[autoLearn]{lang="EN-US"}]{#struct_0_x2060_63618_x1828162312}[模式时，首先需要通过命令]{lang="EN-US" style="font-family:宋体"}**[port-security max-mac-count]{lang="EN-US"}**[设置端口安全允许的最大安全]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口上有用户在线的情况下，端口安全模式无法改变。]{style="font-family:宋体"}]{#struct_0_x2060_63618_1368933032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启了]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x757354379}[地址认证延迟功能的接口上不建议同时配置端口安全的模式为]{lang="EN-US" style="font-family:宋体"}**[mac-else-userlogin-secure]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[mac-else-userlogin-secure-ext]{lang="EN-US"}**[，否则]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证延迟功能不生效。]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证延迟功能的具体配置请参见"安全命令参考"中的"]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[部分端口安全模式的配置生效情况与设备的型号有关，请以设备的实际情况为准。即，]{style="font-family:宋体"}]{#struct_0_x2060_63618_378085332}[部分设备上不支持]{style="font-family:宋体"}[autoLearn]{lang="EN-US"}[模式、]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证的端口安全模式（]{style="font-family:宋体"}[userLoginSecure userLoginWithOUI userLoginSecureExt]{lang="EN-US"}[）以及基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的端口安全模式（]{style="font-family:宋体"}[macAddressWithRadius]{lang="EN-US"}[、]{style="font-family:宋体"}[macAddressOrUserLoginSecure]{lang="EN-US"}[、]{style="font-family:宋体"}[macAddressElseUserLoginSecure]{lang="EN-US"}[、]{style="font-family:宋体"}[macAddressOrUserLoginSecureExt]{lang="EN-US"}[、]{style="font-family:宋体"}[macAddressElseUserLoginSecureExt]{lang="EN-US"}[），因此相关配置不生效。]{style="font-family:
宋体"}

[[表1-5 ]{lang="EN-US"}[接口支持的端口安全模式列表]{style="font-family:黑体"}]{#struct_0_x2060_63618_584251626}

[]{#table_struct_0_649735264}[[接口类型]{style="font-family:黑体"}]{#struct_0_x2060_63618_847345559}

[[支持的端口安全模式]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1291736074}

[[二层以太网接口]{style="font-family:宋体"}]{#struct_0_x2060_63618_x1289437725}

[**[autolearn]{lang="EN-US"}**]{#struct_0_x2060_63618_1741042529}[、]{style="font-family:宋体"}**[mac-authentication]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac-else-userlogin-secure]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac-else-userlogin-secure-ext]{lang="EN-US"}**[、]{style="font-family:
  宋体"}**[secure]{lang="EN-US"}**[、]{style="font-family:
  宋体"}**[userlogin]{lang="EN-US"}**[、]{style="font-family:
  宋体"}**[userlogin-secure]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-secure-ext]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-secure-or-mac]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-secure-or-mac-ext]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-withoui]{lang="EN-US"}**

[[三层以太网接口]{style="font-family:宋体"}]{#struct_0_x2060_63618_1368867496}

[**[mac-authentication]{lang="EN-US"}**]{#struct_0_x2060_63618_818578184}[、]{style="font-family:宋体"}**[mac-else-userlogin-secure]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac-else-userlogin-secure-ext]{lang="EN-US"}**[、]{style="font-family:
  宋体"}**[userlogin-secure]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-secure-ext]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-secure-or-mac]{lang="EN-US"}**[、]{style="font-family:宋体"}**[userlogin-secure-or-mac-ext]{lang="EN-US"}**

[[备注：三层以太网接口下配置安全模式的支持情况与产品型号有关]{style="font-family:宋体"}]{#struct_0_x2060_63618_2688399}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1986709740}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_151135769}[使能端口安全，并配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的端口安全模式为]{style="font-family:宋体"}[secure]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_x897812007}

[\[Sysname\] port-security enable]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security port-mode secure]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1368801960}[将端口]{style="font-family:宋体"}[GigabitEthernet1/1]{lang="EN-US"}[的端口安全模式改变为]{style="font-family:宋体"}[userLogin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/1\] undo port-security port-mode]{lang="EN-US"}]{#struct_0_x2060_63618_1958397797}

[\[Sysname-GigabitEthernet1/]{lang="FR"}[0/]{lang="EN-US"}[1\] port-security port-mode userlogin]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1169945840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1431529040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security max-mac-count]{lang="EN-US"}**]{#struct_0_x2060_63618_x13259898}

::: {#-1822212030 .myid}
[]{#_Toc257729114}[]{#_Toc131563066}[]{#_Toc404792859}[]{#struct_0_x2060_63618_1677100884}[]{#_Toc269744548}[]{#_Toc286752740}[]{#_Toc286753578}[]{#_Toc286853455}[]{#_Toc286853684}[]{#_Toc293341734}[]{#_Toc286752743}[]{#_Toc286753581}[]{#_Toc286853458}[]{#_Toc286853687}[]{#_Toc293341737}[]{#_Toc286752745}[]{#_Toc286753583}[]{#_Toc286853460}[]{#_Toc286853689}[]{#_Toc293341739}[]{#_Toc286752746}[]{#_Toc286753584}[]{#_Toc286853461}[]{#_Toc286853690}[]{#_Toc293341740}[]{#_Toc286752748}[]{#_Toc286753586}[]{#_Toc286853463}[]{#_Toc286853692}[]{#_Toc293341742}[]{#_Toc286752749}[]{#_Toc286753587}[]{#_Toc286853464}[]{#_Toc286853693}[]{#_Toc293341743}[]{#_Toc286752750}[]{#_Toc286753588}[]{#_Toc286853465}[]{#_Toc286853694}[]{#_Toc293341744}[]{#_Toc286752751}[]{#_Toc286753589}[]{#_Toc286853466}[]{#_Toc286853695}[]{#_Toc293341745}[]{#_Toc286752752}[]{#_Toc286753590}[]{#_Toc286853467}[]{#_Toc286853696}[]{#_Toc293341746}[]{#_Toc286752753}[]{#_Toc286753591}[]{#_Toc286853468}[]{#_Toc286853697}[]{#_Toc293341747}[]{#_Toc286752754}[]{#_Toc286753592}[]{#_Toc286853469}[]{#_Toc286853698}[]{#_Toc293341748}[]{#_Toc286752755}[]{#_Toc286753593}[]{#_Toc286853470}[]{#_Toc286853699}[]{#_Toc293341749}[]{#_Toc286752756}[]{#_Toc286753594}[]{#_Toc286853471}[]{#_Toc286853700}[]{#_Toc293341750}[]{#_Toc286752757}[]{#_Toc286753595}[]{#_Toc286853472}[]{#_Toc286853701}[]{#_Toc293341751}[]{#_Toc286752758}[]{#_Toc286753596}[]{#_Toc286853473}[]{#_Toc286853702}[]{#_Toc293341752}[]{#_Toc286752759}[]{#_Toc286753597}[]{#_Toc286853474}[]{#_Toc286853703}[]{#_Toc293341753}[]{#_Toc286752760}[]{#_Toc286753598}[]{#_Toc286853475}[]{#_Toc286853704}[]{#_Toc293341754}[]{#_Toc286752761}[]{#_Toc286753599}[]{#_Toc286853476}[]{#_Toc286853705}[]{#_Toc293341755}[]{#_Toc286752762}[]{#_Toc286753600}[]{#_Toc286853477}[]{#_Toc286853706}[]{#_Toc293341756}[]{#_Toc286752763}[]{#_Toc286753601}[]{#_Toc286853478}[]{#_Toc286853707}[]{#_Toc293341757}[]{#_Toc286752767}[]{#_Toc286753605}[]{#_Toc286853482}[]{#_Toc286853711}[]{#_Toc293341761}[]{#_Toc286752768}[]{#_Toc286753606}[]{#_Toc286853483}[]{#_Toc286853712}[]{#_Toc293341762}[]{#_Toc286752771}[]{#_Toc286753609}[]{#_Toc286853486}[]{#_Toc286853715}[]{#_Toc293341765}[]{#_Toc286752774}[]{#_Toc286753612}[]{#_Toc286853489}[]{#_Toc286853718}[]{#_Toc293341768}[]{#_Toc286752775}[]{#_Toc286753613}[]{#_Toc286853490}[]{#_Toc286853719}[]{#_Toc293341769}[]{#_Toc286752776}[]{#_Toc286753614}[]{#_Toc286853491}[]{#_Toc286853720}[]{#_Toc293341770}[]{#_Toc286752779}[]{#_Toc286753617}[]{#_Toc286853494}[]{#_Toc286853723}[]{#_Toc293341773}[]{#_Toc286752780}[]{#_Toc286753618}[]{#_Toc286853495}[]{#_Toc286853724}[]{#_Toc293341774}[]{#_Toc286752783}[]{#_Toc286753621}[]{#_Toc286853498}[]{#_Toc286853727}[]{#_Toc293341777}[]{#_Toc286752784}[]{#_Toc286753622}[]{#_Toc286853499}[]{#_Toc286853728}[]{#_Toc293341778}[]{#_Toc286752785}[]{#_Toc286753623}[]{#_Toc286853500}[]{#_Toc286853729}[]{#_Toc293341779}[]{#_Toc286752787}[]{#_Toc286753625}[]{#_Toc286853502}[]{#_Toc286853731}[]{#_Toc293341781}

**端口安全 \-- 端口安全配置命令 \-- port-security timer autolearn aging**

------------------------------------------------------------------------

[**[port-security timer autolearn aging]{lang="EN-US"}**]{#struct_0_x2060_63618_x1695206177}[命令用来配置安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的老化时间。]{style="font-family:宋体"}

[**[undo port-security timer autolearn aging]{lang="EN-US"}**]{#struct_0_x2060_63618_x455721166}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_450919951}

[**[port-security timer autolearn aging ]{lang="EN-US"}***[time-value]{lang="EN-US"}*]{#struct_0_x2060_63618_1369260712}

[**[undo port-security timer autolearn aging]{lang="EN-US"}**]{#struct_0_x2060_63618_2018661389}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1374848067}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_x253063379}[地址不会老化。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1218669615}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_x281782578}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1632871466}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x495812990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_x686015110}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369195176}

[*[time-value]{lang="EN-US"}*]{#struct_0_x2060_63618_x1160602953}[：安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的老化时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[129600]{lang="EN-US"}[，单位为分钟，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不会老化。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x994067189}

[[安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2060_63618_607820244}[地址的老化时间对所有端口学习到的安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址以及手工添加的]{style="font-family:宋体"}[Sticky MAC]{lang="EN-US"}[地址均有效。]{style="font-family:宋体"}

[[较短的老化时间可提高端口接入的安全性和端口资源的利用率，但也会影响在线用户的在线稳定性，因此需要结合当前的网络环境和设备的性能合理设置老化时间。]{style="font-family:宋体"}]{#struct_0_x2060_63618_1707933818}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x805786074}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_x1845044550}[配置安全]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_252553645}

[\[Sysname\] port-security timer autolearn aging 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369129640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_x1868487820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security mac-address security]{lang="EN-US"}**]{#struct_0_x2060_63618_1641370250}
:::

::: {#-1965773354 .myid}
[]{#_Toc404792860}[]{#struct_0_x2060_63618_x361020421}

**端口安全 \-- 端口安全配置命令 \-- port-security timer disableport**

------------------------------------------------------------------------

[**[port-security timer disableport]{lang="EN-US"}**]{#struct_0_x2060_63618_x1729879966}[命令用来配置系统暂时关闭端口的时间。]{style="font-family:宋体"}

[**[undo port-security timer disableport]{lang="EN-US"}**]{#struct_0_x2060_63618_x1400878425}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1116906465}

[**[port-security timer disableport ]{lang="EN-US"}***[time-value]{lang="EN-US"}*]{#struct_0_x2060_63618_450316707}

[**[undo port-security timer disableport]{lang="EN-US"}**]{#struct_0_x2060_63618_x382374827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369064104}

[[系统暂时关闭端口的时间为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x2060_63618_432023096}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x380625115}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2060_63618_454921266}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x970373672}

[[network-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1778742976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2060_63618_1402543572}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2060_63618_x1709527385}

[*[time-value]{lang="EN-US"}*]{#struct_0_x2060_63618_x1704360487}[：端口关闭的时间，取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1369522856}

[[当]{style="font-family:宋体"}**[port-security intrusion-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x1167049636}[设置为]{style="font-family:宋体"}**[disableport-temporarily]{lang="EN-US"}**[模式时，系统暂时关闭端口的时间由该命令配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2060_63618_409740556}

[[\# ]{lang="EN-US"}]{#struct_0_x2060_63618_1390322177}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的入侵检测特性检测到非法报文后，将收到非法报文的端口暂时关闭]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2060_63618_x163549287}

[\[Sysname\] port-security timer disableport 30]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-security intrusion-mode disableport-temporarily]{lang="EN-US"}

[]{#_Toc257729115}[]{#_Toc131563067}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2060_63618_1430909168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-security]{lang="EN-US"}**]{#struct_0_x2060_63618_157238323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security intrusion-mode]{lang="EN-US"}**]{#struct_0_x2060_63618_x1520129599}

[ ]{lang="EN-US"}
:::
