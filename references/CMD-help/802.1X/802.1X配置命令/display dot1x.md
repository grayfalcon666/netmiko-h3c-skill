::: {#-1217237132 .myid}
[]{#_Toc404792508}[]{#struct_0_16124_x1536_x1587706106}[]{#_Toc261334517}

**802.1X \-- 802.1X配置命令 \-- display dot1x**

------------------------------------------------------------------------

[**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x795759116}[命令用来显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的相关信息，包括会话连接信息、相关统计信息和配置信息等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1442771757}

[**[display dot1x]{lang="EN-US"}**[ \[ **sessions** \| **statistics** \] \[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type interface-number* \] ]{lang="EN-US"}]{#struct_0_16124_x1536_x659077740}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1613676899}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1026027041}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1537261385}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_426156217}

[[network-operator]{lang="EN-US"}]{#struct_0_16124_x1536_x1934481369}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1536622734}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16124_x1536_x1588689146}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_347973707}

[**[sessions]{lang="EN-US"}**]{#struct_0_16124_x1536_x1729268814}[：显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的会话连接信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_16124_x1536_300453931}[：显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的相关统计信息。]{style="font-family:宋体"}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_16124_x1536_x1645635749}[：显示指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_16124_x1536_2057754893}[：显示指定]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。不指定该参数，则表示显示指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_16124_x1536_731264321}[：显示指定端口的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1464896679}

[[如果不指定参数]{style="font-family:宋体"}**[sessions]{lang="EN-US"}**]{#struct_0_16124_x1536_x1585312149}[或者]{style="font-family:宋体"}**[statistics]{lang="EN-US"}**[，则显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的所有信息，包括会话连接信息、相关统计信息和配置信息等。]{style="font-family:宋体"}

[[如果不指定]{style="font-family:宋体"}**[ap]{lang="EN-US"}**]{#struct_0_16124_x1536_x1598581582}[和]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[参数，则显示所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户的信息，先显示有线的信息再显示无线的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1715653070}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1830463244}[显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的所有信息。]{style="font-family:宋体"}

[[\<Sysname\> display dot1x]{lang="EN-US"}]{#struct_0_16124_x1536_334149446}

[ Global 802.1X parameters:]{lang="EN-US"}

[   802.1X authentication  : Enabled]{lang="EN-US"}

[   CHAP authentication    : Enabled]{lang="EN-US"}

[   Max-tx period          : 30 s]{lang="EN-US"}

[   Handshake period       : 15 s]{lang="EN-US"}

[   Quiet timer            : Disabled]{lang="EN-US"}

[       Quiet period       : 60 s]{lang="EN-US"}

[   Supp timeout           : 30 s]{lang="EN-US"}

[   Server timeout         : 100 s]{lang="EN-US"}

[   Reauth period          : 3600 s]{lang="EN-US"}

[   Max auth requests      : 2]{lang="EN-US"}

[   SmartOn switch ID      : 30]{lang="EN-US"}

[   SmartOn supp timeout   : 30 s]{lang="EN-US"}

[   SmartOn retry counts   : 3]{lang="EN-US"}

[   EAD assistant function : Disabled]{lang="EN-US"}

[       URL                : http://www.dwsoft.com]{lang="EN-US"}

[       Free IP            : 6.6.6.0         255.255.255.0]{lang="EN-US"}

[       EAD timeout        : 30 min]{lang="EN-US"}

[   Domain delimiter       : @]{lang="EN-US"}

[ Max 802.1X users         : 1024 per slot]{lang="EN-US"}

[Online 802.1X wired users    : 1]{lang="EN-US"}

[Online 802.1X wireless users : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ GigabitEthernet1/0/1  is link-up]{lang="EN-US"}

[   802.1X authentication      : Enabled]{lang="EN-US"}

[   Handshake                  : Enabled]{lang="EN-US"}

[   Handshake security         : Disabled]{lang="EN-US"}

[   Unicast trigger            : Disabled]{lang="EN-US"}

[   Periodic reauth            : Disabled]{lang="EN-US"}

[   Port role                  : Authenticator]{lang="EN-US"}

[   Authorization mode         : Auto]{lang="EN-US"}

[   Port access control        : Port-based]{lang="EN-US"}

[   Multicast trigger          : Enabled]{lang="EN-US"}

[   Mandatory auth domain      : Not configured]{lang="EN-US"}

[   Guest VLAN                 : 3]{lang="EN-US"}

[   Auth-Fail VLAN             : Not configured]{lang="EN-US"}

[   Critical VLAN              : Not configured]{lang="EN-US"}

[   Re-auth server-unreachable : Logoff]{lang="EN-US"}

[   Max online users           : 256]{lang="EN-US"}

[   SmartOn                    : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[   EAPOL packets: Tx 3, Rx 3]{lang="EN-US"}

[   Sent EAP Request/Identity packets : 1]{lang="EN-US"}

[        EAP Request/Challenge packets: 1]{lang="EN-US"}

[        EAP Success packets: 1]{lang="EN-US"}

[        EAP Failure packets: 0]{lang="EN-US"}

[   Received EAPOL Start packets : 1]{lang="EN-US"}

[            EAPOL LogOff packets: 1]{lang="EN-US"}

[            EAP Response/Identity packets : 1]{lang="EN-US"}

[            EAP Response/Challenge packets: 1]{lang="EN-US"}

[            Error packets: 0]{lang="EN-US"}

[   Online 802.1X users: 1]{lang="EN-US"}

[          MAC address         Auth state]{lang="EN-US"}

[          0001-0000-0000      Authenticated]{lang="EN-US"}

[AP name: AP1  Radio ID: 1  SSID: wlan_dot1x_ssid]{lang="EN-US"}

[   BSSID                      : 1111-1111-1111]{lang="EN-US"}

[   802.1X authentication      : Enabled]{lang="EN-US"}

[   Handshake                  : Enabled]{lang="EN-US"}

[   Handshake security         : Disabled]{lang="EN-US"}

[   Periodic reauth            : Disabled]{lang="EN-US"}

[   Mandatory auth domain      : Not configured]{lang="EN-US"}

[   Max online users           : 256]{lang="EN-US"}

[ ]{lang="EN-US"}

[   EAPOL packets: Tx 3, Rx 3]{lang="EN-US"}

[   Sent EAP Request/Identity packets : 1]{lang="EN-US"}

[        EAP Request/Challenge packets: 1]{lang="EN-US"}

[        EAP Success packets: 1]{lang="EN-US"}

[        EAP Failure packets: 0]{lang="EN-US"}

[   Received EAPOL Start packets : 1]{lang="EN-US"}

[        EAPOL LogOff packets: 1]{lang="EN-US"}

[        EAP Response/Identity packets : 1]{lang="EN-US"}

[        EAP Response/Challenge packets: 1]{lang="EN-US"}

[        Error packets: 0]{lang="EN-US"}

[   Online 802.1X users: 1]{lang="EN-US"}

[          MAC address         Auth state]{lang="EN-US"}

[          0001-0000-0002      Authenticated]{lang="EN-US"}

[]{#struct_0_16124_x1536_503474542}[]{#_Toc138064418}[]{#_Toc138064378}[]{#_Toc79398232}[[表1-1 ]{lang="EN-US"}[display dot1x]{lang="EN-US"}]{#_Toc38965297}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1539646534}[[字段]{style="font-family:黑体"}]{#struct_0_16124_x1536_1005108665}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2017408859}

[[Global 802.1X parameters]{lang="EN-US"}]{#struct_0_16124_x1536_x1402030296}

[[全局]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_349410754}[参数配置信息]{style="font-family:宋体"}

[[802.1X authentication]{lang="EN-US"}]{#struct_0_16124_x1536_x1522020613}

[[全局]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1627582003}[的开启状态]{style="font-family:宋体"}

[[CHAP authentication]{lang="EN-US"}]{#struct_0_16124_x1536_x537988983}

[[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_1091536855}[终结方式，并采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证方法]{style="font-family:宋体"}

[[EAP authentication]{lang="EN-US"}]{#struct_0_16124_x1536_1028094958}

[[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_2097242487}[中继方式，并支持所有]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方法]{style="font-family:宋体"}

[[PAP authentication]{lang="EN-US"}]{#struct_0_16124_x1536_x1331469636}

[[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_x894284879}[终结方式，并采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[认证方法]{style="font-family:宋体"}

[[Max-tx period ]{lang="EN-US"}]{#struct_0_16124_x1536_x52706429}

[[用户名请求超时定时器的值]{style="font-family:宋体"}]{#struct_0_16124_x1536_1861168640}

[[Handshake period]{lang="EN-US"}]{#struct_0_16124_x1536_x1401964760}

[[握手定时器的值]{style="font-family:宋体"}]{#struct_0_16124_x1536_x475296875}

[[Quiet timer]{lang="EN-US"}]{#struct_0_16124_x1536_x1402554583}

[[静默定时器的开启状态]{style="font-family:宋体"}]{#struct_0_16124_x1536_x769043060}

[[Quiet period]{lang="EN-US"}]{#struct_0_16124_x1536_1301741815}

[[静默定时器的值]{style="font-family:宋体"}]{#struct_0_16124_x1536_334346054}

[[Supp timeout]{lang="EN-US"}]{#struct_0_16124_x1536_1154289540}

[[客户端认证超时定时器的值]{style="font-family:宋体"}]{#struct_0_16124_x1536_1233016212}

[[Server  timeout]{lang="EN-US"}]{#struct_0_16124_x1536_334411590}

[[认证服务器超时定时器的值]{style="font-family:宋体"}]{#struct_0_16124_x1536_280223076}

[[Reauth period]{lang="EN-US"}]{#struct_0_16124_x1536_1756254292}

[[重认证定时器的值]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1597091105}

[[Max auth requests]{lang="EN-US"}]{#struct_0_16124_x1536_x2119887071}

[[设备向接入用户发送认证请求报文的最大次数]{style="font-family:宋体"}]{#struct_0_16124_x1536_1853840390}

[[SmartOn switch ID]{lang="EN-US"}]{#struct_0_16124_x1536_x1402489047}

[[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x1402685655}[的]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}

[[SmartOn supp timeout]{lang="EN-US"}]{#struct_0_16124_x1536_1305285408}

[[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_1929014067}[的客户端认证超时定时器的时长]{style="font-family:宋体"}

[[SmartOn retry counts]{lang="EN-US"}]{#struct_0_16124_x1536_x679911046}

[[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x1402620119}[的通知请求报文的最大发送次数]{style="font-family:宋体"}

[[EAD assistant function]{lang="EN-US"}]{#struct_0_16124_x1536_365812643}

[[EAD]{lang="EN-US"}]{#struct_0_16124_x1536_1210147018}[快速部署辅助功能的开启状态]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_16124_x1536_x958432862}

[[用户]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_16124_x1536_x2041247399}[访问的重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}

[[Free IP]{lang="EN-US"}]{#struct_0_16124_x1536_x1402292439}

[[用户通过认证之前可访问的网段]{style="font-family:宋体"}]{#struct_0_16124_x1536_1677307903}

[[EAD timeout]{lang="EN-US"}]{#struct_0_16124_x1536_1020951600}

[[EAD]{lang="EN-US"}]{#struct_0_16124_x1536_743417684}[老化定时器超时时间]{style="font-family:宋体"}

[[Domain delimiter]{lang="EN-US"}]{#struct_0_16124_x1536_x1402226903}

[[域名分隔符]{style="font-family:宋体"}]{#struct_0_16124_x1536_x341291635}

[[Max 802.1X users]{lang="EN-US"}]{#struct_0_16124_x1536_x986438640}

[[每个单板最大支持的接入用户数]{style="font-family:宋体"}]{#struct_0_16124_x1536_334477126}

[[Online 802.1X wired users]{lang="EN-US"}]{#struct_0_16124_x1536_949685238}

[[在线]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1101499903}[有线用户数]{style="font-family:宋体"}

[[Online 802.1X wireless users]{lang="EN-US"}]{#struct_0_16124_x1536_1418506260}

[[在线]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1640043086}[无线用户数]{style="font-family:宋体"}

[[GigabitEthernet1/0/1 is link-up]{lang="EN-US"}]{#struct_0_16124_x1536_x1692455397}

[[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_16124_x1536_x153832044}[的链路状态]{style="font-family:宋体"}

[[802.1X authentication]{lang="EN-US"}]{#struct_0_16124_x1536_334542662}

[[端口上]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1803059252}[的开启状态]{style="font-family:宋体"}

[[Handshake]{lang="EN-US"}]{#struct_0_16124_x1536_x592560800}

[[在线用户握手功能的开启状态]{style="font-family:宋体"}]{#struct_0_16124_x1536_1568876037}

[[Handshake security]{lang="EN-US"}]{#struct_0_16124_x1536_x1402357975}

[[安全握手功能的开启状态]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1785435054}

[[Unicast trigger ]{lang="EN-US"}]{#struct_0_16124_x1536_334608198}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1436504073}[单播触发功能的开启状态]{style="font-family:宋体"}

[[Periodic reauth]{lang="EN-US"}]{#struct_0_16124_x1536_692793564}

[[周期性重认证功能的开启状态]{style="font-family:宋体"}]{#struct_0_16124_x1536_306821429}

[[Port role]{lang="EN-US"}]{#struct_0_16124_x1536_333625158}

[[该端口担当认证端的作用，目前仅支持作为认证端]{style="font-family:宋体"}]{#struct_0_16124_x1536_1304795076}

[[Authorization mode]{lang="EN-US"}]{#struct_0_16124_x1536_375155351}

[[端口的授权状态]{style="font-family:宋体"}]{#struct_0_16124_x1536_1920843553}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Force-Authorized]{lang="EN-US"}]{#struct_0_16124_x1536_333690694}[：强制授权状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_16124_x1536_570368576}[：自动识别状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Force-Unauthorized]{lang="EN-US"}]{#struct_0_16124_x1536_x1314301260}[：强制非授权状态]{style="font-family:宋体"}

[[Port access control]{lang="EN-US"}]{#struct_0_16124_x1536_x792283674}

[[端口接入控制方式]{style="font-family:宋体"}]{#struct_0_16124_x1536_334149447}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC-based]{lang="EN-US"}]{#struct_0_16124_x1536_503474541}[：基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接入用户进行认证（该方式的生效情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port-based]{lang="EN-US"}]{#struct_0_16124_x1536_1005108664}[：基于端口对接入用户进行认证]{style="font-family:宋体"}

[[Multicast trigger]{lang="EN-US"}]{#struct_0_16124_x1536_334214983}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_366433451}[组播触发功能的开启状态]{style="font-family:宋体"}

[[Mandatory auth domain]{lang="EN-US"}]{#struct_0_16124_x1536_x147776173}

[[端口上的接入用户使用的强制认证域]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1275505202}

[[Guest VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x1402685654}

[[端口配置的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x260798533}

[[Auth-fail VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x336823150}

[[端口配置的]{style="font-family:宋体"}[Auth-Fail VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x1402620118}

[[Critical VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x1200271298}

[[端口配置的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_2109435908}

[[Re-auth server-unreachable]{lang="EN-US"}]{#struct_0_16124_x1536_x1402292438}

[[重认证时服务器不可达对]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1051575452}[在线用户采取的动作]{style="font-family:宋体"}

[[Max online users]{lang="EN-US"}]{#struct_0_16124_x1536_334280519}

[[本端口最多可容纳的接入用户数]{style="font-family:宋体"}]{#struct_0_16124_x1536_1543953426}

[[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x1402226902}

[[端口上]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x1907375576}[的开启状态]{style="font-family:宋体"}

[[EAPOL packets]{lang="EN-US"}]{#struct_0_16124_x1536_1779879445}

[[EAPOL]{lang="EN-US"}]{#struct_0_16124_x1536_334346055}[报文数目。]{style="font-family:宋体"}[Tx]{lang="EN-US"}[表示发送的报文数目；]{style="font-family:宋体"}[Rx]{lang="EN-US"}[表示接受的报文数目]{style="font-family:宋体"}

[[Sent EAP Request/Identity packets]{lang="EN-US"}]{#struct_0_16124_x1536_x1983628325}

[[发送的]{style="font-family:宋体"}[EAP Request/Identity]{lang="EN-US"}]{#struct_0_16124_x1536_977385393}[报文数]{style="font-family:宋体"}

[[EAP Request/Challenge packets]{lang="EN-US"}]{#struct_0_16124_x1536_334411591}

[[发送的]{style="font-family:宋体"}[EAP Request/Challenge]{lang="EN-US"}]{#struct_0_16124_x1536_280223077}[报文数]{style="font-family:宋体"}

[[EAP Success packets]{lang="EN-US"}]{#struct_0_16124_x1536_x2119887070}

[[发送的]{style="font-family:宋体"}[EAP Success]{lang="EN-US"}]{#struct_0_16124_x1536_x875042965}[报文数]{style="font-family:宋体"}

[[EAP Fail packets]{lang="EN-US"}]{#struct_0_16124_x1536_334477127}

[[发送的]{style="font-family:宋体"}[EAP Failure]{lang="EN-US"}]{#struct_0_16124_x1536_1418506261}[报文数]{style="font-family:宋体"}

[[Received EAPOL Start packets]{lang="EN-US"}]{#struct_0_16124_x1536_x1640108622}

[[接收的]{style="font-family:宋体"}[EAPOL Start]{lang="EN-US"}]{#struct_0_16124_x1536_334542663}[报文数]{style="font-family:宋体"}

[[EAPOL LogOff packets]{lang="EN-US"}]{#struct_0_16124_x1536_1803059251}

[[接收的]{style="font-family:宋体"}[EAPOL LogOff]{lang="EN-US"}]{#struct_0_16124_x1536_x592626336}[报文数]{style="font-family:宋体"}

[[EAP Response/Identity packets]{lang="EN-US"}]{#struct_0_16124_x1536_334608199}

[[接收的]{style="font-family:宋体"}[EAP Response/Identity]{lang="EN-US"}]{#struct_0_16124_x1536_x1436504074}[报文数]{style="font-family:宋体"}

[[EAP Response/Challenge packets]{lang="EN-US"}]{#struct_0_16124_x1536_289509037}

[[接收的]{style="font-family:宋体"}[EAP Response/Challenge]{lang="EN-US"}]{#struct_0_16124_x1536_333625159}[报文数]{style="font-family:宋体"}

[[Error packets]{lang="EN-US"}]{#struct_0_16124_x1536_1304795075}

[[接收的错误报文数]{style="font-family:宋体"}]{#struct_0_16124_x1536_333690695}

[[Online 802.1X users]{lang="EN-US"}]{#struct_0_16124_x1536_334149444}

[[端口上的在线]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_503474544}[用户数]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_16124_x1536_x1402292445}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x648749677}[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Auth state]{lang="EN-US"}]{#struct_0_16124_x1536_x1402226909}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1177738139}[用户的认证状态]{style="font-family:宋体"}

[[AP name]{lang="EN-US"}]{#struct_0_16124_x1536_996739405}

[[AP]{lang="EN-US"}]{#struct_0_16124_x1536_x1375979126}[名称]{style="font-family:宋体"}

[[Radio ID]{lang="EN-US"}]{#struct_0_16124_x1536_1369210254}

[[Radio]{lang="EN-US"}]{#struct_0_16124_x1536_816206865}[编号]{style="font-family:宋体"}

[[SSID]{lang="EN-US"}]{#struct_0_16124_x1536_1352904229}

[[服务集标识符]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1834593924}

[[BSSID]{lang="EN-US"}]{#struct_0_16124_x1536_1756188756}

[[基本服务集标识符]{style="font-family:宋体"}]{#struct_0_16124_x1536_x76690996}

[ ]{lang="EN-US"}

::: {#-1015503235 .myid}
[]{#_Toc404792509}[]{#struct_0_16124_x1536_x1402423517}[]{#_Toc351708663}[]{#_Toc350159596}

**802.1X \-- 802.1X配置命令 \-- display dot1x connection**

------------------------------------------------------------------------

[**[display dot1x connection]{lang="EN-US"}**]{#struct_0_16124_x1536_945716005}[命令用来显示当前]{style="font-family:
宋体"}[802.1X]{lang="EN-US"}[在线用户的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1496924927}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1628952080}

[**[display dot1x connection ]{lang="EN-US"}**[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type* *interface-number* \| **user-mac** *mac-addr* \| **user-name** *name-string* \]]{lang="EN-US"}]{#struct_0_16124_x1536_x1886353792}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16124_x1536_x1402357981}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display dot1x connection ]{lang="EN-US"}**[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type* *interface-number* \| **slot** *slot-number* \| **user-mac** *mac-addr* \| **user-name** *name-string* \]]{lang="EN-US"}]{#struct_0_16124_x1536_539573950}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_16124_x1536_x388944163}[模式[:]{lang="EN-US"}]{style="font-family:宋体"}

[**[display dot1x connection ]{lang="EN-US"}**[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **chassis** *chassis-number* **slot** *slot-number* \| **interface** *interface-type* *interface-number*  \| **user-mac** *mac-addr* \| **user-name** *name-string* \]]{lang="EN-US"}]{#struct_0_16124_x1536_x859170891}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1402030301}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x409645382}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_166213811}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_432910035}

[[network-operator]{lang="EN-US"}]{#struct_0_16124_x1536_x954327433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1401964765}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16124_x1536_x878581402}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1667985979}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_16124_x1536_1625524313}[：显示接入指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户的信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_16124_x1536_80765135}[：显示接入指定]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户的信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。不指定该参数，则表示显示接入]{style="font-family:宋体"}[AP]{lang="EN-US"}[下所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_16124_x1536_134617367}[：显示指定端口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。（集中式设备）]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_16124_x1536_x1402554588}[：显示指定单板上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_16124_x1536_x1978896641}[：显示指定成员设备上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持[IRF3]{lang="EN-US"}的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_16124_x1536_949619702}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16124_x1536_x717577989}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持[IRF3]{lang="EN-US"}的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16124_x1536_x2048726225}[：显示指定单板的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[user-mac]{lang="EN-US"}**[ *mac-addr*]{lang="EN-US"}]{#struct_0_16124_x1536_1625524314}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息。其中]{style="font-family:宋体"}*[mac-addr]{lang="EN-US"}*[表示用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-name ]{lang="EN-US"}***[name-string]{lang="EN-US"}*]{#struct_0_16124_x1536_x685357280}[：显示指定用户名]{style="font-family:宋体"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户信息]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}*[name-string]{lang="EN-US"}*[表示]{style="font-family:宋体"}[用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体;color:black"}[253]{lang="EN-US" style="color:black"}[个字符的字符串，区分大小写]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x892887413}

[[若不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_16124_x1536_1762302787}[端口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。]{style="font-family:宋体"}[（集中式设备）]{style="font-family:宋体"}

[[若不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_16124_x1536_1356414236}[单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[若不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1402685660}[成员设备上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[若不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_16124_x1536_1708635471}[成员设备上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_202074793}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1535816358}[显示所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。（]{style="font-family:宋体"}[集中式设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display dot1x connection]{lang="EN-US"}]{#struct_0_16124_x1536_x1402620124}

[User MAC address: 0015-e9a6-7cfe]{lang="EN-US"}

[Access interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Username: ias]{lang="EN-US"}

[Authentication domain: h3c]{lang="EN-US"}

[IPv4 address: 192.168.1.1]{lang="EN-US"}

[IPv6 address: 2000:0:0:0:1:2345:6789:abcd]{lang="EN-US"}

[Authentication method: CHAP]{lang="EN-US"}

[Initial VLAN: 1]{lang="EN-US"}

[Authorization untagged VLAN: N/A]{lang="EN-US"}

[Authorization tagged VLAN list: 1 to 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 29 31 33]{lang="EN-US"}

[                                35 37 40 to 100]{lang="EN-US"}

[Authorization ACL ID: 3001]{lang="EN-US"}

[Authorization user profile: N/A]{lang="EN-US"}

[Termination action: ]{lang="EN-US"}[Default]{lang="EN-US"}

[Session timeout period: 2 s]{lang="EN-US"}

[Online from: 2013/03/02  13:14:15]{lang="EN-US"}

[Online duration: 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[User MAC address                : 0015-e9a6-7cfe]{lang="EN-US"}

[AP name                         : ap1]{lang="EN-US"}

[Radio ID                        : 1]{lang="EN-US"}

[SSID                            : wlan_dot1x_ssid]{lang="EN-US"}

[BSSID                           : 0015-e9a6-7cf0]{lang="EN-US"}

[User name                       : ias]{lang="EN-US"}

[Authentication domain           : 1]{lang="EN-US"}

[IPv4 address                    : 192.168.1.1]{lang="EN-US"}

[IPv6 address                    : 2000:0:0:0:1:2345:6789:abcd]{lang="EN-US"}

[Authentication method           : CHAP]{lang="EN-US"}

[Initial VLAN                    : 1]{lang="EN-US"}

[Authorization VLAN              : N/A]{lang="EN-US"}

[Authorization ACL number        : 3001]{lang="EN-US"}

[Authorization user profile      : N/A]{lang="EN-US"}

[Termination action              : Default]{lang="EN-US"}

[Session timeout period          : 2 sec]{lang="EN-US"}

[Online from                     : 2013/03/02 13:14:15]{lang="EN-US"}

[Online duration                 : 0 h 2 m 15 s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 1 connections matched.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_412932346}[显示所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display dot1x connection]{lang="EN-US"}]{#struct_0_16124_x1536_x18908023}

[Slot ID: 0]{lang="EN-US"}

[User MAC address: 0015-e9a6-7cfe]{lang="EN-US"}

[Access interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Username: ias]{lang="EN-US"}

[Authentication domain: h3c]{lang="EN-US"}

[IPv4 address: 192.168.1.1]{lang="EN-US"}

[IPv6 address: 2000:0:0:0:1:2345:6789:abcd]{lang="EN-US"}

[Authentication method: CHAP]{lang="EN-US"}

[Initial VLAN: 1]{lang="EN-US"}

[Authorization untagged VLAN: N/A]{lang="EN-US"}

[Authorization tagged VLAN list: 1 to 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 29 31 33]{lang="EN-US"}

[                                35 37 40 to 100]{lang="EN-US"}

[Authorization ACL ID: 3001]{lang="EN-US"}

[Authorization user profile: N/A]{lang="EN-US"}

[Termination action: ]{lang="EN-US"}[Default]{lang="EN-US"}

[Session timeout period: 2 s]{lang="EN-US"}

[Online from: 2013/03/02  13:14:15]{lang="EN-US"}

[Online duration: 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[User MAC address                : 0015-e9a6-7cfe]{lang="EN-US"}

[AP name                         : ap1]{lang="EN-US"}

[Radio ID                        : 1]{lang="EN-US"}

[SSID                            : wlan_dot1x_ssid]{lang="EN-US"}

[BSSID                           : 0015-e9a6-7cf0]{lang="EN-US"}

[User name                       : ias]{lang="EN-US"}

[Authentication domain           : 1]{lang="EN-US"}

[IPv4 address                    : 192.168.1.1]{lang="EN-US"}

[IPv6 address                    : 2000:0:0:0:1:2345:6789:abcd]{lang="EN-US"}

[Authentication method           : CHAP]{lang="EN-US"}

[Initial VLAN                    : 1]{lang="EN-US"}

[Authorization VLAN              : N/A]{lang="EN-US"}

[Authorization ACL number        : 3001]{lang="EN-US"}

[Authorization user profile      : N/A]{lang="EN-US"}

[Termination action              : Default]{lang="EN-US"}

[Session timeout period          : 2 sec]{lang="EN-US"}

[Online from                     : 2013/03/02 13:14:15]{lang="EN-US"}

[Online duration                 : 0 h 2 m 15 s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 1 connections matched.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x1402292444}[显示所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display dot1x connection]{lang="EN-US"}]{#struct_0_16124_x1536_917334264}

[Chassis ID: 1]{lang="EN-US"}

[Slot ID: 0]{lang="EN-US"}

[User MAC address: 0015-e9a6-7cfe]{lang="EN-US"}

[Access interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Username: ias]{lang="EN-US"}

[Authentication domain: h3c]{lang="EN-US"}

[IPv4 address: 192.168.1.1]{lang="EN-US"}

[IPv6 address: 2000:0:0:0:1:2345:6789:abcd]{lang="EN-US"}

[Authentication method: CHAP]{lang="EN-US"}

[Initial VLAN: 1]{lang="EN-US"}

[Authorization untagged VLAN: N/A]{lang="EN-US"}

[Authorization tagged VLAN list: 1 to 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 29 31 33]{lang="EN-US"}

[                                35 37 40 to 100]{lang="EN-US"}

[Authorization ACL ID: 3001]{lang="EN-US"}

[Authorization user profile: N/A]{lang="EN-US"}

[Termination action: ]{lang="EN-US"}[Default]{lang="EN-US"}

[Session timeout period: 2 s]{lang="EN-US"}

[Online from: 2013/03/02  13:14:15]{lang="EN-US"}

[Online duration: 0h 2m 15s]{lang="EN-US"}

[ ]{lang="EN-US"}

[User MAC address                : 0015-e9a6-7cfe]{lang="EN-US"}

[AP name                         : ap1]{lang="EN-US"}

[Radio ID                        : 1]{lang="EN-US"}

[SSID                            : wlan_dot1x_ssid]{lang="EN-US"}

[BSSID                           : 0015-e9a6-7cf0]{lang="EN-US"}

[User name                       : ias]{lang="EN-US"}

[Authentication domain           : 1]{lang="EN-US"}

[IPv4 address                    : 192.168.1.1]{lang="EN-US"}

[IPv6 address                    : 2000:0:0:0:1:2345:6789:abcd]{lang="EN-US"}

[Authentication method           : CHAP]{lang="EN-US"}

[Initial VLAN                    : 1]{lang="EN-US"}

[Authorization VLAN              : N/A]{lang="EN-US"}

[Authorization ACL number        : 3001]{lang="EN-US"}

[Authorization user profile      : N/A]{lang="EN-US"}

[Termination action              : Default]{lang="EN-US"}

[Session timeout period          : 2 sec]{lang="EN-US"}

[Online from                     : 2013/03/02 13:14:15]{lang="EN-US"}

[Online duration                 : 0 h 2 m 15 s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 1 connections matched.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display dot1x connection ]{lang="EN-US"}]{#struct_0_16124_x1536_x2008073116}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x455131487}[[字段]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1402226908}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16124_x1536_x388345802}

[[Chassis ID]{lang="EN-US"}]{#struct_0_16124_x1536_x1402423516}

[[当前设备对应的框号]{style="font-family:宋体"}]{#struct_0_16124_x1536_x620367936}

[[Slot ID]{lang="EN-US"}]{#struct_0_16124_x1536_1132498040}

[[当前设备对应的板号]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16124_x1536_x1402357980}

[[User MAC address]{lang="EN-US"}]{#struct_0_16124_x1536_2105657891}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16124_x1536_x1402030300}[地址]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_16124_x1536_1156438559}

[[用户的接入接口名称]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1401964764}

[[AP name]{lang="EN-US"}]{#struct_0_16124_x1536_x330790817}

[[AP]{lang="EN-US"}]{#struct_0_16124_x1536_x330790816}[的名称]{style="font-family:宋体"}

[[Radio ID]{lang="EN-US"}]{#struct_0_16124_x1536_x1427643721}

[[Radio]{lang="EN-US"}]{#struct_0_16124_x1536_x330790815}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[SSID]{lang="EN-US"}]{#struct_0_16124_x1536_x1427578185}

[[服务集标识符]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1902606248}

[[BSSID]{lang="EN-US"}]{#struct_0_16124_x1536_x1902606247}

[[用户所属的基本服务集标识符]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1902606246}

[[Username]{lang="EN-US"}]{#struct_0_16124_x1536_1850301953}

[[用户名]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1230458730}

[[Authentication domain]{lang="EN-US"}]{#struct_0_16124_x1536_972130026}

[[认证时使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_16124_x1536_x302558708}[域的名称]{style="font-family:宋体"}

[[IPv4 address]{lang="EN-US"}]{#struct_0_16124_x1536_972064490}

[[用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16124_x1536_1301118681}[地址]{style="font-family:宋体"}

[[若未获取到用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16124_x1536_x146487141}[地址，则不显示该字段]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_16124_x1536_972261098}

[[用户]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16124_x1536_x393981635}[地址]{style="font-family:宋体"}

[[若未获取到用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16124_x1536_972195562}[地址，则不显示该字段]{style="font-family:宋体"}

[[Authentication method]{lang="EN-US"}]{#struct_0_16124_x1536_x674761471}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_972392170}[系统的认证方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CHAP]{lang="EN-US"}]{#struct_0_16124_x1536_351127403}[：启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[终结方式，并采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_x914436401}[：启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[中继方式，并支持所有]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAP]{lang="EN-US"}]{#struct_0_16124_x1536_972326634}[：启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[终结方式，并采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[认证方法]{style="font-family:宋体"}

[[Initial VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x18913161}

[[初始的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_972523242}

[[Authorization untagged VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_1771649757}

[[授权的]{style="font-family:宋体"}[untagged VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x1461773490}

[[Authorization tagged VLAN list]{lang="EN-US"}]{#struct_0_16124_x1536_972457706}

[[授权的]{style="font-family:宋体"}[tagged VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_617602247}[列表]{style="font-family:宋体"}

[[Authorization ACL ID]{lang="EN-US"}]{#struct_0_16124_x1536_972654314}

[[授权的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_16124_x1536_1261154097}[的编号]{style="font-family:宋体"}

[[Authorization user profile]{lang="EN-US"}]{#struct_0_16124_x1536_972588778}

[[授权用户的]{style="font-family:宋体"}[User profile]{lang="EN-US"}]{#struct_0_16124_x1536_242408908}[名称]{style="font-family:宋体"}

[[Termination action]{lang="EN-US"}]{#struct_0_16124_x1536_x1807990582}

[[服务器下发的终止动作类型：]{style="font-family:宋体"}]{#struct_0_16124_x1536_972130027}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default]{lang="EN-US"}]{#struct_0_16124_x1536_x302558709}[：会话超时时长到达后，强制用户下线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Radius-Request]{lang="EN-US"}]{#struct_0_16124_x1536_972064491}[：会话超时时长到达后，要求]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户进行重认证]{lang="EN-US" style="font-family:宋体"}

[[用户采用本地认证时，该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_16124_x1536_1301118682}

[[Session timeout period]{lang="EN-US"}]{#struct_0_16124_x1536_972261099}

[[服务器下发的会话超时时长，该时间到达之后，用户所在的会话将会被删除，之后，对该用户所采取的动作，由]{style="font-family:宋体"}[Terminate action]{lang="EN-US"}]{#struct_0_16124_x1536_x393981634}[字段的取值决定]{style="font-family:宋体"}

[[用户采用本地认证时，该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_16124_x1536_x1402541716}

[[Online from]{lang="EN-US"}]{#struct_0_16124_x1536_1648407022}

[[用户的上线时间]{style="font-family:宋体"}]{#struct_0_16124_x1536_972195563}

[[Online duration]{lang="EN-US"}]{#struct_0_16124_x1536_x674761472}

[[用户的在线时长]{style="font-family:宋体"}]{#struct_0_16124_x1536_972392171}

[[Total *xxx* connections matched.]{lang="EN-US"}]{#struct_0_16124_x1536_351127402}

[[在线用户个数]{style="font-family:宋体"}]{#struct_0_16124_x1536_972326635}

[ ]{lang="EN-US"}

::: {#261536672 .myid}
[]{#_Toc404792510}[]{#struct_0_16124_x1536_1005108659}[]{#_Toc261334518}[]{#_Toc286656701}[]{#_Toc286753485}[]{#_Toc293327262}[]{#_Toc293330525}[]{#_Toc286656702}[]{#_Toc286753486}[]{#_Toc293327263}[]{#_Toc293330526}[]{#_Toc286656703}[]{#_Toc286753487}[]{#_Toc293327264}[]{#_Toc293330527}[]{#_Toc286656704}[]{#_Toc286753488}[]{#_Toc293327265}[]{#_Toc293330528}[]{#_Toc286656705}[]{#_Toc286753489}[]{#_Toc293327266}[]{#_Toc293330529}[]{#_Toc286656706}[]{#_Toc286753490}[]{#_Toc293327267}[]{#_Toc293330530}[]{#_Toc286656707}[]{#_Toc286753491}[]{#_Toc293327268}[]{#_Toc293330531}[]{#_Toc286656708}[]{#_Toc286753492}[]{#_Toc293327269}[]{#_Toc293330532}[]{#_Toc286656709}[]{#_Toc286753493}[]{#_Toc293327270}[]{#_Toc293330533}[]{#_Toc286656710}[]{#_Toc286753494}[]{#_Toc293327271}[]{#_Toc293330534}[]{#_Toc286656711}[]{#_Toc286753495}[]{#_Toc293327272}[]{#_Toc293330535}[]{#_Toc286656712}[]{#_Toc286753496}[]{#_Toc293327273}[]{#_Toc293330536}[]{#_Toc286656713}[]{#_Toc286753497}[]{#_Toc293327274}[]{#_Toc293330537}[]{#_Toc286656714}[]{#_Toc286753498}[]{#_Toc293327275}[]{#_Toc293330538}[]{#_Toc286656715}[]{#_Toc286753499}[]{#_Toc293327276}[]{#_Toc293330539}[]{#_Toc286656716}[]{#_Toc286753500}[]{#_Toc293327277}[]{#_Toc293330540}[]{#_Toc286656717}[]{#_Toc286753501}[]{#_Toc293327278}[]{#_Toc293330541}[]{#_Toc286656718}[]{#_Toc286753502}[]{#_Toc293327279}[]{#_Toc293330542}[]{#_Toc286656719}[]{#_Toc286753503}[]{#_Toc293327280}[]{#_Toc293330543}[]{#_Toc286656720}[]{#_Toc286753504}[]{#_Toc293327281}[]{#_Toc293330544}[]{#_Toc286656721}[]{#_Toc286753505}[]{#_Toc293327282}[]{#_Toc293330545}[]{#_Toc286656722}[]{#_Toc286753506}[]{#_Toc293327283}[]{#_Toc293330546}[]{#_Toc286656723}[]{#_Toc286753507}[]{#_Toc293327284}[]{#_Toc293330547}[]{#_Toc286656724}[]{#_Toc286753508}[]{#_Toc293327285}[]{#_Toc293330548}[]{#_Toc286656725}[]{#_Toc286753509}[]{#_Toc293327286}[]{#_Toc293330549}[]{#_Toc286656726}[]{#_Toc286753510}[]{#_Toc293327287}[]{#_Toc293330550}[]{#_Toc286656729}[]{#_Toc286753513}[]{#_Toc293327290}[]{#_Toc293330553}[]{#_Toc173241585}[]{#_Toc173722500}[]{#_Toc173241588}[]{#_Toc173722503}[]{#_Toc173241589}[]{#_Toc173722504}[]{#_Toc173241590}[]{#_Toc173722505}[]{#_Toc173241591}[]{#_Toc173722506}[]{#_Toc173241592}[]{#_Toc173722507}[]{#_Toc173241593}[]{#_Toc173722508}[]{#_Toc173241594}[]{#_Toc173722509}[]{#_Toc173241595}[]{#_Toc173722510}[]{#_Toc173241596}[]{#_Toc173722511}[]{#_Toc173241597}[]{#_Toc173722512}[]{#_Toc173241598}[]{#_Toc173722513}[]{#_Toc173241599}[]{#_Toc173722514}[]{#_Toc173241600}[]{#_Toc173722515}[]{#_Toc173241601}[]{#_Toc173722516}[]{#_Toc173241602}[]{#_Toc173722517}[]{#_Toc173241603}[]{#_Toc173722518}[]{#_Toc173241604}[]{#_Toc173722519}[]{#_Toc173241605}[]{#_Toc173722520}[]{#_Toc173241606}[]{#_Toc173722521}[]{#_Toc173241607}[]{#_Toc173722522}[]{#_Toc173241608}[]{#_Toc173722523}[]{#_Toc50808080}[]{#_Toc144631630}[]{#_Toc144716768}[]{#_Toc144631632}[]{#_Toc144716770}[]{#_Toc144631633}[]{#_Toc144716771}[]{#_Toc144631634}[]{#_Toc144716772}[]{#_Toc144631635}[]{#_Toc144716773}[]{#_Toc144631636}[]{#_Toc144716774}[]{#_Toc144631637}[]{#_Toc144716775}[]{#_Toc144631638}[]{#_Toc144716776}[]{#_Toc144631639}[]{#_Toc144716777}[]{#_Toc144631640}[]{#_Toc144716778}[]{#_Toc144631641}[]{#_Toc144716779}[]{#_Toc144631642}[]{#_Toc144716780}[]{#_Toc144631643}[]{#_Toc144716781}[]{#_Toc50808083}[]{#_Toc50808085}[]{#_Toc50808086}[]{#_Toc50808087}[]{#_Toc50808088}[]{#_Toc50808089}[]{#_Toc50808090}[]{#_Toc50808091}[]{#_Toc50808092}[]{#_Toc50808093}[]{#_Toc50808094}[]{#_Toc50808095}[]{#_Toc50808096}[]{#_Toc50808098}[]{#_Toc144631645}[]{#_Toc144716783}[]{#_Toc286656730}[]{#_Toc286753514}[]{#_Toc293327291}[]{#_Toc293330554}[]{#_Toc286656731}[]{#_Toc286753515}[]{#_Toc293327292}[]{#_Toc293330555}[]{#_Toc286656733}[]{#_Toc286753517}[]{#_Toc293327294}[]{#_Toc293330557}[]{#_Toc286656734}[]{#_Toc286753518}[]{#_Toc293327295}[]{#_Toc293330558}[]{#_Toc286656735}[]{#_Toc286753519}[]{#_Toc293327296}[]{#_Toc293330559}[]{#_Toc286656736}[]{#_Toc286753520}[]{#_Toc293327297}[]{#_Toc293330560}[]{#_Toc286656737}[]{#_Toc286753521}[]{#_Toc293327298}[]{#_Toc293330561}[]{#_Toc286656738}[]{#_Toc286753522}[]{#_Toc293327299}[]{#_Toc293330562}[]{#_Toc286656739}[]{#_Toc286753523}[]{#_Toc293327300}[]{#_Toc293330563}[]{#_Toc286656740}[]{#_Toc286753524}[]{#_Toc293327301}[]{#_Toc293330564}[]{#_Toc286656741}[]{#_Toc286753525}[]{#_Toc293327302}[]{#_Toc293330565}[]{#_Toc286656742}[]{#_Toc286753526}[]{#_Toc293327303}[]{#_Toc293330566}[]{#_Toc286656743}[]{#_Toc286753527}[]{#_Toc293327304}[]{#_Toc293330567}[]{#_Toc286656744}[]{#_Toc286753528}[]{#_Toc293327305}[]{#_Toc293330568}[]{#_Toc286656745}[]{#_Toc286753529}[]{#_Toc293327306}[]{#_Toc293330569}[]{#_Toc286656746}[]{#_Toc286753530}[]{#_Toc293327307}[]{#_Toc293330570}[]{#_Toc286656747}[]{#_Toc286753531}[]{#_Toc293327308}[]{#_Toc293330571}[]{#_Toc286656748}[]{#_Toc286753532}[]{#_Toc293327309}[]{#_Toc293330572}[]{#_Toc286656749}[]{#_Toc286753533}[]{#_Toc293327310}[]{#_Toc293330573}[]{#_Toc286656750}[]{#_Toc286753534}[]{#_Toc293327311}[]{#_Toc293330574}[]{#_Toc286656751}[]{#_Toc286753535}[]{#_Toc293327312}[]{#_Toc293330575}[]{#_Toc286656752}[]{#_Toc286753536}[]{#_Toc293327313}[]{#_Toc293330576}[]{#_Toc286656753}[]{#_Toc286753537}[]{#_Toc293327314}[]{#_Toc293330577}[]{#_Toc286656754}[]{#_Toc286753538}[]{#_Toc293327315}[]{#_Toc293330578}[]{#_Toc286656756}[]{#_Toc286753540}[]{#_Toc293327317}[]{#_Toc293330580}[]{#_Toc286656758}[]{#_Toc286753542}[]{#_Toc293327319}[]{#_Toc293330582}[]{#_Toc286656759}[]{#_Toc286753543}[]{#_Toc293327320}[]{#_Toc293330583}[]{#_Toc286656760}[]{#_Toc286753544}[]{#_Toc293327321}[]{#_Toc293330584}[]{#_Toc286656761}[]{#_Toc286753545}[]{#_Toc293327322}[]{#_Toc293330585}[]{#_Toc286656762}[]{#_Toc286753546}[]{#_Toc293327323}[]{#_Toc293330586}[]{#_Toc286656763}[]{#_Toc286753547}[]{#_Toc293327324}[]{#_Toc293330587}[]{#_Toc286656764}[]{#_Toc286753548}[]{#_Toc293327325}[]{#_Toc293330588}[]{#_Toc286656765}[]{#_Toc286753549}[]{#_Toc293327326}[]{#_Toc293330589}[]{#_Toc286656766}[]{#_Toc286753550}[]{#_Toc293327327}[]{#_Toc293330590}[]{#_Toc286656767}[]{#_Toc286753551}[]{#_Toc293327328}[]{#_Toc293330591}[]{#_Toc286656768}[]{#_Toc286753552}[]{#_Toc293327329}[]{#_Toc293330592}[]{#_Toc286656769}[]{#_Toc286753553}[]{#_Toc293327330}[]{#_Toc293330593}[]{#_Toc286656770}[]{#_Toc286753554}[]{#_Toc293327331}[]{#_Toc293330594}[]{#_Toc286656771}[]{#_Toc286753555}[]{#_Toc293327332}[]{#_Toc293330595}[]{#_Toc286656772}[]{#_Toc286753556}[]{#_Toc293327333}[]{#_Toc293330596}[]{#_Toc286656773}[]{#_Toc286753557}[]{#_Toc293327334}[]{#_Toc293330597}[]{#_Toc286656774}[]{#_Toc286753558}[]{#_Toc293327335}[]{#_Toc293330598}[]{#_Toc286656775}[]{#_Toc286753559}[]{#_Toc293327336}[]{#_Toc293330599}[]{#_Toc286656776}[]{#_Toc286753560}[]{#_Toc293327337}[]{#_Toc293330600}[]{#_Toc286656779}[]{#_Toc286753563}[]{#_Toc293327340}[]{#_Toc293330603}[]{#_Toc286656780}[]{#_Toc286753564}[]{#_Toc293327341}[]{#_Toc293330604}[]{#_Toc286656781}[]{#_Toc286753565}[]{#_Toc293327342}[]{#_Toc293330605}[]{#_Toc286656782}[]{#_Toc286753566}[]{#_Toc293327343}[]{#_Toc293330606}[]{#_Toc286656783}[]{#_Toc286753567}[]{#_Toc293327344}[]{#_Toc293330607}[]{#_Toc286656784}[]{#_Toc286753568}[]{#_Toc293327345}[]{#_Toc293330608}[]{#_Toc286656785}[]{#_Toc286753569}[]{#_Toc293327346}[]{#_Toc293330609}[]{#_Toc286656786}[]{#_Toc286753570}[]{#_Toc293327347}[]{#_Toc293330610}[]{#_Toc286656787}[]{#_Toc286753571}[]{#_Toc293327348}[]{#_Toc293330611}[]{#_Toc286656788}[]{#_Toc286753572}[]{#_Toc293327349}[]{#_Toc293330612}[]{#_Toc286656789}[]{#_Toc286753573}[]{#_Toc293327350}[]{#_Toc293330613}[]{#_Toc286656790}[]{#_Toc286753574}[]{#_Toc293327351}[]{#_Toc293330614}[]{#_Toc286656791}[]{#_Toc286753575}[]{#_Toc293327352}[]{#_Toc293330615}[]{#_Toc286656792}[]{#_Toc286753576}[]{#_Toc293327353}[]{#_Toc293330616}[]{#_Toc286656793}[]{#_Toc286753577}[]{#_Toc293327354}[]{#_Toc293330617}[]{#_Toc286656794}[]{#_Toc286753578}[]{#_Toc293327355}[]{#_Toc293330618}[]{#_Toc286656795}[]{#_Toc286753579}[]{#_Toc293327356}[]{#_Toc293330619}[]{#_Toc286656796}[]{#_Toc286753580}[]{#_Toc293327357}[]{#_Toc293330620}[]{#_Toc286656797}[]{#_Toc286753581}[]{#_Toc293327358}[]{#_Toc293330621}[]{#_Toc286656798}[]{#_Toc286753582}[]{#_Toc293327359}[]{#_Toc293330622}[]{#_Toc286656799}[]{#_Toc286753583}[]{#_Toc293327360}[]{#_Toc293330623}[]{#_Toc286656800}[]{#_Toc286753584}[]{#_Toc293327361}[]{#_Toc293330624}[]{#_Toc286656801}[]{#_Toc286753585}[]{#_Toc293327362}[]{#_Toc293330625}[]{#_Toc286656802}[]{#_Toc286753586}[]{#_Toc293327363}[]{#_Toc293330626}[]{#_Toc286656803}[]{#_Toc286753587}[]{#_Toc293327364}[]{#_Toc293330627}[]{#_Toc286656804}[]{#_Toc286753588}[]{#_Toc293327365}[]{#_Toc293330628}[]{#_Toc286656805}[]{#_Toc286753589}[]{#_Toc293327366}[]{#_Toc293330629}[]{#_Toc286656806}[]{#_Toc286753590}[]{#_Toc293327367}[]{#_Toc293330630}[]{#_Toc286656807}[]{#_Toc286753591}[]{#_Toc293327368}[]{#_Toc293330631}[]{#_Toc286656808}[]{#_Toc286753592}[]{#_Toc293327369}[]{#_Toc293330632}[]{#_Toc286656810}[]{#_Toc286753594}[]{#_Toc293327371}[]{#_Toc293330634}[]{#_Toc286656811}[]{#_Toc286753595}[]{#_Toc293327372}[]{#_Toc293330635}[]{#_Toc286656814}[]{#_Toc286753598}[]{#_Toc293327375}[]{#_Toc293330638}[]{#_Toc286656817}[]{#_Toc286753601}[]{#_Toc293327378}[]{#_Toc293330641}[]{#_Toc286656820}[]{#_Toc286753604}[]{#_Toc293327381}[]{#_Toc293330644}[]{#_Toc130093714}

**802.1X \-- 802.1X配置命令 \-- dot1x**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x2018195288}[命令用来开启指定端口上或全局的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1678534868}[命令用来关闭指定端口上或全局的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_446498509}

[**[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x403274626}

[**[undo dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_334214980}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_366433448}

[[所有端口以及全局的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1808538972}[都处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1282590746}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16124_x1536_x224037173}[以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x822703146}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1870946120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1932521344}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1025810393}

[[只有同时开启全局和端口的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_334280516}[后，]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的配置才能在端口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1543953429}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1778896405}[开启全局的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x885133408}

[\[Sysname\] dot1x]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1862127564}[开启端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] interface gabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_16124_x1536_x1431927828}

[\[Sysname-GigabitEthernet1/0/1\] dot1x]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1004187562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_316000164}
:::

::: {#-1210866735 .myid}
[]{#_Toc404792511}[]{#struct_0_16124_x1536_334346052}[]{#_Toc261334519}[]{#_Toc286656822}[]{#_Toc286753606}[]{#_Toc293327383}[]{#_Toc293330646}[]{#_Toc286656823}[]{#_Toc286753607}[]{#_Toc293327384}[]{#_Toc293330647}[]{#_Toc286656824}[]{#_Toc286753608}[]{#_Toc293327385}[]{#_Toc293330648}[]{#_Toc286656825}[]{#_Toc286753609}[]{#_Toc293327386}[]{#_Toc293330649}[]{#_Toc286656826}[]{#_Toc286753610}[]{#_Toc293327387}[]{#_Toc293330650}[]{#_Toc286656827}[]{#_Toc286753611}[]{#_Toc293327388}[]{#_Toc293330651}[]{#_Toc286656828}[]{#_Toc286753612}[]{#_Toc293327389}[]{#_Toc293330652}[]{#_Toc286656829}[]{#_Toc286753613}[]{#_Toc293327390}[]{#_Toc293330653}[]{#_Toc286656830}[]{#_Toc286753614}[]{#_Toc293327391}[]{#_Toc293330654}[]{#_Toc286656831}[]{#_Toc286753615}[]{#_Toc293327392}[]{#_Toc293330655}[]{#_Toc286656832}[]{#_Toc286753616}[]{#_Toc293327393}[]{#_Toc293330656}[]{#_Toc286656833}[]{#_Toc286753617}[]{#_Toc293327394}[]{#_Toc293330657}[]{#_Toc286656834}[]{#_Toc286753618}[]{#_Toc293327395}[]{#_Toc293330658}[]{#_Toc286656835}[]{#_Toc286753619}[]{#_Toc293327396}[]{#_Toc293330659}[]{#_Toc286656836}[]{#_Toc286753620}[]{#_Toc293327397}[]{#_Toc293330660}[]{#_Toc286656837}[]{#_Toc286753621}[]{#_Toc293327398}[]{#_Toc293330661}[]{#_Toc286656838}[]{#_Toc286753622}[]{#_Toc293327399}[]{#_Toc293330662}[]{#_Toc286656839}[]{#_Toc286753623}[]{#_Toc293327400}[]{#_Toc293330663}[]{#_Toc286656840}[]{#_Toc286753624}[]{#_Toc293327401}[]{#_Toc293330664}[]{#_Toc286656841}[]{#_Toc286753625}[]{#_Toc293327402}[]{#_Toc293330665}[]{#_Toc286656842}[]{#_Toc286753626}[]{#_Toc293327403}[]{#_Toc293330666}[]{#_Toc286656843}[]{#_Toc286753627}[]{#_Toc293327404}[]{#_Toc293330667}

**802.1X \-- 802.1X配置命令 \-- dot1x authentication-method**

------------------------------------------------------------------------

[**[dot1x authentication-method]{lang="EN-US"}**]{#struct_0_16124_x1536_x1983628330}[命令用来配置]{style="font-family:
宋体"}[802.1X]{lang="EN-US"}[系统的认证方法。]{style="font-family:宋体"}

[**[undo dot1x authentication-method]{lang="EN-US"}**]{#struct_0_16124_x1536_574166402}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_989159721}

[**[dot1x authentication-method ]{lang="EN-US"}**[{ **chap** *\|* **eap** *\|* **pap** }]{lang="EN-US"}]{#struct_0_16124_x1536_x863900978}

[**[undo dot1x authentication-method]{lang="EN-US"}**]{#struct_0_16124_x1536_582295972}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_678574918}

[[设备]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1582421856}[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[终结方式，并]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_876769180}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_334411588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2058429092}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1357966578}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x864262069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_789907922}

[**[chap]{lang="EN-US"}**]{#struct_0_16124_x1536_x1011800654}[：]{style="font-family:宋体"}[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[终结方式，并支持与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器之间采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[类型的认证方法]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[eap]{lang="EN-US"}**]{#struct_0_16124_x1536_1673841566}[：]{style="font-family:宋体"}[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[中继方式，并支持客户端与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器之间所有类型的]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方法。]{style="font-family:宋体"}

[**[pap]{lang="EN-US"}**]{#struct_0_16124_x1536_536264553}[：]{style="font-family:宋体"}[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[终结方式，并支持与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器之间采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[类型的认证方法]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_861833874}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_334477124}[终结]{style="font-family:宋体"}[：设备将收到的客户端]{style="font-family:宋体"}[EAP]{lang="EN-US"}[报文中的用户认证信息重新封装在标准的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文中，然后采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[或]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证方法与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器完成认证交互。该认证方式的优点是，现有的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器基本均可支持]{style="font-family:宋体"}[PAP]{lang="EN-US"}[和]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证，无需升级服务器，但设备处理较为复杂，且目前仅能支持]{style="font-family:宋体"}[MD5-Challenge]{lang="EN-US"}[类型的]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证以及]{style="font-family:宋体"}[iNode 802.1X]{lang="EN-US"}[客户端发起的"用户名]{style="font-family:宋体"}[+]{lang="EN-US"}[密码"方式的]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAP]{lang="EN-US"}]{#struct_0_16124_x1536_1418506262}[（]{lang="EN-US" style="font-family:
宋体"}[Password Authentication Protocol]{lang="EN-US"}[，密码验证协议）通过用户名和口令来对用户进行验证，其特点是在网络上以明文方式传送用户名和口令，仅适用于对网络安全要求相对较低的环境。目前，]{lang="EN-US" style="font-family:宋体"}[H3C iNode 802.1X]{lang="EN-US"}[客户端支持此认证方法。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CHAP]{lang="EN-US"}]{#struct_0_16124_x1536_x1640174158}[（]{lang="EN-US" style="font-family:宋体"}[Challenge Handshake Authentication Protocol]{lang="EN-US"}[，质询握手验证协议）采用客户端与服务器端交互挑战信息的方式来验证用户身份，其特点是在网络上以明文方式传送用户名，以密文方式传输口令。与]{lang="EN-US" style="font-family:宋体"}[PAP]{lang="EN-US"}[相比，]{lang="EN-US" style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证保密性较好，更为安全可靠。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_x1816446491}[中继]{style="font-family:宋体"}[：设备将收到的客户端]{style="font-family:宋体"}[EAP]{lang="EN-US"}[报文直接封装到]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的属性字段中，发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器完成认证。该认证方式的优点是，设备处理简单，且可支持多种类型的]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方法，例如]{style="font-family:宋体"}[MD5-Challenge]{lang="EN-US"}[、]{style="font-family:宋体"}[EAP-TLS]{lang="EN-US"}[、]{style="font-family:宋体"}[PEAP]{lang="EN-US"}[等，但要求服务器端支持相应的]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方法。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16124_x1536_x2072562318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用远程]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1418560089}[RADIUS]{lang="EN-US"}[认证时，]{style="font-family:宋体"}[PAP]{lang="EN-US"}[、]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证的最终实现，需要]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器支持相应的]{style="font-family:宋体"}[PAP]{lang="EN-US"}[、]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[、]{style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方法。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若采用]{lang="EN-US" style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_16124_x1536_587537627}[认证]{lang="EN-US" style="font-family:宋体"}[方法]{style="font-family:宋体"}[，则]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案下的]{lang="EN-US" style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[配置无效，]{lang="EN-US" style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[的介绍请参见"安全命令参考"中的"]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1294655439}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_334542660}[启用]{style="font-family:宋体"}[EAP]{lang="EN-US"}[终结方式，并支持与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器之间采用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[类型的认证方法]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1803059254}

[\[Sysname\] dot1x authentication-method pap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x592429728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1960250547}
:::

::: {#1446795453 .myid}
[]{#_Toc404792512}[]{#struct_0_16124_x1536_972457707}[]{#_Toc351708648}[]{#_Toc350159580}[]{#_Toc293327409}[]{#_Toc293330672}[]{#_Toc293327411}[]{#_Toc293330674}[]{#_Toc293327412}[]{#_Toc293330675}[]{#_Toc293327413}[]{#_Toc293330676}[]{#_Toc144716786}[]{#_Toc144716787}

**802.1X \-- 802.1X配置命令 \-- dot1x auth-fail vlan**

------------------------------------------------------------------------

[**[dot1x auth-fail vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_617602246}[命令用来配置指定端口的]{style="font-family:宋体"}[802.1X Auth-Fail VLAN]{lang="EN-US"}[，即认证失败的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户被授权访问的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dot1x auth-fail vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_972654315}[命令用来恢复缺省情况**。**]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1261154096}

[**[dot1x auth-fail vlan ]{lang="EN-US"}***[authfail-vlan-id]{lang="EN-US"}*]{#struct_0_16124_x1536_1563371026}

[**[undo dot1x auth-fail vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_1899743367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_138607233}

[[端口上未配置]{style="font-family:宋体"}[802.1X Auth-Fail VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_972588779}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_242408909}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1807990581}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1167183015}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_972130028}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x302558702}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1684510235}

[*[authfail-vlan-id]{lang="EN-US"}*]{#struct_0_16124_x1536_1731557071}[：端口上指定的]{style="font-family:宋体;
color:black"}[Auth-Fail VLAN ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4094]{lang="EN-US" style="color:black"}[（该取值范围与设备型号有关，请以设备的实际情况为准）。该]{style="font-family:宋体;
color:black"}[VLAN]{lang="EN-US" style="color:black"}[必须已经创建。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2034827238}

[[如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_1027844548}[被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为某个端口的]{style="font-family:宋体"}[802.1X Auth-Fail VLAN]{lang="EN-US"}[；同样，如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被指定为某个端口的]{style="font-family:宋体"}[802.1X Auth-Fail VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[禁止删除已被配置为]{style="font-family:宋体"}[Auth-Fail VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x382508944}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，若要删除该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，请先使用命令]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[dot1x auth-fail vlan]{lang="EN-US"}**[取消]{style="font-family:宋体"}[802.1X Auth-Fail VLAN]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1012512419}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_972064492}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Auth-Fail VLAN]{lang="EN-US" style="color:black"}[为]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1301118679}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x auth-fail vlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x145962842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1598302329}
:::

::: {#-136668435 .myid}
[]{#_Toc404792513}[]{#struct_0_16124_x1536_972261100}[]{#_Toc351708649}[]{#_Toc350159581}[]{#_Toc286656849}[]{#_Toc286753633}[]{#_Toc293327415}[]{#_Toc293330678}[]{#_Toc286656850}[]{#_Toc286753634}[]{#_Toc293327416}[]{#_Toc293330679}[]{#_Toc286656851}[]{#_Toc286753635}[]{#_Toc293327417}[]{#_Toc293330680}

**802.1X \-- 802.1X配置命令 \-- dot1x critical vlan**

------------------------------------------------------------------------

[**[dot1x critical vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_1525597664}[命令用来配置指定端口的]{style="font-family:宋体"}[802.1X Critical VLAN]{lang="EN-US"}[，即当]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户认证时对应的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域下所有认证服务器都不可达的情况下端口加入的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dot1x critical vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_x1607156065}[命令用来恢复缺省情况**。**]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x285356762}

[**[dot1x critical vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_16124_x1536_972195564}

[**[undo dot1x critical vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_x674761469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1932947960}

[[端口上未配置]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_567325111}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972392172}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_351127405}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x914436407}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x781337645}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1358668405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972326636}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_16124_x1536_x18913163}[：端口上指定的]{style="font-family:宋体;color:black"}[Critical VLAN ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:
宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4094]{lang="EN-US" style="color:black"}[（该取值范围与设备型号有关，请以设备的实际情况为准）。该]{style="font-family:宋体;color:black"}[VLAN]{lang="EN-US" style="color:black"}[必须已经创建。]{style="font-family:宋体;
color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2034958310}

[[如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x981357528}[被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为某个端口的]{style="font-family:宋体"}[802.1X Critical VLAN]{lang="EN-US"}[；同样，如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被指定为某个端口的]{style="font-family:宋体"}[802.1X Critical VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[禁止删除已被配置为]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x433216932}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，若要删除该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，请先使用命令]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[dot1x critical vlan]{lang="EN-US"}**[取消]{style="font-family:宋体"}[802.1X Critical VLAN]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2035005697}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x2111651444}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Critical VLAN]{lang="EN-US" style="color:black"}[为]{style="font-family:宋体"}[VLAN 100 ]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_972523244}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x critical vlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1771649763}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x1462035637}
:::

::: {#-917181386 .myid}
[]{#_Toc404792514}[]{#struct_0_16124_x1536_420779454}[]{#_Toc351708659}[]{#_Toc350159592}

**802.1X \-- 802.1X配置命令 \-- dot1x domain-delimiter**

------------------------------------------------------------------------

[**[dot1x domain-delimiter]{lang="EN-US"}**]{#struct_0_16124_x1536_972457708}[命令用来配置域名分隔符。]{style="font-family:宋体"}

[**[undo dot1x domain-delimiter]{lang="EN-US"}**]{#struct_0_16124_x1536_617602241}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1861222215}

[**[dot1x domain-delimiter]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_16124_x1536_1880302474}

[**[undo dot1x domain-delimiter]{lang="EN-US"}**]{#struct_0_16124_x1536_577015390}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972654316}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1261154099}[支持的域名分隔符为]{style="font-family:宋体"}[@]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1564354066}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_976168540}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972588780}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x95298092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1577054956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1772353673}

[*[string]{lang="EN-US"}*]{#struct_0_16124_x1536_972130029}[：多个域名分隔符组成的]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[16]{lang="EN-US" style="color:black"}[个字符的字符串，其中每个字符必须是]{style="font-family:宋体;color:black"}[@]{lang="EN-US" style="color:black"}[、]{style="font-family:宋体;color:black"}[/]{lang="EN-US" style="color:black"}[、]{style="font-family:宋体;color:black"}[\\]{lang="EN-US" style="color:black"}[和]{style="font-family:宋体;color:black"}[.]{lang="EN-US" style="color:black"}[四之一]{style="font-family:宋体;color:black"}[。若要指定]{style="font-family:宋体"}[域名分隔符]{style="font-family:宋体;color:black"}[\\]{lang="EN-US" style="color:black"}[，则必须在输入时使用转义操作符]{style="font-family:宋体;color:black"}[\\]{lang="EN-US" style="color:black"}[，即输入]{style="font-family:宋体;color:black"}[\\\\]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x302558703}

[[目前，]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1684444699}[支持的域名分隔符包括]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:
宋体"}[/]{lang="EN-US"}[和]{style="font-family:宋体"}[.]{lang="EN-US"}[，对应的用户名格式分别为]{style="font-family:宋体"}*[username]{lang="EN-US"}*[@*domain-name*]{lang="EN-US"}[，]{style="font-family:宋体"} *[domain-name]{lang="EN-US"}*[\\*username*]{lang="EN-US"}[、]{style="font-family:宋体"}*[username]{lang="EN-US"}*[/*domain-name*]{lang="EN-US"}[和]{style="font-family:宋体"}*[username]{lang="EN-US"}*[.*domain-name*]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[username]{lang="EN-US"}*[为纯用户名、]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为域名。如果用户名中包含有多个域名分隔符字符，则设备仅将最后一个出现的域名分隔符识别为实际使用的域名分隔符，例如，用户输入的用户名为]{style="font-family:宋体"}[121.123/22\\@abc]{lang="EN-US"}[，设备上指定]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[支持的域名分隔符为]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[，则识别出的纯用户名为]{style="font-family:宋体"}[\@abc]{lang="EN-US"}[，域名为]{style="font-family:宋体"}[123/22]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，系统默认支持分隔符]{style="font-family:宋体"}[@]{lang="EN-US"}]{#struct_0_16124_x1536_537151842}[，但如果通过本命令指定的域名分隔符中未包含分隔符]{style="font-family:宋体"}[@]{lang="EN-US"}[，则]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[仅会支持命令中指定的分隔符。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x783188082}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_972064493}[配置]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[支持的域名分隔符为]{style="font-family:宋体"}[@]{lang="EN-US"}[和]{style="font-family:宋体"}[/]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1301118680}

[\[Sysname\] dot1x domain-delimiter @/]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x146421605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x931494423}
:::

::: {#1556982701 .myid}
[]{#_Toc404792515}[]{#struct_0_16124_x1536_972261101}[]{#_Toc351708660}[]{#_Toc350159593}[]{#_Toc286656854}[]{#_Toc286753638}[]{#_Toc293327420}[]{#_Toc293330683}[]{#_Toc286656856}[]{#_Toc286753640}[]{#_Toc293327422}[]{#_Toc293330685}

**802.1X \-- 802.1X配置命令 \-- dot1x ead-assistant enable**

------------------------------------------------------------------------

[**[dot1x ead-assistant enable]{lang="EN-US"}**]{#struct_0_16124_x1536_1525597665}[命令用来开启]{style="font-family:
宋体"}[EAD]{lang="EN-US"}[快速部署辅助功能。]{style="font-family:宋体"}

[**[undo dot1x ead-assistant enable]{lang="EN-US"}**]{#struct_0_16124_x1536_x1607221601}[命令用来关闭]{style="font-family:宋体"}[EAD]{lang="EN-US"}[快速部署辅助功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1407162831}

[**[dot1x ead-assistant enable]{lang="EN-US"}**]{#struct_0_16124_x1536_972195565}

[**[undo dot1x ead-assistant enable]{lang="EN-US"}**]{#struct_0_16124_x1536_x674761470}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1932358137}

[[EAD]{lang="EN-US"}]{#struct_0_16124_x1536_x155792885}[快速部署辅助功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1411970690}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_972392173}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_351127404}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x914436408}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x780878893}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972326637}

[[开启]{style="font-family:宋体"}[EAD]{lang="EN-US"}]{#struct_0_16124_x1536_x18913162}[快速部署辅助功能后，设备允许未通过认证的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户访问一个特定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段，并可以将用户发起的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[访问请求重定向到该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段中的一个指定的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，实现用户自动下载并安装]{style="font-family:宋体"}[EAD]{lang="EN-US"}[客户端的目的。]{style="font-family:宋体"}

[[该命令与]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16124_x1536_2035005696}[地址认证和端口安全的全局使能命令均互斥，即开启]{style="font-family:宋体"}[EAD]{lang="EN-US"}[快速部署辅助功能时，若全局使能了]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证或端口安全，则该配置将会执行失败，反之亦然。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2111585908}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_972523245}[开启]{style="font-family:宋体"}[EAD]{lang="EN-US"}[快速部署辅助功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1771649764}

[\[Sysname\] dot1x ead-assistant enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1461970101}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x1857111466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x ead-assistant free-ip]{lang="EN-US"}**]{#struct_0_16124_x1536_x742803570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x ead-assistant url]{lang="EN-US"}**]{#struct_0_16124_x1536_972457709}
:::

::: {#2025231188 .myid}
[]{#_Toc404792516}[]{#struct_0_16124_x1536_617602240}[]{#_Toc351708662}[]{#_Toc350159595}[]{#_Toc286656858}[]{#_Toc286753642}[]{#_Toc293327424}[]{#_Toc293330687}[]{#_Toc286656860}[]{#_Toc286753644}[]{#_Toc293327426}[]{#_Toc293330689}

**802.1X \-- 802.1X配置命令 \-- dot1x ead-assistant free-ip**

------------------------------------------------------------------------

[**[dot1x ead-assistant free-ip]{lang="EN-US"}**]{#struct_0_16124_x1536_x1861222216}[命令用来配置]{style="font-family:
宋体"}[Free IP]{lang="EN-US"}[，即用户在未通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证之前能够访问的网段。]{style="font-family:宋体"}

[**[undo dot1x ead-assistant free-ip]{lang="EN-US"}**]{#struct_0_16124_x1536_314218533}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972654317}

[**[dot1x ead-assistant free-ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *mask-address* \| *mask-length* }]{lang="EN-US"}]{#struct_0_16124_x1536_1261154098}

[**[undo]{lang="EN-US"}**[ **dot1x ead-assistant free-ip** { *ip-address* { *mask-address* \| *mask-length* } \| **all** }]{lang="EN-US"}]{#struct_0_16124_x1536_1564288530}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1371385652}

[[未配置]{style="font-family:宋体"}[Free IP]{lang="EN-US"}]{#struct_0_16124_x1536_972588781}[，用户在通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证之前不能够访问任何网段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x95298091}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1577054959}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1773336713}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_972130022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x302558712}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1684510236}

[*[ip-address]{lang="EN-US"}*]{#struct_0_16124_x1536_1731360463}[：指定的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[*[mask-address]{lang="EN-US"}*]{#struct_0_16124_x1536_x161802945}[：指定的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[掩码地址]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16124_x1536_972064486}[：指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[掩码地址长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_16124_x1536_x1037533485}[：]{style="font-family:宋体"}[所有配]{style="font-family:宋体"}[置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2034630631}

[[全局使能]{style="font-family:宋体"}[EAD]{lang="EN-US"}]{#struct_0_16124_x1536_1387792603}[快速部署功能且配置]{style="font-family:宋体"}[Free IP]{lang="EN-US"}[之后，未通过认证的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[终端用户可以访问该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段中的网络资源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x545235034}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_115192537}[配置用户在通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证之前能够访问的网段为]{style="font-family:宋体"}[192.168.1.1/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_972261094}

[\[Sysname\] dot1x ead-assistant free-ip 192.168.1.1 255.255.0.0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x393981631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1648210414}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x ead-assistant enable]{lang="EN-US"}**]{#struct_0_16124_x1536_x903855080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x ead-assistant ur]{lang="EN-US"}**]{#struct_0_16124_x1536_1546991861}**[l]{lang="EN-US"}**
:::

::: {#1789924573 .myid}
[]{#_Toc404792517}[]{#struct_0_16124_x1536_972195558}[]{#_Toc351708661}[]{#_Toc350159594}

**802.1X \-- 802.1X配置命令 \-- dot1x ead-assistant url**

------------------------------------------------------------------------

[**[dot1x ead-assistant url]{lang="EN-US"}**]{#struct_0_16124_x1536_899216631}[命令用来配置]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[访问的重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dot1x ead-assistant url]{lang="EN-US"}**]{#struct_0_16124_x1536_x841131126}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_561743204}

[**[dot1x ead-assistant url ]{lang="EN-US"}***[url-string]{lang="EN-US"}*]{#struct_0_16124_x1536_972392166}

[**[undo dot1x ead-assistant url]{lang="EN-US"}**]{#struct_0_16124_x1536_x1605187727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1960050524}

[[未配置重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_16124_x1536_462443470}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972326630}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x18913165}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2035005695}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x2111520372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1303674858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972523238}

[*[url-string]{lang="EN-US"}*]{#struct_0_16124_x1536_x949339417}[：重定向]{style="font-family:宋体;color:black"}[URL]{lang="EN-US" style="color:black"}[地址字符串，为]{style="font-family:宋体;
color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[64]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写]{style="font-family:宋体;color:black"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x607114655}

[[用户在]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_2034761703}[认证成功之前，如果使用浏览器访问非]{style="font-family:宋体"}[Free IP]{lang="EN-US"}[网段的其它网络，设备会将用户访问的]{style="font-family:宋体"}[URL]{lang="EN-US"}[重定向到已配置的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[访问的重定向地址。]{style="font-family:宋体"}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1790034757}[用户]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[访问的重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[和]{style="font-family:宋体"}[Free IP]{lang="EN-US"}[必须在同一个网段内，否则用户无法访问指定的重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_972457702}[用户]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[访问的重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[可多次配置，但仅最后配置的一条有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_617602251}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_477429945}[配置]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[访问的重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://test.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1795622605}

[\[Sysname\] dot1x ead-assistant url http://test.com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972654310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1261154101}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x ead-assistant enable]{lang="EN-US"}**]{#struct_0_16124_x1536_x774822375}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x ead-assistant free-ip]{lang="EN-US"}**]{#struct_0_16124_x1536_x1370756041}
:::

::: {#-319965389 .myid}
[]{#_Toc404792518}[]{#struct_0_16124_x1536_972588774}[]{#_Toc351708647}[]{#_Toc350159579}

**802.1X \-- 802.1X配置命令 \-- dot1x guest-vlan**

------------------------------------------------------------------------

[**[dot1x guest-vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_242408920}[命令用来配置指定端口的]{style="font-family:宋体"}[802.1X Guest VLAN]{lang="EN-US"}[，即]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户在未认证的情况下可以访问的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[资源，该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内通常放置一些用于用户下载客户端软件或其他升级程序的服务器。]{style="font-family:宋体"}

[**[undo dot1x guest-vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_2104639698}[命令用来恢复缺省情况**。**]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1049743081}

[**[dot1x guest-vlan ]{lang="EN-US"}***[guest-vlan-id]{lang="EN-US"}*]{#struct_0_16124_x1536_1237797449}

[**[undo dot1x guest-vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_972130023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x302558713}

[[端口上未配置]{style="font-family:宋体"}[802.1X Guest VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_1684444700}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1418573479}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_972064487}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1037533484}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1020848907}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_328652720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1645359834}

[*[guest-vlan-id]{lang="EN-US"}*]{#struct_0_16124_x1536_972261095}[：端口上指定的]{style="font-family:宋体;color:black"}[Guest VLAN ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:
宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4094]{lang="EN-US" style="color:black"}[（该取值范围与设备型号有关，请以设备的实际情况为准）。该]{style="font-family:宋体;color:black"}[VLAN]{lang="EN-US" style="color:black"}[必须已经创建。]{style="font-family:宋体;
color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x694449329}

[[如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x1995633485}[被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为某个端口的]{style="font-family:宋体"}[802.1X Guest VLAN]{lang="EN-US"}[；同样，如果某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被指定为某个端口的]{style="font-family:宋体"}[802.1X Guest VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能被指定为]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[禁止删除已被配置为]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}]{#struct_0_16124_x1536_x1498856229}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，若要删除该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，请先使用命令]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[dot1x guest-vlan]{lang="EN-US"}**[取消]{style="font-family:宋体"}[802.1X Guest VLAN]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x393981630}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1648144878}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 100 ]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x925011633}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x guest-vlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972195559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_899216630}
:::

::: {#654403475 .myid}
[]{#_Toc404792519}[]{#struct_0_16124_x1536_462509074}[]{#_Toc261334522}[]{#_Toc124063661}[]{#_Toc286656865}[]{#_Toc286753649}[]{#_Toc293327431}[]{#_Toc293330694}[]{#_Toc286656866}[]{#_Toc286753650}[]{#_Toc293327432}[]{#_Toc293330695}[]{#_Toc286656867}[]{#_Toc286753651}[]{#_Toc293327433}[]{#_Toc293330696}[]{#_Toc286656868}[]{#_Toc286753652}[]{#_Toc293327434}[]{#_Toc293330697}[]{#_Toc286656869}[]{#_Toc286753653}[]{#_Toc293327435}[]{#_Toc293330698}[]{#_Toc286656870}[]{#_Toc286753654}[]{#_Toc293327436}[]{#_Toc293330699}[]{#_Toc286656871}[]{#_Toc286753655}[]{#_Toc293327437}[]{#_Toc293330700}[]{#_Toc286656872}[]{#_Toc286753656}[]{#_Toc293327438}[]{#_Toc293330701}[]{#_Toc286656873}[]{#_Toc286753657}[]{#_Toc293327439}[]{#_Toc293330702}[]{#_Toc286656874}[]{#_Toc286753658}[]{#_Toc293327440}[]{#_Toc293330703}[]{#_Toc286656875}[]{#_Toc286753659}[]{#_Toc293327441}[]{#_Toc293330704}[]{#_Toc286656876}[]{#_Toc286753660}[]{#_Toc293327442}[]{#_Toc293330705}[]{#_Toc286656877}[]{#_Toc286753661}[]{#_Toc293327443}[]{#_Toc293330706}[]{#_Toc286656878}[]{#_Toc286753662}[]{#_Toc293327444}[]{#_Toc293330707}[]{#_Toc286656879}[]{#_Toc286753663}[]{#_Toc293327445}[]{#_Toc293330708}[]{#_Toc286656880}[]{#_Toc286753664}[]{#_Toc293327446}[]{#_Toc293330709}[]{#_Toc286656881}[]{#_Toc286753665}[]{#_Toc293327447}[]{#_Toc293330710}[]{#_Toc286656882}[]{#_Toc286753666}[]{#_Toc293327448}[]{#_Toc293330711}[]{#_Toc286656883}[]{#_Toc286753667}[]{#_Toc293327449}[]{#_Toc293330712}[]{#_Toc286656884}[]{#_Toc286753668}[]{#_Toc293327450}[]{#_Toc293330713}[]{#_Toc286656885}[]{#_Toc286753669}[]{#_Toc293327451}[]{#_Toc293330714}[]{#_Toc286656886}[]{#_Toc286753670}[]{#_Toc293327452}[]{#_Toc293330715}[]{#_Toc286656887}[]{#_Toc286753671}[]{#_Toc293327453}[]{#_Toc293330716}[]{#_Toc286656888}[]{#_Toc286753672}[]{#_Toc293327454}[]{#_Toc293330717}[]{#_Toc286656889}[]{#_Toc286753673}[]{#_Toc293327455}[]{#_Toc293330718}[]{#_Toc286656890}[]{#_Toc286753674}[]{#_Toc293327456}[]{#_Toc293330719}[]{#_Toc286656891}[]{#_Toc286753675}[]{#_Toc293327457}[]{#_Toc293330720}[]{#_Toc286656892}[]{#_Toc286753676}[]{#_Toc293327458}[]{#_Toc293330721}[]{#_Toc286656893}[]{#_Toc286753677}[]{#_Toc293327459}[]{#_Toc293330722}[]{#_Toc286656895}[]{#_Toc286753679}[]{#_Toc293327461}[]{#_Toc293330724}[]{#_Toc286656897}[]{#_Toc286753681}[]{#_Toc293327463}[]{#_Toc293330726}[]{#_Toc286656901}[]{#_Toc286753685}[]{#_Toc293327467}[]{#_Toc293330730}[]{#_Toc286656905}[]{#_Toc286753689}[]{#_Toc293327471}[]{#_Toc293330734}

**802.1X \-- 802.1X配置命令 \-- dot1x handshake**

------------------------------------------------------------------------

[**[dot1x handshake]{lang="EN-US"}**]{#struct_0_16124_x1536_x1146347816}[命令用于开启在线用户握手功能。]{style="font-family:宋体"}

[**[undo dot1x handshake]{lang="EN-US"}**]{#struct_0_16124_x1536_388083866}[命令用于关闭在线用户握手功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1001965738}

[**[dot1x handshake]{lang="EN-US"}**]{#struct_0_16124_x1536_x1735366199}

[**[undo dot1x handshake]{lang="EN-US"}**]{#struct_0_16124_x1536_334608196}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1436504087}

[[在线用户握手功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1275854008}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1978149524}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1034156520}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1353372732}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x156217410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x376585815}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1587257294}

[[开启设备的在线用户握手功能后，设备会定期（时间间隔通过命令]{style="font-family:宋体"}**[dot1x timer handshake-period]{lang="EN-US"}**]{#struct_0_16124_x1536_333625156}[设置）向通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证的在线用户发送握手报文，以定期检测用户的在线情况。如果设备连续多次（通过命令]{style="font-family:宋体"}**[dot1x retry]{lang="EN-US"}**[设置）没有收到客户端的响应报文，则会将用户置为下线状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1304795066}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_375155350}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启在线用户握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1920843554}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x handshake]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_621777068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1050797713}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer handshake-period]{lang="EN-US"}**]{#struct_0_16124_x1536_x555944844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x retry]{lang="EN-US"}**]{#struct_0_16124_x1536_1467097213}
:::

::: {#-864664660 .myid}
[]{#_Toc404792520}[]{#struct_0_16124_x1536_972392167}[]{#_Toc351708646}[]{#_Toc173241623}[]{#_Toc173722538}[]{#_Toc173241626}[]{#_Toc173722541}[]{#_Toc173241627}[]{#_Toc173722542}[]{#_Toc173241628}[]{#_Toc173722543}[]{#_Toc173241629}[]{#_Toc173722544}[]{#_Toc173241630}[]{#_Toc173722545}[]{#_Toc173241631}[]{#_Toc173722546}[]{#_Toc173241632}[]{#_Toc173722547}[]{#_Toc173241633}[]{#_Toc173722548}[]{#_Toc173241634}[]{#_Toc173722549}[]{#_Toc173241635}[]{#_Toc173722550}[]{#_Toc173241636}[]{#_Toc173722551}[]{#_Toc173241637}[]{#_Toc173722552}[]{#_Toc173241638}[]{#_Toc173722553}[]{#_Toc173241639}[]{#_Toc173722554}[]{#_Toc173241640}[]{#_Toc173722555}[]{#_Toc173241644}[]{#_Toc173722559}[]{#_Toc173241646}[]{#_Toc173722561}[]{#_Toc173241647}[]{#_Toc173722562}[]{#_Toc173241648}[]{#_Toc173722563}[]{#_Toc173241649}[]{#_Toc173722564}[]{#_Toc173241650}[]{#_Toc173722565}[]{#_Toc173241651}[]{#_Toc173722566}[]{#_Toc173241652}[]{#_Toc173722567}[]{#_Toc173241653}[]{#_Toc173722568}[]{#_Toc173241654}[]{#_Toc173722569}[]{#_Toc173241655}[]{#_Toc173722570}[]{#_Toc173241656}[]{#_Toc173722571}[]{#_Toc173241657}[]{#_Toc173722572}[]{#_Toc173241658}[]{#_Toc173722573}[]{#_Toc173241659}[]{#_Toc173722574}[]{#_Toc173241660}[]{#_Toc173722575}[]{#_Toc173241661}[]{#_Toc173722576}[]{#_Toc173241662}[]{#_Toc173722577}[]{#_Toc173241663}[]{#_Toc173722578}[]{#_Toc173241664}[]{#_Toc173722579}

**802.1X \-- 802.1X配置命令 \-- dot1x handshake secure**

------------------------------------------------------------------------

[**[dot1x handshake secure]{lang="EN-US"}**]{#struct_0_16124_x1536_x1605187728}[命令用来开启在线用户握手安全功能。]{style="font-family:宋体"}

[**[undo dot1x handshake secure]{lang="EN-US"}**]{#struct_0_16124_x1536_x412602471}[命令用来关闭在线用户握手安全功能**。**]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_972326631}

[**[dot1x handshake secure]{lang="EN-US"}**]{#struct_0_16124_x1536_x18913164}

[**[undo dot1x handshake secure]{lang="EN-US"}**]{#struct_0_16124_x1536_2035005694}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2111454836}

[[在线用户握手安全功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16124_x1536_972523239}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x949339416}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x607049119}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1368197617}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_972457703}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_617602250}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_477429944}

[[只有设备上的在线用户握手功能处于开启状态时，安全握手功能才会生效。]{style="font-family:宋体"}]{#struct_0_16124_x1536_1795622606}

[[本功能仅能在]{style="font-family:宋体"}[iNode]{lang="EN-US"}]{#struct_0_16124_x1536_972654311}[客户端和]{style="font-family:宋体"}[iMC]{lang="EN-US"}[服务器配合使用的组网环境中生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1261154100}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x774887911}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启安全握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_972588775}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x handshake secure]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_242408921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_2104639699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x handshake]{lang="EN-US"}**]{#struct_0_16124_x1536_x1049808617}
:::

::: {#1360279618 .myid}
[]{#_Toc404792521}[]{#struct_0_16124_x1536_1430291464}[]{#_Toc261334524}[]{#_Toc162777666}

**802.1X \-- 802.1X配置命令 \-- dot1x mandatory-domain**

------------------------------------------------------------------------

[**[dot1x mandatory-domain]{lang="EN-US"}**]{#struct_0_16124_x1536_333690692}[命令用来指定端口上]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户使用的强制认证域。]{style="font-family:宋体"}

[**[undo dot1x mandatory-domain]{lang="EN-US"}**]{#struct_0_16124_x1536_570368574}[命令用来删除该端口上为]{style="font-family:
宋体"}[802.1X]{lang="EN-US"}[用户指定的强制认证域。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1314301258}

[**[dot1x mandatory-domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_16124_x1536_x1148448498}

[**[undo dot1x]{lang="EN-US"}**[ **mandatory-domain**]{lang="EN-US"}]{#struct_0_16124_x1536_335880898}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1168883703}

[[未指定]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_570208405}[用户使用的强制认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1424090446}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_168047588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334149445}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_503474543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1005108666}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2017474395}

[*[domain-name]{lang="EN-US"}*]{#struct_0_16124_x1536_x793238415}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x170491733}

[[从指定端口上接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1859088923}[用户将按照如下先后顺序选择认证域：端口上指定的强制]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[用户名中指定的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[系统缺省的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_785112529}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1094960238}[指定端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户使用的强制认证域为]{style="font-family:宋体"}[my-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_334214981}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x mandatory-domain my-domain]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_366433449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1808538971}
:::

::: {#-1061994866 .myid}
[]{#_Toc404792522}[]{#struct_0_16124_x1536_1282787354}[]{#_Toc261334525}

**802.1X \-- 802.1X配置命令 \-- dot1x max-user**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**[ **max-user**]{lang="EN-US"}]{#struct_0_16124_x1536_139515111}[命令用来配置端口上最多允许同时接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户数。当接入此端口的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户数超过最大值后，新接入的用户将被拒绝。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**[ **max-user**]{lang="EN-US"}]{#struct_0_16124_x1536_x784407564}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_311141056}

[**[dot1x]{lang="EN-US"}**[ **max-user** *user-number*]{lang="EN-US"}]{#struct_0_16124_x1536_x1775895255}

[**[undo dot1x]{lang="EN-US"}**[ **max-user**]{lang="EN-US"}]{#struct_0_16124_x1536_1972553958}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334280517}

[[端口上最多允许同时接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1543953428}[用户数与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1778961941}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1794883400}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_100596179}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1999726745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1882998673}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x104052389}

[*[user-number]{lang="EN-US"}*]{#struct_0_16124_x1536_334346053}[：端口允许同时接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户数的最大值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1983628331}

[[由于系统资源有限，如果当前端口上接入的用户过多，接入用户之间会发生资源的争用，因此适当地配置该值可以使属于当前端口的用户获得可靠的性能保障。]{style="font-family:宋体"}]{#struct_0_16124_x1536_x991917539}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x284517596}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_804758181}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上最多允许同时接入]{style="font-family:宋体"}[32]{lang="EN-US"}[个]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_420073908}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x max-user 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1894700873}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x188771874}
:::

::: {#1380412543 .myid}
[]{#_Toc404792523}[]{#struct_0_16124_x1536_x1142244953}[]{#_Toc261334526}[]{#_Toc151872613}[]{#_Toc151806675}[]{#_Toc151806365}[]{#_Toc151806277}[]{#_Toc151539879}

**802.1X \-- 802.1X配置命令 \-- dot1x multicast-trigger**

------------------------------------------------------------------------

[**[dot1x multicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_334411589}[命令用来开启]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的组播触发功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo dot1x multicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_x2058429091}[命令用来]{style="font-family:
宋体"}[关闭]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的组播触发功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1370916777}

[**[dot1x multicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_x351569766}

[**[undo dot1x multicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_x168877399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x627355124}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1597136061}[的组播触发功能处于开启状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1842520335}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1653511567}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334477125}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1418506263}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1640239694}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1025886700}

[[开启了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1012998577}[的组播触发功能的端口会定期（间隔时间通过命令]{style="font-family:宋体"}**[dot1x timer tx-period]{lang="EN-US"}**[设置）向客户端组播发送]{style="font-family:宋体"}[EAP-Request/Identity]{lang="EN-US"}[报文来检测客户端并触发认证。该功能用于支持不能主动发送]{style="font-family:宋体"}[EAPOL-Start]{lang="EN-US"}[报文来发起认证的客户端。]{style="font-family:宋体"}

[[对于无线局域网来说，可以由客户端主动发起认证，或由无线模块发现用户并触发认证，而不必设备端定期发送]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1589101944}[的组播报文来触发。同时，组播触发报文会占用无线的通信带宽，因此建议无线局域网中的接入设备关闭该功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1323297777}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x540754040}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的组播触发功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_334542661}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x multicast-trigger]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1803059253}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x592495264}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer tx-period]{lang="EN-US"}**]{#struct_0_16124_x1536_x1252490245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x unicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_1959418436}
:::

::: {#-1131226147 .myid}
[]{#_Toc404792524}[]{#struct_0_16124_x1536_x2036020890}[]{#_Toc261334527}

**802.1X \-- 802.1X配置命令 \-- dot1x port-control**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**[ **port-control**]{lang="EN-US"}]{#struct_0_16124_x1536_317034215}[命令用来设置端口的授权状态。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**[ **port-control**]{lang="EN-US"}]{#struct_0_16124_x1536_x1103555241}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x216043291}

[**[dot1x]{lang="EN-US"}**[ **port-control** { **authorized-force** \| **auto** \| **unauthorized-force** }]{lang="EN-US"}]{#struct_0_16124_x1536_334608197}

[**[undo dot1x]{lang="EN-US"}**[ **port-control**]{lang="EN-US"}]{#struct_0_16124_x1536_x1436504088}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1903368041}

[[端口的授权状态为]{style="font-family:宋体"}**[auto]{lang="EN-US"}**]{#struct_0_16124_x1536_1143982305}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_126114169}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1583597633}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1772104544}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x704678696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_73307780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_419342699}

[**[authorized-force]{lang="EN-US"}**]{#struct_0_16124_x1536_333625157}[：强制授权状态，表示端口始终处于授权状态，允许用户不经认证授权即可访问网络资源。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_16124_x1536_1304795065}[：自动识别状态，表示端口初始状态为非授权状态，仅允许]{style="font-family:宋体"}[EAPOL]{lang="EN-US"}[报文收发，不允许用户访问网络资源；如果用户认证通过，则端口切换到授权状态，允许用户访问网络资源。这也是最常用的一种状态。]{style="font-family:宋体"}

[**[unauthorized-force]{lang="EN-US"}**]{#struct_0_16124_x1536_375220886}[：强制非授权状态，表示端口始终处于非授权状态，不允许用户访问网络资源。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1352613598}

[[通过配置端口的授权状态，可以控制端口上接入的用户是否需要通过认证才能访问网络资源。]{style="font-family:宋体"}]{#struct_0_16124_x1536_499360709}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1207715580}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1992416292}[指定端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[处于强制非授权状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1118519654}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x port-control unauthorized-force]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_333690693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_570368575}
:::

::: {#-1444018256 .myid}
[]{#_Toc404792525}[]{#struct_0_16124_x1536_x1314301257}[]{#_Toc261334528}

**802.1X \-- 802.1X配置命令 \-- dot1x port-method**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**[ **port-method**]{lang="EN-US"}]{#struct_0_16124_x1536_1130096163}[命令用来配置端口的接入控制方式。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**[ **port-method**]{lang="EN-US"}]{#struct_0_16124_x1536_1418669035}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x493669091}

[**[dot1x]{lang="EN-US"}**[ **port-method** { **macbased** \| **portbased** }]{lang="EN-US"}]{#struct_0_16124_x1536_998182139}

[**[undo dot1x]{lang="EN-US"}**[ **port-method**]{lang="EN-US"}]{#struct_0_16124_x1536_x436467052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1401783493}

[[端口的接入控制方式为]{style="font-family:宋体"}**[macbased]{lang="EN-US"}**]{#struct_0_16124_x1536_334149442}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_503474538}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x2098217553}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x823240398}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x2008612691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1092567659}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1619578018}

[**[macbased]{lang="EN-US"}**]{#struct_0_16124_x1536_x1412585128}[：表示基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对接入用户进行认证，即该端口下的所有接入用户均需要单独认证，当某个用户下线时，也只有该用户无法使用网络。]{style="font-family:宋体"}

[**[portbased]{lang="EN-US"}**]{#struct_0_16124_x1536_x1870833108}[：表示基于端口对接入用户进行认证，即只要该端口下的第一个用户认证成功后，其他接入用户无须认证就可使用网络资源，当第一个用户下线后，其它用户也会被拒绝使用网络。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334214978}

[[部分设备上不支持]{style="font-family:宋体"}**[macbased]{lang="EN-US"}**]{#struct_0_16124_x1536_x442870624}[方式，因此]{style="font-family:宋体"}**[macbased]{lang="EN-US"}**[方式的配置生效情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[若端口上同时启动了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1507585580}[和]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证功能，则端口接入控制方式必须为]{style="font-family:宋体"}**[macbased]{lang="EN-US"}**[。关于]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证的相关介绍，请参考"安全配置指导"中的"]{style="font-family:宋体"}[Portal]{lang="EN-US"}["。]{style="font-family:宋体"}

[[在要求所有接入用户都单独认证的情况下，选择基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16124_x1536_1779154610}[的控制方式，可提高网络接入的安全性。否则，可采用基于端口的接入控制方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x905640110}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x1285426781}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置对接入用户进行基于端口的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x26523512}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x port-method portbased]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1791400025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1313895676}
:::

::: {#410525384 .myid}
[]{#_Toc404792526}[]{#struct_0_16124_x1536_334280514}[]{#_Toc261334529}

**802.1X \-- 802.1X配置命令 \-- dot1x quiet-period**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**[ **quiet-period**]{lang="EN-US"}]{#struct_0_16124_x1536_1543953431}[命令用来开启静默定时器功能。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**[ **quiet-period**]{lang="EN-US"}]{#struct_0_16124_x1536_1779420692}[命令用来关闭静默定时器功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1072182411}

[**[dot1x]{lang="EN-US"}**[ **quiet-period**]{lang="EN-US"}]{#struct_0_16124_x1536_560078367}

[**[undo dot1x quiet-period]{lang="EN-US"}**]{#struct_0_16124_x1536_x575037710}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_301680802}

[[静默定时器功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16124_x1536_1914937361}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1976268955}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_334346050}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1983628328}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_217870506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_696747582}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1528857396}

[[在静默定时器功能处于开启状态的情况下，设备将在一段时间之内不对]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1003346626}[认证失败的用户进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证处理，该时间由]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[静默定时器控制，可通过]{style="font-family:宋体"}**[dot1x timer quiet-period]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2042432837}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_754339494}[开启静默定时器功能，并配置静默定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_334411586}

[\[Sysname\] dot1x quiet-period]{lang="EN-US"}

[\[Sysname\] dot1x timer quiet-period 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2058429078}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_550742164}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer]{lang="EN-US"}**]{#struct_0_16124_x1536_2129692680}
:::

::: {#-1586417450 .myid}
[]{#_Toc404792527}[]{#struct_0_16124_x1536_1904677071}[]{#_Toc261334530}[]{#_Toc215628899}

**802.1X \-- 802.1X配置命令 \-- dot1x re-authenticate**

------------------------------------------------------------------------

[**[dot1x re-authenticate]{lang="EN-US"}**]{#struct_0_16124_x1536_x127762062}[命令用来开启周期性重认证功能。]{style="font-family:宋体"}

[**[undo dot1x re-authenticate]{lang="EN-US"}**]{#struct_0_16124_x1536_1708386991}[命令]{style="font-family:
宋体"}[用来关闭周期性重认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_971181369}

[**[dot1x re-authenticate]{lang="EN-US"}**]{#struct_0_16124_x1536_920176092}

[**[undo dot1x re-authenticate]{lang="EN-US"}**]{#struct_0_16124_x1536_515326355}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334477122}

[[周期性重认证功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16124_x1536_1418506256}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1640436299}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1839540153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x938008888}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x245594497}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1513341236}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x148182867}

[[端口启动了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_430974863}[的周期性重认证功能后，设备会根据周期性重认证定时器（]{style="font-family:宋体"}**[dot1x timer reauth-period]{lang="EN-US"}**[）设定的时间间隔定期启动对该端口在线]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户的认证，以检测用户连接状态的变化，更新服务器下发的授权属性（例如]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[、]{style="font-family:宋体"}[QoS Profile]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334542658}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x917929938}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[重认证功能，并配置周期性重认证时间间隔为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x545586370}

[\[Sysname\] dot1x timer reauth-period 1800]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x re-authenticate]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1459137135}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x892621418}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer]{lang="EN-US"}**]{#struct_0_16124_x1536_578597323}
:::

::: {#-830682816 .myid}
[]{#_Toc404792528}[]{#struct_0_16124_x1536_x1756360113}[]{#_Toc351708650}[]{#_Toc350159583}

**802.1X \-- 802.1X配置命令 \-- dot1x re-authenticate server-unreachable keep-online**

------------------------------------------------------------------------

[**[dot1x re-authenticate server-unreachable keep-online]{lang="EN-US"}**]{#struct_0_16124_x1536_378655837}[命令用来配置重认证服务器不可达时端口上的用户保持在线状态。]{style="font-family:宋体"}

[**[undo dot1x re-authenticate server-unreachable]{lang="EN-US"}**]{#struct_0_16124_x1536_229952125}[命令用来恢复缺省情况**。**]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756425649}

[**[dot1x re-authenticate server-unreachable keep-online]{lang="EN-US"}**]{#struct_0_16124_x1536_1361591986}

[**[undo dot1x re-authenticate server-unreachable]{lang="EN-US"}**]{#struct_0_16124_x1536_x2122004532}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x613237423}

[[端口上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_x1756229041}[在线用户重认证时，若认证服务器不可达，则会被强制下线。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x957488248}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_2057541477}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1721457639}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1756294577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1704768130}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756753328}

[[若]{style="font-family:宋体"}]{#struct_0_16124_x1536_2057607251}[端口上启动了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的周期性重认证功能，则]{style="font-family:宋体"}[设备会定期对端口上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户进行重认证，重认证过程中，若设备发现认证服务器状态不可达，则可以根据本配置，决定是否保持其在线状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x523507558}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x278623072}[配置[端口]{style="color:black"}]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体;color:black"}[802.1X]{lang="EN-US"}[在线用户进行]{style="font-family:宋体;color:black"}[重认证时，若服务器不可达，则保持在线状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x1756818864}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x re-authenticate server-unreachable keep-online]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1730964338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1093820743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x]{lang="EN-US"}[ re-authenticate]{lang="EN-US"}**]{#struct_0_16124_x1536_x1891018839}
:::

::: {#-880860465 .myid}
[]{#_Toc404792529}[]{#struct_0_16124_x1536_325513420}[]{#_Toc261334531}

**802.1X \-- 802.1X配置命令 \-- dot1x retry**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_16124_x1536_x569226748}[命令用来设置设备向接入用户发送认证请求报文的最大次数。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_16124_x1536_334608194}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1436504085}

[**[dot1x]{lang="EN-US"}**[ **retry** *max-retry-value*]{lang="EN-US"}]{#struct_0_16124_x1536_1856313874}

[**[undo dot1x]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_16124_x1536_372688738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x656165550}

[[设备向接入用户发送认证请求报文的最大次数为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_16124_x1536_x1369199879}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1694232676}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x487240246}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1357888444}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_333625154}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1304795064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_375286422}

[*[max-retry-value]{lang="EN-US"}*]{#struct_0_16124_x1536_x2135734088}[：向接入用户发送认证请求报文的最大尝试次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1091478858}

[[如果设备向用户发送认证请求报文后，在规定的时间里没有收到用户的响应，则设备将向用户重发该认证请求报文，若设备累计发送认证请求报文的次数达到配置的最大值后，仍然没有得到用户响应，则停止发送认证请求。对于]{style="font-family:宋体"}[EAP-Request/Identity]{lang="EN-US"}]{#struct_0_16124_x1536_x286115871}[报文，该时间由]{style="font-family:宋体"}**[dot1x timer tx-period]{lang="EN-US"}**[设置；对于]{style="font-family:宋体"}[EAP-Request/MD5 Challenge]{lang="EN-US"}[报文，该时间由]{style="font-family:宋体"}**[dot1x timer supp-timeout]{lang="EN-US"}**[设置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1897565033}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_686470618}[配置设备最多向接入用户发送]{style="font-family:宋体"}[9]{lang="EN-US"}[次认证请求报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_1173811418}

[\[Sysname\] dot1x retry 9]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_333690690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_570368572}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer]{lang="EN-US"}**]{#struct_0_16124_x1536_x1314301264}
:::

::: {#1992295413 .myid}
[]{#_Toc404792530}[]{#struct_0_16124_x1536_x1756622256}[]{#_Toc351708651}[]{#_Toc350159584}

**802.1X \-- 802.1X配置命令 \-- dot1x smarton**

------------------------------------------------------------------------

[**[dot1x smarton]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756687792}[命令用来开启端口的]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo dot1x smarton]{lang="EN-US"}**]{#struct_0_16124_x1536_x1832455796}[命令用来关闭端口的]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1594526833}

[**[dot1x smarton]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756491184}

[**[undo dot1x smarton]{lang="EN-US"}**]{#struct_0_16124_x1536_x1529850707}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1860016638}

[[端口的]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_1602407763}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756556720}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1027863423}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x421293909}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x324313465}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1756360112}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1187428104}

[[若开启了]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x125713168}[功能的端口上收到]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[EAPOL-Start]{lang="EN-US"}[报文，则将向其回复单播的]{style="font-family:宋体"}[EAP-Request/Notification]{lang="EN-US"}[报文，并开启定时器（]{style="font-family:宋体"}**[dot1x smarton timer supp-timeout]{lang="EN-US"}**[）等待客户端响应]{style="font-family:宋体"}[EAP-Response/Notification]{lang="EN-US"}[报文。该]{style="font-family:宋体"}[Notification]{lang="EN-US"}[报文中包含一个]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}[和一个]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要，若这两个值与本地配置的]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[的]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}[以及]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[密码的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值相同，则继续客户端的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证，否则中止客户端的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1828151114}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x1756425648}[使能端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x204491955}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x smarton]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x928422400}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_1261759118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton switchid]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756229040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton password]{lang="EN-US"}**]{#struct_0_16124_x1536_1771395107}
:::

::: {#907901970 .myid}
[]{#struct_0_16124_x1536_1621594874}[]{#_Toc351708653}[]{#_Toc350159586}[]{#_Toc404792531}

**802.1X \-- 802.1X配置命令 \-- dot1x smarton password**

------------------------------------------------------------------------

[**[dot1x smarton password]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756294576}[命令用来配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[密码。]{style="font-family:宋体"}

[**[undo dot1x smarton password]{lang="EN-US"}**]{#struct_0_16124_x1536_x1024115225}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x921735297}

[**[dot1x smarton password ]{lang="EN-US"}**[{ **cipher** *cipher-string* \| **simple** *plain-string* }]{lang="EN-US"}]{#struct_0_16124_x1536_1033937843}

[**[undo]{lang="EN-US"}**[ **dot1x smarton password**]{lang="EN-US"}]{#struct_0_16124_x1536_x1756753327}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x671276104}

[[未配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_1427750270}[密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_98382726}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1756818863}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_191349963}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_123942111}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1747492859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756622255}

[**[cipher]{lang="EN-US"}**]{#struct_0_16124_x1536_x468971238}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_16124_x1536_x694187187}[：]{style="font-family:宋体;color:black"}[设置的密文密码]{style="font-family:宋体"}[，区分大小写，[为]{style="color:black"}]{style="font-family:宋体"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[53]{lang="EN-US" style="color:black"}[个字符的字符串。]{style="font-family:宋体;color:black"}

[**[simple]{lang="EN-US"}**]{#struct_0_16124_x1536_2071828035}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_16124_x1536_x1756687791}[：]{style="font-family:宋体;color:black"}[设置的明文密码]{style="font-family:宋体"}[，区分大小写，[为]{style="color:black"}]{style="font-family:宋体"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[16]{lang="EN-US" style="color:black"}[个字符的字符串。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1429171269}

[[使能了]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_618189998}[功能的端口上，需要验证]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[EAP-Response/Notification]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要，]{style="font-family:宋体"}[只有与本命令配置的]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[密码]{style="font-family:宋体"}[的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要]{style="font-family:宋体"}[相同，客户端]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的认证才能继续进行]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[不论以密文形式还是明文形式配置密码，设备均以密文形式存储，并且后配置的密码会覆盖先前配置的密码。]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1756491183}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_392463594}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1211354579}[配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[密码为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_611964851}

[\[Sysname\] dot1x smarton password simple abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756556719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x182186766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton]{lang="EN-US"}**]{#struct_0_16124_x1536_873737623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton switchid]{lang="EN-US"}**]{#struct_0_16124_x1536_x137869875}
:::

::: {#-896700341 .myid}
[]{#_Toc404792532}[]{#struct_0_16124_x1536_x1756360111}[]{#_Toc351708655}[]{#_Toc350159588}

**802.1X \-- 802.1X配置命令 \-- dot1x smarton retry**

------------------------------------------------------------------------

[**[dot1x smarton retry]{lang="EN-US"}**]{#struct_0_16124_x1536_1541455251}[命令用来配置重发]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[通知请求报文的最大次数。]{style="font-family:宋体"}

[**[undo dot1x smarton retry]{lang="EN-US"}**]{#struct_0_16124_x1536_x33495683}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2029585983}

[**[dot1x smarton retry]{lang="EN-US"}**[ *retries*]{lang="EN-US"}]{#struct_0_16124_x1536_x1756425647}

[**[undo dot1x smarton retry]{lang="EN-US"}**]{#struct_0_16124_x1536_x1770575896}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x666702980}

[[重发]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x1756229039}[通知请求报文的最大次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1313259856}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_708353434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1635110983}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1756294575}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_541968716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1266718332}

[*[retries]{lang="EN-US"}*]{#struct_0_16124_x1536_x1296680428}[：]{style="font-family:宋体;color:black"}[重发]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[通知请求报文的最大次数[，取值范围为]{style="color:black"}]{style="font-family:宋体"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[10]{lang="SV" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756753326}

[[设备向客户端发送]{style="font-family:宋体"}[EAP-Request/Notification]{lang="EN-US"}]{#struct_0_16124_x1536_894807837}[报文后，会开启通知请求超时定时器（]{style="font-family:宋体"}**[dot1x smarton timer supp-timeout]{lang="EN-US"}**[）等待客户端响应]{style="font-family:宋体"}[EAP-Response/Notification]{lang="EN-US"}[报文，若定时器超时后客户端仍未回复，则设备会重发]{style="font-family:宋体"}[EAP-Request/Notification]{lang="EN-US"}[报文，并重新启动定时器。当重发次数达到规定的最大次数后，会停止对该客户端的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1408761286}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_31159769}[配置重发]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[通知请求报文的最大次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x1756818862}

[\[Sysname\] dot1x smarton retry 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1757433904}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_726779579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton timer supp-timeout]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756622254}
:::

::: {#589652082 .myid}
[]{#_Toc404792533}[]{#struct_0_16124_x1536_x2035055179}[]{#_Toc351708652}[]{#_Toc350159585}

**802.1X \-- 802.1X配置命令 \-- dot1x smarton switchid**

------------------------------------------------------------------------

[**[dot1x smarton switchid]{lang="EN-US"}**]{#struct_0_16124_x1536_x144327457}[命令用来配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[的]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dot1x smarton switchid]{lang="EN-US"}**]{#struct_0_16124_x1536_x774911509}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756687790}

[**[dot1x smarton switchid ]{lang="EN-US"}***[switch-string]{lang="EN-US"}*]{#struct_0_16124_x1536_1299712086}

[**[undo dot1x smarton switchid]{lang="EN-US"}**]{#struct_0_16124_x1536_x104239346}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_524880431}

[[未配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x1756491182}[的]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1958547535}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_1525871664}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x415651976}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1756556718}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_1383897175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x55782336}

[*[switch-string]{lang="EN-US"}*]{#struct_0_16124_x1536_x1030580935}[：可显示的交换机]{style="font-family:宋体;color:black"}[ID]{lang="EN-US" style="color:black"}[字符串，其长度的取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[30]{lang="EN-US" style="color:black"}[，区分大小写]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756360110}

[[使能了]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_x24628690}[功能的端口上，需要验证]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[EAP-Response/Notification]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}[字符串，]{style="font-family:宋体"}[只有与本命令配置的值相同，客户端]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的认证才能继续进行]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1145918730}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x1756425646}[配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[的]{style="font-family:宋体"}[Switch ID]{lang="EN-US"}[为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_958307459}

[\[Sysname\] dot1x smarton switchid abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x970365074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x210149386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756229038}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton password]{lang="EN-US"}**]{#struct_0_16124_x1536_1415623499}
:::

::: {#-437105148 .myid}
[]{#_Toc404792534}[]{#struct_0_16124_x1536_x1338267879}[]{#_Toc351708654}[]{#_Toc350159587}

**802.1X \-- 802.1X配置命令 \-- dot1x smarton timer supp-timeout**

------------------------------------------------------------------------

[**[dot1x smarton timer supp-timeout]{lang="EN-US"}**]{#struct_0_16124_x1536_x1734623251}[命令用来配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[通知请求超时定时器时长。]{style="font-family:宋体"}

[**[undo dot1x smarton timer supp-timeout]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756294574}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_2108052657}

[**[dot1x smarton timer supp-timeout]{lang="EN-US"}**[ *supp-timeout-value*]{lang="EN-US"}]{#struct_0_16124_x1536_x1678823880}

[**[undo dot1x smarton timer supp-timeout]{lang="EN-US"}**]{#struct_0_16124_x1536_1112952786}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756753333}

[[SmartOn]{lang="EN-US"}]{#struct_0_16124_x1536_1298026828}[通知请求超时定时器时长为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1322565147}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1756818869}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1327679811}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_697520195}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x781999446}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756622261}

[*[supp-timeout-value]{lang="EN-US"}*]{#struct_0_16124_x1536_1856693126}[：]{style="font-family:宋体;
color:black"}[SmartOn]{lang="EN-US"}[通知请求超时[定时器的值，取值范围为]{style="color:black"}]{style="font-family:
宋体"}[1]{lang="EN-US" style="color:black"}[0]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[120]{lang="SV" style="color:black"}[，单位为秒。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x36845828}

[[设备向客户端发送]{style="font-family:宋体"}[EAP-Request/Notification]{lang="EN-US"}]{#struct_0_16124_x1536_x1078756236}[报文后，会开启通知请求超时定时器等待客户端响应]{style="font-family:宋体"}[EAP-Response/Notification]{lang="EN-US"}[报文，若定时器超时后客户端仍未回复，则设备会重发]{style="font-family:宋体"}[EAP-Request/Notification]{lang="EN-US"}[报文，并重新启动定时器。当重发次数达到规定的最大次数（]{style="font-family:宋体"}**[dot1x smarton retry]{lang="EN-US"}**[）后，会停止对该客户端的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756687797}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1702996613}[配置]{style="font-family:宋体"}[SmartOn]{lang="EN-US"}[定时器时长为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x124449801}

[\[Sysname\] dot1x smarton timer supp-timeout 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1045174987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x1756491189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x smarton retry]{lang="EN-US"}**]{#struct_0_16124_x1536_x414105460}
:::

::: {#2066251323 .myid}
[]{#_Toc404792535}[]{#struct_0_16124_x1536_1533315154}[]{#_Toc261334533}[]{#_Toc91231747}

**802.1X \-- 802.1X配置命令 \-- dot1x timer**

------------------------------------------------------------------------

[**[dot1x]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_16124_x1536_x2072064455}[命令用来配置]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的定时器参数。]{style="font-family:宋体"}

[**[undo dot1x]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_16124_x1536_x24221307}[命令用来将指定的定时器恢复为缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_580033546}

[**[dot1x timer ]{lang="EN-US"}**[{ **ead-timeout** *ead-timeout-value* \| **handshake-period** *handshake-period-value* \| **quiet-period** *quiet-period-value* \| **reauth-period** *reauth-period-value* \| **server-timeout** *server-timeout-value* \| **supp-timeout** *supp-timeout-value* \| **tx-period** *tx-period-value* }]{lang="EN-US"}]{#struct_0_16124_x1536_x54175210}

[**[undo dot1x timer ]{lang="EN-US"}**[{ **ead-timeout** \| **handshake-period** \| **quiet-period** \| **reauth-period** \| **server-timeout** \| **supp-timeout** \| **tx-period** }]{lang="EN-US"}]{#struct_0_16124_x1536_x24500166}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334149443}

[[握手定时器的值为]{style="font-family:宋体"}[15]{lang="EN-US"}]{#struct_0_16124_x1536_503474537}[秒，]{style="font-family:宋体"}[EAD]{lang="EN-US"}[超时定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[分钟，静默定时器的值为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒，周期性重认证定时器的值为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒，认证服务器超时定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒，客户端认证超时定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒，用户名请求超时定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2098217546}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1582689749}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x2024679588}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1358546833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_478511034}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_728719881}

[*[ead-timeout-value]{lang="SV"}*]{#struct_0_16124_x1536_x1756360117}[：]{style="font-family:宋体"}[EAD]{lang="EN-US"}[超时定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[handshake-period]{lang="SV"}**]{#struct_0_16124_x1536_313243894}*[ handshake-period-value]{lang="SV"}*[：]{style="font-family:宋体"}[握手定时器的值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[5]{lang="SV"}[～]{style="font-family:宋体"}[1024]{lang="SV"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[**[quiet-period]{lang="SV"}**]{#struct_0_16124_x1536_334214979}*[ quiet-period-value]{lang="SV"}*[：]{style="font-family:宋体"}[静默定时器的值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[10]{lang="SV"}[～]{style="font-family:宋体"}[120]{lang="SV"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[**[reauth-period]{lang="SV"}**]{#struct_0_16124_x1536_x442870623}*[ reauth-period-value]{lang="SV"}*[：]{style="font-family:宋体"}[周期性重认证定时器的值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[60]{lang="SV"}[～]{style="font-family:宋体"}[7200]{lang="SV"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[**[server-timeout]{lang="SV"}**]{#struct_0_16124_x1536_x1507913260}*[ server-timeout-value]{lang="SV"}*[：]{style="font-family:宋体"}[认证服务器超时定时器的值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[100]{lang="SV"}[～]{style="font-family:宋体"}[300]{lang="SV"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[**[supp-timeout]{lang="SV"}**]{#struct_0_16124_x1536_1348133764}*[ supp-timeout-value]{lang="SV"}*[：]{style="font-family:宋体"}[客户端认证超时定时器的值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[120]{lang="SV"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[**[tx-period ]{lang="SV"}**]{#struct_0_16124_x1536_x1609380066}*[tx-period-value]{lang="SV"}*[：]{style="font-family:宋体"}[用户名请求超时定时器的值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[10]{lang="SV"}[～]{style="font-family:宋体"}[120]{lang="SV"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x271158152}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_2142068001}[认证过程受以下定时器的控制：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[握手定时器（]{style="font-family:宋体"}]{#struct_0_16124_x1536_x700130259}**[handshake-period]{lang="EN-US"}**[）：此定时器是在用户认证成功后启动的，设备端以此间隔为周期发送握手请求报文，以定期检测用户的在线情况。如果配置发送次数为]{style="font-family:宋体"}[N]{lang="EN-US"}[，则当设备端连续]{style="font-family:宋体"}[N]{lang="EN-US"}[次没有收到客户端的响应报文，就认为用户已经下线。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静默定时器（]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1576013607}**[quiet-period]{lang="EN-US"}**[）：对用户认证失败以后，设备端需要静默一段时间（该时间由静默定时器设置），在静默期间，设备端不对]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证失败的用户进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证处理]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[周期性重认证定时器（]{style="font-family:宋体"}]{#struct_0_16124_x1536_334280515}**[reauth-period]{lang="EN-US"}**[）：端口下开启了周期性重认证功能（通过命令]{style="font-family:宋体"}**[dot1x re-authenticate]{lang="EN-US"}**[）后，设备端以此间隔为周期对端口上的在线用户发起重认证。对于已在线的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户，要等当前重认证周期结束并且认证通过后才会按新配置的周期进行后续的重认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[认证服务器超时定时器（]{style="font-family:宋体"}]{#struct_0_16124_x1536_1543953430}**[server-timeout]{lang="EN-US"}**[）：当设备端向认证服务器发送了]{style="font-family:宋体"}[RADIUS Access-Request]{lang="EN-US"}[请求报文后，设备端启动]{style="font-family:宋体"}**[server-timeout]{lang="EN-US"}**[定时器，若在该定时器设置的时长内，设备端没有收到认证服务器的响应，设备端将重发认证请求报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[客户端认证超时定时器（]{style="font-family:宋体"}]{#struct_0_16124_x1536_1779486228}**[supp-timeout]{lang="EN-US"}**[）：当设备端向客户端发送了]{style="font-family:宋体"}[EAP-Request/MD5 Challenge]{lang="EN-US"}[请求报文后，设备端启动此定时器，若在该定时器设置的时长内，设备端没有收到客户端的响应，设备端将重发该报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户名请求超时定时器（]{style="font-family:宋体"}]{#struct_0_16124_x1536_1051521062}**[tx-period]{lang="EN-US"}**[）：当设备端向客户端发送]{style="font-family:宋体"}[EAP-Request/Identity]{lang="EN-US"}[请求报文后，设备端启动该定时器，若在该定时器设置的时长内，设备端没有收到客户端的响应，则设备端将重发认证请求报文。]{style="font-family:宋体"}[另外，为了兼容不主动发送]{lang="EN-US" style="font-family:宋体"}[EAPOL-Start]{lang="EN-US"}[连接请求报文的客户端，设备会定期组播]{lang="EN-US" style="font-family:宋体"}[EAP-Request/Identity]{lang="EN-US"}[请求报文来检测客户端。]{lang="EN-US" style="font-family:宋体"}**[tx-period]{lang="EN-US"}**[定义了该组播报文的发送时间间隔。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是，一般情况下，用户无需修改定时器的值，除非在一些特殊或恶劣的网络环境下，可以使用该命令调节交互进程。修改后的定时器值，可立即生效。]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1755205683}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1119306647}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x690986874}[设置认证服务器的超时定时器时长为]{style="font-family:宋体"}[150]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_x1800859716}

[\[Sysname\] dot1x timer server-timeout 150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x614042799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_334346051}
:::

::: {#784092545 .myid}
[]{#_Toc404792536}[]{#struct_0_16124_x1536_x1983628329}[]{#_Toc261334534}[]{#_Toc240689598}

**802.1X \-- 802.1X配置命令 \-- dot1x unicast-trigger**

------------------------------------------------------------------------

[**[dot1x unicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_x1348213435}[命令用来开启端口上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的单播触发功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo dot1x unicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_1836813858}[命令用来]{style="font-family:
宋体"}[关闭]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的单播触发功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1313568591}

[**[dot1x unicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_x1151460819}

[**[undo dot1x unicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_x351006271}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1814312448}

[[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_1398283278}[的单播触发功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_334411587}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x2058429077}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1760595745}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x68117973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_2028213290}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x214006537}

[[单播触发功能]{style="font-family:宋体"}]{#struct_0_16124_x1536_1122810608}[开启后，当端口收到源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[未知的报文时，主动向该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址发送单播认证报文来触发认证。若设备端在设置的客户端认证超时时间内（该时间由]{style="font-family:宋体"}**[dot1x timer supp-timeout]{lang="EN-US"}**[设置）没有收到客户端的响应，则重发该报文（重发次数由]{style="font-family:宋体"}**[dot1x retry]{lang="EN-US"}**[设置）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1158991144}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x1623349123}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的单播触发功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16124_x1536_334477123}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1x unicast-trigger]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1418506257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x1640501835}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x multicast-trigger]{lang="EN-US"}**]{#struct_0_16124_x1536_1675110298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x retry]{lang="EN-US"}**]{#struct_0_16124_x1536_1183724766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer]{lang="EN-US"}**]{#struct_0_16124_x1536_x1070708349}
:::

::: {#1121724801 .myid}
[]{#_Toc404792537}[]{#struct_0_16124_x1536_x1756229045}

**802.1X \-- 802.1X配置命令 \-- reset dot1x guest-vlan**

------------------------------------------------------------------------

[**[reset dot1x guest-vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_1011880220}[命令用来清除]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[内]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户，使其退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1907557407}

[**[reset dot1x guest-vlan]{lang="EN-US"}**[ **interface** *interface-type interface-number* \[ **mac-address** *mac-address* \]]{lang="EN-US"}]{#struct_0_16124_x1536_154894616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1756294581}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x1427858504}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_413792386}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1756753332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_x1430856527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_743277278}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_16124_x1536_x714021890}[：表]{style="font-family:宋体"}[示使指定端口上的用户]{style="font-family:宋体"}[退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:
宋体"}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_16124_x1536_x1756818868}[：表示使]{style="font-family:宋体"}[指定]{style="font-family:宋体"} [MAC]{lang="EN-US"}[地址的用户退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_238404130}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_x1707417716}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使得]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1-1-1]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户退出]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset dot1x guest-vlan interface gigabitethernet 1/0/1 mac-address 1-1-1]{lang="EN-US"}]{#struct_0_16124_x1536_x1756622260}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_290609185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x guest-vlan]{lang="EN-US"}**]{#struct_0_16124_x1536_1761381385}
:::

::: {#1770216554 .myid}
[]{#_Toc404792538}[]{#struct_0_16124_x1536_898837438}[]{#_Toc261334535}

**802.1X \-- 802.1X配置命令 \-- reset dot1x statistics**

------------------------------------------------------------------------

[**[reset dot1x]{lang="EN-US"}***[ ]{lang="EN-US"}***[statistics]{lang="EN-US"}**]{#struct_0_16124_x1536_x615488560}[命令用来清除]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_408516474}

[**[reset dot1x]{lang="EN-US"}***[ ]{lang="EN-US"}***[statistics]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **ap** *ap-name* \[ **radio** *radio-id* \] \| **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_16124_x1536_334542659}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x917929939}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16124_x1536_x545520834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1810558673}

[[network-admin]{lang="EN-US"}]{#struct_0_16124_x1536_27596161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16124_x1536_425351507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16124_x1536_342411567}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_16124_x1536_x1330473806}[：清除指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_16124_x1536_1826085521}[：清除指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。如果不指定该参数，则清除指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_16124_x1536_206949749}[：清除指定端口上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16124_x1536_1932359685}

[[如果不指定任何参数，则清除所有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_16124_x1536_334608195}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16124_x1536_x1436504086}

[[\# ]{lang="EN-US"}]{#struct_0_16124_x1536_1453029347}[清除端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dot1x statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_16124_x1536_156980562}[]{#_Toc33590707}[]{#_Toc34814443}

[]{#_Toc261334536}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16124_x1536_671783372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dot1x]{lang="EN-US"}**]{#struct_0_16124_x1536_x1384150316}

[ ]{lang="EN-US"}
:::
