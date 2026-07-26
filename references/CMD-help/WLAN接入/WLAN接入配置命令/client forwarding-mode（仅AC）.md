::::: {#164345303 .myid}
[]{#_Toc404794900}[]{#struct_0_95659_x1109_x42790710}[]{#_Toc393111387}

**WLAN接入 \-- WLAN接入配置命令 \-- client forwarding-mode（仅AC）**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](WLAN接入命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_95659_x1109_1897212578}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_95659_x1109_1136291770}
:::

[ ]{lang="EN-US"}

[**[client forwarding-mode]{lang="EN-US"}**]{#struct_0_95659_x1109_x301626078}[命令用配置客户端的数据报文在]{style="font-family:宋体"}[AP]{lang="EN-US"}[本地转发。]{style="font-family:宋体"}

[**[undo client forwarding-mode local]{lang="EN-US"}**]{#struct_0_95659_x1109_1045027547}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1523293231}

[**[client forwarding-mode local ]{lang="EN-US"}**[\[ **vlan** { *vlan-id1* \[ **to** *vlan-id2* \] } \]]{lang="EN-US"}]{#struct_0_95659_x1109_x1078488591}

[**[undo client forwarding-mode local]{lang="EN-US"}**]{#struct_0_95659_x1109_x583808992}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1659068258}

[[客户端的数据转发模式为集中转发。]{style="font-family:宋体"}]{#struct_0_95659_x1109_1324076685}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1427027294}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_797366722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1624990052}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x737791301}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_281505306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1321493799}

[**[vlan ]{lang="EN-US"}***[vlan-id1]{lang="EN-US"}***[ to]{lang="EN-US"}**[ *vlan-id2*]{lang="EN-US"}]{#struct_0_95659_x1109_1881930374}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的客户端的数据报文在]{style="font-family:宋体"}[AP]{lang="EN-US"}[本地转发。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，则表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的客户端数据报文均在]{style="font-family:宋体"}[AC]{lang="EN-US"}[进行集中转发。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1334212174}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只能在无线服务模板处于关闭状态下配置。]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1205590124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_95659_x1109_1357404874}[AC/FitAP]{lang="EN-US"}[的组网情况下，可以在]{style="font-family:宋体"}[AC]{lang="EN-US"}[上将客户端的数据报文转发模式配置成集中转发模式或者本地转发模式。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[若转发模式为集中转发时，客户端的数据流量由]{style="font-family:宋体"}]{#struct_0_95659_x1109_632705566}[AP]{lang="EN-US"}[通过]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道透传到]{style="font-family:宋体"}[AC]{lang="EN-US"}[，由]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发数据报文。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[若转发模式为本地转发时，客户端的数据流量直接由]{style="font-family:宋体"}]{#struct_0_95659_x1109_x333334392}[AP]{lang="EN-US"}[进行转发。将转发位置配置在]{style="font-family:宋体"}[AP]{lang="EN-US"}[上在保持了]{style="font-family:宋体"}[AC/Fit AP]{lang="EN-US"}[架构在安全、管理等方面的优势的前提下，缓解了]{style="font-family:宋体"}[AC]{lang="EN-US"}[的数据转发压力。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[本地转发可以基于]{style="font-family:宋体"}]{#struct_0_95659_x1109_413274063}[VLAN]{lang="EN-US"}[进行配置，即只有处于指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的客户端，才在]{style="font-family:宋体"}[AP]{lang="EN-US"}[本地转发其数据流量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_140050554}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_1499425354}[配置无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[的客户端的转发模式本地转发模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_95659_x1109_x1446464011}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client forwarding-mode local]{lang="EN-US"}
:::::

::: {#-499069877 .myid}
[]{#_Toc404794901}[]{#struct_0_95659_x1109_403332785}

**WLAN接入 \-- WLAN接入配置命令 \-- display wlan client**

------------------------------------------------------------------------

[**[display wlan client]{lang="EN-US"}**]{#struct_0_95659_x1109_394437155}[命令用来查看客户端的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1245032331}

[[AC]{lang="EN-US"}]{#struct_0_95659_x1109_1244945057}[设备：]{style="font-family:宋体"}

[**[display wlan client]{lang="EN-US"}**]{#struct_0_95659_x1109_x322837277}[ \[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **mac-address** *mac-address* \| **service-template** *service-template-name* \] \[ **verbose** \]]{lang="EN-US"}

[[FAT AP]{lang="EN-US"}]{#struct_0_95659_x1109_x431217023}[设备：]{style="font-family:宋体"}

[**[display wlan client]{lang="EN-US"}**]{#struct_0_95659_x1109_1376158750}[ \[ **interface wlan-radio** *interface-num*ber \| **mac-address** *mac-address* \| **service-template** *service-template-name* \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1025019198}

[[任意视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_1235701066}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1075470299}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x1771030453}

[[network-operator]{lang="EN-US"}]{#struct_0_95659_x1109_1071579524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_360493817}

[[mdc-operator]{lang="EN-US"}]{#struct_0_95659_x1109_x2034843855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_674185852}

[**[ap]{lang="EN-US"}**]{#struct_0_95659_x1109_569822254}[ *ap-nam*e]{lang="EN-US"}[：]{style="font-family:宋体"}[显示连接到指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的客户端信息。]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，]{style="font-family:宋体"}[不区分大小写。（仅]{style="font-family:宋体"}[AC]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_95659_x1109_394437156}[：]{style="font-family:宋体"}[显示连接到指定射频的客户端信息。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[。如果未指定本参数，表示显示连接到指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的客户端信息。（仅]{style="font-family:宋体"}[AC]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[wlan-radio ]{lang="EN-US"}***[interface-num]{lang="EN-US"}[ber]{lang="EN-US"}*]{#struct_0_95659_x1109_x1997300964}[：显示连接到指定射频接口的客户端信息。（仅]{style="font-family:宋体"}[FAT AP]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}**]{#struct_0_95659_x1109_1245032328}*[mac-address]{lang="EN-US"}*[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的客户端信息。]{style="font-family:宋体"}

[**[service-template]{lang="EN-US"}**]{#struct_0_95659_x1109_1244355234}[ *service-template-name*]{lang="EN-US"}[：]{style="font-family:宋体"}[显示连接到指定无线服务模板的客户端信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_95659_x1109_x707271125}[：]{style="font-family:宋体"}[显示客户端的详细信息。如果未指定本参数，表示显示客户端的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_776562008}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x718325481}[显示所有客户端的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan client]{lang="EN-US"}]{#struct_0_95659_x1109_349712420}

[Total number of clients: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[MAC address    Username            APID/RID  IP address                VLAN ID]{lang="EN-US"}

[000f-e265-6400 N/A                    1/1    1.1.1.1                   300]{lang="EN-US"}

[000f-e265-6401 user                1024/1    3.0.0.3                   300]{lang="EN-US"}

[000f-e265-6402 ]{lang="EN-US"}[[abcde]{lang="EN-US" style="color:windowtext;text-decoration:
none"}](mailto:mac@h3c.com)[                102/1    FE:11:12:03::11:25:13     300]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display wlan client]{lang="EN-US"}]{#struct_0_95659_x1109_x2039537032}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1112016431}[[字段]{style="font-family:黑体"}]{#struct_0_95659_x1109_x250501389}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_95659_x1109_x722043433}

[[MAC address]{lang="EN-US"}]{#struct_0_95659_x1109_674185853}

[[客户端的]{style="font-family:宋体"}]{#struct_0_95659_x1109_569822253}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_95659_x1109_403332787}

[[客户端的用户名，若客户端采用]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_1245032333}[认证或]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，则显示认证使用的用户名，若客户端不进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证或]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[需要注意的是，如果客户端采用]{style="font-family:宋体"}]{#struct_0_95659_x1109_1245076129}[Portal]{lang="EN-US"}[认证方式，]{style="font-family:宋体"}[Username]{lang="EN-US"}[字段不会显示客户端的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户名]{style="font-family:宋体"}

[[APID/RID]{lang="EN-US"}]{#struct_0_95659_x1109_x1472165834}

[[客户端的关联]{style="font-family:宋体"}]{#struct_0_95659_x1109_921709986}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[及]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[IP address]{lang="EN-US"}]{#struct_0_95659_x1109_1341543152}

[[客户端的]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1442394475}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_95659_x1109_x964502125}

[[客户端的所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_95659_x1109_x1364391335}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_569822260}[显示所有客户端的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan client verbose]{lang="EN-US"}]{#struct_0_95659_x1109_1977310900}

[Total number of clients: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[MAC address                        : 000f-e265-6400]{lang="EN-US"}

[Username                           : N/A]{lang="EN-US"}

[AP ID                              : 1]{lang="EN-US"}

[AP name                            : ap1]{lang="EN-US"}

[Radio ID                           : 1]{lang="EN-US"}

[SSID                               : office]{lang="EN-US"}

[BSSID                              : 0026-3e08-1150]{lang="EN-US"}

[VLAN ID                            : 3]{lang="EN-US"}

[Power save mode                    : Active]{lang="EN-US"}

[Wireless mode                      : 11gn]{lang="EN-US"}

[Channel bandwidth                  : 20MHz]{lang="EN-US"}

[SM power save                      : Disabled]{lang="EN-US"}

[Short GI for 20MHz                 : Not supported]{lang="EN-US"}

[Short GI for 40MHz                 : Supported]{lang="EN-US"}

[Support MCS set                    : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]{lang="EN-US"}

[Block Ack (TID 0)                  : In]{lang="EN-US"}

[QoS mode                           : WMM]{lang="EN-US"}

[Listen interval                    : 10]{lang="EN-US"}

[RSSI                               : 62]{lang="EN-US"}

[Rx/Tx rate                         : 130/11]{lang="EN-US"}

[Authentication method              : Open system]{lang="EN-US"}

[Security mode                      : PRE-RSNA]{lang="EN-US"}

[AKM mode                           : None]{lang="EN-US"}

[Cipher suite                       : N/A]{lang="EN-US"}

[User authentication mode           : Bypass]{lang="EN-US"}

[Authorization ACL ID               : 3001(Not effective)]{lang="EN-US"}

[Authorization user profile         : N/A]{lang="EN-US"}

[Roam status                        : Normal]{lang="EN-US"}

[Key derivation                     : SHA1]{lang="EN-US"}

[PMF status                         : Enabled]{lang="EN-US"}

[Online time                        : 0hr 1min 13sec]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display wlan client verbose]{lang="EN-US"}]{#struct_0_95659_x1109_977286442}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1118504849}[[字段]{style="font-family:黑体"}]{#struct_0_95659_x1109_1086137860}

[[描述]{style="font-family:黑体"}]{#struct_0_95659_x1109_674185855}

[[MAC address]{lang="EN-US"}]{#struct_0_95659_x1109_569822259}

[[客户端的]{style="font-family:宋体"}]{#struct_0_95659_x1109_403332797}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_95659_x1109_x1944215007}

[[客户端的用户名，若客户端采用]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x112092854}[认证或]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，则显示认证使用的用户名，若客户端不进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证或]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[需要注意的是，如果客户端采用]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1899042690}[Portal]{lang="EN-US"}[认证方式，]{style="font-family:宋体"}[Username]{lang="EN-US"}[字段不会显示客户端的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户名]{style="font-family:宋体"}

[[AP ID]{lang="EN-US"}]{#struct_0_95659_x1109_x869357018}

[[客户端的关联的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_95659_x1109_x1085976287}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[AP name]{lang="EN-US"}]{#struct_0_95659_x1109_x544797344}

[[接入点名称]{style="font-family:宋体"}]{#struct_0_95659_x1109_105171565}

[[Radio ID]{lang="EN-US"}]{#struct_0_95659_x1109_x164962898}

[[客户端关联的]{style="font-family:宋体"}]{#struct_0_95659_x1109_674185856}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[SSID]{lang="EN-US"}]{#struct_0_95659_x1109_569822258}

[[客户端关联的]{style="font-family:宋体"}]{#struct_0_95659_x1109_403332796}[SSID]{lang="EN-US"}

[[BSSID]{lang="EN-US"}]{#struct_0_95659_x1109_x1944215006}

[[基本服务集识别码]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1678176795}

[[VLAN ID]{lang="EN-US"}]{#struct_0_95659_x1109_1840277727}

[[客户端的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_95659_x1109_x187368177}

[[Power save mode]{lang="EN-US"}]{#struct_0_95659_x1109_687579064}

[[客户端节电模式的状态：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1398794633}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_95659_x1109_674185857}[：表示客户端处于正常工作状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sleep]{lang="EN-US"}]{#struct_0_95659_x1109_569822257}[：表示客户端处于睡眠状态]{style="font-family:宋体"}

[[Wireless mode]{lang="EN-US"}]{#struct_0_95659_x1109_403332783}

[[无线模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_394437157}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11a]{lang="EN-US"}]{#struct_0_95659_x1109_1245032329}[：表示客户端工作模式为]{style="font-family:宋体"}[ 802.11a]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11b]{lang="EN-US"}]{#struct_0_95659_x1109_1244420770}[：表示客户端工作模式为]{style="font-family:宋体"}[ 802.11b]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11g]{lang="EN-US"}]{#struct_0_95659_x1109_2008040271}[：表示客户端工作模式为]{style="font-family:宋体"}[ 802.11g]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11gn]{lang="EN-US"}]{#struct_0_95659_x1109_464918384}[：表示客户端工作模式为]{style="font-family:宋体"}[ 802.11gn]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11an]{lang="EN-US"}]{#struct_0_95659_x1109_x572868142}[：表示客户端工作模式为]{style="font-family:宋体"}[ 802.11an ]{lang="EN-US"}

[[Channel bandwidth]{lang="EN-US"}]{#struct_0_95659_x1109_1863664248}

[[客户端工作的带宽模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_2086675954}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[20MHz]{lang="EN-US"}]{#struct_0_95659_x1109_70693439}[：工作带宽为]{style="font-family:宋体"}[20MHz]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[40MHz]{lang="EN-US"}]{#struct_0_95659_x1109_x822304487}[：工作带宽为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}

[[SM Power Save ]{lang="EN-US"}]{#struct_0_95659_x1109_1140207251}

[[省电模式可以使客户端上只有一个天线处于工作状态，其余天线均处于休眠状态，从而达到节省电源的目的：]{style="font-family:宋体"}]{#struct_0_95659_x1109_1833303316}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_2031454682}[：省电模式处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_1863664249}[：]{lang="EN-US" style="font-family:宋体"}[省电模式处于关闭状态]{style="font-family:宋体"}

[[Short GI for 20MHz]{lang="EN-US"}]{#struct_0_95659_x1109_2086610418}

[[客户端工作带宽为]{style="font-family:宋体"}[20MHz]{lang="EN-US"}]{#struct_0_95659_x1109_x720737484}[时，对于]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[的支持情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_95659_x1109_x674788121}[：客户端支持]{lang="EN-US" style="font-family:宋体"}[Short GI]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:Symbol"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ]{lang="EN-US"}]{#struct_0_95659_x1109_1977638343}[s]{lang="EN-US"}[upported]{lang="EN-US"}[：客户端不支持]{lang="EN-US" style="font-family:宋体"}[Short GI]{lang="EN-US"}

[[Short GI for 40MHz]{lang="EN-US"}]{#struct_0_95659_x1109_x1286500375}

[[客户端工作带宽为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}]{#struct_0_95659_x1109_1863664250}[时，对于]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[的支持情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_95659_x1109_2087200241}[：客户端支持]{lang="EN-US" style="font-family:宋体"}[Short GI]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ]{lang="EN-US"}]{#struct_0_95659_x1109_x1081251157}[s]{lang="EN-US"}[upported]{lang="EN-US"}[：客户端不支持]{lang="EN-US" style="font-family:宋体"}[Short GI]{lang="EN-US"}

[[Support MCS set]{lang="EN-US"}]{#struct_0_95659_x1109_232278665}

[[客户端支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}]{#struct_0_95659_x1109_1816870413}

[[Block Ack (TID 0)]{lang="EN-US"}]{#struct_0_95659_x1109_x1477573604}

[[QoS TID]{lang="EN-US"}]{#struct_0_95659_x1109_1863664251}[的]{style="font-family:宋体"}[Block Ack]{lang="EN-US"}[协商结果：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In]{lang="EN-US"}]{#struct_0_95659_x1109_2087134705}[：表示上行数据报文支持]{lang="EN-US" style="font-family:宋体"}[Block Ack]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Out]{lang="EN-US"}]{#struct_0_95659_x1109_x1864942340}[：表示下行数据报文支持]{lang="EN-US" style="font-family:宋体"}[Block Ack]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both]{lang="EN-US"}]{#struct_0_95659_x1109_x822665629}[：表示上行和上行数据报文都支持]{lang="EN-US" style="font-family:宋体"}[Block Ack]{lang="EN-US"}

[[QoS mode]{lang="EN-US"}]{#struct_0_95659_x1109_x55073849}

[[QoS]{lang="EN-US"}]{#struct_0_95659_x1109_x710830198}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_95659_x1109_1863664252}[：不支持]{style="font-family:宋体"}[WMM]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WMM]{lang="EN-US"}]{#struct_0_95659_x1109_2087331313}[：支持]{style="font-family:宋体"}[WMM]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[WMM]{lang="EN-US"}]{#struct_0_95659_x1109_x697377048}[的支持情况，]{style="font-family:宋体"}[AP]{lang="EN-US"}[和客户端会进行协商。对于只有]{style="font-family:宋体"}[AP]{lang="EN-US"}[和客户端同时支持]{style="font-family:宋体"}[WMM]{lang="EN-US"}[时，才能协商成功]{style="font-family:宋体"}

[[Listen interval]{lang="EN-US"}]{#struct_0_95659_x1109_x1378772358}

[[处于]{style="font-family:宋体"}[Sleep]{lang="EN-US"}]{#struct_0_95659_x1109_2136399531}[模式的客户端定期醒来，接收缓存在]{style="font-family:宋体"}[AP]{lang="EN-US"}[中的数据帧的时间间隔，间隔时间单位为信标发送时间间隔]{style="font-family:宋体"}

[[RSSI]{lang="EN-US"}]{#struct_0_95659_x1109_1776695349}

[[客户端信号强度指示，该值表明了]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_95659_x1109_1863664253}[检测到客户端的信号强度]{style="font-family:宋体"}

[[Rx/Tx rate]{lang="EN-US"}]{#struct_0_95659_x1109_2087265777}

[[客户端发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95659_x1109_856797617}[接收报文的速率（包括数据、管理和控制报文）]{style="font-family:宋体"}

[[Authentication method]{lang="EN-US"}]{#struct_0_95659_x1109_857090596}

[[链路层认证方法：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x180834931}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Open system]{lang="EN-US"}]{#struct_0_95659_x1109_1863664254}[：开放系统认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shared key]{lang="EN-US"}]{#struct_0_95659_x1109_2086938097}[：共享密钥认证]{lang="EN-US" style="font-family:宋体"}

[[Security mode]{lang="EN-US"}]{#struct_0_95659_x1109_x1845246777}

[[安全模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_1283780786}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSN]{lang="EN-US"}]{#struct_0_95659_x1109_944600841}[：信标和探查响应帧携带]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WPA]{lang="EN-US"}]{#struct_0_95659_x1109_1863664255}[：信标和探查响应帧携带]{style="font-family:宋体"}[WPA IE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRE-RSN]{lang="EN-US"}]{#struct_0_95659_x1109_2086872561}[：信标和探查响应帧不携带]{lang="EN-US" style="font-family:宋体"}[RSN IE]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[WPA IE]{lang="EN-US"}

[[AKM mode]{lang="EN-US"}]{#struct_0_95659_x1109_442728633}

[[身份认证与密钥管理模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_864826860}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x917831048}[：表示身份认证与密钥管理模式是]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSK]{lang="EN-US"}]{#struct_0_95659_x1109_1863664256}[：表示身份认证与密钥管理模式是]{style="font-family:宋体"}[PSK]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Cipher suite]{lang="EN-US"}]{#struct_0_95659_x1109_2087069169}

[[加密套件：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x677365062}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_95659_x1109_680222728}[：明文方式，不加密]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP40]{lang="EN-US"}]{#struct_0_95659_x1109_195650556}[：使用]{lang="EN-US" style="font-family:宋体"}[WEP40]{lang="EN-US"}[加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP104]{lang="EN-US"}]{#struct_0_95659_x1109_1863664257}[：使用]{lang="EN-US" style="font-family:宋体"}[WEP104]{lang="EN-US"}[加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP128]{lang="EN-US"}]{#struct_0_95659_x1109_2087003633}[：使用]{lang="EN-US" style="font-family:宋体"}[WEP128]{lang="EN-US"}[加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CCMP]{lang="EN-US"}]{#struct_0_95659_x1109_x279972263}[：使用]{lang="EN-US" style="font-family:宋体"}[AES-CCMP]{lang="EN-US"}[加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP]{lang="EN-US"}]{#struct_0_95659_x1109_x801772524}[：使用]{lang="EN-US" style="font-family:宋体"}[TKIP]{lang="EN-US"}[加密套件]{lang="EN-US" style="font-family:宋体"}

[[User authentication mode]{lang="EN-US"}]{#struct_0_95659_x1109_x92650888}

[[用户认证模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x908745191}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bypass]{lang="EN-US"}]{#struct_0_95659_x1109_x61654891}[：不做用户认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_95659_x1109_x1990297772}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x92650887}[：]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OUI ]{lang="EN-US"}]{#struct_0_95659_x1109_x908745196}[：]{style="font-family:宋体"}[OUI]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[Authorization ACL ID]{lang="EN-US"}]{#struct_0_95659_x1109_x62113643}

[[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_95659_x1109_1898846111}[对应的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权]{style="font-family:宋体"}]{#struct_0_95659_x1109_x92650886}[ACL]{lang="EN-US"}[生效，则显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_95659_x1109_x908745197}[未生效，则显示]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[编号]{lang="EN-US" style="font-family:宋体"}[ + N]{lang="EN-US"}[ot]{lang="EN-US"}[ effective]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置授权]{style="font-family:宋体"}]{#struct_0_95659_x1109_x62048107}[ACL]{lang="EN-US"}[，显示]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Authorization user profile]{lang="EN-US"}]{#struct_0_95659_x1109_x92650885}

[[授权]{style="font-family:宋体"}[User profile]{lang="EN-US"}]{#struct_0_95659_x1109_x908745194}[名称：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果下发授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_95659_x1109_x61982571}[生效，显示]{lang="EN-US" style="font-family:宋体"}[Authorization User Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果下发授权]{style="font-family:宋体"}]{#struct_0_95659_x1109_x607375118}[User Profile]{lang="EN-US"}[未生效，显示]{style="font-family:宋体"}[Authorization User Profile]{lang="EN-US"}[名称]{style="font-family:宋体"}[+Not effective]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置授权]{style="font-family:宋体"}]{#struct_0_95659_x1109_x92650884}[User profile]{lang="EN-US"}[，显示]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Roam status]{lang="EN-US"}]{#struct_0_95659_x1109_x908745195}

[[漫游状态：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x61917035}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Roaming in progress]{lang="EN-US"}]{#struct_0_95659_x1109_x92650883}[：漫游切换中]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inter-AC slow roam]{lang="EN-US"}]{#struct_0_95659_x1109_x908745200}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[间慢速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inter-AC fast roam]{lang="EN-US"}]{#struct_0_95659_x1109_1512257676}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[间快速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra-AC slow roam]{lang="EN-US"}]{#struct_0_95659_x1109_x92650882}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[内慢速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra-AC fast roam]{lang="EN-US"}]{#struct_0_95659_x1109_x908745201}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[内快速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inter-MA slow roam]{lang="EN-US"}]{#struct_0_95659_x1109_1512323212}[：]{lang="EN-US" style="font-family:
  宋体"}[MA]{lang="EN-US"}[间慢速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inter-MA fast roam]{lang="EN-US"}]{#struct_0_95659_x1109_x92650881}[：]{lang="EN-US" style="font-family:
  宋体"}[MA]{lang="EN-US"}[间快速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra-MA slow roam]{lang="EN-US"}]{#struct_0_95659_x1109_x908745198}[：]{lang="EN-US" style="font-family:
  宋体"}[MA]{lang="EN-US"}[内慢速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra-MA fast roam]{lang="EN-US"}]{#struct_0_95659_x1109_x62244715}[：]{lang="EN-US" style="font-family:
  宋体"}[MA]{lang="EN-US"}[内快速漫游]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_95659_x1109_x1372943167}[：客户端正常上线]{style="font-family:宋体"}

[[Key derivation]{lang="EN-US" style="color:black"}]{#struct_0_95659_x1109_x802371133}

[[密钥衍生类型，包括以下几种：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_985752991}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA1]{lang="EN-US"}]{#struct_0_95659_x1109_x906464556}[：]{style="font-family:宋体"}[SHA1 Key Derivation]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA256]{lang="EN-US"}]{#struct_0_95659_x1109_1476173528}[：]{style="font-family:宋体"}[SHA256 Key Derivation]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_95659_x1109_1968417153}[：不涉及密钥衍生算法]{style="font-family:宋体"}

[[PMF status]{lang="EN-US" style="color:black"}]{#struct_0_95659_x1109_262767488}

[[保护管理帧状态，包括以下几种：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_x1252709827}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_1038700919}[：保护管理帧功能开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_1450054843}[：保护管理帧功能关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_95659_x1109_1119877632}[：不涉及保护管理帧功能]{style="font-family:宋体"}

[[Online time]{lang="EN-US"}]{#struct_0_95659_x1109_x92650880}

[[客户端在线的时间]{style="font-family:宋体"}]{#struct_0_95659_x1109_x908745199}

[ ]{lang="EN-US"}

::: {#250171928 .myid}
[]{#_Toc404794902}[]{#struct_0_95659_x1109_x62179179}[]{#_Toc351972630}

**WLAN接入 \-- WLAN接入配置命令 \-- display wlan service-template**

------------------------------------------------------------------------

[**[display wlan service-template]{lang="EN-US" style="color:windowtext"}**]{#struct_0_95659_x1109_x482380260}[命令用来查看无线服务模板信息。]{style="font-family:宋体;color:windowtext"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1945156465}

[**[display wlan service-template ]{lang="EN-US"}**[\[ *service-template-name* \]]{lang="EN-US"}]{#struct_0_95659_x1109_1778114909}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1727264941}

[[任意视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_167850521}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_95982131}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x1551373303}

[[network-operator]{lang="EN-US"}]{#struct_0_95659_x1109_575243621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x1609005723}

[[mdc-operator]{lang="EN-US"}]{#struct_0_95659_x1109_x1756533436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1002920175}

[*[service-template-name]{lang="EN-US"}*]{#struct_0_95659_x1109_x92650879}[：]{style="font-family:宋体"}[无线服务模板名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。不区分大小写。如果未指定本参数，则显示所有无线服务模板的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x188701158}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x322520667}[显示无线服务模板信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan service-template]{lang="EN-US"}]{#struct_0_95659_x1109_x2048966024}

[Service template name        : service1]{lang="EN-US"}

[SSID                         : wuxianfuwu]{lang="EN-US"}

[SSID-hide                    : Disabled]{lang="EN-US"}

[Service template status      : Disabled]{lang="EN-US"}

[Maximum clients per BSS      : 64]{lang="EN-US"}

[VLAN ID                      : 1]{lang="EN-US"}

[AKM mode                     : PSK]{lang="EN-US"}

[Security IE                  : RSN]{lang="EN-US"}

[Cipher suite                 : WEP40]{lang="EN-US"}

[WEP key ID                   : 1]{lang="EN-US"}

[TKIP countermeasure time     : 100 sec]{lang="EN-US"}

[PTK lifetime                 : 43200 sec]{lang="EN-US"}

[GTK rekey                    : Enabled]{lang="EN-US"}

[GTK rekey method             : Time-based]{lang="EN-US"}

[GTK rekey time               : 86400 sec]{lang="EN-US"}

[GTK rekey client-offline     : Enabled]{lang="EN-US"}

[User authentication mode     : Central]{lang="EN-US"}

[Authentication mode          : 802.1X]{lang="EN-US"}

[Intrusion protection         : Disabled]{lang="EN-US"}

[Intrusion protection mode    : Temporary-block]{lang="EN-US"}

[Temporary block time         : 180 sec]{lang="EN-US"}

[Temporary service stop time  : 20 sec]{lang="EN-US"}

[Fail VLAN ID                 : 1]{lang="EN-US"}

[Critical VLAN ID             : Not configured]{lang="EN-US"}

[802.1X handshake             : Enabled]{lang="EN-US"}

[802.1X handshake secure      : Disabled]{lang="EN-US"}

[802.1X domain                : my-domain]{lang="EN-US"}

[MAC-auth domain              : Not configured]{lang="EN-US"}

[Max 802.1X users             : 4096]{lang="EN-US"}

[Max MAC-auth users           : 4096]{lang="EN-US"}

[802.1X re-authenticate       : Enabled]{lang="EN-US"}

[Authorization fail mode      : Online]{lang="EN-US"}

[Accounting fail mode         : Online]{lang="EN-US"}

[Authorization                : Permitted]{lang="EN-US"}

[Key derivation               : SHA1]{lang="EN-US"}

[PMF status                   : Optional]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display wlan service-template]{lang="EN-US"}]{#struct_0_95659_x1109_1579474081}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1121034159}[[字段]{style="font-family:黑体"}]{#struct_0_95659_x1109_x361101578}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1335913129}

[[Service template name]{lang="EN-US"}]{#struct_0_95659_x1109_319030472}

[[当前无线服务模板名称]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1972886988}

[[SSID]{lang="EN-US"}]{#struct_0_95659_x1109_x381288762}

[[客户端关联的]{style="font-family:宋体"}[SSID]{lang="EN-US"}]{#struct_0_95659_x1109_x654139542}

[[SSID-hide]{lang="EN-US"}]{#struct_0_95659_x1109_1034297918}

[[SSID]{lang="EN-US"}]{#struct_0_95659_x1109_x2089437301}[隐藏]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_774058583}[：启用]{lang="EN-US" style="font-family:宋体"}[SSID]{lang="EN-US"}[通告]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_1434962936}[：禁用]{lang="EN-US" style="font-size:10.0pt;font-family:宋体"}[SSID]{lang="EN-US" style="font-size:10.0pt"}[通告]{lang="EN-US" style="font-size:10.0pt;
  font-family:宋体"}

[[Service template status]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_x2048966023}

[[无线服务模板状态：]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_95659_x1109_13390140}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_x77188366}[：无线服务模板处于关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_x1876723813}[：无线服务模板处于开启状态]{style="font-family:宋体"}

[[Maximum clients per BSS]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_1830477819}

[[一个]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_95659_x1109_x159402299}[BSS]{lang="EN-US" style="font-size:10.0pt"}[中能够连接的最大客户端数]{style="font-size:10.0pt;font-family:
  宋体"}

[[VLAN ID]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_1388579162}

[[无线服务模板配置的]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_x822851956}[VLAN ID]{lang="EN-US" style="font-size:10.0pt"}

[[AKM mode]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_x823232910}

[[身份认证与密钥管理模式：]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_x2048966022}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x1552693801}[：以]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[作为身份认证与密钥管理模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSK]{lang="EN-US"}]{#struct_0_95659_x1109_303921251}[：以]{style="font-family:宋体"}[PSK]{lang="EN-US"}[作为身份认证与密钥管理模式]{style="font-family:宋体"}

[[Security IE]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_720106892}

[[安全]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_871542586}[IE]{lang="EN-US" style="font-size:10.0pt"}[类型：]{style="font-size:10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSN]{lang="EN-US"}]{#struct_0_95659_x1109_x500007912}[：]{lang="EN-US" style="font-family:宋体"}[RSN]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[IE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WPA]{lang="EN-US"}]{#struct_0_95659_x1109_x634827185}[：]{lang="EN-US" style="font-family:宋体"}[WPA]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[IE]{lang="EN-US"}

[[Cipher suite]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_x965507763}

[[加密套件：]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_943411556}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP40]{lang="EN-US"}]{#struct_0_95659_x1109_x2048966021}[：使用]{lang="EN-US" style="font-family:宋体"}[WEP40]{lang="EN-US"}[作为加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP104]{lang="EN-US"}]{#struct_0_95659_x1109_1176189554}[：使用]{lang="EN-US" style="font-family:宋体"}[WEP104]{lang="EN-US"}[作为加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP128]{lang="EN-US"}]{#struct_0_95659_x1109_506272634}[：使用]{lang="EN-US" style="font-family:宋体"}[WEP128]{lang="EN-US"}[作为加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TKIP]{lang="EN-US"}]{#struct_0_95659_x1109_782302989}[：使用]{lang="EN-US" style="font-family:宋体"}[TKIP]{lang="EN-US"}[作为加密套件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CCMP]{lang="EN-US"}]{#struct_0_95659_x1109_x2020920364}[：使用]{lang="EN-US" style="font-family:宋体"}[CCMP]{lang="EN-US"}[作为加密套件]{lang="EN-US" style="font-family:宋体"}

[[WEP key ID]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_x1773379546}

[[WEP]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_95659_x1109_2034363404}[密钥]{style="font-size:10.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:10.0pt"}

[[TKIP countermeasure time]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_197098642}

[[TKIP]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_95659_x1109_x2048966020}[反制策略的时间，]{style="font-size:10.0pt;font-family:宋体"}[0]{lang="EN-US" style="font-size:10.0pt"}[表示不启动反制策略]{style="font-size:10.0pt;
  font-family:宋体"}

[[PTK life time]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_x389894387}

[[PTK]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_95659_x1109_x106031134}[的生存时间]{style="font-size:10.0pt;font-family:宋体"}

[[GTK rekey]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_818898202}

[[GTK]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_95659_x1109_2017175790}[更新功能状态：]{style="font-size:10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_x1558096357}[：开启状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_x2048966019}[：关闭状态]{lang="EN-US" style="font-family:宋体"}

[[GTK rekey method]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_1532616522}

[[GTK]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_653667232}[更新方法：]{style="font-size:10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Time-based]{lang="EN-US"}]{#struct_0_95659_x1109_380755879}[：基于时间更新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet-based]{lang="EN-US"}]{#struct_0_95659_x1109_x1595424610}[：基于报文数更新]{lang="EN-US" style="font-family:宋体"}

[[GTK rekey time]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_x2048966018}

[[GTK]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_95659_x1109_x33467419}[更新的时间间隔]{style="font-size:10.0pt;font-family:宋体"}

[[GTK rekey packets]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_671289456}

[[触发]{style="font-size:10.0pt;font-family:
  宋体"}]{#struct_0_95659_x1109_4897557}[GTK]{lang="EN-US" style="font-size:10.0pt"}[更新的最大报文数量]{style="font-size:10.0pt;font-family:宋体"}

[[GTK rekey client-offline]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_1710275819}

[[客户端离线更新功能状态：]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_x2048966017}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_1982955216}[：开启状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_x595542701}[：关闭状态]{lang="EN-US" style="font-family:宋体"}

[[User authentication mode]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_95659_x1109_1791311055}

[[用户认证点模式：]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_723706935}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Central]{lang="EN-US"}]{#struct_0_95659_x1109_1114647509}[：集中式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Split]{lang="EN-US"}]{#struct_0_95659_x1109_x2048966016}[：分离式]{lang="EN-US" style="font-family:宋体"}

[[Authentication mode]{lang="EN-US"}]{#struct_0_95659_x1109_416871275}

[[认证模式，包括以下几种：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x2146621337}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bypass]{lang="EN-US"}]{#struct_0_95659_x1109_1970741980}[：不认证模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_95659_x1109_x1728921597}[：只进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC-or-802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_862559422}[：先进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，如果失败在进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x2048966015}[：只进行]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X-or-MAC]{lang="EN-US"}]{#struct_0_95659_x1109_x1149212666}[：先进行]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证，如果失败，再进行]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OUI-or-802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x2001085156}[：先进行]{style="font-family:宋体"}[OUI]{lang="EN-US"}[认证，如果失败，再进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[Intrusion protec]{lang="EN-US"}]{#struct_0_95659_x1109_2090792115}[tion]{lang="EN-US"}

[[入侵检测功能使能状态：]{style="font-family:宋体"}]{#struct_0_95659_x1109_174088918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_289686136}[：入侵检测功能处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_298833551}[：入侵检测功能处于关闭状态]{style="font-family:宋体"}

[[Intrusion protec]{lang="EN-US"}]{#struct_0_95659_x1109_1739698516}[tion]{lang="EN-US"}[ mode]{lang="EN-US"}

[[入侵检测特性模式，包括以下三种：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x712394319}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Temporary-block]{lang="EN-US"}]{#struct_0_95659_x1109_1150264518}[：表示临时将用户]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[加入阻止]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[列表中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service-stop]{lang="EN-US"}]{#struct_0_95659_x1109_289686137}[：表示直接关闭对应]{lang="EN-US" style="font-family:宋体"}[BSS]{lang="EN-US"}[上的所有服务，直到重启该]{lang="EN-US" style="font-family:宋体"}[BSS]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Temporary-service-stop]{lang="EN-US"}]{#struct_0_95659_x1109_298833552}[：表示临时关闭收到非法报文的]{lang="EN-US" style="font-family:宋体"}[BSS]{lang="EN-US"}[所提供的接入服务]{lang="EN-US" style="font-family:宋体"}

[[Temporary block time]{lang="EN-US"}]{#struct_0_95659_x1109_1739698519}

[[临时阻塞非法入侵用户的时长，单位为秒]{style="font-family:宋体"}]{#struct_0_95659_x1109_x713115215}

[[Temporary service stop time]{lang="EN-US"}]{#struct_0_95659_x1109_289686138}

[[临时关闭]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_95659_x1109_298833553}[服务时长，单位为秒]{style="font-family:宋体"}

[[Fail VLAN ID]{lang="EN-US"}]{#struct_0_95659_x1109_1739698518}

[[认证失败的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_95659_x1109_x713049679}[。未配置，则显示"]{style="font-family:宋体"}[Not configured]{lang="EN-US"}["]{style="font-family:宋体"}

[[Critical VLAN ID]{lang="EN-US"}]{#struct_0_95659_x1109_x826080780}

[[认证服务器不可达]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_95659_x1109_289686139}[。未配置，则显示"]{style="font-family:宋体"}[Not configured]{lang="EN-US"}["]{style="font-family:宋体"}

[[802.1X handshake]{lang="EN-US"}]{#struct_0_95659_x1109_298833554}

[[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_1739698513}[握手功能开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_x712721999}[：开启状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_289686140}[：关闭状态]{lang="EN-US" style="font-family:宋体"}

[[802.1X handshake secure]{lang="EN-US"}]{#struct_0_95659_x1109_x1657481591}

[[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_452621363}[安全握手功能开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_218725612}[：开启状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_x2098441245}[：关闭状态]{lang="EN-US" style="font-family:宋体"}

[[802.1X domain]{lang="EN-US"}]{#struct_0_95659_x1109_289686141}

[[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x1657481590}[认证域的域名。未配置，则显示"]{style="font-family:宋体"}[Not configured]{lang="EN-US"}["]{style="font-family:宋体"}

[[MAC-auth domain]{lang="EN-US"}]{#struct_0_95659_x1109_2018705304}

[[MAC]{lang="EN-US"}]{#struct_0_95659_x1109_289686142}[地址认证域的域名。未配置，则显示"]{style="font-family:宋体"}[Not configured]{lang="EN-US"}["]{style="font-family:宋体"}

[[Max 802.1X users]{lang="EN-US"}]{#struct_0_95659_x1109_x1657481589}

[[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_808786187}[认证的最大用户数]{style="font-family:宋体"}

[[Max MAC-auth users]{lang="EN-US"}]{#struct_0_95659_x1109_x751696223}

[[MAC]{lang="EN-US"}]{#struct_0_95659_x1109_289686143}[地址认证的最大用户数]{style="font-family:宋体"}

[[802.1X re-authenticate]{lang="EN-US"}]{#struct_0_95659_x1109_x1657481588}

[[802.1X]{lang="EN-US"}]{#struct_0_95659_x1109_x1920097168}[重认证功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_95659_x1109_289686144}[：开启状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_x1657481587}[：关闭状态]{lang="EN-US" style="font-family:宋体"}

[[Authorization fail mode]{lang="EN-US"}]{#struct_0_95659_x1109_x710243587}

[[授权失败处理模式包括以下两种模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_2089579553}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_95659_x1109_289686145}[：强制下线模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_95659_x1109_x1657481586}[：非强制下线模式]{lang="EN-US" style="font-family:宋体"}

[[Accounting fail mode]{lang="EN-US"}]{#struct_0_95659_x1109_855840354}

[[计费请求失败处理模式包括以下两种模式：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1220812704}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_95659_x1109_x1666629000}[：下线模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_95659_x1109_1558531976}[：非下线模式]{lang="EN-US" style="font-family:宋体"}

[[Authorization]{lang="EN-US"}]{#struct_0_95659_x1109_x2058244145}

[[服务器的授权信息：]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1666628999}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permitted]{lang="EN-US"}]{#struct_0_95659_x1109_x230351022}[：应用]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或本地设备下发的授权信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ignored]{lang="EN-US"}]{#struct_0_95659_x1109_1888710041}[：忽略]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或本地设备下发的授权信息]{style="font-family:宋体"}

[[Key derivation]{lang="EN-US" style="color:black"}]{#struct_0_95659_x1109_1254095360}

[[密钥衍生类型，包括以下几种：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_1764154896}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA1]{lang="EN-US"}]{#struct_0_95659_x1109_x1474787995}[：表示使用]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[算法衍生密钥]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA256]{lang="EN-US"}]{#struct_0_95659_x1109_x2020773472}[：表示使用]{style="font-family:宋体"}[SHA256]{lang="EN-US"}[算法衍生密钥]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA1-AND-SHA256]{lang="EN-US"}]{#struct_0_95659_x1109_x1180514926}[：表示使用]{style="font-family:宋体"}[SHA1 and SHA256]{lang="EN-US"}[算法衍生密钥]{style="font-family:宋体"}

[[PMF status]{lang="EN-US" style="color:black"}]{#struct_0_95659_x1109_91295946}

[[保护管理帧状态，包括以下几种：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_95659_x1109_x1759685988}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_95659_x1109_1657379887}[：保护管理帧功能关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Optional]{lang="EN-US"}]{#struct_0_95659_x1109_520574312}[：保护管理帧功能可选]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mandatory]{lang="EN-US"}]{#struct_0_95659_x1109_x152985868}[：保护管理帧功能强制]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-954920834 .myid}
[]{#_Toc404794903}[]{#struct_0_95659_x1109_x1666628998}

**WLAN接入 \-- WLAN接入配置命令 \-- service-template**

------------------------------------------------------------------------

[[AC]{lang="EN-US"}]{#struct_0_95659_x1109_1335732919}[设备：]{style="font-family:宋体"}

[**[service-template]{lang="EN-US"}**]{#struct_0_95659_x1109_x1272185359}[命令用来将无线服务模板绑定到当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上。]{style="font-family:宋体"}

[**[undo service-template]{lang="EN-US"}**]{#struct_0_95659_x1109_767898794}[命令用来解除当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[与无线服务模板的绑定关系。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_95659_x1109_x1997169892}[设备：]{style="font-family:宋体"}

[**[service-template]{lang="EN-US"}**]{#struct_0_95659_x1109_x19100723}[命令用来将无线服务模板绑定到当前]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[射频接口上。]{style="font-family:宋体"}

[**[undo service-template]{lang="EN-US"}**]{#struct_0_95659_x1109_x1594910243}[命令用来解除当前]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[射频接口上与无线服务模板的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1196843892}

[[AC]{lang="EN-US"}]{#struct_0_95659_x1109_x1523516965}[设备：]{style="font-family:宋体"}

[**[service-template ]{lang="EN-US"}***[service-template-name ]{lang="EN-US"}*[\[ **vlan** *vlan-id \|* **vlan-group** *vlan-group-name* \]]{lang="EN-US"}]{#struct_0_95659_x1109_1333674200}

[**[undo service-template ]{lang="EN-US"}***[service-template-name ]{lang="EN-US"}*]{#struct_0_95659_x1109_x1534508435}

[[FAT AP]{lang="EN-US"}]{#struct_0_95659_x1109_x1247258628}[设备：]{style="font-family:宋体"}

[**[service-template ]{lang="EN-US"}***[service-template-name]{lang="EN-US"}*]{#struct_0_95659_x1109_x203988719}

[**[undo service-template ]{lang="EN-US"}***[service-template-name]{lang="EN-US"}*]{#struct_0_95659_x1109_x1253337440}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_411437989}

[[未绑定无线服务模版]{style="font-family:宋体"}]{#struct_0_95659_x1109_1467621447}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1869137953}

[[AC]{lang="EN-US"}]{#struct_0_95659_x1109_x1891531793}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_95659_x1109_x1950115725}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1760752587}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_692993192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x726758501}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1510824366}

[*[service-template-name]{lang="EN-US"}*]{#struct_0_95659_x1109_x1666628997}[：]{style="font-family:宋体;
color:black"}[无线服务模板名字，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[63]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写。]{style="font-family:宋体;color:black"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_95659_x1109_932448392}[：无线服务模板绑定]{style="font-family:宋体;color:black"}[Radio]{lang="EN-US" style="color:black"}[时绑定的]{style="font-family:宋体;color:black"}[VLAN ID]{lang="EN-US" style="color:black"}[，]{style="font-family:宋体;
color:black"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan-group]{lang="EN-US"}***[ vlan-group-name]{lang="EN-US"}*]{#struct_0_95659_x1109_x259150121}[：指定无线服务模板绑定]{style="font-family:宋体"}[Radio]{lang="EN-US"}[时绑定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[组，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x112725500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当只指定无线服务模板名字时，该无线服务模板须先被创建才可完成绑定。]{style="font-family:宋体"}]{#struct_0_95659_x1109_1991520401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定]{style="font-family:宋体"}]{#struct_0_95659_x1109_x672835574}[VLAN ID]{lang="EN-US"}[时，该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[须已经创建才可完成绑定，否则绑定失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_95659_x1109_924344530}[组由]{style="font-family:宋体"}**[vlan-group]{lang="EN-US"}**[命令创建，有关该命令的详细介绍，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[VLAN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1764426537}

[[AC]{lang="EN-US"}]{#struct_0_95659_x1109_797773548}[设备：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_621901957}[将无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[绑定到]{style="font-family:宋体"}[Radio1]{lang="EN-US"}[上，并绑定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[组]{style="font-family:宋体"}[vg1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_95659_x1109_1619204060}

[\[Sysname\] wlan ap ap1]{lang="EN-US"}

[\[Sysname-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-ap-ap1-radio-1\] service-template service1 vlan-group vg1]{lang="EN-US"}

[[FAT AP]{lang="EN-US"}]{#struct_0_95659_x1109_778767630}[设备：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_1381647867}[将无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[绑定到]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[射频接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_95659_x1109_516216059}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-wlan-radio-1\] service-template service1]{lang="EN-US"}
:::

::: {#312953742 .myid}
[]{#_Toc351972629}[]{#_Toc351031906}[]{#_Toc404794904}[]{#struct_0_95659_x1109_546363348}

**WLAN接入 \-- WLAN接入配置命令 \-- service-template enable**

------------------------------------------------------------------------

[**[service-template enable]{lang="EN-US"}**]{#struct_0_95659_x1109_x270032553}[命令用来打开无线服务模板。]{style="font-family:宋体"}

[**[undo service-template enable]{lang="EN-US"}**]{#struct_0_95659_x1109_x1786910004}[命令用来关闭无线服务模板。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1814938819}

[**[service-template enable]{lang="EN-US"}**]{#struct_0_95659_x1109_x1666628996}

[**[undo service-template enable]{lang="EN-US"}**]{#struct_0_95659_x1109_x1796434963}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1706461457}

[[无线服务模板处于关闭状态]{style="font-family:宋体"}]{#struct_0_95659_x1109_401480553}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x304001910}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1119197928}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1703436641}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_1402735767}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_2146003606}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x2098281798}

[[若]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_95659_x1109_1737832980}[上所能创建的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[（基本服务集）已达上限，则不能打开其它处于关闭状态的无线服务模板。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1768357200}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_898073643}[打开无线服务模板开关。]{style="font-family:宋体"}

[[\<[Sysname]{style="color:black"}\> system-view]{lang="EN-US"}]{#struct_0_95659_x1109_x1666628995}

[\[[Sysname]{style="color:black"}\] wlan service-template service1]{lang="EN-US"}

[\[[Sysname]{style="color:black"}-wlan-st-service1\] service-template enable]{lang="EN-US"}
:::

::: {#76696090 .myid}
[]{#_Toc404794905}[]{#struct_0_95659_x1109_2095247806}[]{#_Toc351972628}

**WLAN接入 \-- WLAN接入配置命令 \-- ssid**

------------------------------------------------------------------------

[**[ssid]{lang="EN-US"}**]{#struct_0_95659_x1109_1527824517}[命令用来在无线服务模板视图下配置]{style="font-family:宋体"}[SSID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ssid]{lang="EN-US"}**]{#struct_0_95659_x1109_x864853908}[命令用来删除当前无线服务模板的]{style="font-family:宋体"}[SSID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_42827673}

[**[ssid ]{lang="EN-US"}***[ssid-name]{lang="EN-US"}*]{#struct_0_95659_x1109_x107625240}

[**[undo ssid]{lang="EN-US"}**]{#struct_0_95659_x1109_1213610159}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x673577762}

[[未配置]{style="font-family:宋体"}[SSID]{lang="EN-US"}]{#struct_0_95659_x1109_x650622612}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1754990997}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_911746032}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x592371125}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x1666628994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x633635549}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1231905839}

[*[ssid-name]{lang="EN-US" style="color:black"}*]{#struct_0_95659_x1109_738516219}[：]{style="font-family:
宋体;color:black"}[指定无线服务模板的]{style="font-family:宋体;color:black"}[SSID]{lang="EN-US" style="color:black"}[，为]{style="font-family:宋体;
color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[32]{lang="EN-US" style="color:black"}[个字符的字符串，区分大小写。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x524454752}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只能在无线服务模板处于关闭状态下配置。]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1118557635}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSID]{lang="EN-US" style="color:black"}]{#struct_0_95659_x1109_x389665040}[的名称应该尽量具有唯一性。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_310545463}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x271978923}[设置]{style="font-family:宋体"}[SSID]{lang="EN-US"}[为]{style="font-family:宋体"}[lynn]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_95659_x1109_617373194}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] ssid lynn]{lang="EN-US"}
:::

::: {#1579347695 .myid}
[]{#_Toc404794906}[]{#struct_0_95659_x1109_x2082651086}[]{#_Toc384278681}[]{#_Toc351972635}

**WLAN接入 \-- WLAN接入配置命令 \-- vlan**

------------------------------------------------------------------------

[**[vlan]{lang="EN-US"}**]{#struct_0_95659_x1109_1857476046}[命令用来在无线服务模板下配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vlan]{lang="EN-US"}**]{#struct_0_95659_x1109_x1216648985}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_222292855}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_95659_x1109_1228655337}

[**[undo vlan]{lang="EN-US"}**]{#struct_0_95659_x1109_x1515465270}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1254029824}

[[无线服务模板的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_95659_x1109_984241488}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_98471558}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_2022430513}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1007560676}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x118217918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x49789291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1670759054}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_95659_x1109_x1188115425}[：指定无线服务模板的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1329299308}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只能在无线服务模板处于关闭状态下配置。]{style="font-family:宋体"}]{#struct_0_95659_x1109_2111851925}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无线服务模板配置]{style="font-family:宋体"}]{#struct_0_95659_x1109_x984513789}[VLAN]{lang="EN-US"}[后，客户端在该服务模板上线后会被加入此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无线服务模板配置]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1470377928}[VLAN]{lang="EN-US"}[时，若指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[没有创建则配置失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1474853531}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x1629041967}[配置基于服务模板的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_95659_x1109_x640304430}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] vlan 2]{lang="EN-US"}
:::

::: {#-27160651 .myid}
[]{#_Toc351972627}[]{#_Toc404794907}[]{#struct_0_95659_x1109_x1549360676}

**WLAN接入 \-- WLAN接入配置命令 \-- wlan service-template**

------------------------------------------------------------------------

[**[wlan service-template]{lang="EN-US" style="color:black"}**]{#struct_0_95659_x1109_x1577669663}[命令用来创建无线服务模板。]{style="font-family:宋体;color:windowtext"}

[**[undo wlan service-template]{lang="EN-US" style="color:black"}**]{#struct_0_95659_x1109_157974031}[命令用来删除无线服务模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1666628993}

[**[wlan service-template ]{lang="EN-US" style="color:black"}**]{#struct_0_95659_x1109_x1036920076}*[service-template-name]{lang="EN-US" style="color:black"}*

[**[undo wlan service-template ]{lang="EN-US" style="color:black"}**]{#struct_0_95659_x1109_1390049301}*[service-template-name]{lang="EN-US" style="color:black"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1840135994}

[[未创建无线服务模板。]{style="font-family:宋体"}]{#struct_0_95659_x1109_600237535}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1106096948}

[[系统视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_2009162044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_463941070}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x488570725}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_24003785}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_973846689}

[*[service-template-name]{lang="EN-US"}*]{#struct_0_95659_x1109_1590053121}[：无线服务模板名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1266678493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建无线服务模板时，如果输入的无线服务模板已经存在，则直接进入该视图。]{style="font-family:宋体"}]{#struct_0_95659_x1109_x329535815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除无线服务模板时，如果指定的无线服务模板映射到射频，则在解除映射之前不能删除此无线服务模板。]{style="font-family:宋体"}]{#struct_0_95659_x1109_x1666628992}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_529163865}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x1076190310}[创建无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[。]{style="font-size:8.5pt;font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_95659_x1109_468746752}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}
:::

::: {#-2027243627 .myid}
[]{#_Toc404794908}[]{#struct_0_95659_x1109_331259709}[]{#_Toc393111393}[]{#_GoBack}

**WLAN接入 \-- WLAN接入配置命令 \-- client forwarding-location**

------------------------------------------------------------------------

[**[client forwarding-location]{lang="EN-US"}**]{#struct_0_95659_x1109_x914919012}[命令用来配置客户端数据报文的转发位置。]{style="font-family:
宋体"}

[**[undo client forwarding-location]{lang="EN-US"}**]{#struct_0_95659_x1109_x790756544}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1103368065}

[**[client forwarding-location ]{lang="EN-US"}**[{ **ac** \| **ap** \[ **vlan** { *vlan-start* \[ **to** *vlan-end* \] } \] \| **mac** }]{lang="EN-US"}]{#struct_0_95659_x1109_1897343650}

[**[undo client forwarding-location]{lang="EN-US"}**]{#struct_0_95659_x1109_350288636}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1204550865}

[[客户端数据报文转发位置在]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_95659_x1109_x1741267377}[上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_640424607}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_95659_x1109_872935260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1486173951}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_609419965}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_1127227735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1365655676}

[**[ac]{lang="EN-US"}**]{#struct_0_95659_x1109_x132825083}[：配置客户端数据报文的转发位置在]{style="font-family:宋体"}[AC]{lang="EN-US"}[上。]{style="font-family:宋体"}

[**[ap]{lang="EN-US"}**]{#struct_0_95659_x1109_x220816360}[：配置客户端数据报文的转发位置在]{style="font-family:宋体"}[AP]{lang="EN-US"}[上。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-start ]{lang="EN-US"}***[to ]{lang="EN-US"}***[vlan-end]{lang="EN-US"}*]{#struct_0_95659_x1109_x179038044}[：配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的客户端在]{style="font-family:宋体"}[AP]{lang="EN-US"}[上转发数据报文。若未配置本参数，表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的客户端数据报文的转发位置都在]{style="font-family:宋体"}[AP]{lang="EN-US"}[上。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_95659_x1109_1529175231}[：配置客户端数据报文的转发位置在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1654576624}

[[本命令只能在无线服务模板处于关闭状态时配置。]{style="font-family:宋体"}]{#struct_0_95659_x1109_1500801229}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1306433406}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x2069647669}[配置无线客户端的数据报文转发位置在]{style="font-family:宋体"}[AP]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_95659_x1109_x831539705}

[\[Sysname\] wlan service-template s1]{lang="EN-US"}

[\[Sysname-wlan-st-s1\] user-forward location ap]{lang="EN-US"}
:::

::: {#380372841 .myid}
[]{#_Toc404794909}[]{#struct_0_95659_x1109_959320753}[]{#_Toc402799591}

**WLAN接入 \-- WLAN接入配置命令 \-- broadcast-probe reply (仅AC)**

------------------------------------------------------------------------

[**[broadcast-probe reply]{lang="EN-US"}**]{#struct_0_95659_x1109_726067984}[命令用来使能]{style="font-family:宋体"}[AP]{lang="EN-US"}[回复广播]{style="font-family:宋体"}[Probe request]{lang="EN-US"}[报文功能**。**]{style="font-family:宋体"}

[**[undo broadcast-probe reply]{lang="EN-US"}**]{#struct_0_95659_x1109_x697169697}[命令用来禁止]{style="font-family:
宋体"}[AP]{lang="EN-US"}[回复广播]{style="font-family:宋体"}[Probe request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_252775461}

[**[broadcast-probe reply]{lang="EN-US"}**]{#struct_0_95659_x1109_1090016468}

[**[undo broadcast-probe reply]{lang="EN-US"}**]{#struct_0_95659_x1109_x586661399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x810698289}

[[AP]{lang="EN-US"}]{#struct_0_95659_x1109_1251047359}[回应广播]{style="font-family:宋体"}[Probe request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1243280599}

[[AP]{lang="EN-US"}]{#struct_0_95659_x1109_x1791867889}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x772745670}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_x1252958093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_677356716}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1269932611}

[[广播]{style="font-family:宋体"}[Probe request]{lang="EN-US"}]{#struct_0_95659_x1109_1767500889}[报文即报文中不携带服务的]{style="font-family:宋体"}[SSID]{lang="EN-US"}[，]{style="font-family:宋体"}[AP]{lang="EN-US"}[收到广播报文后，将]{style="font-family:宋体"}[AP]{lang="EN-US"}[提供的所有服务的信息封装在]{style="font-family:宋体"}[Probe response]{lang="EN-US"}[报文中，回应给客户端。]{style="font-family:宋体"}

[[配置不回应客户端的广播]{style="font-family:宋体"}[Probe request]{lang="EN-US"}]{#struct_0_95659_x1109_734544236}[报文，可以减少]{style="font-family:宋体"}[AP]{lang="EN-US"}[回应的]{style="font-family:宋体"}[Probe response]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1038303280}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x70809135}[在]{style="font-family:宋体"}[ap1]{lang="EN-US"}[下配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[不回应广播]{style="font-family:宋体"}[Probe request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_95659_x1109_620193045}

[\[Sysname\] wlan ap ap1 model wa2620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] undo broadcast-probe reply]{lang="EN-US"}
:::

::: {#-1978313198 .myid}
[]{#_Toc404794910}[]{#struct_0_95659_x1109_x665516273}[]{#_Toc384278672}[]{#_Toc351972633}

**WLAN接入 \-- WLAN接入配置命令 \-- client idle-timeout**

------------------------------------------------------------------------

[**[client idle-timeout]{lang="EN-US"}**]{#struct_0_95659_x1109_x927408949}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[和客户端之间连接允许的最大空闲时间。]{style="font-family:宋体"}

[**[undo client idle-timeout]{lang="EN-US"}**]{#struct_0_95659_x1109_592750132}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1056282586}

[**[client idle-timeout]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_95659_x1109_x1374405611}

[**[undo client idle-timeout]{lang="EN-US"}**]{#struct_0_95659_x1109_477017578}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_43613563}

[[AP]{lang="EN-US"}]{#struct_0_95659_x1109_510721807}[和客户端之间连接允许的最大空闲时间为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1183037433}

[[AP]{lang="EN-US"}]{#struct_0_95659_x1109_x1085024956}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_602306493}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_1944397817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_1736899827}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1045513297}

[*[interval]{lang="EN-US"}*]{#struct_0_95659_x1109_x2139173215}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[和客户端之间连接允许的最大空闲时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1829728443}

[[当客户端处于空闲状态，即客户端与]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_95659_x1109_x18632747}[无任何报文交互，当达到最大空闲时间时，]{style="font-family:宋体"}[AP]{lang="EN-US"}[会自动与客户端断开连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1330077087}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x1430231554}[设置]{style="font-family:宋体"}[AP]{lang="EN-US"}[和客户端之间连接允许的最大空闲时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_95659_x1109_x325669817}

[\[sysname\] wlan ap ap1 model WA2620-AGN]{lang="EN-US"}

[\[sysname-wlan-ap-ap1\] client idle-timeout 2000]{lang="EN-US"}
:::

::: {#-1567482213 .myid}
[]{#_Toc404794911}[]{#struct_0_95659_x1109_1699552012}[]{#_Toc384278673}

**WLAN接入 \-- WLAN接入配置命令 \-- client keep-alive**

------------------------------------------------------------------------

[**[client keep-alive]{lang="EN-US"}**]{#struct_0_95659_x1109_x381325614}[命令用来配置客户端保活时间。]{style="font-family:宋体"}

[**[undo client keep-alive]{lang="EN-US"}**]{#struct_0_95659_x1109_x1482126447}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95659_x1109_619936550}

[**[client keep-alive]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_95659_x1109_1774295126}

[**[undo client keep-alive]{lang="EN-US"}**]{#struct_0_95659_x1109_1755550487}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1626743925}

[[客户端保活功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_95659_x1109_x37777075}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x784485538}

[[AP]{lang="EN-US"}]{#struct_0_95659_x1109_1490979827}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1584710127}

[[network-admin]{lang="EN-US"}]{#struct_0_95659_x1109_988490341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95659_x1109_1078731209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x1805074421}

[*[interval]{lang="EN-US"}*]{#struct_0_95659_x1109_849801100}[：客户端保活时间，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_95659_x1109_1698823579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_95659_x1109_1973025242}[会定期给客户端发送空数据报文，以确认其是否在线。如果在保活时间内未收到客户端回应的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，则断开客户端与]{style="font-family:宋体"}[AP]{lang="EN-US"}[的连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[保活机制通常用来检测客户端是否在线。导致客户端异常离线原因有电源故障、系统崩溃等。]{style="font-family:宋体"}]{#struct_0_95659_x1109_467833564}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95659_x1109_x662209103}

[[\# ]{lang="EN-US"}]{#struct_0_95659_x1109_x1136463772}[设置客户端保活时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_95659_x1109_1322492061}

[\[Sysname\] wlan ap ap1 model WA2100]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] client keep-alive 20]{lang="EN-US"}
:::
