<!-- CMD-INDEX
  arp resolving-route enable          | 系统视图             | L33
  arp resolving-route probe-count     | 系统视图             | L87
  arp resolving-route probe-interval  | 系统视图             | L133
  arp source-suppression enable       | 系统视图             | L179
  arp source-suppression limit        | 系统视图             | L223
  display arp source-suppression      | 任意视图             | L271
  arp rate-limit                      | 二层以太网接口视图/二层聚合接口视图 | L319
  arp rate-limit log enable           | 系统视图             | L365
  arp rate-limit log interval         | 系统视图             | L405
  snmp-agent trap enable arp          | 系统视图             | L457
  arp source-mac                      | 系统视图             | L503
  arp source-mac aging-time           | 系统视图             | L553
  arp source-mac exclude-mac          | 系统视图             | L593
  arp source-mac threshold            | 系统视图             | L637
  display arp source-mac              | 任意视图             | L677
  arp valid-check enable              | 系统视图             | L767
  arp active-ack enable               | 系统视图             | L809
  arp authorized enable               | 三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图/VLAN接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准） | L853
  arp detection enable                | VLAN视图           | L891
  arp detection trust                 | 二层以太网接口视图/二层聚合接口视图 | L929
  arp detection validate              | 系统视图             | L967
  arp restricted-forwarding enable    | VLAN视图           | L1011
  display arp detection               | 任意视图             | L1049
  display arp detection statistics    | 任意视图             | L1097
  reset arp detection statistics      | 用户视图             | L1183
  arp fixup                           | 系统视图             | L1217
  arp scan                            | 三层以太网接口视图/三层以太网子接口视图/VLAN接口视图/三层聚合接口视图/三层聚合子接口视图 | L1255
  arp filter source                   | 二层以太网接口视图/二层聚合接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准） | L1331
  arp filter binding                  | 二层以太网接口视图/二层聚合接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准） | L1379
-->

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp resolving-route enable**

------------------------------------------------------------------------

**[arp resolving-route enable**]命令用来开启ARP黑洞路由功能。

**[undo arp resolving-route enable**]命令用来关闭ARP黑洞路由功能。

【命令】

**[arp resolving-route enable**]

**[undo arp resolving-route enable**]

【缺省情况】

不同型号的设备的缺省情况不同，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

建议在网关设备上配置本功能。

如果网络中有主机通过向设备发送大量目标IP地址不能解析的IP报文来攻击设备，则会造成下面的危害：

·设备向目的网段发送大量ARP请求报文，加重目的网段的负载。

·设备会试图反复地对目标IP地址进行解析，增加了CPU的负担。

如果发送攻击报文的源不固定，可以采用ARP黑洞路由功能。开启该功能后，一旦接收到目标IP地址不能解析的IP报文，设备立即产生一个黑洞路由，使得设备在一段时间内将去往该地址的报文直接丢弃。等待黑洞路由老化时间过后，如有报文触发则再次发起解析，如果解析成功则进行转发，否则仍然产生一个黑洞路由将去往该地址的报文丢弃。这种方式能够有效地防止IP报文的攻击，减轻CPU的负担。

【举例】

\# 开启ARP黑洞路由功能。

\<Sysname\> system-view

Sysname arp resolving-route enable

【相关命令】

·**arp resolving-route probe-count**

·**arp resolving-route probe-interval**

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp resolving-route probe-count**

------------------------------------------------------------------------

**[arp resolving-route probe-count**]命令用来配置发送ARP请求报文的次数。

**[undo arp resolving-route probe-count**]命令用来恢复缺省情况。

【命令】

**[arp resolving-route probe-count** *count*]

**[undo arp resolving-route probe-count**]

【缺省情况】

发送ARP请求报文的次数为1次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定发送ARP请求报文的次数，取值范围为1～25。

【举例】

\# 配置发送ARP请求报文的次数为3次。

\<Sysname\> system-view

Sysname arp resolving-route probe-count 3

【相关命令】

·**arp resolving-route enable**

·**arp resolving-route probe-interval**

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp resolving-route probe-interval**

------------------------------------------------------------------------

**[arp resolving-route probe-interval**]命令用来配置发送ARP请求报文的时间间隔。

**[undo arp resolving-route probe-interval**]命令用来恢复缺省情况。

【命令】

**[arp resolving-route probe-interval ***interval*]

**[undo arp resolving-route probe-interval**]

【缺省情况】

发送ARP请求报文的时间间隔是1秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送ARP请求报文的时间间隔，取值范围为1～5，单位为秒。

【举例】

\# 配置发送ARP请求报文的时间间隔为3秒。

\<Sysname\> system-view

Sysname arp resolving-route probe-interval 3

【相关命令】

·**arp resolving-route enable**

·**arp resolving-route probe-count**

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp source-suppression enable**

------------------------------------------------------------------------

**[arp source-suppression enable**]命令用来使能ARP源地址抑制功能。

**[undo arp source-suppression enable**]命令用来恢复缺省情况。

【命令】

**[arp source-suppression enable**]

**[undo arp source-suppression enable**]

【缺省情况】

ARP源地址抑制功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

建议在网关设备上配置本功能。

【举例】

\# 使能ARP源地址抑制功能。

\<Sysname\> system-view

Sysname arp source-suppression enable

【相关命令】

·**display arp source-suppression**

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp source-suppression limit**

------------------------------------------------------------------------

**[arp source-suppression limit**]命令用来配置ARP源抑制的阈值。

**[undo arp source-suppression limit**]命令用来恢复缺省情况。

【命令】

**[arp source-suppression limit ***limit-value*]

**[undo arp source-suppression limit**]

【缺省情况】

ARP源抑制的阈值为10。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit-value*]：ARP源抑制的阈值，即设备在5秒间隔内可以处理的源IP相同，但目的IP地址不能解析的IP报文的最大数目，取值范围为2～1024。

【使用指导】

如果网络中每5秒内从某IP地址向设备某接口发送目的IP地址不能解析的IP报文超过了设置的阈值，则设备将不再处理由此IP地址发出的IP报文直至该5秒结束，从而避免了恶意攻击所造成的危害。

【举例】

\# 配置ARP源抑制的阈值为100。

\<Sysname\> system-view

Sysname arp source-suppression limit 100

【相关命令】

·**display arp source-suppression**

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- display arp source-suppression**

------------------------------------------------------------------------

**[display arp source-suppression**]命令用来显示当前ARP源抑制的配置信息。

【命令】

**[display arp source-suppression**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示当前ARP源抑制的配置信息。

\<Sysname\> display arp source-suppression

 ARP source suppression is enabled

 Current suppression limit: 100

表1-1 display arp source-suppression显示信息描述表

字段

描述

ARP source suppression is enabled

ARP源地址抑制功能处于使能状态

Current suppression limit

设备在5秒时间间隔内可以接收到的源IP相同，但目的IP地址不能解析的IP报文的最大数目

**ARP攻击防御 \-- ARP报文限速配置命令 \-- arp rate-limit**

------------------------------------------------------------------------

**[arp rate-limit**]命令用来开启ARP报文限速功能。

**[undo arp rate-limit**]命令用来关闭ARP报文限速功能。

【命令】

**[arp** **rate-limit** [ *pps* ]]

**[undo arp rate-limit**]

【缺省情况】

ARP报文限速功能处于开启状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pps*]：ARP限速速率，单位为包每秒（pps）。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

不指定限速速率时，设备使用缺省限速速率，超过限速部分的报文会被丢弃。缺省限速速率和设备型号有关，请以设备的实际情况为准。

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1接口ARP报文限速为50pps，超过限速部分的报文被丢弃。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp rate-limit 50

**ARP攻击防御 \-- ARP报文限速配置命令 \-- arp rate-limit log enable**

------------------------------------------------------------------------

**[arp rate-limit log enable**]命令用来开启ARP报文限速日志功能，如果设备收到ARP报文的速率超过用户设定的限速值，则生成日志信息。

**[undo arp rate-limit log enable**]命令用来关闭ARP报文限速日志功能。

【命令】

**[arp rate-limit log enable**]

**[undo arp rate-limit log enable**]

【缺省情况】

设备的ARP报文限速日志功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当开启了ARP限速日志功能后，设备将这个时间间隔内的超速峰值作为日志的速率值发送到设备的信息中心，通过设置信息中心的参数，最终决定日志报文的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的设置请参见"网络管理和监控配置指导"中的"信息中心"）

【举例】

\# 开启ARP报文限速日志功能。

\<Sysname\> system-view

Sysname arp rate-limit log enable

**ARP攻击防御 \-- ARP报文限速配置命令 \-- arp rate-limit log interval**

------------------------------------------------------------------------

**[arp rate-limit log interval**]命令用来配置当设备收到的ARP报文速率超过用户设定的限速值时，设备发送告警或日志的时间间隔。

**[undo arp rate-limit log interval**]命令用来恢复缺省情况。

【命令】

**[arp rate-limit log interval ***seconds*]

**[undo arp rate-limit log interval**]

【缺省情况】

当设备收到的ARP报文速率超过用户设定的限速值时，设备发送告警或日志的时间间隔为60秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：当端口上的ARP报文速率超过用户设定的限速值时，设备发送告警或日志的时间间隔。*seconds*的取值范围为1～86400，单位为秒。

【使用指导】

用户需要先开启发送告警或日志功能，然后配置此命令指定设备发送告警或日志的时间间隔，同时本命令必须和端口下的**arp rate-limit**命令配合使用，单独配置本命令无效。

【举例】

\# 当设备收到的ARP报文速率超过用户设定的限速值时，配置设备发送告警或日志的时间间隔为120秒。

\<Sysname\> system-view

Sysname arp rate-limit log interval 120

【相关命令】

·**arp rate-limit**

·**arp rate-limit log enable**

·**snmp-agent trap ****enable arp**

**ARP攻击防御 \-- ARP报文限速配置命令 \-- snmp-agent trap enable arp**

------------------------------------------------------------------------

**[snmp-agent trap enable arp**]命令用来开启ARP模块的告警功能。

**[undo snmp-agent trap enable arp**]命令用来关闭ARP模块的告警功能。

【命令】

**[snmp-agent trap enable arp ** **rate-limit** ]

**[undo snmp-agent trap enable arp ** **rate-limit** ]

【缺省情况】

ARP模块的告警功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rate-limit**]：启动ARP报文限速的告警功能。

【使用指导】

当开启了ARP模块的告警功能后，设备将这个时间间隔内的超速峰值作为告警信息发送出去，生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关特性。

有关告警信息的详细描述，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 启动ARP报文限速的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable arp rate-limit

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac**

------------------------------------------------------------------------

**[arp source-mac**]命令用来开启源MAC地址固定的ARP攻击检测功能，并选择检查模式。

**[undo arp source-mac**]命令用来恢复缺省情况。

【命令】

**[arp source-mac **[{ **filter** \| **monitor** }]]

**[undo arp source-mac **[[ **filter** \| **monitor** ]]]

【缺省情况】

源MAC地址固定的ARP攻击检测功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[filter**]：检测到攻击后，打印Log信息，同时对该源MAC地址对应的ARP报文进行过滤。

**[monitor**]：检测到攻击后，只打印Log信息，不对该源MAC地址对应的ARP报文进行过滤。

【使用指导】

·建议在网关设备上开启本功能。

·开启源MAC地址固定的ARP攻击检测之后，该特性会对上送CPU的ARP报文按照源MAC地址和VLAN进行统计。当在一定时间（5秒）内收到某固定源MAC地址的ARP报文超过设定的阈值，不同模式的处理方式存在差异：在**filter**模式下会打印Log信息并对该源MAC地址对应的ARP报文进行过滤；在**monitor**模式下只打印Log信息，不过滤ARP报文。

·如果**undo arp source-mac**命令中没有指定检查模式，则关闭任意检查模式的源MAC地址固定的ARP攻击检测功能。

【举例】

\# 开启源MAC地址固定的ARP攻击检测功能，并选择**filter**检查模式。

\<Sysname\> system-view

Sysname arp source-mac filter

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac aging-time**

------------------------------------------------------------------------

**[arp source-mac aging-time**]命令用来配置源MAC地址固定的ARP攻击检测表项的老化时间。

**[undo arp source-mac aging-time**]命令用来恢复缺省情况。

【命令】

**[arp source-mac aging-time ***time*]

**[undo arp source-mac aging-time**]

【缺省情况】

源MAC地址固定的ARP攻击检测表项的老化时间为300秒，即5分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：源MAC地址固定的ARP攻击检测表项的老化时间，取值范围为60～6000，单位为秒。

【举例】

\# 配置源MAC地址固定的ARP攻击检测表项的老化时间为60秒。

\<Sysname\> system-view

Sysname arp source-mac aging-time 60

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac exclude-mac**

------------------------------------------------------------------------

**[arp source-mac exclude-mac**]命令用来配置保护MAC地址。当配置了保护MAC地址之后，即使该ARP报文中的MAC地址存在攻击也不会被检测过滤。

**[undo arp source-mac exclude-mac**]命令用来取消配置的保护MAC地址。

【命令】

**[arp source-mac exclude-mac ***mac-address*&\<1-n\>]

**[undo arp source-mac exclude-mac** [ *mac-address*&\<1-n\> ]]

【缺省情况】

没有配置任何保护MAC地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*&\<1-n\>]：MAC地址列表。其中，*mac-address*表示配置的保护MAC地址，格式为H-H-H。&\<1-n\>表示每次最多可以配置的保护MAC地址个数。n的取值范围和设备相关，请以设备的实际情况为准。

【使用指导】

如果**undo**命令中没有指定MAC地址，则取消所有已配置的保护MAC地址。

【举例】

\# 配置源MAC地址固定的ARP攻击检查的保护MAC地址为2-2-2。

\<Sysname\> system-view

Sysname arp source-mac exclude-mac 2-2-2

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac threshold**

------------------------------------------------------------------------

**[arp source-mac threshold**]命令用来配置源MAC地址固定的ARP报文攻击检测阈值，当在固定的时间（5秒）内收到源MAC地址固定的ARP报文超过该阈值则认为存在ARP报文攻击。

**[undo arp source-mac threshold**]命令用来恢复缺省情况。

【命令】

**[arp source-mac threshold ***threshold-value*]

**[undo arp source-mac threshold**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：固定时间内源MAC地址固定的ARP报文攻击检测的阈值，单位为报文个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置源MAC地址固定的ARP报文攻击检测阈值为30个。

\<Sysname\> system-view

Sysname arp source-mac threshold 30

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- display arp source-mac**

------------------------------------------------------------------------

**[display arp source-mac**]命令用来显示检测到的源MAC地址固定的ARP攻击检测表项。

【命令】

集中式设备：

**[display arp source-mac ** **interface** *interface-type interface-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display arp source-mac **{ **slot** *slot-number* [ **cpu** *cpu-number*  \| **interface** *interface-type interface-number* }]]

分布式设备－IRF模式：

**[display arp source-mac **{ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  \| **interface** *interface-type interface-number* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口检测到的源MAC地址固定的ARP攻击检测表项，*interface-type interface-number*表示指定接口的类型和编号。

**[slot*** slot-number*]：显示指定单板检测到的源MAC地址固定的ARP攻击检测表项。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板检测到的源MAC地址固定的ARP攻击检测表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备检测到的源MAC地址固定的ARP攻击检测表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上检测到的源MAC地址固定的ARP攻击检测表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备检测到的源MAC地址固定的ARP攻击检测表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上检测到的源MAC地址固定的ARP攻击检测表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板检测到的源MAC地址固定的ARP攻击检测表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上检测到的源MAC地址固定的ARP攻击检测表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板检测到的源MAC地址固定的ARP攻击检测表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上检测到的源MAC地址固定的ARP攻击检测表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU检测到的源MAC地址固定的ARP攻击检测表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示检测到的源MAC地址固定的ARP攻击检测表项。

\<Sysname\> display arp source-mac

Source-MAC          VLAN ID  Interface                Aging-time

23f3-1122-3344      4094     GE1/0/1                  10

23f3-1122-3355      4094     GE1/0/2                  30

23f3-1122-33ff      4094     GE1/0/3                  25

23f3-1122-33ad      4094     GE1/0/4                  30

23f3-1122-33ce      4094     GE1/0/5                  2

表1-2 display arp source-mac命令显示信息描述表

字段

描述

Source-MAC

检测到攻击的源MAC地址

VLAN ID

检测到攻击的VLAN ID

Interface

攻击来源的接口

Aging-time

ARP防攻击策略表项老化剩余时间

**ARP攻击防御 \-- ARP报文源MAC地址一致性检查配置命令 \-- arp valid-check enable**

------------------------------------------------------------------------

**[arp valid-check enable**]命令用来开启ARP报文源MAC地址一致性检查功能。

**[undo arp valid-check enable**]命令用来关闭ARP报文源MAC地址一致性检查功能。

【命令】

**[arp valid-check enable**]

**[undo arp valid-check enable**]

【缺省情况】

ARP报文源MAC地址一致性检查功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

ARP报文源MAC地址一致性检查功能主要应用于网关设备。

开启ARP报文源MAC地址一致性检查功能后，设备会对接收的ARP报文进行检查，如果以太网数据帧首部中的源MAC地址和ARP报文中的源MAC地址不同，则丢弃该报文。

【举例】

\# 使能ARP报文源MAC地址一致性检查功能。

\<Sysname\> system-view

Sysname arp valid-check enable

**ARP攻击防御 \-- ARP主动确认配置命令 \-- arp active-ack enable**

------------------------------------------------------------------------

**[arp active-ack enable**]命令用来使能ARP主动确认功能。

**[undo arp active-ack enable**]命令用来恢复缺省情况。

【命令】

**[arp active-ack ** **strict** ] **enable**

**[undo arp active-ack ** **strict** ] **enable**

【缺省情况】

ARP主动确认功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[strict**]：ARP主动确认功能的严格模式。

【使用指导】

ARP的主动确认功能主要应用于网关设备，防止攻击者仿冒用户欺骗网关设备。通过**strict**参数使能或关闭主动确认的严格模式。使能严格模式后，ARP主动确认功能执行更严格的检查，新建ARP表项前，需要本设备先对其IP地址发起ARP解析，解析成功后才能触发正常的主动确认流程，在主动确认流程成功后，才允许设备学习该表项。

【举例】

\# 使能ARP主动确认功能。

\<Sysname\> system-view

Sysname arp active-ack enable

**ARP攻击防御 \-- 授权ARP配置命令 \-- arp authorized enable**

------------------------------------------------------------------------

**[arp authorized enable**]命令用来使能接口下的授权ARP功能。

**[undo arp authorized enable**]命令用来恢复缺省情况。

【命令】

**[arp authorized enable**]

**[undo arp authorized enable**]

【缺省情况】

接口下的授权ARP功能处于关闭状态。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图/VLAN接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准）

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能接口下授权ARP功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp authorized enable

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp detection enable**

------------------------------------------------------------------------

**[arp detection enable**]命令用来使能ARP Detection功能，即对ARP报文进行用户合法性检查。

**[undo arp detection enable**]命令用来恢复缺省情况。

【命令】

**[arp detection enable**]

**[undo arp detection enable**]

【缺省情况】

ARP Detection功能处于关闭状态，即不进行用户合法性检查。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能ARP Detection功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 arp detection enable

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp detection trust**

------------------------------------------------------------------------

**[arp detection trust**]命令用来配置接口为ARP信任接口。

**[undo arp detection trust**]命令用来恢复缺省情况。

【命令】

**[arp detection trust**]

**[undo arp detection trust**]

【缺省情况】

接口为ARP非信任接口。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1为ARP信任接口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp detection trust

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp detection validate**

------------------------------------------------------------------------

**[arp detection validate**]命令用来使能对ARP报文的目的MAC地址或源MAC地址、IP地址的有效性检查。使能有效性检查时可以指定某一种检查方式也可以配置成多种检查方式的组合。

**[undo arp detection validate**]命令用来关闭对ARP报文的有效性检查。关闭时可以指定关闭某一种或多种检查，在不指定检查方式时，表示关闭所有有效性检查。

【命令】

**[arp detection validate **[{ **dst-mac** \| **ip** \| **src-mac** } \*]]

**[undo arp detection validate **[[ **dst-mac** \| **ip** \| **src-mac** ] \*]]

【缺省情况】

不同型号的设备支持的缺省情况不同，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dst-mac**]：检查ARP应答报文中的目的MAC地址，是否为全0或者全1，是否和以太网报文头中的目的MAC地址一致。全0、全1、不一致的报文都是无效的，无效的报文需要被丢弃。

**[ip**]：检查ARP报文源IP和目的IP地址，全1或者组播IP地址都是不合法的，需要丢弃。对于ARP应答报文，源IP和目的IP地址都进行检查；对于ARP请求报文，只检查源IP地址。

**[src-mac**]：检查ARP报文中的源MAC地址和以太网报文头中的源MAC地址是否一致，一致认为有效，否则丢弃。

【举例】

\# 使能对ARP报文的MAC地址和IP地址的有效性检查。

\<Sysname\> system-view

Sysname arp detection validate dst-mac src-mac ip

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp restricted-forwarding enable**

------------------------------------------------------------------------

**[arp restricted-forwarding enable**]命令用来使能ARP报文强制转发功能。

**[undo arp restricted-forwarding enable**]命令用来关闭ARP报文强制转发功能。

【命令】

**[arp restricted-forwarding enable**]

**[undo arp restricted-forwarding enable**]

【缺省情况】

ARP报文强制转发功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能VLAN 2的ARP报文强制转发功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 arp restricted-forwarding enable

**ARP攻击防御 \-- ARP Detection配置命令 \-- display arp detection**

------------------------------------------------------------------------

**[display arp detection**]命令用来显示使能了ARP Detection功能的VLAN。

【命令】

**[display arp detection**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有使能了ARP Detection功能的VLAN。

\<Sysname\> display arp detection

 ARP detection is enabled in the following VLANs:

 1-2, 4-5

表1-3 display arp detection命令显示信息描述表

字段

描述

ARP detection is enabled in the following VLANs

使能了ARP Detection功能的VLAN

【相关命令】

·**arp detection enable**

**ARP攻击防御 \-- ARP Detection配置命令 \-- display arp detection statistics**

------------------------------------------------------------------------

**[display arp detection statistics**]命令用来显示ARP Detection功能报文检查的丢弃计数的统计信息。

【命令】

**[display arp detection statistics ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口的统计信息。*interface-type interface-number*用来指定接口类型和编号。

【使用指导】

按接口显示用户合法性检查、报文有效性检查和ARP报文上送限速的统计情况，只显示ARP Detection功能报文的丢弃情况。不指定接口时，显示所有接口的统计信息。

【举例】

\# 显示ARP Detection功能报文检查的丢弃计数的统计信息。

\<Sysname\> display arp detection statistics

State: U-Untrusted  T-Trusted

ARP packets dropped by ARP inspect checking:

Interface(State)            IP        Src-MAC   Dst-MAC   Inspect

GE1/0/1(U)                  40        0         0         78

GE1/0/2(U)                  0         0         0         0

GE1/0/3(T)                  0         0         0         0

GE1/0/4(U)                  0         0         30        0

表1-4 display arp detection statistics命令显示信息描述表

字段

描述

State

接口状态：

·U：ARP非信任接口

·T：ARP信任接口

Interface(State)

ARP报文入接口，State表示该接口的信任状态

IP

ARP报文源和目的IP地址检查不通过丢弃的报文计数

Src-MAC

ARP报文源MAC地址检查不通过丢弃的报文计数

Dst-MAC

ARP报文目的MAC地址检查不通过丢弃的报文计数

Inspect

ARP报文结合用户合法性检查不通过丢弃的报文计数

**ARP攻击防御 \-- ARP Detection配置命令 \-- reset arp detection statistics**

------------------------------------------------------------------------

**[reset arp detection statistics**]命令用来清除ARP Detection的统计信息。

【命令】

**[reset arp detection statistics ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：表示清除指定接口下的统计信息。*interface-type interface-number*用来指定接口类型和编号。

【使用指导】

不指定接口时，清除所有ARP Detection统计信息。

【举例】

\# 清除所有ARP Detection统计信息。

\<Sysname\> reset arp detection statistics

**ARP攻击防御 \-- ARP自动扫描、固化配置命令 \-- arp fixup**

------------------------------------------------------------------------

**[arp fixup**]命令用来配置ARP固化功能，将当前的动态ARP表项转换为静态ARP表项。后续学习到的动态ARP表项可以通过再次执行**arp fixup**命令进行固化。

【命令】

**[arp fixup**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

固化后的静态ARP表项与配置产生的静态ARP表项相同。

固化生成的静态ARP表项数量同样受到设备可以支持的静态ARP表项数目的限制，由于静态ARP表项数量的限制可能导致只有部分动态ARP表项被固化。

如果用户执行固化前有D个动态ARP表项，S个静态ARP表项，由于固化过程中存在动态ARP表项的老化或者新建动态ARP表项的情况，所以固化后的静态ARP表项可能为（D＋S＋M－N）个。其中，M为固化过程中新建的动态ARP表项个数，N为固化过程中老化的动态ARP表项个数。

通过固化生成的静态ARP表项，可以通过命令行**undo arp ***ip-address* [ *vpn-instance-name* ]逐条删除，也可以通过命令行**reset arp all**或**reset arp static**全部删除。

【举例】

\# 配置ARP固化功能。

\<Sysname\> system-view

Sysname arp fixup

**ARP攻击防御 \-- ARP自动扫描、固化配置命令 \-- arp scan**

------------------------------------------------------------------------

**[arp scan**]命令用来启动ARP自动扫描功能，该功能可以对接口下指定地址范围内的邻居进行扫描。

【命令】

**[arp scan** [ *start-ip-address* **to** *end-ip-address* ]]

【视图】

三层以太网接口视图/三层以太网子接口视图/VLAN接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-ip-address*]：ARP扫描区间的起始IP地址。起始IP地址必须小于等于终止IP地址。

*[end-ip-address*]：ARP扫描区间的终止IP地址。终止IP地址必须大于等于起始IP地址。

【使用指导】

·如果用户知道局域网内邻居分配的IP地址范围，指定了ARP扫描区间，则对该范围内的邻居进行扫描，减少扫描等待的时间。如果指定的扫描区间同时在接口下多个IP地址的网段内，则发送的ARP请求报文的源IP地址选择网段范围较小的接口IP地址。

·如果用户不指定ARP扫描区间的起始IP地址和终止IP地址，则仅对接口下的主IP地址网段内的邻居进行扫描。其中，发送的ARP请求报文的源IP地址就是接口的主IP地址。

·ARP扫描区间的起始IP地址和终止IP地址必须与接口的IP地址（主IP地址或手工配置的从IP地址）在同一网段。

·对于已存在ARP表项的IP地址不进行扫描。

·扫描操作可能比较耗时，用户可以通过\<Ctrl_C\>来终止扫描（在终止扫描时，对于已经收到的邻居应答，会建立该邻居的动态ARP表项）。

【举例】

·路由应用

\# 对接口GigabitEthernet1/0/1下的主IP地址网段内的邻居进行扫描。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp scan

\# 对接口GigabitEthernet1/0/1下指定地址范围内的邻居进行扫描。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp scan 1.1.1.1 to 1.1.1.20

·交换应用

\# 对接口Vlan-interface2下的主IP地址网段内的邻居进行扫描。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 arp scan

\# 对接口Vlan-interface2下指定地址范围内的邻居进行扫描。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 arp scan 1.1.1.1 to 1.1.1.20

**ARP攻击防御 \-- ARP网关保护配置命令 \-- arp filter source**

------------------------------------------------------------------------

**[arp filter source**]命令用来开启ARP网关保护功能，配置受保护的网关IP地址。

**[undo arp filter source**]命令用来删除已配置的受保护网关IP地址。

【命令】

**[arp filter source** *ip-address*]

**[undo arp filter source** *ip-address*]

【缺省情况】

ARP网关保护功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准）

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：受保护的网关IP地址。

【使用指导】

·每个接口最多支持配置8个受保护的网关IP地址。

·不能在同一接口下同时配置命令**arp filter source**和**arp filter binding**。

【举例】

\# 在GigabitEthernet1/0/1下开启ARP网关保护功能，受保护的网关IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp filter source 1.1.1.1

**ARP攻击防御 \-- ARP过滤保护配置命令 \-- arp filter binding**

------------------------------------------------------------------------

**[arp filter binding**]命令用来开启ARP过滤保护功能，限制只有特定源IP地址和源MAC地址的ARP报文才允许通过。

**[undo arp filter binding**]命令用来删除已配置的被允许通过的ARP报文的源IP地址和源MAC地址。

【命令】

**[arp filter binding ***ip-address mac-address*]

**[undo arp filter binding** *ip-address*]

【缺省情况】

ARP过滤保护功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准）

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：允许通过的ARP报文的源IP地址。

*[mac-address*]：允许通过的ARP报文的源MAC地址。

【使用指导】

·每个接口最多支持配置8组允许通过的ARP报文的源IP地址和源MAC地址。

·不能在同一接口下同时配置命令**arp filter source**和**arp filter binding**。

【举例】

\# 在GigabitEthernet1/0/1下开启ARP过滤保护功能，允许源IP地址为1.1.1.1、源MAC地址为2-2-2的ARP报文通过。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 arp filter binding 1.1.1.1 2-2-2
