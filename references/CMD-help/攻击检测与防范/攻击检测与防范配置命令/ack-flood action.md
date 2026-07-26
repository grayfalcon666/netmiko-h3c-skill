::: {#-559134163 .myid}
[]{#_Toc404793873}[]{#struct_0_12741_x1014_1932001112}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood action**

------------------------------------------------------------------------

[**[ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_639279231}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的全局处理行为。]{style="font-family:宋体"}

[**[undo ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_468603114}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1135159547}

[**[ack-flood action ]{lang="EN-US"}**[{ **client-verify** \| **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_139144396}

[**[undo ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_285014614}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x465937271}

[[不对检测到的]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_1940017633}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1566112976}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_881278183}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1578936845}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_365917171}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_808167379}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1623923751}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_1735430284}[：表示自动将受到]{style="font-family:宋体"}[攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添]{style="font-family:宋体"}[加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_1529681054}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_529894556}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1435346029}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_355544074}[参数的使用需要和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能的接口检测到]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x167961322}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1575705216}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的全局处理行为是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_714510965}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] ack-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x66305119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x370961165}**[threshold]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x826569149}**[detect ]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1588337328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify tcp ]{lang="EN-US"}**]{#struct_0_12741_x1014_171496803}**[enable]{lang="EN-US"}**
:::

::: {#1691237600 .myid}
[]{#struct_0_12741_x1014_996190422}[]{#_Toc404793874}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood detect**

------------------------------------------------------------------------

[**[ack-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1906621145}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[触发阈值和对]{style="font-family:
宋体"}[ACK flood]{lang="EN-US"}[攻击的]{style="font-family:
宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo ack-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1382500272}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_12741_x1014_9621275}

[**[ack-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1291729092}

[**[undo ack-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}]{#struct_0_12741_x1014_x2070043150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1199951307}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_2100899146}[地址配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_350302168}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1171484662}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1506243042}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1337241492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1773756231}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1319266168}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1556462666}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_978788449}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_238250086}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_391539478}[：指定]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x778973514}[：设置对]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击的处理行为。若不指定该参数，则表示采用]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的全局处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_665352061}[：表示自动将]{style="font-family:宋体"}[被攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_1200948935}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x1671500228}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_1723007030}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_639277555}

[[每[个攻击防范策略下可以同时对多个]{style="color:black"}]{style="font-family:宋体"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_1172420689}[地址配置]{style="font-family:宋体;
color:black"}[ACK flood]{lang="EN-US" style="color:black"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[使能]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x408931189}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1337288298}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1668135468}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x422602055}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] ack-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_316992211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x591449254}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_907611318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1486473107}**[threshold]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify tcp ]{lang="EN-US"}**]{#struct_0_12741_x1014_2138899027}**[enable]{lang="EN-US"}**
:::

::: {#-1396757925 .myid}
[]{#_Toc404793875}[]{#struct_0_12741_x1014_x728156207}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood detect non-specific**

------------------------------------------------------------------------

[**[ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x749893612}[命令用来对所有非受保护]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址开启]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1631886647}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x736941344}

[**[ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_625241688}

[**[undo ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x404862098}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1454372681}

[[未对所有非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_2046802654}[地址开启]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x322286308}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_628889472}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1823527581}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_203397198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x787901778}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1978989743}

[[对所有未配置具体攻击防范策略的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x277603727}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[ack-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[ack-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_599684954}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_119483594}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x251415174}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] ack-flood detect non-specific]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2030152583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1092488841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1919522522}**[detect ]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x665256072}
:::

::: {#1480177388 .myid}
[]{#_Toc404793876}[]{#struct_0_12741_x1014_x1301160898}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood threshold**

------------------------------------------------------------------------

[**[ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_412905802}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1490142131}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x83267753}

[**[ack-flood threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1085963007}

[**[undo ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_821853741}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x310209789}

[[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x775486928}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_230276642}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x230883198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1089230777}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1467054005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2053495240}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1153178139}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_581245415}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1887684372}

[[对于没有专门配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x581613163}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1518653586}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x650336487}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，即当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x189712739}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] ack-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_93674458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_2070907898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x858821061}**[detect ]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1931935576}
:::

::: {#501131650 .myid}
[]{#_Toc404793877}[]{#struct_0_12741_x1014_1984482544}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense apply policy**

------------------------------------------------------------------------

[**[attack-defense apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_493129140}[命令用来在接口上应用攻击防范策略。]{style="font-family:
宋体"}

[**[undo attack-defense apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x1929409601}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1974115024}

[**[attack-defense apply]{lang="EN-US"}**[ **policy** *policy-name*]{lang="EN-US"}]{#struct_0_12741_x1014_331780791}

[**[undo attack-defense apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x385191979}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1814542589}

[[接口上未应用任何攻击防范策略。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x572056748}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_835566904}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_365851635}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x365993644}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_296517494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1332930222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1124479695}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1469739288}[：攻击防范策略]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_901622506}

[[一个接口上只能应用一个攻击防范策略（可多次配置，最后一次配置的有效），但一个攻击防范策略可应用到多个接口上。]{style="font-family:宋体"}]{#struct_0_12741_x1014_1151107266}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x771754825}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_840553739}[将攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[应用到接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1575639680}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] attack-defense apply policy atk-policy-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1204282535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_1570678301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_1022922732}
:::

::: {#-415636442 .myid}
[]{#_Toc404793878}[]{#struct_0_12741_x1014_x1740039186}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense local apply policy**

------------------------------------------------------------------------

[**[attack-defense local apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_495917040}[命令用来在本机应用安全攻击防范策略。]{style="font-family:宋体"}

[**[undo attack-defense local apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_1896943533}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x478545484}

[**[attack-defense]{lang="EN-US"}**[ **local**]{lang="EN-US"}**[ apply policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x131571655}

[**[undo attack-defense local apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x2071826978}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_387753862}

[[本机未应用任何攻击防范策略。]{style="font-family:宋体"}]{#struct_0_12741_x1014_9555739}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1782072952}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1267961408}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2012596032}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2125078022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1663898476}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_342181024}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_52111858}[：攻击防范策略]{style="font-family:宋体"}[名称，为]{style="font-size:10.0pt;font-family:
宋体;color:black"}[1]{lang="EN-US" style="font-size:10.0pt;color:black"}[～]{style="font-size:10.0pt;font-family:宋体;color:black"}[31]{lang="EN-US" style="font-size:10.0pt;color:black"}[个字符的字符串，不区分大小写。]{style="font-size:10.0pt;
font-family:宋体;color:black"}[合法取值包括大写字母、小写字母、数字、特殊字符"]{style="font-family:
宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x797420874}

[[此功能主要用于交换机产品，缺省情况下交换机产品将需要转发的报文下发给硬件转发，只有目的地址是本机的报文才会由软件处理，但软件没有攻击防范功能。因此在交换机产品上，为处理针对本机的攻击，需要通过在本机上应用攻击防范策略来实现。]{style="font-family:宋体"}]{#struct_0_12741_x1014_1492395563}

[[对于非交换机产品，可以通过在本机上应用攻击方法策略提高对目的地址为本机的攻击报文的处理效率。]{style="font-family:宋体"}]{#struct_0_12741_x1014_151631519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本机只能应用一个攻击防范策略（可多次配置，最后一次配置的有效），但一个攻击防范策略除了可以应用到本机外，还可应用到多个接口上。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1298308337}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同时在接口和本机应用攻击防范策略时，目的地址是本机的报文到达设备后，将会被根据应用在接口上的策略和应用在本机的策略先后检测两次。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1556528202}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x222293323}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1595563653}[在本机应用攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1405549107}

[\[Sysname\] attack-defense local apply policy atk-policy-1 ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1243823290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_987024954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x1109640862}
:::

::: {#317991045 .myid}
[]{#_Toc404793879}[]{#struct_0_12741_x1014_x2031296943}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense policy**

------------------------------------------------------------------------

[**[attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x1377396735}[命令用来创建一个攻击防范策略，并进入攻击防范策略视图。]{style="font-family:宋体"}

[**[undo attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_247479525}[命令用来删除指定的攻击防范策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1172355153}

[**[attack-defense policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_12741_x1014_1889964792}

[**[undo attack-defense policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x11450176}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1073241573}

[[不存在任何攻击防范策略。]{style="font-family:宋体"}]{#struct_0_12741_x1014_946585775}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_380019356}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1182292300}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_836175142}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1006625259}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1394829994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1215381049}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x749959148}[：攻击防范策略]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1170352929}

[[无]{style="font-family:宋体"}]{#struct_0_12741_x1014_1659313762}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x368785564}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1972922476}[创建攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[，并进入攻击防范策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_867310873}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1780569639}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attack-defense apply policy]{lang="EN-US"}**]{#struct_0_12741_x1014_1814943199}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_229353014}
:::

::: {#321444552 .myid}
[]{#_Toc340488502}[]{#_Toc404793880}[]{#struct_0_12741_x1014_1978924207}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense signature log non-aggregate**

------------------------------------------------------------------------

[**[attack-defense signature log non-aggregate]{lang="EN-US"}**]{#struct_0_12741_x1014_x748812724}[命令用来指定对单包攻击防范日志]{style="font-family:宋体"}[非]{style="font-family:宋体"}[聚合输出。]{style="font-family:宋体"}

[**[undo attack-defense]{lang="EN-US"}**[ **signature log non-aggregate**]{lang="EN-US"}]{#struct_0_12741_x1014_x323934051}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1830104910}

[**[attack-defense signature log non-aggregate]{lang="EN-US"}**]{#struct_0_12741_x1014_x544652655}

[**[undo attack-defense]{lang="EN-US"}**[ **signature log non-aggregate**]{lang="EN-US"}]{#struct_0_12741_x1014_x1847777186}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1155675858}

[[单包攻击防范的日志信息经系统聚合后再输出。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x995369533}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_254741588}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1909316095}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1204286148}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_412840266}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_376506521}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_414880337}

[[对日志进行聚合输出是指，在一定时间内，对在同一个接口上检测到的相同攻击类型、相同攻击防范动作、相同的源]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x694175541}[目的地址以及属于相同]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的单包攻击的所有日志聚合成一条日志输出。通常不建议开启单包攻击防范的日志非聚合输出功能，因为在单包攻击较为频繁的情况下，它会导致大量日志信息输出，占用控制台的显示资源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1836155758}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_204393978}[开启对单包攻击防范日志的非聚合输出功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1065176951}

[\[Sysname\] attack-defense signature log non-aggregate]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x467398828}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_1063746573}**[detect]{lang="EN-US"}**
:::

::: {#1840935002 .myid}
[]{#_Toc404793881}[]{#struct_0_12741_x1014_x835869268}[]{#_Toc395519769}[]{#_Toc391478040}[]{#_Toc391037413}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense tcp fragment enable**

------------------------------------------------------------------------

[**[attack-defense tcp fragment enable]{lang="EN-US"}**]{#struct_0_12741_x1014_289477458}[命令用来开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击防范功能。]{style="font-family:宋体"}

[**[undo attack-defense tcp fragment enable]{lang="EN-US"}**]{#struct_0_12741_x1014_1175068273}[命令用来关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击防范功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1043304500}

[**[attack-defense tcp fragment enable]{lang="EN-US"}**]{#struct_0_12741_x1014_740271541}

[**[undo attack-defense tcp fragment enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x569290585}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1467490457}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x874097853}[分片攻击防范功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_196561053}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_740271538}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1378594658}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x436692202}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1774990325}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_740271537}

[[设备的包过滤功能一般是通过判断]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x1378594655}[首个分片中的五元组（源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、源端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、目的端口号、传输层协议号）信息来决定后续]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片是否允许通过。]{style="font-family:宋体"}[RFC 1858]{lang="EN-US"}[对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片报文进行了规定，认为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片报文中，首片报文中]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文长度小于]{style="font-family:宋体"}[20]{lang="EN-US"}[字节，或后续分片报文中分片偏移量等于]{style="font-family:宋体"}[8]{lang="EN-US"}[字节的报文为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击报文。这类报文可以成功绕过上述包过滤功能，对设备造成攻击。为防止这类攻击，可以在设备上开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击防范功能，对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击报文进行丢弃。]{style="font-family:宋体"}

[[需要注意的是，如果设备上开启了]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x33407675}[分片攻击防范功能，并应用了单包攻击防范策略，则]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击防范功能会先于单包攻击防范策略检测并处理入方向的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2078541708}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1834840381}[开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分片攻击防范功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_740271536}

[\[Sysname\] attack-defense tcp fragment enable]{lang="EN-US"}
:::

::::: {#1319926231 .myid}
[]{#_Toc404793882}[]{#struct_0_12741_x1014_1564938004}[]{#_Toc375152419}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x1710641716}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_655321111}
:::

[ ]{lang="EN-US"}

[**[blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1153243675}[命令用来开启接口上的黑名单过滤功能。]{style="font-family:宋体"}

[**[undo blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_1927452971}[命令用来关闭接口上的黑名单过滤功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1394154639}

[**[blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_1910450937}

[**[undo blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_1848771746}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_407418900}

[[接口上的黑名单过滤功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12741_x1014_1636501040}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1877565480}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_508235403}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_297548032}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x419092212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1858791554}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1931870040}

[[若全局的黑名单过滤功能处于开启状态，则所有接口上的黑名单过滤功能均处于开启状态。若全局的黑名单过滤功能处于关闭状态，则接口上的黑名单过滤功能由本命令决定是否开启。]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_1545671703}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1257879598}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_450581581}[开启接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的黑名单过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x496282492}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]blacklist enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x886227900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x585719271}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1286673616}
:::::

::::: {#823903005 .myid}
[]{#_Toc404793883}[]{#struct_0_12741_x1014_1081541268}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist global enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1600908132}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_1721354139}
:::

[ ]{lang="EN-US"}

[**[blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_365786099}[命令用来开启全局黑名单过滤功能。]{style="font-family:宋体"}

[**[undo blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_553523999}[命令用来关闭全局黑名单过滤功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x646171490}

[**[blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1525447332}

[**[undo blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1979663528}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_688045121}

[[全局黑名单过滤功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12741_x1014_552455685}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_818690573}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1745561302}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_129422332}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1771371292}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1575574144}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_729679563}

[[无]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_403807282}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_260827468}

[[使能全局黑名单过滤功能[表示开启所有接口下黑名单过滤功能。]{style="color:black"}]{style="font-family:宋体"}]{#struct_0_12741_x1014_1618340250}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1358038346}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x750466579}[开启全局黑名单过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1916679917}

[\[Sysname\] blacklist global enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_283522335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1232372496}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x990769210}
:::::

::::: {#-2050867008 .myid}
[]{#_Toc404793884}[]{#struct_0_12741_x1014_9490203}[]{#_Toc349981905}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x1576211447}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_248952337}
:::

[ ]{lang="EN-US"}

[**[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x783944070}[命令用来添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。]{style="font-family:宋体"}

[**[undo blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_444536759}[命令用来删除指定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1886644148}

[**[blacklist ip]{lang="EN-US"}***[ source-ip-address ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \] \[ **ds-lite-peer** *ds-lite-peer-address* \] \[ **timeout** *minutes* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x625194600}

[**[undo blacklist]{lang="EN-US"}***[ ]{lang="EN-US"}***[ip]{lang="EN-US"}***[ source-ip-address ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \] \[ **ds-lite-peer** *ds-lite-peer-address* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1132253592}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x250950034}

[[无]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_40170221}[黑名单表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1558180977}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1556593738}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2079348339}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x297794751}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x716965711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x307941167}

[*[source-ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1088185948}[：黑名单的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，用于匹配报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x569000354}[：黑名单所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该黑名单属于公网。]{style="font-family:宋体"}

[**[ds-lite-peer ]{lang="EN-US"}***[ds-lite-peer-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1723072560}[：黑名单所属的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[隧道对端地址。其中，]{style="font-family:宋体"}*[ds-lite-peer-address]{lang="EN-US"}*[表示黑名单的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[隧道]{style="font-family:宋体"}[B4]{lang="EN-US"}[端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[timeout ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_12741_x1014_x1658838948}[：黑名单表项的老化时间。其中，]{style="font-family:宋体"}*[minutes]{lang="EN-US"}*[表示老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为分钟。若不指定该参数，则表示该黑名单表项永不老化，除非用户手动将其删除。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x407184972}

[[通过执行]{style="font-family:宋体;color:black"}**[undo ]{lang="EN-US" style="color:black"}[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x2045983930}[命令可以删除用户手工添加的黑名单表项，动态生成的黑名单表项需通过执行]{style="font-family:宋体;color:black"}**[reset blacklist ip]{lang="EN-US" style="color:black"}**[命令删除。指定了老化时间的黑名单表项不会被保存在配置文件中，且保存配置重启后会被删除。可通过执行]{style="font-family:宋体;color:black"}**[display blacklist ip]{lang="EN-US" style="color:black"}**[命令查看当前所有生效的]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[黑名单表项。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x835133867}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x802007387}[将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[加入黑名单，指定其老化时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1172289617}

[\[Sysname\] blacklist ip 192.168.1.2 timeout 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_779951061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_177553058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x990497685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display blacklist ip]{lang="EN-US" style="color:black"}**]{#struct_0_12741_x1014_904829640}
:::::

::::: {#557500796 .myid}
[]{#_Toc404793885}[]{#struct_0_12741_x1014_314942974}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1230853455}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x2008184655}
:::

[ ]{lang="EN-US"}

[**[blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1668900890}[命令用来添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。]{style="font-family:宋体"}

[**[undo blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_884752348}[命令用来删除指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x750024684}

[**[blacklist ipv6]{lang="EN-US"}***[ source-ipv6-address ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \] \[ **timeout** *minutes* \]]{lang="EN-US"}]{#struct_0_12741_x1014_374153008}

[**[undo blacklist]{lang="EN-US"}***[ ]{lang="EN-US"}***[ipv6]{lang="EN-US"}***[ source-ipv6-address ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x973718608}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1277648330}

[[无]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x1729720342}[黑名单表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_605420148}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1237937481}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x55287628}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1162950514}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_224285350}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1978858671}

[*[source-ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_90804012}[：黑名单的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，用于匹配报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x342106828}[：黑名单所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该黑名单属于公网。]{style="font-family:宋体"}

[**[timeout ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_12741_x1014_x1918151385}[：黑名单表项的老化时间。其中，]{style="font-family:宋体"}*[minutes]{lang="EN-US"}*[表示老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为分钟。若不指定该参数，则表示该黑名单表项永不老化，除非用户手动将其删除。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1787683325}

[[通过执行]{style="font-family:宋体;color:black"}**[undo]{lang="EN-US" style="color:black"}[ blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1820328594}[命令可以删除用户手工添加的黑名单表项，动态生成的黑名单表项需通过执行]{style="font-family:宋体;color:black"}**[reset blacklist ipv6]{lang="EN-US" style="color:black"}**[命令删除。指定了老化时间的黑名单表项不会被保存在配置文件中，且保存配置重启后会被删除。可通过执行]{style="font-family:宋体;color:black"}**[display blacklist ipv6]{lang="EN-US" style="color:black"}**[命令查看当前所有生效的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[黑名单表项。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1593825492}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x59853442}[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[2012::12:25]{lang="EN-US"}[加入黑名单，指定其老化时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1483864179}

[\[Sysname\] blacklist ipv6 2012::12:25 timeout 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1529198373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_412774730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x616912217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_350808522}
:::::

::::: {#-1684324493 .myid}
[]{#_Toc404793886}[]{#struct_0_12741_x1014_717447788}[]{#_Toc340488497}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist logging enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x542154340}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x939901350}
:::

[ ]{lang="EN-US"}

[**[blacklist logging enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1737920934}[命令用来使能黑名单日志功能。]{style="font-family:
宋体"}

[**[undo blacklist logging enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x467595002}[命令用来关闭黑名单日志功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_649750572}

[**[blacklist logging enable]{lang="EN-US"}**]{#struct_0_12741_x1014_722507826}

[**[undo blacklist logging enable]{lang="EN-US"}**]{#struct_0_12741_x1014_1082310452}

[]{#_Toc325276362}[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1509980050}

[[黑名单日志功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1153309211}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1499047631}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1022112439}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1090577947}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1754346335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x949059639}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x236312098}

[[开启黑名单日志功能后，当增加黑名单、删除黑名单、扫描攻击防范动态添加黑名单、黑名单老化被删除时会有相应的日志输出，日志的内容主要包括黑名单的源]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_x1997943951}[地址、]{style="font-family:宋体;
color:black"}[DS-Lite]{lang="EN-US" style="color:black"}[隧道对端地址、]{style="font-family:宋体;color:black"}[VPN]{lang="EN-US" style="color:black"}[实例名称、添加或删除的原因以及老化时间等。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2051483433}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_598981446}[开启黑名单日志功能，并配置一条黑名单后，输出如下日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1931804504}

[\[Sysname\] blacklist logging enable]{lang="EN-US"}

[\[Sysname\] blacklist ip 192.168.100.12]{lang="EN-US"}

[%Mar 13 03:47:49:736 2013 Sysname BLS/5/BLS_ENTRY_ADD:SrcIPAddr(1003)=192.168.100.12; DSLiteTunnelPeer(1040)=\--; RcvVPNInstance(1041)=\--; TTL(1051)=; Reason(1052)=Configuration.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_412172711}[删除一条黑名单后，输出如下日志信息。]{style="font-family:宋体"}

[[\[Sysname\] undo blacklist ip 192.168.100.12]{lang="EN-US"}]{#struct_0_12741_x1014_x1024939354}

[%Mar 13 03:49:52:737 2013 Sysname BLS/5/BLS_ENTRY_DEL:SrcIPAddr(1003)=192.168.100.12; DSLiteTunnelPeer(1040)=\--; RcvVPNInstance(1041)=\--; Reason(1052)=Configuration.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1444997869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1127349162}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1287474548}
:::::

::::: {#-1368805486 .myid}
[]{#_Toc404793887}[]{#struct_0_12741_x1014_x1626191530}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify dns enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1383250397}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x10586197}
:::

[ ]{lang="EN-US"}

[**[client-verify dns enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x582261122}[命令用来在接口上使能]{style="font-family:
宋体"}[DNS]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[undo client-verify dns enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1728005920}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_365720563}

[**[client-verify dns enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x556673720}

[**[undo ]{lang="EN-US"}[client-verify dns enable]{lang="EN-US"}**]{#struct_0_12741_x1014_102536439}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_488726928}

[[接口上的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_12741_x1014_1777087084}[客户端验证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1637448709}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1486046866}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1668002599}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1976943366}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1193218162}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1453634585}

[[该功能一般应用在设备连接外部网络的接口上，用来保护内部网络的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_12741_x1014_1349014123}[服务器免受外部网络中非法客户端发起的]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击。当设备监测到某服务器受到了]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击时，会根据配置的攻击防范处理行为启动相应的防范措施。若防范处理行为配置为对攻击报文进行客户端验证（指定参数为]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[），则设备会将该服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项中（可通过]{style="font-family:宋体"}**[display client-verify dns protected ip]{lang="EN-US"}**[命令查看），对后续新建]{style="font-family:宋体"}[DNS query]{lang="EN-US"}[请求连接的协商报文进行合法性检查，过滤非法客户端发起的]{style="font-family:宋体"}[DNS query]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1575508608}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1527156619}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x2043786615}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] client-verify dns enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1983211767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify dns protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1068001040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify dns protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1340271694}
:::::

::::: {#1321250095 .myid}
[]{#_Toc404793888}[]{#struct_0_12741_x1014_284619105}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify http enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x1354781814}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x697501973}
:::

[ ]{lang="EN-US"}

[**[client-verify http enable]{lang="EN-US"}**]{#struct_0_12741_x1014_933736815}[命令用来在接口上使能]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[undo client-verify http enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x270215141}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_12741_x1014_9424667}

[**[client-verify http enable]{lang="EN-US"}**]{#struct_0_12741_x1014_276738158}

[**[undo ]{lang="EN-US"}[client-verify http enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x803357878}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x932622631}

[[接口上的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_12741_x1014_1814481928}[客户端验证]{style="font-family:宋体"}[功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x113274872}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1909021600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1781721537}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x369648711}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1666940077}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1008315735}

[[该功能一般应用在设备连接外部网络的接口上，用来保护内部网络的服务器免受外部网络中非法客户端发起的]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1164546050}[攻击。当设备监测到某服务器受到了]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击时，会根据配置的攻击防范处理行为启动相应的防范措施。若防范处理行为配置为对攻击报文进行客户端验证（指定参数为]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[），则设备会将该服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项中（可通过]{style="font-family:宋体"}**[display client-verify http protected ip]{lang="EN-US"}**[命令查看），对后续新建]{style="font-family:宋体"}[HTTP get]{lang="EN-US"}[请求连接的协商报文进行合法性检查，过滤非法客户端发起的]{style="font-family:宋体"}[HTTP get]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1556659274}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x292330014}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x855169595}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] client-verify http enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1948966340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify http protected]{lang="EN-US"}**]{#struct_0_12741_x1014_860005105}**[ ip]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_1762898448}**[http]{lang="EN-US"}[ protected ip]{lang="EN-US"}**
:::::

::::: {#1430292971 .myid}
[]{#_Toc404793889}[]{#struct_0_12741_x1014_1421848047}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify protected ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_35706804}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x1271126774}
:::

[ ]{lang="EN-US"}

[**[client-verify protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1009583038}[命令用来配置]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[类型客户端验证]{style="font-family:宋体"}[的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo client-verify protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1105678677}[命令用来删除指定的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1172224081}

[**[client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected ip**]{lang="EN-US"}[ *destination-ip-address* \[ **vpn-instance** *vpn-instance-name* \] \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1995438163}

[**[undo client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected ip**]{lang="EN-US"}*[ destination-ip-address ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \] \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1633711818}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_263476287}

[[不存在任何]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_226816439}[类型客户端验证]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即]{style="font-family:宋体"}[客户端验证功能]{style="font-family:宋体"}[未保护任何]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x154265251}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x626480421}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_288358745}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x357119768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x140500419}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2085023440}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_x895185278}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_828605294}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_x1988712503}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[*[destination-ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1644391477}[：指定受]{style="font-family:宋体"}[客户端验证]{style="font-family:宋体"}[保护的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，即会对向该目的地址发送的连接请求进行代理。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x750090220}[：受]{style="font-family:宋体"}[客户端验证]{style="font-family:宋体"}[保护]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址属于公网。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x815533658}[：指定受]{style="font-family:宋体"}[客户端验证]{style="font-family:宋体"}[保护的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。若不指定该参数，对于]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[端口]{style="font-family:宋体"}[53]{lang="EN-US"}[的]{style="font-family:宋体"}[DNS query]{lang="EN-US"}[连接请求做代理]{style="font-family:宋体"}[；对于]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[端]{style="font-family:宋体"}[口]{style="font-family:宋体"}[80]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[连接请求做代理]{style="font-family:宋体"}[；对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[所有端口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求做代理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x168594254}

[[可通过多次执行本命令添加多个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_1719071638}[类型客户端验证受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x823029620}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x112387607}[配置一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.5]{lang="EN-US"}[、受保护端口号为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1149024553}

[[\[Sysname\] client-verify tcp protected ip 2.2.2.5 port 25]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x462490261}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1047060150}[配置一个]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.5]{lang="EN-US"}[、受保护端口号为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1978793135}

[[\[Sysname\] client-verify dns protected ip 2.2.2.5 port 50]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1904236220}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_746252071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_538720676}
:::::

::::: {#-1649639928 .myid}
[]{#_Toc404793890}[]{#struct_0_12741_x1014_917589984}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify protected ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_679229992}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_678699380}
:::

[ ]{lang="EN-US"}

[**[client-verify protected ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x2072123912}[命令用来配置]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[类型客户端验证]{style="font-family:宋体"}[的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo client-verify protected ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_807660483}[命令用来删除指定的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1507991741}

[**[client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected ipv6** ]{lang="EN-US"}*[destination-ipv6-address ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \] \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x231762079}

[**[undo client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected ipv6**]{lang="EN-US"}[ *destination-ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_12741_x1014_412709194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1848208524}

[[不存在任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_1527335758}[类型客户端验证]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即]{style="font-family:宋体"}[客户端验证功能]{style="font-family:宋体"}[未保护任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1475401268}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1400389658}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1692444183}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1204390957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_637543434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1238231406}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_1320115716}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_407885297}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_2039154637}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[*[destination-ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1756520254}[：指定受]{style="font-family:
宋体"}[客户端验证]{style="font-family:宋体"}[保护的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址，即会对向该目的地址发送的连接请求进行代理。]{style="font-family:宋体"}[对于受]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，发送的是]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求；对于受]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，发送的是]{style="font-family:宋体"}[DNS query]{lang="EN-US"}[请求；对于受]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，发送的是]{style="font-family:宋体"}[HTTP get]{lang="EN-US"}[连接请求。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x1778612811}[：受]{style="font-family:宋体"}[客户端验证]{style="font-family:宋体"}[保]{style="font-family:宋体"}[护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大]{style="font-family:宋体"}[小写。若不指定该参数，则表示]{style="font-family:宋体"}[该受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址属]{style="font-family:宋体"}[于公网。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1153374747}[：指定受]{style="font-family:宋体"}[客户端验证]{style="font-family:宋体"}[保护的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。若不指定该参数，对于]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[端口]{style="font-family:宋体"}[53]{lang="EN-US"}[的]{style="font-family:宋体"}[DNS query]{lang="EN-US"}[连接请求做代理]{style="font-family:宋体"}[；对于]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[端]{style="font-family:宋体"}[口]{style="font-family:宋体"}[80]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[连接请求做代理]{style="font-family:宋体"}[；对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示对]{style="font-family:宋体"}[所有端口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求做代理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1471251865}

[[可通过多次执行本命令添加多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_94107607}[类型客户端验证受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1539176015}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1010379716}[配置一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2013::12]{lang="EN-US"}[、受保护端口号为]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x437897850}

[[\[Sysname\] client-verify tcp protected ipv6 2013::12 port 23]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x603617983}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_99700604}[配置一个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2013::12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1246878158}

[[\[Sysname\] client-verify http protected ipv6 2013::12]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x507743961}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1312128235}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify protected ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1407822301}
:::::

::::: {#459967431 .myid}
[]{#_Toc404793891}[]{#struct_0_12741_x1014_1163213228}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify tcp enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1931738968}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x1959020136}
:::

[ ]{lang="EN-US"}

[**[client-verify tcp enable]{lang="EN-US"}**]{#struct_0_12741_x1014_514236843}[命令用来在接口上使能]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[undo client-verify tcp enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x1468016688}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1111639297}

[**[client-verify tcp enable]{lang="EN-US"}**[ \[ **mode** { **syn-cookie** \| **safe-reset** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1584977389}

[**[undo ]{lang="EN-US"}[client-verify tcp enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x639573061}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_678319892}

[[接口上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x1789676367}[客户端验证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1199974910}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_2025313879}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1443330934}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x321540904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_39059769}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_365655027}

[**[mode]{lang="EN-US"}**]{#struct_0_12741_x1014_958995700}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的工作模式。不指定该参数时，则表示工作模式为]{style="font-family:宋体"}**[syn-cookie]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[syn-cookie]{lang="EN-US"}**]{#struct_0_12741_x1014_x995953613}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的工作模式为]{style="font-family:宋体"}[syn-cookie]{lang="EN-US"}[，即开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证双向代理。]{style="font-family:宋体"}

[**[safe-reset]{lang="EN-US"}**]{#struct_0_12741_x1014_x2126133062}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的工作模式为]{style="font-family:宋体"}[safe-reset]{lang="EN-US"}[，即开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证单向代理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1720896777}

[[该功能一般应用在设备连接外部网络的接口上，用来保护内部网络的服务器免受外部网络中非法客户端发起的]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1425913432}[、]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[、]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[、]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[、]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击。当设备监测到某服务器受到了]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[、]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[、]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[、]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[、]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击时，会根据配置的攻击防范处理行为启动相应的防范措施。若防范处理行为配置为对攻击报文进行客户端验证（指定参数为]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[），则设备会将该服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项中（可通过]{style="font-family:宋体"}**[display client-verify tcp protected ip]{lang="EN-US"}**[命令查看），并按照指定的单向或双向工作模式，对后续新建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的协商报文进行合法性检查，过滤非法客户端发起的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接报文。]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能]{style="font-family:宋体"}[支持两种代理模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单向代理模式（]{style="font-family:宋体"}]{#struct_0_12741_x1014_x467140247}**[safe-reset]{lang="EN-US"}**[）：是指仅对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的正向报文进行处理。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[双向代理模式（]{style="font-family:宋体"}]{#struct_0_12741_x1014_x464183107}**[syn-cookie]{lang="EN-US"}**[）：是指对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的正向和反向报文都进行处理。]{style="font-family:宋体"}

[[用户可以根据实际的组网情况选择不同的代理模式。若从客户端发出的报文经过使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_768966290}[客户端验证]{style="font-family:宋体"}[功能的设备时]{style="font-family:宋体"}[，而从服务器端发出的报文不经过该]{style="font-family:宋体"}[设备]{style="font-family:宋体"}[，此时只能使用单向代理模式；从客户端发出的报文经和从服务器端发出的报文都经过使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能的设备时]{style="font-family:宋体"}[，此时可以使用单向代理模式，也可以使用双向代理模式；代理只适合在入接口使能，否则无法建立正常连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1803711375}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1015846955}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}[功能，并指定工作模式为]{style="font-family:宋体"}[双向代理]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1575443072}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] client-verify tcp enable mode syn-cookie]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x821712612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify tcp protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1238624946}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify tcp protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1013235095}
:::::

::: {#-1034685090 .myid}
[]{#_Toc404793892}[]{#struct_0_12741_x1014_x505913562}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense flood statistics ip**

------------------------------------------------------------------------

[**[display attack-defense flood statistics ip]{lang="EN-US"}**]{#struct_0_12741_x1014_264731945}[命令用来显示]{style="font-family:宋体"}[IPv4 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1926475743}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_416655747}

[**[display attack-defense ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **statistics ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **interface** *interface-type interface-number* \| **local** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1874161454}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x1032798126}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **statistics ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **interface** *interface-type interface-number* \| **local** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x880455455}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x1797878796}[模式：]{style="font-family:宋体"}

[**[display attack-defense ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **statistics ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **interface** *interface-type interface-number* \| **local** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x255899045}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_12741_x1014_9359131}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x176774750}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2010699019}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1632884444}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_690183331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_139301587}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_2074064515}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1567750899}

[**[ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1230721905}[：显示]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[dns-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1581604833}[：显示]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[fin-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x653701260}[：显示]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1556724810}[：显示所有类型的]{style="font-family:宋体"}[IPv4 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[http-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x67987898}[：显示]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[icmp-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1307453833}[：显示]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[rst-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x508055860}[：显示]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[syn-ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x67529146}[：显示]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[syn-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1643104382}[：显示]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[udp-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_521986337}[：显示]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1240700133}[：]{style="font-family:宋体"}[显示指定目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击]{style="font-family:宋体"}[防范]{style="font-family:宋体"}[统计信息。]{style="font-family:宋体"}[若不指定该参数，则显示指定接口或本机上的所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_1085883256}[：指]{style="font-family:宋体"}[定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址所]{style="font-family:宋体"}[属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示]{style="font-family:宋体"}[该]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_964624850}[：显示指定接口的]{style="font-family:宋体;color:black"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:
宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_12741_x1014_x1564866953}[：显示本机上进行检测的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12741_x1014_176389621}[：显示指定]{style="font-family:宋体"}[单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号]{style="font-family:宋体"}[。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1172158545}[：显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有成员设备或指定全局接口在所有成员设备上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2099423057}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有成员]{style="font-family:宋体"}[设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[或]{style="font-family:宋体"}[指定全局接口在所有成员设]{style="font-family:宋体"}[备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1171951636}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1602481884}[：显示指定单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机所有单板或指定全局接口在所有单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_1654374212}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_1899320006}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[符合指定条件的]{style="font-family:宋体"}[被进行]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址数目]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1694718160}

[[由于]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1105507181}[攻击不关心源地址，因此本命令显示的是对指定目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的攻击防范统计信息。]{style="font-family:宋体"}

[[若不指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_12741_x1014_1319984645}[和]{style="font-family:宋体"}**[local]{lang="EN-US"}**[参数，则显示所有接口以及本机上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2117435680}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_583751409}[显示所有类型的]{style="font-family:宋体"}[IPv4 flood]{lang="EN-US"}[攻击防范统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_238694921}

[[IP address      VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_x750155756}

[192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295]{lang="EN-US"}

[201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111]{lang="EN-US"}

[192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222]{lang="EN-US"}

[201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x25318663}[显示所有类型的]{style="font-family:宋体"}[IPv4 flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip]{lang="EN-US"}]{#struct_0_12741_x1014_x68053433}

[slot 1:]{lang="EN-US"}

[IP address      VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295]{lang="EN-US"}

[201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111]{lang="EN-US"}

[192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222]{lang="EN-US"}

[201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[slot 2:]{lang="EN-US"}

[IP address      VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295]{lang="EN-US"}

[201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111]{lang="EN-US"}

[192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222]{lang="EN-US"}

[201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1036565323}[显示所有类型的]{style="font-family:宋体"}[IPv4 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x68118969}

[[Slot 1 in chassis 1:]{lang="EN-US"}]{#struct_0_12741_x1014_39457824}

[IP address      VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295]{lang="EN-US"}

[201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111]{lang="EN-US"}

[192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222]{lang="EN-US"}

[201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[slot 2 in chassis 2:]{lang="EN-US"}

[IP address      VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295]{lang="EN-US"}

[201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111]{lang="EN-US"}

[192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222]{lang="EN-US"}

[201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1413751337}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址数目。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x68250041}

[Totally 2 flood entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1593181157}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址数目。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x67791289}

[Slot 1:]{lang="EN-US"}

[Totally 2 flood entries.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 2 flood entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1536133552}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址数目。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip count]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x67856825}

[[Slot 1 in chassis 1:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_155999626}

[[Totally 2 flood entries.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1244633011}

[[Slot 2 in chassis 2:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_375742613}

[[Totally 2 flood entries.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x67922361}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1742760404}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址数目。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x538931432}

[CPU 0 on slot 1:]{lang="EN-US"}

[Totally 2 flood entries.]{lang="EN-US"}

[CPU 1 on slot 2:]{lang="EN-US"}

[Totally 2 flood entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x2113376675}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址数目。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ip count]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_2088734343}

[[CPU 0 on slot 1 in chassis 1:]{lang="EN-US"}]{#struct_0_12741_x1014_x904250046}

[Totally 2 flood entries.]{lang="EN-US"}

[CPU 1 on slot 2 in chassis 2:]{lang="EN-US"}

[Totally 2 flood entries.]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display attack-defense flood statistics ip]{lang="EN-US"}]{#struct_0_12741_x1014_352158161}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1002546163}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1787076700}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_618029223}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_231239796}

[[被检测的目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x105616230}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地]{style="font-family:宋体"}[址]{style="font-family:宋体"}

[[VPN ]{lang="EN-US"}]{#struct_0_12741_x1014_365589491}

[[目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x831698757}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地]{style="font-family:宋体"}[址所属]{style="font-family:宋体"}[的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实]{style="font-family:宋体"}[例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Detected on]{lang="EN-US"}]{#struct_0_12741_x1014_x67987897}

[[进行攻击检测的位置，包括接口]{style="font-family:宋体"}]{#struct_0_12741_x1014_x67529145}[和本机（]{style="font-family:
  宋体"}[Local]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Detect type]{lang="EN-US"}]{#struct_0_12741_x1014_x585529424}

[[检测的]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1680020623}[攻击类型]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12741_x1014_1709660800}

[[接口或本机是否处于攻击状态，可包括以下取值：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1782897753}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attacked]{lang="EN-US"}]{#struct_0_12741_x1014_1698059203}[：受攻击状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_12741_x1014_825048889}[：正常状态（当前并未受到攻击）]{style="font-family:宋体"}

[[PPS]{lang="EN-US"}]{#struct_0_12741_x1014_x1142430969}

[[指定的目的]{style="font-family:宋体"}[Pv4]{lang="EN-US"}]{#struct_0_12741_x1014_1085334927}[地址收到]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击报文的速率（单位为]{style="font-family:宋体"}[报文每秒]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_1779780099}

[[接口或本机丢弃的]{style="font-family:宋体"}]{#struct_0_12741_x1014_143576859}[flood]{lang="EN-US"}[攻击报文数目]{style="font-family:宋体"}

[[Totally 2 flood entries]{lang="EN-US"}]{#struct_0_12741_x1014_293714315}

[[被检测的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x1561035569}[地址数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-42229465 .myid}
[]{#_Toc404793893}[]{#struct_0_12741_x1014_x1897457855}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense flood statistics ipv6**

------------------------------------------------------------------------

[**[display attack-defense flood statistics ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1855181364}[命令用来显示]{style="font-family:宋体"}[IPv6 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1636216921}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_495856676}

[**[display attack-defense ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-flood** \| **syn-ack-flood** \| **udp-flood** } **statistics ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **interface** *interface-type interface-number* \| **local** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x416983915}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x1422507082}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-flood** \| **syn-ack-flood** \| **udp-flood** } **statistics ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **interface** *interface-type interface-number \|* **local** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x305552237}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x356513780}[模式：]{style="font-family:宋体"}

[**[display attack-defense ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-flood** \| **syn-ack-flood** \| **udp-flood** } **statistics ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **interface** *interface-type interface-number \|* **local** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_232297633}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_644693213}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_578305471}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1517078310}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1036864605}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1626445882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_646513077}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1555286553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1306376273}

[**[ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1448545602}[：显示指定]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[**[dns-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x729356958}[：显示指定]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[**[fin-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1265887269}[：显示指定]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[**[flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x952224466}[：显示所有类型的]{style="font-family:宋体"}[IPv6 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[http-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x68118968}[：显示]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[icmpv6-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1956192117}[：显示指定]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[**[rst-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1816577091}[：显示指定]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[**[syn-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_803925993}[：显示指定]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[**[syn-ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_39457825}[：显示]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[udp-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x529965274}[：显示指定]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[类型统计信息。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1660724200}[：]{style="font-family:宋体"}[显示指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击]{style="font-family:宋体"}[防范]{style="font-family:宋体"}[统计信息。]{style="font-family:宋体"}[若不指定该参数，则显示指定接口或本机上的所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[vpn]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x2125097428}[：指]{style="font-family:宋体"}[定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址所]{style="font-family:宋体"}[属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示]{style="font-family:宋体"}[该]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x615938028}[：显示指定接口的]{style="font-family:宋体;color:black"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:
宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_12741_x1014_1653432536}[：显示本机上进行检测的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12741_x1014_2007857115}[：显示指定]{style="font-family:宋体"}[单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号]{style="font-family:宋体"}[。该参数仅在指定本机或指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1710394317}[：显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有成员设备或指定全局接口在所有成员设备上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x629525834}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[或指定全局接口在所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_709830133}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1428839576}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。]{style="font-family:宋体"}[若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x356529622}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x585424219}[：]{style="font-family:宋体"}[仅显示]{style="font-family:宋体"}[符合指定条件的]{style="font-family:宋体"}[被进行]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址数目]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1249908566}

[[由于]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1814108279}[攻击不关心源地址，因此本命令显示的是对指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的攻击防范统计信息。]{style="font-family:宋体"}

[[若不指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_12741_x1014_1319919110}[和]{style="font-family:宋体"}**[local]{lang="EN-US"}**[参数，则显示所有接口以及本机上的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_366150602}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1846343858}[显示所有类型的]{style="font-family:宋体"}[IPv6 flood]{lang="EN-US"}[攻击防范统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_2112945327}

[IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295]{lang="EN-US"}

[1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222]{lang="EN-US"}

[1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1169730262}[显示所有类型的]{style="font-family:宋体"}[IPv6 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ipv6]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x995486671}

[[Slot 1:]{lang="EN-US"}]{#struct_0_12741_x1014_546861386}

[IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295]{lang="EN-US"}

[1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222]{lang="EN-US"}

[1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295]{lang="EN-US"}

[1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222]{lang="EN-US"}

[1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_848601441}[显示所有类型的]{style="font-family:宋体"}[IPv6 flood]{lang="EN-US"}[攻击防范统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1320969064}

[Slot 1 in chassis 1:]{lang="EN-US"}

[IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295]{lang="EN-US"}

[1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222]{lang="EN-US"}

[1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[Slot 2 in chassis 2:]{lang="EN-US"}

[IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped]{lang="EN-US"}

[2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295]{lang="EN-US"}

[1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222]{lang="EN-US"}

[1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111]{lang="EN-US"}

[1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1909410862}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址数目。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x67791288}

[Totally 5 flood entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1787532844}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址数目。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x1750654575}

[Slot 1:]{lang="EN-US"}

[Totally 5 flood entries.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 5 flood entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_2066168154}[显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击检测的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址数目。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood statistics ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_1380098573}

[Slot 1 in chassis 1:]{lang="EN-US"}

[Totaly 5 flood entries.]{lang="EN-US"}

[Slot 2 in chassis 2:]{lang="EN-US"}

[Totally 5 flood entries.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display attack-defense flood]{lang="EN-US"}[ statistics ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_298040036}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x974099793}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_x41063565}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x1082576717}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12741_x1014_x536736552}

[[被检测的目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1572341374}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地]{style="font-family:宋体"}[址]{style="font-family:宋体"}

[[VPN]{lang="EN-US"}]{#struct_0_12741_x1014_189220408}

[[目]{style="font-family:宋体"}]{#struct_0_12741_x1014_2109746003}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实]{style="font-family:宋体"}[例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Detected on]{lang="EN-US"}]{#struct_0_12741_x1014_x67529144}

[[进行攻击检测的位置，包括接口]{style="font-family:宋体"}]{#struct_0_12741_x1014_x67594680}[和本机（]{style="font-family:
  宋体"}[Local]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Detect type]{lang="EN-US"}]{#struct_0_12741_x1014_499807219}

[[检测的]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1877367421}[攻击类型]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12741_x1014_x1923173034}

[[接口或本机是否处于攻击状态，可包括以下取值：]{style="font-family:宋体"}]{#struct_0_12741_x1014_1182020676}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attacked]{lang="EN-US"}]{#struct_0_12741_x1014_1688631159}[：受攻击状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_12741_x1014_x538580025}[：正常状态（当前并未受到攻击）]{lang="EN-US" style="font-family:宋体"}

[[PPS]{lang="EN-US"}]{#struct_0_12741_x1014_1358553717}

[[指定的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_1709595264}[地址收到报文的速率（单位]{style="font-family:宋体"}[为报文每秒]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_x2139919797}

[[接口或本机丢弃的]{style="font-family:宋体"}]{#struct_0_12741_x1014_401959042}[flood]{lang="EN-US"}[攻击报文数目]{style="font-family:宋体"}

[[Totally 2 flood entries]{lang="EN-US"}]{#struct_0_12741_x1014_x2133987257}

[[被检测的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1925341280}[地址数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-548584350 .myid}
[]{#_Toc404793894}[]{#struct_0_12741_x1014_485601857}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense policy**

------------------------------------------------------------------------

[**[display attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_143511323}[用来显示攻击防范策略的配置信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_325552534}

[**[display attack-defense policy ]{lang="EN-US"}**[\[ *policy-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1343957527}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1031284988}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x655211799}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1458208068}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1666566701}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1674710730}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1557121886}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1174201612}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2109357907}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x670225068}[：攻击防范策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写]{style="font-family:宋体"}[。若不指定该参数，则表示显示所有攻击防范策略的摘要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x915120217}

[[本命令显示的内容主要包括各类型攻击防范的使能情况、对攻击报文的处理方式和相关的阈值参数。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1544629733}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1422572618}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_2041274120}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc]{lang="EN-US"}]{#struct_0_12741_x1014_x616003564}

[          Attack-defense Policy Information]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Policy name                        : abc]{lang="EN-US"}

[Applied list                       : GE1/0/1]{lang="EN-US"}

[                                     Vlan-int1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Exempt IPv4 ACL]{lang="EN-US"}[：]{style="font-family:宋体"}[                  : Not configured]{lang="EN-US"}

[Exempt IPv6 ACL]{lang="EN-US"}[：]{style="font-family:宋体"}[                  : vip]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Actions: CV-Client verify  BS-Block source  L-Logging  D-Drop  N-None]{lang="EN-US"}

[ ]{lang="EN-US"}

[Signature attack defense configuration:]{lang="EN-US"}

[Signature name                     Defense      Level             Actions]{lang="EN-US"}

[Fragment                           Enabled      Info              L]{lang="EN-US"}

[Impossible                         Enabled      Info              L]{lang="EN-US"}

[Teardrop                           Disabled     Info              L]{lang="EN-US"}

[Tiny fragment                      Disabled     Info              L]{lang="EN-US"}

[IP option abnormal                 Disabled     Info              L]{lang="EN-US"}

[Smurf                              Disabled     Info              N]{lang="EN-US"}

[Traceroute                         Disabled     Medium            L,D]{lang="EN-US"}

[Ping of death                      Disabled     Low               L]{lang="EN-US"}

[Large ICMP                         Disabled     Medium            L,D]{lang="EN-US"}

[  Max length                       4000 bytes]{lang="EN-US"}

[Large ICMPv6                       Disabled     Low               L]{lang="EN-US"}

[  Max length                       4000 bytes]{lang="EN-US"}

[TCP invalid flags                  Disabled     medium            L,D]{lang="EN-US"}

[TCP null flag                      Disabled     Low               L]{lang="EN-US"}

[TCP all flags                      Enabled      Info              L]{lang="EN-US"}

[TCP SYN-FIN flags                  Disabled     Info              L]{lang="EN-US"}

[TCP FIN only flag                  Enabled      Info              L]{lang="EN-US"}

[TCP Land                           Disabled     Info              L]{lang="EN-US"}

[Winnuke                            Disabled     Info              L]{lang="EN-US"}

[UDP Bomb                           Disabled     Info              L]{lang="EN-US"}

[UDP Snork                          Disabled     Info              L]{lang="EN-US"}

[UDP Fraggle                        Enabled      Info              L]{lang="EN-US"}

[IP option record route             Disabled     Info              L]{lang="EN-US"}

[IP option internet timestamp       Enabled      Info              L]{lang="EN-US"}

[IP option security                 Disabled     Info              L]{lang="EN-US"}

[IP option loose source routing     Enabled      Info              L]{lang="EN-US"}

[IP option stream ID                Disabled     Info              L]{lang="EN-US"}

[IP option strict source routing    Disabled     Info              L]{lang="EN-US"}

[IP option route alert              Disabled     Info              L]{lang="EN-US"}

[ICMP echo request                  Disabled     Info              L]{lang="EN-US"}

[ICMP echo reply                    Disabled     Info              L]{lang="EN-US"}

[ICMP source quench                 Disabled     Info              L]{lang="EN-US"}

[ICMP destination unreachable       Enabled      Info              L]{lang="EN-US"}

[ICMP redirect                      Enabled      Info              L]{lang="EN-US"}

[ICMP time exceeded                 Enabled      Info              L]{lang="EN-US"}

[ICMP parameter problem             Disabled     Info              L]{lang="EN-US"}

[ICMP timestamp request             Disabled     Info              L]{lang="EN-US"}

[ICMP timestamp reply               Disabled     Info              L]{lang="EN-US"}

[ICMP information request           Disabled     Info              L]{lang="EN-US"}

[ICMP information reply             Disabled     Medium            L,D]{lang="EN-US"}

[ICMP address mask request          Disabled     Medium            L,D]{lang="EN-US"}

[ICMP address mask reply            Disabled     Medium            L,D]{lang="EN-US"}

[ICMPv6 echo request                Enabled      Medium            L,D]{lang="EN-US"}

[ICMPv6 echo reply                  Disabled     Medium            L,D]{lang="EN-US"}

[ICMPv6 group membership query      Disabled     Medium            L,D]{lang="EN-US"}

[ICMPv6 group membership report     Disabled     Medium            L,D]{lang="EN-US"}

[ICMPv6 group membership reduction  Disabled     Medium            L,D]{lang="EN-US"}

[ICMPv6 destination unreachable     Enabled      Medium            L,D]{lang="EN-US"}

[ICMPv6 time exceeded               Enabled      Medium            L,D]{lang="EN-US"}

[ICMPv6 parameter problem           Disabled     Medium            L,D]{lang="EN-US"}

[ICMPv6 packet too big              Disabled     Medium            L,D]{lang="EN-US"}

[ ]{lang="EN-US"}

[Scan attack defense configuration:]{lang="EN-US"}

[ Defense: Disabled]{lang="EN-US"}

[ Level: Medium]{lang="EN-US"}

[ Actions: L]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flood attack defense configuration:]{lang="EN-US"}

[Flood type      Global thres(pps)  Global actions  Service ports   Non-specific]{lang="EN-US"}

[SYN flood       1000(default)      -               -               Disabled]{lang="EN-US"}

[ACK flood       1000(default)      -               -               Enabled]{lang="EN-US"}

[SYN-ACK flood   1000(default)      -               -               Disabled]{lang="EN-US"}

[RST flood       200                -               -               Enabled]{lang="EN-US"}

[FIN flood       1000(default)      L,D             -               Disabled]{lang="EN-US"}

[UDP flood       1000(default)      -               -               Disabled]{lang="EN-US"}

[ICMP flood      1000(default)      -               -               Disabled]{lang="EN-US"}

[ICMPv6 flood    1000(default)      CV              -               Disabled]{lang="EN-US"}

[DNS flood       10000              -               30,61 to 62     Enabled]{lang="EN-US"}

[HTTP flood      10000              -               80,8080         Enabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flood attack defense for protected IP addresses:]{lang="EN-US"}

[ Address                 VPN instance Flood type    Thres(pps)  Actions Ports]{lang="EN-US"}

[ 1::1                    \--           FIN-FLOOD     10          L,D     -]{lang="EN-US"}

[ 192.168.1.1             A01234567890 SYN-ACK-FLOOD 10          -       -]{lang="EN-US"}

[                         123456789012    ]{lang="EN-US"}

[                         3456789]{lang="EN-US"}

[ 1::1                    \--           FIN-FLOOD     -           L       -]{lang="EN-US"}

[ 2013:2013:2013:2013:    A0123456789  DNS-FLOOD     100         L,CV    53]{lang="EN-US"}

[ 2013:2013:2013:2013]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display attack-defense policy]{lang="EN-US"}]{#struct_0_12741_x1014_345011173}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x980521077}[[字段]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1629837352}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12741_x1014_x934076268}

[[Policy name]{lang="EN-US"}]{#struct_0_12741_x1014_x248448905}

[[攻击防范策略名称]{style="font-family:宋体"}]{#struct_0_12741_x1014_68859430}

[[Applied list]{lang="EN-US"}]{#struct_0_12741_x1014_211939900}

[[攻击防范策略应用的对象列表，包括接口名称和本机（]{style="font-family:宋体"}[Local]{lang="EN-US"}]{#struct_0_12741_x1014_338896958}[）]{style="font-family:宋体"}

[[Exempt IPv4 ACL]{lang="EN-US"}]{#struct_0_12741_x1014_2112879791}

[[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_389425122}[例外列表]{style="font-family:宋体"}

[[Exempt IPv6 ACL]{lang="EN-US"}]{#struct_0_12741_x1014_1229183824}

[[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1971023472}[例外列表]{style="font-family:宋体"}

[[Actions]{lang="EN-US"}]{#struct_0_12741_x1014_x806390998}

[[攻击防范的处理行为，包括以下取值：]{style="font-family:宋体"}]{#struct_0_12741_x1014_1585770762}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CV]{lang="EN-US"}]{#struct_0_12741_x1014_1647933194}[：启用客户端验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BS]{lang="EN-US"}]{#struct_0_12741_x1014_x720974310}[：添加黑名单（老化时间，单位为分钟）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_12741_x1014_x1852297393}[：输出告警日志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_12741_x1014_x810298173}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_12741_x1014_546795850}[：不采用任何处理行为]{style="font-family:宋体"}

[[Signature attack defense configuration]{lang="EN-US"}]{#struct_0_12741_x1014_752524521}

[[单包攻击防范配置信息]{style="font-family:宋体"}]{#struct_0_12741_x1014_787659847}

[[Signature name]{lang="EN-US"}]{#struct_0_12741_x1014_1641379341}

[[单包的类型]{style="font-family:宋体"}]{#struct_0_12741_x1014_385506671}

[[Defense]{lang="EN-US"}]{#struct_0_12741_x1014_1613979884}

[[单包攻击防范的开启状态]{style="font-family:宋体"}]{#struct_0_12741_x1014_1785738306}

[[Level]{lang="EN-US"}]{#struct_0_12741_x1014_367514168}

[[单包攻击的级别，包括以下取值：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1019288091}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Info]{lang="EN-US"}]{#struct_0_12741_x1014_1233218101}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[提示级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[l]{lang="EN-US"}[ow]{lang="EN-US"}]{#struct_0_12741_x1014_x599147979}[：低级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m]{lang="EN-US"}[edium]{lang="EN-US"}]{#struct_0_12741_x1014_x1659266503}[：中级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[high]{lang="EN-US"}]{#struct_0_12741_x1014_663467289}[：高级别（目前暂无实例）]{style="font-family:宋体"}

[[Actions]{lang="EN-US"}]{#struct_0_12741_x1014_228974492}

[[单包攻击防范]{style="font-family:宋体"}]{#struct_0_12741_x1014_1260993856}[的处理行为，]{style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_12741_x1014_807972987}[：输出告警日志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_12741_x1014_2065825624}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_12741_x1014_1829604684}[：不采用任何处理行为]{style="font-family:宋体"}

[[IP option record  route]{lang="EN-US"}]{#struct_0_12741_x1014_x854564550}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_1991712771}[选项]{style="font-family:宋体"}[record route]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[IP option security]{lang="EN-US"}]{#struct_0_12741_x1014_500592413}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_753591370}[选项]{style="font-family:宋体"}[security]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[IP option stream ID]{lang="EN-US"}]{#struct_0_12741_x1014_499741683}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x711053981}[选项]{style="font-family:宋体"}[stream ]{lang="EN-US"}[identifier]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[IP option internet timestamp]{lang="EN-US"}]{#struct_0_12741_x1014_1721791455}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_1293592596}[选项]{style="font-family:宋体"}[ internet timestamp]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[IP option loose source routing]{lang="EN-US"}]{#struct_0_12741_x1014_1709529728}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_1362312379}[选项]{style="font-family:宋体"}[loose source routing]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[IP option strict source routing]{lang="EN-US"}]{#struct_0_12741_x1014_x1894236892}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_114218942}[选项]{style="font-family:宋体"}[strict source routing]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[IP option abnormal]{lang="EN-US"}]{#struct_0_12741_x1014_143445787}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x392120637}[选项异常攻击]{style="font-family:宋体"}

[[IP option route alert]{lang="EN-US"}]{#struct_0_12741_x1014_x1453972063}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1106074707}[选项]{style="font-family:宋体"}[route alert]{lang="EN-US"}[攻击]{style="font-family:宋体"}

[[Fragment]{lang="EN-US"}]{#struct_0_12741_x1014_x1422638154}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_501001357}[分片异常攻击]{style="font-family:宋体"}

[[IP impossible]{lang="EN-US"}]{#struct_0_12741_x1014_x1560177075}

[[IP impossible]{lang="EN-US"}]{#struct_0_12741_x1014_718850403}[攻击]{style="font-family:宋体"}

[[Tiny fragment]{lang="EN-US"}]{#struct_0_12741_x1014_1227894712}

[[IP tiny fragment]{lang="EN-US"}]{#struct_0_12741_x1014_1306245201}[攻击]{style="font-family:宋体"}

[[Teardrop]{lang="EN-US"}]{#struct_0_12741_x1014_1055943475}

[[IP teardrop]{lang="EN-US"}]{#struct_0_12741_x1014_x1622555108}[攻击，又称]{style="font-family:宋体"}[IP overlapping fragments]{lang="EN-US"}

[[Large ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_x852547023}

[[Large ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_x971980245}[攻击]{style="font-family:宋体"}

[[Max length]{lang="EN-US"}]{#struct_0_12741_x1014_x616069100}

[[ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_1112605173}[报文所允许的最大长度]{style="font-family:宋体"}

[[Smurf ]{lang="EN-US"}]{#struct_0_12741_x1014_x1543150931}

[[Smurf]{lang="EN-US"}]{#struct_0_12741_x1014_x439398784}[攻击]{style="font-family:宋体"}

[[Traceroute ]{lang="EN-US"}]{#struct_0_12741_x1014_2112814255}

[[Traceroute]{lang="EN-US"}]{#struct_0_12741_x1014_x776680947}[攻击]{style="font-family:宋体"}

[[Ping of death]{lang="EN-US"}]{#struct_0_12741_x1014_903414468}

[[Ping of death]{lang="EN-US"}]{#struct_0_12741_x1014_x943300448}[攻击]{style="font-family:宋体"}

[[ICMP echo request]{lang="EN-US"}]{#struct_0_12741_x1014_546730314}

[[ICMP echo request]{lang="EN-US"}]{#struct_0_12741_x1014_1459331264}[攻击]{style="font-family:宋体"}

[[ICMP echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x259346281}

[[ICMP echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x878233970}[攻击]{style="font-family:宋体"}

[[ICMP source quench]{lang="EN-US"}]{#struct_0_12741_x1014_x1019353627}

[[ICMP source quench]{lang="EN-US"}]{#struct_0_12741_x1014_1326140266}[攻击]{style="font-family:宋体"}

[[ICMP redirect ]{lang="EN-US"}]{#struct_0_12741_x1014_13906883}

[[ICMP redirect]{lang="EN-US"}]{#struct_0_12741_x1014_2065760088}[攻击]{style="font-family:宋体"}

[[ICMP parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x85309660}

[[ICMP parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x1342360061}[攻击]{style="font-family:宋体"}

[[ICMP timestamp request]{lang="EN-US"}]{#struct_0_12741_x1014_499676147}

[[ICMP timestamp request]{lang="EN-US"}]{#struct_0_12741_x1014_x1858613387}[攻击]{style="font-family:宋体"}

[[ICMP timestamp reply]{lang="EN-US"}]{#struct_0_12741_x1014_556614489}

[[ICMP timestamp reply]{lang="EN-US"}]{#struct_0_12741_x1014_1709464192}[攻击]{style="font-family:宋体"}

[[ICMP information request]{lang="EN-US"}]{#struct_0_12741_x1014_969536986}

[[ICMP information request]{lang="EN-US"}]{#struct_0_12741_x1014_x400532122}[攻击]{style="font-family:宋体"}

[[ICMP information reply]{lang="EN-US"}]{#struct_0_12741_x1014_143380251}

[[ICMP information reply]{lang="EN-US"}]{#struct_0_12741_x1014_828177736}[攻击]{style="font-family:宋体"}

[[ICMP address mask request]{lang="EN-US"}]{#struct_0_12741_x1014_x1422703690}

[[ICMP address mask request]{lang="EN-US"}]{#struct_0_12741_x1014_x1999652009}[攻击]{style="font-family:宋体"}

[[ICMP address mask reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1578519479}

[[ICMP address mask reply]{lang="EN-US"}]{#struct_0_12741_x1014_1306179665}[攻击]{style="font-family:宋体"}

[[ICMP destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_x159302336}

[[ICMP destination  unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_x949483275}[攻击]{style="font-family:宋体"}

[[ICMP time exceeded ]{lang="EN-US"}]{#struct_0_12741_x1014_x616134636}

[[ICMP time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_313959558}[攻击]{style="font-family:宋体"}

[[Large ICMPv6]{lang="EN-US"}]{#struct_0_12741_x1014_2112748719}

[[Large ICMPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1173971620}[攻击]{style="font-family:宋体"}

[[ICMPv6 echo request]{lang="EN-US"}]{#struct_0_12741_x1014_1795901993}

[[ICMPv6 echo request]{lang="EN-US"}]{#struct_0_12741_x1014_546664778}[攻击]{style="font-family:宋体"}

[[ICMPv6 echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_243954627}

[[ICMPv6 echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1019419163}[攻击]{style="font-family:宋体"}

[[ICMPv6 group membership query]{lang="EN-US"}]{#struct_0_12741_x1014_897210649}

[[ICMPv6 group membership query]{lang="EN-US"}]{#struct_0_12741_x1014_x1103099304}[攻击]{style="font-family:宋体"}

[[ICMPv6 group membership report]{lang="EN-US"}]{#struct_0_12741_x1014_2065694552}

[[ICMPv6 group membership report]{lang="EN-US"}]{#struct_0_12741_x1014_659560958}[攻击]{style="font-family:宋体"}

[[ICMPv6 group membership reduction]{lang="EN-US"}]{#struct_0_12741_x1014_499610611}

[[ICMPv6 group membership reduction]{lang="EN-US"}]{#struct_0_12741_x1014_x683594626}[攻击]{style="font-family:宋体"}

[[ICMPv6 destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_1027675960}

[[ICMPv6 destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_1709398656}[攻击]{style="font-family:宋体"}

[[ICMPv6 time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_986958055}

[[ICMPv6 time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_143314715}[攻击]{style="font-family:宋体"}

[[ICMPv6 parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x687360208}

[[ICMPv6 parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x1496955736}[攻击]{style="font-family:宋体"}

[[ICMPv6 packet too big]{lang="EN-US"}]{#struct_0_12741_x1014_x1422769226}

[[ICMPv6 packet too big]{lang="EN-US"}]{#struct_0_12741_x1014_1348433071}[攻击]{style="font-family:宋体"}

[[Winnuke]{lang="EN-US"}]{#struct_0_12741_x1014_1306114129}

[[Winnuke]{lang="EN-US"}]{#struct_0_12741_x1014_268760629}[攻击]{style="font-family:宋体"}

[[TCP Land]{lang="EN-US"}]{#struct_0_12741_x1014_x349744033}

[[Land]{lang="EN-US"}]{#struct_0_12741_x1014_x616200172}[攻击]{style="font-family:宋体"}

[[TCP NULL flag]{lang="EN-US"}]{#struct_0_12741_x1014_x822554123}

[[TCP NULL flag]{lang="EN-US"}]{#struct_0_12741_x1014_2112683183}[攻击]{style="font-family:宋体"}

[[TCP invalid flags]{lang="EN-US"}]{#struct_0_12741_x1014_x753886451}

[[TCP invalid flags]{lang="EN-US"}]{#struct_0_12741_x1014_546599242}[攻击]{style="font-family:宋体"}

[[TCP all flags]{lang="EN-US"}]{#struct_0_12741_x1014_1550854901}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x1019484699}[所有标志位均被置位攻击，又称圣诞树攻击]{style="font-family:宋体"}

[[TCP SYN-FIN flags]{lang="EN-US"}]{#struct_0_12741_x1014_329499991}

[[TCP SYN]{lang="EN-US"}]{#struct_0_12741_x1014_1411462546}[和]{style="font-family:宋体"}[FIN]{lang="EN-US"}[被同时置位攻击]{style="font-family:宋体"}

[[TCP FIN only flag]{lang="EN-US"}]{#struct_0_12741_x1014_2065629016}

[[TCP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1999104175}[只有]{style="font-family:宋体"}[FIN]{lang="EN-US"}[被置位的攻击]{style="font-family:宋体"}

[[Fraggle]{lang="EN-US"}]{#struct_0_12741_x1014_499545075}

[[Fraggle]{lang="EN-US"}]{#struct_0_12741_x1014_x576306125}[攻击，又称]{style="font-family:宋体"}[UDP chargen DoS attack]{lang="EN-US"}

[[UDP Bomb]{lang="EN-US"}]{#struct_0_12741_x1014_1709333120}

[[UDP Bomb]{lang="EN-US"}]{#struct_0_12741_x1014_218738543}[攻击]{style="font-family:宋体"}

[[Snork]{lang="EN-US"}]{#struct_0_12741_x1014_143249179}

[[Snork]{lang="EN-US"}]{#struct_0_12741_x1014_x332357629}[攻击]{style="font-family:宋体"}

[[Scan attack defense configuration]{lang="EN-US"}]{#struct_0_12741_x1014_x1422834762}

[[扫描攻击防范配置信息]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1210530991}

[[Defense]{lang="EN-US"}]{#struct_0_12741_x1014_1306048593}

[[扫描攻击防范的开启状态]{style="font-family:宋体"}]{#struct_0_12741_x1014_x921188167}

[[Level]{lang="EN-US"}]{#struct_0_12741_x1014_x616265708}

[[扫描攻击的级别，包括以下取值：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x66506805}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[l]{lang="EN-US"}[ow]{lang="EN-US"}]{#struct_0_12741_x1014_2112617647}[：低级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m]{lang="EN-US"}[edium]{lang="EN-US"}]{#struct_0_12741_x1014_x1137939067}[：中级别]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[high]{lang="EN-US"}]{#struct_0_12741_x1014_546533706}[：高级别]{style="font-family:宋体"}

[[Actions]{lang="EN-US"}]{#struct_0_12741_x1014_1558672174}

[[扫描攻击防范]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1019550235}[的处理行为，]{style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BS]{lang="EN-US"}]{#struct_0_12741_x1014_x1684917084}[：添加黑名单（老化时间，单位为分钟）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_12741_x1014_2065563480}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_12741_x1014_275555639}[：输出告警日志]{lang="EN-US" style="font-family:宋体"}

[[Flood attack defense configuration]{lang="EN-US"}]{#struct_0_12741_x1014_499479539}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1410310615}[攻击防范配置信息]{style="font-family:宋体"}

[[Flood type]{lang="EN-US"}]{#struct_0_12741_x1014_1843550848}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_277466907}[攻击类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_1002835801}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1288617034}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_x700862732}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1440266321}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_1371572340}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_x482047980}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1889230385}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x2048131921}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_680751434}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1147262984}

[[Global thres(pps)]{lang="EN-US"}]{#struct_0_12741_x1014_x885332507}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1089231699}[攻击防范的全局触发阈值，单位为每秒报文数，默认值为]{style="font-family:宋体"}[1000pps]{lang="EN-US"}

[[Global actions]{lang="EN-US"}]{#struct_0_12741_x1014_x2056000442}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_x2095186088}[攻击防范的全局处理行为，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_12741_x1014_1865431412}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_12741_x1014_633697267}[：输出告警日志，]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CV]{lang="EN-US"}]{#struct_0_12741_x1014_x1059135116}[：启用客户端验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_12741_x1014_69093667}[：未配置]{style="font-family:宋体"}

[[Service ports]{lang="EN-US"}]{#struct_0_12741_x1014_1843485312}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1863391872}[攻击防范的全局检测端口号。该字段只对]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范和]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范生效，对于其它]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[，显示为"[-]{lang="EN-US"}"]{style="font-family:宋体"}

[[Non-specific]{lang="EN-US"}]{#struct_0_12741_x1014_277401371}

[[对]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1288682570}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测的状态]{style="font-family:宋体"}

[[Flood attack defense for protected IP addresses]{lang="EN-US"}]{#struct_0_12741_x1014_1324084640}

[[对受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1440200785}[地址的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范配置]{style="font-family:宋体"}

[[Address]{lang="EN-US"}]{#struct_0_12741_x1014_x204258288}

[[指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x482113516}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_x2048197457}

[[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12741_x1014_596166303}[实例名称，未配置时显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Thres(pps)]{lang="EN-US"}]{#struct_0_12741_x1014_680685898}

[[攻击防范检测的触发阈值，单位为报文每秒，未配置时显示为"[-]{lang="EN-US"}"]{style="font-family:宋体"}]{#struct_0_12741_x1014_x885398043}

[[Actions]{lang="EN-US"}]{#struct_0_12741_x1014_x803561547}

[[对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x2095251624}[地址采用的]{style="font-family:宋体"}[攻击防范处理行为，包括 取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CV]{lang="EN-US"}]{#struct_0_12741_x1014_633631731}[：启用客户端验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BS]{lang="EN-US"}]{#struct_0_12741_x1014_x248997599}[：添加黑名单]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_12741_x1014_1843419776}[：输出告警日志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_12741_x1014_277335835}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_12741_x1014_1529119495}[：不采用任何处理行为]{style="font-family:宋体"}

[[Ports]{lang="EN-US"}]{#struct_0_12741_x1014_x1288748106}

[[Flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1459849450}[攻击防范的检测端口号。该字段只对]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范和]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范生效，对于其他攻击防范，显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1051913969}[显示所有攻击防范策略的概要配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy ]{lang="EN-US"}]{#struct_0_12741_x1014_1440135249}

[           Attack-defense Policy Brief Information]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Policy Name                        Applied list]{lang="EN-US"}

[Atk-policy-1                       GigabitEthernet1/0/1]{lang="EN-US"}

[                                   GigabitEthernet1/0/2]{lang="EN-US"}

[                                   GigabitEthernet1/0/3]{lang="EN-US"}

[P2                                 None]{lang="EN-US"}

[P123                               GigabitEthernet1/0/2]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[表]{style="font-family:黑体"}[1-2 display attack-defense policy]{lang="EN-US"}]{#struct_0_12741_x1014_x1380391446}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x943228163}[[字段]{style="font-family:黑体"}]{#struct_0_12741_x1014_508188663}

[[描述]{style="font-family:黑体"}]{#struct_0_12741_x1014_x742175171}

[[Policy Name]{lang="EN-US"}]{#struct_0_12741_x1014_1244312310}

[[攻击防范策略编号]{style="font-family:宋体"}]{#struct_0_12741_x1014_74209988}

[[Applied list]{lang="EN-US"}]{#struct_0_12741_x1014_1882507326}

[[攻击防范策略应用的对象列表，包括接口名称和本机（]{style="font-family:宋体"}[Local]{lang="EN-US"}]{#struct_0_12741_x1014_794875038}[）]{style="font-family:宋体"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x482179052}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_70915111}

::: {#2034591529 .myid}
[]{#_Toc404793895}[]{#struct_0_12741_x1014_x1373187188}[]{#_Toc349981917}[]{#_Toc349981918}[]{#_Toc349981919}[]{#_Toc349981920}[]{#_Toc349981921}[]{#_Toc349981922}[]{#_Toc349981923}[]{#_Toc349981924}[]{#_Toc349981925}[]{#_Toc349981926}[]{#_Toc349981927}[]{#_Toc349981928}[]{#_Toc349981929}[]{#_Toc349981930}[]{#_Toc349981931}[]{#_Toc349981932}[]{#_Toc349981933}[]{#_Toc349981934}[]{#_Toc349981935}[]{#_Toc349981936}[]{#_Toc349981937}[]{#_Toc349981938}[]{#_Toc349981939}[]{#_Toc349981940}[]{#_Toc349981941}[]{#_Toc349981942}[]{#_Toc349981943}[]{#_Toc349981944}[]{#_Toc349981945}[]{#_Toc349981946}[]{#_Toc349981948}[]{#_Toc349981949}[]{#_Toc349981950}[]{#_Toc349981951}[]{#_Toc349981952}[]{#_Toc349981953}[]{#_Toc349981954}[]{#_Toc349981955}[]{#_Toc349981956}[]{#_Toc349981957}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense policy ip**

------------------------------------------------------------------------

[**[display attack-defense policy ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1612855057}[命令用来显示]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_834975127}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x457584144}

[**[display attack-defense policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1102585858}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x1274058165}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x388175445}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x1244296342}[模式：]{style="font-family:宋体"}

[**[display attack-defense policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_439382451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_461182127}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1231062501}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1357654066}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2048262993}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_572150083}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2080711489}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x324477083}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_919375045}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_610498137}[：]{style="font-family:宋体"}[攻击防范策略]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_150109096}[：显示]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[dns-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_147661807}[：显示]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[fin-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_72191974}[：显示]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[flood]{lang="EN-US"}**]{#struct_0_12741_x1014_205941054}[：显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[http-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x67594677}[：显示]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[icmp-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x725018352}[：显示]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[rst-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_680620362}[：显示]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[syn-ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1498030507}[：显示]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[syn-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x825388666}[：显示]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[udp-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1787058731}[：显示]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x556753528}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。若不指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[参数，则表示显示符合指定条件的所有]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x284650280}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示显示指公网的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2008565044}[：显示指定单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1602248343}[：显示指定成员设备上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_802864667}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1914910457}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1747950600}[：显示指定单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_138385742}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x1222192067}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[符合指定条件的]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的数目]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1844806100}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1802691270}[显示攻击防范]{style="font-family:宋体"}[策略]{style="font-family:
宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ip]{lang="EN-US"}]{#struct_0_12741_x1014_284278266}

[IP address      VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[201.55.7.45     \--               ICMP-FLOOD    100                 10]{lang="EN-US"}

[192.168.11.5    \--               DNS-FLOOD     23                  100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1871557114}[显示攻击防范]{style="font-family:宋体"}[策略]{style="font-family:
宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2095317160}

[Slot 1:]{lang="EN-US"}

[IP address      VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[201.55.7.45     \--               ICMP-FLOOD    100                 10]{lang="EN-US"}

[192.168.11.5    \--               DNS-FLOOD     23                  100]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[IP address      VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[201.55.7.45     \--               ICMP-FLOOD    100                 10]{lang="EN-US"}

[192.168.11.5    \--               DNS-FLOOD     23                  100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1903283504}[显示攻击防范]{style="font-family:宋体"}[策略]{style="font-family:
宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ip]{lang="EN-US"}]{#struct_0_12741_x1014_801681297}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address      VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[201.55.7.45     \--               ICMP-FLOOD    100                 10]{lang="EN-US"}

[192.168.11.5    \--               DNS-FLOOD     23                  100]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address      VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[201.55.7.45     \--               ICMP-FLOOD    100                 10]{lang="EN-US"}

[192.168.11.5    \--               DNS-FLOOD     23                  100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1207383683}[显示攻击防范]{style="font-family:宋体"}[策略]{style="font-family:
宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ip count]{lang="EN-US"}]{#struct_0_12741_x1014_633566195}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x857505326}[显示攻击防范]{style="font-family:宋体"}[策略]{style="font-family:
宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1203721375}

[Slot 1:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Totally 3 flood protected entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1938416974}[显示攻击防范]{style="font-family:宋体"}[策略]{style="font-family:
宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ip count]{lang="EN-US"}]{#struct_0_12741_x1014_1697981754}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display attack-defense flood ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1766530323}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x939571847}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_953942602}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1843354240}

[[Totally 3 flood protected IP addresses]{lang="EN-US"}]{#struct_0_12741_x1014_2021880201}

[[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_321201751}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项数目]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_890466621}

[[受保护的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_1055073896}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_371967799}

[[受保护的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x87723656}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，]{style="font-family:宋体"}[未指定时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12741_x1014_x1914585735}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_359368754}[攻击类型]{style="font-family:宋体"}

[[Rate threshold(PPS)]{lang="EN-US"}]{#struct_0_12741_x1014_1498161579}

[[配置的]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1498096043}[攻击防范触发阈值（单位为报文每秒）]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_277270299}

[[检测到]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1510281621}[攻击后的丢包数，若只输出日志该项显示为]{style="font-family:宋体"}[0]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#363758766 .myid}
[]{#_Toc404793896}[]{#struct_0_12741_x1014_x115531744}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense policy ipv6**

------------------------------------------------------------------------

[**[display attack-defense]{lang="EN-US"}**[ **policy ipv6**]{lang="EN-US"}]{#struct_0_12741_x1014_x2054005273}[命令用来显示]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x119234923}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x46750619}

[**[display attack-defense policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1056038096}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_1347209696}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_2063228290}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x1083530694}[模式：]{style="font-family:宋体"}

[**[display attack-defense policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1288813642}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1882834364}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x769046308}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1678957569}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1070564628}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1222083226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1585499941}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1962271962}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1843670825}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1165573702}[：]{style="font-family:宋体"}[攻击防范策略]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1965739106}[：显示]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[dns-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1123454356}[：显示]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[fin-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_2093392163}[：显示]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1440069713}[：显示所有类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[http-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1498030508}[：显示]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[icmpv6-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1409393336}[：显示]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[rst-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x385646388}[：显示]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[syn-ack-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1701861549}[：显示]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[syn-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x2104545686}[：显示]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[udp-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_756789334}[：显示]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_847747362}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。若不指定]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[参数，则表示显示符合指定条件的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1496333627}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2047413061}[：显示指定单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的黑名单表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2041365308}[：显示指定成员设备上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的黑名单表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x359934747}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的黑名单表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1891575583}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2012718248}[：显示指定单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_1236850775}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x482244588}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[符合指定条件的]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的数目]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x680690265}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1180779821}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1663416618}

[IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[2::5            \--               ACK-FLOOD     100                 10]{lang="EN-US"}

[1::5            \--               ACK-FLOOD     100                 23]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1846490920}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2048328529}

[Slot 1:]{lang="EN-US"}

[IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[2::5            \--               ACK-FLOOD     100                 10]{lang="EN-US"}

[1::5            \--               ACK-FLOOD     100                 23 ]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[2::5            \--               ACK-FLOOD     100                 10]{lang="EN-US"}

[1::5            \--               ACK-FLOOD     100                 23]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x837107879}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_197100602}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[2::5            \--               ACK-FLOOD     100                 10]{lang="EN-US"}

[1::5            \--               ACK-FLOOD     100                 23]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped]{lang="EN-US"}

[2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295]{lang="EN-US"}

[2::5            \--               ACK-FLOOD     100                 10]{lang="EN-US"}

[1::5            \--               ACK-FLOOD     100                 23 ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_680554826}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense flood ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_2002627186}

[Totally 3 flood protected entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1653765492}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_835444143}

[Slot 1:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1581790822}[显示攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense policy abc flood ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x1162446718}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 flood protected IP addresses.]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display flood ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1436587572}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x944557763}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x885529115}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x441314161}

[[Totally3 flood protected IP addresses]{lang="EN-US"}]{#struct_0_12741_x1014_x982827385}

[[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_589079367}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项数目]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12741_x1014_x1207899522}

[[受保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_1129279954}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_x882225768}

[[受保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2095382696}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，未指定时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12741_x1014_527693080}

[[flood]{lang="EN-US"}]{#struct_0_12741_x1014_x953867524}[攻击类型]{style="font-family:宋体"}

[[Rate threshold(PPS)]{lang="EN-US"}]{#struct_0_12741_x1014_1498096044}

[[配置的]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_1498489260}[攻击防范触发阈值（单位为报文每秒）]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_x1969044782}

[[检测到]{style="font-family:宋体"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_2145664551}[攻击后的丢包数，若只输出日志该项显示为]{style="font-family:宋体"}[0]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#936894524 .myid}
[]{#_Toc404793897}[]{#struct_0_12741_x1014_633500659}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan attacker ip**

------------------------------------------------------------------------

[**[display attack-defense scan attacker ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1296691607}[命令用来显示扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_203274493}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x784124400}

[**[display attack-defense scan attacker ip]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_697308882}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x616140116}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense scan attacker ip]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x813641192}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_1526488651}[模式：]{style="font-family:宋体"}

[**[display attack-defense scan attacker ip]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_960026672}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1390619367}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1843288704}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1145378576}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_483138093}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x2091909130}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2129108497}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_739625949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1446454649}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1764658974}[：显示指定接口上检测到的]{style="font-family:宋体;color:black"}[扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_12741_x1014_1088341423}[：显示本机检测到的扫描攻击者]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1070591026}[：显示指定]{style="font-family:宋体"}[单板上]{style="font-family:宋体"}[的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号]{style="font-family:宋体"}[。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示所有单板上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1458159559}[：显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1965598545}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_517297460}[：显示指定成员设备的指定单板上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_43284244}[：显示指定单板上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_277204763}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x93294711}[：]{style="font-family:宋体"}[显示符合指定条件的当前扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x528906968}

[[若不指定任何参数，则表示显示所有]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_x1510860668}[扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x465028950}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x291931261}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ip]{lang="EN-US"}]{#struct_0_12741_x1014_1497899437}

[IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)]{lang="EN-US"}

[192.168.31.2    \--               \--                   GE1/0/2      1284]{lang="EN-US"}

[2.2.2.3         \--               \--                   GE1/0/2      23]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1288879178}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1381370882}

[[Slot 1:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_192607230}

[[IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x153281258}

[[192.168.31.2    \--               \--                   GE1/0/2      1284]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x2092139193}

[[2.2.2.3         \--               \--                   GE1/0/2      23]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_438770310}

[[Slot 2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1827082695}[：]{style="font-size:8.5pt;
font-family:\"Arial Unicode MS\",\"sans-serif\""}

[[IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1662871939}

[[192.168.31.2    \--               \--                   GE1/0/2      1284]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1179174369}

[[2.2.2.3         \--               \--                   GE1/0/2      23]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_292821675}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1780127126}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1763707906}

[[Slot 1 in chassis 0:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1121690019}

[[IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x1280775211}

[[192.168.31.2    \--               \--                   GE1/0/2      1284]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x289652793}

[[2.2.2.3         \--               \--                   GE1/0/2      23]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_156916733}

[[Slot 2 in chassis 1:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_273581034}

[[IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x803862739}

[[192.168.31.2    \--               \--                   GE1/0/2      1284]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x2128803663}

[[2.2.2.3         \--               \--                   GE1/0/2      23]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_1161442069}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1338363408}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ip count]{lang="EN-US"}]{#struct_0_12741_x1014_1498161581}

[Totally 3 attackers.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1512478716}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ip ]{lang="EN-US"}]{#struct_0_12741_x1014_1498096045}[count]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x784746900}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1969904211}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display attack-defense scan attacker ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2048394065}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x952008045}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1628942297}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_934878197}

[[Total 3 attackers]{lang="EN-US"}]{#struct_0_12741_x1014_x2074683873}

[[扫描攻击者的数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x203497869}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_x1587785927}

[[发起攻击的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_381820047}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_1893858398}

[[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_12741_x1014_1780986580}[实例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_12741_x1014_680489290}

[[DS-Lite]{lang="EN-US"}]{#struct_0_12741_x1014_154672695}[隧道对端地址。]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[组网下，若本设备为]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[，此列表示报文来自具体的哪个]{style="font-family:宋体"}[B4]{lang="EN-US"}[，如果不在]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[组网或本设备不为]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[，则该字段无意义，显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Detected on]{lang="EN-US"}]{#struct_0_12741_x1014_815040461}

[[进行攻击检测的位置，包括接口或本机（]{style="font-family:宋体"}]{#struct_0_12741_x1014_803302347}[Local]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Duration(min)]{lang="EN-US"}]{#struct_0_12741_x1014_719102786}

[[检测到攻击持续的时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_12741_x1014_792703940}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x923978803}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense scan victim ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x885594651}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scan detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1269819588}

::: {#350748833 .myid}
[]{#_Toc404793898}[]{#struct_0_12741_x1014_1339468841}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan attacker ipv6**

------------------------------------------------------------------------

[**[display attack-defense scan attacker ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x95897237}[命令用来显示扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1623848525}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_1709941566}

[**[display attack-defense scan attacker ipv6]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_619288419}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x575402347}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense scan attacker ipv6]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x58004552}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x442463474}[模式：]{style="font-family:宋体"}

[**[display attack-defense scan attacker ipv6]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x321807176}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1168470722}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1557842885}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2095448232}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1690785900}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1668576784}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1442456198}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_2012770051}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1011349640}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1221118591}[：显示指定接口的]{style="font-family:宋体;color:black"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_12741_x1014_1345802265}[：显示本机检测到的扫描攻击者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x923182690}[：显示指定]{style="font-family:宋体"}[单板上]{style="font-family:宋体"}[的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号]{style="font-family:宋体"}[。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2072111620}[：显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_802733595}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1361032072}[：显示指定成员设备的指定单板上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_348254204}[：显示指定单板上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_633435123}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_1846313561}[：]{style="font-family:宋体"}[显示符合指定条件的当前扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_569560924}

[[若不指定任何参数，则表示显示所有]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_1498164991}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2036607731}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_873442058}[显示]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1497899438}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  1234]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x403066189}[显示]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1497833902}

[Slot 1:]{lang="EN-US"}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  1234]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  10]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
\"Arial Unicode MS\",\"sans-serif\""}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  1234]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1680013001}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1498161582}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  1234]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  10]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  1234]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x452433631}[显示]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_1498096046}

[Totally 3 attackers.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x349273074}[显示]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_1498489262}

[Slot 1:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Totally 3 attackers.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1153789410}[显示所有]{style="font-family:宋体"}[扫描攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan attacker ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_1498030511}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 attackers.]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display attack-defense scan attacker ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1951221552}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x954578397}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x1317047509}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x1167806581}

[[Totally 3 attackers]{lang="EN-US"}]{#struct_0_12741_x1014_x379607218}

[[攻击者的数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1409201721}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12741_x1014_x397916220}

[[发起攻击的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_1026691006}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_x482375660}

[[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_12741_x1014_x1924428906}[实例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Detected on]{lang="EN-US"}]{#struct_0_12741_x1014_x1501352783}

[[进行攻击检测的位置，包括接口或本机（]{style="font-family:宋体"}]{#struct_0_12741_x1014_501299078}[Local]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Duration(min)]{lang="EN-US"}]{#struct_0_12741_x1014_x1330646254}

[[检测到攻击持续的时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_12741_x1014_1584775850}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1285864978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense scan victim ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1639401691}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scan detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x2048459601}

::: {#723009972 .myid}
[]{#_Toc404793899}[]{#struct_0_12741_x1014_1686200919}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan victim ip**

------------------------------------------------------------------------

[**[display attack-defense scan victim ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1101301836}[命令用来显示扫描攻击被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_370535169}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x296906840}

[**[display attack-defense scan victim ip]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x688189508}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x1685449687}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense scan victim ip]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1330756167}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_1301883786}[模式：]{style="font-family:宋体"}

[**[display attack-defense scan victim ip]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1285771697}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x18119446}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x173664563}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1501025583}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1698982632}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_680423754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1108384776}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x89052187}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x451235474}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x838423847}[：显示指定接口的]{style="font-family:宋体;color:black"}[被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_12741_x1014_x1962649806}[：显示本机检测到的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1645285257}[：显示指定]{style="font-family:宋体"}[单板上]{style="font-family:宋体"}[的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号]{style="font-family:宋体"}[。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ slot-number]{lang="EN-US"}]{#struct_0_12741_x1014_543090251}[：显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ slot-number]{lang="EN-US"}]{#struct_0_12741_x1014_x360065819}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1370624953}[：显示指定成员设备的指定单板上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1784047462}[：显示指定单板上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1097409609}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x885660187}[：]{style="font-family:宋体"}[显示符合指定条件的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1474053428}

[[若不指定任何参数，则表示显示所有]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_x633689692}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x914025702}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x393072758}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ip]{lang="EN-US"}]{#struct_0_12741_x1014_1498096047}

[IP address      VPN instance                    Detected on        Duration(min)]{lang="EN-US"}

[192.168.31.2    \--                              GE1/0/4            21]{lang="EN-US"}

[2.2.2.3         \--                              GE1/0/4            1234]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1710715402}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ip]{lang="EN-US"}]{#struct_0_12741_x1014_1498489263}

[Slot 1:]{lang="EN-US"}

[IP address      VPN instance                    Detected on        Duration(min)]{lang="EN-US"}

[192.168.31.2    \--                              GE1/0/4            21]{lang="EN-US"}

[2.2.2.3         \--                              GE1/0/4            1234]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IP address      VPN instance                    Detected on        Duration(min)]{lang="EN-US"}

[192.168.31.2    \--                              GE1/0/4            21]{lang="EN-US"}

[2.2.2.3         \--                              GE1/0/4            1234]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1694172112}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ip]{lang="EN-US"}]{#struct_0_12741_x1014_1498030512}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address      VPN instance                    Detected on        Duration(min)]{lang="EN-US"}

[192.168.31.2    \--                              GE1/0/4            21]{lang="EN-US"}

[2.2.2.3         \--                              GE1/0/4            1234]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address      VPN instance                    Detected on        Duration(min)]{lang="EN-US"}

[192.168.31.2    \--                              GE1/0/4            21]{lang="EN-US"}

[2.2.2.3         \--                              GE1/0/4            1234]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_2076774086}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ip count]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_1376354147}

[[Totally 3 victim IP addresses.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_734005138}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1384603185}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ip ]{lang="EN-US"}]{#struct_0_12741_x1014_x579960989}[count]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x2120055636}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ip ]{lang="EN-US"}]{#struct_0_12741_x1014_1498292656}[count]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display attack-defense scan victim ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2042220006}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x953484005}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1629124401}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_2138399060}

[[Totally 3 victim IP addresses]{lang="EN-US"}]{#struct_0_12741_x1014_x728483790}

[[被攻击者的数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_741302065}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_1899686818}

[[被攻击的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x1154726986}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_1331045028}

[[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_12741_x1014_156290582}[实例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Detected on]{lang="EN-US"}]{#struct_0_12741_x1014_1902090669}

[[进行攻击检测的位置，包括接口或本机（]{style="font-family:宋体"}]{#struct_0_12741_x1014_x355589136}[Local]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Duration(min)]{lang="EN-US"}]{#struct_0_12741_x1014_727655078}

[[检测到被攻击的持续时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_12741_x1014_1574156369}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1103294607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense scan attacker ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1313802600}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scan detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1209354871}

::: {#2122685774 .myid}
[]{#_Toc404793900}[]{#struct_0_12741_x1014_1133064480}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan victim ipv6**

------------------------------------------------------------------------

[**[display attack-defense scan victim ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x247053657}[命令用来显示扫描攻击被攻击者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_742562762}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1383029605}

[**[display attack-defense scan victim ipv6]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1542720646}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x1715190928}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense scan victim ipv6]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x348157932}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x1245525565}[模式：]{style="font-family:宋体"}

[**[display attack-defense scan victim ipv6]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \| **local** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1984357642}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1500680989}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_177264408}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1855129400}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_396580143}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x585449862}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x610069326}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x72941065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_332005724}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1914241873}[：显示指定接口的]{style="font-family:宋体;color:black"}[被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号[。]{style="color:black"}]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x2113061425}[：]{style="font-family:宋体"}[仅显示符合指定条件的当前被攻击者的数目。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12741_x1014_480771534}[：显示指定]{style="font-family:宋体"}[单板上]{style="font-family:宋体"}[的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号]{style="font-family:宋体"}[。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x418818473}[：显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1965467473}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1464170486}[：显示指定成员设备的指定单板上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1399291006}[：显示指定单板上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定本机或指定全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x375237723}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_12741_x1014_435833058}[：显示本机检测到的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1487859721}

[[若不指定任何参数，则表示显示所有]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_1947484043}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_814641482}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x81818995}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1498096048}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  210]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  13]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x912833533}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1498554800}

[Slot 1:]{lang="EN-US"}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  210]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  13]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
\"Arial Unicode MS\",\"sans-serif\""}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  210]{lang="EN-US"}

[1230[::22                 \--               GE1/0/4                  13]{.TerminalDisplayChar}]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x715324661}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1094745980}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  210]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  13]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address             VPN instance     Detected on              Duration(min)]{lang="EN-US"}

[2013::2                  \--               GE1/0/4                  210]{lang="EN-US"}

[1230::22                 \--               GE1/0/4                  13]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x19188540}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_1094614908}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x454205419}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ipv6 ]{lang="EN-US"}]{#struct_0_12741_x1014_x1609291049}[count]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1205113128}[显示]{style="font-family:宋体"}[扫描攻击的被攻击者的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址表项的个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense scan victim ipv6 ]{lang="EN-US"}]{#struct_0_12741_x1014_1095008124}[count]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 victim IP addresses.]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display attack-defense scan victim ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1470743184}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x654415393}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_407546169}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1977375360}

[[Totally 3 victim IP addresses]{lang="EN-US"}]{#struct_0_12741_x1014_x1339911431}

[[被攻击者的数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x305045393}

[[IPv6 ]{lang="EN-US"}]{#struct_0_12741_x1014_x766363780}[address]{lang="EN-US" style="font-size:10.0pt"}

[[被攻击的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_1836023499}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_969705901}

[[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_12741_x1014_1394433218}[实例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Detected on]{lang="EN-US"}]{#struct_0_12741_x1014_x788399529}

[[进行攻击检测的位置，包括接口或本机（]{style="font-family:宋体"}]{#struct_0_12741_x1014_411291419}[Local]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Duration(min)]{lang="EN-US"}]{#struct_0_12741_x1014_1180483900}

[[检测到被攻击的持续时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_12741_x1014_x137887149}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x98335422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense scan attacker ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_986846967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scan detect]{lang="EN-US"}**]{#struct_0_12741_x1014_1720271024}

::: {#34258731 .myid}
[]{#_Toc404793901}[]{#struct_0_12741_x1014_1245620410}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense statistics interface**

------------------------------------------------------------------------

[**[display attack-defense statistics interface]{lang="EN-US"}**]{#struct_0_12741_x1014_835732371}[命令用来显示接口上的攻击防范统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1661148887}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1154792522}

[**[display attack-defense statistics interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x849637069}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_813877899}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense statistics interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12741_x1014_1587467120}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_371905728}[模式：]{style="font-family:宋体"}

[**[display attack-defense statistics interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \[ **chassis** *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12741_x1014_1108242757}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_666057465}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x630061078}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1626500370}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2026622151}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1508842051}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1574090833}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1598999287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1882117988}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1110059748}[：]{style="font-family:宋体"}[表示指定接口的接口类型和接口编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1217052640}[：显示全局接口在指定单板上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示指定全局接口在所有单板上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2000469049}[：显示全局接口在指定成员设备上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示指定全局接口在所有成员设备上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2012521640}[：显示全局接口在指定成员设备上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示指定全局接口在所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1767820964}[：显示全局接口在指定成员设备的指定单板上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示指定全局接口在所有单板上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_446437699}[：显示全局接口在指定单板上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示指定全局接口在所有单板上的]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1636072031}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的攻击防范统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1221266127}

[[参数]{style="font-family:宋体"}]{#struct_0_12741_x1014_602229482}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[（分布式设备－独立运行模式）、 ]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）、 ]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）只在指定接口为全局接口时可以输入。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x138263637}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x348223468}[显]{style="font-family:宋体"}[示]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的攻击防范统计信息]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense statistics interface gigabitethernet 1/0/1 ]{lang="EN-US"}]{#struct_0_12741_x1014_814575946}

[Attack policy name: abc]{lang="EN-US"}

[Scan attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ Port scan                           2           23]{lang="EN-US"}

[ IP sweep                            3           33]{lang="EN-US"}

[ Distribute port scan                1           10]{lang="EN-US"}

[Flood attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ SYN flood                           1           0]{lang="EN-US"}

[ ACK flood                           1           0]{lang="EN-US"}

[ SYN-ACK flood                       3           5000]{lang="EN-US"}

[ RST flood                           2           0]{lang="EN-US"}

[ FIN flood                           2           0]{lang="EN-US"}

[ UDP flood                           1           0]{lang="EN-US"}

[ ICMP flood                          1           0]{lang="EN-US"}

[ ICMPv6 flood                        1           0]{lang="EN-US"}

[ DNS flood                           1           0]{lang="EN-US"}

[ HTTP flood                          1           0]{lang="EN-US"}

[Signature attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ IP option record route              1           100]{lang="EN-US"}

[ IP option security                  2           0]{lang="EN-US"}

[ IP option stream ID                 3           0]{lang="EN-US"}

[ IP option internet timestamp        4           1]{lang="EN-US"}

[ IP option loose source routing      5           0]{lang="EN-US"}

[ IP option strict source routing     6           0]{lang="EN-US"}

[ IP option route alert               3           0 ]{lang="EN-US"}

[ Fragment                            1           0]{lang="EN-US"}

[ Impossible                          1           1]{lang="EN-US"}

[ Teardrop                            1           1]{lang="EN-US"}

[ Tiny fragment                       1           0]{lang="EN-US"}

[ IP options abnormal                 3           0]{lang="EN-US"}

[ Smurf                               1           0]{lang="EN-US"}

[ Ping of death                       1           0]{lang="EN-US"}

[ Traceroute                          1           0]{lang="EN-US"}

[ Large ICMP                          1           0]{lang="EN-US"}

[ TCP NULL flag                       1           0]{lang="EN-US"}

[ TCP all flags                       1           0]{lang="EN-US"}

[ TCP SYN-FIN flags                   1           0]{lang="EN-US"}

[ TCP FIN only flag                   1           0]{lang="EN-US"}

[ TCP invalid flag                    1           0]{lang="EN-US"}

[ TCP Land                            1           0]{lang="EN-US"}

[ Winnuke                             1           0]{lang="EN-US"}

[ UDP Bomb                            1           0]{lang="EN-US"}

[ Snork                               1           0 ]{lang="EN-US"}

[ Fraggle                             1           0]{lang="EN-US"}

[ Large ICMPv6                        1           0]{lang="EN-US"}

[ ICMP echo request                   1           0]{lang="EN-US"}

[ ICMP echo reply                     1           0]{lang="EN-US"}

[ ICMP source quench                  1           0]{lang="EN-US"}

[ ICMP destination unreachable        1           0]{lang="EN-US"}

[ ICMP redirect                       2           0]{lang="EN-US"}

[ ICMP time exceeded                  3           0]{lang="EN-US"}

[ ICMP parameter problem              4           0]{lang="EN-US"}

[ ICMP timestamp request              5           0]{lang="EN-US"}

[ ICMP timestamp reply                6           0]{lang="EN-US"}

[ ICMP information request            7           0]{lang="EN-US"}

[ ICMP information reply              4           0]{lang="EN-US"}

[ ICMP address mask request           2           0]{lang="EN-US"}

[ ICMP address mask reply             1           0]{lang="EN-US"}

[ ICMPv6 echo request                 1           1]{lang="EN-US"}

[ ICMPv6 echo reply                   1           1]{lang="EN-US"}

[ ICMPv6 group membership query       1           0]{lang="EN-US"}

[ ICMPv6 group membership report      1           0]{lang="EN-US"}

[ ICMPv6 group membership reduction   1           0]{lang="EN-US"}

[ ICMPv6 destination unreachable      1           0]{lang="EN-US"}

[ ICMPv6 time exceeded                1           0]{lang="EN-US"}

[ ICMPv6 parameter problem            1           0]{lang="EN-US"}

[ ICMPv6 packet too big               1           0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x459442487}[显示]{style="font-family:宋体"}[Slot 1]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的攻击防范统计信息]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense statistics interface gigabitethernet 1/0/1 slot 1]{lang="EN-US"}]{#struct_0_12741_x1014_767521779}

[Attack policy name: abc]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Scan attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ Port scan                           2           23]{lang="EN-US"}

[ IP sweep                            3           33]{lang="EN-US"}

[ Distribute port scan                1           10]{lang="EN-US"}

[Flood attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ SYN flood                           1           0]{lang="EN-US"}

[ ACK flood                           1           0]{lang="EN-US"}

[ SYN-ACK flood                       3           5000]{lang="EN-US"}

[ RST flood                           2           0]{lang="EN-US"}

[ FIN flood                           2           0]{lang="EN-US"}

[ UDP flood                           1           0]{lang="EN-US"}

[ ICMP flood                          1           0]{lang="EN-US"}

[ ICMPv6 flood                        1           0]{lang="EN-US"}

[ DNS flood                           1           0]{lang="EN-US"}

[ HTTP flood                          1           0]{lang="EN-US"}

[Signature attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ IP option record route              1           100]{lang="EN-US"}

[ IP option security                  2           0]{lang="EN-US"}

[ IP option stream ID                 3           0]{lang="EN-US"}

[ IP option internet timestamp        4           1]{lang="EN-US"}

[ IP option loose source routing      5           0]{lang="EN-US"}

[ IP option strict source routing     6           0]{lang="EN-US"}

[ IP option route alert               3           0 ]{lang="EN-US"}

[ Fragment                            1           0]{lang="EN-US"}

[ Impossible                          1           1]{lang="EN-US"}

[ Teardrop                            1           1]{lang="EN-US"}

[ Tiny fragment                       1           0]{lang="EN-US"}

[ IP options abnormal                 3           0]{lang="EN-US"}

[ Smurf                               1           0]{lang="EN-US"}

[ Ping of death                       1           0]{lang="EN-US"}

[ Traceroute                          1           0]{lang="EN-US"}

[ Large ICMP                          1           0]{lang="EN-US"}

[ TCP NULL flag                       1           0]{lang="EN-US"}

[ TCP all flags                       1           0]{lang="EN-US"}

[ TCP SYN-FIN flags                   1           0]{lang="EN-US"}

[ TCP FIN only flag                   1           0]{lang="EN-US"}

[ TCP invalid flag                    1           0]{lang="EN-US"}

[ TCP Land                            1           0]{lang="EN-US"}

[ Winnuke                             1           0]{lang="EN-US"}

[ UDP Bomb                            1           0]{lang="EN-US"}

[ Snork                               1           0]{lang="EN-US"}

[ Fraggle                             1           0]{lang="EN-US"}

[ Large ICMPv6                        1           0]{lang="EN-US"}

[ ICMP echo request                   1           0]{lang="EN-US"}

[ ICMP echo reply                     1           0]{lang="EN-US"}

[ ICMP source quench                  1           0]{lang="EN-US"}

[ ICMP destination unreachable        1           0]{lang="EN-US"}

[ ICMP redirect                       2           0]{lang="EN-US"}

[ ICMP time exceeded                  3           0]{lang="EN-US"}

[ ICMP parameter problem              4           0]{lang="EN-US"}

[ ICMP timestamp request              5           0]{lang="EN-US"}

[ ICMP timestamp reply                6           0]{lang="EN-US"}

[ ICMP information request            7           0]{lang="EN-US"}

[ ICMP information reply              4           0]{lang="EN-US"}

[ ICMP address mask request           2           0]{lang="EN-US"}

[ ICMP address mask reply             1           0]{lang="EN-US"}

[ ICMPv6 echo request                 1           1]{lang="EN-US"}

[ ICMPv6 echo reply                   1           1]{lang="EN-US"}

[ ICMPv6 group membership query       1           0]{lang="EN-US"}

[ ICMPv6 group membership report      1           0]{lang="EN-US"}

[ ICMPv6 group membership reduction   1           0]{lang="EN-US"}

[ ICMPv6 destination unreachable      1           0]{lang="EN-US"}

[ ICMPv6 time exceeded                1           0]{lang="EN-US"}

[ ICMPv6 parameter problem            1           0]{lang="EN-US"}

[ ICMPv6 packet too big               1           0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_369779278}[显示]{style="font-family:宋体"}[Chassis 0]{lang="EN-US"}[的]{style="font-family:宋体"}[slot 1]{lang="EN-US"}[上]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的攻击防范信息]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense statistics interface gigabitethernet 1/0/1 chassis 0 slot 1]{lang="EN-US"}]{#struct_0_12741_x1014_x1154858058}

[Attack policy name: abc]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Scan attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ Port scan                           2           23]{lang="EN-US"}

[ IP sweep                            3           33]{lang="EN-US"}

[ Distribute port scan                1           10]{lang="EN-US"}

[Flood attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ SYN flood                           1           0]{lang="EN-US"}

[ ACK flood                           1           0]{lang="EN-US"}

[ SYN-ACK flood                       3           5000]{lang="EN-US"}

[ RST flood                           2           0]{lang="EN-US"}

[ FIN flood                           2           0]{lang="EN-US"}

[ UDP flood                           1           0]{lang="EN-US"}

[ ICMP flood                          1           0]{lang="EN-US"}

[ ICMPv6 flood                        1           0]{lang="EN-US"}

[ DNS flood                           1           0]{lang="EN-US"}

[ HTTP flood                          1           0]{lang="EN-US"}

[Signature attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ IP option record route              1           100]{lang="EN-US"}

[ IP option security                  2           0]{lang="EN-US"}

[ IP option stream ID                 3           0]{lang="EN-US"}

[ IP option internet timestamp        4           1]{lang="EN-US"}

[ IP option loose source routing      5           0]{lang="EN-US"}

[ IP option strict source routing     6           0]{lang="EN-US"}

[ IP option route alert               3           0]{lang="EN-US"}

[ Fragment                            1           0]{lang="EN-US"}

[ Impossible                          1           1]{lang="EN-US"}

[ Teardrop                            1           1]{lang="EN-US"}

[ Tiny fragment                       1           0]{lang="EN-US"}

[ IP options abnormal                 3           0]{lang="EN-US"}

[ Smurf                               1           0]{lang="EN-US"}

[ Ping of death                       1           0]{lang="EN-US"}

[ Traceroute                          1           0]{lang="EN-US"}

[ Large ICMP                          1           0]{lang="EN-US"}

[ TCP NULL flag                       1           0]{lang="EN-US"}

[ TCP all flags                       1           0]{lang="EN-US"}

[ TCP SYN-FIN flags                   1           0]{lang="EN-US"}

[ TCP FIN only flag                   1           0]{lang="EN-US"}

[ TCP invalid flag                    1           0]{lang="EN-US"}

[ TCP Land                            1           0]{lang="EN-US"}

[ Winnuke                             1           0]{lang="EN-US"}

[ UDP Bomb                            1           0]{lang="EN-US"}

[ Snork                               1           0]{lang="EN-US"}

[ Fraggle                             1           0]{lang="EN-US"}

[ Large ICMPv6                        1           0]{lang="EN-US"}

[ ICMP echo request                   1           0]{lang="EN-US"}

[ ICMP echo reply                     1           0]{lang="EN-US"}

[ ICMP source quench                  1           0]{lang="EN-US"}

[ ICMP destination unreachable        1           0]{lang="EN-US"}

[ ICMP redirect                       2           0]{lang="EN-US"}

[ ICMP time exceeded                  3           0]{lang="EN-US"}

[ ICMP parameter problem              4           0]{lang="EN-US"}

[ ICMP timestamp request              5           0]{lang="EN-US"}

[ ICMP timestamp reply                6           0]{lang="EN-US"}

[ ICMP information request            7           0]{lang="EN-US"}

[ ICMP information reply              4           0]{lang="EN-US"}

[ ICMP address mask request           2           0]{lang="EN-US"}

[ ICMP address mask reply             1           0]{lang="EN-US"}

[ ICMPv6 echo request                 1           1]{lang="EN-US"}

[ ICMPv6 echo reply                   1           1]{lang="EN-US"}

[ ICMPv6 group membership query       1           0]{lang="EN-US"}

[ ICMPv6 group membership report      1           0]{lang="EN-US"}

[ ICMPv6 group membership reduction   1           0]{lang="EN-US"}

[ ICMPv6 destination unreachable      1           0]{lang="EN-US"}

[ ICMPv6 time exceeded                1           0]{lang="EN-US"}

[ ICMPv6 parameter problem            1           0]{lang="EN-US"}

[ ICMPv6 packet too big               1           0]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[d]{lang="EN-US"}]{#struct_0_12741_x1014_1854322082}[isplay attack-defense statistics interface ]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x661964115}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_57883638}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1788474009}

[[AttackType]{lang="EN-US"}]{#struct_0_12741_x1014_785008985}

[[攻击类型]{style="font-family:宋体"}]{#struct_0_12741_x1014_1102724043}

[[AttackTimes]{lang="EN-US"}]{#struct_0_12741_x1014_1574025297}

[[受到攻击的次数]{style="font-family:宋体"}]{#struct_0_12741_x1014_x828992816}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_x510203148}

[[丢弃报文的数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1289259995}

[[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_369974965}

[[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_1608005341}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1151440140}

[[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x348289004}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1288099297}

[[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1234192065}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_417255299}

[[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_1927678292}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_1018812541}

[[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1725818133}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1914372945}

[[UDP flood ]{lang="EN-US"}]{#struct_0_12741_x1014_x1552826351}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1695435777}

[[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1129332157}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_1384524542}

[[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_x973649609}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_814510410}

[[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_x372733166}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_588543803}

[[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x826424805}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Port scan]{lang="EN-US"}]{#struct_0_12741_x1014_x751573531}

[[端口扫描]{style="font-family:宋体"}]{#struct_0_12741_x1014_1917490329}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP Sweep]{lang="EN-US"}]{#struct_0_12741_x1014_x70712157}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_21980534}[扫描攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Distribute port scan]{lang="EN-US"}]{#struct_0_12741_x1014_x351343938}

[[分布式端口扫描]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1961427112}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option record  route]{lang="EN-US"}]{#struct_0_12741_x1014_2038461231}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1246653306}[选项]{style="font-family:宋体"}[record route]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option security]{lang="EN-US"}]{#struct_0_12741_x1014_1625936673}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_767456243}[选项]{style="font-family:宋体"}[security]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option stream ID]{lang="EN-US"}]{#struct_0_12741_x1014_1956185136}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1415520790}[选项]{style="font-family:宋体"}[stream ]{lang="EN-US"}[identifier]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option internet timestamp]{lang="EN-US"}]{#struct_0_12741_x1014_x1464357907}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1977244288}[选项]{style="font-family:宋体"}[ internet timestamp]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option loose source routing]{lang="EN-US"}]{#struct_0_12741_x1014_x574224467}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1248078782}[选项]{style="font-family:宋体"}[loose source routing]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option strict source routing]{lang="EN-US"}]{#struct_0_12741_x1014_x2010324135}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_411160347}[选项]{style="font-family:宋体"}[strict source routing]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option route alert]{lang="EN-US"}]{#struct_0_12741_x1014_968200982}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1606458178}[选项]{style="font-family:宋体"}[strict source routing]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Fragment]{lang="EN-US"}]{#struct_0_12741_x1014_x423875819}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1154923594}[分片异常攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Impossible]{lang="EN-US"}]{#struct_0_12741_x1014_824654186}

[[IP impossible]{lang="EN-US"}]{#struct_0_12741_x1014_738251187}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Teardrop]{lang="EN-US"}]{#struct_0_12741_x1014_x1176710677}

[[IP teardrop]{lang="EN-US"}]{#struct_0_12741_x1014_1573959761}[攻击，又称]{style="font-family:宋体"}[IP overlapping fragments]{lang="EN-US"}[，]{style="font-family:宋体"}[当]{style="font-size:10.0pt;font-family:宋体;color:black"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US" style="font-size:10.0pt;
  font-family:\"Segoe UI\",\"sans-serif\";color:black"}[时，该列不显示]{style="font-size:10.0pt;font-family:宋体;color:black"}

[[Tiny fragment]{lang="EN-US"}]{#struct_0_12741_x1014_x276161934}

[[IP tiny fragment]{lang="EN-US"}]{#struct_0_12741_x1014_x1352037024}[攻击]{style="font-family:宋体"}

[[IP option abnormal]{lang="EN-US"}]{#struct_0_12741_x1014_x348354540}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x810533243}[选项异常攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Smurf ]{lang="EN-US"}]{#struct_0_12741_x1014_1276867761}

[[Smurf]{lang="EN-US"}]{#struct_0_12741_x1014_x1914438481}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Ping of death]{lang="EN-US"}]{#struct_0_12741_x1014_x1625001330}

[[Ping of death]{lang="EN-US"}]{#struct_0_12741_x1014_1846463125}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Traceroute ]{lang="EN-US"}]{#struct_0_12741_x1014_x212742471}

[[Traceroute]{lang="EN-US"}]{#struct_0_12741_x1014_814444874}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Large ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_x2013855281}

[[Large ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_1019109750}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为[0]{lang="EN-US"}时，该列不显示]{style="font-family:宋体"}

[[TCP NULL flag]{lang="EN-US"}]{#struct_0_12741_x1014_2145269064}

[[TCP NULL flag]{lang="EN-US"}]{#struct_0_12741_x1014_x751639067}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP all flags]{lang="EN-US"}]{#struct_0_12741_x1014_x2043141367}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_238748968}[所有标志位均被置位攻击，又称圣诞树攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP SYN-FIN flags]{lang="EN-US"}]{#struct_0_12741_x1014_x1961492648}

[[TCP SYN]{lang="EN-US"}]{#struct_0_12741_x1014_39309357}[和]{style="font-family:宋体"}[FIN]{lang="EN-US"}[被同时置位攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP FIN only flag]{lang="EN-US"}]{#struct_0_12741_x1014_514768398}

[[TCP ]{lang="EN-US"}]{#struct_0_12741_x1014_767390707}[只有]{style="font-family:宋体"}[FIN]{lang="EN-US"}[被置位的攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP invalid flag]{lang="EN-US"}]{#struct_0_12741_x1014_1291477873}

[[TCP ]{lang="EN-US"}]{#struct_0_12741_x1014_852413633}[非法标志位攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP Land]{lang="EN-US"}]{#struct_0_12741_x1014_1977178752}

[[TCP Land]{lang="EN-US"}]{#struct_0_12741_x1014_x2057662443}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Winnuke]{lang="EN-US"}]{#struct_0_12741_x1014_2053013780}

[[Winnuke]{lang="EN-US"}]{#struct_0_12741_x1014_411094811}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[UDP Bomb]{lang="EN-US"}]{#struct_0_12741_x1014_x1063152720}

[[UDP Bomb]{lang="EN-US"}]{#struct_0_12741_x1014_663380347}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Snork]{lang="EN-US"}]{#struct_0_12741_x1014_x1154989130}

[[UDP snork]{lang="EN-US"}]{#struct_0_12741_x1014_x1217832032}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Fraggle]{lang="EN-US"}]{#struct_0_12741_x1014_x26934553}

[[Fraggle]{lang="EN-US"}]{#struct_0_12741_x1014_1573894225}[攻击，又称]{style="font-family:宋体"}[UDP chargen DoS attack]{lang="EN-US"}[，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Large ICMPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1905523092}

[[Large ICMPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x348420076}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP echo request]{lang="EN-US"}]{#struct_0_12741_x1014_x65924781}

[[ICMP echo request]{lang="EN-US"}]{#struct_0_12741_x1014_1563607466}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1914504017}

[[ICMP echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x2066751793}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP source quench]{lang="EN-US"}]{#struct_0_12741_x1014_814379338}

[[ICMP source quench]{lang="EN-US"}]{#struct_0_12741_x1014_x1445599047}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_x667814684}

[[ICMP destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_x751704603}[攻击，当]{style="font-family:
  宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP redirect ]{lang="EN-US"}]{#struct_0_12741_x1014_1927094335}

[[ICMP redirect]{lang="EN-US"}]{#struct_0_12741_x1014_313155957}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_x1961558184}

[[ICMP time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_223136300}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_767325171}

[[ICMP parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_152544932}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP timestamp request]{lang="EN-US"}]{#struct_0_12741_x1014_1130843344}

[[ICMP timestamp request]{lang="EN-US"}]{#struct_0_12741_x1014_1977113216}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP timestamp reply]{lang="EN-US"}]{#struct_0_12741_x1014_x161437308}

[[ICMP timestamp reply]{lang="EN-US"}]{#struct_0_12741_x1014_411029275}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP information request]{lang="EN-US"}]{#struct_0_12741_x1014_554960691}

[[ICMP information request]{lang="EN-US"}]{#struct_0_12741_x1014_x1155054666}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP information reply]{lang="EN-US"}]{#struct_0_12741_x1014_1783776147}

[[ICMP information reply]{lang="EN-US"}]{#struct_0_12741_x1014_1573828689}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP address mask request]{lang="EN-US"}]{#struct_0_12741_x1014_498044718}

[[ICMP address mask request]{lang="EN-US"}]{#struct_0_12741_x1014_x348485612}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP address mask reply]{lang="EN-US"}]{#struct_0_12741_x1014_x822103172}

[[ICMP address mask reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1914569553}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 echo request]{lang="EN-US"}]{#struct_0_12741_x1014_1546387520}

[[ICMPv6 echo request]{lang="EN-US"}]{#struct_0_12741_x1014_1518206191}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_814313802}

[[ICMPv6 echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_87163480}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 group membership query]{lang="EN-US"}]{#struct_0_12741_x1014_x751770139}

[[ICMPv6 group membership query]{lang="EN-US"}]{#struct_0_12741_x1014_x2016611672}[攻击，当]{style="font-family:
  宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 group membership report]{lang="EN-US"}]{#struct_0_12741_x1014_1463477340}

[[ICMPv6 group membership report]{lang="EN-US"}]{#struct_0_12741_x1014_x1961623720}[攻击，当]{style="font-family:
  宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 group membership reduction]{lang="EN-US"}]{#struct_0_12741_x1014_767259635}

[[ICMPv6 group membership reduction]{lang="EN-US"}]{#struct_0_12741_x1014_1647236762}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_2111330944}

[[ICMPv6 destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_1757935613}[攻击，当]{style="font-family:
  宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_x773923615}

[[ICMPv6 time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_545247003}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_179508370}

[[ICMPv6 parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x1020836938}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 packet too big]{lang="EN-US"}]{#struct_0_12741_x1014_x831495869}

[[ICMPv6 packet too big]{lang="EN-US"}]{#struct_0_12741_x1014_1708046417}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#2016420116 .myid}
[]{#_Toc404793902}[]{#struct_0_12741_x1014_607915296}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense statistics local**

------------------------------------------------------------------------

[**[display attack-defense statistics local]{lang="EN-US"}**]{#struct_0_12741_x1014_x1854144423}[命令用来显示本机攻击防范的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_348432843}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1635137098}

[**[display attack-defense statistics local]{lang="EN-US"}**]{#struct_0_12741_x1014_x282827665}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_1352704829}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display attack-defense statistics local]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12741_x1014_548688454}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x654821522}[模式：]{style="font-family:宋体"}

[**[display attack-defense statistics local]{lang="EN-US"}**[ \[ **chassis** *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12741_x1014_x214267884}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1948694898}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1094933671}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_332659128}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1583308714}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1498835284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1055543882}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1068124621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1183196695}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_77488258}[：显示本机攻击防范在指定单板上的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上检测到的本机攻击防范统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1802032522}[：显示]{style="font-family:宋体"}[本机攻击防范]{style="font-family:宋体"}[在指定成员设备上的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上检测到的本机]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x360262427}[：显示]{style="font-family:宋体"}[本机攻击防范]{style="font-family:宋体"}[在指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上检测到的本机]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1780351825}[：显示]{style="font-family:宋体"}[本机攻击防范]{style="font-family:宋体"}[在指定成员设备的指定单板上的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上检测到的本机]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1342305834}[：显示]{style="font-family:宋体"}[本机攻击防范]{style="font-family:宋体"}[在指定单板上的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上检测到的本机]{style="font-family:宋体"}[攻击防范统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1947219442}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的本机攻击防范]{style="font-family:宋体"}[的]{style="font-family:宋体"}[统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_686966943}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1408367389}[显示]{style="font-family:宋体"}[本机攻击防范统计信息]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense statistics local]{lang="EN-US"}]{#struct_0_12741_x1014_x1827405992}

[Attack defense policy name: abc]{lang="EN-US"}

[Scan attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ Port scan                           2           23]{lang="EN-US"}

[ IP sweep                            3           33]{lang="EN-US"}

[ Distribute port scan                1           10]{lang="EN-US"}

[Flood attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ SYN flood                           1           0]{lang="EN-US"}

[ ACK flood                           1           0]{lang="EN-US"}

[ SYN-ACK flood                       3           5000]{lang="EN-US"}

[ RST flood                           2           0]{lang="EN-US"}

[ FIN flood                           2           0]{lang="EN-US"}

[ UDP flood                           1           0]{lang="EN-US"}

[ ICMP flood                          1           0]{lang="EN-US"}

[ ICMPv6 flood                        1           0]{lang="EN-US"}

[ DNS flood                           1           0]{lang="EN-US"}

[ HTTP flood                          1           0]{lang="EN-US"}

[Signature attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ IP option record route              1           100]{lang="EN-US"}

[ IP option security                  2           0]{lang="EN-US"}

[ IP option stream ID                 3           0]{lang="EN-US"}

[ IP option internet timestamp        4           1]{lang="EN-US"}

[ IP option loose source routing      5           0]{lang="EN-US"}

[ IP option strict source routing     6           0]{lang="EN-US"}

[ IP option route alert               3           0 ]{lang="EN-US"}

[ Fragment                            1           0]{lang="EN-US"}

[ Impossible                          1           1]{lang="EN-US"}

[ Teardrop                            1           1]{lang="EN-US"}

[ Tiny fragment                       1           0]{lang="EN-US"}

[ IP options abnormal                 3           0]{lang="EN-US"}

[ Smurf                               1           0]{lang="EN-US"}

[ Ping of death                       1           0]{lang="EN-US"}

[ Traceroute                          1           0]{lang="EN-US"}

[ Large ICMP                          1           0]{lang="EN-US"}

[ TCP NULL flag                       1           0]{lang="EN-US"}

[ TCP all flags                       1           0]{lang="EN-US"}

[ TCP SYN-FIN flags                   1           0]{lang="EN-US"}

[ TCP FIN only flag                   1           0]{lang="EN-US"}

[ TCP invalid flag                    1           0]{lang="EN-US"}

[ TCP Land                            1           0]{lang="EN-US"}

[ Winnuke                             1           0]{lang="EN-US"}

[ UDP Bomb                            1           0]{lang="EN-US"}

[ Snork                               1           0 ]{lang="EN-US"}

[ Fraggle                             1           0]{lang="EN-US"}

[ Large ICMPv6                        1           0 ]{lang="EN-US"}

[ ICMP echo request                   1           0]{lang="EN-US"}

[ ICMP echo reply                     1           0]{lang="EN-US"}

[ ICMP source quench                  1           0]{lang="EN-US"}

[ ICMP destination unreachable        1           0]{lang="EN-US"}

[ ICMP redirect                       2           0]{lang="EN-US"}

[ ICMP time exceeded                  3           0]{lang="EN-US"}

[ ICMP parameter problem              4           0]{lang="EN-US"}

[ ICMP timestamp request              5           0]{lang="EN-US"}

[ ICMP timestamp reply                6           0]{lang="EN-US"}

[ ICMP information request            7           0]{lang="EN-US"}

[ ICMP information reply              4           0]{lang="EN-US"}

[ ICMP address mask request           2           0]{lang="EN-US"}

[ ICMP address mask reply             1           0]{lang="EN-US"}

[ ICMPv6 echo request                 1           1]{lang="EN-US"}

[ ICMPv6 echo reply                   1           1]{lang="EN-US"}

[ ICMPv6 group membership query       1           0]{lang="EN-US"}

[ ICMPv6 group membership report      1           0]{lang="EN-US"}

[ ICMPv6 group membership reduction   1           0]{lang="EN-US"}

[ ICMPv6 destination unreachable      1           0]{lang="EN-US"}

[ ICMPv6 time exceeded                1           0]{lang="EN-US"}

[ ICMPv6 parameter problem            1           0]{lang="EN-US"}

[ ICMPv6 packet too big               1           0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x208009571}[显示]{style="font-family:宋体"}[本机攻击防范统计信息]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense statistics local]{lang="EN-US"}]{#struct_0_12741_x1014_1707980881}

[Attack policy name: abc]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Scan attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ Port scan                           2           23]{lang="EN-US"}

[ IP sweep                            3           33]{lang="EN-US"}

[ Distribute port scan                1           10]{lang="EN-US"}

[Flood attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ SYN flood                           1           0]{lang="EN-US"}

[ ACK flood                           1           0]{lang="EN-US"}

[ SYN-ACK flood                       3           5000]{lang="EN-US"}

[ RST flood                           2           0]{lang="EN-US"}

[ FIN flood                           2           0]{lang="EN-US"}

[ UDP flood                           1           0]{lang="EN-US"}

[ ICMP flood                          1           0]{lang="EN-US"}

[ ICMPv6 flood                        1           0]{lang="EN-US"}

[ DNS flood                           1           0]{lang="EN-US"}

[ HTTP flood                          1           0]{lang="EN-US"}

[Signature attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ IP option record route              1           100]{lang="EN-US"}

[ IP option security                  2           0]{lang="EN-US"}

[ IP option stream ID                 3           0]{lang="EN-US"}

[ IP option internet timestamp        4           1]{lang="EN-US"}

[ IP option loose source routing      5           0]{lang="EN-US"}

[ IP option strict source routing     6           0]{lang="EN-US"}

[ IP option route alert               3           0 ]{lang="EN-US"}

[ Fragment                            1           0]{lang="EN-US"}

[ Impossible                          1           1]{lang="EN-US"}

[ Teardrop                            1           1]{lang="EN-US"}

[ Tiny fragment                       1           0]{lang="EN-US"}

[ IP options abnormal                 3           0]{lang="EN-US"}

[ Smurf                               1           0]{lang="EN-US"}

[ Ping of death                       1           0]{lang="EN-US"}

[ Traceroute                          1           0]{lang="EN-US"}

[ Large ICMP                          1           0]{lang="EN-US"}

[ TCP NULL flag                       1           0]{lang="EN-US"}

[ TCP all flags                       1           0]{lang="EN-US"}

[ TCP SYN-FIN flags                   1           0]{lang="EN-US"}

[ TCP FIN only flag                   1           0]{lang="EN-US"}

[ TCP invalid flag                    1           0]{lang="EN-US"}

[ TCP Land                            1           0]{lang="EN-US"}

[ Winnuke                             1           0]{lang="EN-US"}

[ UDP Bomb                            1           0]{lang="EN-US"}

[ Snork                               1           0 ]{lang="EN-US"}

[ Fraggle                             1           0]{lang="EN-US"}

[ Large ICMPv6                        1           0 ]{lang="EN-US"}

[ ICMP echo request                   1           0]{lang="EN-US"}

[ ICMP echo reply                     1           0]{lang="EN-US"}

[ ICMP source quench                  1           0]{lang="EN-US"}

[ ICMP destination unreachable        1           0]{lang="EN-US"}

[ ICMP redirect                       2           0]{lang="EN-US"}

[ ICMP time exceeded                  3           0]{lang="EN-US"}

[ ICMP parameter problem              4           0]{lang="EN-US"}

[ ICMP timestamp request              5           0]{lang="EN-US"}

[ ICMP timestamp reply                6           0]{lang="EN-US"}

[ ICMP information request            7           0]{lang="EN-US"}

[ ICMP information reply              4           0]{lang="EN-US"}

[ ICMP address mask request           2           0]{lang="EN-US"}

[ ICMP address mask reply             1           0]{lang="EN-US"}

[ ICMPv6 echo request                 1           1]{lang="EN-US"}

[ ICMPv6 echo reply                   1           1]{lang="EN-US"}

[ ICMPv6 group membership query       1           0]{lang="EN-US"}

[ ICMPv6 group membership report      1           0]{lang="EN-US"}

[ ICMPv6 group membership reduction   1           0]{lang="EN-US"}

[ ICMPv6 destination unreachable      1           0]{lang="EN-US"}

[ ICMPv6 time exceeded                1           0]{lang="EN-US"}

[ ICMPv6 parameter problem            1           0]{lang="EN-US"}

[ ICMPv6 packet too big               1           0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1950622410}[显示]{style="font-family:宋体"}[本机攻击防范统计信息]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display attack-defense statistics local]{lang="EN-US"}]{#struct_0_12741_x1014_948465994}

[Attack policy name: abc]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Scan attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ Port scan                           2           23]{lang="EN-US"}

[ IP sweep                            3           33]{lang="EN-US"}

[ Distribute port scan                1           10]{lang="EN-US"}

[Flood attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ SYN flood                           1           0]{lang="EN-US"}

[ ACK flood                           1           0]{lang="EN-US"}

[ SYN-ACK flood                       3           5000]{lang="EN-US"}

[ RST flood                           2           0]{lang="EN-US"}

[ FIN flood                           2           0]{lang="EN-US"}

[ UDP flood                           1           0]{lang="EN-US"}

[ ICMP flood                          1           0]{lang="EN-US"}

[ ICMPv6 flood                        1           0]{lang="EN-US"}

[ DNS flood                           1           0]{lang="EN-US"}

[ HTTP flood                          1           0]{lang="EN-US"}

[Signature attack defense statistics:]{lang="EN-US"}

[ AttackType                          AttackTimes Dropped]{lang="EN-US"}

[ IP option record route              1           100]{lang="EN-US"}

[ IP option security                  2           0]{lang="EN-US"}

[ IP option stream ID                 3           0]{lang="EN-US"}

[ IP option internet timestamp        4           1]{lang="EN-US"}

[ IP option loose source routing      5           0]{lang="EN-US"}

[ IP option strict source routing     6           0]{lang="EN-US"}

[ IP option route alert               3           0 ]{lang="EN-US"}

[ Fragment                            1           0]{lang="EN-US"}

[ Impossible                          1           1]{lang="EN-US"}

[ Teardrop                            1           1]{lang="EN-US"}

[ Tiny fragment                       1           0]{lang="EN-US"}

[ IP options abnormal                 3           0]{lang="EN-US"}

[ Smurf                               1           0]{lang="EN-US"}

[ Ping of death                       1           0]{lang="EN-US"}

[ Traceroute                          1           0]{lang="EN-US"}

[ Large ICMP                          1           0]{lang="EN-US"}

[ TCP NULL flag                       1           0]{lang="EN-US"}

[ TCP all flags                       1           0]{lang="EN-US"}

[ TCP SYN-FIN flags                   1           0]{lang="EN-US"}

[ TCP FIN only flag                   1           0]{lang="EN-US"}

[ TCP invalid flag                    1           0]{lang="EN-US"}

[ TCP Land                            1           0]{lang="EN-US"}

[ Winnuke                             1           0]{lang="EN-US"}

[ UDP Bomb                            1           0]{lang="EN-US"}

[ Snork                               1           0 ]{lang="EN-US"}

[ Fraggle                             1           0]{lang="EN-US"}

[ Large ICMPv6                        1           0 ]{lang="EN-US"}

[ ICMP echo request                   1           0]{lang="EN-US"}

[ ICMP echo reply                     1           0]{lang="EN-US"}

[ ICMP source quench                  1           0]{lang="EN-US"}

[ ICMP destination unreachable        1           0]{lang="EN-US"}

[ ICMP redirect                       2           0]{lang="EN-US"}

[ ICMP time exceeded                  3           0]{lang="EN-US"}

[ ICMP parameter problem              4           0]{lang="EN-US"}

[ ICMP timestamp request              5           0]{lang="EN-US"}

[ ICMP timestamp reply                6           0]{lang="EN-US"}

[ ICMP information request            7           0]{lang="EN-US"}

[ ICMP information reply              4           0]{lang="EN-US"}

[ ICMP address mask request           2           0]{lang="EN-US"}

[ ICMP address mask reply             1           0]{lang="EN-US"}

[ ICMPv6 echo request                 1           1]{lang="EN-US"}

[ ICMPv6 echo reply                   1           1]{lang="EN-US"}

[ ICMPv6 group membership query       1           0]{lang="EN-US"}

[ ICMPv6 group membership report      1           0]{lang="EN-US"}

[ ICMPv6 group membership reduction   1           0]{lang="EN-US"}

[ ICMPv6 destination unreachable      1           0]{lang="EN-US"}

[ ICMPv6 time exceeded                1           0]{lang="EN-US"}

[ ICMPv6 parameter problem            1           0]{lang="EN-US"}

[ ICMPv6 packet too big               1           0]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[d]{lang="EN-US"}]{#struct_0_12741_x1014_1153524887}[isplay attack-defense statistics local]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x653328455}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1480151562}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1737944048}

[[AttackType]{lang="EN-US"}]{#struct_0_12741_x1014_x908181109}

[[攻击类型]{style="font-family:宋体"}]{#struct_0_12741_x1014_1931044218}

[[AttackTimes]{lang="EN-US"}]{#struct_0_12741_x1014_x404471122}

[[受到攻击的次数]{style="font-family:宋体"}]{#struct_0_12741_x1014_479356415}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_x617617947}

[[丢弃报文的数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x460109955}

[[Port scan]{lang="EN-US"}]{#struct_0_12741_x1014_1095204735}

[[端口扫描]{style="font-family:宋体"}]{#struct_0_12741_x1014_1094680448}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP Sweep]{lang="EN-US"}]{#struct_0_12741_x1014_1094549376}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1094942592}[扫描攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Distribute port scan]{lang="EN-US"}]{#struct_0_12741_x1014_1094811520}

[[分布式端口扫描]{style="font-family:宋体"}]{#struct_0_12741_x1014_1095204736}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_1503719553}

[[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_1515928822}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_414165207}

[[ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1712634270}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1827471528}

[[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1954144252}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_1995652553}

[[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_x2118226128}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_780090515}

[[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_901411827}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1266993129}

[[UDP flood ]{lang="EN-US"}]{#struct_0_12741_x1014_1184804980}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1174489310}

[[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x908780785}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1944063603}

[[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_2111199872}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_1702176889}

[[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1300034312}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x914567950}

[[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_818628382}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option record  route]{lang="EN-US"}]{#struct_0_12741_x1014_630893989}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_813310070}[选项]{style="font-family:宋体"}[record route]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option security]{lang="EN-US"}]{#struct_0_12741_x1014_x641257789}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_66308508}[选项]{style="font-family:宋体"}[security]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option stream ID]{lang="EN-US"}]{#struct_0_12741_x1014_1707915345}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1563727411}[选项]{style="font-family:宋体"}[stream ]{lang="EN-US"}[identifier]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option internet timestamp]{lang="EN-US"}]{#struct_0_12741_x1014_x1678724025}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_1656091129}[选项]{style="font-family:宋体"}[ internet timestamp]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option loose source routing]{lang="EN-US"}]{#struct_0_12741_x1014_x214398956}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1997310183}[选项]{style="font-family:宋体"}[loose source routing]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option strict source routing]{lang="EN-US"}]{#struct_0_12741_x1014_1487170522}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_209483601}[选项]{style="font-family:宋体"}[strict source routing]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[IP option route alert]{lang="EN-US"}]{#struct_0_12741_x1014_710816859}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1780482897}[选项]{style="font-family:宋体"}[strict source routing]{lang="EN-US"}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Fragment]{lang="EN-US"}]{#struct_0_12741_x1014_x522904079}

[[IP]{lang="EN-US"}]{#struct_0_12741_x1014_914698061}[分片异常攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Impossible]{lang="EN-US"}]{#struct_0_12741_x1014_948400458}

[[IP impossible]{lang="EN-US"}]{#struct_0_12741_x1014_x905287826}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Teardrop]{lang="EN-US"}]{#struct_0_12741_x1014_x855421297}

[[IP teardrop]{lang="EN-US"}]{#struct_0_12741_x1014_x617683483}[攻击，又称]{style="font-family:宋体"}[IP overlapping fragments]{lang="EN-US"}[，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Tiny fragment]{lang="EN-US"}]{#struct_0_12741_x1014_1532720405}

[[IP tiny fragment]{lang="EN-US"}]{#struct_0_12741_x1014_x511306567}[攻击]{style="font-family:宋体"}

[[IP option abnormal]{lang="EN-US"}]{#struct_0_12741_x1014_x893600885}

[[IP ]{lang="EN-US"}]{#struct_0_12741_x1014_x1827537064}[选项异常攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Smurf ]{lang="EN-US"}]{#struct_0_12741_x1014_1909988407}

[[Smurf]{lang="EN-US"}]{#struct_0_12741_x1014_1534707611}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Ping of death]{lang="EN-US"}]{#struct_0_12741_x1014_901346291}

[[Ping of death]{lang="EN-US"}]{#struct_0_12741_x1014_1058355474}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Traceroute ]{lang="EN-US"}]{#struct_0_12741_x1014_60677676}

[[Traceroute]{lang="EN-US"}]{#struct_0_12741_x1014_567374688}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Large ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_2111134336}

[[Large ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_1700121260}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为[0]{lang="EN-US"}时，该列不显示]{style="font-family:宋体"}

[[TCP NULL flag]{lang="EN-US"}]{#struct_0_12741_x1014_1158781035}

[[TCP NULL flag]{lang="EN-US"}]{#struct_0_12741_x1014_545050395}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP all flags]{lang="EN-US"}]{#struct_0_12741_x1014_1117828774}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x989288198}[所有标志位均被置位攻击，又称圣诞树攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP SYN-FIN flags]{lang="EN-US"}]{#struct_0_12741_x1014_x1021033546}

[[TCP SYN]{lang="EN-US"}]{#struct_0_12741_x1014_1292620700}[和]{style="font-family:宋体"}[FIN]{lang="EN-US"}[被同时置位攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP FIN only flag]{lang="EN-US"}]{#struct_0_12741_x1014_1103452267}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_1707849809}[只有]{style="font-family:宋体"}[FIN]{lang="EN-US"}[被置位的攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP invalid flag]{lang="EN-US"}]{#struct_0_12741_x1014_715340884}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x140398725}[非法标志位攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[TCP Land]{lang="EN-US"}]{#struct_0_12741_x1014_204518855}

[[TCP Land]{lang="EN-US"}]{#struct_0_12741_x1014_x214464492}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Winnuke]{lang="EN-US"}]{#struct_0_12741_x1014_x57826032}

[[Winnuke]{lang="EN-US"}]{#struct_0_12741_x1014_x1511128614}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[UDP Bomb]{lang="EN-US"}]{#struct_0_12741_x1014_x1780548433}

[[UDP Bomb]{lang="EN-US"}]{#struct_0_12741_x1014_x1257239995}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Snork]{lang="EN-US"}]{#struct_0_12741_x1014_948334922}

[[Snork]{lang="EN-US"}]{#struct_0_12741_x1014_475948386}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Fraggle]{lang="EN-US"}]{#struct_0_12741_x1014_x606883130}

[[Fraggle]{lang="EN-US"}]{#struct_0_12741_x1014_x617749019}[攻击，又称]{style="font-family:宋体"}[UDP chargen DoS attack]{lang="EN-US"}[，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[Large ICMPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x446954757}

[[Large ICMPv6]{lang="EN-US"}]{#struct_0_12741_x1014_574373700}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP echo request]{lang="EN-US"}]{#struct_0_12741_x1014_x1465455503}

[[ICMP echo request]{lang="EN-US"}]{#struct_0_12741_x1014_x1827602600}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x2036523684}

[[ICMP echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1260232371}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP source quench]{lang="EN-US"}]{#struct_0_12741_x1014_1795484439}

[[ICMP source quench]{lang="EN-US"}]{#struct_0_12741_x1014_901280755}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_1031051347}

[[ICMP destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_859742340}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP redirect ]{lang="EN-US"}]{#struct_0_12741_x1014_x250342400}

[[ICMP redirect]{lang="EN-US"}]{#struct_0_12741_x1014_2111068800}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_155295100}

[[ICMP time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_1535815502}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x1039217397}

[[ICMP parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_544984859}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP timestamp request]{lang="EN-US"}]{#struct_0_12741_x1014_x1951738311}

[[ICMP timestamp request]{lang="EN-US"}]{#struct_0_12741_x1014_x1537290281}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP timestamp reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1021099082}

[[ICMP timestamp reply]{lang="EN-US"}]{#struct_0_12741_x1014_1219109741}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP information request]{lang="EN-US"}]{#struct_0_12741_x1014_2002466119}

[[ICMP information request]{lang="EN-US"}]{#struct_0_12741_x1014_1707784273}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP information reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1930299923}

[[ICMP information reply]{lang="EN-US"}]{#struct_0_12741_x1014_778054385}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP address mask request]{lang="EN-US"}]{#struct_0_12741_x1014_1395714248}

[[ICMP address mask request]{lang="EN-US"}]{#struct_0_12741_x1014_x214530028}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMP address mask reply]{lang="EN-US"}]{#struct_0_12741_x1014_1153094268}

[[ICMP address mask reply]{lang="EN-US"}]{#struct_0_12741_x1014_x1695198549}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 echo request]{lang="EN-US"}]{#struct_0_12741_x1014_x1780613969}

[[ICMPv6 echo request]{lang="EN-US"}]{#struct_0_12741_x1014_852809653}[攻击，当]{style="font-family:宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_948269386}

[[ICMPv6 echo reply]{lang="EN-US"}]{#struct_0_12741_x1014_2009538615}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 group membership query]{lang="EN-US"}]{#struct_0_12741_x1014_x617814555}

[[ICMPv6 group membership query]{lang="EN-US"}]{#struct_0_12741_x1014_1137681801}[攻击，当]{style="font-family:
  宋体"}[AttackTimes ]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 group membership report]{lang="EN-US"}]{#struct_0_12741_x1014_x1827668136}

[[ICMPv6 group membership report]{lang="EN-US"}]{#struct_0_12741_x1014_x173182541}[攻击，当]{style="font-family:
  宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 group membership reduction]{lang="EN-US"}]{#struct_0_12741_x1014_901215219}

[[ICMPv6 group membership reduction]{lang="EN-US"}]{#struct_0_12741_x1014_x2102445599}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_2111003264}

[[ICMPv6 destination unreachable]{lang="EN-US"}]{#struct_0_12741_x1014_2118621913}[攻击，当]{style="font-family:
  宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:
  宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_544919323}

[[ICMPv6 time exceeded]{lang="EN-US"}]{#struct_0_12741_x1014_x1574978025}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_x1021164618}

[[ICMPv6 parameter problem]{lang="EN-US"}]{#struct_0_12741_x1014_468865752}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[[ICMPv6 packet too big]{lang="EN-US"}]{#struct_0_12741_x1014_1707718737}

[[ICMPv6 packet too big]{lang="EN-US"}]{#struct_0_12741_x1014_1563150429}[攻击，当]{style="font-family:宋体"}[AttackTimes]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，该列不显示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x69512274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset attack-defense statistics local]{lang="EN-US"}**]{#struct_0_12741_x1014_1850817639}

::::: {#-933695044 .myid}
[]{#_Toc404793903}[]{#struct_0_12741_x1014_1921905613}[]{#_Toc340488499}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display blacklist ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x214595564}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x462671791}
:::

[ ]{lang="EN-US"}

[**[display blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1017539032}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_770352817}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2121552207}

[**[display blacklist]{lang="EN-US"}**[ **ip** \[ *source-ip-address* \[ **vpn-instance** *vpn-instance-name* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1373623199}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x425516894}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display blacklist ip ]{lang="EN-US"}**[\[ *source-ip-address* \[ **vpn-instance** *vpn-instance-name* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1807357964}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_322732508}[模式：]{style="font-family:宋体"}

[**[display blacklist]{lang="EN-US"}[ ip]{lang="EN-US"}**[ \[ *source-ip-address* \[ **vpn-instance** *vpn-instance-name* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1021300020}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1780679505}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x76551297}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_873597535}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1576343352}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1619931218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_170954593}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_940403278}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1257527364}

[*[source-ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1294726187}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的黑名单表项。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1378532998}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_855749869}[：显示指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_948203850}[：显示指定成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_536633418}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1091440606}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1029450523}[：显示指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_1638824344}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_1084178858}[：]{style="font-family:宋体"}[显示符合指定条件的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_644272768}

[[若不指定任何参数，则表示显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_2017844795}[黑名单表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1176816145}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_2031021989}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1046637577}

[IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped]{lang="EN-US"}

[192.168.11.5    \--             \--                   Dynamic 10       353452]{lang="EN-US"}

[123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295]{lang="EN-US"}

[201.55.7.45     abc            2013::1              Manual  Never   14478]{lang="EN-US"}

[[ # ]{lang="EN-US"}]{#struct_0_12741_x1014_x617880091}[显示]{style="font-family:宋体"}[Slot 1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项的信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ip slot 1]{lang="EN-US"}]{#struct_0_12741_x1014_1893978921}

[Slot 1:]{lang="EN-US"}

[IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped]{lang="EN-US"}

[192.168.11.5    \--             \--                   Dynamic 10       353452]{lang="EN-US"}

[123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295]{lang="EN-US"}

[201.55.7.45     abc            2013::1              Manual  Never   14478]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_631288492}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项的信息。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633940767}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped]{lang="EN-US"}

[192.168.11.5    \--             \--                   Dynamic 10       353452]{lang="EN-US"}

[123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295]{lang="EN-US"}

[201.55.7.45     abc            2013::1              Manual  Never   14478]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped]{lang="EN-US"}

[192.168.11.5    \--             \--                   Dynamic 10       353452]{lang="EN-US"}

[123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295]{lang="EN-US"}

[201.55.7.45     abc            2013::1              Manual  Never   14478]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x858941088}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x645235109}

[Totally 3 blacklist entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_2142679770}[显示]{style="font-family:宋体"}[Slot 1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项的]{style="font-family:宋体"}[个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ip slot 1 count]{lang="EN-US"}]{#struct_0_12741_x1014_x316321523}

[Slot 1:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1579376035}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单表项的]{style="font-family:宋体"}[个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1634071839}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display blacklist ip]{lang="EN-US"}]{#struct_0_12741_x1014_1157696384}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x613914041}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x366384843}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x162466989}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_x1336484626}

[[黑名单表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1117088706}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_x1010521603}

[[VPN]{lang="EN-US"}]{#struct_0_12741_x1014_525938662}[实例名称，属于公网时显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_12741_x1014_x2049746304}

[[DS-Lite]{lang="EN-US"}]{#struct_0_12741_x1014_1666486607}[隧道对端地址]{style="font-family:宋体"} [。]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[组网下，若本设备为]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[，此列表示报文来自具体的哪个]{style="font-family:宋体"}[B4]{lang="EN-US"}[，如果不在]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[组网或本设备不为]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[，则该字段无意义，显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12741_x1014_x700641559}

[[黑名单表项的添加方式]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1183619517}

[[TTL(sec)]{lang="EN-US"}]{#struct_0_12741_x1014_887384006}

[[黑名单表项的剩余老化时间，单位为秒。若未指定老化时间，则显示"]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_12741_x1014_1453281178}["]{style="font-family:宋体"}

[[Dropped ]{lang="EN-US"}]{#struct_0_12741_x1014_679137051}

[[丢弃的来自该]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_337132165}[地址的报文数目]{style="font-family:宋体"}

[[Totally 3 blacklist entries.]{lang="EN-US"}]{#struct_0_12741_x1014_1519302534}

[[黑名单表项数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1817699314}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x600380328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_958525726}

::::: {#2033459765 .myid}
[]{#_Toc404793904}[]{#struct_0_12741_x1014_x1479478514}[]{#_Toc349981964}[]{#_Toc349981965}[]{#_Toc349981966}[]{#_Toc349981967}[]{#_Toc349981968}[]{#_Toc349981969}[]{#_Toc349981970}[]{#_Toc349981971}[]{#_Toc349981972}[]{#_Toc349981973}[]{#_Toc349981974}[]{#_Toc349981975}[]{#_Toc349981976}[]{#_Toc349981977}[]{#_Toc349981978}[]{#_Toc349981979}[]{#_Toc349981980}[]{#_Toc349981981}[]{#_Toc349981982}[]{#_Toc349981983}[]{#_Toc349981984}[]{#_Toc349981985}[]{#_Toc349981986}[]{#_Toc349981987}[]{#_Toc349981988}[]{#_Toc349981989}[]{#_Toc349981990}[]{#_Toc349981991}[]{#_Toc349981992}[]{#_Toc349981993}[]{#_Toc349981995}[]{#_Toc349981996}[]{#_Toc349981997}[]{#_Toc349981998}[]{#_Toc349981999}[]{#_Toc349982000}[]{#_Toc349982001}[]{#_Toc349982002}[]{#_Toc349982003}[]{#_Toc349982004}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display blacklist ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x886946890}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x1360515442}
:::

[ ]{lang="EN-US"}

[**[display blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1616720274}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1520043196}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_621121961}

[**[display blacklist]{lang="EN-US"}**[ **ipv6** \[ *source-ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1356195940}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x1967720955}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display blacklist ipv6 ]{lang="EN-US"}**[\[ *source-ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1050952608}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x2127152460}[模式：]{style="font-family:宋体"}

[**[display blacklist]{lang="EN-US"}[ ipv6]{lang="EN-US"}**[ \[ *source-ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x2124356098}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1841936465}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_213616399}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_305495259}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1634651589}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1721147250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1258012456}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x476824610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x397290130}

[*[source-ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1115854684}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的黑名单表项。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_1030674065}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x80377836}[：显示指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1370646949}[：显示指定成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1296082769}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1536309731}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1984393085}[：显示指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_1897350519}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x2004461359}[：]{style="font-family:宋体"}[仅显示符合指定条件的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1183178439}

[[若不指定任何参数，则表示显示所有的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_x1045966214}[黑名单表项。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1508170748}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1558455246}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1646461777}

[Totally 3 blacklist entries.]{lang="EN-US"}

[IPv6 address         VPN instance      Type    TTL(sec) Dropped]{lang="EN-US"}

[1::4                 \--                Manual  Never   14478]{lang="EN-US"}

[1::5                 \--                Dynamic 10       353452]{lang="EN-US"}

[2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295]{lang="EN-US"}

[2013:fe07:221a:4011  67890123456789]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1976695809}[显示]{style="font-family:宋体"}[Slot 1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项的信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ipv6 slot 1]{lang="EN-US"}]{#struct_0_12741_x1014_x913337706}

[Slot 1:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[IPv6 address         VPN instance      Type    TTL(sec) Dropped]{lang="EN-US"}

[1::4                 \--                Manual  Never   14478]{lang="EN-US"}

[1::5                 \--                Dynamic 10       353452]{lang="EN-US"}

[2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295]{lang="EN-US"}

[2013:fe07:221a:4011  67890123456789]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1419950377}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项的信息。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_1082421578}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[IPv6 address         VPN instance      Type    TTL(sec) Dropped]{lang="EN-US"}

[1::4                 \--                Manual  Never   14478]{lang="EN-US"}

[1::5                 \--                Dynamic 10       353452]{lang="EN-US"}

[2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295]{lang="EN-US"}

[2013:fe07:221a:4011  67890123456789]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[IPv6 address         VPN instance      Type    TTL(sec) Dropped]{lang="EN-US"}

[1::4                 \--                Manual  Never   14478]{lang="EN-US"}

[1::5                 \--                Dynamic 10       353452]{lang="EN-US"}

[2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295]{lang="EN-US"}

[2013:fe07:221a:4011  67890123456789]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x2015368314}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x1745953795}

[Totally 3 blacklist entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x209138978}[显示]{style="font-family:宋体"}[Slot 1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项的]{style="font-family:宋体"}[个数]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ipv6 slot 1 count]{lang="EN-US"}]{#struct_0_12741_x1014_1045927346}

[Slot 1:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1784675244}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单表项的个数。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display blacklist ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x483662363}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 blacklist entries.]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display blacklist ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1104323592}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x620621723}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1276477553}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_133856133}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12741_x1014_753704924}

[[黑名单表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1181209643}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_x1693515944}

[[VPN]{lang="EN-US"}]{#struct_0_12741_x1014_1875584684}[实例名称，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12741_x1014_921765592}

[[黑名单表项的添加方式]{style="font-family:宋体"}]{#struct_0_12741_x1014_980910170}

[[TTL(sec)]{lang="EN-US"}]{#struct_0_12741_x1014_2146481774}

[[黑名单表项的剩余老化时间，单位为秒。若未指定老化时间，则显示"]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_12741_x1014_1385999475}["]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_12741_x1014_1035367411}

[[丢弃的来自该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1344293010}[地址的报文数目]{style="font-family:宋体"}

[[Totally 3 blacklist entries.]{lang="EN-US"}]{#struct_0_12741_x1014_1466897537}

[[黑名单表项数目]{style="font-family:宋体"}]{#struct_0_12741_x1014_x162757886}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x956608084}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1639356331}

::::: {#1305790763 .myid}
[]{#_Toc404793905}[]{#struct_0_12741_x1014_x879023100}[]{#_Toc279431620}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify protected ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x1316653514}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x2049811840}
:::

[ ]{lang="EN-US"}

[**[display client-verify protected]{lang="EN-US"}**[ **ip**]{lang="EN-US"}]{#struct_0_12741_x1014_x1557541445}[命令用来显示客户端验证的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1495192161}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_826109786}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected**]{lang="EN-US"}[ **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **port** *port-number* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x376463980}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x390105310}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected**]{lang="EN-US"}[ **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **port** *port-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_218268532}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_1231860280}[模式：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected** ]{lang="EN-US"}**[ip ]{lang="EN-US"}**[\[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **port** *port-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1495471131}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x718347377}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_679071515}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_309827566}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1145066056}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1162644825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1661704412}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_524428757}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1606085638}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_1712089843}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_798766437}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_x809750737}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x587402872}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x827696198}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示显示公网中]{style="font-family:宋体"}[的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1634006300}[：]{style="font-family:宋体"}[显示指定端口号的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。若不指定该参数，对于]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示]{style="font-family:宋体"}[端口]{style="font-family:宋体"}[53]{lang="EN-US"}[；对于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示]{style="font-family:宋体"}[端]{style="font-family:宋体"}[口]{style="font-family:宋体"}[80]{lang="EN-US"}[；对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示]{style="font-family:宋体"}[所有端口。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_2071664747}[：显示指定单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－独立运行模式）。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x887012426}[：显示指定成员设备上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x222947005}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x2124653870}[：显示指定成员设备上指定单板的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1699301760}[：显示指定单板的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_2033837543}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_350857669}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[符合指定条件的]{style="font-family:宋体"}[客户端验证受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_384173305}

[[如果不指定任何参数，则显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x379919306}[类型的客户端验证受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1285228359}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_876794591}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1634071836}

[IP address           VPN instance     Port  Type    Requested  Trusted]{lang="EN-US"}

[192.168.11.5         \--               23    Dynamic 353452     555]{lang="EN-US"}

[123.123.123.123      VPN1             65535 Dynamic 4294967295 15151]{lang="EN-US"}

[201.55.7.45          \--               10    Manual  15000      222]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x943978530}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x990595446}

[Slot 1:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               23    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               10    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               23    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               10    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x80443372}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633678620}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               23    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               10    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               23    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               10    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_194177123}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1634202907}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1622053472}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1634268443}

[Slot 1:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1082356042}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1633875227}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x305747843}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633940763}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               53    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               53    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_838574823}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1634006299}

[Slot 1:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               53    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               53    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               53    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               53    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1824296549}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633613083}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               53    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               53    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               53    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               53    Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1291019009}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1634137370}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1632728950}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1634202906}

[Slot 1:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x875846595}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1634333978}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1554992992}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633875226}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               80    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               8080  Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_126753426}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633940762}

[Slot 1:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               80    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               8080  Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               80    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               8080  Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1801427762}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1633613082}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               80    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               8080  Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address           VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[192.168.11.5         \--               80    Dynamic 353452      555]{lang="EN-US"}

[201.55.7.45          \--               8080  Manual  15000       222]{lang="EN-US"}

[123.123.123.123      VPN1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1285686198}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1633678618}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1264443240}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037421902}

[Slot 1:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1109809069}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037552974}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 protected IP addresses.]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display client-verify protected ip]{lang="EN-US"}]{#struct_0_12741_x1014_32453037}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x590070137}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_177127227}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1584406145}

[[Totally 3 protected IP addresses.]{lang="EN-US"}]{#struct_0_12741_x1014_1255366687}

[[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x975476342}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项数目]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_1082290506}

[[受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x463898700}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_1336966384}

[[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1805178170}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，]{style="font-family:宋体"}[属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_12741_x1014_x1349420306}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_338734964}[连接的目的端口]{style="font-family:宋体"}

[[any]{lang="EN-US"}]{#struct_0_12741_x1014_x483793435}[表示对该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的所有端口的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求都做代理]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12741_x1014_791859317}

[[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_910855474}[地址的添加方式，取值包括]{style="font-family:宋体"}[Dynamic]{lang="EN-US"}[和]{style="font-family:宋体"}[Manual]{lang="EN-US"}

[[Requested]{lang="EN-US"}]{#struct_0_12741_x1014_x145484841}

[[收到的匹配该受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_422461158}[地址的报文数目]{style="font-family:宋体"}

[[Trusted]{lang="EN-US"}]{#struct_0_12741_x1014_1101304886}

[[通过验证的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x1693647016}[连接请求报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1477652126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify protected ip]{lang="EN-US"}**]{#struct_0_12741_x1014_44047865}

::::: {#1531728780 .myid}
[]{#_Toc404793906}[]{#struct_0_12741_x1014_x450364219}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify protected ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1499144125}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_913517304}
:::

[ ]{lang="EN-US"}

[**[display client-verify protected]{lang="EN-US"}**[ **ipv6**]{lang="EN-US"}]{#struct_0_12741_x1014_10266531}[命令用来显示客户端验证的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1508278770}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_1915209990}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected**]{lang="EN-US"}[ **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **port** *port-number* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_418067867}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_1035236339}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected**]{lang="EN-US"}[ **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **port** *port-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1330172892}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x275469059}[模式：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } **protected** ]{lang="EN-US"}**[ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **port** *port-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x2000623345}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x305599605}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_336857782}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1187808274}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x416492313}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1479546522}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1927489498}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x912503594}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2049942912}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_1026336803}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_1571965645}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_x572550732}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1642791520}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1279870963}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示显示公网中]{style="font-family:宋体"}[的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x2037290830}[：]{style="font-family:宋体"}[显示指定端口号的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。若不指定该参数，对于]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示]{style="font-family:宋体"}[端口]{style="font-family:宋体"}[53]{lang="EN-US"}[；对于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示]{style="font-family:宋体"}[端]{style="font-family:宋体"}[口]{style="font-family:宋体"}[80]{lang="EN-US"}[；对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[，则表示]{style="font-family:宋体"}[所有端口。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1546117958}[：显示指定单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－独立运行模式）。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x758055758}[：显示指定成员设备上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_133152283}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1375971994}[：显示指定成员设备上指定单板的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_533659053}[：显示指定单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1425096882}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_678940443}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[符合指定条件的]{style="font-family:宋体"}[客户端验证受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项个数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_819014513}

[[如果不指定任何参数，则显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1432931658}[类型的客户端验证受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_917644209}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1656109912}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037356366}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_590925765}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2036897614}

[Slot 1:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1638805923}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037421901}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             65535 Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1423540039}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037552973}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_59360237}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip ]{lang="EN-US"}]{#struct_0_12741_x1014_x2037618509}[count]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1436628030}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp protected ip ]{lang="EN-US"}]{#struct_0_12741_x1014_x2037159757}[count]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x378479666}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037225293}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1153180403}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037356365}

[Slot 1:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x646330171}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2036897613}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             53    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1561495995}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037421900}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_202815224}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037487436}

[Slot 1:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1296666732}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037552972}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 protected entries.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 protected entries.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_251335932}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037618508}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1929466279}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037225292}

[Slot 1:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1619188167}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP ]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x2037290828}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address         VPN instance     Port  Type    Requested   Trusted]{lang="EN-US"}

[1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501]{lang="EN-US"}

[1023::1123           vpn1             80    Dynamic 4294967295  15151]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1934534747}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2036897612}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x2101186257}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2036963148}

[Slot 1:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1288158710}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP ]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的个数。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http protected ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037421899}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 protected IPv6 addresses.]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display client-verify protected ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_284228091}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x587262925}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_482883348}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1841674321}

[[Totally 3 protected IPv6 addresses]{lang="EN-US"}]{#struct_0_12741_x1014_177959206}

[[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1661198953}[类型受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项数目]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12741_x1014_x50159036}

[[受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_2059333960}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_1966914074}

[[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_2024482068}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}[，属于公网时]{style="font-family:宋体"}[显示为"[\--]{lang="EN-US"}"]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_12741_x1014_853807383}

[[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x80639980}[连接的目的端口]{style="font-family:宋体"}

[[any]{lang="EN-US"}]{#struct_0_12741_x1014_x1963259276}[表示对该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的所有端口的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求都做代理]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12741_x1014_x1054809831}

[[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1729460271}[地址的添加方式，取值包括]{style="font-family:宋体"}[Dynamic]{lang="EN-US"}[和]{style="font-family:宋体"}[Manual]{lang="EN-US"}

[[Requested]{lang="EN-US"}]{#struct_0_12741_x1014_x380751280}

[[收到的匹配该受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x289883728}[地址的报文数目]{style="font-family:宋体"}

[[Trusted]{lang="EN-US"}]{#struct_0_12741_x1014_x1415196459}

[[通过验证的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12741_x1014_x1646723921}[连接请求报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x660904359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify protected ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1833241585}

::::: {#1198698068 .myid}
[]{#_Toc404793907}[]{#struct_0_12741_x1014_377816892}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify trusted ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x124352629}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_1028581935}
:::

[ ]{lang="EN-US"}

[**[display client-verify trusted ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1436506153}[命令用来显示客户端验证的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_960442587}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_1082159434}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted]{lang="EN-US"}**[ **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x420853995}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x700817484}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted]{lang="EN-US"}**[ **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1937461182}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_1572446212}[模式：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted]{lang="EN-US"}**[ **ip** \[ *ip-address* \[ **vpn** *vpn-instance-name* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x731647963}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1443988741}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1967528053}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1311178553}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1559057949}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x483924507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x772794437}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1113249034}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x781044319}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_x1778968974}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_1455424740}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_2001359389}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1356214337}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_1124638905}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[若不指定该参数，则表示信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[位于公网。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1693778088}[：显示指定单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－独立运行模式）。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_550058601}[：显示指定成员设备上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1432997194}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_101645439}[：显示指定成员设备上指定单板的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_837642491}[：显示指定单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）。]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1991125228}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x2037159755}[：仅]{style="font-family:宋体"}[显示符合指定条件的]{style="font-family:宋体"}[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[的]{style="font-family:宋体"}[个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2058842243}

[[如果不指定任何参数，则显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_1295886161}[类型的客户端验证]{style="font-family:宋体"}[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1714799861}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_207502762}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1164808305}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1035105267}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_1418644983}

[Slot 1:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.3        vpn1                \--                     1200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x513419433}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2037290827}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.3        vpn1                \--                     1200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_56026790}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1902498526}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x2050073984}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x961404066}

[Slot 1:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_2002973622}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x2036897611}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1298032915}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x1311215754}

[Totally 2 trusted addresses.]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_414712245}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_678809371}

[Slot 1:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1246946640}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2037421898}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_338970551}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_1494726171}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1530052215}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x887274570}

[Slot 1:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x985655635}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x2037552970}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x77507444}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2037618506}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                    3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1438769857}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2037159754}

[Slot 1:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1451391088}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_x2037290826}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)]{lang="EN-US"}

[11.1.1.2        vpn1                \--                     3600]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1513148056}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP ]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_785115307}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1873259930}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x1646789457}

[Slot 1:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1578303554}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ip count]{lang="EN-US"}]{#struct_0_12741_x1014_x2036897610}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 trusted IP addresses.]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display client-verify trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_1621030578}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x591799229}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_12741_x1014_721433574}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1082093898}

[[Totally 3 trusted IP addresses]{lang="EN-US"}]{#struct_0_12741_x1014_x2000485682}

[[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_113100475}[类型信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_12741_x1014_295649970}

[[信任]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_12741_x1014_x1880798895}[地址]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_x1253744671}

[[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_669021752}[地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，属于公网时显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_12741_x1014_x1403539582}

[[DS-Lite]{lang="EN-US"}]{#struct_0_12741_x1014_x483990043}[隧道对端地址。]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[组网下，若本设备为]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[，此列表示报文来自具体的哪个]{style="font-family:宋体"}[B4]{lang="EN-US"}[，如果不在]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[组网或本设备不为]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[，则该字段无意义，显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[TTL(sec)]{lang="EN-US"}]{#struct_0_12741_x1014_x1539029685}

[[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_842071050}[地址的剩余老化时间，单位为秒。]{style="font-family:宋体"}[若未指定老化时间，则显示"]{style="font-family:宋体"}[Never]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1114143708 .myid}
[]{#_Toc404793908}[]{#struct_0_12741_x1014_459754854}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify trusted ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_950771448}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x1693843624}
:::

[ ]{lang="EN-US"}

[**[display client-verify trusted ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_2091718618}[命令用来显示客户端验证的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x939350220}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x969874892}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted]{lang="EN-US"}**[ **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **count** \] ]{lang="EN-US"}]{#struct_0_12741_x1014_638317627}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12741_x1014_x807451965}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted]{lang="EN-US"}**[ **ipv6** \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_x840014333}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12741_x1014_x977388033}[模式：]{style="font-family:宋体"}

[**[display client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \[ **vpn** *vpn-instance-name* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12741_x1014_1445551433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x870598707}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1265982856}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1035039731}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1774828199}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_931151469}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1167002353}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x989741538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x196626005}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_778243997}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_515910853}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_x580732731}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1540250579}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1915856256}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[若不指定该参数，则表示信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[位于公网。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1508196136}[：显示指定单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x454488831}[：显示指定成员设备上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，则表示显示所有成员设备上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x1566559562}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_x752838814}[：显示指定成员设备上指定单板的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12741_x1014_735792925}[：显示指定单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，则表示显示所有单板上的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x1359898651}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12741_x1014_x2036963145}[：仅]{style="font-family:宋体"}[显示符合指定条件的]{style="font-family:宋体"}[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2071893322}

[[如果不指定任何参数，则显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_1162323793}[类型的客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x541478607}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x840780251}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x471337961}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_832598019}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify ]{lang="EN-US"}]{#struct_0_12741_x1014_x471403497}[dns ]{lang="EN-US"}[trusted ipv6]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x457653318}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify ]{lang="EN-US"}]{#struct_0_12741_x1014_x471469033}[dns ]{lang="EN-US"}[trusted ipv6]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1576986885}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ipv6 count]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_12741_x1014_x2117203255}

[[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}]{#struct_0_12741_x1014_1913364513}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x859246688}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify dns trusted ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x1003080131}

[Slot 1:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_55732592}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify ]{lang="EN-US"}]{#struct_0_12741_x1014_x471141353}[dns ]{lang="EN-US"}[trusted ipv6 ]{lang="EN-US"}[count]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x600535757}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x471206889}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1290033802}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x470813673}

[Slot 1:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x842393704}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x470879209}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x446785798}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x471337960}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x164654929}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify http trusted ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_2053698544}

[Slot 1:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_8306094}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify ]{lang="EN-US"}]{#struct_0_12741_x1014_x471469032}[http ]{lang="EN-US"}[trusted ipv6 ]{lang="EN-US"}[count]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1331130257}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x471534568}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x842091823}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x471075816}

[Slot 1:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1738348607}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x471206888}

[Slot 1 in chassis 0:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[1234::1234                              a012345678901234 1234]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[IPv6 address                            VPN instance     TTL(sec)]{lang="EN-US"}

[1::3                                    vpn1             1643]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1276845652}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_x471272424}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1726317646}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的个数。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify tcp trusted ipv6 count]{lang="EN-US"}]{#struct_0_12741_x1014_2044444523}

[Slot 1:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_194340207}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display client-verify ]{lang="EN-US"}]{#struct_0_12741_x1014_x470879208}[tcp ]{lang="EN-US"}[trusted ipv6 ]{lang="EN-US"}[count]{lang="EN-US"}

[Slot 1 in chassis 0:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[Slot 2 in chassis 1:]{lang="EN-US"}

[Totally 3 trusted IPv6 addresses.]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display client-verify trusted ipv6]{lang="EN-US"}]{#struct_0_12741_x1014_x271909126}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x599257925}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_x575608465}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_12741_x1014_1144085994}

[[Totally 3 trusted IPv6 addresses]{lang="EN-US"}]{#struct_0_12741_x1014_411231740}

[[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1519557474}[类型信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的个数]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12741_x1014_x34541208}

[[信任]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_x1311168480}[地址]{style="font-family:宋体"}

[[TTL(sec)]{lang="EN-US"}]{#struct_0_12741_x1014_812961563}

[[信任]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1163521881}[地址的剩余老化时间，单位为秒。若未指定老化时间，则显示"]{style="font-family:宋体"}[Never]{lang="EN-US"}["]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_12741_x1014_653510604}

[[VPN]{lang="EN-US"}]{#struct_0_12741_x1014_134548994}[实例名称，属于公网时显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1236307615 .myid}
[]{#_Toc404793909}[]{#struct_0_12741_x1014_x946381631}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood action**

------------------------------------------------------------------------

[**[dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x422804085}[命令用来配置对]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1123561336}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_18196439}

[**[dns-flood action]{lang="EN-US"}**[ { **client-verify** \| **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_x753122378}

[**[undo dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1015023820}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_947693398}

[[不对检测到的]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_x332674933}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1126821786}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1084248507}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2044331401}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1382241459}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1495576261}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1599357242}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x473379474}[：表示自动将受到攻击]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加]{style="font-family:宋体"}[到]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1640044366}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_1975760977}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1939879085}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_574112856}[参数的使用需要和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的接口检测到]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_576313224}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x207803430}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置对]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的全局处理行为是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1700560204}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] dns-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1585306810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}[-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1949973373}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_381266340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}[-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1150525204}**[threshold]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1153704601}**[dns]{lang="EN-US"}[ ]{lang="EN-US"}[enable]{lang="EN-US"}**
:::

::: {#-652696510 .myid}
[]{#_Toc404793910}[]{#struct_0_12741_x1014_53446676}[]{#_Toc349982008}[]{#_Toc349982009}[]{#_Toc349982010}[]{#_Toc349982011}[]{#_Toc349982012}[]{#_Toc349982013}[]{#_Toc349982014}[]{#_Toc349982015}[]{#_Toc349982016}[]{#_Toc349982017}[]{#_Toc349982018}[]{#_Toc349982019}[]{#_Toc349982020}[]{#_Toc349982021}[]{#_Toc349982022}[]{#_Toc349982023}[]{#_Toc349982024}[]{#_Toc349982025}[]{#_Toc349982026}[]{#_Toc349982027}[]{#_Toc349982028}[]{#_Toc349982029}[]{#_Toc349982030}[]{#_Toc349982031}[]{#_Toc349982032}[]{#_Toc349982033}[]{#_Toc349982034}[]{#_Toc349982035}[]{#_Toc349982036}[]{#_Toc349982037}[]{#_Toc349982038}[]{#_Toc349982040}[]{#_Toc349982041}[]{#_Toc349982042}[]{#_Toc349982043}[]{#_Toc349982044}[]{#_Toc349982045}[]{#_Toc349982046}[]{#_Toc349982047}[]{#_Toc349982048}[]{#_Toc349982049}[]{#_Toc349982052}[]{#_Toc349982053}[]{#_Toc349982054}[]{#_Toc349982055}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood detect**

------------------------------------------------------------------------

[**[dns-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1364726636}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的攻击防范检测，并配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[触发阈值和对]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击的]{style="font-family:宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo dns-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1786109007}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1171676919}

[**[dns-flood detect ]{lang="EN-US"}**[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **port** *port-list* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_95940710}

[**[undo dns-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_702272829}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_171097702}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1463846758}[地址配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1735308588}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1512637265}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1260489662}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x326687991}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1981189382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x783005938}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x685405425}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_129010674}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_1226326472}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-list*]{lang="EN-US"}]{#struct_0_12741_x1014_x561100084}[：指定开启]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测的端口列表，表示方式为]{style="font-family:宋体"}[{ *start-port-number* \[ **to** *end-port-number* \] } &\<1-65535\>]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-65535\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[65535]{lang="EN-US"}[次。]{style="font-family:宋体"}*[end-port-number]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[。若不指定该参数，则表示使用全局配置的检测端口列表。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1103945544}[：指定]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_1839307050}[：设置对]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_1216246090}[：表示自动将受到攻]{style="font-family:宋体"}[击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地]{style="font-family:宋体"}[址添加到]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1721700716}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x1718178821}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x245902686}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_972233352}

[[每[个攻击防范策略下可以同时对多个]{style="color:black"}]{style="font-family:宋体"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_x36917287}[地址配置]{style="font-family:宋体;
color:black"}[DNS flood]{lang="EN-US" style="color:black"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[使能]{style="font-family:宋体"}[DNS ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1163326990}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[DNS]{lang="EN-US" style="color:black"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[DNS ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1649210501}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x920818067}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测，并指定检测端口为]{style="font-family:宋体"}[53]{lang="EN-US"}[、触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[53]{lang="EN-US"}[端口每秒发送的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x349837851}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] dns-flood detect ip 192.168.1.2 port 53 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1481886406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1413521504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_638441793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1702447299}**[threshold]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_681362987}**[port]{lang="EN-US"}**
:::

::: {#-904601652 .myid}
[]{#_Toc404793911}[]{#struct_0_12741_x1014_x1597434190}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood detect non-specific**

------------------------------------------------------------------------

[**[dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1152045965}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_292806160}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1854956550}

[**[dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1559691432}

[**[undo dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_975182749}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1940394844}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_x364809847}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x365629049}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1943531853}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1433057227}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1270003532}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x223172189}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1169191923}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1815754682}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[dns-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[dns-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1063166383}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_413863751}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x650861810}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] dns-flood detect non-specific]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x184648078}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1970184277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x2136996009}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_x1394152294}**[-flood threshold]{lang="EN-US"}**
:::

::: {#-1454477850 .myid}
[]{#_Toc404793912}[]{#struct_0_12741_x1014_x610433237}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood port**

------------------------------------------------------------------------

[**[dns-flood port]{lang="EN-US"}**]{#struct_0_12741_x1014_x1915987328}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的全局检测端口号。]{style="font-family:宋体"}

[**[undo dns-flood port]{lang="EN-US"}**]{#struct_0_12741_x1014_35949238}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1990071594}

[**[dns-flood port]{lang="EN-US"}***[ ]{lang="EN-US"}[port-list]{lang="EN-US"}*]{#struct_0_12741_x1014_581317564}

[**[undo dns-flood port]{lang="EN-US"}**]{#struct_0_12741_x1014_x2017832497}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x234010404}

[[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_1631904175}[攻击防范的全局检测端口号为]{style="font-family:宋体"}[53]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_462373260}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1344276599}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1314748307}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_812896027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x25932139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1847491990}

[*[port-list]{lang="EN-US"}*]{#struct_0_12741_x1014_x1379026956}[：指定开启]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范检测的端口列表，表示方式为]{style="font-family:宋体"}[{ *start-port-number* \[ **to** *end-port-number* \] } &\<1-65535\>]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-65535\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[65535]{lang="EN-US"}[次。]{style="font-family:宋体"}*[end-port-number]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x65788903}

[[设备只对指定检测端口上收到的报文进行]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1040112820}[攻击检测。]{style="font-family:宋体"}

[[对于所有非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1212101534}[地址，或未指定检测端口的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的检测端口进行]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击检测。对于所有指定检测端口的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备针对为每个受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址指定的端口进行]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1091623478}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x564462957}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的全局检测端口为]{style="font-family:宋体"}[53]{lang="EN-US"}[与]{style="font-family:宋体"}[61000]{lang="EN-US"}[，当设备检测到访问]{style="font-family:宋体"}[53]{lang="EN-US"}[端口或]{style="font-family:宋体"}[61000]{lang="EN-US"}[端口的]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击时，启动攻击防范措施。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x753187914}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] dns-flood port 53 61000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x870661689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_814583342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1965495862}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1881521519}
:::

::: {#1892102393 .myid}
[]{#_Toc404793913}[]{#struct_0_12741_x1014_x1665731764}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood threshold**

------------------------------------------------------------------------

[**[dns-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_863742841}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo dns-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1228067606}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_845266757}

[**[dns-flood threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x170979806}

[**[undo dns-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1975695441}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1897435794}

[[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_1508881921}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1655859330}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1624638857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_419414631}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1844106114}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_177556174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_951435204}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x360629731}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_53381140}

[[对于没有专门配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}]{#struct_0_12741_x1014_x861195665}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_287664066}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1943131958}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[全局触发阈]{style="font-family:宋体"}[值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，即当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动攻击防范措施。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x64208395}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] dns-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1084398539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_977720000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_857756368}**[detect ]{lang="EN-US"}[ip]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1699626275}
:::

::: {#-1075069651 .myid}
[]{#_Toc404793914}[]{#struct_0_12741_x1014_x1512702801}[]{#_Toc349982059}[]{#_Toc349982060}[]{#_Toc349982061}[]{#_Toc349982062}[]{#_Toc349982063}[]{#_Toc349982064}[]{#_Toc349982065}[]{#_Toc349982066}[]{#_Toc349982067}[]{#_Toc349982068}[]{#_Toc349982069}[]{#_Toc349982070}[]{#_Toc349982071}[]{#_Toc349982072}[]{#_Toc349982073}[]{#_Toc349982074}[]{#_Toc349982075}[]{#_Toc349982076}[]{#_Toc349982077}[]{#_Toc349982079}[]{#_Toc349982080}[]{#_Toc349982081}[]{#_Toc349982082}[]{#_Toc349982083}[]{#_Toc349982084}[]{#_Toc349982085}[]{#_Toc349982086}[]{#_Toc349982087}[]{#_Toc349982088}[]{#_Toc349982089}[]{#_Toc349982091}[]{#_Toc349982092}[]{#_Toc349982093}[]{#_Toc349982094}[]{#_Toc349982095}[]{#_Toc349982096}[]{#_Toc349982097}[]{#_Toc349982098}[]{#_Toc349982099}[]{#_Toc349982100}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- exempt acl**

------------------------------------------------------------------------

[**[exempt acl]{lang="EN-US"}**]{#struct_0_12741_x1014_799357067}[命令用来配置攻击防范例外列表。]{style="font-family:宋体"}

[**[undo exempt acl]{lang="EN-US"}**]{#struct_0_12741_x1014_734215819}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1503383314}

[**[exempt acl ]{lang="EN-US"}**[\[ **ipv6** \] { *acl-number* \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_12741_x1014_x1167675536}

[**[undo exempt acl ]{lang="EN-US"}**[\[ **ipv6** \]]{lang="EN-US"}]{#struct_0_12741_x1014_102958662}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x207926779}

[[应用了攻击防范策略的接口接收到的所有报文都需要进行攻击防范检测。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1419977992}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x930175876}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1527604476}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1216180554}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_210437387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x192568792}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_671646007}

[**[ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_907732660}[：指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。如果没有指定本参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x462156076}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_12741_x1014_2084756574}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：若未指定]{lang="EN-US" style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[；否则表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_12741_x1014_x1789897715}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[；否则表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_12741_x1014_891228270}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2125936058}

[[通过配置例外列表，使用]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_12741_x1014_x883344165}[过滤不需要进行攻击防范检测的主机报文。当接口上收到的报文与攻击防范例外列表引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的]{style="font-family:宋体"}[permit]{lang="EN-US"}[规则匹配时，设备不对其进行攻击防范检测。该配置用于过滤某些被信任的安全主机发送的报文，可以有效的减小误报率，并提高服务器处理效率。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12741_x1014_x245902693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[例外列表引用的]{style="font-family:宋体"}]{#struct_0_12741_x1014_x246492516}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[permit]{lang="EN-US"}[规则中仅源地址、目的地址、源端口、目的端口、协议号、]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}[和非首片分片标记参数用于匹配报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置的攻击防范例外列表]{style="font-family:宋体"}]{#struct_0_12741_x1014_x349903387}[中]{style="font-size:10.0pt;font-family:宋体"}[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在，或引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未定义任何规则，例外列表不会生效]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_333028640}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1824251103}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置例外列表]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[，过滤]{style="font-family:宋体"}[来自主机]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的报文，不对其进行攻击防范检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1013508506}

[\[Sysname\] acl number 2001 name acl_1]{lang="EN-US"}

[\[Sysname-acl-basic-2001\] rule permit source 1.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[attack-defense-policy-atk-policy-1\] exempt acl name acl_1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x385239807}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x486730741}
:::

::: {#-1377832662 .myid}
[]{#_Toc404793915}[]{#struct_0_12741_x1014_1711031561}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood action**

------------------------------------------------------------------------

[**[fin-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x643460977}[命令用来配置对]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo fin-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1559756968}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_373939540}

[**[fin-flood action]{lang="EN-US"}**[ { **client-verify** \| **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_511427888}

[**[undo fin-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x98461373}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1471885170}

[[不对检测到的]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_1240017424}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1516174545}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2087594123}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1936418641}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1661304124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1169126387}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2119569223}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_739715330}[：表示自动将受]{style="font-family:宋体"}[到攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x2061770441}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x1448223555}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1680120447}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_850754546}[参数的使用需要和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的接口检测到]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_546997298}

[[\#]{lang="EN-US"}]{#struct_0_12741_x1014_864365295}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[配置对]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1916052864}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] fin-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x173058467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_1146772673}**[tcp enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x543204794}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin]{lang="EN-US"}[-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x540787144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x50083219}**[threshold]{lang="EN-US"}**
:::

::: {#2090529951 .myid}
[]{#_Toc404793916}[]{#struct_0_12741_x1014_134154424}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood detect**

------------------------------------------------------------------------

[**[fin-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_1678602435}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[触发阈值和对]{style="font-family:
宋体"}[FIN flood]{lang="EN-US"}[攻击的]{style="font-family:
宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo fin-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_1282547193}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x234367831}

[**[fin-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_812830491}

[**[undo fin-flood detect]{lang="EN-US"}**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_1903131485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2844578}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_204719102}[地址配置]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1107121267}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1408639682}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1792852701}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_331783357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x716333725}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_507344008}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_951526527}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1571717314}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x753253450}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_1762694162}[：指定攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1382537745}[：设置对]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_935150023}[：表示当自动将受]{style="font-family:宋体"}[到攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加]{style="font-family:宋体"}[到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_1004552853}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x570174273}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x246099300}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1365955684}

[[每[个攻击防范策略下可以同时对多个]{style="color:black"}]{style="font-family:宋体"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_1483708852}[地址配置]{style="font-family:宋体;
color:black"}[FIN flood]{lang="EN-US" style="color:black"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[使能]{style="font-family:宋体"}[FIN ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_889377342}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[FIN]{lang="EN-US" style="color:black"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[FIN ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1975629905}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1137239214}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1732278130}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] fin-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x336294412}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x655618172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin]{lang="EN-US"}[-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x899377243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_510302819}**[threshold]{lang="EN-US"}**
:::

::: {#-722865925 .myid}
[]{#_Toc404793917}[]{#struct_0_12741_x1014_x1684686907}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood detect non-specific**

------------------------------------------------------------------------

[**[fin-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1098121087}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo fin-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1981277163}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_53315604}

[**[fin-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_82511071}

[**[undo fin-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_605087199}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1739680782}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_156204302}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2017676898}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_2122528919}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_399625305}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_502395411}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x154906774}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1512768337}

[[无]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_1822236536}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_348801769}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_1573440712}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[fin-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[fin-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1479723901}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_844404141}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1655909893}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] fin-flood detect non-specific]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1542102282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x2118165896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1216115018}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1013277400}**[threshold]{lang="EN-US"}**
:::

::: {#-1699934259 .myid}
[]{#_Toc404793918}[]{#struct_0_12741_x1014_993884674}[]{#_Toc349982104}[]{#_Toc349982105}[]{#_Toc349982106}[]{#_Toc349982107}[]{#_Toc349982108}[]{#_Toc349982109}[]{#_Toc349982110}[]{#_Toc349982111}[]{#_Toc349982112}[]{#_Toc349982113}[]{#_Toc349982114}[]{#_Toc349982115}[]{#_Toc349982116}[]{#_Toc349982117}[]{#_Toc349982118}[]{#_Toc349982119}[]{#_Toc349982120}[]{#_Toc349982121}[]{#_Toc349982122}[]{#_Toc349982123}[]{#_Toc349982124}[]{#_Toc349982125}[]{#_Toc349982126}[]{#_Toc349982127}[]{#_Toc349982128}[]{#_Toc349982129}[]{#_Toc349982130}[]{#_Toc349982131}[]{#_Toc349982132}[]{#_Toc349982133}[]{#_Toc349982135}[]{#_Toc349982136}[]{#_Toc349982137}[]{#_Toc349982138}[]{#_Toc349982139}[]{#_Toc349982140}[]{#_Toc349982141}[]{#_Toc349982142}[]{#_Toc349982143}[]{#_Toc349982144}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood threshold**

------------------------------------------------------------------------

[**[fin-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x2108339591}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo fin-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1250640353}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1998857418}

[**[fin-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1630942145}

[**[undo fin-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1003070133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1847385109}

[[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_862522820}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x349968923}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_273987209}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1126829986}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x13128117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_257387855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1454472640}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_474361721}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1843468144}

[[对于没有专门配置]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}]{#struct_0_12741_x1014_1231641189}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_336699462}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1786569583}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[全局触发阈值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[，即当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[FIN flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1559822504}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] fin-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x400688115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1840027259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1760363310}**[detect ]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x281923318}
:::

::: {#1349243606 .myid}
[]{#_Toc404793919}[]{#struct_0_12741_x1014_x2031365963}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood action**

------------------------------------------------------------------------

[**[http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x243249106}[命令用来配置对]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_536619551}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1396340303}

[**[http-flood action]{lang="EN-US"}**[ { **client-verify** \| **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_x1762659320}

[**[undo http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1371475305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1707484423}

[[不对检测到的]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1169060851}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2108314575}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_244640047}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_169293784}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_60214308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1975639238}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2082359609}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_2002304085}[：表示自动将受到攻击]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地]{style="font-family:宋体"}[址添加到]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_2048125242}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_308074783}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_64343267}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x2136270016}[参数的使用需要和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的接口检测到]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1916118400}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_823326561}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置对]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1000597472}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] http-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1732607725}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1865845546}**[http]{lang="EN-US"}[ ]{lang="EN-US"}[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood]{lang="EN-US"}[ detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x55179394}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_12741_x1014_1290245342}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_12741_x1014_419542724}**[threshold]{lang="EN-US"}**
:::

::: {#-257120870 .myid}
[]{#_Toc404793920}[]{#struct_0_12741_x1014_x1055016755}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood detect**

------------------------------------------------------------------------

[**[http-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_812764955}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范的触发阈值和对]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击的]{style="font-family:宋体"}[处理行为。]{style="font-family:
宋体"}

[**[undo http-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_519792287}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_763059559}

[**[http-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **port** *port-list* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_844149761}

[**[undo http-flood detect ]{lang="EN-US"}**[{ **ip** *ip-address* **\| ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1771694603}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1044743200}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_600559322}[地址配置]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1590718205}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1142865842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_387686320}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x753318986}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1384617751}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_208131324}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_445248943}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1313358030}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_1816308259}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-list*]{lang="EN-US"}]{#struct_0_12741_x1014_x1498633699}[：指定开启]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测的端口列表，表示方式为]{style="font-family:宋体"}[{ *start-port-number* \[ **to** *end-port-number* \] } &\<1-65535\>]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-65535\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[65535]{lang="EN-US"}[次。]{style="font-family:宋体"}*[end-port-number]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[。若不指定该参数，则表示使用全局配置的检测端口列表。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1799836919}[：指定攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_793504006}[：设置对]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_2075917207}[：表示自动将受到攻]{style="font-family:宋体"}[击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1924108732}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_1882326730}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x1740332446}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1591828686}

[[每[个攻击防范策略下可以同时对多个]{style="color:black"}]{style="font-family:宋体"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_x1427328300}[地址配置]{style="font-family:宋体;
color:black"}[HTTP flood]{lang="EN-US" style="color:black"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[使能]{style="font-family:宋体"}[HTTP ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_x236344273}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[HTTP]{lang="EN-US" style="color:black"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[HTTP ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x815067187}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1342290356}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测，并指定检测端口为]{style="font-family:宋体"}[80]{lang="EN-US"}[与]{style="font-family:宋体"}[8080]{lang="EN-US"}[、触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[80]{lang="EN-US"}[或]{style="font-family:宋体"}[8080]{lang="EN-US"}[端口每秒发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_2139314234}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] http-flood detect ip 192.168.1.2 port 80 8080 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_502478220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_467799225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood]{lang="EN-US"}[ detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_53250068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1681472105}**[threshold]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1126134345}**[port]{lang="EN-US"}**
:::

::: {#-150979437 .myid}
[]{#_Toc404793921}[]{#struct_0_12741_x1014_x948562931}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood detect non-specific**

------------------------------------------------------------------------

[**[http-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1017042952}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo http-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_52144097}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1235625253}

[**[http-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1279970765}

[**[undo http-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x772787230}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_700467621}

[[未对任何]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1512833873}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1874556142}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1822494718}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1552048845}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1197749780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1587726140}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1929338946}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_1196742871}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[http-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[http-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1205563165}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x145838426}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1216049482}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] http-flood detect non-specific ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x197380774}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1187587531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x137505633}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x52847764}**[threshold]{lang="EN-US"}**
:::

::: {#-1918837093 .myid}
[]{#_Toc404793922}[]{#struct_0_12741_x1014_505121984}[]{#_Toc349982148}[]{#_Toc349982149}[]{#_Toc349982150}[]{#_Toc349982151}[]{#_Toc349982152}[]{#_Toc349982153}[]{#_Toc349982154}[]{#_Toc349982155}[]{#_Toc349982156}[]{#_Toc349982157}[]{#_Toc349982158}[]{#_Toc349982159}[]{#_Toc349982160}[]{#_Toc349982161}[]{#_Toc349982162}[]{#_Toc349982163}[]{#_Toc349982164}[]{#_Toc349982165}[]{#_Toc349982166}[]{#_Toc349982167}[]{#_Toc349982168}[]{#_Toc349982169}[]{#_Toc349982170}[]{#_Toc349982171}[]{#_Toc349982172}[]{#_Toc349982173}[]{#_Toc349982174}[]{#_Toc349982175}[]{#_Toc349982176}[]{#_Toc349982177}[]{#_Toc349982179}[]{#_Toc349982180}[]{#_Toc349982181}[]{#_Toc349982182}[]{#_Toc349982183}[]{#_Toc349982184}[]{#_Toc349982185}[]{#_Toc349982186}[]{#_Toc349982187}[]{#_Toc349982188}[]{#_Toc349982190}[]{#_Toc349982191}[]{#_Toc349982192}[]{#_Toc349982193}[]{#_Toc349982194}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood port**

------------------------------------------------------------------------

[**[http-flood port]{lang="EN-US"}**]{#struct_0_12741_x1014_1369851016}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范的全局检测端口号。]{style="font-family:宋体"}

[**[undo http-flood port]{lang="EN-US"}**]{#struct_0_12741_x1014_x1123170466}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x838788630}

[**[http-flood port]{lang="EN-US"}***[ ]{lang="EN-US"}[port-list]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_12741_x1014_1599571857}

[**[undo http-flood port]{lang="EN-US"}**]{#struct_0_12741_x1014_x350034459}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1035804468}

[[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_234308013}[攻击防范的全局检测端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1525036888}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1597852321}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_523267696}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_242424745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1758573183}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x612907356}

[*[port-list]{lang="EN-US"}*]{#struct_0_12741_x1014_1752844183}[：指定开启]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范检测的端口列表，表示方式为]{style="font-family:宋体"}[{ *start-port-number* \[ **to** *end-port-number* \] } &\<1-65535\>]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-65535\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[65535]{lang="EN-US"}[次。]{style="font-family:宋体"}*[end-port-number]{lang="EN-US"}*[必须大于或等于]{style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1559888040}

[[设备只对指定检测端口上收到的报文进行]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1476014994}[攻击检测。]{style="font-family:宋体"}

[[对于所有非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x732428438}[地址，或未指定检测端口的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的检测端口进行]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击检测。对于所有指定检测端口的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备针对为每个受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址指定的端口进行]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x306280595}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1303252809}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[DNS flood]{lang="EN-US"}[攻击防范的全局检测端口为]{style="font-family:宋体"}[80]{lang="EN-US"}[与]{style="font-family:宋体"}[8080]{lang="EN-US"}[，当设备检测到访问]{style="font-family:宋体"}[80]{lang="EN-US"}[端口或]{style="font-family:宋体"}[8080]{lang="EN-US"}[端口的]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击时，启动攻击防范措施。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_428401825}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] http-flood port 80 8080]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1662041492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_420137055}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1282150083}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1168995315}
:::

::: {#1878586678 .myid}
[]{#_Toc404793923}[]{#struct_0_12741_x1014_x1803380307}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood threshold**

------------------------------------------------------------------------

[**[http-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x480673996}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo http-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x193867624}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1328047290}

[**[http-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x81815938}

[**[undo http-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x2059271601}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1448288861}

[[缺省情况下，]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_150946280}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1521105455}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x900606478}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1916183936}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x32036187}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_20411801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1227240375}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x2113129437}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1374084544}

[[对于没有专门配置]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x38013210}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1472505039}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_469368763}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[全局触发阈值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"} [即当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[HTTP flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1562855161}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] http-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_812699419}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x243762149}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_588589111}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x58336864}
:::

::: {#-435866779 .myid}
[]{#_Toc404793924}[]{#struct_0_12741_x1014_x1693737012}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood action**

------------------------------------------------------------------------

[**[icmp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1802166321}[命令用来配置对]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo icmp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_69646321}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2043925414}

[**[icmp-flood action ]{lang="EN-US"}**[{ **drop** \| **logging** } **\***]{lang="EN-US"}]{#struct_0_12741_x1014_2098880684}

[**[undo icmp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x744862932}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1585436514}

[[不对检测到的]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1008729885}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_425127162}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x753384522}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1020469209}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1862487247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1692828545}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_79082192}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1129894696}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_1164647668}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1229882305}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_404298766}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置对]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1975498833}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmp-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x349401172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1113163246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1617536825}**[detect ]{lang="EN-US"}[ip]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_317451705}**[threshold]{lang="EN-US"}**
:::

::: {#1595207881 .myid}
[]{#_Toc404793925}[]{#struct_0_12741_x1014_991523822}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood detect ip**

------------------------------------------------------------------------

[**[icmp-flood detect ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1187330107}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[触发阈值和对]{style="font-family:
宋体"}[ICMP flood]{lang="EN-US"}[攻击的]{style="font-family:
宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo icmp-flood detect ip]{lang="EN-US"}**]{#struct_0_12741_x1014_407579324}[命令用来取消对指定]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_29070600}

[**[icmp-flood detect]{lang="EN-US"}**[ **ip** *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_648156108}

[**[undo icmp-flood detect ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_942394811}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_53184532}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1767937815}[地址配置]{style="font-family:宋体"}[ICMP flood ]{lang="EN-US"}[攻击防范触发阈值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1296858400}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_181845086}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x113572705}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1529616056}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_941530982}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2112531569}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_893052307}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x796744969}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1985021771}[：指定攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x50361761}[：设置对]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x15184011}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_1895743342}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x1739742621}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x726926721}

[[每个攻击防范策略下可以同时对多个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1656166536}[地址配置]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_197028176}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1319583568}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1866574570}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_504033260}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmp-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_869747135}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x966001359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1215983946}**[threshold]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1546279375}
:::

::: {#-564576495 .myid}
[]{#_Toc404793926}[]{#struct_0_12741_x1014_x1178660467}[]{#_Toc349982198}[]{#_Toc349982199}[]{#_Toc349982200}[]{#_Toc349982201}[]{#_Toc349982202}[]{#_Toc349982203}[]{#_Toc349982204}[]{#_Toc349982205}[]{#_Toc349982206}[]{#_Toc349982207}[]{#_Toc349982208}[]{#_Toc349982209}[]{#_Toc349982210}[]{#_Toc349982211}[]{#_Toc349982212}[]{#_Toc349982213}[]{#_Toc349982214}[]{#_Toc349982215}[]{#_Toc349982216}[]{#_Toc349982217}[]{#_Toc349982219}[]{#_Toc349982220}[]{#_Toc349982221}[]{#_Toc349982222}[]{#_Toc349982223}[]{#_Toc349982224}[]{#_Toc349982225}[]{#_Toc349982226}[]{#_Toc349982227}[]{#_Toc349982229}[]{#_Toc349982230}[]{#_Toc349982231}[]{#_Toc349982232}[]{#_Toc349982233}[]{#_Toc349982234}[]{#_Toc349982235}[]{#_Toc349982236}[]{#_Toc349982237}[]{#_Toc349982238}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood detect non-specific**

------------------------------------------------------------------------

[**[icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x549883066}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_2122161460}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1190108051}

[**[icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1548176453}

[**[undo icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x350099995}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1743904295}

[[未对任何]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2142145248}[非受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1331355234}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_504923812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x912402454}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x615257750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1101248878}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x145415753}

[[对任何]{style="font-family:宋体"}]{#struct_0_12741_x1014_x794971264}[非受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[icmp-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[icmp]{lang="EN-US"}[-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_81572332}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1393408078}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1559953576}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmp-flood detect non-specific ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1481473230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_163054164}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood detect ip]{lang="EN-US"}**]{#struct_0_12741_x1014_472555480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_279858323}**[threshold]{lang="EN-US"}**
:::

::: {#-512650383 .myid}
[]{#_Toc404793927}[]{#struct_0_12741_x1014_x183701892}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood threshold**

------------------------------------------------------------------------

[**[icmp-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x244794959}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo icmp-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_2042642178}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1168929779}

[**[icmp-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x927587733}

[**[undo icmp-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x857109347}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1478042175}

[[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_242818626}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1277411902}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2129249791}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1175831531}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_800628505}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1534579771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_894648039}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1574609676}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2039947889}

[[对于没有专门配置]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}]{#struct_0_12741_x1014_291088760}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1648464841}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1913306968}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[全局触]{style="font-family:宋体"}[发阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，即当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[ICMP flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_31504170}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmp-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x2137332519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1287186010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_303915146}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x841574427}
:::

::: {#1354486879 .myid}
[]{#_Toc404793928}[]{#struct_0_12741_x1014_1369194177}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood action**

------------------------------------------------------------------------

[**[icmpv6-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_405415452}[命令用来配置对]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo icmpv6-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1497513283}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1597588111}

[**[icmpv6-flood action ]{lang="EN-US"}**[{ **drop** \| **logging** } **\***]{lang="EN-US"}]{#struct_0_12741_x1014_1686418224}

[**[undo icmpv6-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1887251945}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1230098997}

[[不对检测到的]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_1479850474}[攻击采取任何防范措施]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1053176836}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_507472207}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1602424287}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2005923289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1131295244}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x812174630}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x834493307}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_1921013550}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1032294836}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1164526318}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置对]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_86904524}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmpv6-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_970154111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_791019057}**[detect]{lang="EN-US"}[ ipv6]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1658524801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1635400595}**[threshold]{lang="EN-US"}[ ]{lang="EN-US"}**
:::

::: {#1241474436 .myid}
[]{#_Toc404793929}[]{#struct_0_12741_x1014_1671506028}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood detect ipv6**

------------------------------------------------------------------------

[**[icmpv6-flood detect ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x538710009}[命令用来开启对指定]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测的触发阈值]{style="font-family:宋体"}[和对]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击的]{style="font-family:宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo icmpv6-flood detect ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_1376445109}[命令用来取消对指定]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1989045676}

[**[icmpv6-flood detect ]{lang="EN-US"}[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_942185463}

[**[undo icmpv6-flood]{lang="EN-US"}[ detect ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_1265467397}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x254377076}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1341603342}[地址配置]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_759537302}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1937864298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_810764137}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_828223955}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1788829949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_419186224}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1195943672}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_1215094215}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_329308048}[：指定攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}[ ]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_671043635}[：设置对]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x371780357}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_2048429033}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x1739742620}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x922791601}

[[每个攻击防范策略下可以同时对多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12741_x1014_2091480598}[地址配置]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_976637097}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x436047369}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x168590372}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2012::12]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1731993896}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmpv6-flood detect ipv6 2012::12 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1194303584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1444545801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_105326464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x713731349}**[threshold]{lang="EN-US"}**
:::

::: {#-1177854258 .myid}
[]{#_Toc404793930}[]{#struct_0_12741_x1014_7167528}[]{#_Toc349982242}[]{#_Toc349982243}[]{#_Toc349982244}[]{#_Toc349982245}[]{#_Toc349982246}[]{#_Toc349982247}[]{#_Toc349982248}[]{#_Toc349982249}[]{#_Toc349982250}[]{#_Toc349982251}[]{#_Toc349982252}[]{#_Toc349982253}[]{#_Toc349982254}[]{#_Toc349982255}[]{#_Toc349982256}[]{#_Toc349982257}[]{#_Toc349982258}[]{#_Toc349982259}[]{#_Toc349982260}[]{#_Toc349982261}[]{#_Toc349982262}[]{#_Toc349982263}[]{#_Toc349982264}[]{#_Toc349982265}[]{#_Toc349982266}[]{#_Toc349982267}[]{#_Toc349982268}[]{#_Toc349982269}[]{#_Toc349982270}[]{#_Toc349982271}[]{#_Toc349982273}[]{#_Toc349982274}[]{#_Toc349982275}[]{#_Toc349982276}[]{#_Toc349982277}[]{#_Toc349982278}[]{#_Toc349982279}[]{#_Toc349982280}[]{#_Toc349982281}[]{#_Toc349982282}[]{#_Toc349982284}[]{#_Toc349982285}[]{#_Toc349982286}[]{#_Toc349982287}[]{#_Toc349982288}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood detect non-specific**

------------------------------------------------------------------------

[**[icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1806262674}[命令用来对所有非受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x52143351}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_248340265}

[**[icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1991475772}

[**[undo icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1257813495}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1178349411}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_x961034342}[非受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_52753096}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1113781418}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1559871023}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_827622990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1702480545}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x956615424}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_1290316738}[非受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[icmpv6-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[icmpv6]{lang="EN-US"}[-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1226916361}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_387734530}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有非受保护]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1135441419}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmpv6-flood detect non-specific ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1982633666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x542506353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x2105059953}**[detect ]{lang="EN-US"}[ipv6]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1564826212}**[threshold]{lang="EN-US"}**
:::

::: {#-200915907 .myid}
[]{#_Toc404793931}[]{#struct_0_12741_x1014_1758400102}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood threshold**

------------------------------------------------------------------------

[**[icmpv6-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x998890356}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo icmpv6-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x1614076252}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1378135230}

[**[icmpv6-flood threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1534645307}

[**[undo icmpv6-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x2005115480}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1501115085}

[[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_1229013165}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1528720969}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1137214706}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_331498225}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x624029109}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_413145574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1850915225}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x446374687}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1768341879}

[[对于没有专门配置]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}]{#struct_0_12741_x1014_x2104339776}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_31438634}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1863499572}[在攻击防范策]{style="font-family:宋体"}[略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范检测的全局触发阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，即当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[ICMPv6 flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_977281800}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] icmpv6-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x820203842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6]{lang="EN-US"}**]{#struct_0_12741_x1014_2029870723}**[-flood]{lang="EN-US"}[ action]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1378408871}**[-flood]{lang="EN-US"}[ ]{lang="EN-US"}[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmpv6-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1263946128}
:::

::: {#-1578703362 .myid}
[]{#_Toc340488565}[]{#struct_0_12741_x1014_x1839421840}[]{#_Toc404793932}[]{#_Toc344706686}[]{#_Toc359225220}[]{#_Toc359334601}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset attack-defense policy flood**

------------------------------------------------------------------------

[**[reset attack-defense policy flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1254683214}[命令用来清除]{style="font-family:宋体"}[flood]{lang="EN-US"}[攻击防范受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1039864246}

[**[reset attack-defense policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}***[ flood protected ]{lang="EN-US"}**[{ **ip** \| **ipv6** } **statistics**]{lang="EN-US"}]{#struct_0_12741_x1014_1597522575}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_143355600}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_87370562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_96279793}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_708722311}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1478891250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2008550483}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_80811908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_860514429}

[*[policy-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1235611642}[：]{style="font-family:宋体"}[攻击防范策略]{style="font-family:宋体"}[名称，为]{style="font-size:10.0pt;font-family:
宋体;color:black"}[1]{lang="EN-US" style="font-size:10.0pt;color:black"}[～]{style="font-size:10.0pt;font-family:宋体;color:black"}[31]{lang="EN-US" style="font-size:10.0pt;color:black"}[个字符的字符串，不区分大小写。]{style="font-size:10.0pt;
font-family:宋体;color:black"}[合法取值包括大写字母、小写字母、数字、特殊字符"]{style="font-family:
宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1052195555}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x938984941}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_12741_x1014_x1131360780}[：清除指定类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x235555172}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1455973520}[清除攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的]{style="font-family:宋体"}[flood]{lang="EN-US"}[保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的统计信息]{style="font-family:宋体"}

[[\<Sysname\> reset attack-defense policy abc flood protected ip statistics]{lang="EN-US"}]{#struct_0_12741_x1014_593637209}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1570312855}[清除攻击防范策略]{style="font-family:宋体"}[abc]{lang="EN-US"}[中所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Flood]{lang="EN-US"}[保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的统计信息]{style="font-family:宋体"}

[[\<Sysname\> reset attack-defense policy abc flood protected ipv6 statistics]{lang="EN-US"}]{#struct_0_12741_x1014_1539743253}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_991201615}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense policy ip]{lang="EN-US"}**]{#struct_0_12741_x1014_519441382}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense policy ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1787827618}

[ ]{lang="EN-US"}
:::

::: {#-773764955 .myid}
[]{#_Toc404793933}[]{#struct_0_12741_x1014_830619279}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset attack-defense statistics interface**

------------------------------------------------------------------------

[**[reset attack-defense statistics interface]{lang="EN-US"}**]{#struct_0_12741_x1014_x2089331613}[命令用来清除接口上的攻击防范统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1144527752}

[**[reset attack-defense statistics interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12741_x1014_1181613097}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_790953521}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1222160183}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2143359307}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_80826405}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x847157124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2127509054}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1385311003}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1233942201}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12741_x1014_x2137981654}[：表示指定接口的]{style="font-family:宋体;color:black"}[接口类型和接口编号[。]{style="color:black"}]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1071322299}

[[本命令会将指定接口上攻击防范的所有统计信息清零。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2059198887}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1937929834}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1852195743}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的攻击防范的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset attack-defense statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_12741_x1014_x2117214737}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x491427772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[d]{lang="EN-US"}**]{#struct_0_12741_x1014_x480011579}**[isplay attack-defense policy]{lang="EN-US"}**
:::

::: {#-740973305 .myid}
[]{#_Toc404793934}[]{#struct_0_12741_x1014_1728690334}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset attack-defense statistics local**

------------------------------------------------------------------------

[**[reset attack-defense statistics local]{lang="EN-US"}**]{#struct_0_12741_x1014_1903178652}[命令用来清除本机攻击防范的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1530251432}

[**[reset attack-defense statistics local]{lang="EN-US"}**]{#struct_0_12741_x1014_784769216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1788821490}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x371845893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1580769061}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x391444369}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x173279081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1952639074}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1618717435}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1043831839}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1134409578}[清除本机上所有攻击防范的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset attack-defense statistics local]{lang="EN-US"}]{#struct_0_12741_x1014_1532118225}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_980597205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[d]{lang="EN-US"}**]{#struct_0_12741_x1014_99113386}**[isplay attack-defense statistics local]{lang="EN-US"}**
:::

::::: {#-43879982 .myid}
[]{#_Toc404793935}[]{#struct_0_12741_x1014_1194238048}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset blacklist ip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x1015237605}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x773234838}
:::

[ ]{lang="EN-US"}

[**[reset blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1111413831}[命令用来清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[动态黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_200255185}

[**[reset blacklist]{lang="EN-US"}**[ **ip** { *source-ip-address* \[ **vpn-instance** *vpn-instance-name* \] \[ **ds-lite-peer** *ds-lite-peer-address* \] \| **all** }]{lang="EN-US"}]{#struct_0_12741_x1014_912231466}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_811958173}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1558817231}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1211042866}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_454456840}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1178414947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1734997010}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_787985953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_695599891}

[*[source-ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1694388982}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的动态黑名单表项。其中]{style="font-family:宋体"}*[source-ip-address]{lang="EN-US"}*[表示黑名单表项的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x268852818}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的动态黑名单表项。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示清除公网中的指定动态黑名单表项。]{style="font-family:宋体"}

[**[ds-lite-peer]{lang="EN-US"}**[ *ds-lite-peer-address*]{lang="EN-US"}]{#struct_0_12741_x1014_x1740135842}[：]{style="font-family:宋体"}[清除黑名单所属的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[隧道对端地址。其中，]{style="font-family:宋体"}*[ds-lite-peer-address]{lang="EN-US"}*[表示黑名单的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[隧道]{style="font-family:宋体"}[B4]{lang="EN-US"}[端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[。若不指定该参数，则表示清除公网中的的指定动态黑名单表项。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_12741_x1014_x1746728195}[：表示清除所有动态]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的黑名单表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x804813386}

[[该命令仅用来清除]{style="font-family:宋体"}]{#struct_0_12741_x1014_x280789677}[动态生成的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的黑名单表项。]{style="font-family:宋体"}[用户添加的黑名单表项需要通过]{style="font-family:宋体"}**[undo blacklist ip]{lang="EN-US"}**[命令来删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1220274993}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x59419002}[清除所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[动态黑名单表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset blacklist ip all]{lang="EN-US"}]{#struct_0_12741_x1014_387668994}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1045032104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1045818062}
:::::

::::: {#2086771844 .myid}
[]{#_Toc404793936}[]{#struct_0_12741_x1014_563799980}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset blacklist ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_773731148}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x2073327968}
:::

[ ]{lang="EN-US"}

[**[reset blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_540780472}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x406789140}

[**[reset blacklist]{lang="EN-US"}**[ **ipv6** { *source-ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **all** }]{lang="EN-US"}]{#struct_0_12741_x1014_1077611252}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1534710843}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_9721858}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1345926677}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1509809266}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_329362995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1564817149}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1392016636}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2143295583}

[*[source-ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1462380214}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的动态黑名单表项。其中]{style="font-family:宋体"}*[source-ip-address]{lang="EN-US"}*[表示黑名单表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12741_x1014_x1486226342}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[的动态黑名单表项。其中]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示清除公网中的指定动态黑名单表项。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_12741_x1014_1389609746}[：表示清除所有动态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的黑名单表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_31373098}

[[该命令仅用来清除]{style="font-family:宋体"}]{#struct_0_12741_x1014_811414872}[动态生成的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的黑名单表项。]{style="font-family:宋体"}[用户添加的黑名单表项需要通过]{style="font-family:宋体"}**[undo blacklist ipv6]{lang="EN-US"}**[命令来删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x145243225}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1939250191}[清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态黑名单表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset blacklist ipv6 all]{lang="EN-US"}]{#struct_0_12741_x1014_604050772}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x681124221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_781784788}**[v6]{lang="EN-US"}**
:::::

::::: {#-2000748896 .myid}
[]{#_Toc404793937}[]{#struct_0_12741_x1014_x1495899846}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset blacklist statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1928101969}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_x1133139874}
:::

[ ]{lang="EN-US"}

[**[reset blacklist statistics]{lang="EN-US"}**]{#struct_0_12741_x1014_x1742698480}[命令用来清除黑名单表项的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1597457039}

[**[reset blacklist statistics]{lang="EN-US"}**]{#struct_0_12741_x1014_x1454519098}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_738310781}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_772258719}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1574066894}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1142503151}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x1442263403}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_47525286}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_13613452}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_120556313}

[[执行本命令后，将清空所有黑名单表项的丢包统计信息。]{style="font-family:宋体;color:black"}]{#struct_0_12741_x1014_x148656469}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1131426316}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1107513986}[清除所有黑名单表项的丢包统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset blacklist statistics]{lang="EN-US"}]{#struct_0_12741_x1014_1647697129}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1228143754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display blacklist ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1210356119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display blacklist ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x187830657}
:::::

::::: {#-429667395 .myid}
[]{#_Toc404793938}[]{#struct_0_12741_x1014_x2057616023}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset client-verify protected statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_1020191803}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_352626780}
:::

[ ]{lang="EN-US"}

[**[reset client-verify protected statistics]{lang="EN-US"}**]{#struct_0_12741_x1014_790887985}[命令用来清除客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1457792226}

[**[reset client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[protected ]{lang="EN-US"}**[{ **ip** \| **ipv6** } **statistics**]{lang="EN-US"}]{#struct_0_12741_x1014_x68338820}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1873321936}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x847069038}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x248567330}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1341049383}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_459038017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_840713093}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x58180205}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1937995370}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_709670761}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_x601115906}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_994392037}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_12741_x1014_1808818890}[：清除所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1051605055}[：清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1353403174}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_185990283}[清除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> **reset client-verify tcp protected ip** statistics]{lang="EN-US"}]{#struct_0_12741_x1014_x1050527053}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2138202149}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_x371911429}**[protected ip]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_1138527815}**[protected ipv6]{lang="EN-US"}**
:::::

::::: {#-1319060822 .myid}
[]{#struct_0_12741_x1014_x690375000}[]{#_Toc404793939}[]{#_Toc359425713}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset client-verify trusted**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](攻击检测与防范命令.files/image001.png){#图片 20 width="62" height="25"}]{lang="EN-US"}]{#struct_0_12741_x1014_x1802796108}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_12741_x1014_1570923219}
:::

[ ]{lang="EN-US"}

[**[reset client-verify trusted]{lang="EN-US"}**]{#struct_0_12741_x1014_1766697081}[命令用来清除客户端验证的信任]{style="font-family:
宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_706118606}

[**[reset client-verify ]{lang="EN-US"}**[{ **dns** \| **http** \| **tcp** } ]{lang="EN-US"}**[trusted ]{lang="EN-US"}**[{ **ip** \| **ipv6** }]{lang="EN-US"}]{#struct_0_12741_x1014_x1435437625}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2122523054}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1194172512}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1273261913}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1485848403}

[[network-operator]{lang="EN-US"}]{#struct_0_12741_x1014_x627175277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_363176704}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12741_x1014_1245097710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1903756082}

[**[dns]{lang="EN-US"}**]{#struct_0_12741_x1014_x377459588}[：指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_12741_x1014_x745346796}[：指定]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_12741_x1014_x821865119}[：指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_12741_x1014_x1495161846}[：清除所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1178480483}[：清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1757282736}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_547888895}[清除所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证的信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset client-verify dns trusted ip]{lang="EN-US"}]{#struct_0_12741_x1014_223837630}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1771888959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1239992378}**[trusted ip]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_x3396168}**[trusted ipv6]{lang="EN-US"}**
:::::

::: {#1739857698 .myid}
[]{#_Toc404793940}[]{#struct_0_12741_x1014_x1680008542}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood action**

------------------------------------------------------------------------

[**[rst-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1497767786}[命令用来配置对]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo rst-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x328567435}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1027181725}

[**[rst-flood action ]{lang="EN-US"}**[{]{lang="EN-US"}[ **client-verify** \| **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_387603458}

[**[undo rst-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1949696263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x558748607}

[[不对检测到的]{style="font-family:宋体"}[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_318084995}[攻击采取任何措施]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_674184518}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1383713151}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1929052795}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_80289037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_959546052}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1722059310}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_1130172764}[：表示自动将受到攻击]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1685062092}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x1534776379}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x217848901}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_1741322233}[参数的使用需要和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的接口检测到]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1748936001}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1996656116}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置对]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范的全局处理行为是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x691388000}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] rst-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1006272245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1218239349}**[tcp]{lang="EN-US"}[ ]{lang="EN-US"}[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_707771458}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_31307562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1478091799}**[threshold]{lang="EN-US"}**
:::

::: {#133178575 .myid}
[]{#_Toc404793941}[]{#struct_0_12741_x1014_x347587445}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood detect**

------------------------------------------------------------------------

[**[rst-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1416443348}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[的]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范的触发阈值]{style="font-family:宋体"}[和对]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击的]{style="font-family:宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo rst-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x954056406}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1713293821}

[**[rst-flood detect ]{lang="EN-US"}**[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1115865783}

[**[undo rst-flood detect ]{lang="EN-US"}**[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_x230419239}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1870926545}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1170272134}[地址配置]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1597391503}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1448877004}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x529864464}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2079797101}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_498560878}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2069282389}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x17354681}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1594180093}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_2055817719}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1603016884}[：指定攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1375459669}[：设置对]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x1131491852}[：表示自动将受到攻击]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1096094090}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x791286751}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x1739677089}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1917914805}

[[每[个攻击防范策略下可以同时对多个]{style="color:black"}]{style="font-family:宋体"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_x2101225878}[地址配置]{style="font-family:宋体;
color:black"}[RST flood]{lang="EN-US" style="color:black"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[使能]{style="font-family:宋体"}[RST ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}]{#struct_0_12741_x1014_811744133}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[RST]{lang="EN-US" style="color:black"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[RST ]{lang="EN-US" style="color:black"}[flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_969386414}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x361870932}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_790822449}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] rst-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1584931691}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1931108052}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1901967833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1412530029}**[threshold]{lang="EN-US"}**
:::

::: {#-1535867569 .myid}
[]{#_Toc404793942}[]{#struct_0_12741_x1014_x678319643}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood detect non-specific**

------------------------------------------------------------------------

[**[rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_945481926}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1982952420}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_630230291}

[**[rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x986833781}

[**[undo rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1938060906}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_200236697}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_1678311417}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1683800205}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2045282711}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_888498612}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2028242086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1702331739}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1302128623}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_x660682591}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[rst-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[rst-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x371976965}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x38420864}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x2080202900}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] rst-flood detect non-specific ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1039557210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1963322781}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x844088035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_294630723}**[threshold]{lang="EN-US"}**
:::

::: {#2063516836 .myid}
[]{#_Toc404793943}[]{#struct_0_12741_x1014_x395120724}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood threshold**

------------------------------------------------------------------------

[**[rst-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x1211423328}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo rst-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1194106976}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1315783111}

[**[rst-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x227039500}

[**[undo rst-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_600906215}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1877598932}

[[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_1744914991}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1559720009}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1887904943}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1312704699}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1678387415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1178546019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_410329798}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_297626866}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1790149478}

[[对于没有专门配置]{style="font-family:宋体"}[RST flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1183170785}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_644648584}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1738749952}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[全局触发阈]{style="font-family:宋体"}[值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[RST flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x359098595}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] rst-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x742222220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_2029856627}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_387537922}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rst-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x983887185}
:::

::: {#-1861088116 .myid}
[]{#struct_0_12741_x1014_621912903}[]{#_Toc404793944}[]{#_Toc359225234}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- scan detect**

------------------------------------------------------------------------

[**[scan detect]{lang="EN-US"}**]{#struct_0_12741_x1014_429725561}[命令用来配置开启指定级别的扫描攻击防范。]{style="font-family:宋体"}

[**[undo scan detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1097555522}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_359531556}

[**[scan detect level ]{lang="EN-US"}**[{ **high** \| **low** \| **medium** } **action** { { **block-source**]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **timeout** *minutes* \] \| **drop** } \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_x2140492392}

[**[undo scan detect level ]{lang="EN-US"}**[{ **high** \| **low** \| **medium** }]{lang="EN-US"}]{#struct_0_12741_x1014_x750129634}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_327098947}

[[扫描攻击防范处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12741_x1014_193532402}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x236698924}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x2011723861}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1534841915}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x319666460}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1301103593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1303047377}

[**[level]{lang="EN-US"}**]{#struct_0_12741_x1014_1773674751}[：]{style="font-family:宋体"}[指定攻击防范的检测级别。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_12741_x1014_677316397}[：表示低]{style="font-family:宋体"}[防范]{style="font-family:宋体"}[级别，该级别提供基本的扫描攻击检测，有很低的误报率，但对于一些扫描攻击类型不能检出。]{style="font-family:宋体"}

[**[high]{lang="EN-US"}**]{#struct_0_12741_x1014_x829912130}[：表示高]{style="font-family:宋体"}[防范]{style="font-family:宋体"}[级别，该级别能检测出大部分的扫描攻击，但对活跃主机误报率较高，即将可提供服务的主机的报文错误判断为攻击报文的概率比较高。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_12741_x1014_683600626}[：表示中]{style="font-family:宋体"}[防范]{style="font-family:宋体"}[级别，该级别有适中的攻击检出率与误报率，通常能够检测出]{style="font-family:宋体"}[Filtered Scan]{lang="EN-US"}[等攻击。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_997658206}[：设置对扫描攻击的处理行为。]{style="font-family:宋体"}

[**[block-source]{lang="EN-US"}**]{#struct_0_12741_x1014_x2111161412}[：表示阻断并丢弃来自该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的后续报文。具体实现是，当设备检测到攻击发生后，会自动将发起攻击的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到黑名单动态表项中，当接口上的黑名单过滤功能处于开启状态时，来自该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的报文将被丢弃。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[timeout ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_12741_x1014_881958867}[：动态添加的黑名单表项的老化时间。其中，]{style="font-family:宋体"}*[minutes]{lang="EN-US"}*[表示老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x861224130}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，由该攻击者发送的报文都将被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x130354421}[：表示输出告警日志，即设备检测到攻击发生时，生成记录告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_31242026}

[[要使扫描攻击防范添加的黑名单动态表项生效，必须保证接口上的黑名单过滤功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_12741_x1014_844107029}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x225878680}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1845929660}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置扫描攻击的检测级别为低级别，处理行为是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_637754404}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] scan detect level low action drop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x817501915}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置扫描攻击的检测级别为低级别，处理行为是发日志，阻断并丢弃来自该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的后续报文，并设置添加的黑名单表项的老化时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x696689180}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] scan detect level low action logging block-source timeout 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1377170181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist enable]{lang="EN-US"}**]{#struct_0_12741_x1014_x49566195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blacklist global enable]{lang="EN-US"}**]{#struct_0_12741_x1014_2046079439}
:::

::: {#-1658102277 .myid}
[]{#_Toc404793945}[]{#struct_0_12741_x1014_x1097943390}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature { large-icmp \| large-icmpv6 } max-length**

------------------------------------------------------------------------

[**[signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1998012763}[{]{lang="EN-US"}**[ large-icmp]{lang="EN-US"}***[ ]{lang="EN-US"}*[\| **large-icmpv6** ]{lang="EN-US"}[}]{lang="EN-US"}**[ max-length]{lang="EN-US"}**[命令用来]{style="font-family:宋体"}[配置启动]{style="font-family:宋体"}[Large ICMP]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文长度的最大值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo signature level detect]{lang="EN-US"}**]{#struct_0_12741_x1014_1222077495}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_92651324}

[**[signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_1448029742}[{]{lang="EN-US"}**[ large-icmp]{lang="EN-US"}***[ ]{lang="EN-US"}*[\| **large-icmpv6** ]{lang="EN-US"}[}]{lang="EN-US"}**[ max-length ]{lang="EN-US"}***[length]{lang="EN-US"}*

[**[undo signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_x16556723}[{]{lang="EN-US"}**[ large-icmp ]{lang="EN-US"}***[ ]{lang="EN-US"}*[\| **large-icmpv6** ]{lang="EN-US"}[}]{lang="EN-US"}**[ max-length]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2014531937}

[[ICMP]{lang="EN-US"}]{#struct_0_12741_x1014_x631667671}[报文和]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文长度的最大值均为]{style="font-family:宋体"}[4000]{lang="EN-US"}[字节]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_865830150}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1131557388}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1971077251}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2122808337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1987327182}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x815857862}

[**[large-icmp]{lang="EN-US"}**]{#struct_0_12741_x1014_x524073030}[：表示超大]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文攻击防范。]{style="font-family:宋体"}

[**[large-icmpv6]{lang="EN-US"}**]{#struct_0_12741_x1014_x1184145849}[：表示超大]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文攻击防范。]{style="font-family:宋体"}

[*[length]{lang="EN-US"}*]{#struct_0_12741_x1014_905942757}[：表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文长度的最大值，]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文取值范围为]{style="font-family:宋体"}[28]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文取值范围为]{style="font-family:宋体"}[48]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1641157109}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_448658607}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[启动]{style="font-family:宋体"}[Large ICMP]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文长度的最大值为]{style="font-family:宋体"}[50000]{lang="EN-US"}[字节]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_790756913}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] signature large-icmp max-length 50000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2072847159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1025675638}**[detect]{lang="EN-US"}**
:::

::: {#-2039397366 .myid}
[]{#_Toc404793946}[]{#struct_0_12741_x1014_x1961478065}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature detect**

------------------------------------------------------------------------

[**[signature detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1055183152}[命令用来开启指定类型单包攻击报文的特征检测，并设置攻击防范的处理行为。]{style="font-family:宋体"}

[**[undo signature detect]{lang="EN-US"}**]{#struct_0_12741_x1014_511797682}[命令用来取消对指定类型的单包攻击报文的特征检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_523623502}

[**[signature]{lang="EN-US"}**[ **detect** { **fraggle** \|]{lang="EN-US"}]{#struct_0_12741_x1014_380616016}**[ ]{lang="EN-US"}[fragment]{lang="EN-US"}**[ \| **impossible** \| ]{lang="EN-US"}**[ip-option-abnormal]{lang="EN-US"}**[ \| **land**]{lang="EN-US"}**[ ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ ]{lang="EN-US"}[large-icmp]{lang="EN-US"}**[ \| **large-icmpv6** \| **ping-of-death** \| **smurf** \|]{lang="EN-US"}**[ snork]{lang="EN-US"}**[ \| **tcp-all-flags** \| **tcp-fin-only** \| **tcp-invalid-flags** \| **tcp-null-flag** \| **tcp-syn-fin**]{lang="EN-US"}**[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[teardrop]{lang="EN-US"}**[ \| **tiny-fragment** \| **traceroute** \|]{lang="EN-US"}**[ ]{lang="EN-US"}[udp-]{lang="EN-US"}[bomb]{lang="EN-US"}**[ \| **winnuke** } \[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}

[**[undo signature]{lang="EN-US"}**[ **detect** { **fraggle** \|]{lang="EN-US"}]{#struct_0_12741_x1014_x1212802225}**[ ]{lang="EN-US"}[fragment]{lang="EN-US"}**[ \| **impossible** \| ]{lang="EN-US"}**[ip-option-abnormal]{lang="EN-US"}**[ \| **land**]{lang="EN-US"}**[ ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ ]{lang="EN-US"}[large-icmp]{lang="EN-US"}**[ \| **large-icmpv6** \| **ping-of-death** \| **smurf** \|]{lang="EN-US"}**[ snork]{lang="EN-US"}**[ \| **tcp-all-flags** \| **tcp-fin-only** \| **tcp-invalid-flags** \| **tcp-null-flag** \| **tcp-syn-fin**]{lang="EN-US"}**[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[teardrop]{lang="EN-US"}**[ \| **tiny-fragment** \| **traceroute** \|]{lang="EN-US"}**[ ]{lang="EN-US"}[udp-]{lang="EN-US"}[bomb]{lang="EN-US"}**[ \| **winnuke** }]{lang="EN-US"}

[**[signature ]{lang="EN-US"}[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12741_x1014_x2050071138}**[icmp-type ]{lang="EN-US"}**[{ *icmp-type-value*]{lang="EN-US"}[ \| ]{lang="EN-US"}**[address-mask-reply ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[address-mask-request ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[destination-unreachable ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[echo-reply ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[echo-request ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ information-reply ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ information-request ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ parameter-problem ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ redirect ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ source-quench ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[time-exceeded ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ timestamp-reply ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ timestamp-request ]{lang="EN-US"}**[} ]{lang="EN-US"}[\[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}

[**[undo signature ]{lang="EN-US"}[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12741_x1014_x1938126442}**[icmp-type ]{lang="EN-US"}**[{ *icmp-type-value*]{lang="EN-US"}[ \| ]{lang="EN-US"}**[address-mask-reply ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[address-mask-request ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[destination-unreachable ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[echo-reply ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[echo-request ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ information-reply ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ information-request ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ parameter-problem ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ redirect ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ source-quench ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[time-exceeded ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ timestamp-reply ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ timestamp-request]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[signature ]{lang="EN-US"}[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12741_x1014_x409665642}**[icmpv6-type ]{lang="EN-US"}**[{ *icmpv6-type-value*]{lang="EN-US"}[ \| ]{lang="EN-US"}**[destination-unreachable ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ echo-reply ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ echo-request ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[group-query ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ group-reduction ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[group-report ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ packet-too-big ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ parameter-problem ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ time-exceeded ]{lang="EN-US"}**[} ]{lang="EN-US"}[\[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}

[**[undo signature ]{lang="EN-US"}[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12741_x1014_1736128687}**[icmpv6-type ]{lang="EN-US"}**[{ *icmpv6-type-value* ]{lang="EN-US"}[\|]{lang="EN-US"}**[ destination-unreachable ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[echo-reply ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ echo-request ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[group-query ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ group-reduction ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[group-report ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ packet-too-big ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ parameter-problem ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ time-exceeded ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[signature ]{lang="EN-US"}[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12741_x1014_2140649931}**[ip-option ]{lang="EN-US"}**[{ *option-code* ]{lang="EN-US"}[\|]{lang="EN-US"}**[ internet-timestamp ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ loose-source-routing ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[record-route ]{lang="EN-US"}**[\| **route-alert** \| **security** ]{lang="EN-US"}[\|]{lang="EN-US"}**[ stream-id ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ strict-source-routing ]{lang="EN-US"}**[} ]{lang="EN-US"}[\[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}

[**[undo signature ]{lang="EN-US"}[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12741_x1014_x1729015543}**[ip-option ]{lang="EN-US"}**[{ *option-code* ]{lang="EN-US"}[\|]{lang="EN-US"}**[ internet-timestamp ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ loose-source-routing ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[record-route ]{lang="EN-US"}**[\| **route-alert** \| **security** ]{lang="EN-US"}[\|]{lang="EN-US"}**[ stream-id ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ strict-source-routing]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[signature detect ipv6-ext-header]{lang="EN-US"}**[ *ext-header-value*]{lang="EN-US"}]{#struct_0_12741_x1014_1562743974}*[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[\[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[signature detect ipv6-ext-header]{lang="EN-US"}**[ *next-header-value*]{lang="EN-US"}]{#struct_0_12741_x1014_x1204965068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x90815957}

[[所有类型的单包攻击报文的特征检测均处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12741_x1014_1498090061}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_114448563}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x19143294}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x372042501}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1722684719}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1782731710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x913964702}

[**[fraggle]{lang="EN-US"}**]{#struct_0_12741_x1014_x1833917074}[：表示]{style="font-family:宋体"}[Fraggle]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[fragment]{lang="EN-US"}**]{#struct_0_12741_x1014_1454123945}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片报文攻击。]{style="font-family:宋体"}

[**[icmp-type]{lang="EN-US"}**]{#struct_0_12741_x1014_1651885861}[：表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的报文攻击。可以指定报文的类型值，或者指定报文的类型关键字。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[icmp-type-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1762861817}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文类型]{lang="EN-US" style="font-family:宋体"}[的数值，取值范围为]{lang="EN-US" style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:
宋体"}[255]{lang="EN-US"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address-mask-reply]{lang="EN-US"}**]{#struct_0_12741_x1014_x1595365922}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP address mask reply]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address-mask-request]{lang="EN-US"}**]{#struct_0_12741_x1014_28278232}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP address mask request]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[destination-unreachable]{lang="EN-US"}**]{#struct_0_12741_x1014_x413433461}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP destination unreachable]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-reply]{lang="EN-US"}**]{#struct_0_12741_x1014_1194041440}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP echo reply]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-request]{lang="EN-US"}**]{#struct_0_12741_x1014_1665655830}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP echo request]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[information-reply]{lang="EN-US"}**]{#struct_0_12741_x1014_x1264280945}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP information reply]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[information-request]{lang="EN-US"}**]{#struct_0_12741_x1014_1975608042}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP information request]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[parameter-problem]{lang="EN-US"}**]{#struct_0_12741_x1014_1160417257}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP para problem]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect]{lang="EN-US"}**]{#struct_0_12741_x1014_x68254848}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP redirect]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source-quench]{lang="EN-US"}**]{#struct_0_12741_x1014_732930042}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP source quench]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-exceeded]{lang="EN-US"}**]{#struct_0_12741_x1014_237312503}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP time exceeded]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timestamp-reply]{lang="EN-US"}**]{#struct_0_12741_x1014_200050163}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP timestamp reply]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timestamp-request]{lang="EN-US"}**]{#struct_0_12741_x1014_1033276452}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP timestamp request]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[**[icmpv6-type]{lang="EN-US"}**]{#struct_0_12741_x1014_x1178611555}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[类型的报文攻击。可以指定报文的类型值，或者指定报文的类型关键字。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[icmpv6-type-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1793925828}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文类型的数值，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[destination-unreachable]{lang="EN-US"}**]{#struct_0_12741_x1014_926760469}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 destination unreachable]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-reply]{lang="EN-US"}**]{#struct_0_12741_x1014_1227637653}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 echo reply]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[echo-request]{lang="EN-US"}**]{#struct_0_12741_x1014_1038401278}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 echo request]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group-query]{lang="EN-US"}**]{#struct_0_12741_x1014_x1234132999}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 group query]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group-reduction]{lang="EN-US"}**]{#struct_0_12741_x1014_6339524}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 group reduction]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group-report]{lang="EN-US"}**]{#struct_0_12741_x1014_508899848}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 group report]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[packet-too-big]{lang="EN-US"}**]{#struct_0_12741_x1014_x2023964537}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMPv6 packet too big]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[parameter-problem]{lang="EN-US"}**]{#struct_0_12741_x1014_x1755611664}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP]{lang="EN-US"}[v6]{lang="EN-US"}[ para problem]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-exceeded]{lang="EN-US"}**]{#struct_0_12741_x1014_1640010791}[：表示]{lang="EN-US" style="font-family:宋体"}[ICMP]{lang="EN-US"}[v6]{lang="EN-US"}[ time exceeded]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[**[impossible]{lang="EN-US"}**]{#struct_0_12741_x1014_387472386}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[不可信报文的攻击。]{style="font-family:宋体"}

[**[ip-option]{lang="EN-US"}**]{#struct_0_12741_x1014_2140905797}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项类型的报文攻击。可以指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项代码值，或者指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项关键字。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[option-code]{lang="EN-US"}*]{#struct_0_12741_x1014_275241010}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项代码值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[internet-timestamp]{lang="EN-US"}**]{#struct_0_12741_x1014_x2137974509}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[timestamp]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loose-source-routing]{lang="EN-US"}**]{#struct_0_12741_x1014_x102496698}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[loose source route]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[record-route]{lang="EN-US"}**]{#struct_0_12741_x1014_269867679}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[record packet route]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-alert]{lang="EN-US"}**]{#struct_0_12741_x1014_x1937558118}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[route alert]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[security]{lang="EN-US"}**]{#struct_0_12741_x1014_x571922269}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[security]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stream-id]{lang="EN-US"}**]{#struct_0_12741_x1014_1749281815}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[stream identifier]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[strict-source-routing]{lang="EN-US"}**]{#struct_0_12741_x1014_417708211}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}[strict source route]{lang="EN-US"}[类型的报文攻击。]{lang="EN-US" style="font-family:宋体"}

[**[ip-option-abnormal]{lang="EN-US"}**]{#struct_0_12741_x1014_x1534907451}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项异常]{style="font-family:宋体"}[类型的报文攻击。]{style="font-family:宋体"}

[**[ipv6-ext-header]{lang="EN-US"}**]{#struct_0_12741_x1014_1167276345}*[ ]{lang="EN-US" style="font-size:
10.0pt;color:black"}[ext-header-value]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[扩展头]{style="font-family:宋体"}[参数值，取值范围在]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[land]{lang="EN-US"}**]{#struct_0_12741_x1014_741543860}[：表示]{style="font-family:宋体"}[Land]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[large-icmp]{lang="EN-US"}**]{#struct_0_12741_x1014_x1004433517}[：表示超大]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文的攻击。]{style="font-family:宋体"}

[**[large-icmpv6]{lang="EN-US"}**]{#struct_0_12741_x1014_6441152}[：表示超大]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的攻击。]{style="font-family:宋体"}

[**[ping-of-death]{lang="EN-US"}**]{#struct_0_12741_x1014_1159023101}[：表示]{style="font-family:宋体"}[Ping-of-death]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[smurf]{lang="EN-US"}**]{#struct_0_12741_x1014_238536512}[：表示]{style="font-family:宋体"}[Smurf]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[snork]{lang="EN-US"}**]{#struct_0_12741_x1014_1397862743}[：表示]{style="font-family:宋体"}[UDP Snork attack]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[tcp-all-flags]{lang="EN-US"}**]{#struct_0_12741_x1014_x96637325}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[所有标志位均置位的报文攻击。]{style="font-family:宋体"}

[**[tcp-fin-only]{lang="EN-US"}**]{#struct_0_12741_x1014_x327713095}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[仅]{style="font-family:宋体"}[FIN]{lang="EN-US"}[标志被置位的报文攻击。]{style="font-family:宋体"}

[**[tcp-invalid-flags]{lang="EN-US"}**]{#struct_0_12741_x1014_x2924715}[：表示]{style="font-family:宋体"}[TCP ]{lang="EN-US"}[标志位非法的报文攻击。]{style="font-family:宋体"}

[**[tcp-null-flag]{lang="EN-US"}**]{#struct_0_12741_x1014_2018759373}[：表示]{style="font-family:宋体"}[TCP ]{lang="EN-US"}[标志位为零的报文攻击。]{style="font-family:宋体"}

[**[tcp-syn-fin]{lang="EN-US"}**]{#struct_0_12741_x1014_1733109959}[：表示]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}[和]{style="font-family:宋体"}[FIN]{lang="EN-US"}[标志位被同时置位的报文攻击。]{style="font-family:宋体"}

[**[teardrop]{lang="EN-US"}**]{#struct_0_12741_x1014_31176490}[：表示]{style="font-family:宋体"}[teardrop]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[tiny-fragment]{lang="EN-US"}**]{#struct_0_12741_x1014_x435870363}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片报文的攻击。]{style="font-family:宋体"}

[**[traceroute]{lang="EN-US"}**]{#struct_0_12741_x1014_x443817195}[：表示]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[udp-bomb]{lang="EN-US"}**]{#struct_0_12741_x1014_851299026}[：表示]{style="font-family:宋体"}[UDP Bomb attack]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[winnuke]{lang="EN-US"}**]{#struct_0_12741_x1014_890773466}[：表示]{style="font-family:宋体"}[WinNuke]{lang="EN-US"}[类型的报文攻击。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1783492650}[：对指定报文攻击所采取的攻击防范处理行为。若不指定该参数，则]{style="font-family:宋体"}[采用该攻击报文所属的攻击防范级别所对应的默认处理行为。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_901231074}[：设置单包攻击的处理行为为丢弃报文。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x1313332404}[：设置单包攻击的处理行为为发送日志。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x454773074}[：不采取任何动作。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_849777882}

[[可以通过多次执行本命令开启多种类型的]{style="font-family:宋体"}]{#struct_0_12741_x1014_1597260431}[单包攻击报文的特征检测。]{style="font-family:
宋体"}

[[若通过数值指定了报文类型，则当指定的数值为标准的报文]{style="font-family:宋体"}]{#struct_0_12741_x1014_x641771283}[类型值时，在显示信息中将会显示该数值对应的报文类型字符串，否则显示为数值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1926920685}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1020872621}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中开启对]{style="font-family:宋体"}[Smurf]{lang="EN-US"}[攻击报文的特征检测，并指定攻击防范处理行为为为丢弃报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_440881401}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] signature detect smurf action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1399857172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_855428077}**[level ]{lang="EN-US"}[action]{lang="EN-US"}**
:::

::: {#-397225840 .myid}
[]{#_Toc404793947}[]{#struct_0_12741_x1014_x1360249124}[]{#_Toc340488524}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature level action**

------------------------------------------------------------------------

[**[signature level action]{lang="EN-US"}**]{#struct_0_12741_x1014_1623340866}[命令用来配置指定级别单包攻击的处理行为。]{style="font-family:宋体"}

[**[undo signature level action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1131622924}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1730362302}

[**[signature level]{lang="EN-US"}**[ { **high** \| **info** \| **low** \| **medium** } **action** { { **drop** \| **logging** } \* \| **none** }]{lang="EN-US"}]{#struct_0_12741_x1014_399692601}

[**[undo signature level]{lang="EN-US"}**[ { **high** \| **info** \| **low** \| **medium** } **action**]{lang="EN-US"}]{#struct_0_12741_x1014_1277048891}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1774415834}

[[对提示级别和低级别的单包攻击的处理行为是发送日志；对中级别的单包攻击的处理行为是发送日志并丢包；对高级别的单包攻击的处理行为是发送日志并丢包。]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1877371828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1645188266}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_496101524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_820086220}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2054182213}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_790691377}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1301321393}

[**[high]{lang="EN-US"}**]{#struct_0_12741_x1014_654219425}[：表示高级别的单包攻击，暂无实例。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_12741_x1014_991515528}[：表示提示级别的单包攻击，例如]{style="font-family:宋体"}[Large ICMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_12741_x1014_x1959821081}[：表示低级别的单包攻击，例如]{style="font-family:宋体"}[Traceroute]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_12741_x1014_x934668731}[：表示中级别的单包攻击，例如]{style="font-family:宋体"}[Winnuke]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_75401130}[：设置单包攻击的处理行为为丢弃报文。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_38452921}[：设置单包攻击的处理行为为发送日志。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_616319647}[：不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x614927991}

[[系统根据单包攻击结果的严重程度由低到高将其划分为四个攻击级别：提示、低级、中级、高级。开启某一个级别的]{style="font-family:宋体"}]{#struct_0_12741_x1014_113330083}[单包攻击报文的特征检测]{style="font-family:宋体"}[，相当于批量开启了属于该级别的所有类型的单包攻击报文的特征检测。]{style="font-family:宋体"}[针对某一级别的单包攻击的处理行为由]{style="font-family:宋体"}**[signature level action]{lang="EN-US"}**[命令指定。]{style="font-family:宋体"}

[[若同时通过]{style="font-family:宋体"}**[signature detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x214297279}[命令开启了具体类型的单包攻击报文的特征检测，则以]{style="font-family:宋体"}**[signature detect]{lang="EN-US"}**[命令配置的参数为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1938191978}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1618762918}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置对提示级别的单包攻击的处理行为是丢弃后续报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_154409868}

[\[Sysname\] attack-defense policy 1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-1\] signature level info action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x353834843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature]{lang="EN-US"}**]{#struct_0_12741_x1014_1322524829}**[ detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature]{lang="EN-US"}**]{#struct_0_12741_x1014_x476225329}**[ level detect]{lang="EN-US"}**
:::

::: {#1907806521 .myid}
[]{#_Toc404793948}[]{#struct_0_12741_x1014_x1551736916}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature level detect**

------------------------------------------------------------------------

[**[signature level detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1070857444}[命令用来开启指定级别单包攻击报文的特征检测。]{style="font-family:宋体"}

[**[undo signature level detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x9358503}[命令用来取消对指定级别的单包攻击报文的特征检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x554499110}

[**[signature level]{lang="EN-US"}**[ { **high** \| **info** \| **low** \| **medium** } **detect**]{lang="EN-US"}]{#struct_0_12741_x1014_x372108037}

[**[undo signature level]{lang="EN-US"}**[ { **high** \| **info** \| **low** \| **medium** } **detect**]{lang="EN-US"}]{#struct_0_12741_x1014_x528982749}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1886197010}

[[未开启任何级别的单包攻击报文的特征检测。]{style="font-family:宋体"}]{#struct_0_12741_x1014_87342816}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1756065394}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1900938392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2058995620}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x330575810}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2127731566}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1193975904}

[**[high]{lang="EN-US"}**]{#struct_0_12741_x1014_x127486633}[：表示高级别的单包攻击，暂无实例。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_12741_x1014_x1777395677}[：表示提示级别的单包攻击，例如]{style="font-family:宋体"}[Large ICMP]{lang="EN-US"}[报文攻击。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_12741_x1014_x1144606114}[：表示低级别的单包攻击，例如]{style="font-family:宋体"}[Traceroute]{lang="EN-US"}[报文攻击。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_12741_x1014_1891030209}[：表示中级别的单包攻击，例如]{style="font-family:宋体"}[Winnuke]{lang="EN-US"}[报文攻击。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_682186925}

[[系统根据单包攻击结果的严重程度将其划分为四个级别：提示、低级、中级、高级。开启某一个级别的]{style="font-family:宋体"}]{#struct_0_12741_x1014_x385666861}[单包攻击报文的特征检测]{style="font-family:宋体"}[，相当于批量开启了属于该级别的所有单包攻击报文的特征检测。]{style="font-family:宋体"}[针对某一级别的单包攻击的处理行为由]{style="font-family:宋体"}**[signature level action]{lang="EN-US"}**[命令指定。]{style="font-family:宋体"}[若通过]{style="font-family:宋体"}**[signature detect]{lang="EN-US"}**[命令开启了具体的单包攻击报文的特征检测，则对该类攻击报文的处理行为以]{style="font-family:宋体"}**[signature detect]{lang="EN-US"}**[命令配置的参数为准。]{style="font-family:宋体"}

[[可通过]{style="font-family:宋体"}**[display attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_x1681314204}[命令查看各类型单包攻击所属的级别。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1652500095}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_33105012}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启提示级别的单包攻击报文的特征检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1178677091}

[\[Sysname\] attack-defense policy 1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-1\] signature level info detect]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1051901859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display attack-defense policy]{lang="EN-US"}**]{#struct_0_12741_x1014_1014017876}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1803519547}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[signature]{lang="EN-US"}**]{#struct_0_12741_x1014_x544819437}**[ level action]{lang="EN-US"}**
:::

::: {#1244956865 .myid}
[]{#_Toc404793949}[]{#struct_0_12741_x1014_x1521538233}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood action**

------------------------------------------------------------------------

[**[syn-ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1068862189}[命令用来配置对]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo syn-ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_599126890}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_157000467}

[**[syn-ack-flood action ]{lang="EN-US"}**[{]{lang="EN-US"}[ **client-verify** \| **drop** \| **logging** }\*]{lang="EN-US"}]{#struct_0_12741_x1014_591726457}

[**[undo syn-ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1852622536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_387406850}

[[不对检测到的]{style="font-family:宋体"}[ SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x615151699}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_74145141}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1252312843}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1919630330}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1279657184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_364149716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_424211666}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x561810738}[：表示自动将]{style="font-family:宋体"}[受到攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加]{style="font-family:宋体"}[到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_464462282}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x1400689723}[：表示输出告警日志，即设备检测到攻击发生时，生成记录]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_677849515}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x1672645527}[参数的使用需要和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的接口检测到]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1281865486}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_1693889430}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置对]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范的全局处理行为是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1592278580}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-ack-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_14660622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify ]{lang="EN-US"}**]{#struct_0_12741_x1014_545074501}**[tcp enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x845623890}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_737320188}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_165394218}**[threshold]{lang="EN-US"}**
:::

::: {#-1950533276 .myid}
[]{#_Toc404793950}[]{#struct_0_12741_x1014_1616460475}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood detect**

------------------------------------------------------------------------

[**[syn-ack-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_1911489695}[命令用来对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测触发阈值]{style="font-family:宋体"}[和防范行为。]{style="font-family:宋体"}

[**[undo syn-ack-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x909167387}[命令用来取消对指定]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x437825880}

[**[syn-ack-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1751409640}

[**[undo syn-ack-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_2040743778}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1639498400}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1807726958}[地址配置]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1887046852}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1731478159}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1378043541}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_782734967}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1107348625}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_963907138}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1855176207}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_x1102026416}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x376984228}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1241459378}[：指定]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x351313812}[：设置对]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x997405196}[：表示自动将受到攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地]{style="font-family:宋体"}[址添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_x1851030531}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x252664115}[：表示输出告警日志，即]{style="font-family:宋体"}[设备检测到]{style="font-family:宋体"}[攻]{style="font-family:宋体"}[击发生时，生成告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:
宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x173658679}[：]{style="font-family:宋体"}[表示不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_327295070}

[[每[个攻击防范策略下可以同时对多个]{style="color:black"}]{style="font-family:宋体"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_12741_x1014_1983261534}[地址配置]{style="font-family:宋体;
color:black"}[SYN-ACK flood]{lang="EN-US" style="color:black"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[使能]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US" style="color:black"}[ flood]{lang="EN-US"}]{#struct_0_12741_x1014_202107980}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US" style="color:black"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US" style="color:black"}[ flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1498038482}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x993676339}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_924909105}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-ack-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x651766276}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1751660298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_702424279}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x715193515}**[threshold]{lang="EN-US"}**
:::

::: {#122321439 .myid}
[]{#_Toc404793951}[]{#struct_0_12741_x1014_280523847}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood detect non-specific**

------------------------------------------------------------------------

[**[syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1903510534}[命令用来对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1610556499}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_734588350}

[**[syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x171395395}

[**[undo syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1803974250}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1902413139}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_991157509}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1421574260}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_2024759499}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x748535638}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1100565666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1002278432}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x11156012}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1013394820}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[syn-ack-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[syn-ack-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x237890309}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x818945257}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1862742224}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-ack-flood detect non-specific ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_909130915}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1330160286}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_404547946}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x249673524}**[threshold]{lang="EN-US"}**
:::

::: {#-1657628576 .myid}
[]{#_Toc404793952}[]{#struct_0_12741_x1014_x610755341}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood threshold**

------------------------------------------------------------------------

[**[syn-ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1890005140}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo syn-ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1328193632}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1350856303}

[**[syn-ack-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_334988870}

[**[undo syn-ack-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x1662394684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1882217247}

[[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1537616503}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x251439078}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1535761717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1131945985}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_709020917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1044459363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_455964832}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_289453481}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_846012090}

[[对于没有专门配置]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}]{#struct_0_12741_x1014_x876057228}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1944565596}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x339386863}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[全局触发]{style="font-family:宋体"}[阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN-ACK]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[SYN-ACK flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x1636435710}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-ack-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x196015703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-]{lang="EN-US"}**]{#struct_0_12741_x1014_x1607564526}**[ack-]{lang="EN-US"}[flood action]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-]{lang="EN-US"}**]{#struct_0_12741_x1014_521624578}**[ack-]{lang="EN-US"}[flood ]{lang="EN-US"}[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-ack-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_194728508}
:::

::: {#2089584542 .myid}
[]{#_Toc404793953}[]{#struct_0_12741_x1014_1186653759}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood action**

------------------------------------------------------------------------

[**[syn-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x950402416}[命令用来配置对]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo syn-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1447818926}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x710749156}

[**[syn-flood action]{lang="EN-US"}**[ { **client-verify** \| **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_78250751}

[**[undo syn-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1831156340}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1673497214}

[[不对检测到的]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_894794634}[攻击采取任何措施。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1156996376}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_571653891}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1400755259}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_619570015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2080717340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x735197017}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_1572045885}[：表示自动将受到攻击]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地]{style="font-family:宋体"}[址添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_2055377615}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_722921391}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_12741_x1014_1341416}

[[本命令中]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x1169000333}[参数的使用分别需要和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能配合。使能了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的接口检测到]{style="font-family:宋体"}[ACK flood]{lang="EN-US"}[攻击时，若本命令中指定了]{style="font-family:宋体"}**[client-verify]{lang="EN-US"}**[参数，则设备会将受攻击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址动态添加到相应客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中，并对与这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x722354596}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1962922335}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置对]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_165328682}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_74213806}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x837737636}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_1817412840}**[ detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood]{lang="EN-US"}**]{#struct_0_12741_x1014_x1080747161}**[ threshold]{lang="EN-US"}**
:::

::: {#1261406995 .myid}
[]{#_Toc404793954}[]{#struct_0_12741_x1014_281102591}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood detect**

------------------------------------------------------------------------

[**[syn-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_2060473974}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测的]{style="font-family:宋体"}[触发阈值和对]{style="font-family:
宋体"}[SYN flood]{lang="EN-US"}[攻击的]{style="font-family:
宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo syn-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x1001675361}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_877023579}

[**[syn-flood]{lang="EN-US"}**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_52276393}

[**[undo syn-flood detect]{lang="EN-US"}**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_717110552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1270970677}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1731412623}[地址配置]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1396112846}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1064660828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1896305544}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1278101859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_669381171}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x749877357}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1999030983}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_685725861}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_1482533923}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_65077810}[：指定]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_x942176292}[：设置对]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[client-verify]{lang="EN-US"}**]{#struct_0_12741_x1014_x997470732}[：表示自动将受到攻]{style="font-family:宋体"}[击的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址添加到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证的]{style="font-family:宋体"}[受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}[。]{style="font-family:宋体"}[若客户端验证功能已使能，则对客户端与受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的连接进行代理。]{style="font-family:宋体"}[本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_1699751462}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_984875475}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x174117437}[：]{style="font-family:宋体"}[表示不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x350515434}

[[每个攻击防范策略下可以同时对多个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x1689474206}[地址配置]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1432584309}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1263082097}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x1428862024}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1299603213}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1846147737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1387135825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_924843569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x591789280}**[threshold]{lang="EN-US"}**
:::

::: {#1918802353 .myid}
[]{#_Toc404793955}[]{#struct_0_12741_x1014_875105500}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood detect non-specific**

------------------------------------------------------------------------

[**[syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x433588334}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1146124469}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1275350799}

[**[syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x932945708}

[**[undo syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x2075616271}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x258814675}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_x1804039786}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x651033265}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1337889745}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_130696276}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x2065548913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_922336873}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1526270234}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_366446121}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[syn-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[syn-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1071300713}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x2025638613}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x237955845}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-flood detect non-specific]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1615225875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1467913101}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1460514934}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1455236500}**[threshold]{lang="EN-US"}**
:::

::: {#998536135 .myid}
[]{#_Toc404793956}[]{#struct_0_12741_x1014_454191537}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood threshold**

------------------------------------------------------------------------

[**[syn-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1915277239}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo syn-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_1179220479}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1126380874}

[**[syn-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_1328128096}

[**[undo syn-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_572643474}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_488001783}

[[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_576897087}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_882065853}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_1594552834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_663449300}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1000838324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1338108425}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1116977618}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1044524899}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1767161570}

[[对于没有专门配置]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}]{#struct_0_12741_x1014_x836777908}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1312455451}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_563101564}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[全局触发]{style="font-family:宋体"}[阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x310854389}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] syn-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_394634645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1544650574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_2036089742}**[detect ]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1919862565}
:::

::: {#-579893585 .myid}
[]{#_Toc404793957}[]{#struct_0_12741_x1014_521559042}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood action**

------------------------------------------------------------------------

[**[udp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x1613237116}[命令用来配置对]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范的全局处理行为]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo udp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1180061028}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_228060175}

[**[udp-flood action]{lang="EN-US"}**[ { **drop** \| **logging** } \*]{lang="EN-US"}]{#struct_0_12741_x1014_1488445395}

[**[undo udp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_1554431484}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1732333575}

[[不对检测到的]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_217823837}[攻击进行任何处理。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1592687769}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x315435172}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1400820795}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1966498843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2125377132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x501370334}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_2088825117}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_x2085572367}[：表示输出告警日志，即设备检测到攻击发生时，生成]{style="font-family:宋体"}[告警信息，生成的告警信息将被]{style="font-family:宋体"}[发送到日志系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1001255583}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x560367591}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[配置对]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范的全局处理行为是丢弃后续报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_165263146}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] udp-flood action drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_838185005}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x1851354616}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood]{lang="EN-US"}[ detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_1253238858}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x68433362}**[threshold]{lang="EN-US"}**
:::

::: {#277049612 .myid}
[]{#_Toc404793958}[]{#struct_0_12741_x1014_x227094517}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood detect**

------------------------------------------------------------------------

[**[udp-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_x536269305}[命令用来开启对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测，并配置]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测的触发阈值]{style="font-family:宋体"}[和对]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击的]{style="font-family:宋体"}[处理行为。]{style="font-family:宋体"}

[**[undo udp-flood detect]{lang="EN-US"}**]{#struct_0_12741_x1014_1145377325}[命令用来取消对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1567816948}

[**[udp-flood detect ]{lang="EN-US"}**[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **threshold** *threshold-value* \] \[ **action** { { **drop** \| **logging** } \* \| **none** } \]]{lang="EN-US"}]{#struct_0_12741_x1014_x1922036119}

[**[undo udp-flood detect]{lang="EN-US"}**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12741_x1014_1662962959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_431635421}

[[未对任何指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_1731347087}[地址配置]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1017296740}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_3665569}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_648483733}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x488392503}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x778216621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1285046916}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_12741_x1014_425358973}[：指定要保护的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址或全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_12741_x1014_1048461423}[：指定要保护的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12741_x1014_x2052343825}[：受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示该保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[属于公网。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x997536268}[：指定]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范的触发阈值。其中，]{style="font-family:宋体"}*[threshold-value]{lang="EN-US"}*[为向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_12741_x1014_1678118718}[：设置对]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击的处理行为。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_12741_x1014_1718652942}[：表示丢弃]{style="font-family:宋体"}[攻击]{style="font-family:宋体"}[报文，即设备检测到攻击发生后，向被攻击者发送的后续所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文都会被丢弃。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_12741_x1014_2147319053}[：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_12741_x1014_x173658685}[：表示]{style="font-family:宋体"}[不采取任何动作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x948678624}

[[每个攻击防范策略下可以同时对多个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12741_x1014_x214256026}[地址配置]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范参数，具体数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_x1991918801}[攻击防范后，设备处于攻击检测状态，当它监测到向指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文的速率持续达到或超过了触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的]{style="font-family:宋体"}[3/4]{lang="EN-US"}[）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x767852043}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_706611961}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中]{style="font-family:宋体"}[开启对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.2]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测，并指定触发阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当设备监测到向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[2000]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_924778033}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] udp-flood detect ip 192.168.1.2 threshold 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1888051584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_x383456251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x804245981}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_2047752127}**[threshold]{lang="EN-US"}**
:::

::: {#-813919139 .myid}
[]{#_Toc404793959}[]{#struct_0_12741_x1014_1260539394}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood detect non-specific**

------------------------------------------------------------------------

[**[udp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1499127051}[命令用来对所有]{style="font-family:
宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[**[undo udp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x485935149}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1457949778}

[**[udp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x1804105322}

[**[undo udp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_x452983182}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1400597211}

[[未对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_1703152363}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_266418842}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x897080817}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1647696576}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_335794306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_1837481373}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1421189113}

[[对所有]{style="font-family:宋体"}]{#struct_0_12741_x1014_393432373}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址开]{style="font-family:宋体"}[启]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测后]{style="font-family:宋体"}[，设备将采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置（由]{style="font-family:宋体"}**[udp-flood threshold]{lang="EN-US"}**[命令设置）和处理行为（由]{style="font-family:宋体"}**[udp-flood action]{lang="EN-US"}**[命令配置）对这些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x238021381}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_966552844}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中，对所有]{style="font-family:宋体"}[非受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_x91435916}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] udp-flood detect non-specific]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1538065023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_636014101}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_989440640}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_1979408135}**[threshold]{lang="EN-US"}**
:::

::: {#1868780481 .myid}
[]{#_Toc404793960}[]{#struct_0_12741_x1014_x311914580}

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood threshold**

------------------------------------------------------------------------

[**[udp-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_405906806}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范的全局触发阈值。]{style="font-family:宋体"}

[**[undo udp-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_x1575570208}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_1328062560}

[**[udp-flood threshold]{lang="EN-US"}***[ ]{lang="EN-US"}[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_x1332732644}

[**[undo udp-flood threshold]{lang="EN-US"}**]{#struct_0_12741_x1014_318682723}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1712403626}

[[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_611641714}[攻击防范的全局触发阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12741_x1014_2119326651}

[[攻击防范策略视图]{style="font-family:宋体"}]{#struct_0_12741_x1014_x775954126}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12741_x1014_566744401}

[[network-admin]{lang="EN-US"}]{#struct_0_12741_x1014_2097812920}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12741_x1014_x1369021968}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1044590435}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_12741_x1014_2080354137}[：指定向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64000]{lang="EN-US"}[。使能]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范后，设备处于攻击检测状态，当它监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文的速率持续达到或超过了该触发阈值时，即认为该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址受到了]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x1927136069}

[[对于没有专门配置]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}]{#struct_0_12741_x1014_1656933845}[攻击防范检测的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，设备采用全局的]{style="font-family:宋体"}[阈值]{style="font-family:宋体"}[设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器或者]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器）的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12741_x1014_x554449380}

[[\# ]{lang="EN-US"}]{#struct_0_12741_x1014_x173530419}[在攻击防范策略]{style="font-family:宋体"}[atk-policy-1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范的]{style="font-family:宋体"}[全局触发阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[当设备监测到向某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址每秒发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数持续达到或超过]{style="font-family:宋体"}[100]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[UDP flood]{lang="EN-US"}[攻击防范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12741_x1014_1515586145}

[\[Sysname\] attack-defense policy atk-policy-1]{lang="EN-US"}

[\[Sysname-attack-defense-policy-atk-policy-1\] udp-flood threshold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12741_x1014_383184307}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood action]{lang="EN-US"}**]{#struct_0_12741_x1014_184057797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood ]{lang="EN-US"}**]{#struct_0_12741_x1014_x572523481}**[detect]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-flood detect non-specific]{lang="EN-US"}**]{#struct_0_12741_x1014_521493506}
:::
