
**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood action**

------------------------------------------------------------------------

**[ack-flood action**]命令用来配置ACK flood攻击防范的全局处理行为。

**[undo ack-flood action**]命令用来恢复缺省情况。

【命令】

**[ack-flood action **[{ **client-verify** \| **drop** \| **logging** } \*]]

**[undo ack-flood action**]

【缺省情况】

不对检测到的ACK flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有ACK报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用需要和TCP客户端验证功能配合。使能了TCP客户端验证功能的接口检测到ACK flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\# 在攻击防范策略atk-policy-1中配置ACK flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 ack-flood action drop

【相关命令】

·**ack-flood ****threshold**

·**ack-flood ****detect **

·**ack-flood detect non-specific**

·**client-verify tcp ****enable**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood detect**

------------------------------------------------------------------------

**[ack-flood detect**]命令用来开启对指定IP地址的ACK flood攻击防范检测，并配置ACK flood攻击防范的触发阈值和对ACK flood攻击的处理行为。

**[undo ack-flood detect**]命令用来取消对指定IP地址的ACK flood攻击防范检测。

【命令】

**[ack-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo ack-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ] ]]

【缺省情况】

未对任何指定IP地址配置ACK flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold*** threshold-value*]：指定ACK flood攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的ACK报文数目，取值范围为1～1000000。

**[action**]：设置对ACK flood攻击的处理行为。若不指定该参数，则表示采用ACK flood攻击防范的全局处理行为。

**[client-verify**]：表示自动将被攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有ACK报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置ACK flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能ACK flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送ACK报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了ACK flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的ACK flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的ACK报文数持续达到或超过2000时，启动ACK flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 ack-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**ack-flood action**

·**ack-flood detect non-specific**

·**ack-flood ****threshold**

·**client-verify tcp ****enable**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood detect non-specific**

------------------------------------------------------------------------

**[ack-flood detect non-specific**]命令用来对所有非受保护IP地址开启ACK flood攻击防范检测。

**[undo ack-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[ack-flood detect non-specific**]

**[undo ack-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启ACK flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有未配置具体攻击防范策略的IP地址开启ACK flood攻击防范检测后，设备将采用全局的阈值设置（由**ack-flood threshold**命令设置）和处理行为（由**ack-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启ACK flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 ack-flood detect non-specific

【相关命令】

·**ack-flood action**

·**ack-flood ****detect **

·**ack-flood threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- ack-flood threshold**

------------------------------------------------------------------------

**[ack-flood threshold**]命令用来配置ACK flood攻击防范的全局触发阈值。

**[undo ack-flood threshold**]命令用来恢复缺省情况。

【命令】

**[ack-flood threshold*** threshold-value*]

**[undo ack-flood threshold**]

【缺省情况】

ACK flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的ACK报文数目，取值范围为1～1000000。使能ACK flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送ACK报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了ACK flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置ACK flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的ACK报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置ACK flood攻击防范的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的ACK报文数持续达到或超过100时，启动ACK flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 ack-flood threshold 100

【相关命令】

·**ack-flood action**

·**ack-flood ****detect **

·**ack-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense apply policy**

------------------------------------------------------------------------

**[attack-defense apply policy**]命令用来在接口上应用攻击防范策略。

**[undo attack-defense apply policy**]命令用来恢复缺省情况。

【命令】

**[attack-defense apply** **policy** *policy-name*]

**[undo attack-defense apply policy**]

【缺省情况】

接口上未应用任何攻击防范策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"\_"和"-"。

【使用指导】

一个接口上只能应用一个攻击防范策略（可多次配置，最后一次配置的有效），但一个攻击防范策略可应用到多个接口上。

【举例】

\# 将攻击防范策略atk-policy-1应用到接口GigabitEthernet1/0/1上。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 attack-defense apply policy atk-policy-1

【相关命令】

·**attack-defense policy**

·**display attack-defense policy**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense local apply policy**

------------------------------------------------------------------------

**[attack-defense local apply policy**]命令用来在本机应用安全攻击防范策略。

**[undo attack-defense local apply policy**]命令用来恢复缺省情况。

【命令】

**[attack-defense** **local**** apply policy** *policy-name*]

**[undo attack-defense local apply policy**]

【缺省情况】

本机未应用任何攻击防范策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"\_"和"-"。

【使用指导】

此功能主要用于交换机产品，缺省情况下交换机产品将需要转发的报文下发给硬件转发，只有目的地址是本机的报文才会由软件处理，但软件没有攻击防范功能。因此在交换机产品上，为处理针对本机的攻击，需要通过在本机上应用攻击防范策略来实现。

对于非交换机产品，可以通过在本机上应用攻击方法策略提高对目的地址为本机的攻击报文的处理效率。

·本机只能应用一个攻击防范策略（可多次配置，最后一次配置的有效），但一个攻击防范策略除了可以应用到本机外，还可应用到多个接口上。

·当同时在接口和本机应用攻击防范策略时，目的地址是本机的报文到达设备后，将会被根据应用在接口上的策略和应用在本机的策略先后检测两次。

【举例】

\# 在本机应用攻击防范策略atk-policy-1。

\<Sysname\> system-view

Sysname attack-defense local apply policy atk-policy-1

【相关命令】

·**attack-defense policy**

·**display attack-defense policy**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense policy**

------------------------------------------------------------------------

**[attack-defense policy**]命令用来创建一个攻击防范策略，并进入攻击防范策略视图。

**[undo attack-defense policy**]命令用来删除指定的攻击防范策略。

【命令】

**[attack-defense policy** *policy-name*]

**[undo attack-defense policy** *policy-name*]

【缺省情况】

不存在任何攻击防范策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"\_"和"-"。

【使用指导】

无

【举例】

\# 创建攻击防范策略atk-policy-1，并进入攻击防范策略视图。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1

【相关命令】

·**attack-defense apply policy**

·**display attack-defense policy**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense signature log non-aggregate**

------------------------------------------------------------------------

**[attack-defense signature log non-aggregate**]命令用来指定对单包攻击防范日志非聚合输出。

**[undo attack-defense** **signature log non-aggregate**]命令用来恢复缺省情况。

【命令】

**[attack-defense signature log non-aggregate**]

**[undo attack-defense** **signature log non-aggregate**]

【缺省情况】

单包攻击防范的日志信息经系统聚合后再输出。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对日志进行聚合输出是指，在一定时间内，对在同一个接口上检测到的相同攻击类型、相同攻击防范动作、相同的源/目的地址以及属于相同VPN的单包攻击的所有日志聚合成一条日志输出。通常不建议开启单包攻击防范的日志非聚合输出功能，因为在单包攻击较为频繁的情况下，它会导致大量日志信息输出，占用控制台的显示资源。

【举例】

\# 开启对单包攻击防范日志的非聚合输出功能。

\<Sysname\> system-view

Sysname attack-defense signature log non-aggregate

【相关命令】

·**signature ****detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- attack-defense tcp fragment enable**

------------------------------------------------------------------------

**[attack-defense tcp fragment enable**]命令用来开启TCP分片攻击防范功能。

**[undo attack-defense tcp fragment enable**]命令用来关闭TCP分片攻击防范功能。

【命令】

**[attack-defense tcp fragment enable**]

**[undo attack-defense tcp fragment enable**]

【缺省情况】

TCP分片攻击防范功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备的包过滤功能一般是通过判断TCP首个分片中的五元组（源IP地址、源端口号、目的IP地址、目的端口号、传输层协议号）信息来决定后续TCP分片是否允许通过。RFC 1858对TCP分片报文进行了规定，认为TCP分片报文中，首片报文中TCP报文长度小于20字节，或后续分片报文中分片偏移量等于8字节的报文为TCP分片攻击报文。这类报文可以成功绕过上述包过滤功能，对设备造成攻击。为防止这类攻击，可以在设备上开启TCP分片攻击防范功能，对TCP分片攻击报文进行丢弃。

需要注意的是，如果设备上开启了TCP分片攻击防范功能，并应用了单包攻击防范策略，则TCP分片攻击防范功能会先于单包攻击防范策略检测并处理入方向的TCP报文。

【举例】

\# 开启TCP分片攻击防范功能。

\<Sysname\> system-view

Sysname attack-defense tcp fragment enable

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist enable**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[blacklist enable**]命令用来开启接口上的黑名单过滤功能。

**[undo blacklist enable**]命令用来关闭接口上的黑名单过滤功能。

【命令】

**[blacklist enable**]

**[undo blacklist enable**]

【缺省情况】

接口上的黑名单过滤功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

若全局的黑名单过滤功能处于开启状态，则所有接口上的黑名单过滤功能均处于开启状态。若全局的黑名单过滤功能处于关闭状态，则接口上的黑名单过滤功能由本命令决定是否开启。

【举例】

\# 开启接口GigabitEthernet1/0/1上的黑名单过滤功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1blacklist enable

【相关命令】

·**blacklist ip**

·**blacklist ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist global enable**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[blacklist global enable**]命令用来开启全局黑名单过滤功能。

**[undo blacklist global enable**]命令用来关闭全局黑名单过滤功能。

【命令】

**[blacklist global enable**]

**[undo blacklist global enable**]

【缺省情况】

全局黑名单过滤功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【使用指导】

使能全局黑名单过滤功能表示开启所有接口下黑名单过滤功能。

【举例】

\# 开启全局黑名单过滤功能。

\<Sysname\> system-view

Sysname blacklist global enable

【相关命令】

·**blacklist enable**

·**blacklist ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist ip**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[blacklist ip**]命令用来添加IPv4黑名单表项。

**[undo blacklist ip**]命令用来删除指定的IPv4黑名单表项。

【命令】

**[blacklist ip*** source-ip-address * **vpn-instance** *vpn-instance-name* ]  **ds-lite-peer** *ds-lite-peer-address*   **timeout** *minutes*

**[undo blacklist******ip*** source-ip-address * **vpn-instance** *vpn-instance-name* ]  **ds-lite-peer** *ds-lite-peer-address*

【缺省情况】

无IPv4黑名单表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-ip-address*]：黑名单的IPv4地址，用于匹配报文的源IP地址。

**[vpn-instance** *vpn-instance-name*]：黑名单所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该黑名单属于公网。

**[ds-lite-peer ***ds-lite-peer-address*]：黑名单所属的DS-Lite隧道对端地址。其中，*ds-lite-peer-address*表示黑名单的IPv4地址所属的DS-Lite隧道B4端IPv6地址。

**[timeout ***minutes*]：黑名单表项的老化时间。其中，*minutes*表示老化时间，取值范围为1～1000，单位为分钟。若不指定该参数，则表示该黑名单表项永不老化，除非用户手动将其删除。

【使用指导】

通过执行**undo blacklist ip**命令可以删除用户手工添加的黑名单表项，动态生成的黑名单表项需通过执行**reset blacklist ip**命令删除。指定了老化时间的黑名单表项不会被保存在配置文件中，且保存配置重启后会被删除。可通过执行**display blacklist ip**命令查看当前所有生效的IPv4黑名单表项。

【举例】

\# 将IP地址192.168.1.2加入黑名单，指定其老化时间为20分钟。

\<Sysname\> system-view

Sysname blacklist ip 192.168.1.2 timeout 20

【相关命令】

·**blacklist enable**

·**blacklist global enable**

·**display blacklist ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist ipv6**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[blacklist ipv6**]命令用来添加IPv6黑名单表项。

**[undo blacklist ipv6**]命令用来删除指定的IPv6黑名单表项。

【命令】

**[blacklist ipv6*** source-ipv6-address * **vpn-instance** *vpn-instance-name* ]  **timeout** *minutes*

**[undo blacklist******ipv6*** source-ipv6-address * **vpn-instance** *vpn-instance-name* ]

【缺省情况】

无IPv4黑名单表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-ipv6-address*]：黑名单的IPv6地址，用于匹配报文的源IP地址。

**[vpn-instance** *vpn-instance-name*]：黑名单所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该黑名单属于公网。

**[timeout ***minutes*]：黑名单表项的老化时间。其中，*minutes*表示老化时间，取值范围为1～1000，单位为分钟。若不指定该参数，则表示该黑名单表项永不老化，除非用户手动将其删除。

【使用指导】

通过执行**undo blacklist ipv6**命令可以删除用户手工添加的黑名单表项，动态生成的黑名单表项需通过执行**reset blacklist ipv6**命令删除。指定了老化时间的黑名单表项不会被保存在配置文件中，且保存配置重启后会被删除。可通过执行**display blacklist ipv6**命令查看当前所有生效的IPv6黑名单表项。

【举例】

\# 将IPv6地址2012::12:25加入黑名单，指定其老化时间为10分钟。

\<Sysname\> system-view

Sysname blacklist ipv6 2012::12:25 timeout 10

【相关命令】

·**blacklist enable**

·**blacklist global enable**

·**blacklist ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- blacklist logging enable**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[blacklist logging enable**]命令用来使能黑名单日志功能。

**[undo blacklist logging enable**]命令用来关闭黑名单日志功能。

【命令】

**[blacklist logging enable**]

**[undo blacklist logging enable**]

【缺省情况】

黑名单日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启黑名单日志功能后，当增加黑名单、删除黑名单、扫描攻击防范动态添加黑名单、黑名单老化被删除时会有相应的日志输出，日志的内容主要包括黑名单的源IP地址、DS-Lite隧道对端地址、VPN实例名称、添加或删除的原因以及老化时间等。

【举例】

\# 开启黑名单日志功能，并配置一条黑名单后，输出如下日志信息。

\<Sysname\> system-view

Sysname blacklist logging enable

Sysname blacklist ip 192.168.100.12

%Mar 13 03:47:49:736 2013 Sysname BLS/5/BLS_ENTRY_ADD:SrcIPAddr(1003)=192.168.100.12; DSLiteTunnelPeer(1040)=\--; RcvVPNInstance(1041)=\--; TTL(1051)=; Reason(1052)=Configuration.

\# 删除一条黑名单后，输出如下日志信息。

Sysname undo blacklist ip 192.168.100.12

%Mar 13 03:49:52:737 2013 Sysname BLS/5/BLS_ENTRY_DEL:SrcIPAddr(1003)=192.168.100.12; DSLiteTunnelPeer(1040)=\--; RcvVPNInstance(1041)=\--; Reason(1052)=Configuration.

【相关命令】

·**blacklist ip**

·**blacklist ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify dns enable**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[client-verify dns enable**]命令用来在接口上使能DNS客户端验证功能。

**[undo client-verify dns enable**]命令用来恢复缺省情况。

【命令】

**[client-verify dns enable**]

**[undo client-verify dns enable**]

【缺省情况】

接口上的DNS客户端验证功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该功能一般应用在设备连接外部网络的接口上，用来保护内部网络的DNS服务器免受外部网络中非法客户端发起的DNS flood攻击。当设备监测到某服务器受到了DNS flood攻击时，会根据配置的攻击防范处理行为启动相应的防范措施。若防范处理行为配置为对攻击报文进行客户端验证（指定参数为**client-verify**），则设备会将该服务器IP地址添加到受保护IP表项中（可通过**display client-verify dns protected ip**命令查看），对后续新建DNS query请求连接的协商报文进行合法性检查，过滤非法客户端发起的DNS query请求报文。

【举例】

\# 在接口GigabitEthernet1/0/1上使能DNS客户端验证功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 client-verify dns enable

【相关命令】

·**client-verify dns protected ip**

·**display client-verify dns protected ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify http enable**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[client-verify http enable**]命令用来在接口上使能HTTP客户端验证功能。

**[undo client-verify http enable**]命令用来恢复缺省情况。

【命令】

**[client-verify http enable**]

**[undo client-verify http enable**]

【缺省情况】

接口上的HTTP客户端验证功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该功能一般应用在设备连接外部网络的接口上，用来保护内部网络的服务器免受外部网络中非法客户端发起的HTTP flood攻击。当设备监测到某服务器受到了HTTP flood攻击时，会根据配置的攻击防范处理行为启动相应的防范措施。若防范处理行为配置为对攻击报文进行客户端验证（指定参数为**client-verify**），则设备会将该服务器IP地址添加到受保护IP表项中（可通过**display client-verify http protected ip**命令查看），对后续新建HTTP get请求连接的协商报文进行合法性检查，过滤非法客户端发起的HTTP get请求报文。

【举例】

\# 在接口GigabitEthernet1/0/1上使能HTTP客户端验证功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 client-verify http enable

【相关命令】

·**client-verify http protected**** ip**

·**display client-verify ****http protected ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify protected ip**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[client-verify protected ip**]命令用来配置IPv4类型客户端验证的受保护IP地址。

**[undo client-verify protected ip**]命令用来删除指定的受保护IP地址。

【命令】

**[client-verify **[{ **dns** \| **http** \| **tcp** } **protected ip**] *destination-ip-address* [ **vpn-instance** *vpn-instance-name*   **port** *port-number* ]]

**[undo client-verify **[{ **dns** \| **http** \| **tcp** } **protected ip**]* destination-ip-address * **vpn-instance** *vpn-instance-name* ]  **port** *port-number*

【缺省情况】

不存在任何IPv4类型客户端验证受保护IP地址，即客户端验证功能未保护任何IPv4地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

*[destination-ip-address*]：指定受客户端验证保护的IPv4地址，即会对向该目的地址发送的连接请求进行代理。

**[vpn-instance** *vpn-instance-name*]：受客户端验证保护的IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该受保护IP地址属于公网。

**[port ***port-number*]：指定受客户端验证保护的端口号，取值范围为1～65535。若不指定该参数，对于DNS客户端验证的受保护IP，则表示对端口53的DNS query连接请求做代理；对于HTTP客户端验证的受保护IP，则表示对端口80的HTTP GET连接请求做代理；对于TCP客户端验证的受保护IP，则表示对所有端口的TCP连接请求做代理。

【使用指导】

可通过多次执行本命令添加多个IPv4类型客户端验证受保护IP地址。

【举例】

\# 配置一个TCP客户端验证受保护IPv4地址为2.2.2.5、受保护端口号为25。

\<Sysname\> system-view

Sysname client-verify tcp protected ip 2.2.2.5 port 25

\# 配置一个DNS客户端验证受保护IPv4地址为2.2.2.5、受保护端口号为50。

\<Sysname\> system-view

Sysname client-verify dns protected ip 2.2.2.5 port 50

【相关命令】

·**display client-verify protected ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify protected ipv6**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[client-verify protected ipv6**]命令用来配置IPv6类型客户端验证的受保护IP地址。

**[undo client-verify protected ipv6**]命令用来删除指定的受保护IP地址。

【命令】

**[client-verify **[{ **dns** \| **http** \| **tcp** } **protected ipv6** ]*destination-ipv6-address * **vpn-instance** *vpn-instance-name* ]  **port** *port-number*

**[undo client-verify **[{ **dns** \| **http** \| **tcp** } **protected ipv6**] *destination-ipv6-address* [ **vpn-instance** *vpn-instance-name*   **port** *port-number* ]]

【缺省情况】

不存在任何IPv6类型客户端验证受保护IP地址，即客户端验证功能未保护任何IPv6地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

*[destination-ipv6-address*]：指定受客户端验证保护的IPv6地址，即会对向该目的地址发送的连接请求进行代理。对于受TCP客户端验证保护的IPv6地址，发送的是TCP连接请求；对于受DNS客户端验证保护的IPv6地址，发送的是DNS query请求；对于受HTTP客户端验证保护的IPv6地址，发送的是HTTP get连接请求。

**[vpn-instance** *vpn-instance-name*]：受客户端验证保护的IPv6地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该受保护IP地址属于公网。

**[port ***port-number*]：指定受客户端验证保护的端口号，取值范围为1～65535。若不指定该参数，对于DNS客户端验证的受保护IP，则表示对端口53的DNS query连接请求做代理；对于HTTP客户端验证的受保护IP，则表示对端口80的HTTP GET连接请求做代理；对于TCP客户端验证的受保护IP，则表示对所有端口的TCP连接请求做代理。

【使用指导】

可通过多次执行本命令添加多个IPv6类型客户端验证受保护IP地址。

【举例】

\# 配置一个TCP客户端验证受保护IPv6地址为2013::12、受保护端口号为23。

\<Sysname\> system-view

Sysname client-verify tcp protected ipv6 2013::12 port 23

\# 配置一个HTTP客户端验证受保护IPv6地址为2013::12。

\<Sysname\> system-view

Sysname client-verify http protected ipv6 2013::12

【相关命令】

·**display client-verify protected ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- client-verify tcp enable**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[client-verify tcp enable**]命令用来在接口上使能TCP客户端验证功能。

**[undo client-verify tcp enable**]命令用来恢复缺省情况。

【命令】

**[client-verify tcp enable**[ [ **mode** { **syn-cookie** \| **safe-reset** } ]]]

**[undo client-verify tcp enable**]

【缺省情况】

接口上的TCP客户端验证功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mode**]：指定TCP客户端验证的工作模式。不指定该参数时，则表示工作模式为**syn-cookie**。

**[syn-cookie**]：指定TCP客户端验证的工作模式为syn-cookie，即开启TCP客户端验证双向代理。

**[safe-reset**]：指定TCP客户端验证的工作模式为safe-reset，即开启TCP客户端验证单向代理。

【使用指导】

该功能一般应用在设备连接外部网络的接口上，用来保护内部网络的服务器免受外部网络中非法客户端发起的SYN flood、SYN-ACK flood、RST flood、FIN flood、ACK flood攻击。当设备监测到某服务器受到了SYN flood、SYN-ACK flood、RST flood、FIN flood、ACK flood攻击时，会根据配置的攻击防范处理行为启动相应的防范措施。若防范处理行为配置为对攻击报文进行客户端验证（指定参数为**client-verify**），则设备会将该服务器IP地址添加到受保护IP表项中（可通过**display client-verify tcp protected ip**命令查看），并按照指定的单向或双向工作模式，对后续新建TCP连接的协商报文进行合法性检查，过滤非法客户端发起的TCP连接报文。TCP客户端验证功能支持两种代理模式：

·单向代理模式（**safe-reset**）：是指仅对TCP连接的正向报文进行处理。

·双向代理模式（**syn-cookie**）：是指对TCP连接的正向和反向报文都进行处理。

用户可以根据实际的组网情况选择不同的代理模式。若从客户端发出的报文经过使能了TCP客户端验证功能的设备时，而从服务器端发出的报文不经过该设备，此时只能使用单向代理模式；从客户端发出的报文经和从服务器端发出的报文都经过使能了TCP客户端验证功能的设备时，此时可以使用单向代理模式，也可以使用双向代理模式；代理只适合在入接口使能，否则无法建立正常连接。

【举例】

\# 在接口GigabitEthernet1/0/1上使能TCP客户端验证功能，并指定工作模式为双向代理。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 client-verify tcp enable mode syn-cookie

【相关命令】

·**client-verify tcp protected ip**

·**display client-verify tcp protected ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense flood statistics ip**

------------------------------------------------------------------------

**[display attack-defense flood statistics ip**]命令用来显示IPv4 flood攻击防范统计信息。

【命令】

集中式设备：

**[display attack-defense **[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **statistics ip** [ *ip-address* [ **vpn** *vpn-instance-name* ]   **interface** *interface-type interface-number* \| **local** ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense **[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **statistics ip** [ *ip-address* [ **vpn** *vpn-instance-name* ]   **interface** *interface-type interface-number* \| **local** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense **[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **statistics ip** [ *ip-address* [ **vpn** *vpn-instance-name* ]   **interface** *interface-type interface-number* \| **local** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ack-flood**]：显示ACK flood攻击防范统计信息。

**[dns-flood**]：显示DNS flood攻击防范统计信息。

**[fin-flood**]：显示FIN flood攻击防范统计信息。

**[flood**]：显示所有类型的IPv4 flood攻击防范统计信息。

**[http-flood**]：显示HTTP flood攻击防范统计信息。

**[icmp-flood**]：显示ICMP flood攻击防范统计信息。

**[rst-flood**]：显示RST flood攻击防范统计信息。

**[syn-ack-flood**]：显示SYN-ACK flood攻击防范统计信息。

**[syn-flood**]：显示SYN flood攻击防范统计信息。

**[udp-flood**]：显示UDP flood攻击防范统计信息。

*[ip-address*]：显示指定目的IPv4地址的flood攻击防范统计信息。若不指定该参数，则显示指定接口或本机上的所有flood攻击防范统计信息。

**[vpn-instance** *vpn-instance-name*]：指定IPv4地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该IPv4地址属于公网。

**[interface** *interface-type interface-number*]：显示指定接口的flood攻击防范统计信息，*interface-type interface-number*表示接口类型和接口编号[。]

**[local**]：显示本机上进行检测的flood攻击防范统计信息。

**[slot*** slot-number*]：显示指定单板上的flood攻击防范统计信息，*slot-number*表示单板所在槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的flood攻击防范统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的flood攻击防范统计信息，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有成员设备或指定全局接口在所有成员设备上的flood攻击防范统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的flood攻击防范统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有成员设备/PEX或指定全局接口在所有成员设备/PEX上的flood攻击防范统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的flood攻击防范统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的flood攻击防范统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的flood攻击防范统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机所有单板或指定全局接口在所有单板上的flood攻击防范统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的flood攻击防范统计信息，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的被进行flood攻击检测的IPv4地址数目。

【使用指导】

由于flood攻击不关心源地址，因此本命令显示的是对指定目的IPv4地址的攻击防范统计信息。

若不指定**interface**和**local**参数，则显示所有接口以及本机上的flood攻击防范统计信息。

【举例】

\# 显示所有类型的IPv4 flood攻击防范统计信息。（集中式设备）

\<Sysname\> display attack-defense flood statistics ip

IP address      VPN         Detected on  Detect type   State    PPS    Dropped

192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295

201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111

192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222

201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111

192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222

\# 显示所有类型的IPv4 flood攻击防范统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense flood statistics ip

slot 1:

IP address      VPN         Detected on  Detect type   State    PPS    Dropped

192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295

201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111

192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222

201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111

192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222

slot 2:

IP address      VPN         Detected on  Detect type   State    PPS    Dropped

192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295

201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111

192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222

201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111

192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222

\# 显示所有类型的IPv4 flood攻击防范统计信息。（分布式设备－IRF模式）

\<Sysname\> display attack-defense flood statistics ip

Slot 1 in chassis 1:

IP address      VPN         Detected on  Detect type   State    PPS    Dropped

192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295

201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111

192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222

201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111

192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222

slot 2 in chassis 2:

IP address      VPN         Detected on  Detect type   State    PPS    Dropped

192.168.100.221 a0123456789 GE1/0/2      SYN-ACK-FLOOD Normal   1000   4294967295

201.55.7.45     asd         GE1/0/2      SYN-ACK-FLOOD Normal   1000   111111111

192.168.11.5    \--          GE1/0/3      ACK-FLOOD     Normal   1000   222222222

201.55.7.44     \--          GE1/0/4      DNS-FLOOD     Normal   1000   111111111

192.168.11.4    \--          GE1/0/5      ACK-FLOOD     Normal   1000   22222222

\# 显示所有类型的flood攻击检测的IPv4地址数目。（集中式设备）

\<Sysname\> display attack-defense flood statistics ip count

Totally 2 flood entries.

\# 显示所有类型的flood攻击检测的IPv4地址数目。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense flood statistics ip count

Slot 1:

Totally 2 flood entries.

Slot 2:

Totally 2 flood entries.

\# 显示所有类型的flood攻击检测的IPv4地址数目。（分布式设备－IRF模式）

\<Sysname\> display attack-defense flood statistics ip count

Slot 1 in chassis 1:

Totally 2 flood entries.

Slot 2 in chassis 2:

Totally 2 flood entries.

\# 显示所有类型的flood攻击检测的IPv4地址数目。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense flood statistics ip count

CPU 0 on slot 1:

Totally 2 flood entries.

CPU 1 on slot 2:

Totally 2 flood entries.

\# 显示所有类型的flood攻击检测的IPv4地址数目。（分布式设备－IRF模式）

\<Sysname\> display attack-defense flood statistics ip count

CPU 0 on slot 1 in chassis 1:

Totally 2 flood entries.

CPU 1 on slot 2 in chassis 2:

Totally 2 flood entries.

表1-1 display attack-defense flood statistics ip命令显示信息描述表

字段

描述

IP address

被检测的目的IPv4地址

VPN

目的IPv4地址所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

Detected on

进行攻击检测的位置，包括接口和本机（Local）

Detect type

检测的flood攻击类型

State

接口或本机是否处于攻击状态，可包括以下取值：

·Attacked：受攻击状态

·Normal：正常状态（当前并未受到攻击）

PPS

指定的目的Pv4地址收到flood攻击报文的速率（单位为报文每秒）

Dropped

接口或本机丢弃的flood攻击报文数目

Totally 2 flood entries

被检测的IPv4地址数目

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense flood statistics ipv6**

------------------------------------------------------------------------

**[display attack-defense flood statistics ipv6**]命令用来显示IPv6 flood攻击防范统计信息。

【命令】

集中式设备：

**[display attack-defense **[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-flood** \| **syn-ack-flood** \| **udp-flood** } **statistics ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name* ]   **interface** *interface-type interface-number* \| **local** ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense **[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-flood** \| **syn-ack-flood** \| **udp-flood** } **statistics ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name* ]   **interface** *interface-type interface-number \|* **local** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense **[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-flood** \| **syn-ack-flood** \| **udp-flood** } **statistics ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name* ]   **interface** *interface-type interface-number \|* **local** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ack-flood**]：显示指定ACK flood类型统计信息。

**[dns-flood**]：显示指定DNS flood类型统计信息。

**[fin-flood**]：显示指定FIN flood类型统计信息。

**[flood**]：显示所有类型的IPv6 flood攻击防范统计信息。

**[http-flood**]：显示HTTP flood攻击防范统计信息。

**[icmpv6-flood**]：显示指定ICMPv6 flood类型统计信息。

**[rst-flood**]：显示指定RST flood类型统计信息。

**[syn-flood**]：显示指定SYN flood类型统计信息。

**[syn-ack-flood**]：显示SYN-ACK flood攻击防范统计信息。

**[udp-flood**]：显示指定UDP flood类型统计信息。

*[ipv6-address*]：显示指定目的IPv6地址的flood攻击防范统计信息。若不指定该参数，则显示指定接口或本机上的所有flood攻击防范统计信息。

**[vpn** *vpn-instance-name*]：指定IPv6地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该IPv6地址属于公网。

**[interface** *interface-type interface-number*]：显示指定接口的flood攻击防范统计信息，*interface-type interface-number*表示接口类型和接口编号[。]

**[local**]：显示本机上进行检测的flood攻击防范统计信息。

**[slot*** slot-number*]：显示指定单板上的flood攻击防范统计信息，*slot-number*表示单板所在槽位号。该参数仅在指定本机或指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的flood攻击防范统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的flood攻击防范统计信息，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有成员设备或指定全局接口在所有成员设备上的flood攻击防范统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的flood攻击防范统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有成员设备/PEX或指定全局接口在所有成员设备/PEX上的flood攻击防范统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的flood攻击防范统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的flood攻击防范统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的flood攻击防范统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板所在的槽位号或PEX所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。若不指定该参数，则表示显示本机上所有单板或指定全局接口在所有单板上的flood攻击防范统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的flood攻击防范统计信息，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：仅显示符合指定条件的被进行flood攻击检测的IPv6地址数目。

【使用指导】

由于flood攻击不关心源地址，因此本命令显示的是对指定目的IPv6地址的攻击防范统计信息。

若不指定**interface**和**local**参数，则显示所有接口以及本机上的flood攻击防范统计信息。

【举例】

\# 显示所有类型的IPv6 flood攻击防范统计信息。（集中式设备）

\<Sysname\> display attack-defense flood statistics ipv6

IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped

2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295

1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111

1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222

1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111

1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222

\# 显示所有类型的IPv6 flood攻击防范统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense flood statistics ipv6

Slot 1:

IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped

2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295

1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111

1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222

1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111

1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222

Slot 2:

IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped

2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295

1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111

1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222

1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111

1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222

\# 显示所有类型的IPv6 flood攻击防范统计信息。（分布式设备－IRF模式）

\<Sysname\> display attack-defense flood statistics ipv6

Slot 1 in chassis 1:

IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped

2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295

1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111

1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222

1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111

1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222

Slot 2 in chassis 2:

IPv6 address    VPN         Detected on  Detect type   State    PPS    Dropped

2000::1011      a0123456789 GE1/0/2      SYN-FLOOD     Normal   0      4294967295

1::2            1222232     GE1/0/2      DNS-FLOOD     Normal   1000   111111111

1::3            \--          GE1/0/3      SYN-ACK-FLOOD Normal   1000   222222222

1::4            \--          GE1/0/4      ACK-FLOOD     Normal   1000   111111111

1::5            \--          GE1/0/5      SYN-FLOOD     Normal   1000   22222222

\# 显示所有类型的flood攻击检测的IPv6地址数目。（集中式设备）

\<Sysname\> display attack-defense flood statistics ipv6 count

Totally 5 flood entries.

\# 显示所有类型的flood攻击检测的IPv6地址数目。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense flood statistics ipv6 count

Slot 1:

Totally 5 flood entries.

Slot 2:

Totally 5 flood entries.

\# 显示所有类型的flood攻击检测的IPv6地址数目。（分布式设备－IRF模式）

\<Sysname\> display attack-defense flood statistics ipv6 count

Slot 1 in chassis 1:

Totaly 5 flood entries.

Slot 2 in chassis 2:

Totally 5 flood entries.

表1-2 display attack-defense flood statistics ipv6命令显示信息描述表

字段

描述

IPv6 address

被检测的目的IPv6地址

VPN

目的IPv6地址所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

Detected on

进行攻击检测的位置，包括接口和本机（Local）

Detect type

检测的flood攻击类型

State

接口或本机是否处于攻击状态，可包括以下取值：

·Attacked：受攻击状态

·Normal：正常状态（当前并未受到攻击）

PPS

指定的目的IPv6地址收到报文的速率（单位为报文每秒）

Dropped

接口或本机丢弃的flood攻击报文数目

Totally 2 flood entries

被检测的IPv6地址数目

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense policy**

------------------------------------------------------------------------

**[display attack-defense policy**]用来显示攻击防范策略的配置信息。

【命令】

**[display attack-defense policy ** *policy-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。若不指定该参数，则表示显示所有攻击防范策略的摘要信息。

【使用指导】

本命令显示的内容主要包括各类型攻击防范的使能情况、对攻击报文的处理方式和相关的阈值参数。

【举例】

\# 显示攻击防范策略abc的配置信息。

\<Sysname\> display attack-defense policy abc

          Attack-defense Policy Information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Policy name                        : abc

Applied list                       : GE1/0/1

                                     Vlan-int1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Exempt IPv4 ACL：                  : Not configured

Exempt IPv6 ACL：                  : vip

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Actions: CV-Client verify  BS-Block source  L-Logging  D-Drop  N-None

Signature attack defense configuration:

Signature name                     Defense      Level             Actions

Fragment                           Enabled      Info              L

Impossible                         Enabled      Info              L

Teardrop                           Disabled     Info              L

Tiny fragment                      Disabled     Info              L

IP option abnormal                 Disabled     Info              L

Smurf                              Disabled     Info              N

Traceroute                         Disabled     Medium            L,D

Ping of death                      Disabled     Low               L

Large ICMP                         Disabled     Medium            L,D

  Max length                       4000 bytes

Large ICMPv6                       Disabled     Low               L

  Max length                       4000 bytes

TCP invalid flags                  Disabled     medium            L,D

TCP null flag                      Disabled     Low               L

TCP all flags                      Enabled      Info              L

TCP SYN-FIN flags                  Disabled     Info              L

TCP FIN only flag                  Enabled      Info              L

TCP Land                           Disabled     Info              L

Winnuke                            Disabled     Info              L

UDP Bomb                           Disabled     Info              L

UDP Snork                          Disabled     Info              L

UDP Fraggle                        Enabled      Info              L

IP option record route             Disabled     Info              L

IP option internet timestamp       Enabled      Info              L

IP option security                 Disabled     Info              L

IP option loose source routing     Enabled      Info              L

IP option stream ID                Disabled     Info              L

IP option strict source routing    Disabled     Info              L

IP option route alert              Disabled     Info              L

ICMP echo request                  Disabled     Info              L

ICMP echo reply                    Disabled     Info              L

ICMP source quench                 Disabled     Info              L

ICMP destination unreachable       Enabled      Info              L

ICMP redirect                      Enabled      Info              L

ICMP time exceeded                 Enabled      Info              L

ICMP parameter problem             Disabled     Info              L

ICMP timestamp request             Disabled     Info              L

ICMP timestamp reply               Disabled     Info              L

ICMP information request           Disabled     Info              L

ICMP information reply             Disabled     Medium            L,D

ICMP address mask request          Disabled     Medium            L,D

ICMP address mask reply            Disabled     Medium            L,D

ICMPv6 echo request                Enabled      Medium            L,D

ICMPv6 echo reply                  Disabled     Medium            L,D

ICMPv6 group membership query      Disabled     Medium            L,D

ICMPv6 group membership report     Disabled     Medium            L,D

ICMPv6 group membership reduction  Disabled     Medium            L,D

ICMPv6 destination unreachable     Enabled      Medium            L,D

ICMPv6 time exceeded               Enabled      Medium            L,D

ICMPv6 parameter problem           Disabled     Medium            L,D

ICMPv6 packet too big              Disabled     Medium            L,D

Scan attack defense configuration:

 Defense: Disabled

 Level: Medium

 Actions: L

Flood attack defense configuration:

Flood type      Global thres(pps)  Global actions  Service ports   Non-specific

SYN flood       1000(default)      -               -               Disabled

ACK flood       1000(default)      -               -               Enabled

SYN-ACK flood   1000(default)      -               -               Disabled

RST flood       200                -               -               Enabled

FIN flood       1000(default)      L,D             -               Disabled

UDP flood       1000(default)      -               -               Disabled

ICMP flood      1000(default)      -               -               Disabled

ICMPv6 flood    1000(default)      CV              -               Disabled

DNS flood       10000              -               30,61 to 62     Enabled

HTTP flood      10000              -               80,8080         Enabled

Flood attack defense for protected IP addresses:

 Address                 VPN instance Flood type    Thres(pps)  Actions Ports

 1::1                    \--           FIN-FLOOD     10          L,D     -

 192.168.1.1             A01234567890 SYN-ACK-FLOOD 10          -       -

                         123456789012   

                         3456789

 1::1                    \--           FIN-FLOOD     -           L       -

 2013:2013:2013:2013:    A0123456789  DNS-FLOOD     100         L,CV    53

 2013:2013:2013:2013

表1-3 display attack-defense policy命令显示信息描述表

字段

描述

Policy name

攻击防范策略名称

Applied list

攻击防范策略应用的对象列表，包括接口名称和本机（Local）

Exempt IPv4 ACL

IPv4例外列表

Exempt IPv6 ACL

IPv6例外列表

Actions

攻击防范的处理行为，包括以下取值：

·CV：启用客户端验证

·BS：添加黑名单（老化时间，单位为分钟）

·L：输出告警日志

·D：丢弃报文

·N：不采用任何处理行为

Signature attack defense configuration

单包攻击防范配置信息

Signature name

单包的类型

Defense

单包攻击防范的开启状态

Level

单包攻击的级别，包括以下取值：

·Info：提示级别

·low：低级别

·medium：中级别

·high：高级别（目前暂无实例）

Actions

单包攻击防范的处理行为，包括以下取值：

·L：输出告警日志

·D：丢弃报文

·N：不采用任何处理行为

IP option record  route

IP 选项record route攻击

IP option security

IP 选项security攻击

IP option stream ID

IP 选项stream identifier攻击

IP option internet timestamp

IP 选项 internet timestamp攻击

IP option loose source routing

IP 选项loose source routing攻击

IP option strict source routing

IP 选项strict source routing攻击

IP option abnormal

IP 选项异常攻击

IP option route alert

IP 选项route alert攻击

Fragment

IP分片异常攻击

IP impossible

IP impossible攻击

Tiny fragment

IP tiny fragment攻击

Teardrop

IP teardrop攻击，又称IP overlapping fragments

Large ICMP

Large ICMP攻击

Max length

ICMP报文所允许的最大长度

Smurf

Smurf攻击

Traceroute

Traceroute攻击

Ping of death

Ping of death攻击

ICMP echo request

ICMP echo request攻击

ICMP echo reply

ICMP echo reply攻击

ICMP source quench

ICMP source quench攻击

ICMP redirect

ICMP redirect攻击

ICMP parameter problem

ICMP parameter problem攻击

ICMP timestamp request

ICMP timestamp request攻击

ICMP timestamp reply

ICMP timestamp reply攻击

ICMP information request

ICMP information request攻击

ICMP information reply

ICMP information reply攻击

ICMP address mask request

ICMP address mask request攻击

ICMP address mask reply

ICMP address mask reply攻击

ICMP destination unreachable

ICMP destination  unreachable攻击

ICMP time exceeded

ICMP time exceeded攻击

Large ICMPv6

Large ICMPv6攻击

ICMPv6 echo request

ICMPv6 echo request攻击

ICMPv6 echo reply

ICMPv6 echo reply攻击

ICMPv6 group membership query

ICMPv6 group membership query攻击

ICMPv6 group membership report

ICMPv6 group membership report攻击

ICMPv6 group membership reduction

ICMPv6 group membership reduction攻击

ICMPv6 destination unreachable

ICMPv6 destination unreachable攻击

ICMPv6 time exceeded

ICMPv6 time exceeded攻击

ICMPv6 parameter problem

ICMPv6 parameter problem攻击

ICMPv6 packet too big

ICMPv6 packet too big攻击

Winnuke

Winnuke攻击

TCP Land

Land攻击

TCP NULL flag

TCP NULL flag攻击

TCP invalid flags

TCP invalid flags攻击

TCP all flags

TCP所有标志位均被置位攻击，又称圣诞树攻击

TCP SYN-FIN flags

TCP SYN和FIN被同时置位攻击

TCP FIN only flag

TCP 只有FIN被置位的攻击

Fraggle

Fraggle攻击，又称UDP chargen DoS attack

UDP Bomb

UDP Bomb攻击

Snork

Snork攻击

Scan attack defense configuration

扫描攻击防范配置信息

Defense

扫描攻击防范的开启状态

Level

扫描攻击的级别，包括以下取值：

·low：低级别

·medium：中级别

·high：高级别

Actions

扫描攻击防范的处理行为，包括以下取值：

·BS：添加黑名单（老化时间，单位为分钟）

·D：丢弃报文

·L：输出告警日志

Flood attack defense configuration

flood攻击防范配置信息

Flood type

flood攻击类型，包括以下取值：

·ACK flood

·DNS flood

·FIN flood

·ICMP flood

·ICMPv6 flood

·SYN flood

·SYN-ACK flood

·UDP flood

·RST flood

·HTTP flood

Global thres(pps)

flood攻击防范的全局触发阈值，单位为每秒报文数，默认值为1000pps

Global actions

flood攻击防范的全局处理行为，包括以下取值：

·D：丢弃报文

·L：输出告警日志，

·CV：启用客户端验证

·-：未配置

Service ports

flood攻击防范的全局检测端口号。该字段只对DNS flood攻击防范和HTTP flood攻击防范生效，对于其它flood攻击防范，显示为"[-"]

Non-specific

对非受保护IP地址开启SYN flood攻击防范检测的状态

Flood attack defense for protected IP addresses

对受保护IP地址的flood攻击防范配置

Address

指定的IP地址

VPN instance

所属的VPN实例名称，未配置时显示为"[\--"]

Thres(pps)

攻击防范检测的触发阈值，单位为报文每秒，未配置时显示为"-"

Actions

对指定IP地址采用的攻击防范处理行为，包括 取值：

·CV：启用客户端验证

·BS：添加黑名单

·L：输出告警日志

·D：丢弃报文

·N：不采用任何处理行为

Ports

Flood攻击防范的检测端口号。该字段只对DNS flood攻击防范和HTTP flood攻击防范生效，对于其他攻击防范，显示为"-"

\# 显示所有攻击防范策略的概要配置信息。

\<Sysname\> display attack-defense policy

           Attack-defense Policy Brief Information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Policy Name                        Applied list

Atk-policy-1                       GigabitEthernet1/0/1

                                   GigabitEthernet1/0/2

                                   GigabitEthernet1/0/3

P2                                 None

P123                               GigabitEthernet1/0/2

表1-4 表1-2 display attack-defense policy命令显示信息描述表

字段

描述

Policy Name

攻击防范策略编号

Applied list

攻击防范策略应用的对象列表，包括接口名称和本机（Local）

【相关命令】

·**attack-defense policy**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense policy ip**

------------------------------------------------------------------------

**[display attack-defense policy ip**]命令用来显示flood攻击防范的IPv4类型的受保护IP表项。

【命令】

集中式设备：

**[display attack-defense policy*** policy-name*****[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ip** [ *ip-address* [ **vpn** *vpn-instance-name* ] ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense policy*** policy-name*****[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ip** [ *ip-address* [ **vpn** *vpn-instance-name* ] ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense policy*** policy-name*****[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmp-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ip** [ *ip-address* [ **vpn** *vpn-instance-name* ] ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"\_"和"-"。

**[ack-flood**]：显示ACK flood攻击防范受保护IP表项。

**[dns-flood**]：显示DNS flood攻击防范受保护IP表项。

**[fin-flood**]：显示FIN flood攻击防范受保护IP表项。

**[flood**]：显示所有类型的flood攻击防范受保护IP表项。

**[http-flood**]：显示HTTP flood攻击防范受保护IP表项。

**[icmp-flood**]：显示ICMP flood攻击防范受保护IP表项。

**[rst-flood**]：显示RST flood攻击防范受保护IP表项。

**[syn-ack-flood**]：显示SYN-ACK flood攻击防范受保护IP表项。

**[syn-flood**]：显示SYN flood攻击防范受保护IP表项。

**[udp-flood**]：显示UDP flood攻击防范受保护IP表项。

**[ip ***ip-address*]：显示指定IPv4地址的受保护IP表项。若不指定*ip-address*参数，则表示显示符合指定条件的所有受保护IP表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的受保护IP表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示显示指公网的受保护IP表项。

**[slot** *slot-number*]：显示指定单板上的受保护IP表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的受保护IP表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的受保护IP表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板所在的槽位号或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的受保护IP表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的flood受保护IP表项的数目。

【举例】

\# 显示攻击防范策略abc中所有flood攻击防范的IPv4类型受保护IP表项的信息。（集中式设备）

\<Sysname\> display attack-defense policy abc flood ip

IP address      VPN instance     Type          Rate threshold(PPS) Dropped

123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295

201.55.7.45     \--               ICMP-FLOOD    100                 10

192.168.11.5    \--               DNS-FLOOD     23                  100

\# 显示攻击防范策略abc中所有flood攻击防范的IPv4类型受保护IP表项的信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense policy abc flood ip

Slot 1:

IP address      VPN instance     Type          Rate threshold(PPS) Dropped

123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295

201.55.7.45     \--               ICMP-FLOOD    100                 10

192.168.11.5    \--               DNS-FLOOD     23                  100

Slot 2：

IP address      VPN instance     Type          Rate threshold(PPS) Dropped

123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295

201.55.7.45     \--               ICMP-FLOOD    100                 10

192.168.11.5    \--               DNS-FLOOD     23                  100

\# 显示攻击防范策略abc中所有flood攻击防范的IPv4类型受保护IP表项的信息。（分布式设备－IRF模式）

\<Sysname\> display attack-defense policy abc flood ip

Slot 1 in chassis 0:

IP address      VPN instance     Type          Rate threshold(PPS) Dropped

123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295

201.55.7.45     \--               ICMP-FLOOD    100                 10

192.168.11.5    \--               DNS-FLOOD     23                  100

Slot 2 in chassis 1:

IP address      VPN instance     Type          Rate threshold(PPS) Dropped

123.123.123.123 a012345678901234 SYN-ACK-FLOOD 100                 4294967295

201.55.7.45     \--               ICMP-FLOOD    100                 10

192.168.11.5    \--               DNS-FLOOD     23                  100

\# 显示攻击防范策略abc中所有flood攻击防范的IPv4类型受保护IP表项的个数。（集中式设备）

\<Sysname\> display attack-defense policy abc flood ip count

Totally 3 flood protected IP addresses.

\# 显示攻击防范策略abc中所有IPv4类型flood受保护IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense policy abc flood ip count

Slot 1:

Totally 3 flood protected IP addresses.

Slot 2：

Totally 3 flood protected entries.

\# 显示攻击防范策略abc中所有IPv4类型flood受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display attack-defense policy abc flood ip count

Slot 1 in chassis 0:

Totally 3 flood protected IP addresses.

Slot 2 in chassis 1:

Totally 3 flood protected IP addresses.

表1-5 display attack-defense flood ip命令显示信息描述表

字段

描述

Totally 3 flood protected IP addresses

IPv4类型受保护IP表项数目

IP address

受保护的IPv4地址

VPN instance

受保护的IPv4地址所属的MPLS L3VPN实例名称，未指定时显示为"[\--"]

Type

flood攻击类型

Rate threshold(PPS)

配置的flood攻击防范触发阈值（单位为报文每秒）

Dropped

检测到flood攻击后的丢包数，若只输出日志该项显示为0

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense policy ipv6**

------------------------------------------------------------------------

**[display attack-defense** **policy ipv6**]命令用来显示flood攻击防范的IPv6类型的受保护IP表项。

【命令】

集中式设备：

**[display attack-defense policy*** policy-name*****[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name* ] ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense policy*** policy-name*****[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name* ] ]  **slot** *slot-number* [ **cpu** *cpu-number*  ] ]  **count** ]

分布式设备－IRF模式：

**[display attack-defense policy*** policy-name*****[{ **ack-flood** \| **dns-flood** \| **fin-flood** \| **flood** \| **http-flood** \| **icmpv6-flood** \| **rst-flood** \| **syn-ack-flood** \| **syn-flood** \| **udp-flood** } **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name* ] ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"\_"和"-"。

**[ack-flood**]：显示ACK flood攻击防范受保护IP表项。

**[dns-flood**]：显示DNS flood攻击防范受保护IP表项。

**[fin-flood**]：显示FIN flood攻击防范受保护IP表项。

**[flood**]：显示所有类型的flood攻击防范受保护IP表项。

**[http-flood**]：显示HTTP flood攻击防范受保护IP表项。

**[icmpv6-flood**]：显示ICMPv6 flood攻击防范受保护IP表项。

**[rst-flood**]：显示RST flood攻击防范受保护IP表项。

**[syn-ack-flood**]：显示SYN-ACK flood攻击防范受保护IP表项。

**[syn-flood**]：显示SYN flood攻击防范受保护IP表项。

**[udp-flood**]：显示UDP flood攻击防范受保护IP表项。

**[ipv6 ***ipv6-address*]：显示指定IPv6地址的受保护IP表项。若不指定*ipv6-address*参数，则表示显示符合指定条件的所有IPv6类型的受保护IP表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的受保护IP表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[slot** *slot-number*]：显示指定单板上的受保护IP表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的黑名单表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的黑名单表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的黑名单表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的受保护IP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板所在的槽位号或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的受保护IP表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的flood受保护IP表项的数目。

【举例】

\# 显示攻击防范策略abc中所有flood攻击防范的IPv6类型受保护IP表项。（集中式设备）

\<Sysname\> display attack-defense policy abc flood ipv6

IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped

2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295

2::5            \--               ACK-FLOOD     100                 10

1::5            \--               ACK-FLOOD     100                 23

\# 显示攻击防范策略abc中所有flood攻击防范的IPv6类型受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense policy abc flood ipv6

Slot 1:

IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped

2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295

2::5            \--               ACK-FLOOD     100                 10

1::5            \--               ACK-FLOOD     100                 23

Slot 2:

IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped

2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295

2::5            \--               ACK-FLOOD     100                 10

1::5            \--               ACK-FLOOD     100                 23

\# 显示攻击防范策略abc中所有flood攻击防范的IPv6类型受保护IP表项。（分布式设备－IRF模式）

\<Sysname\> display attack-defense policy abc flood ipv6

Slot 1 in chassis 0:

IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped

2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295

2::5            \--               ACK-FLOOD     100                 10

1::5            \--               ACK-FLOOD     100                 23

Slot 2 in chassis 1:

IPv6 address    VPN instance     Type          Rate threshold(PPS) Dropped

2013::127f      a012345678901234 SYN-ACK-FLOOD 100                 4294967295

2::5            \--               ACK-FLOOD     100                 10

1::5            \--               ACK-FLOOD     100                 23

\# 显示攻击防范策略abc中所有flood攻击防范的IPv6类型受保护IP表项的个数。（集中式设备）

\<Sysname\> display attack-defense flood ipv6 count

Totally 3 flood protected entries.

\# 显示攻击防范策略abc中所有flood攻击防范的IPv6类型受保护IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense policy abc flood ipv6 count

Slot 1:

Totally 3 flood protected IP addresses.

Slot 2:

Totally 3 flood protected IP addresses.

\# 显示攻击防范策略abc中所有flood攻击防范的IPv6类型受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display attack-defense policy abc flood ipv6 count

Slot 1 in chassis 0:

Totally 3 flood protected IP addresses.

Slot 2 in chassis 1:

Totally 3 flood protected IP addresses.

表1-6 display flood ipv6命令显示信息描述表

字段

描述

Totally3 flood protected IP addresses

IPv6类型受保护IP表项数目

IPv6 address

受保护的IPv6地址

VPN instance

受保护的IPv6地址所属的MPLS L3VPN实例名称，未指定时显示为"[\--"]

Type

flood攻击类型

Rate threshold(PPS)

配置的flood攻击防范触发阈值（单位为报文每秒）

Dropped

检测到flood攻击后的丢包数，若只输出日志该项显示为0

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan attacker ip**

------------------------------------------------------------------------

**[display attack-defense scan attacker ip**]命令用来显示扫描攻击者的IPv4地址表项。

【命令】

集中式设备：

**[display attack-defense scan attacker ip**[ [ **interface** *interface-type interface-number* \| **local** ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense scan attacker ip**[ [ **interface** *interface-type interface-number* \| **local** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense scan attacker ip**[ [ **interface** *interface-type interface-number* \| **local** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口上检测到的扫描攻击者的IPv4地址表项，*interface-type interface-number*表示接口类型和接口编号[。]

**[local**]：显示本机检测到的扫描攻击者IPv4地址表项。

**[slot** *slot-number*]：显示指定单板上的扫描攻击者的IPv4地址表项，*slot-number*表示单板所在槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示所有单板上的扫描攻击者的IPv4地址表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的扫描攻击者的IPv4地址表项，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备上的扫描攻击者的IPv4地址表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的扫描攻击者的IPv4地址表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备/PEX上的扫描攻击者的IPv4地址表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的扫描攻击者的IPv4地址表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的IPv4地址表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的扫描攻击者的IPv4地址表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的IPv4地址表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的扫描攻击者的IPv4地址表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的当前扫描攻击者的IPv4地址表项数目。

【使用指导】

若不指定任何参数，则表示显示所有扫描攻击者的IPv4地址表项。

【举例】

\# 显示所有扫描攻击者的IPv4地址表项。（集中式设备）

\<Sysname\> display attack-defense scan attacker ip

IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)

192.168.31.2    \--               \--                   GE1/0/2      1284

2.2.2.3         \--               \--                   GE1/0/2      23

\# 显示所有扫描攻击者的IPv4地址表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan attacker ip

Slot 1:

IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)

192.168.31.2    \--               \--                   GE1/0/2      1284

2.2.2.3         \--               \--                   GE1/0/2      23

Slot 2：

IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)

192.168.31.2    \--               \--                   GE1/0/2      1284

2.2.2.3         \--               \--                   GE1/0/2      23

\# 显示所有扫描攻击者的IPv4地址表项。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan attacker ip

Slot 1 in chassis 0:

IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)

192.168.31.2    \--               \--                   GE1/0/2      1284

2.2.2.3         \--               \--                   GE1/0/2      23

Slot 2 in chassis 1:

IP address      VPN instance     DS-Lite tunnel peer  Detected on  Duration(min)

192.168.31.2    \--               \--                   GE1/0/2      1284

2.2.2.3         \--               \--                   GE1/0/2      23

\# 显示所有扫描攻击者的IPv4地址表项的个数。（集中式设备）

\<Sysname\> display attack-defense scan attacker ip count

Totally 3 attackers.

\# 显示所有扫描攻击者的IPv4地址表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan attacker ip count

Slot 1:

Totally 3 attackers.

Slot 2:

Totally 3 attackers.

\# 显示所有扫描攻击者的IPv4地址表项的个数。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan attacker ip count

Slot 1 in chassis 0:

Totally 3 attackers.

Slot 2 in chassis 1:

Totally 3 attackers.

表1-7 display attack-defense scan attacker ip命令显示信息描述表

字段

描述

Total 3 attackers

扫描攻击者的数目

IP address

发起攻击的IPv4地址

VPN instance

所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

DS-Lite tunnel peer

DS-Lite隧道对端地址。DS-Lite组网下，若本设备为AFTR，此列表示报文来自具体的哪个B4，如果不在DS-Lite组网或本设备不为AFTR，则该字段无意义，显示为"\--"

Detected on

进行攻击检测的位置，包括接口或本机（Local）

Duration(min)

检测到攻击持续的时间，单位为分钟

【相关命令】

·**display attack-defense scan victim ip**

·**scan detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan attacker ipv6**

------------------------------------------------------------------------

**[display attack-defense scan attacker ipv6**]命令用来显示扫描攻击者的IPv6地址表项。

【命令】

集中式设备：

**[display attack-defense scan attacker ipv6**[ [ **interface** *interface-type interface-number* \| **local** ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense scan attacker ipv6**[ [ **interface** *interface-type interface-number* \| **local** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense scan attacker ipv6**[ [ **interface** *interface-type interface-number* \| **local** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的扫描攻击者的IPv6地址表项，*interface-type interface-number*表示接口类型和接口编号[。]

**[local**]：显示本机检测到的扫描攻击者IPv6地址表项。

**[slot*** slot-number*]：显示指定单板上的扫描攻击者的IPv6地址表项，*slot-number*表示单板所在槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的IPv6地址表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的扫描攻击者的IPv6地址表项，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备上的扫描攻击者的IPv6地址表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的扫描攻击者的IPv6地址表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备/PEX上的扫描攻击者的IPv6地址表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的扫描攻击者的IPv6地址表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的IPv6地址表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的扫描攻击者的IPv6地址表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的扫描攻击者的IPv6地址表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的扫描攻击者的IPv6地址表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的当前扫描攻击者的IPv6地址表项数目。

【使用指导】

若不指定任何参数，则表示显示所有扫描攻击者的IPv6地址表项。

【举例】

\# 显示扫描攻击者的IPv6地址表项。（集中式设备）

\<Sysname\> display attack-defense scan attacker ipv6

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  1234

1230::22                 \--               GE1/0/4                  10

\# 显示扫描攻击者的IPv6地址表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan attacker ipv6

Slot 1:

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  1234

1230::22                 \--               GE1/0/4                  10

Slot 2：

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  1234

1230::22                 \--               GE1/0/4                  10

\# 显示所有扫描攻击者的IPv6地址表项。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan attacker ipv6

Slot 1 in chassis 0:

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  1234

1230::22                 \--               GE1/0/4                  10

Slot 2 in chassis 1:

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  1234

1230::22                 \--               GE1/0/4                  10

\# 显示扫描攻击者的IPv6地址表项的个数。（集中式设备）

\<Sysname\> display attack-defense scan attacker ipv6 count

Totally 3 attackers.

\# 显示扫描攻击者的IPv6地址表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan attacker ipv6 count

Slot 1:

Totally 3 attackers.

Slot 2：

Totally 3 attackers.

\# 显示所有扫描攻击者的IPv6地址表项的个数。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan attacker ipv6 count

Slot 1 in chassis 0:

Totally 3 attackers.

Slot 2 in chassis 1:

Totally 3 attackers.

表1-8 display attack-defense scan attacker ipv6命令显示信息描述表

字段

描述

Totally 3 attackers

攻击者的数目

IPv6 address

发起攻击的IPv6地址

VPN instance

所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

Detected on

进行攻击检测的位置，包括接口或本机（Local）

Duration(min)

检测到攻击持续的时间，单位为分钟

【相关命令】

·**display attack-defense scan victim ipv6**

·**scan detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan victim ip**

------------------------------------------------------------------------

**[display attack-defense scan victim ip**]命令用来显示扫描攻击被攻击者的IPv4地址表项。

【命令】

集中式设备：

**[display attack-defense scan victim ip**[ [ **interface** *interface-type interface-number* \| **local** ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense scan victim ip**[ [ **interface** *interface-type interface-number* \| **local** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense scan victim ip**[ [ **interface** *interface-type interface-number* \| **local** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的被攻击者的IPv4地址表项，*interface-type interface-number*表示接口类型和接口编号[。]

**[local**]：显示本机检测到的被攻击者的IPv4地址表项。

**[slot** *slot-number*]：显示指定单板上的被攻击者的IPv4地址表项，*slot-number*表示单板所在槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的IPv4地址表项。（分布式设备－独立运行模式）

**[slot** slot-number]：显示指定成员设备上的被攻击者的IPv4地址表项，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备上的被攻击者的IPv4地址表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** slot-number]：显示指定成员设备/PEX上的被攻击者的IPv4地址表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备/PEX上的被攻击者的IPv4地址表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的被攻击者的IPv4地址表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的IPv4地址表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的被攻击者的IPv4地址表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的IPv4地址表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上被攻击者的IPv4地址表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的被攻击者的IPv4地址表项数目。

【使用指导】

若不指定任何参数，则表示显示所有扫描攻击的被攻击者的IPv4地址表项。

【举例】

\# 显示扫描攻击的被攻击者的IPv4地址表项。（集中式设备）

\<Sysname\> display attack-defense scan victim ip

IP address      VPN instance                    Detected on        Duration(min)

192.168.31.2    \--                              GE1/0/4            21

2.2.2.3         \--                              GE1/0/4            1234

\# 显示扫描攻击的被攻击者的IPv4地址表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan victim ip

Slot 1:

IP address      VPN instance                    Detected on        Duration(min)

192.168.31.2    \--                              GE1/0/4            21

2.2.2.3         \--                              GE1/0/4            1234

Slot 2:

IP address      VPN instance                    Detected on        Duration(min)

192.168.31.2    \--                              GE1/0/4            21

2.2.2.3         \--                              GE1/0/4            1234

\# 显示扫描攻击的被攻击者的IPv4地址表项。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan victim ip

Slot 1 in chassis 0:

IP address      VPN instance                    Detected on        Duration(min)

192.168.31.2    \--                              GE1/0/4            21

2.2.2.3         \--                              GE1/0/4            1234

Slot 2 in chassis 1:

IP address      VPN instance                    Detected on        Duration(min)

192.168.31.2    \--                              GE1/0/4            21

2.2.2.3         \--                              GE1/0/4            1234

\# 显示扫描攻击的被攻击者的IPv4地址表项。（集中式设备）

\<Sysname\> display attack-defense scan victim ip count

Totally 3 victim IP addresses.

\# 显示扫描攻击的被攻击者的IPv4地址表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan victim ip count

Slot 1:

Totally 3 victim IP addresses.

Slot 2:

Totally 3 victim IP addresses.

\# 显示扫描攻击的被攻击者的IPv4地址表项的个数。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan victim ip count

Slot 1 in chassis 0:

Totally 3 victim IP addresses.

Slot 2 in chassis 1:

Totally 3 victim IP addresses.

表1-9 display attack-defense scan victim ip命令显示信息描述表

字段

描述

Totally 3 victim IP addresses

被攻击者的数目

IP address

被攻击的IPv4地址

VPN instance

所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

Detected on

进行攻击检测的位置，包括接口或本机（Local）

Duration(min)

检测到被攻击的持续时间，单位为分钟

【相关命令】

·**display attack-defense scan attacker ip**

·**scan detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense scan victim ipv6**

------------------------------------------------------------------------

**[display attack-defense scan victim ipv6**]命令用来显示扫描攻击被攻击者IPv6表项。

【命令】

集中式设备：

**[display attack-defense scan victim ipv6**[ [ **interface** *interface-type interface-number* \| **local** ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense scan victim ipv6**[ [ **interface** *interface-type interface-number* \| **local** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display attack-defense scan victim ipv6**[ [ **interface** *interface-type interface-number* \| **local** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的被攻击者的IPv6地址表项，*interface-type interface-number*表示接口类型和接口编号[。]

**[count**]：仅显示符合指定条件的当前被攻击者的数目。

**[slot*** slot-number*]：显示指定单板上的被攻击者的IPv6地址表项，*slot-number*表示单板所在槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的IPv6地址表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的被攻击者的IPv6地址表项，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备上的被攻击者的IPv6地址表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的被攻击者的IPv6地址表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有成员设备/PEX上的被攻击者的IPv6地址表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的被攻击者的IPv6地址表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的IPv6地址表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的被攻击者的IPv6地址表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定本机或指定全局接口（例如VLAN接口、Tunnel接口）时可见。如果不指定该参数，则表示显示所有单板上的被攻击者的IPv6地址表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的被攻击者的IPv6地址表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[local**]：显示本机检测到的被攻击者的IPv6地址表项。

【使用指导】

若不指定任何参数，则表示显示所有扫描攻击的被攻击者的IPv6地址表项。

【举例】

\# 显示扫描攻击的被攻击者的IPv6地址表项。（集中式设备）

\<Sysname\> display attack-defense scan victim ipv6

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  210

1230::22                 \--               GE1/0/4                  13

\# 显示扫描攻击的被攻击者的IPv6地址表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan victim ipv6

Slot 1:

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  210

1230::22                 \--               GE1/0/4                  13

Slot 2：

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  210

1230[::22                 \--               GE1/0/4                  13{.TerminalDisplayChar}]

\# 显示扫描攻击的被攻击者的IPv6地址表项。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan victim ipv6

Slot 1 in chassis 0:

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  210

1230::22                 \--               GE1/0/4                  13

Slot 2 in chassis 1:

IPv6 address             VPN instance     Detected on              Duration(min)

2013::2                  \--               GE1/0/4                  210

1230::22                 \--               GE1/0/4                  13

\# 显示扫描攻击的被攻击者的IPv6地址表项的个数。（集中式设备）

\<Sysname\> display attack-defense scan victim ipv6 count

Totally 3 victim IP addresses.

\# 显示扫描攻击的被攻击者的IPv6地址表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense scan victim ipv6 count

Slot 1:

Totally 3 victim IP addresses.

Slot 2:

Totally 3 victim IP addresses.

\# 显示扫描攻击的被攻击者的IPv6地址表项的个数。（分布式设备－IRF模式）

\<Sysname\> display attack-defense scan victim ipv6 count

Slot 1 in chassis 0:

Totally 3 victim IP addresses.

Slot 2 in chassis 1:

Totally 3 victim IP addresses.

表1-10 display attack-defense scan victim ipv6命令显示信息描述表

字段

描述

Totally 3 victim IP addresses

被攻击者的数目

IPv6 address

被攻击的IPv6地址

VPN instance

所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

Detected on

进行攻击检测的位置，包括接口或本机（Local）

Duration(min)

检测到被攻击的持续时间，单位为分钟

【相关命令】

·**display attack-defense scan attacker ipv6**

·**scan detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense statistics interface**

------------------------------------------------------------------------

**[display attack-defense statistics interface**]命令用来显示接口上的攻击防范统计信息。

【命令】

集中式设备：

**[display attack-defense statistics interface ***interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense statistics interface ***interface-type interface-number* \**[slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display attack-defense statistics interface ***interface-type interface-number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：表示指定接口的接口类型和接口编号。

**[slot** *slot-number*]：显示全局接口在指定单板上的攻击防范统计信息，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示指定全局接口在所有单板上的攻击防范统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示全局接口在指定成员设备上的攻击防范统计信息，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示指定全局接口在所有成员设备上的攻击防范统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示全局接口在指定成员设备上的攻击防范统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示指定全局接口在所有成员设备/PEX上的攻击防范统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示全局接口在指定成员设备的指定单板上的攻击防范统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示指定全局接口在所有单板上的攻击防范统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示全局接口在指定单板上的攻击防范统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示指定全局接口在所有单板上的攻击防范统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的攻击防范统计信息，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

参数**slot** *slot-number*（分布式设备－独立运行模式）、 **slot** *slot-number*（集中式IRF设备）、 **chassis** *chassis-number* **slot** *slot-number*（分布式设备－IRF模式）只在指定接口为全局接口时可以输入。

【举例】

\# 显示GigabitEthernet1/0/1上的攻击防范统计信息。（集中式设备）

\<Sysname\> display attack-defense statistics interface gigabitethernet 1/0/1

Attack policy name: abc

Scan attack defense statistics:

 AttackType                          AttackTimes Dropped

 Port scan                           2           23

 IP sweep                            3           33

 Distribute port scan                1           10

Flood attack defense statistics:

 AttackType                          AttackTimes Dropped

 SYN flood                           1           0

 ACK flood                           1           0

 SYN-ACK flood                       3           5000

 RST flood                           2           0

 FIN flood                           2           0

 UDP flood                           1           0

 ICMP flood                          1           0

 ICMPv6 flood                        1           0

 DNS flood                           1           0

 HTTP flood                          1           0

Signature attack defense statistics:

 AttackType                          AttackTimes Dropped

 IP option record route              1           100

 IP option security                  2           0

 IP option stream ID                 3           0

 IP option internet timestamp        4           1

 IP option loose source routing      5           0

 IP option strict source routing     6           0

 IP option route alert               3           0

 Fragment                            1           0

 Impossible                          1           1

 Teardrop                            1           1

 Tiny fragment                       1           0

 IP options abnormal                 3           0

 Smurf                               1           0

 Ping of death                       1           0

 Traceroute                          1           0

 Large ICMP                          1           0

 TCP NULL flag                       1           0

 TCP all flags                       1           0

 TCP SYN-FIN flags                   1           0

 TCP FIN only flag                   1           0

 TCP invalid flag                    1           0

 TCP Land                            1           0

 Winnuke                             1           0

 UDP Bomb                            1           0

 Snork                               1           0

 Fraggle                             1           0

 Large ICMPv6                        1           0

 ICMP echo request                   1           0

 ICMP echo reply                     1           0

 ICMP source quench                  1           0

 ICMP destination unreachable        1           0

 ICMP redirect                       2           0

 ICMP time exceeded                  3           0

 ICMP parameter problem              4           0

 ICMP timestamp request              5           0

 ICMP timestamp reply                6           0

 ICMP information request            7           0

 ICMP information reply              4           0

 ICMP address mask request           2           0

 ICMP address mask reply             1           0

 ICMPv6 echo request                 1           1

 ICMPv6 echo reply                   1           1

 ICMPv6 group membership query       1           0

 ICMPv6 group membership report      1           0

 ICMPv6 group membership reduction   1           0

 ICMPv6 destination unreachable      1           0

 ICMPv6 time exceeded                1           0

 ICMPv6 parameter problem            1           0

 ICMPv6 packet too big               1           0

\# 显示Slot 1的GigabitEthernet1/0/1上的攻击防范统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense statistics interface gigabitethernet 1/0/1 slot 1

Attack policy name: abc

Slot 1:

Scan attack defense statistics:

 AttackType                          AttackTimes Dropped

 Port scan                           2           23

 IP sweep                            3           33

 Distribute port scan                1           10

Flood attack defense statistics:

 AttackType                          AttackTimes Dropped

 SYN flood                           1           0

 ACK flood                           1           0

 SYN-ACK flood                       3           5000

 RST flood                           2           0

 FIN flood                           2           0

 UDP flood                           1           0

 ICMP flood                          1           0

 ICMPv6 flood                        1           0

 DNS flood                           1           0

 HTTP flood                          1           0

Signature attack defense statistics:

 AttackType                          AttackTimes Dropped

 IP option record route              1           100

 IP option security                  2           0

 IP option stream ID                 3           0

 IP option internet timestamp        4           1

 IP option loose source routing      5           0

 IP option strict source routing     6           0

 IP option route alert               3           0

 Fragment                            1           0

 Impossible                          1           1

 Teardrop                            1           1

 Tiny fragment                       1           0

 IP options abnormal                 3           0

 Smurf                               1           0

 Ping of death                       1           0

 Traceroute                          1           0

 Large ICMP                          1           0

 TCP NULL flag                       1           0

 TCP all flags                       1           0

 TCP SYN-FIN flags                   1           0

 TCP FIN only flag                   1           0

 TCP invalid flag                    1           0

 TCP Land                            1           0

 Winnuke                             1           0

 UDP Bomb                            1           0

 Snork                               1           0

 Fraggle                             1           0

 Large ICMPv6                        1           0

 ICMP echo request                   1           0

 ICMP echo reply                     1           0

 ICMP source quench                  1           0

 ICMP destination unreachable        1           0

 ICMP redirect                       2           0

 ICMP time exceeded                  3           0

 ICMP parameter problem              4           0

 ICMP timestamp request              5           0

 ICMP timestamp reply                6           0

 ICMP information request            7           0

 ICMP information reply              4           0

 ICMP address mask request           2           0

 ICMP address mask reply             1           0

 ICMPv6 echo request                 1           1

 ICMPv6 echo reply                   1           1

 ICMPv6 group membership query       1           0

 ICMPv6 group membership report      1           0

 ICMPv6 group membership reduction   1           0

 ICMPv6 destination unreachable      1           0

 ICMPv6 time exceeded                1           0

 ICMPv6 parameter problem            1           0

 ICMPv6 packet too big               1           0

\# 显示Chassis 0的slot 1上GigabitEthernet1/0/1上的攻击防范信息。（分布式设备－IRF设备）

\<Sysname\> display attack-defense statistics interface gigabitethernet 1/0/1 chassis 0 slot 1

Attack policy name: abc

Slot 1 in chassis 0:

Scan attack defense statistics:

 AttackType                          AttackTimes Dropped

 Port scan                           2           23

 IP sweep                            3           33

 Distribute port scan                1           10

Flood attack defense statistics:

 AttackType                          AttackTimes Dropped

 SYN flood                           1           0

 ACK flood                           1           0

 SYN-ACK flood                       3           5000

 RST flood                           2           0

 FIN flood                           2           0

 UDP flood                           1           0

 ICMP flood                          1           0

 ICMPv6 flood                        1           0

 DNS flood                           1           0

 HTTP flood                          1           0

Signature attack defense statistics:

 AttackType                          AttackTimes Dropped

 IP option record route              1           100

 IP option security                  2           0

 IP option stream ID                 3           0

 IP option internet timestamp        4           1

 IP option loose source routing      5           0

 IP option strict source routing     6           0

 IP option route alert               3           0

 Fragment                            1           0

 Impossible                          1           1

 Teardrop                            1           1

 Tiny fragment                       1           0

 IP options abnormal                 3           0

 Smurf                               1           0

 Ping of death                       1           0

 Traceroute                          1           0

 Large ICMP                          1           0

 TCP NULL flag                       1           0

 TCP all flags                       1           0

 TCP SYN-FIN flags                   1           0

 TCP FIN only flag                   1           0

 TCP invalid flag                    1           0

 TCP Land                            1           0

 Winnuke                             1           0

 UDP Bomb                            1           0

 Snork                               1           0

 Fraggle                             1           0

 Large ICMPv6                        1           0

 ICMP echo request                   1           0

 ICMP echo reply                     1           0

 ICMP source quench                  1           0

 ICMP destination unreachable        1           0

 ICMP redirect                       2           0

 ICMP time exceeded                  3           0

 ICMP parameter problem              4           0

 ICMP timestamp request              5           0

 ICMP timestamp reply                6           0

 ICMP information request            7           0

 ICMP information reply              4           0

 ICMP address mask request           2           0

 ICMP address mask reply             1           0

 ICMPv6 echo request                 1           1

 ICMPv6 echo reply                   1           1

 ICMPv6 group membership query       1           0

 ICMPv6 group membership report      1           0

 ICMPv6 group membership reduction   1           0

 ICMPv6 destination unreachable      1           0

 ICMPv6 time exceeded                1           0

 ICMPv6 parameter problem            1           0

 ICMPv6 packet too big               1           0

表1-11 display attack-defense statistics interface 命令显示信息描述表

字段

描述

AttackType

攻击类型

AttackTimes

受到攻击的次数

Dropped

丢弃报文的数目

SYN flood

SYN flood攻击，当AttackTimes为0时，该列不显示

ACK flood

ACK flood攻击，当AttackTimes为0时，该列不显示

SYN-ACK flood

SYN-ACK flood攻击，当AttackTimes为0时，该列不显示

RST flood

RST flood攻击，当AttackTimes为0时，该列不显示

FIN flood

FIN flood攻击，当AttackTimes为0时，该列不显示

UDP flood

UDP flood 攻击，当AttackTimes为0时，该列不显示

ICMP flood

ICMP flood攻击，当AttackTimes为0时，该列不显示

ICMPv6 flood

ICMPv6 flood攻击，当AttackTimes为0时，该列不显示

DNS flood

DNS flood攻击，当AttackTimes为0时，该列不显示

HTTP flood

HTTP flood攻击，当AttackTimes为0时，该列不显示

Port scan

端口扫描攻击，当AttackTimes 为0时，该列不显示

IP Sweep

IP扫描攻击，当AttackTimes 为0时，该列不显示

Distribute port scan

分布式端口扫描攻击，当AttackTimes为0时，该列不显示

IP option record  route

IP选项record route攻击，当AttackTimes为0时，该列不显示

IP option security

IP选项security攻击，当AttackTimes 为0时，该列不显示

IP option stream ID

IP选项stream identifier攻击，当AttackTimes 为0时，该列不显示

IP option internet timestamp

IP选项 internet timestamp攻击，当AttackTimes为0时，该列不显示

IP option loose source routing

IP选项loose source routing攻击，当AttackTimes为0时，该列不显示

IP option strict source routing

IP选项strict source routing攻击，当AttackTimes为0时，该列不显示

IP option route alert

IP 选项strict source routing攻击，当AttackTimes为0时，该列不显示

Fragment

IP分片异常攻击，当AttackTimes为0时，该列不显示

Impossible

IP impossible攻击，当AttackTimes为0时，该列不显示

Teardrop

IP teardrop攻击，又称IP overlapping fragments，当AttackTimes为0时，该列不显示

Tiny fragment

IP tiny fragment攻击

IP option abnormal

IP选项异常攻击，当AttackTimes为0时，该列不显示

Smurf

Smurf攻击，当AttackTimes为0时，该列不显示

Ping of death

Ping of death攻击，当AttackTimes为0时，该列不显示

Traceroute

Traceroute攻击，当AttackTimes为0时，该列不显示

Large ICMP

Large ICMP攻击，当AttackTimes为[0时，该列不显示]

TCP NULL flag

TCP NULL flag攻击，当AttackTimes为0时，该列不显示

TCP all flags

TCP所有标志位均被置位攻击，又称圣诞树攻击，当AttackTimes为0时，该列不显示

TCP SYN-FIN flags

TCP SYN和FIN被同时置位攻击，当AttackTimes为0时，该列不显示

TCP FIN only flag

TCP 只有FIN被置位的攻击，当AttackTimes为0时，该列不显示

TCP invalid flag

TCP 非法标志位攻击，当AttackTimes 为0时，该列不显示

TCP Land

TCP Land攻击，当AttackTimes为0时，该列不显示

Winnuke

Winnuke攻击，当AttackTimes为0时，该列不显示

UDP Bomb

UDP Bomb攻击，当AttackTimes为0时，该列不显示

Snork

UDP snork攻击，当AttackTimes为0时，该列不显示

Fraggle

Fraggle攻击，又称UDP chargen DoS attack，当AttackTimes为0时，该列不显示

Large ICMPv6

Large ICMPv6攻击，当AttackTimes为0时，该列不显示

ICMP echo request

ICMP echo request攻击，当AttackTimes为0时，该列不显示

ICMP echo reply

ICMP echo reply攻击，当AttackTimes为0时，该列不显示

ICMP source quench

ICMP source quench攻击，当AttackTimes为0时，该列不显示

ICMP destination unreachable

ICMP destination unreachable攻击，当AttackTimes为0时，该列不显示

ICMP redirect

ICMP redirect攻击，当AttackTimes为0时，该列不显示

ICMP time exceeded

ICMP time exceeded攻击，当AttackTimes为0时，该列不显示

ICMP parameter problem

ICMP parameter problem攻击，当AttackTimes 为0时，该列不显示

ICMP timestamp request

ICMP timestamp request攻击，当AttackTimes为0时，该列不显示

ICMP timestamp reply

ICMP timestamp reply攻击，当AttackTimes为0时，该列不显示

ICMP information request

ICMP information request攻击，当AttackTimes为0时，该列不显示

ICMP information reply

ICMP information reply攻击，当AttackTimes为0时，该列不显示

ICMP address mask request

ICMP address mask request攻击，当AttackTimes为0时，该列不显示

ICMP address mask reply

ICMP address mask reply攻击，当AttackTimes为0时，该列不显示

ICMPv6 echo request

ICMPv6 echo request攻击，当AttackTimes 为0时，该列不显示

ICMPv6 echo reply

ICMPv6 echo reply攻击，当AttackTimes为0时，该列不显示

ICMPv6 group membership query

ICMPv6 group membership query攻击，当AttackTimes为0时，该列不显示

ICMPv6 group membership report

ICMPv6 group membership report攻击，当AttackTimes为0时，该列不显示

ICMPv6 group membership reduction

ICMPv6 group membership reduction攻击，当AttackTimes为0时，该列不显示

ICMPv6 destination unreachable

ICMPv6 destination unreachable攻击，当AttackTimes为0时，该列不显示

ICMPv6 time exceeded

ICMPv6 time exceeded攻击，当AttackTimes为0时，该列不显示

ICMPv6 parameter problem

ICMPv6 parameter problem攻击，当AttackTimes为0时，该列不显示

ICMPv6 packet too big

ICMPv6 packet too big攻击，当AttackTimes为0时，该列不显示

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display attack-defense statistics local**

------------------------------------------------------------------------

**[display attack-defense statistics local**]命令用来显示本机攻击防范的统计信息。

【命令】

集中式设备：

**[display attack-defense statistics local**]

分布式设备－独立运行模式/集中式IRF设备：

**[display attack-defense statistics local****\**[slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display attack-defense statistics local** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示本机攻击防范在指定单板上的统计信息，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上检测到的本机攻击防范统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示本机攻击防范在指定成员设备上的统计信息，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上检测到的本机攻击防范统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示本机攻击防范在指定成员设备/PEX上的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上检测到的本机攻击防范统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示本机攻击防范在指定成员设备的指定单板上的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上检测到的本机攻击防范统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示本机攻击防范在指定单板上的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上检测到的本机攻击防范统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的本机攻击防范的统计信息，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示本机攻击防范统计信息。（集中式设备）

\<Sysname\> display attack-defense statistics local

Attack defense policy name: abc

Scan attack defense statistics:

 AttackType                          AttackTimes Dropped

 Port scan                           2           23

 IP sweep                            3           33

 Distribute port scan                1           10

Flood attack defense statistics:

 AttackType                          AttackTimes Dropped

 SYN flood                           1           0

 ACK flood                           1           0

 SYN-ACK flood                       3           5000

 RST flood                           2           0

 FIN flood                           2           0

 UDP flood                           1           0

 ICMP flood                          1           0

 ICMPv6 flood                        1           0

 DNS flood                           1           0

 HTTP flood                          1           0

Signature attack defense statistics:

 AttackType                          AttackTimes Dropped

 IP option record route              1           100

 IP option security                  2           0

 IP option stream ID                 3           0

 IP option internet timestamp        4           1

 IP option loose source routing      5           0

 IP option strict source routing     6           0

 IP option route alert               3           0

 Fragment                            1           0

 Impossible                          1           1

 Teardrop                            1           1

 Tiny fragment                       1           0

 IP options abnormal                 3           0

 Smurf                               1           0

 Ping of death                       1           0

 Traceroute                          1           0

 Large ICMP                          1           0

 TCP NULL flag                       1           0

 TCP all flags                       1           0

 TCP SYN-FIN flags                   1           0

 TCP FIN only flag                   1           0

 TCP invalid flag                    1           0

 TCP Land                            1           0

 Winnuke                             1           0

 UDP Bomb                            1           0

 Snork                               1           0

 Fraggle                             1           0

 Large ICMPv6                        1           0

 ICMP echo request                   1           0

 ICMP echo reply                     1           0

 ICMP source quench                  1           0

 ICMP destination unreachable        1           0

 ICMP redirect                       2           0

 ICMP time exceeded                  3           0

 ICMP parameter problem              4           0

 ICMP timestamp request              5           0

 ICMP timestamp reply                6           0

 ICMP information request            7           0

 ICMP information reply              4           0

 ICMP address mask request           2           0

 ICMP address mask reply             1           0

 ICMPv6 echo request                 1           1

 ICMPv6 echo reply                   1           1

 ICMPv6 group membership query       1           0

 ICMPv6 group membership report      1           0

 ICMPv6 group membership reduction   1           0

 ICMPv6 destination unreachable      1           0

 ICMPv6 time exceeded                1           0

 ICMPv6 parameter problem            1           0

 ICMPv6 packet too big               1           0

\# 显示本机攻击防范统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display attack-defense statistics local

Attack policy name: abc

Slot 1:

Scan attack defense statistics:

 AttackType                          AttackTimes Dropped

 Port scan                           2           23

 IP sweep                            3           33

 Distribute port scan                1           10

Flood attack defense statistics:

 AttackType                          AttackTimes Dropped

 SYN flood                           1           0

 ACK flood                           1           0

 SYN-ACK flood                       3           5000

 RST flood                           2           0

 FIN flood                           2           0

 UDP flood                           1           0

 ICMP flood                          1           0

 ICMPv6 flood                        1           0

 DNS flood                           1           0

 HTTP flood                          1           0

Signature attack defense statistics:

 AttackType                          AttackTimes Dropped

 IP option record route              1           100

 IP option security                  2           0

 IP option stream ID                 3           0

 IP option internet timestamp        4           1

 IP option loose source routing      5           0

 IP option strict source routing     6           0

 IP option route alert               3           0

 Fragment                            1           0

 Impossible                          1           1

 Teardrop                            1           1

 Tiny fragment                       1           0

 IP options abnormal                 3           0

 Smurf                               1           0

 Ping of death                       1           0

 Traceroute                          1           0

 Large ICMP                          1           0

 TCP NULL flag                       1           0

 TCP all flags                       1           0

 TCP SYN-FIN flags                   1           0

 TCP FIN only flag                   1           0

 TCP invalid flag                    1           0

 TCP Land                            1           0

 Winnuke                             1           0

 UDP Bomb                            1           0

 Snork                               1           0

 Fraggle                             1           0

 Large ICMPv6                        1           0

 ICMP echo request                   1           0

 ICMP echo reply                     1           0

 ICMP source quench                  1           0

 ICMP destination unreachable        1           0

 ICMP redirect                       2           0

 ICMP time exceeded                  3           0

 ICMP parameter problem              4           0

 ICMP timestamp request              5           0

 ICMP timestamp reply                6           0

 ICMP information request            7           0

 ICMP information reply              4           0

 ICMP address mask request           2           0

 ICMP address mask reply             1           0

 ICMPv6 echo request                 1           1

 ICMPv6 echo reply                   1           1

 ICMPv6 group membership query       1           0

 ICMPv6 group membership report      1           0

 ICMPv6 group membership reduction   1           0

 ICMPv6 destination unreachable      1           0

 ICMPv6 time exceeded                1           0

 ICMPv6 parameter problem            1           0

 ICMPv6 packet too big               1           0

\# 显示本机攻击防范统计信息。（分布式IRF设备）

\<Sysname\> display attack-defense statistics local

Attack policy name: abc

Slot 1 in chassis 0:

Scan attack defense statistics:

 AttackType                          AttackTimes Dropped

 Port scan                           2           23

 IP sweep                            3           33

 Distribute port scan                1           10

Flood attack defense statistics:

 AttackType                          AttackTimes Dropped

 SYN flood                           1           0

 ACK flood                           1           0

 SYN-ACK flood                       3           5000

 RST flood                           2           0

 FIN flood                           2           0

 UDP flood                           1           0

 ICMP flood                          1           0

 ICMPv6 flood                        1           0

 DNS flood                           1           0

 HTTP flood                          1           0

Signature attack defense statistics:

 AttackType                          AttackTimes Dropped

 IP option record route              1           100

 IP option security                  2           0

 IP option stream ID                 3           0

 IP option internet timestamp        4           1

 IP option loose source routing      5           0

 IP option strict source routing     6           0

 IP option route alert               3           0

 Fragment                            1           0

 Impossible                          1           1

 Teardrop                            1           1

 Tiny fragment                       1           0

 IP options abnormal                 3           0

 Smurf                               1           0

 Ping of death                       1           0

 Traceroute                          1           0

 Large ICMP                          1           0

 TCP NULL flag                       1           0

 TCP all flags                       1           0

 TCP SYN-FIN flags                   1           0

 TCP FIN only flag                   1           0

 TCP invalid flag                    1           0

 TCP Land                            1           0

 Winnuke                             1           0

 UDP Bomb                            1           0

 Snork                               1           0

 Fraggle                             1           0

 Large ICMPv6                        1           0

 ICMP echo request                   1           0

 ICMP echo reply                     1           0

 ICMP source quench                  1           0

 ICMP destination unreachable        1           0

 ICMP redirect                       2           0

 ICMP time exceeded                  3           0

 ICMP parameter problem              4           0

 ICMP timestamp request              5           0

 ICMP timestamp reply                6           0

 ICMP information request            7           0

 ICMP information reply              4           0

 ICMP address mask request           2           0

 ICMP address mask reply             1           0

 ICMPv6 echo request                 1           1

 ICMPv6 echo reply                   1           1

 ICMPv6 group membership query       1           0

 ICMPv6 group membership report      1           0

 ICMPv6 group membership reduction   1           0

 ICMPv6 destination unreachable      1           0

 ICMPv6 time exceeded                1           0

 ICMPv6 parameter problem            1           0

 ICMPv6 packet too big               1           0

表1-12 display attack-defense statistics local命令显示信息描述表

字段

描述

AttackType

攻击类型

AttackTimes

受到攻击的次数

Dropped

丢弃报文的数目

Port scan

端口扫描攻击，当AttackTimes为0时，该列不显示

IP Sweep

IP扫描攻击，当AttackTimes为0时，该列不显示

Distribute port scan

分布式端口扫描攻击，当AttackTimes为0时，该列不显示

SYN flood

SYN flood攻击，当AttackTimes 为0时，该列不显示

ACK flood

ACK flood攻击，当AttackTimes 为0时，该列不显示

SYN-ACK flood

SYN-ACK flood攻击，当AttackTimes为0时，该列不显示

RST flood

RST flood攻击，当AttackTimes为0时，该列不显示

FIN flood

FIN flood攻击，当AttackTimes为0时，该列不显示

UDP flood

UDP flood 攻击，当AttackTimes为0时，该列不显示

ICMP flood

ICMP flood攻击，当AttackTimes为0时，该列不显示

ICMPv6 flood

ICMPv6 flood攻击，当AttackTimes为0时，该列不显示

DNS flood

DNS flood攻击，当AttackTimes为0时，该列不显示

HTTP flood

HTTP flood攻击，当AttackTimes为0时，该列不显示

IP option record  route

IP 选项record route攻击，当AttackTimes为0时，该列不显示

IP option security

IP 选项security攻击，当AttackTimes为0时，该列不显示

IP option stream ID

IP 选项stream identifier攻击，当AttackTimes为0时，该列不显示

IP option internet timestamp

IP 选项 internet timestamp攻击，当AttackTimes为0时，该列不显示

IP option loose source routing

IP 选项loose source routing攻击，当AttackTimes为0时，该列不显示

IP option strict source routing

IP 选项strict source routing攻击，当AttackTimes为0时，该列不显示

IP option route alert

IP 选项strict source routing攻击，当AttackTimes为0时，该列不显示

Fragment

IP分片异常攻击，当AttackTimes为0时，该列不显示

Impossible

IP impossible攻击，当AttackTimes为0时，该列不显示

Teardrop

IP teardrop攻击，又称IP overlapping fragments，当AttackTimes为0时，该列不显示

Tiny fragment

IP tiny fragment攻击

IP option abnormal

IP 选项异常攻击，当AttackTimes为0时，该列不显示

Smurf

Smurf攻击，当AttackTimes为0时，该列不显示

Ping of death

Ping of death攻击，当AttackTimes为0时，该列不显示

Traceroute

Traceroute攻击，当AttackTimes为0时，该列不显示

Large ICMP

Large ICMP攻击，当AttackTimes为[0时，该列不显示]

TCP NULL flag

TCP NULL flag攻击，当AttackTimes为0时，该列不显示

TCP all flags

TCP所有标志位均被置位攻击，又称圣诞树攻击，当AttackTimes为0时，该列不显示

TCP SYN-FIN flags

TCP SYN和FIN被同时置位攻击，当AttackTimes为0时，该列不显示

TCP FIN only flag

TCP只有FIN被置位的攻击，当AttackTimes为0时，该列不显示

TCP invalid flag

TCP非法标志位攻击，当AttackTimes为0时，该列不显示

TCP Land

TCP Land攻击，当AttackTimes为0时，该列不显示

Winnuke

Winnuke攻击，当AttackTimes为0时，该列不显示

UDP Bomb

UDP Bomb攻击，当AttackTimes为0时，该列不显示

Snork

Snork攻击，当AttackTimes为0时，该列不显示

Fraggle

Fraggle攻击，又称UDP chargen DoS attack，当AttackTimes为0时，该列不显示

Large ICMPv6

Large ICMPv6攻击，当AttackTimes为0时，该列不显示

ICMP echo request

ICMP echo request攻击，当AttackTimes 为0时，该列不显示

ICMP echo reply

ICMP echo reply攻击，当AttackTimes为0时，该列不显示

ICMP source quench

ICMP source quench攻击，当AttackTimes为0时，该列不显示

ICMP destination unreachable

ICMP destination unreachable攻击，当AttackTimes为0时，该列不显示

ICMP redirect

ICMP redirect攻击，当AttackTimes为0时，该列不显示

ICMP time exceeded

ICMP time exceeded攻击，当AttackTimes为0时，该列不显示

ICMP parameter problem

ICMP parameter problem攻击，当AttackTimes为0时，该列不显示

ICMP timestamp request

ICMP timestamp request攻击，当AttackTimes为0时，该列不显示

ICMP timestamp reply

ICMP timestamp reply攻击，当AttackTimes为0时，该列不显示

ICMP information request

ICMP information request攻击，当AttackTimes为0时，该列不显示

ICMP information reply

ICMP information reply攻击，当AttackTimes为0时，该列不显示

ICMP address mask request

ICMP address mask request攻击，当AttackTimes为0时，该列不显示

ICMP address mask reply

ICMP address mask reply攻击，当AttackTimes为0时，该列不显示

ICMPv6 echo request

ICMPv6 echo request攻击，当AttackTimes 为0时，该列不显示

ICMPv6 echo reply

ICMPv6 echo reply攻击，当AttackTimes为0时，该列不显示

ICMPv6 group membership query

ICMPv6 group membership query攻击，当AttackTimes 为0时，该列不显示

ICMPv6 group membership report

ICMPv6 group membership report攻击，当AttackTimes为0时，该列不显示

ICMPv6 group membership reduction

ICMPv6 group membership reduction攻击，当AttackTimes为0时，该列不显示

ICMPv6 destination unreachable

ICMPv6 destination unreachable攻击，当AttackTimes为0时，该列不显示

ICMPv6 time exceeded

ICMPv6 time exceeded攻击，当AttackTimes为0时，该列不显示

ICMPv6 parameter problem

ICMPv6 parameter problem攻击，当AttackTimes为0时，该列不显示

ICMPv6 packet too big

ICMPv6 packet too big攻击，当AttackTimes为0时，该列不显示

【相关命令】

·**reset attack-defense statistics local**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display blacklist ip**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display blacklist ip**]命令用来显示IPv4黑名单表项。

【命令】

集中式设备：

**[display blacklist** **ip** [ *source-ip-address* [ **vpn-instance** *vpn-instance-name*  ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display blacklist ip ** *source-ip-address*  **vpn-instance** *vpn-instance-name*  ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count**

分布式设备－IRF模式：

**[display blacklist ip** [ *source-ip-address* [ **vpn-instance** *vpn-instance-name*  ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[source-ip-address*]：显示指定IPv4地址的黑名单表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv4黑名单表项。其中*vpn-instance-name*表示VPN实例名称，为1～31个字符的字符串，区分大小写。

**[slot** *slot-number*]：显示指定单板上的IPv4黑名单表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的IPv4黑名单表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv4黑名单表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的IPv4黑名单表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的IPv4黑名单表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的IPv4黑名单表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv4黑名单表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有单板上的IPv4黑名单表项。（分布式设备－IRF模式）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的IPv4黑名单表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的IPv4黑名单表项。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：显示指定CPU上的IPv4黑名单表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的IPv4黑名单个数。

【使用指导】

若不指定任何参数，则表示显示所有的IPv4黑名单表项。

【举例】

\# 显示所有IPv4黑名单表项的信息。（集中式设备）

\<Sysname\> display blacklist ip

IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped

192.168.11.5    \--             \--                   Dynamic 10       353452

123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295

201.55.7.45     abc            2013::1              Manual  Never   14478

 # 显示Slot 1上所有IPv4黑名单表项的信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display blacklist ip slot 1

Slot 1:

IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped

192.168.11.5    \--             \--                   Dynamic 10       353452

123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295

201.55.7.45     abc            2013::1              Manual  Never   14478

\# 显示所有IPv4黑名单表项的信息。（分布式IRF设备）

\<Sysname\> display blacklist ip

Slot 1 in chassis 0:

IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped

192.168.11.5    \--             \--                   Dynamic 10       353452

123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295

201.55.7.45     abc            2013::1              Manual  Never   14478

Slot 2 in chassis 1:

IP address      VPN instance   DS-Lite tunnel peer  Type    TTL(sec) Dropped

192.168.11.5    \--             \--                   Dynamic 10       353452

123.123.123.123 a0123456789012 2013::fe07:221a:4011 Dynamic 123      4294967295

201.55.7.45     abc            2013::1              Manual  Never   14478

\# 显示所有IPv4黑名单表项的个数。（集中式设备）

\<Sysname\> display blacklist ip count

Totally 3 blacklist entries.

\# 显示Slot 1上所有IPv4黑名单表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display blacklist ip slot 1 count

Slot 1:

Totally 3 blacklist entries.

\# 显示所有IPv4黑名单表项的个数。（分布式IRF设备）

\<Sysname\> display blacklist ip count

Slot 1 in chassis 0:

Totally 3 blacklist entries.

Slot 2 in chassis 1:

Totally 3 blacklist entries.

表1-13 display blacklist ip命令显示信息描述表

字段

描述

IP address

黑名单表项的IP地址

VPN instance

VPN实例名称，属于公网时显示为"\--"

DS-Lite tunnel peer

DS-Lite隧道对端地址 。DS-Lite组网下，若本设备为AFTR，此列表示报文来自具体的哪个B4，如果不在DS-Lite组网或本设备不为AFTR，则该字段无意义，显示为"\--"

Type

黑名单表项的添加方式

TTL(sec)

黑名单表项的剩余老化时间，单位为秒。若未指定老化时间，则显示"Never"

Dropped

丢弃的来自该IP地址的报文数目

Totally 3 blacklist entries.

黑名单表项数目

【相关命令】

·**blacklist ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display blacklist ipv6**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display blacklist ipv6**]命令用来显示IPv6黑名单表项。

【命令】

集中式设备：

**[display blacklist** **ipv6** [ *source-ipv6-address* [ **vpn-instance** *vpn-instance-name*  ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display blacklist ipv6 ** *source-ipv6-address*  **vpn-instance** *vpn-instance-name*  ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count**

分布式设备－IRF模式：

**[display blacklist ipv6** [ *source-ipv6-address* [ **vpn-instance** *vpn-instance-name*  ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[source-ipv6-address*]：显示指定IPv6地址的黑名单表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv6黑名单表项。其中*vpn-instance-name*表示VPN实例名称，为1～31个字符的字符串，区分大小写。

**[slot** *slot-number*]：显示指定单板上的IPv6黑名单表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的IPv6黑名单表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv6黑名单表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的IPv6黑名单表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的IPv6黑名单表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的IPv6黑名单表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6黑名单表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的IPv6黑名单表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的IPv6黑名单表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的IPv6黑名单表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的IPv6黑名单表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：仅显示符合指定条件的IPv6黑名单个数。

【使用指导】

若不指定任何参数，则表示显示所有的IPv6黑名单表项。

【举例】

\# 显示所有IPv6黑名单表项的信息。（集中式设备）

\<Sysname\> display blacklist ipv6

Totally 3 blacklist entries.

IPv6 address         VPN instance      Type    TTL(sec) Dropped

1::4                 \--                Manual  Never   14478

1::5                 \--                Dynamic 10       353452

2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295

2013:fe07:221a:4011  67890123456789

\# 显示Slot 1上所有IPv6黑名单表项的信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display blacklist ipv6 slot 1

Slot 1:

Totally 3 blacklist entries.

IPv6 address         VPN instance      Type    TTL(sec) Dropped

1::4                 \--                Manual  Never   14478

1::5                 \--                Dynamic 10       353452

2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295

2013:fe07:221a:4011  67890123456789

\# 显示所有IPv6黑名单表项的信息。（分布式IRF设备）

\<Sysname\> display blacklist ipv6

Slot 1 in chassis 0:

Totally 3 blacklist entries.

IPv6 address         VPN instance      Type    TTL(sec) Dropped

1::4                 \--                Manual  Never   14478

1::5                 \--                Dynamic 10       353452

2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295

2013:fe07:221a:4011  67890123456789

Slot 2 in chassis 1:

Totally 3 blacklist entries.

IPv6 address         VPN instance      Type    TTL(sec) Dropped

1::4                 \--                Manual  Never   14478

1::5                 \--                Dynamic 10       353452

2013:fe07:221a:4011: a0123456789012345 Dynamic 123      4294967295

2013:fe07:221a:4011  67890123456789

\# 显示所有IPv6黑名单表项的个数。（集中式设备）

\<Sysname\> display blacklist ipv6 count

Totally 3 blacklist entries.

\# 显示Slot 1上所有IPv6黑名单表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display blacklist ipv6 slot 1 count

Slot 1:

Totally 3 blacklist entries.

\# 显示所有IPv6黑名单表项的个数。（分布式IRF设备）

\<Sysname\> display blacklist ipv6 count

Slot 1 in chassis 0:

Totally 3 blacklist entries.

Slot 2 in chassis 1:

Totally 3 blacklist entries.

表1-14 display blacklist ipv6命令显示信息描述表

字段

描述

IPv6 address

黑名单表项的IPv6地址

VPN instance

VPN实例名称，属于公网时显示为"[\--"]

Type

黑名单表项的添加方式

TTL(sec)

黑名单表项的剩余老化时间，单位为秒。若未指定老化时间，则显示"Never"

Dropped

丢弃的来自该IPv6地址的报文数目

Totally 3 blacklist entries.

黑名单表项数目

【相关命令】

·**blacklist ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify protected ip**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display client-verify protected** **ip**]命令用来显示客户端验证的IPv4类型的受保护IP表项。

【命令】

集中式设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } **protected**] **ip** [ *ip-address* [ **vpn** *vpn-instance-name*  ]  **port** *port-number*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } **protected**] **ip** [ *ip-address* [ **vpn** *vpn-instance-name*  ]  **port** *port-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } **protected** ]**ip ** *ip-address*  **vpn** *vpn-instance-name*  ]  **port** *port-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

*[ip-address*]：显示指定IPv4地址的受保护IP表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的受保护IP表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示显示公网中的受保护IP地址。

**[port** *port-number*]：显示指定端口号的受保护IP表项，*port-number*的取值范围为1～65535。若不指定该参数，对于DNS客户端验证的受保护IP，则表示端口53；对于HTTP客户端验证的受保护IP，则表示端口80；对于TCP客户端验证的受保护IP，则表示所有端口。

**[slot** *slot-number*]：显示指定单板上的受保护IP表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－独立运行模式）。

**[slot** *slot-number*]：显示指定成员设备上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的受保护IP表项。（集中式IRF设备）。（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的受保护IP表项。（集中式IRF设备）。（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的受保护IP表项。（分布式设备－IRF模式）。（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－IRF模式）。（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的受保护IP表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的客户端验证受保护IP表项。

【使用指导】

如果不指定任何参数，则显示所有的IPv4类型的客户端验证受保护IP表项。

【举例】

\# 显示所有IPv4类型TCP客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify tcp protected ip

IP address           VPN instance     Port  Type    Requested  Trusted

192.168.11.5         \--               23    Dynamic 353452     555

123.123.123.123      VPN1             65535 Dynamic 4294967295 15151

201.55.7.45          \--               10    Manual  15000      222

\# 显示所有IPv4类型TCP客户端验证的受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp protected ip

Slot 1:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               23    Dynamic 353452      555

201.55.7.45          \--               10    Manual  15000       222

123.123.123.123      VPN1             65535 Dynamic 4294967295  15151

Slot 2：

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               23    Dynamic 353452      555

201.55.7.45          \--               10    Manual  15000       222

123.123.123.123      VPN1             65535 Dynamic 4294967295  15151

\# 显示所有IPv4类型TCP客户端验证的受保护IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp protected ip

Slot 1 in chassis 0:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               23    Dynamic 353452      555

201.55.7.45          \--               10    Manual  15000       222

123.123.123.123      VPN1             65535 Dynamic 4294967295  15151

Slot 2 in chassis 1:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               23    Dynamic 353452      555

201.55.7.45          \--               10    Manual  15000       222

123.123.123.123      VPN1             65535 Dynamic 4294967295  15151

\# 显示所有IPv4类型TCP客户端验证的受保护IP表项的个数。（集中式设备）

\<Sysname\> display client-verify tcp protected ip count

Totally 3 protected IP addresses.

\# 显示所有IPv4类型TCP客户端验证的受保护IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp protected ip count

Slot 1:

Totally 3 protected IP addresses.

Slot 2：

Totally 3 protected IP addresses.

\# 显示所有IPv4类型TCP客户端验证的受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp protected ip count

Slot 1 in chassis 0:

Totally 3 protected IP addresses.

Slot 2 in chassis 1:

Totally 3 protected IP addresses.

\# 显示所有IPv4类型DNS客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify dns protected ip

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               53    Dynamic 353452      555

201.55.7.45          \--               53    Manual  15000       222

123.123.123.123      VPN1             53    Dynamic 4294967295  15151

\# 显示所有IPv4类型DNS客户端验证的受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns protected ip

Slot 1:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               53    Dynamic 353452      555

201.55.7.45          \--               53    Manual  15000       222

123.123.123.123      VPN1             53    Dynamic 4294967295  15151

Slot 2：

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               53    Dynamic 353452      555

201.55.7.45          \--               53    Manual  15000       222

123.123.123.123      VPN1             53    Dynamic 4294967295  15151

\# 显示所有IPv4类型DNS客户端验证的受保护IP表项。（分布式IRF设备）

\<Sysname\> display client-verify dns protected ip

Slot 1 in chassis 0:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               53    Dynamic 353452      555

201.55.7.45          \--               53    Manual  15000       222

123.123.123.123      VPN1             53    Dynamic 4294967295  15151

Slot 2 in chassis 1:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               53    Dynamic 353452      555

201.55.7.45          \--               53    Manual  15000       222

123.123.123.123      VPN1             53    Dynamic 4294967295  15151

\# 显示所有IPv4类型DNS客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify dns protected ip count

Totally 3 protected IP addresses.

\# 显示所有IPv4类型DNS客户端验证的受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns protected ip count

Slot 1:

Totally 3 protected IP addresses.

Slot 2：

Totally 3 protected IP addresses.

\# 显示所有IPv4类型DNS客户端验证的受保护IP表项的个数。（分布式IRF设备）

\<Sysname\> display client-verify dns protected ip count

Slot 1 in chassis 0:

Totally 3 protected IP addresses.

Slot 2 in chassis 1:

Totally 3 protected IP addresses.

\# 显示所有IPv4类型HTTP客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify http protected ip

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               80    Dynamic 353452      555

201.55.7.45          \--               8080  Manual  15000       222

123.123.123.123      VPN1             80    Dynamic 4294967295  15151

\# 显示所有IPv4类型HTTP客户端验证的受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify http protected ip

Slot 1:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               80    Dynamic 353452      555

201.55.7.45          \--               8080  Manual  15000       222

123.123.123.123      VPN1             80    Dynamic 4294967295  15151

Slot 2：

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               80    Dynamic 353452      555

201.55.7.45          \--               8080  Manual  15000       222

123.123.123.123      VPN1             80    Dynamic 4294967295  15151

\# 显示所有IPv4类型HTTP客户端验证的受保护IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify http protected ip

Slot 1 in chassis 0:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               80    Dynamic 353452      555

201.55.7.45          \--               8080  Manual  15000       222

123.123.123.123      VPN1             80    Dynamic 4294967295  15151

Slot 2 in chassis 1:

IP address           VPN instance     Port  Type    Requested   Trusted

192.168.11.5         \--               80    Dynamic 353452      555

201.55.7.45          \--               8080  Manual  15000       222

123.123.123.123      VPN1             80    Dynamic 4294967295  15151

\# 显示所有IPv4类型HTTP客户端验证的受保护IP表项的个数。（集中式设备）

\<Sysname\> display client-verify http protected ip count

Totally 3 protected IP addresses.

\# 显示所有IPv4类型HTTP客户端验证的受保护IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify http protected ip count

Slot 1:

Totally 3 protected IP addresses.

Slot 2：

Totally 3 protected IP addresses.

\# 显示所有IPv4类型HTTP客户端验证的受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify http protected ip count

Slot 1 in chassis 0:

Totally 3 protected IP addresses.

Slot 2 in chassis 1:

Totally 3 protected IP addresses.

表1-15 display client-verify protected ip命令显示信息描述表

字段

描述

Totally 3 protected IP addresses.

IPv4类型受保护IP表项数目

IP address

受保护IPv4地址

VPN instance

受保护IP地址所属的MPLS L3VPN实例名称，属于公网时显示为"[\--"]

Port

TCP连接的目的端口

any表示对该IP地址的所有端口的TCP连接请求都做代理

Type

受保护IP地址的添加方式，取值包括Dynamic和Manual

Requested

收到的匹配该受保护IP地址的报文数目

Trusted

通过验证的TCP连接请求报文数目

【相关命令】

·**client-verify protected ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify protected ipv6**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display client-verify protected** **ipv6**]命令用来显示客户端验证的IPv6类型的受保护IP表项。

【命令】

集中式设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } **protected**] **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name*  ]  **port** *port-number*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } **protected**] **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name*  ]  **port** *port-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } **protected** ]**ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name*  ]  **port** *port-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

*[ipv6-address*]：显示指定IPv6地址的受保护IP表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的受保护IP表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示显示公网中的受保护IP地址。

**[port** *port-number*]：显示指定端口号的受保护IP表项，*port-number*的取值范围为1～65535。若不指定该参数，对于DNS客户端验证的受保护IP，则表示端口53；对于HTTP客户端验证的受保护IP，则表示端口80；对于TCP客户端验证的受保护IP，则表示所有端口。

**[slot** *slot-number*]：显示指定单板上的受保护IP表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－独立运行模式）。

**[slot** *slot-number*]：显示指定成员设备上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的受保护IP表项。（集中式IRF设备）。（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的受保护IP表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的受保护IP表项。（集中式IRF设备）。（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－IRF模式）。（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的受保护IP表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的受保护IP表项。（分布式设备－IRF模式）。（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的受保护IP表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示符合指定条件的客户端验证受保护IP表项个数。

【使用指导】

如果不指定任何参数，则显示所有的IPv6类型的客户端验证受保护IP表项。

【举例】

\# 显示所有IPv6类型的TCP客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify tcp protected ipv6

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501

1023::1123           vpn1             65535 Dynamic 4294967295  15151

\# 显示所有IPv6类型的TCP客户端验证的受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp protected ipv6

Slot 1:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501

1023::1123           vpn1             65535 Dynamic 4294967295  15151

Slot 2:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501

1023::1123           vpn1             65535 Dynamic 4294967295  15151

\# 显示所有IPv6类型TCP客户端验证的受保护IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp protected ipv6

Slot 1 in chassis 0:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501

1023::1123           vpn1             65535 Dynamic 4294967295  15151

Slot 2 in chassis 1:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               100   Manual  14478       5501

1023::1123           vpn1             65535 Dynamic 4294967295  15151

\# 显示所有IPv6类型的TCP客户端验证的受保护IP表项的个数。（集中式设备）

\<Sysname\> display client-verify tcp protected ipv6 count

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型的TCP客户端验证的受保护IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp protected ip count

Slot 1:

Totally 3 protected IPv6 addresses.

Slot 2:

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型TCP客户端验证的受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp protected ip count

Slot 1 in chassis 0:

Totally 3 protected IPv6 addresses.

Slot 2 in chassis 1:

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型DNS客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify dns protected ipv6

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501

1023::1123           vpn1             53    Dynamic 4294967295  15151

\# 显示所有IPv6类型DNS客户端验证的受保护IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns protected ipv6

Slot 1:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501

1023::1123           vpn1             53    Dynamic 4294967295  15151

Slot 2:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501

1023::1123           vpn1             53    Dynamic 4294967295  15151

\# 显示所有IPv6类型DNS客户端验证的受保护IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify dns protected ipv6

Slot 1 in chassis 0:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501

1023::1123           vpn1             53    Dynamic 4294967295  15151

Slot 2 in chassis 1:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               53    Manual  14478       5501

1023::1123           vpn1             53    Dynamic 4294967295  15151

\# 显示所有IPv6类型DNS客户端验证的受保护IP表项的个数。（集中式设备）

\<Sysname\> display client-verify dns protected ipv6 count

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型DNS客户端验证的受保护IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns protected ipv6 count

Slot 1:

Totally 3 protected IPv6 addresses.

Slot 2:

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型DNS客户端验证的受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify dns protected ipv6 count

Slot 1 in chassis 0:

Totally 3 protected entries.

Slot 2 in chassis 1:

Totally 3 protected entries.

\# 显示所有IPv6类型HTTP客户端验证的受保护IP表项。（集中式设备）

\<Sysname\> display client-verify http protected ipv6

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501

1023::1123           vpn1             80    Dynamic 4294967295  15151

\# 显示所有IPv6类型HTTP客户端验证的受保护IP表项。（分布式设备－独立运行模式/IRF模式）

\<Sysname\> display client-verify http protected ipv6

Slot 1:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501

1023::1123           vpn1             80    Dynamic 4294967295  15151

Slot 2:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501

1023::1123           vpn1             80    Dynamic 4294967295  15151

\# 显示所有IPv6类型HTTP 客户端验证的受保护IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify http protected ipv6

Slot 1 in chassis 0:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501

1023::1123           vpn1             80    Dynamic 4294967295  15151

Slot 2 in chassis 1:

IPv6 address         VPN instance     Port  Type    Requested   Trusted

1:2:3:4:5:6:7:8      \--               8080  Manual  14478       5501

1023::1123           vpn1             80    Dynamic 4294967295  15151

\# 显示所有IPv6类型HTTP客户端验证的受保护IP表项的个数。（集中式设备）

\<Sysname\> display client-verify http protected ipv6 count

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型HTTP客户端验证的受保护IP表项的个数。（分布式设备－独立运行模式/IRF模式）

\<Sysname\> display client-verify http protected ipv6 count

Slot 1:

Totally 3 protected IPv6 addresses.

Slot 2:

Totally 3 protected IPv6 addresses.

\# 显示所有IPv6类型HTTP 客户端验证的受保护IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify http protected ipv6 count

Slot 1 in chassis 0:

Totally 3 protected IPv6 addresses.

Slot 2 in chassis 1:

Totally 3 protected IPv6 addresses.

表1-16 display client-verify protected ipv6命令显示信息描述表

字段

描述

Totally 3 protected IPv6 addresses

IPv6类型受保护IP表项数目

IPv6 address

受保护IPv6地址

VPN instance

受保护IP地址所属的VPN实例名称，属于公网时显示为"[\--"]

Port

TCP连接的目的端口

any表示对该IP地址的所有端口的TCP连接请求都做代理

Type

受保护IP地址的添加方式，取值包括Dynamic和Manual

Requested

收到的匹配该受保护IP地址的报文数目

Trusted

通过验证的TCP连接请求报文数目

【相关命令】

·**client-verify protected ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify trusted ip**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display client-verify trusted ip**]命令用来显示客户端验证的IPv4类型的信任IP表项。

【命令】

集中式设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted** **ip** [ *ip-address* [ **vpn** *vpn-instance-name*  ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted** **ip** [ *ip-address* [ **vpn** *vpn-instance-name*  ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted** **ip** [ *ip-address* [ **vpn** *vpn-instance-name*  ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

*[ip-address*]：显示指定IPv4地址的信任IP表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信任IP表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示信任IP表项位于公网。

**[slot** *slot-number*]：显示指定单板上的信任IP表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的信任IP表项。（分布式设备－独立运行模式）。

**[slot** *slot-number*]：显示指定成员设备上的信任IP表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的信任IP表项。（集中式IRF设备）。（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的信任IP表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的信任IP表项。（集中式IRF设备）。（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信任IP表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的信任IP表项。（分布式设备－IRF模式）。（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信任IP表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的信任IP表项。（分布式设备－IRF模式）。（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信任IP表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：仅显示符合指定条件的信任IP表项的个数。

【使用指导】

如果不指定任何参数，则显示所有的IPv4类型的客户端验证信任IP表项。

【举例】

\# 显示所有IPv4类型DNS 客户端验证的信任IP表项。（集中式设备）

\<Sysname\> display client-verify dns trusted ip

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

\# 显示所有IPv4类型DNS 客户端验证的信任IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns trusted ip

Slot 1:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

Slot 2:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.3        vpn1                \--                     1200

\# 显示所有IPv4类型DNS 客户端验证的信任IP表项。（分布式IRF设备）

\<Sysname\> display client-verify dns trusted ip

Slot 1 in chassis 0:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

Slot 2 in chassis 1:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.3        vpn1                \--                     1200

\# 显示所有IPv4类型DNS 客户端验证的信任IP表项的个数。（集中式设备）

\<Sysname\> display client-verify dns trusted ip count

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型DNS 客户端验证的信任IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns trusted ip count

Slot 1:

Totally 3 trusted IP addresses.

Slot 2:

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型DNS 客户端验证的信任IP表项的个数。（分布式IRF设备）

\<Sysname\> display client-verify dns trusted ip count

Slot 1 in chassis 0:

Totally 3 trusted IP addresses.

Slot 2 in chassis 1:

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型HTTP客户端验证的信任IP表项的信息。（集中式设备）

\<Sysname\> display client-verify http trusted ip

Totally 2 trusted addresses.

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

\# 显示所有IPv4类型HTTP客户端验证的信任IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify http trusted ip

Slot 1:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

Slot 2:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

\# 显示所有IPv4类型HTTP客户端验证的信任IP表项。（分布式IRF设备）

\<Sysname\> display client-verify http trusted ip

Slot 1 in chassis 0:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

Slot 2 in chassis 1:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

\# 显示所有IPv4类型HTTP 客户端验证的信任IP表项。（集中式设备）

\<Sysname\> display client-verify http trusted ip count

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型HTTP 客户端验证的信任IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify http trusted ip count

Slot 1:

Totally 3 trusted IP addresses.

Slot 2:

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型HTTP 客户端验证的信任IP表项的个数。（分布式IRF设备）

\<Sysname\> display client-verify http trusted ip count

Slot 1 in chassis 0:

Totally 3 trusted IP addresses.

Slot 2 in chassis 1:

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型的TCP客户端验证的信任IP表项。（集中式设备）

\<Sysname\> display client-verify trusted ip

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                    3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

\# 显示所有IPv4类型的TCP客户端验证的信任IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp trusted ip

Slot 1:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

Slot 2:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

\# 显示所有IPv4类型的TCP客户端验证的信任IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp trusted ip

Slot 1 in chassis 0:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

123.123.123.123 a012345678901234567 1234:1234::1234:1234   3550

Slot 2 in chassis 1:

IP address      VPN instance        DS-Lite tunnel peer    TTL(sec)

11.1.1.2        vpn1                \--                     3600

\# 显示所有IPv4类型TCP 客户端验证的信任IP表项的个数。（集中式设备）

\<Sysname\> display client-verify tcp trusted ip count

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型TCP客户端验证的信任IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp trusted ip count

Slot 1:

Totally 3 trusted IP addresses.

Slot 2:

Totally 3 trusted IP addresses.

\# 显示所有IPv4类型TCP客户端验证的信任IP表项的个数。（分布式IRF设备）

\<Sysname\> display client-verify tcp trusted ip count

Slot 1 in chassis 0:

Totally 3 trusted IP addresses.

Slot 2 in chassis 1:

Totally 3 trusted IP addresses.

表1-17 display client-verify trusted ip命令显示信息描述表

字段

描述

Totally 3 trusted IP addresses

IPv4类型信任IP表项的个数

IP address

信任IPv4地址

VPN instance

信任IP地址所属的MPLS L3VPN实例名称，属于公网时显示为"\--"

DS-Lite tunnel peer

DS-Lite隧道对端地址。DS-Lite组网下，若本设备为AFTR，此列表示报文来自具体的哪个B4，如果不在DS-Lite组网或本设备不为AFTR，则该字段无意义，显示为"\--"

TTL(sec)

信任IP地址的剩余老化时间，单位为秒。若未指定老化时间，则显示"Never"

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- display client-verify trusted ipv6**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display client-verify trusted ipv6**]命令用来显示客户端验证的IPv6类型的信任IP表项。

【命令】

集中式设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted** **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name*  ]  **count**  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted** **ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name*  ]  **slot** *slot-number* [ **cpu** *cpu-number*  ] ]  **count** ]

分布式设备－IRF模式：

**[display client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted ipv6** [ *ipv6-address* [ **vpn** *vpn-instance-name*  ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

*[ipv6-address*]：显示指定IPv6地址的信任IP表项。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信任IP表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示信任IP表项位于公网。

**[slot** *slot-number*]：显示指定单板上的信任IP表项，*slot-number*表示单板所在槽位号。如果不指定该参数，则表示显示所有单板上的信任IP表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信任IP表项，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，则表示显示所有成员设备上的信任IP表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的信任IP表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，则表示显示所有成员设备/PEX上的信任IP表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的信任IP表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，则表示显示所有成员设备上的信任IP表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信任IP表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，则表示显示所有单板上的信任IP表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信任IP表项，*cpu-number*表示单板上的CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：仅显示符合指定条件的信任IP地址的个数。

【使用指导】

如果不指定任何参数，则显示所有IPv6类型的客户端验证的信任IP表项。

【举例】

\# 显示所有IPv6类型的DNS客户端验证的信任IP表项。（集中式设备）

\<Sysname\> display client-verify dns trusted ipv6

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

\# 显示所有IPv6类型的DNS客户端验证的信任IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns trusted ipv6

Slot 1:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

Slot 2:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

\# 显示所有IPv6类型的DNS客户端验证的信任IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify dns trusted ipv6

Slot 1 in chassis 0:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

Slot 2 in chassis 1:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

\# 显示所有IPv6类型的DNS客户端验证的信任IP表项的个数。（集中式设备）

\<Sysname\> display client-verify dns trusted ipv6 count

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型的DNS客户端验证的信任IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify dns trusted ipv6 count

Slot 1:

Totally 3 trusted IPv6 addresses.

Slot 2:

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型的DNS客户端验证的信任IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify dns trusted ipv6 count

Slot 1 in chassis 0:

Totally 3 trusted IPv6 addresses.

Slot 2 in chassis 1:

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型HTTP客户端验证的信任IP表项。（集中式设备）

\<Sysname\> display client-verify http trusted ipv6

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

\# 显示所有IPv6类型HTTP客户端验证的信任IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify http trusted ipv6

Slot 1:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

Slot 2:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

\# 显示所有IPv6类型HTTP客户端验证的信任IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify http trusted ipv6

Slot 1 in chassis 0:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

Slot 2 in chassis 1:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

\# 显示所有IPv6类型的HTTP客户端验证的信任IP表项的个数。（集中式设备）

\<Sysname\> display client-verify http trusted ipv6 count

IPv6 address                            VPN instance     TTL(sec)

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型的HTTP客户端验证的信任IP表项的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify http trusted ipv6 count

Slot 1:

Totally 3 trusted IPv6 addresses.

Slot 2:

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型的HTTP客户端验证的信任IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify http trusted ipv6 count

Slot 1 in chassis 0:

Totally 3 trusted IPv6 addresses.

Slot 2 in chassis 1:

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型TCP客户端验证的信任IP表项。（集中式设备）

\<Sysname\> display client-verify tcp trusted ipv6

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

\# 显示所有IPv6类型TCP客户端验证的信任IP表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp trusted ipv6

Slot 1:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

Slot 2:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

\# 显示所有IPv6类型TCP客户端验证信任IP表项。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp trusted ipv6

Slot 1 in chassis 0:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

1234::1234                              a012345678901234 1234

Slot 2 in chassis 1:

IPv6 address                            VPN instance     TTL(sec)

1::3                                    vpn1             1643

\# 显示所有IPv6类型的TCP客户端验证的信任IP表项的个数。（集中式设备）

\<Sysname\> display client-verify tcp trusted ipv6 count

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型的TCP客户端验证的信任IP地址的个数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display client-verify tcp trusted ipv6 count

Slot 1:

Totally 3 trusted IPv6 addresses.

Slot 2:

Totally 3 trusted IPv6 addresses.

\# 显示所有IPv6类型的TCP客户端验证的信任IP表项的个数。（分布式设备－IRF模式）

\<Sysname\> display client-verify tcp trusted ipv6 count

Slot 1 in chassis 0:

Totally 3 trusted IPv6 addresses.

Slot 2 in chassis 1:

Totally 3 trusted IPv6 addresses.

表1-18 display client-verify trusted ipv6命令显示信息描述表

字段

描述

Totally 3 trusted IPv6 addresses

IPv6类型信任IP表项的个数

IPv6 address

信任IPv6地址

TTL(sec)

信任IP地址的剩余老化时间，单位为秒。若未指定老化时间，则显示"Never"

VPN instance

VPN实例名称，属于公网时显示为"\--"

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood action**

------------------------------------------------------------------------

**[dns-flood action**]命令用来配置对DNS flood攻击防范的全局处理行为。

**[undo dns-flood action**]命令用来恢复缺省情况。

【命令】

**[dns-flood action**[ { **client-verify** \| **drop** \| **logging** } \*]]

**[undo dns-flood action**]

【缺省情况】

不对检测到的DNS flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到DNS客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有DNS报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用需要和TCP客户端验证功能配合。使能了DNS客户端验证的接口检测到DNS flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\# 在攻击防范策略atk-policy-1中配置对DNS flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 dns-flood action drop

【相关命令】

·**dns-flood ****detect**

·**dns-flood detect non-specific**

·**dns-flood ****threshold**

·**client-verify ****dnsenable**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood detect**

------------------------------------------------------------------------

**[dns-flood detect**]命令用来开启对指定IP地址的攻击防范检测，并配置DNS flood攻击防范检测的触发阈值和对DNS flood攻击的处理行为。

**[undo dns-flood detect**]命令用来取消对指定IP地址的DNS flood攻击防范检测。

【命令】

**[dns-flood detect **[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **port** *port-list*   **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo dns-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置DNS flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[port** *port-list*]：指定开启DNS flood攻击防范检测的端口列表，表示方式为{ *start-port-number* [ **to** *end-port-number*  } &\<1-65535\>]。&\<1-65535\>表示前面的参数最多可以输入65535次。*end-port-number*必须大于或等于*start-port-number*。若不指定该参数，则表示使用全局配置的检测端口列表。

**[threshold*** threshold-value*]：指定DNS flood攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的DNS报文数目，取值范围为1～1000000。

**[action**]：设置对DNS flood攻击的处理行为。

**[client-verify**]：表示自动将受到攻击的IP地址添加到DNS客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有DNS报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置DNS flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能DNS flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送DNS报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了DNS flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的DNS flood攻击防范检测，并指定检测端口为53、触发阈值为2000。当设备监测到向该IP地址的53端口每秒发送的DNS报文数持续达到或超过2000时，启动DNS flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 dns-flood detect ip 192.168.1.2 port 53 threshold 2000

【相关命令】

·**dns-flood action**

·**dns-flood detect non-specific**

·**dns-flood ****threshold**

·**dns-flood ****port**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood detect non-specific**

------------------------------------------------------------------------

**[dns-flood detect non-specific**]命令用来对所有非受保护IP地址开启DNS flood攻击防范检测。

**[undo dns-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[dns-flood detect non-specific**]

**[undo dns-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启DNS flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IP地址开启DNS flood攻击防范检测后，设备将采用全局的阈值设置（由**dns-flood threshold**命令设置）和处理行为（由**dns-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启DNS flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 dns-flood detect non-specific

【相关命令】

·**dns-flood action**

·**dns-flood ****detect**

·**dns****-flood threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood port**

------------------------------------------------------------------------

**[dns-flood port**]命令用来配置DNS flood攻击防范的全局检测端口号。

**[undo dns-flood port**]命令用来恢复缺省情况。

【命令】

**[dns-flood port***port-list*]

**[undo dns-flood port**]

【缺省情况】

DNS flood攻击防范的全局检测端口号为53。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-list*]：指定开启DNS flood攻击防范检测的端口列表，表示方式为{ *start-port-number* [ **to** *end-port-number*  } &\<1-65535\>]。&\<1-65535\>表示前面的参数最多可以输入65535次。*end-port-number*必须大于或等于*start-port-number*。

【使用指导】

设备只对指定检测端口上收到的报文进行DNS flood攻击检测。

对于所有非受保护IP地址，或未指定检测端口的受保护IP地址，设备采用全局的检测端口进行DNS flood攻击检测。对于所有指定检测端口的受保护IP地址，设备针对为每个受保护IP地址指定的端口进行DNS flood攻击检测。

【举例】

\# 在攻击防范策略atk-policy-1中配置DNS flood攻击防范的全局检测端口为53与61000，当设备检测到访问53端口或61000端口的DNS flood攻击时，启动攻击防范措施。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 dns-flood port 53 61000

【相关命令】

·**dns-flood action**

·**dns-flood ****detect**

·**dns-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- dns-flood threshold**

------------------------------------------------------------------------

**[dns-flood threshold**]命令用来配置DNS flood攻击防范的全局触发阈值。

**[undo dns-flood threshold**]命令用来恢复缺省情况。

【命令】

**[dns-flood threshold*** threshold-value*]

**[undo dns-flood threshold**]

【缺省情况】

DNS flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的DNS报文数目，取值范围为1～1000000。使能DNS flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送DNS报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了DNS flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置DNS flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（DNS服务器）的DNS报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置DNS flood攻击防范的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的DNS报文数持续达到或超过100时，启动攻击防范措施。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 dns-flood threshold 100

【相关命令】

·**dns-flood action**

·**dns-flood ****detect ip**

·**dns-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- exempt acl**

------------------------------------------------------------------------

**[exempt acl**]命令用来配置攻击防范例外列表。

**[undo exempt acl**]命令用来恢复缺省情况。

【命令】

**[exempt acl **[ **ipv6**  { *acl-number* \| **name** *acl-name* }]]

**[undo exempt acl ** **ipv6** ]

【缺省情况】

应用了攻击防范策略的接口接收到的所有报文都需要进行攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定IPv6 ACL。如果没有指定本参数，则表示IPv4 ACL。

*[acl-number*]：指定ACL的编号。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：若未指定**ipv6**关键字，表示IPv4基本ACL；否则表示IPv6基本ACL。

·3000～3999：若未指定**ipv6**关键字，表示IPv4高级ACL；否则表示IPv6高级ACL。

**[name** *acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，ACL的名称不允许使用英文单词all。

【使用指导】

通过配置例外列表，使用ACL过滤不需要进行攻击防范检测的主机报文。当接口上收到的报文与攻击防范例外列表引用的ACL中的permit规则匹配时，设备不对其进行攻击防范检测。该配置用于过滤某些被信任的安全主机发送的报文，可以有效的减小误报率，并提高服务器处理效率。

需要注意的是：

·例外列表引用的ACL的permit规则中仅源地址、目的地址、源端口、目的端口、协议号、L3VPN和非首片分片标记参数用于匹配报文。

·如果配置的攻击防范例外列表中引用的ACL不存在，或引用的ACL中未定义任何规则，例外列表不会生效。

【举例】

\# 在攻击防范策略atk-policy-1中配置例外列表ACL 2001，过滤来自主机1.1.1.1的报文，不对其进行攻击防范检测。

\<Sysname\> system-view

Sysname acl number 2001 name acl_1

Sysname-acl-basic-2001 rule permit source 1.1.1.1 0

Sysname-acl-basic-2001 quit

Sysname attack-defense policy atk-policy-1

attack-defense-policy-atk-policy-1 exempt acl name acl_1

【相关命令】

·**attack-defense policy**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood action**

------------------------------------------------------------------------

**[fin-flood action**]命令用来配置对FIN flood攻击防范的全局处理行为。

**[undo fin-flood action**]命令用来恢复缺省情况。

【命令】

**[fin-flood action**[ { **client-verify** \| **drop** \| **logging** } \*]]

**[undo fin-flood action**]

【缺省情况】

不对检测到的FIN flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有FIN报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用需要和TCP客户端验证功能配合。使能了TCP客户端验证的接口检测到ACK flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\#在攻击防范策略atk-policy-1配置对FIN flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 fin-flood action drop

【相关命令】

·**client-verify ****tcp enable**

·**fin-flood ****detect**

·**fin-flood detect non-specific**

·**fin-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood detect**

------------------------------------------------------------------------

**[fin-flood detect**]命令用来开启对指定IP地址的FIN flood攻击防范检测，并配置FIN flood攻击防范检测的触发阈值和对FIN flood攻击的处理行为。

**[undo fin-flood detect**]命令用来取消对指定IP地址的FIN flood攻击防范检测。

【命令】

**[fin-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo fin-flood detect**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置FIN flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold*** threshold-value*]：指定攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的FIN报文数目，取值范围为1～1000000。

**[action**]：设置对FIN flood攻击的处理行为。

**[client-verify**]：表示当自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有FIN报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置FIN flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能FIN flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送FIN报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了FIN flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的FIN flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的FIN报文数持续达到或超过2000时，启动FIN flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 fin-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**fin-flood action**

·**fin-flood detect non-specific**

·**fin-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood detect non-specific**

------------------------------------------------------------------------

**[fin-flood detect non-specific**]命令用来对所有非受保护IP地址开启FIN flood攻击防范检测。

**[undo fin-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[fin-flood detect non-specific**]

**[undo fin-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启FIN flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【使用指导】

对所有非受保护IP地址开启FIN flood攻击防范检测后，设备将采用全局的阈值设置（由**fin-flood threshold**命令设置）和处理行为（由**fin-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启FIN flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 fin-flood detect non-specific

【相关命令】

·**fin-flood action**

·**fin-flood ****detect**

·**fin-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- fin-flood threshold**

------------------------------------------------------------------------

**[fin-flood threshold**]命令用来配置FIN flood攻击防范的全局触发阈值。

**[undo fin-flood threshold**]命令用来恢复缺省情况。

【命令】

**[fin-flood threshold***threshold-value*]

**[undo fin-flood threshold**]

【缺省情况】

FIN flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的FIN报文数目，取值范围为1～1000000。使能FIN flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送FIN报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了FIN flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置FIN flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的FIN报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置FIN flood攻击防范检测的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的FIN报文数持续达到或超过100时，启动FIN flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 fin-flood threshold 100

【相关命令】

·**fin-flood action**

·**fin-flood ****detect **

·**fin-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood action**

------------------------------------------------------------------------

**[http-flood action**]命令用来配置对HTTP flood攻击防范的全局处理行为。

**[undo http-flood action**]命令用来恢复缺省情况。

【命令】

**[http-flood action**[ { **client-verify** \| **drop** \| **logging** } \*]]

**[undo http-flood action**]

【缺省情况】

不对检测到的HTTP flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到HTTP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有HTTP报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用需要和HTTP客户端验证功能配合。使能了HTTP客户端验证的接口检测到HTTP flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\# 在攻击防范策略atk-policy-1中配置对HTTP flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 http-flood action drop

【相关命令】

·**client-verify ****httpenable**

·**http-flood detect non-specific**

·**http-flood****detect**

·**http-flood****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood detect**

------------------------------------------------------------------------

**[http-flood detect**]命令用来开启对指定IP地址的HTTP flood攻击防范检测，并配置HTTP flood攻击防范的触发阈值和对HTTP flood攻击的处理行为。

**[undo http-flood detect**]命令用来取消对指定IP地址的HTTP flood攻击防范检测。

【命令】

**[http-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **port** *port-list*   **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo http-flood detect **[{ **ip** *ip-address* **\| ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置HTTP flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[port** *port-list*]：指定开启HTTP flood攻击防范检测的端口列表，表示方式为{ *start-port-number* [ **to** *end-port-number*  } &\<1-65535\>]。&\<1-65535\>表示前面的参数最多可以输入65535次。*end-port-number*必须大于或等于*start-port-number*。若不指定该参数，则表示使用全局配置的检测端口列表。

**[threshold***threshold-value*]：指定攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的HTTP报文数目，取值范围为1～1000000。

**[action**]：设置对HTTP flood攻击的处理行为。

**[client-verify**]：表示自动将受到攻击的IP地址添加到HTTP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有HTTP报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置HTTP flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能HTTP flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送HTTP报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了HTTP flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的HTTP flood攻击防范检测，并指定检测端口为80与8080、触发阈值为2000。当设备监测到向该IP地址的80或8080端口每秒发送的HTTP报文数持续达到或超过2000时，启动HTTP flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 http-flood detect ip 192.168.1.2 port 80 8080 threshold 2000

【相关命令】

·**http-flood action**

·**http-flood detect non-specific**

·**http-flood ****threshold**

·**http-flood ****port**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood detect non-specific**

------------------------------------------------------------------------

**[http-flood detect non-specific**]命令用来对所有非受保护IPv4地址开启HTTP flood攻击防范检测。

**[undo http-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[http-flood detect non-specific**]

**[undo http-flood detect non-specific**]

【缺省情况】

未对任何非受保护IP地址开启HTTP flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IP地址开启HTTP flood攻击防范检测后，设备将采用全局的阈值设置（由**http-flood threshold**命令设置）和处理行为（由**http-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启HTTP flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 http-flood detect non-specific

【相关命令】

·**http-flood action**

·**http-flood ****detect**

·**http-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood port**

------------------------------------------------------------------------

**[http-flood port**]命令用来配置HTTP flood攻击防范的全局检测端口号。

**[undo http-flood port**]命令用来恢复缺省情况。

【命令】

**[http-flood port***port-list*]

**[undo http-flood port**]

【缺省情况】

HTTP flood攻击防范的全局检测端口号为80。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-list*]：指定开启HTTP flood攻击防范检测的端口列表，表示方式为{ *start-port-number* [ **to** *end-port-number*  } &\<1-65535\>]。&\<1-65535\>表示前面的参数最多可以输入65535次。*end-port-number*必须大于或等于*start-port-number*。

【使用指导】

设备只对指定检测端口上收到的报文进行HTTP flood攻击检测。

对于所有非受保护IP地址，或未指定检测端口的受保护IP地址，设备采用全局的检测端口进行HTTP flood攻击检测。对于所有指定检测端口的受保护IP地址，设备针对为每个受保护IP地址指定的端口进行HTTP flood攻击检测。

【举例】

\# 在攻击防范策略atk-policy-1中配置DNS flood攻击防范的全局检测端口为80与8080，当设备检测到访问80端口或8080端口的HTTP flood攻击时，启动攻击防范措施。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 http-flood port 80 8080

【相关命令】

·**http-flood action**

·**http-flood ****detect**

·**http-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- http-flood threshold**

------------------------------------------------------------------------

**[http-flood threshold**]命令用来配置HTTP flood攻击防范的全局触发阈值。

**[undo http-flood threshold**]命令用来恢复缺省情况。

【命令】

**[http-flood threshold***threshold-value*]

**[undo http-flood threshold**]

【缺省情况】

缺省情况下，HTTP flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的HTTP报文数目，取值范围为1～1000000。使能HTTP flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送HTTP报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了HTTP flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置HTTP flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器）的HTTP报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置HTTP flood攻击防范的全局触发阈值为100， 即当设备监测到向某IP地址每秒发送的HTTP报文数持续达到或超过100时，启动HTTP flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 http-flood threshold 100

【相关命令】

·**http-flood action**

·**http-flood ****detect**

·**http-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood action**

------------------------------------------------------------------------

**[icmp-flood action**]命令用来配置对ICMP flood攻击防范的全局处理行为。

**[undo icmp-flood action**]命令用来恢复缺省情况。

【命令】

**[icmp-flood action **[{ **drop** \| **logging** } **\***]]

**[undo icmp-flood action**]

【缺省情况】

不对检测到的ICMP flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有ICMP报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【举例】

\# 在攻击防范策略atk-policy-1中配置对ICMP flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmp-flood action drop

【相关命令】

·**icmp-flood detect non-specific**

·**icmp-flood ****detect ip**

·**icmp-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood detect ip**

------------------------------------------------------------------------

**[icmp-flood detect ip**]命令用来开启对指定IP地址的ICMP flood攻击防范检测，并配置ICMP flood攻击防范检测的触发阈值和对ICMP flood攻击的处理行为。

**[undo icmp-flood detect ip**]命令用来取消对指定IP地址的ICMP flood攻击防范检测。

【命令】

**[icmp-flood detect** **ip** *ip-address* [ **vpn-instance** *vpn-instance-name*   **threshold** *threshold-value*  [ **action** { { **drop** \| **logging** } \* \| **none** } ]]]

**[undo icmp-flood detect ip ***ip-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

未对任何指定IP地址配置ICMP flood 攻击防范触发阈值。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold***threshold-value*]：指定攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的ICMP报文数目，取值范围为1～1000000。

**[action**]：设置对ICMP flood攻击的处理行为。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有ICMP报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置ICMP flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能ICMP flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送ICMP报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了ICMP flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的ICMP flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的ICMP报文数持续达到或超过2000时，启动ICMP flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmp-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**icmp-flood action**

·**icmp-flood ****threshold**

·**icmp-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood detect non-specific**

------------------------------------------------------------------------

**[icmp-flood detect non-specific**]命令用来对所有非受保护IPv4地址开启ICMP flood攻击防范检测。

**[undo icmp-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[icmp-flood detect non-specific**]

**[undo icmp-flood detect non-specific**]

【缺省情况】

未对任何非受保护IPv4地址开启ICMP flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对任何非受保护IPv4地址开启ICMP flood攻击防范检测后，设备将采用全局的阈值设置（由**icmp-flood threshold**命令设置）和处理行为（由**icmp-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IPv4地址开启ICMP flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmp-flood detect non-specific

【相关命令】

·**icmp-flood action**

·**icmp-flood detect ip**

·**icmp-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmp-flood threshold**

------------------------------------------------------------------------

**[icmp-flood threshold**]命令用来配置ICMP flood攻击防范的全局触发阈值。

**[undo icmp-flood threshold**]命令用来恢复缺省情况。

【命令】

**[icmp-flood threshold***threshold-value*]

**[undo icmp-flood threshold**]

【缺省情况】

ICMP flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的ICMP报文数目，取值范围为1～1000000。使能ICMP flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送ICMP报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了ICMP flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置ICMP flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的ICMP报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置ICMP flood攻击防范检测的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的ICMP报文数持续达到或超过100时，启动ICMP flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmp-flood threshold 100

【相关命令】

·**icmp-flood action**

·**icmp-flood ****detect**

·**icmp-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood action**

------------------------------------------------------------------------

**[icmpv6-flood action**]命令用来配置对ICMPv6 flood攻击防范的全局处理行为。

**[undo icmpv6-flood action**]命令用来恢复缺省情况。

【命令】

**[icmpv6-flood action **[{ **drop** \| **logging** } **\***]]

**[undo icmpv6-flood action**]

【缺省情况】

不对检测到的ICMPv6 flood攻击采取任何防范措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有ICMPv6报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【举例】

\# 在攻击防范策略atk-policy-1中配置对ICMPv6 flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmpv6-flood action drop

【相关命令】

·**icmpv6-flood ****detect ipv6**

·**icmpv6-flood detect non-specific**

·**icmpv6-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood detect ipv6**

------------------------------------------------------------------------

**[icmpv6-flood detect ipv6**]命令用来开启对指定IPv6地址的ICMPv6 flood攻击防范检测，并配置ICMPv6 flood攻击防范检测的触发阈值和对ICMPv6 flood攻击的处理行为。

**[undo icmpv6-flood detect ipv6**]命令用来取消对指定IPv6地址的ICMPv6 flood攻击防范检测。

【命令】

**[icmpv6-flood detect ipv6 ***ipv6-address* [ **vpn-instance** *vpn-instance-name*   **threshold** *threshold-value*  [ **action** { { **drop** \| **logging** } \* \| **none** } ]]]

**[undo icmpv6-flood detect ipv6 ***ipv6-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

未对任何指定IP地址配置ICMPv6 flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold***threshold-value*]：指定攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的ICMPv6报文数目，取值范围为1～1000000。

**[action**]：设置对ICMPv6 flood攻击的处理行为。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有ICMPv6报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IPv6地址配置ICMPv6 flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能ICMPv6 flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送ICMPv6报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了ICMPv6 flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址2012::12的ICMPv6 flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的ICMP报文数持续达到或超过2000时，启动ICMPv6 flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmpv6-flood detect ipv6 2012::12 threshold 2000

【相关命令】

·**icmpv6-flood action**

·**icmpv6-flood detect non-specific**

·**icmpv6-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood detect non-specific**

------------------------------------------------------------------------

**[icmpv6-flood detect non-specific**]命令用来对所有非受保护IPv6地址开启ICMPv6 flood攻击防范检测。

**[undo icmpv6-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[icmpv6-flood detect non-specific**]

**[undo icmpv6-flood detect non-specific**]

【缺省情况】

未对所有非受保护IPv6地址开启ICMPv6 flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IPv6地址开启ICMPv6 flood攻击防范检测后，设备将采用全局的阈值设置（由**icmpv6-flood threshold**命令设置）和处理行为（由**icmpv6-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IPv6地址开启ICMPv6 flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmpv6-flood detect non-specific

【相关命令】

·**icmpv6-flood action**

·**icmpv6-flood ****detect ipv6**

·**icmpv6-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- icmpv6-flood threshold**

------------------------------------------------------------------------

**[icmpv6-flood threshold**]命令用来配置ICMPv6 flood攻击防范的全局触发阈值。

**[undo icmpv6-flood threshold**]命令用来恢复缺省情况。

【命令】

**[icmpv6-flood threshold*** threshold-value*]

**[undo icmpv6-flood threshold**]

【缺省情况】

ICMPv6 flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的ICMPv6报文数目，取值范围为1～1000000。使能ICMPv6 flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送ICMPv6报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了ICMPv6 flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置ICMPv6 flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的ICMPv6报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置ICMPv6 flood攻击防范检测的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的ICMPv6报文数持续达到或超过100时，启动ICMPv6 flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 icmpv6-flood threshold 100

【相关命令】

·**icmpv6****-flood action**

·**icmpv6****-flooddetect**

·**icmpv6-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset attack-defense policy flood**

------------------------------------------------------------------------

**[reset attack-defense policy flood**]命令用来清除flood攻击防范受保护IP表项的统计信息。

【命令】

**[reset attack-defense policy ***policy-name*** flood protected **[{ **ip** \| **ipv6** } **statistics**]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：攻击防范策略名称，为1～31个字符的字符串，不区分大小写。合法取值包括大写字母、小写字母、数字、特殊字符"\_"和"-"。

**[ip**]：指定IPv4类型的flood受保护IP表项。

**[ipv6**]：指定IPv6类型的flood受保护IP表项。

**[statistics**]：清除指定类型的flood受保护IP表项的统计信息。

【举例】

\# 清除攻击防范策略abc中所有IPv4类型的flood保护IP表项的统计信息

\<Sysname\> reset attack-defense policy abc flood protected ip statistics

\# 清除攻击防范策略abc中所有IPv6类型的Flood保护IP表项的统计信息

\<Sysname\> reset attack-defense policy abc flood protected ipv6 statistics

【相关命令】

·**display attack-defense policy ip**

·**display attack-defense policy ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset attack-defense statistics interface**

------------------------------------------------------------------------

**[reset attack-defense statistics interface**]命令用来清除接口上的攻击防范统计信息。

【命令】

**[reset attack-defense statistics interface** *interface-type interface-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：表示指定接口的接口类型和接口编号[。]

【使用指导】

本命令会将指定接口上攻击防范的所有统计信息清零。

【举例】

\# 清除接口GigabitEthernet1/0/1上的攻击防范的统计信息。

\<Sysname\> reset attack-defense statistics interface gigabitethernet 1/0/1

【相关命令】

·**d****isplay attack-defense policy**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset attack-defense statistics local**

------------------------------------------------------------------------

**[reset attack-defense statistics local**]命令用来清除本机攻击防范的统计信息。

【命令】

**[reset attack-defense statistics local**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 清除本机上所有攻击防范的统计信息。

\<Sysname\> reset attack-defense statistics local

【相关命令】

·**d****isplay attack-defense statistics local**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset blacklist ip**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset blacklist ip**]命令用来清除IPv4动态黑名单表项。

【命令】

**[reset blacklist** **ip** { *source-ip-address* [ **vpn-instance** *vpn-instance-name*   **ds-lite-peer** *ds-lite-peer-address*  \| **all** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[source-ip-address*]：清除指定IPv4地址的动态黑名单表项。其中*source-ip-address*表示黑名单表项的IPv4地址。

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的动态黑名单表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示清除公网中的指定动态黑名单表项。

**[ds-lite-peer** *ds-lite-peer-address*]：清除黑名单所属的DS-Lite隧道对端地址。其中，*ds-lite-peer-address*表示黑名单的IPv4地址所属的DS-Lite隧道B4端IPv6地址。若不指定该参数，则表示清除公网中的的指定动态黑名单表项。

**[all**]：表示清除所有动态IPv4的黑名单表项。

【使用指导】

该命令仅用来清除动态生成的IPv4的黑名单表项。用户添加的黑名单表项需要通过**undo blacklist ip**命令来删除。

【举例】

\# 清除所有IPv4动态黑名单表项的信息。

\<Sysname\> reset blacklist ip all

【相关命令】

·**display blacklist ip**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset blacklist ipv6**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset blacklist ipv6**]命令用来清除IPv6动态黑名单表项。

【命令】

**[reset blacklist** **ipv6** { *source-ipv6-address* [ **vpn-instance** *vpn-instance-name*  \| **all** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[source-ipv6-address*]：清除指定IPv6地址的动态黑名单表项。其中*source-ip-address*表示黑名单表项的IPv6地址。

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的动态黑名单表项。其中*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示清除公网中的指定动态黑名单表项。

**[all**]：表示清除所有动态IPv6的黑名单表项。

【使用指导】

该命令仅用来清除动态生成的IPv6的黑名单表项。用户添加的黑名单表项需要通过**undo blacklist ipv6**命令来删除。

【举例】

\# 清除所有IPv6动态黑名单表项的信息。

\<Sysname\> reset blacklist ipv6 all

【相关命令】

·**display blacklist ip****v6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset blacklist statistics**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset blacklist statistics**]命令用来清除黑名单表项的统计信息。

【命令】

**[reset blacklist statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

执行本命令后，将清空所有黑名单表项的丢包统计信息。

【举例】

\# 清除所有黑名单表项的丢包统计信息。

\<Sysname\> reset blacklist statistics

【相关命令】

·**display blacklist ip**

·**display blacklist ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset client-verify protected statistics**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset client-verify protected statistics**]命令用来清除客户端验证的受保护IP地址的统计信息。

【命令】

**[reset client-verify **[{ **dns** \| **http** \| **tcp** } ]**protected **[{ **ip** \| **ipv6** } **statistics**]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

**[ip**]：清除所有IPv4类型客户端验证的受保护IP地址的统计信息。

**[ipv6**]：清除所有IPv6类型客户端验证的受保护IP地址的统计信息。

【举例】

\# 清除TCP客户端验证的受保护IP地址的统计信息。

\<Sysname\> **reset client-verify tcp protected ip** statistics

【相关命令】

·**display client-verify ****protected ip**

·**display client-verify ****protected ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- reset client-verify trusted**

------------------------------------------------------------------------

![说明](攻击检测与防范命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset client-verify trusted**]命令用来清除客户端验证的信任IP表项。

【命令】

**[reset client-verify **[{ **dns** \| **http** \| **tcp** } ]**trusted **[{ **ip** \| **ipv6** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dns**]：指定DNS客户端验证功能。

**[http**]：指定HTTP客户端验证功能。

**[tcp**]：指定TCP客户端验证功能。

**[ip**]：清除所有IPv4类型客户端验证的信任IP表项。

**[ipv6**]：清除所有IPv6类型客户端验证的信任IP表项。

【举例】

\# 清除所有IPv4类型DNS客户端验证的信任IP表项。

\<Sysname\> reset client-verify dns trusted ip

【相关命令】

·**display client-verify ****trusted ip**

·**display client-verify ****trusted ipv6**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood action**

------------------------------------------------------------------------

**[rst-flood action**]命令用来配置对RST flood攻击防范的全局处理行为。

**[undo rst-flood action**]命令用来恢复缺省情况。

【命令】

**[rst-flood action **[[ **client-verify** \| **drop** \| **logging** } \*]]

**[undo rst-flood action**]

【缺省情况】]

不对检测到的RST flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有RST报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用需要和TCP客户端验证功能配合。使能了TCP客户端验证的接口检测到ACK flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\# 在攻击防范策略atk-policy-1中配置对RST flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 rst-flood action drop

【相关命令】

·**client-verify ****tcpenable**

·**rst-flood ****detect**

·**rst-flood detect non-specific**

·**rst-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood detect**

------------------------------------------------------------------------

**[rst-flood detect**]命令用来开启对指定IP地址的RST flood攻击防范检测，并配置RST flood攻击防范的触发阈值和对RST flood攻击的处理行为。

**[undo rst-flood**]命令用来取消对指定IP地址的RST flood攻击防范检测。

【命令】

**[rst-flood detect **[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo rst-flood detect **[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置RST flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold***threshold-value*]：指定攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的RST报文数目，取值范围为1～1000000。

**[action**]：设置对RST flood攻击的处理行为。

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有RST报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置RST flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能RST flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送RST报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了RST flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的RST flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的RST报文数持续达到或超过2000时，启动RST flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 rst-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**rst-flood action**

·**rst-flood detect non-specific**

·**rst-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood detect non-specific**

------------------------------------------------------------------------

**[rst-flood detect non-specific**]命令用来对所有非受保护IP地址开启RST flood攻击防范检测。

**[undo rst-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[rst-flood detect non-specific**]

**[undo rst-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启RST flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IP地址开启RST flood攻击防范检测后，设备将采用全局的阈值设置（由**rst-flood threshold**命令设置）和处理行为（由**rst-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启RST flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 rst-flood detect non-specific

【相关命令】

·**rst-flood action**

·**rst-flood detect**

·**rst-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- rst-flood threshold**

------------------------------------------------------------------------

**[rst-flood threshold**]命令用来配置RST flood攻击防范的全局触发阈值。

**[undo rst-flood threshold**]命令用来恢复缺省情况。

【命令】

**[rst-flood threshold***threshold-value*]

**[undo rst-flood threshold**]

【缺省情况】

RST flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的RST报文数目，取值范围为1～1000000。使能RST flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送RST报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了RST flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置RST flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的RST报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置RST flood攻击防范检测的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的RST报文数持续达到或超过100时，启动RST flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 rst-flood threshold 100

【相关命令】

·**rst-flood action**

·**rst-flood ****detect**

·**rst-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- scan detect**

------------------------------------------------------------------------

**[scan detect**]命令用来配置开启指定级别的扫描攻击防范。

**[undo scan detect**]命令用来恢复缺省情况。

【命令】

**[scan detect level **[{ **high** \| **low** \| **medium** } **action** **[[ **timeout** *minutes* ] \| **drop** } \| **logging** } \*]]

**[undo scan detect level **[{ **high** \| **low** \| **medium** }]]

【缺省情况】]

扫描攻击防范处于关闭状态。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level**]：指定攻击防范的检测级别。

**[low**]：表示低防范级别，该级别提供基本的扫描攻击检测，有很低的误报率，但对于一些扫描攻击类型不能检出。

**[high**]：表示高防范级别，该级别能检测出大部分的扫描攻击，但对活跃主机误报率较高，即将可提供服务的主机的报文错误判断为攻击报文的概率比较高。

**[medium**]：表示中防范级别，该级别有适中的攻击检出率与误报率，通常能够检测出Filtered Scan等攻击。

**[action**]：设置对扫描攻击的处理行为。

**[block-source**]：表示阻断并丢弃来自该IP地址的后续报文。具体实现是，当设备检测到攻击发生后，会自动将发起攻击的源IP地址添加到黑名单动态表项中，当接口上的黑名单过滤功能处于开启状态时，来自该IP地址的报文将被丢弃。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[timeout ***minutes*]：动态添加的黑名单表项的老化时间。其中，*minutes*表示老化时间，取值范围为1～1000，单位为分钟，缺省值为10。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，由该攻击者发送的报文都将被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成记录告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

要使扫描攻击防范添加的黑名单动态表项生效，必须保证接口上的黑名单过滤功能处于开启状态。

【举例】

\# 在攻击防范策略atk-policy-1中配置扫描攻击的检测级别为低级别，处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 scan detect level low action drop

\# 在攻击防范策略atk-policy-1中配置扫描攻击的检测级别为低级别，处理行为是发日志，阻断并丢弃来自该IP地址的后续报文，并设置添加的黑名单表项的老化时间为10分钟。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 scan detect level low action logging block-source timeout 10

【相关命令】

·**blacklist enable**

·**blacklist global enable**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature { large-icmp \| large-icmpv6 } max-length**

------------------------------------------------------------------------

**[signature **]**[ large-icmp****[\| **large-icmpv6** ]}** max-length**命令用来配置启动Large ICMP攻击防范的ICMP报文长度的最大值。

**[undo signature level detect**]命令用来恢复缺省情况。

【命令】]

**[signature **]**[ large-icmp****[\| **large-icmpv6** ]}** max-length ***length*

**[undo signature **]**[ large-icmp ****[\| **large-icmpv6** ]}** max-length**

【缺省情况】]

ICMP]报文和ICMPv6报文长度的最大值均为4000字节。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[large-icmp**]：表示超大ICMP报文攻击防范。

**[large-icmpv6**]：表示超大ICMPv6报文攻击防范。

*[length*]：表示ICMP报文长度的最大值，ICMP报文取值范围为28～65534，ICMPv6报文取值范围为48～65534，单位为字节。

【举例】

\# 在攻击防范策略atk-policy-1中配置启动Large ICMP攻击防范的ICMP报文长度的最大值为50000字节。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 signature large-icmp max-length 50000

【相关命令】

·**signature ****detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature detect**

------------------------------------------------------------------------

**[signature detect**]命令用来开启指定类型单包攻击报文的特征检测，并设置攻击防范的处理行为。

**[undo signature detect**]命令用来取消对指定类型的单包攻击报文的特征检测。

【命令】

**[signature** **detect** **fragment**[ \| **impossible** \| ]**ip-option-abnormal**[ \| **land**]****[\|]**large-icmp**[ \| **large-icmpv6** \| **ping-of-death** \| **smurf** \|]** snork**[ \| **tcp-all-flags** \| **tcp-fin-only** \| **tcp-invalid-flags** \| **tcp-null-flag** \| **tcp-syn-fin**]****[\| ]**teardrop**[ \| **tiny-fragment** \| **traceroute** \|]**udp-bomb**[ \| **winnuke** } [ **action** { { **drop** \| **logging** } \* \| **none** } ]]

**[undo signature** **detect** **fragment**[ \| **impossible** \| ]**ip-option-abnormal**[ \| **land**]****[\|]**large-icmp**[ \| **large-icmpv6** \| **ping-of-death** \| **smurf** \|]** snork**[ \| **tcp-all-flags** \| **tcp-fin-only** \| **tcp-invalid-flags** \| **tcp-null-flag** \| **tcp-syn-fin**]****[\| ]**teardrop**[ \| **tiny-fragment** \| **traceroute** \|]**udp-bomb**[ \| **winnuke** }]

**[signature detect**]**icmp-type **[[ \| ]**address-mask-reply **[\| ]**address-mask-request **[\| ]**destination-unreachable **[\| ]**echo-reply **[\| ]**echo-request **[\|]** information-reply **[\|]** information-request **[\|]** parameter-problem **[\|]** redirect **[\|]** source-quench **[\| ]**time-exceeded **[\|]** timestamp-reply **[\|]** timestamp-request **} [[ **action** { { **drop** \| **logging** } \* \| **none** } ]]

**[undo signature detect**]**icmp-type **[[ \| ]**address-mask-reply **[\| ]**address-mask-request **[\| ]**destination-unreachable **[\| ]**echo-reply **[\| ]**echo-request **[\|]** information-reply **[\|]** information-request **[\|]** parameter-problem **[\|]** redirect **[\|]** source-quench **[\| ]**time-exceeded **[\|]** timestamp-reply **[\|]** timestamp-request** }

**[signature detect**]**icmpv6-type **[[ \| ]**destination-unreachable **[\|]** echo-reply **[\|]** echo-request **[\| ]**group-query **[\|]** group-reduction **[\| ]**group-report **[\|]** packet-too-big **[\|]** parameter-problem **[\|]** time-exceeded **} [[ **action** { { **drop** \| **logging** } \* \| **none** } ]]

**[undo signature detect**]**icmpv6-type **[[\|]** destination-unreachable **[\| ]**echo-reply **[\|]** echo-request **[\| ]**group-query **[\|]** group-reduction **[\| ]**group-report **[\|]** packet-too-big **[\|]** parameter-problem **[\|]** time-exceeded **}

**[signature detect**]**ip-option **[[\|]** internet-timestamp **[\|]** loose-source-routing **[\| ]**record-route **[\| **route-alert** \| **security**  \|]** stream-id **[\|]** strict-source-routing **} [[ **action** { { **drop** \| **logging** } \* \| **none** } ]]

**[undo signature detect**]**ip-option **[[\|]** internet-timestamp **[\|]** loose-source-routing **[\| ]**record-route **[\| **route-alert** \| **security**  \|]** stream-id **[\|]** strict-source-routing** }

**[signature detect ipv6-ext-header** *ext-header-value*]**[[ **action** { { **drop** \| **logging** } \* \| **none** } ]]

**[undo signature detect ipv6-ext-header** *next-header-value*]

【缺省情况】]

所有类型的单包攻击报文的特征检测均处于关闭状态。]

【视图】]

攻击防范策略视图]

【缺省用户角色】]

network-admin]

mdc-admin]

【参数】]

**[fraggle**]：表示Fraggle类型的报文攻击。

**[fragment**]：表示IP分片报文攻击。

**[icmp-type**]：表示ICMP类型的报文攻击。可以指定报文的类型值，或者指定报文的类型关键字。

·*icmp-type-value*：表示ICMP报文类型的数值，取值范围为0～255。

·**address-mask-reply**：表示ICMP address mask reply类型的报文攻击。

·**address-mask-request**：表示ICMP address mask request类型的报文攻击。

·**destination-unreachable**：表示ICMP destination unreachable类型的报文攻击。

·**echo-reply**：表示ICMP echo reply类型的报文攻击。

·**echo-request**：表示ICMP echo request类型的报文攻击。

·**information-reply**：表示ICMP information reply类型的报文攻击。

·**information-request**：表示ICMP information request类型的报文攻击。

·**parameter-problem**：表示ICMP para problem类型的报文攻击。

·**redirect**：表示ICMP redirect类型的报文攻击。

·**source-quench**：表示ICMP source quench类型的报文攻击。

·**time-exceeded**：表示ICMP time exceeded类型的报文攻击。

·**timestamp-reply**：表示ICMP timestamp reply类型的报文攻击。

·**timestamp-request**：表示ICMP timestamp request类型的报文攻击。

**[icmpv6-type**]：表示ICMPv6类型的报文攻击。可以指定报文的类型值，或者指定报文的类型关键字。

·*icmpv6-type-value*：表示ICMPv6报文类型的数值，取值范围为0～255。

·**destination-unreachable**：表示ICMPv6 destination unreachable类型的报文攻击。

·**echo-reply**：表示ICMPv6 echo reply类型的报文攻击。

·**echo-request**：表示ICMPv6 echo request类型的报文攻击。

·**group-query**：表示ICMPv6 group query类型的报文攻击。

·**group-reduction**：表示ICMPv6 group reduction类型的报文攻击。

·**group-report**：表示ICMPv6 group report类型的报文攻击。

·**packet-too-big**：表示ICMPv6 packet too big类型的报文攻击。

·**parameter-problem**：表示ICMPv6 para problem类型的报文攻击。

·**time-exceeded**：表示ICMPv6 time exceeded类型的报文攻击。

**[impossible**]：表示IP不可信报文的攻击。

**[ip-option**]：表示IP选项类型的报文攻击。可以指定IP选项代码值，或者指定IP选项关键字。

·*option-code*：表示IP选项代码值，取值范围为0～255。

·**internet-timestamp**：表示IP选项timestamp类型的报文攻击。

·**loose-source-routing**：表示IP选项loose source route类型的报文攻击。

·**record-route**：表示IP选项record packet route类型的报文攻击。

·**route-alert**：表示IP选项route alert类型的报文攻击。

·**security**：表示IP选项security类型的报文攻击。

·**stream-id**：表示IP选项stream identifier类型的报文攻击。

·**strict-source-routing**：表示IP选项strict source route类型的报文攻击。

**[ip-option-abnormal**]：表示IP选项异常类型的报文攻击。

**[ipv6-ext-header**]*ext-header-value*：表示IPv6扩展头参数值，取值范围在0～255。

**[land**]：表示Land类型的报文攻击。

**[large-icmp**]：表示超大ICMP报文的攻击。

**[large-icmpv6**]：表示超大ICMPv6报文的攻击。

**[ping-of-death**]：表示Ping-of-death类型的报文攻击。

**[smurf**]：表示Smurf类型的报文攻击。

**[snork**]：表示UDP Snork attack类型的报文攻击。

**[tcp-all-flags**]：表示TCP所有标志位均置位的报文攻击。

**[tcp-fin-only**]：表示TCP仅FIN标志被置位的报文攻击。

**[tcp-invalid-flags**]：表示TCP 标志位非法的报文攻击。

**[tcp-null-flag**]：表示TCP 标志位为零的报文攻击。

**[tcp-syn-fin**]：表示TCP SYN和FIN标志位被同时置位的报文攻击。

**[teardrop**]：表示teardrop类型的报文攻击。

**[tiny-fragment**]：表示IP分片报文的攻击。

**[traceroute**]：表示Trace route类型的报文攻击。

**[udp-bomb**]：表示UDP Bomb attack类型的报文攻击。

**[winnuke**]：表示WinNuke类型的报文攻击。

**[action**]：对指定报文攻击所采取的攻击防范处理行为。若不指定该参数，则采用该攻击报文所属的攻击防范级别所对应的默认处理行为。

·**drop**：设置单包攻击的处理行为为丢弃报文。

·**logging**：设置单包攻击的处理行为为发送日志。

·**none**：不采取任何动作。

【使用指导】

可以通过多次执行本命令开启多种类型的单包攻击报文的特征检测。

若通过数值指定了报文类型，则当指定的数值为标准的报文类型值时，在显示信息中将会显示该数值对应的报文类型字符串，否则显示为数值。

【举例】

\# 在攻击防范策略atk-policy-1中开启对Smurf攻击报文的特征检测，并指定攻击防范处理行为为为丢弃报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 signature detect smurf action drop

【相关命令】

·**signature ****level action**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature level action**

------------------------------------------------------------------------

**[signature level action**]命令用来配置指定级别单包攻击的处理行为。

**[undo signature level action**]命令用来恢复缺省情况。

【命令】

**[signature level**[ { **high** \| **info** \| **low** \| **medium** } **action** { { **drop** \| **logging** } \* \| **none** }]]

**[undo signature level**[ { **high** \| **info** \| **low** \| **medium** } **action**]]

【缺省情况】

对提示级别和低级别的单包攻击的处理行为是发送日志；对中级别的单包攻击的处理行为是发送日志并丢包；对高级别的单包攻击的处理行为是发送日志并丢包。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[high**]：表示高级别的单包攻击，暂无实例。

**[info**]：表示提示级别的单包攻击，例如Large ICMP。

**[low**]：表示低级别的单包攻击，例如Traceroute。

**[medium**]：表示中级别的单包攻击，例如Winnuke。

**[drop**]：设置单包攻击的处理行为为丢弃报文。

**[logging**]：设置单包攻击的处理行为为发送日志。

**[none**]：不采取任何动作。

【使用指导】

系统根据单包攻击结果的严重程度由低到高将其划分为四个攻击级别：提示、低级、中级、高级。开启某一个级别的单包攻击报文的特征检测，相当于批量开启了属于该级别的所有类型的单包攻击报文的特征检测。针对某一级别的单包攻击的处理行为由**signature level action**命令指定。

若同时通过**signature detect**命令开启了具体类型的单包攻击报文的特征检测，则以**signature detect**命令配置的参数为准。

【举例】

\# 在攻击防范策略atk-policy-1中配置对提示级别的单包攻击的处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy 1

Sysname-attack-defense-policy-1 signature level info action drop

【相关命令】

·**signature**** detect**

·**signature**** level detect**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- signature level detect**

------------------------------------------------------------------------

**[signature level detect**]命令用来开启指定级别单包攻击报文的特征检测。

**[undo signature level detect**]命令用来取消对指定级别的单包攻击报文的特征检测。

【命令】

**[signature level**[ { **high** \| **info** \| **low** \| **medium** } **detect**]]

**[undo signature level**[ { **high** \| **info** \| **low** \| **medium** } **detect**]]

【缺省情况】

未开启任何级别的单包攻击报文的特征检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[high**]：表示高级别的单包攻击，暂无实例。

**[info**]：表示提示级别的单包攻击，例如Large ICMP报文攻击。

**[low**]：表示低级别的单包攻击，例如Traceroute报文攻击。

**[medium**]：表示中级别的单包攻击，例如Winnuke报文攻击。

【使用指导】

系统根据单包攻击结果的严重程度将其划分为四个级别：提示、低级、中级、高级。开启某一个级别的单包攻击报文的特征检测，相当于批量开启了属于该级别的所有单包攻击报文的特征检测。针对某一级别的单包攻击的处理行为由**signature level action**命令指定。若通过**signature detect**命令开启了具体的单包攻击报文的特征检测，则对该类攻击报文的处理行为以**signature detect**命令配置的参数为准。

可通过**display attack-defense policy**命令查看各类型单包攻击所属的级别。

【举例】

\# 在攻击防范策略atk-policy-1中开启提示级别的单包攻击报文的特征检测。

\<Sysname\> system-view

Sysname attack-defense policy 1

Sysname-attack-defense-policy-1 signature level info detect

【相关命令】

·**display attack-defense policy**

·**signature ****detect**

·**signature**** level action**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood action**

------------------------------------------------------------------------

**[syn-ack-flood action**]命令用来配置对SYN-ACK flood攻击防范的全局处理行为。

**[undo syn-ack-flood action**]命令用来恢复缺省情况。

【命令】

**[syn-ack-flood action **[[ **client-verify** \| **drop** \| **logging** }\*]]

**[undo syn-ack-flood action**]

【缺省情况】]

不对检测到的 SYN-ACK flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有SYN-ACK报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成记录告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用需要和TCP客户端验证功能配合。使能了TCP客户端验证的接口检测到ACK flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\# 在攻击防范策略atk-policy-1中配置对SYN-ACK flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-ack-flood action drop

【相关命令】

·**client-verify ****tcp enable**

·**syn-ack-flood ****detect**

·**syn-ack-flood detect non-specific**

·**syn-ack-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood detect**

------------------------------------------------------------------------

**[syn-ack-flood detect**]命令用来对指定IP地址的SYN-ACK flood攻击防范检测，并配置SYN-ACK flood攻击防范检测触发阈值和防范行为。

**[undo syn-ack-flood detect**]命令用来取消对指定IP地址的SYN-ACK flood攻击防范检测。

【命令】

**[syn-ack-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo syn-ack-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置SYN-ACK flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold***threshold-value*]：指定SYN-ACK flood攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的SYN-ACK报文数目，取值范围为1～1000000。

**[action**]：设置对SYN-ACK flood攻击的处理行为。

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有SYN-ACK报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置SYN-ACK flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能SYN-ACK flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送SYN-ACK报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了SYN-ACK flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 开启对IP地址192.168.1.2的SYN-ACK flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的SYN-ACK报文数持续达到或超过2000时，启动SYN-ACK攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-ack-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**syn-ack-flood action**

·**syn-ack-flood detect non-specific**

·**syn-ack-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood detect non-specific**

------------------------------------------------------------------------

**[syn-ack-flood detect non-specific**]命令用来对所有非受保护IP地址开启SYN-ACK flood攻击防范检测。

**[undo syn-ack-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[syn-ack-flood detect non-specific**]

**[undo syn-ack-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启SYN-ACK flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IP地址开启SYN-ACK flood攻击防范检测后，设备将采用全局的阈值设置（由**syn-ack-flood threshold**命令设置）和处理行为（由**syn-ack-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启UDP flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-ack-flood detect non-specific

【相关命令】

·**syn-ack flood action**

·**syn-ack-flood ****detect**

·**syn-ack-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-ack-flood threshold**

------------------------------------------------------------------------

**[syn-ack-flood threshold**]命令用来配置SYN-ACK flood攻击防范的全局触发阈值。

**[undo syn-ack-flood threshold**]命令用来恢复缺省情况。

【命令】

**[syn-ack-flood threshold***threshold-value*]

**[undo syn-ack-flood threshold**]

【缺省情况】

SYN-ACK flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的SYN-ACK报文数目，取值范围为1～1000000。使能SYN-ACK flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送SYN-ACK报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了SYN-ACK flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置SYN-ACK flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的SYN-ACK报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置SYN-ACK flood攻击防范的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的SYN-ACK报文数持续达到或超过100时，启动SYN-ACK flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-ack-flood threshold 100

【相关命令】

·**syn-****ack-flood action**

·**syn-****ack-flood detect**

·**syn-ack-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood action**

------------------------------------------------------------------------

**[syn-flood action**]命令用来配置对SYN flood攻击防范的全局处理行为。

**[undo syn-flood action**]命令用来恢复缺省情况。

【命令】

**[syn-flood action**[ { **client-verify** \| **drop** \| **logging** } \*]]

**[undo syn-flood action**]

【缺省情况】

不对检测到的SYN flood攻击采取任何措施。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有SYN报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【使用指导】

本命令中**client-verify**参数的使用分别需要和TCP客户端验证功能配合。使能了TCP客户端验证的接口检测到ACK flood攻击时，若本命令中指定了**client-verify**参数，则设备会将受攻击的IP地址动态添加到相应客户端验证的受保护IP列表中，并对与这些IP地址建立的连接进行代理。若接口上没有使能相应的代理功能，则不会对任何连接进行代理。

【举例】

\# 在攻击防范策略atk-policy-1中配置对SYN flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-flood action drop

【相关命令】

·**syn-flood detect non-specific**

·**syn-flood**** detect**

·**syn-flood**** threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood detect**

------------------------------------------------------------------------

**[syn-flood detect**]命令用来开启对指定IP地址的SYN flood攻击防范检测，并配置SYN flood攻击防范检测的触发阈值和对SYN flood攻击的处理行为。

**[undo syn-flood detect**]命令用来取消对指定IP地址的SYN flood攻击防范检测。

【命令】

**[syn-flood**[ **detect** { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **threshold** *threshold-value*  [ **action** { { **client-verify** \| **drop** \| **logging** } \* \| **none** } ]]]

**[undo syn-flood detect**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置SYN flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold***threshold-value*]：指定SYN flood攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的SYN报文数目，取值范围为1～1000000。

**[action**]：设置对SYN flood攻击的处理行为。

**[client-verify**]：表示自动将受到攻击的IP地址添加到TCP客户端验证的受保护IP列表中。若客户端验证功能已使能，则对客户端与受保护IP地址之间的连接进行代理。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有SYN报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置SYN flood攻击防范检测，具体数目与设备的型号有关，请以设备的实际情况为准。

使能SYN flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送SYN报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了SYN flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的SYN flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的SYN报文数持续达到或超过2000时，启动SYN flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**syn-flood action**

·**syn-flood detect non-specific**

·**syn-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood detect non-specific**

------------------------------------------------------------------------

**[syn-flood detect non-specific**]命令用来对所有非受保护IP地址开启SYN flood攻击防范检测。

**[undo syn-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[syn-flood detect non-specific**]

**[undo syn-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启SYN flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IP地址开启SYN flood攻击防范检测后，设备将采用全局的阈值设置（由**syn-flood threshold**命令设置）和处理行为（由**syn-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启SYN flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-flood detect non-specific

【相关命令】

·**syn-flood action**

·**syn-flood ****detect**

·**syn-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- syn-flood threshold**

------------------------------------------------------------------------

**[syn-flood threshold**]命令用来配置SYN flood攻击防范的全局触发阈值。

**[undo syn-flood threshold**]命令用来恢复缺省情况。

【命令】

**[syn-flood threshold***threshold-value*]

**[undo syn-flood threshold**]

【缺省情况】

SYN flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的SYN报文数目，取值范围为1～1000000。使能SYN flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送SYN报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了SYN flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置SYN flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的SYN报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置SYN flood攻击防范的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的SYN报文数持续达到或超过100时，启动SYN flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 syn-flood threshold 100

【相关命令】

·**syn-flood action**

·**syn-flood ****detect **

·**syn-flood detect non-specific**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood action**

------------------------------------------------------------------------

**[udp-flood action**]命令用来配置对UDP flood攻击防范的全局处理行为。

**[undo udp-flood action**]命令用来恢复缺省情况。

【命令】

**[udp-flood action**[ { **drop** \| **logging** } \*]]

**[undo udp-flood action**]

【缺省情况】

不对检测到的UDP flood攻击进行任何处理。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有UDP报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

【举例】

\# 在攻击防范策略atk-policy-1中配置对UDP flood攻击防范的全局处理行为是丢弃后续报文。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 udp-flood action drop

【相关命令】

·**udp-flood ****detect**

·**udp-flood detect non-specific**

·**udp-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood detect**

------------------------------------------------------------------------

**[udp-flood detect**]命令用来开启对指定IP地址的UDP flood攻击防范检测，并配置UDP flood攻击防范检测的触发阈值和对UDP flood攻击的处理行为。

**[undo udp-flood detect**]命令用来取消对指定IP地址的UDP flood攻击防范检测。

【命令】

**[udp-flood detect **[{ **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]  **threshold** *threshold-value*  [ **action** { { **drop** \| **logging** } \* \| **none** } ]]]

**[undo udp-flood detect**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ]]]

【缺省情况】

未对任何指定IP地址配置UDP flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：指定要保护的IP地址。该IP地址不能为全1地址或全0地址。

**[ipv6*** ipv6-address*]：指定要保护的IPv6地址。

**[vpn-instance** *vpn-instance-name*]：受保护IP地址所属的VPN实例。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若不指定该参数，则表示该保护IP地址属于公网。

**[threshold***threshold-value*]：指定UDP flood攻击防范的触发阈值。其中，*threshold-value*为向指定IP地址每秒发送的UDP报文数目，取值范围为1～64000。

**[action**]：设置对UDP flood攻击的处理行为。

**[drop**]：表示丢弃攻击报文，即设备检测到攻击发生后，向被攻击者发送的后续所有UDP报文都会被丢弃。

**[logging**]：表示输出告警日志，即设备检测到攻击发生时，生成告警信息，生成的告警信息将被发送到日志系统。

**[none**]：表示不采取任何动作。

【使用指导】

每个攻击防范策略下可以同时对多个IP地址配置UDP flood攻击防范参数，具体数目与设备的型号有关，请以设备的实际情况为准。

使能UDP flood攻击防范后，设备处于攻击检测状态，当它监测到向指定IP地址发送UDP报文的速率持续达到或超过了触发阈值时，即认为该IP地址受到了UDP flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。此后，当设备检测到向该服务器发送报文的速率低于恢复阈值（触发阈值的3/4）时，即认为攻击结束，则由攻击防范状态恢复为攻击检测状态，并停止执行防范措施。

【举例】

\# 在攻击防范策略atk-policy-1中开启对IP地址192.168.1.2的UDP flood攻击防范检测，并指定触发阈值为2000。当设备监测到向该IP地址每秒发送的UDP报文数持续达到或超过2000时，启动UDP flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 udp-flood detect ip 192.168.1.2 threshold 2000

【相关命令】

·**udp-flood action**

·**udp-flood detect non-specific**

·**udp-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood detect non-specific**

------------------------------------------------------------------------

**[udp-flood detect non-specific**]命令用来对所有非受保护IP地址开启UDP flood攻击防范检测。

**[undo udp-flood detect non-specific**]命令用来恢复缺省情况。

【命令】

**[udp-flood detect non-specific**]

**[undo udp-flood detect non-specific**]

【缺省情况】

未对所有非受保护IP地址开启UDP flood攻击防范检测。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对所有非受保护IP地址开启UDP flood攻击防范检测后，设备将采用全局的阈值设置（由**udp-flood threshold**命令设置）和处理行为（由**udp-flood action**命令配置）对这些IP地址进行保护。

【举例】

\# 在攻击防范策略atk-policy-1中，对所有非受保护IP地址开启UDP flood攻击防范检测。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 udp-flood detect non-specific

【相关命令】

·**udp-flood action**

·**udp-flood ****detect**

·**udp-flood ****threshold**

**攻击检测与防范 \-- 攻击检测与防范配置命令 \-- udp-flood threshold**

------------------------------------------------------------------------

**[udp-flood threshold**]命令用来配置UDP flood攻击防范的全局触发阈值。

**[undo udp-flood threshold**]命令用来恢复缺省情况。

【命令】

**[udp-flood threshold***threshold-value*]

**[undo udp-flood threshold**]

【缺省情况】

UDP flood攻击防范的全局触发阈值为1000。

【视图】

攻击防范策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：指定向某IP地址每秒发送的UDP报文数目，取值范围为1～64000。使能UDP flood攻击防范后，设备处于攻击检测状态，当它监测到向某IP地址发送UDP报文的速率持续达到或超过了该触发阈值时，即认为该IP地址受到了UDP flood攻击，则进入攻击防范状态，并根据配置启动相应的防范措施。

【使用指导】

对于没有专门配置UDP flood攻击防范检测的IP地址，设备采用全局的阈值设置来进行保护。阈值的取值需要根据实际网络应用场景进行调整，对于正常情况下到被保护对象（HTTP服务器或者FTP服务器）的UDP报文流量较大的应用场景，建议调大触发阈值，以免阈值太小对正常的业务流量造成影响；对于网络状况较差，且对攻击流量比较敏感的场景，可以适当调小触发阈值。

【举例】

\# 在攻击防范策略atk-policy-1中配置UDP flood攻击防范的全局触发阈值为100，即当设备监测到向某IP地址每秒发送的UDP报文数持续达到或超过100时，启动UDP flood攻击防范。

\<Sysname\> system-view

Sysname attack-defense policy atk-policy-1

Sysname-attack-defense-policy-atk-policy-1 udp-flood threshold 100

【相关命令】

·**udp-flood action**

·**udp-flood ****detect**

·**udp-flood detect non-specific**
