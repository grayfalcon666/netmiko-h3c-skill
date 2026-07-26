
**QoS策略 \-- 定义类的命令 \-- display traffic classifier**

------------------------------------------------------------------------

**[display traffic classifier**]命令用来显示类的配置信息。

【命令】

集中式设备：

**[display traffic classifier**[ { **system-defined** \| **user-defined** } [ *classifier-name* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display traffic classifier**[ { **system-defined** \| **user-defined** } [ *classifier-name* ]  **slot**]*slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display traffic classifier**} [ *classifier-name*  \**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ] ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[system-defined**]：系统定义类。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[user-defined**]：用户定义类。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

*[classifier-name*]：类名，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有类的配置信息。

**[slot**]* slot-number*：显示指定单板的流分类的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板的类的配置信息。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的流分类的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主用设备的类的配置信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上流分类的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主用设备上类的配置信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的流分类的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板的类的配置信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上流分类的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上类的配置信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上流分类的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示用户定义类的配置信息。

\<Sysname\> display traffic classifier user-defined

  User-defined classifier information:

   Classifier: 1 (ID 100)

     Operator: AND

     Rule(s) :

      If-match acl 2000

   Classifier: 2 (ID 101)

     Operator: AND

     Rule(s) :

      If-match not protocol ipv6

   Classifier: 3 (ID 102)

     Operator: AND

     Rule(s) :

      -none-

\# 显示系统定义类default-class的配置信息。

\<Sysname\> display traffic classifier system-defined default-class

  System-defined classifier information:

   Classifier: default-class (ID 0)

     Operator: AND

     Rule(s) :

      If-match any

表1-1 display traffic classifier命令显示信息描述表

字段

描述

User-defined classifier information

用户自定义类的信息

System-defined classifier information

系统定义类的信息

Classifier

类的名字及其内容，内容可以有多种类型

Operator

分类规则之间的逻辑关系

Rule(s)

分类规则

**QoS策略 \-- 定义类的命令 \-- if-match**

------------------------------------------------------------------------

**[if-match**]命令用来定义匹配数据包的规则。

**[undo if-match**]命令用来删除配置的匹配数据包的规则。

【命令】

**[if-match ** **not** ] *match-criteria*

**[undo if-match** [ **not**  *match-criteria*]]

【缺省情况】

没有定义匹配数据包的规则。

【视图】

类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[not**]：不匹配该规则。

*[match-criteria*]：类的匹配规则，具体情况如[表]1-2(?-1354469580#_Ref213127397)所示。

表1-2 类的匹配规则取值

取值

描述

**[acl** [ **ipv6**  { *acl-numbe*r \| **name** *acl-name* }]]

定义匹配ACL的规则

*[acl-number*]是ACL的序号，IPv4 ACL序号的取值范围是2000～5999，IPv6 ACL序号的取值范围是2000～5999

*[acl-name*]是ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头，为避免混淆，ACL的名称不可以使用英文单词all

**[app-group*** group-name*]

定义匹配应用组的规则，*group-name*为系统预定义应用组的名称。应用组的取值范围与设备的型号有关，请以设备的实际情况为准

**[application*** app-name*]

定义匹配应用名的规则，*app-name*为系统预定义应用的名称。应用名的取值范围与设备的型号有关，请以设备的实际情况为准

**[any**]

定义匹配所有数据包的规则

**[cellular ***cellular-mode*]

定义匹配所处网络环境属性的的规则，*cellular-mode*的取值可以为2g，3g，4g。取值范围与设备的型号有关，请以设备的实际情况为准

**[classifier**]*****classifier-name*

定义匹配QoS类的规则，*classifier-name*为类名

**[control-plane protocol ***protocol-name*&\<1-8\>]

定义匹配控制平面或者管理口控制平面协议的规则，*protocol-name*&\<1-8\>为系统预定义匹配协议报文类型名称的列表，具体如[表]1-3(?-1354469580#_Ref362545063)所示，&\<1-8\>表示前面的参数最多可以输入8次。协议类型的取值范围与设备的型号有关，请以设备的实际情况为准

**[control-plane protocol-group ***protocol-group-name*]

定义匹配控制平面或者管理口控制平面协议组的规则，*protocol-group-name*取值为critical、exception、important、management、monitor、normal、redirect

**[customer-dot1p** *dot1p-value*&\<1-8\>]

定义匹配内层VLAN Tag 802.1p优先级的规则，*dot1p-value*&\<1-8\>为802.1p优先级值的列表，802.1p优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次

**[customer-vlan-id ***vlan-id-list*]

定义匹配内层VLAN Tag VLAN ID的规则，*vlan-id-list*：VLAN列表，表示方式为*vlan-id-list *[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-10\>]，*vlan-id*、*vlan-id1*、*vlan-id2*取值范围为1～4094，且*vlan-id1*的值必须小于*vlan-id2*的值；&\<1-10\>表示前面的参数最多可以重复输入10次

**[destination-mac** *mac-address*]

定义匹配目的MAC地址的规则

**[dscp** *dscp-value*&\<1-8\>]

定义匹配DSCP的规则，*dscp-value*&\<1-8\>为DSCP取值的列表，DSCP的取值范围为0～63，&\<1-8\>表示前面的参数最多可以输入8次；也可以输入关键字，具体如[表]1-5(?-580725274#_Ref163816081)所示

**[forwarding-layer ** { **bridge** \| **route** }]

定义匹配转发报文的二、三层属性的规则：

·**bridge**：只匹配二层转发报文

·**route**：只匹配三层转发报文

**[inbound-interface** *interface-type* *interface-number*]

定义匹配入接口的规则，*interface-type interface-number*为接口类型和接口编号

**[ip-precedence** *ip-precedence-value*&\<1-8\>]

定义匹配IP优先级的规则，*ip-precedence-value*&\<1-8\>为IP优先级的列表，IP优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次

**[local-precedence ***local-precedence-value*&\<1-8\>]

定义匹配本地优先级的规则，*local-precedence-value*&\<1-8\>为本地优先级的列表，本地优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次

**[mpls-exp** *exp-value*&\<1-8\>]

定义匹配第一层MPLS EXP优先级的规则，*exp-value*&\<1-8\>为EXP的列表，EXP优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次

**[mpls-label**[ { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]]

定义匹配第一层MPLS标签的规则，*label-value*&\<1-8\>为MPLS标签值的列表，&\<1-8\>表示前面的参数最多可以输入8次，*label-value1*** to** *label-value2*表示一个MPLS标签的范围，*label-value1*的值必须小于*label-value2*的值，MPLS标签的取值范围为0～1048575

**[packet-length**]*[min-value*[\|]**max ***max-value*} \*

定义匹配报文长度的规则，]*min-value*为匹配报文最小长度的字节数，*max-value*为匹配报文最大长度的字节数

**[protocol** *protocol-name*]

定义匹配协议的规则，*protocol-name*取值为arp、ip、ipv6

**[qos-local-id** *local-id-value*]

定义匹配QoS本地ID值的规则，*local-id-value*为QoS本地ID，取值范围为1～4095

**[rtp start-port**]*****start-port-number***end-port***end-port-number*

定义匹配RTP协议端口的规则。*start-port-number*为起始RTP端口号，取值范围为2000～65535；*end-port-number*为结束RTP端口号，取值范围为2000～65535

**[second-mpls-exp** *exp-value*&\<1-8\>]

定义匹配第二层MPLS EXP优先级的规则，*exp-value*&\<1-8\>为EXP的列表，EXP优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次

**[second-mpls-label**[ { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]]

定义匹配第二层MPLS标签的规则，*label-value*&\<1-8\>为MPLS标签值的列表，&\<1-8\>表示前面的参数最多可以输入8次，*label-value1*** to*** label-value2*表示一个MPLS标签的范围，*label-value1*的值必须小于*label-value2*的值，MPLS标签的取值范围为0～1048575

**[service-dot1p ***dot1p-value*&\<1-8\>]

定义匹配外层VLAN Tag 802.1p优先级的规则，*dot1p-value*&\<1-8\>为802.1p优先级值的列表，802.1p优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次

**[service-vlan-id** *vlan-id-list*]

定义匹配外层VLAN Tag VLAN ID的规则，*vlan-id-list*：VLAN列表，表示方式为*vlan-id-list *[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-10\>]，*vlan-id*、*vlan-id1*、*vlan-id2*取值范围为1～4094，且*vlan-id1*的值必须小于*vlan-id2*的值；&\<1-10\>表示前面的参数最多可以重复输入10次

**[source-mac** *mac-address*]

定义匹配源MAC地址的规则

表1-3 系统预定义匹配协议报文类型名称的列表

报文类型

说明

default

其他协议

arp

ARP协议

arp-snooping

ARP Snooping协议

bgp

BGP协议

bgp4+

IPv6 BGP

bpdu-tunnel

BPDU Tunnel协议

cdp

CDP协议

cfd

CFD协议

dhcp

DHCP协议

dhcp-snooping

DHCP Snooping协议

dhcpv6

IPv6 DHCP协议

dldp

DLDP协议

dot1x

802.1p 协议

gmrp

GMRP协议

mvrp

MVRP协议（包含GVRP协议）

http

HTTP协议

https

HTTPS协议

icmp

ICMP协议

icmpv6

IPv6 ICMP协议

igmp

IGMP协议

igmp-snooping

IGMP Snooping协议

irdp

IRDP协议

isis

IS-IS协议

lacp

LACP协议

ldp

LDP协议

ldp6

IPv6 LDP协议

lldp

LLDP协议

mld

MLD协议

msdp

MSDP协议

ntp

NTP协议

oam

OAM协议

ospf-multicast

OSPF组播

ospf-unicast

OSPF单播

ospf3-multicast

OSPFv3组播

ospf3-unicast

OSPFv3单播

pim-multicast

PIM组播

pim-unicast

PIM单播

pim6-multicast

IPv6 PIM组播

pim6-unicast

IPv6 PIM单播

portal

PORTAL协议

pppoe-negotiation

PPPoE协商

pvst

PVST协议

radius

RADIUS协议

rip

RIP协议

ripng

RIPng协议

rrpp

RRPP协议

rsvp

RSVP协议

smart-link

Smart Link协议

snmp

SNMP协议

stp

STP协议

tacacs

TACACS协议

udld

UDLD协议

udp-helper

UDP中继转发

vrrp

VRRP协议

vrrp6

IPv6 VRRP协议

vtp

VLAN中继协议

ip-option

带选项字段的IPv4报文

ipv6-option

带选项字段的IPv6报文

ssh

SSH协议

telnet

TELNET协议

ftp

FTP协议

tftp

TFTP协议

bfd

BFD协议

ttl-expires

TTL超时

hoplimit-expires

Hop Limit超时

【使用指导】

在定义各个规则的时候，注意事项如下：

(1)定义匹配ACL的规则

·如果类中引用的ACL不存在，则不能在硬件中下发。

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·对同一个类，允许通过ACL名称和序号的方式分别引用一次同一个ACL。

·对于有些产品而言，当**if-match**中引用的ACL规则的动作为**deny**时，则跳出该**if-match**，继续进行后续规则的查找；对于有些产品而言，直接忽略ACL规则的动作，以流行为中定义的动作为准，报文匹配只使用ACL中的分类域。具体情况和设备的型号有关，请以设备的实际情况为准。

(2)定义匹配用户组或者应用名的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

(3)定义匹配所处网络环境属性的的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·该命令用于匹配指定网络环境下的报文。**2g**表示匹配处于2G网络环境下的报文，**3g**表示匹配处于3G网络环境下的报文，**4g**表示匹配处于4G网络环境下的报文。

(4)定义匹配类的规则

如果匹配类的规则之间既有逻辑与，又有逻辑或的关系，采用本匹配方法可以解决。

例如，需要定义classA，满足以下关系：规则1 & 规则[2 \| ]规则3，可以这样定义：

·traffic classifier classB operator and

·if-match规则1

·if-match规则2

·traffic classifier classA operator or

·if-match规则3

·if-match classifier classB

一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

(5)定义匹配目的MAC地址规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·匹配目的MAC地址规则只对以太网接口有意义。

(6)定义匹配源MAC地址规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·匹配源MAC地址规则只对以太网接口有意义。

(7)定义匹配DSCP的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个DSCP值，最多可指定8个；如果指定了多个相同的DSCP值，系统默认为一个；多个不同的DSCP值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配DSCP的规则时，指定的所有DSCP值必须与该规则中定义的完全相同才会删除，顺序可不一样。

(8)定义匹配内层VLAN Tag和外层VLAN Tag 802.1p优先级的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个802.1p优先级值，最多可指定8个；如果指定了多个相同的802.1p优先级值，系统默认为一个；多个不同的802.1p优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配802.1p优先级的规则时，指定的所有802.1p优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。

(9)定义匹配IP优先级的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个IP优先级值，最多可指定8个；如果指定了多个相同的IP优先级值，系统默认为一个；多个不同的IP优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配IP优先级的规则时，指定的所有IP优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。

(10)定义匹配本地优先级的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。每条命令在配置后，本地优先级的值将自动按照从小到大的顺序排序。

·一条命令可以配置多个本地优先级值，最多可指定8个；如果指定了多个相同的本地优先级值，系统默认为一个；多个不同的本地优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配本地优先级的规则时，指定的所有本地优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。

(11)定义匹配MPLS EXP优先级的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个MPLS EXP优先级值，最多可指定8个；如果指定了多个相同的MPLS EXP优先级值，系统默认为一个；多个不同的MPLS EXP优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配MPLS EXP优先级的规则时，指定的所有MPLS EXP优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。

·MPLS EXP为MPLS报文特有的参数，该匹配规则仅对MPLS报文生效。

·对于软转发QoS，MPLS报文不支持匹配IP相关匹配规则。

(12)定义匹配MPLS Label的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个MPLS Label值，如果指定了多个相同的MPLS Label值，系统默认为一个；多个不同的MPLS Label值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配MPLS Label的规则时，指定的所有MPLS Label值必须与该规则中定义的完全相同才会删除，顺序可不一样。

(13)定义匹配内层VLAN Tag和外层VLAN Tag VLAN ID的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个VLAN ID值，如果指定了多个相同的VLAN ID值，系统默认为一个；多个不同的VLAN ID值是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配VLAN ID的规则时，指定的所有VLAN ID值必须与该规则中定义的完全相同才会删除，顺序可不一样。

·若只携带单层VLAN Tag，可以用外层VLAN Tag的VLAN ID规则来匹配。

(14)定义匹配报文长度的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·如果只配置**min**，则表示匹配大于*min-value*长度的报文；如果只配置**max**，表示匹配小于*max-value*长度的报文；同时配置**min**和**max**，表示匹配长度在*min-value*～*max-value*之间的报文。其中*max-value*必须大于等于*min-value*。

(15)定义匹配预定义的上送控制平面或者管理口控制平面报文类型的规则

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

·一条命令可以配置多个protocol，如果指定了多个相同的protocol，系统默认为一个；多个不同的protocol是或的关系，即只要有一个值匹配，就算匹配这条规则。

·删除某条匹配protocol的规则时，指定的所有protocol必须与该规则中定义的完全相同才会删除，顺序可不一样。

(16)定义匹配RTP协议端口的规则

·该命令用于匹配落在指定RTP端口号范围内的RTP报文，即匹配所有在*start-port-number*与*end-port-number*之间的偶数UDP端口号的报文。

·一个类下可配置多条这样的命令，各个配置之间互相不覆盖。

【举例】

\# 定义类class1的匹配规则为：匹配目的MAC地址为0050-ba27-bed3的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match destination-mac 0050-ba27-bed3

\# 定义类class2的匹配规则为：匹配源MAC地址为0050-ba27-bed2的报文。

\<Sysname\> system-view

Sysname traffic classifier class2

Sysname-classifier-class2 if-match source-mac 0050-ba27-bed2

\# 定义类class1的匹配规则为：匹配内层VLAN Tag的802.1p优先级为3。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match customer-dot1p 3

\# 定义类class1的匹配规则为：匹配外层VLAN Tag的802.1p优先级为5。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match service-dot1p 5

\# 定义类匹配ACL3101。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match acl 3101

\# 定义类匹配ACL flow。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match acl name flow

\# 定义类匹配IPv6 ACL3101。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match acl ipv6 3101

\# 定义类匹配IPv6 ACL flow。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match acl ipv6 name flow

\# 定义匹配所有数据包的规则。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match any

\# 定义类class1的匹配规则为：匹配DSCP值为1或6或9的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match dscp 1 6 9

\# 定义类class1的匹配规则为：匹配IP优先级值为1或6的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match ip-precedence 1 6

\# 定义类class1的匹配规则为：匹配本地优先级值为1或6的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match local-precedence 1 6

\# 定义类匹配IP协议的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match protocol ip

\# 定义类class1的匹配规则为：匹配RTP端口号在16384和32767之间的偶数UDP端口号的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match rtp start-port 16384 end-port 32767

\# 定义类class1的匹配规则为：匹配内层VLAN Tag的VLAN ID值为1或6或9的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match customer-vlan-id 1 6 9

\# 定义类class1的匹配规则为：匹配外层VLAN Tag的VLAN ID值为2或7或10的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match service-vlan-id 2 7 10

\# 定义类class1匹配qos-local-id 3。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match qos-local-id 3

\# 定义类class1匹配应用组multimedia。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match app-group multimedia

\# 定义类class1匹配应用名3link。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match app-name 3link

\# 在流分类class1中配置匹配MPLS-Label为1到10000的报文类型。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match mpls-label 1 to 10000

\# 在流分类class1中配置只匹配二层转发报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match forwarding-layer bridge

\# 在流分类class1中配置匹配上送控制平面或管理口控制平面的ARP协议报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match control-plane protocol arp

\# 在流分类class1中配置匹配上送控制平面或管理口控制平面的normal协议组报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match control-plane protocol-group normal

\# 在流分类class1中配置匹配报文长度为100～200字节的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match packet-length min 100 max 200

\# 在流分类class1中配置匹配处于3G网络环境下的报文。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1 if-match cellular 3g

**QoS策略 \-- 定义类的命令 \-- traffic classifier**

------------------------------------------------------------------------

**[traffic classifier**]命令用来定义一个类，并进入类视图。

**[undo traffic classifier**]命令用来删除一个类。

【命令】

**[traffic classifier**[ *classifier-name* [ **operator** { **and** \| **or** } ]]]

**[undo traffic classifier** *classifier-name*]

【缺省情况】

没有定义类。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[classifier-name*]：类名，为1～31个字符的字符串，区分大小写。

**[operator**]：指定各规则之间的逻辑运算符。缺省情况为**and**。

**[and**]：指定类下的规则之间是逻辑与的关系，即数据包必须匹配全部规则才属于该类。

**[or**]：指定类下的规则之间是逻辑或的关系，即数据包只要匹配其中任何一个规则就属于该类。

【举例】

\# 定义一个名为class1的类。

\<Sysname\> system-view

Sysname traffic classifier class1

Sysname-classifier-class1

【相关命令】

·**display traffic classifier**

**QoS策略 \-- 定义流行为的命令 \-- accounting**

------------------------------------------------------------------------

**[accounting**]命令用来配置流量统计动作。

**[undo accounting**]命令用来取消流量统计动作配置。

【命令】

**[accounting **[[ **byte** \| **packet** ] \*]]

**[undo accounting**]

【缺省情况】

没有配置流量统计动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[byte**]：表示报文基于字节进行统计。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet**]：表示报文基于包进行统计。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·当设备仅支持一种统计方式或者不支持配置流统计单位时，命令行中不提示**byte**和**packet**关键字，默认的统计单位由产品决定。

·当设备支持两种统计方式，但在某一时刻仅能使用一种统计单位进行统计时，**byte**和**packet**为必选参数，即必须在配置中指明流统计单位。

·当设备支持同时按两种方式进行统计，**byte**和**packet**为可选参数，也可以两种统计方式同时指定。若用户不指明统计单位，则采用默认的统计单位进行统计，默认的统计单位和是否可以同时指定两种方式进行统计由产品决定。

【举例】

\# 为流行为配置流量统计动作，基于字节进行统计。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database accounting byte

**QoS策略 \-- 定义流行为的命令 \-- car**

------------------------------------------------------------------------

**[car**]命令用来配置流量监管动作。

**[undo car**]命令用来取消流量监管动作配置。

【命令】

**[car cir ***committed-information-rate* [ **cbs** *committed-burst-size* [ **ebs** *excess-burst-size*    **green** *action* \| **red** *action* \| **yellow** *action* ] \* [ **hierarchy-car** *hierarchy-car-name* [ **mode** { **and** \| **or** } ] ]]]

**[car cir ***committed-information-rate* [ **cbs** *committed-burst-size*  **pir** *peak-information-rate*  **ebs** *excess-burst-size*  [ **green** *action* \| **red** *action* \| **yellow** *action* ] \* [ **hierarchy-car** *hierarchy-car-name* [ **mode** { **and** \| **or** } ] ]]]

**[undo car**]

【缺省情况】

没有配置流量监管动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cir*** committed-information-rate*]：承诺信息速率。流量的平均速率，单位为kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[cbs ***committee-burst-size*]：承诺突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *excess-burst-size*]：超出突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir ***peak-information-rate*]：峰值速率，单位为kbps。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[green ***action*]：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为**pass**。

**[red ***action*]：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为**discard**。

**[yellow ***action*]：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为**pass**。

*[action*]：对数据包采取的动作，有以下几种：

·**discard**：丢弃数据包。

·**pass**：允许数据包通过。

·**remark-atmclp-pass** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-dot1p-pass** *new-cos*：设置新的802.1P报文的优先级值，并允许数据包通过，取值范围为0～7。

·**remark-dscp-pass** *new-dscp*：设置报文新的DSCP值，并允许数据包通过，取值范围为0～63。

·**remark-frde-pass** *new-frde*：设置新的FR报文的DE标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-lp-pass ***new-local-precedence*：设置新的本地优先级，并允许数据包通过，取值范围为0～7。

·**remark-mpls-exp-pass** *new-exp*：设置新的MPLS报文的EXP标志位的值，并允许数据包通过，取值范围为0～7。

·**remark-prec-pass** *new-precedence*：设置新的IP优先级，并允许数据包通过，取值范围为0～7。

*[hierarchy-car-name*]：分层CAR的名称。

**[mode**]：分层CAR和CAR动作的合作模式。有**and**和**or**两种模式，默认为**and**模式。

·**and**：在该模式下，对于多条数据流应用同一个分层CAR，必须每条流满足各自的CAR配置，同时各流量之和又满足分层CAR的配置，流量才能正常通过。

·**or**：在该模式下，对于多条数据流应用同一个分层CAR，只要每条流满足各自的CAR配置或者各流量之和满足分层CAR配置，流量即可正常通过。

【使用指导】

·接口上应用的策略中使用**car**时，可以应用到接口报文的接收或者发送方向。

·如果多次使用该命令在同一个流行为上配置，最后一次配置生效。

·CAR支持的动作与设备相关，请以设备的实际情况为准。

·不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。

【举例】

\# 为流行为配置流量监管。报文正常流速为200kbps，承诺突发尺寸为50000bytes，速率大于200kbps时，报文DSCP值改为0并发送。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database car cir 200 cbs 50000 ebs 0 green pass red remark-dscp-pass 0

**QoS策略 \-- 定义流行为的命令 \-- display traffic behavior**

------------------------------------------------------------------------

**[display traffic behavior**]命令用来显示流行为的配置信息。

【命令】

集中式设备：

**[display traffic behavior**[ { **system-defined** \| **user-defined** } [ *behavior-name* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display traffic behavior**[ { **system-defined** \| **user-defined** } [ *behavior-name* ]  **slot**]*slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display traffic behavior**[ { **system-defined** \| **user-defined** } [ *behavior-name* ] ]**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[system-defined**]：系统定义行为。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[user-defined**]：用户定义行为。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

*[behavior-name*]：行为名，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示所有流行为的配置信息。

**[slot**]* slot-number*：显示指定单板的流行为的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的流行为的配置信息。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的流行为的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备的流行为的配置信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上流行为的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备上流行为的配置信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的流行为的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的流行为的配置信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上流行为的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上流行为的配置信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上流行为的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示用户定义行为的配置信息。

\<Sysname\> display traffic behavior user-defined

  User-defined behavior information:

    Behavior: 1 (ID 100)

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

      Primap pre-defined table: dscp-dp

      Assured Forwarding:

        Bandwidth 30 (kbps)

        Discard Method: Tail

    Behavior: 2 (ID 101)

      Accounting enable: Packet

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

      Redirecting:

        Redirect to the CPU

      Mirroring:

        Mirror to the VLAN: VLAN 1000

      Expedited Forwarding:

        Bandwidth 50 (kbps) CBS 1250 (Bytes)

    Behavior: 3 (ID 102)

      -none-

\# 显示系统定义行为的配置信息。

\<Sysname\> display traffic behavior system-defined

  System-defined behavior information:

    Behavior: be (ID 0)

      -none-

    Behavior: af (ID 1)

      Assured Forwarding:

        Bandwidth 20 (%)

        Discard Method: Tail

    Behavior: ef (ID 2)

      Expedited Forwarding:

        Bandwidth 20 (%) Cbs-ratio 25

    Behavior: be-flow-based (ID 3)

      Flow based Weighted Fair Queue:

        Max number of hashed queues: 256

        Discard Method: IP Precedence based WRED

        Exponential Weight: 9

        Pre  Low   High  Dis-prob

        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

        0    10    30    10

        1    10    30    10

        2    10    30    10

        3    10    30    10

        4    10    30    10

        5    10    30    10

        6    10    30    10

        7    10    30    10

表1-4 display traffic behavior命令显示信息描述表

字段

描述

User-defined behavior information

用户自定义流行为的信息

System-defined behavior information

系统定义流行为的信息

Behavior

行为的名字及其内容，内容可以有多种类型

Marking

标记相关信息

Remark dscp

重新标记报文的DSCP优先级值

Committed Access Rate

流量限速的相关信息

CIR

承诺信息速率，单位为kbps

CBS

承诺突发尺寸，单位为byte

EBS

超出突发尺寸，单位为byte

Green action

对绿色报文的动作

Red action

对红色报文的动作

Yellow action

对黄色报文的动作

Primap pre-defined table

预定义映射表相关信息。对于映射表的描述可以参考2.1  (#_Ref307496562)[优先级映射表配置命令](#_Ref307496567)

Primap color-map-dp

根据报文颜色标记丢弃优先级的映射表

Primap pre-defined color table

预定义带颜色映射表相关信息。对于带颜色映射表的描述可以参考2.1  (#_Ref307496562)[优先级映射表配置命令](#_Ref307496567)

Assured Forwarding

确保转发（AF队列）的相关信息

Bandwidth

队列的带宽

Discard Method

丢弃方式

Accounting enable

流量统计动作

Filter enable

流量过滤动作

Remark mpls-exp

重新标记报文的EXP优先级值

Redirecting

流量重定向相关信息

Mirroring

流量镜像相关信息

Expedited Forwarding

加速转发（EF队列）相关信息

none

表示没有配置其他流行为

Flow based Weighted Fair Queue

基于流的加权公平队列相关信息

Max number of hashed queues

加权公平队列的长度

Exponential Weight

计算平均队列长度的指数

Pre

报文的IP优先级

Low

队列下限

High

队列上限

Dis-prob

计算丢弃概率时的分母

**QoS策略 \-- 定义流行为的命令 \-- filter**

------------------------------------------------------------------------

**[filter**]命令用来配置流量过滤动作。

**[undo filter**]命令用来取消流量过滤动作配置。

【命令】

**[filter **[{ **deny** \| **permit** }]]

**[undo filter**]

【缺省情况】

没有配置流量过滤动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[deny**]：丢弃数据包。

**[permit**]：允许数据包通过。

【举例】

\# 为流行为配置丢弃数据包的过滤动作。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database filter deny

**QoS策略 \-- 定义流行为的命令 \-- gts**

------------------------------------------------------------------------

**[gts**]命令用来采用绝对值的方式为流行为配置流量整形动作。

**[undo gts**]命令用来取消流量整形动作配置。

【命令】

**[gts cir ***committed-information-rate* [ **cbs** *committed-burst-size* [ **ebs** *excess-burst-size*  ]  **queue-length** *queue-length* ]]

**[gts cir ***committed-information-rate* [ **cbs** *committed-burst-size*  **pir** *peak-information-rate*  **ebs** *excess-burst-size*   **queue-length** *queue-length* ]]

**[undo gts**]

【缺省情况】

没有配置流量整形动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cir ***committed-information-rate*]：承诺信息速率，单位为kbps。

**[cbs** *committed-burst-size*]：承诺突发尺寸，实际平均速率在承诺速率以内时的突发流量，单位为byte。

**[ebs** *excess-burst-size*]：超出突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率。PIR必须大于等于CIR。

**[queue-length*** queue-length*]：队列的最大长度，缺省值为50。

【使用指导】

接口上应用的策略中使用**gts**时，只能应用到接口的出方向。

接口上应用配置了**gts**的策略将导致原有的**qos gts**命令失效。

如果多次使用该命令在同一个流行为上配置，最后一次的配置将覆盖前面的配置。

不配置PIR表示所配置的是单速桶流量整形，否则表示双速桶流量整形。

【举例】

\# 为流行为配置GTS，正常流速为200kbps，承诺突发尺寸为50000bytes，速率大于200kbps时，将进入队列缓存，缓存队列长度为100。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database gts cir 200 cbs 50000 ebs 0 queue-length 100

【相关命令】

·**gts percent**

**QoS策略 \-- 定义流行为的命令 \-- gts percent**

------------------------------------------------------------------------

**[gts percent**]命令用来采用百分比的方式为流行为配置流量整形动作。

**[undo gts**]命令用来取消流量整形动作配置。

【命令】

**[gts percent cir** *cir-percent* [ **cbs** *cbs-time* [ **ebs** *ebs-time*  ]  **queue-length** *queue-length* ]]

**[undo gts**]

【缺省情况】

没有配置流量整形动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cir ***cir-percent*]：承诺信息速率百分比，取值范围为1～100。CIR的实际值是百分比值乘以接口带宽值。

**[cbs** *cbs-time*]：某段时间内的承诺突发尺寸，单位为ms，缺省值为500ms。CBS的实际值是CBS的配置时间值乘以实际的承诺信息速率（**cir**值乘以接口带宽）。

**[ebs** *ebs-time*]：某段时间内的超出突发尺寸，单位为ms，缺省值为0ms。EBS的实际值是EBS的配置时间值乘以实际的承诺信息速率（**cir**值乘以接口带宽）。

**[queue-length*** queue-length*]：队列的最大长度，缺省值为50。

【使用指导】

接口上应用的策略中使用**gts**时，只能应用到接口的出方向。

接口上应用配置了**gts**的策略将导致原有的**qos gts**命令失效。

如果多次使用该命令在同一个流行为上配置，最后一次的配置将覆盖前面的配置。

【举例】

\# 配置使用流量整形，正常流量为50%的接口带宽，在第一时间可以有200ms×50%接口带宽的突发流量通过，以后速率小于等于50%的接口带宽时正常发送，速率大于50%的接口带宽时，将进入队列缓存。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database gts percent cir 50 cbs 200

【相关命令】

·**gts**

**QoS策略 \-- 定义流行为的命令 \-- nest top-most**

------------------------------------------------------------------------

**[nest** **top-most**]命令用来配置添加VLAN Tag的动作。

**[undo nest** **top-most**]命令用来取消添加VLAN Tag的动作。

【命令】

**[nest top-most vlan ***vlan-id * **dot1p** *802.1p* ]

**[undo nest top-most**]

【缺省情况】

没有配置添加VLAN Tag的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan***vlan-id*]：添加的VLAN ID，取值范围为1～4094。

**[dot1p ***802.1p*]：添加的VLAN Tag的802.1p优先级，取值范围为0～7。如果不指定该参数，则表示报文外层VLAN Tag的802.1p优先级和内层保持一致。

【使用指导】

·引用了添加VLAN Tag动作的QoS策略只能应用到接口的入方向上。

·在同一个流行为上多次配置本命令，新配置将覆盖旧配置。

【举例】

\# 在流行为b1上配置如下动作：添加VLAN ID为123的VLAN Tag，并配置该层VLAN Tag的802.1p优先级为3。

\<Sysname\> system-view

Sysname traffic behavior b1

Sysname-behavior-b1 nest top-most vlan 123 dot1p 3

**QoS策略 \-- 定义流行为的命令 \-- packet-rate**

------------------------------------------------------------------------

**[packet-rate**]命令用来为流行为配置限速动作。

**[undo packet-rate**]命令用来取消配置。

【命令】

**[packet-rate**]*****value*

**[undo packet-rate**]

【缺省情况】

没有配置限速动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：协议报文速率，单位为包每秒（pps）。取值范围和设备的型号有关，请以设备的实际情况为准。

【使用指导】

通过限速可以实现CPU的协议报文防攻击功能。

【举例】

\# 为流行为copp配置CPU报文限速动作。

\<Sysname\> system-view

Sysname traffic behavior copp

Sysname-behavior-copp packet-rate 1600

**QoS策略 \-- 定义流行为的命令 \-- primap color-map-dp**

------------------------------------------------------------------------

**[primap color-map-dp**]命令用来配置流行为中的动作为根据报文颜色标记报文的丢弃优先级。

**[undo primap color-map-dp**]命令用来取消流行为中的根据报文颜色标记报文的丢弃优先级的动作。

【命令】

**[primap color-map-dp**]

**[undo primap color-map-dp**]

【缺省情况】

没有配置流优先级映射动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令需要和car结合在一起使用。

映射关系为：红色对应丢弃优先级2，黄色对应丢弃优先级1，绿色对应丢弃优先级0。此映射关系固定，不能修改。

【举例】

 # 根据报文的颜色标记报文的丢弃优先级。

\<Sysname\> system-view

Sysname traffic behavior behavior1

Sysname-behavior-behavior1 car cir 1600

Sysname-behavior-behavior1 primap color-map-dp

【相关命令】

·**primap pre-defined**

·**primap pre-defined color**

**QoS策略 \-- 定义流行为的命令 \-- primap pre-defined**

------------------------------------------------------------------------

**[primap pre-defined**]命令用来配置流行为中的动作为使用相应的优先级映射表为报文获取其他的优先级参数。

**[undo primap pre-defined**]命令用来取消流行为中的使用相应优先级映射表为报文映射优先级的动作。

【命令】

**[primap pre-defined**[ { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]]

**[undo primap pre-defined**[ { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]]

【缺省情况】

没有配置流优先级映射动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pre-defined**]：预先定义的优先级映射表。

**[dot11e-lp**]：802.11e优先级到本地优先级映射表。

**[dot1p-dot1p**]：802.1p优先级到802.1p优先级映射表。

**[dot1p-dp**]：802.1p优先级到丢弃优先级映射表。

**[dot1p-dscp**]：802.1p优先级到DSCP映射表。

**[dot1p-exp**]：802.1p优先级到EXP映射表。

**[dot1p-lp**]**：**802.1p优先级到本地优先级映射表。

**[dot1p-rpr**]：802.1p优先级到RPR优先级映射表

**[dscp-dot1p**]**：**DSCP到802.1p优先级映射表。

**[dscp-dp**]**：**DSCP到丢弃优先级映射表。

**[dscp-dscp**]**：**DSCP到DSCP映射表。

**[dscp-exp**]**：**DSCP到EXP映射表。

**[dscp-lp**]**：**DSCP到本地优先级映射表。

**[dscp-rpr**]**：**DSCP到RPR优先级映射表。

**[exp-dot1p**]**：**EXP到802.1p优先级映射表。

**[exp-dp**]**：**EXP到丢弃优先级映射表。

**[exp-dscp**]**：**EXP到DSCP映射表。

**[exp-exp**]**：**EXP到EXP映射表。

**[exp-lp**]**：**EXP到本地优先级映射表。

**[exp-rpr**]**：**EXP到RPR优先级映射表

**[ippre-rpr**]**：**IP优先级到RPR优先级映射表。

**[lp-dot11e**]**：**本地优先级到802.11e优先级映射表。

**[lp-dot1p**]**：**本地优先级到802.1p优先级映射表。

**[lp-dp**]**：**本地优先级到丢弃优先级映射表。

**[lp-dscp**]**：**本地优先级到DSCP映射表。

**[lp-exp**]**：**本地优先级到EXP映射表。

**[lp-lp**]**：**本地优先级到本地优先级映射表。

**[up-dot1p**]：用户优先级到802.1p优先级映射表。

**[up-dp**]：用户优先级到丢弃优先级映射表。

**[up-dscp**]：用户优先级到DSCP映射表。

**[up-exp**]：用户优先级到EXP映射表。

**[up-fc**]：用户优先级到转发类映射表。

**[up-lp**]：用户优先级到本地优先级映射表。

**[up-rpr**]：用户优先级到RPR优先级映射表。

**[up-up**]：用户优先级到用户优先级映射表。

【举例】

\# 使用DSCP到丢弃优先级映射表为报文获取丢弃优先级参数。

\<Sysname\> system-view

Sysname traffic behavior behavior1

Sysname-behavior-behavior1 primap pre-defined dscp-dp

【相关命令】

·**display qos map-table**

·**primap color-map-dp**

·**primap pre-defined color**

**QoS策略 \-- 定义流行为的命令 \-- primap pre-defined color**

------------------------------------------------------------------------

**[primap pre-defined color**]命令用来配置流行为中的动作为使用相应的带颜色优先级映射表为报文获取其他的优先级参数。

**[undo primap pre-defined color**]命令用来取消流行为中的使用相应的带颜色优先级映射表为报文映射优先级的动作。

【命令】

**[primap**[ **pre-defined** **color** { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]]

**[undo primap**[ **pre-defined** **color** { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]]

【缺省情况】

没有配置流优先级映射动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pre-defined**]：预先定义的优先级映射表。

**[color**]：使用带颜色优先级映射表做映射。

**[dot11e-lp**]：802.11e优先级到本地优先级映射表。

**[dot1p-dot1p**]：802.1p优先级到802.1p优先级映射表。

**[dot1p-dp**]：802.1p优先级到丢弃优先级映射表。

**[dot1p-dscp**]：802.1p优先级到DSCP映射表。

**[dot1p-exp**]：802.1p优先级到EXP映射表。

**[dot1p-lp**]**：**802.1p优先级到本地优先级映射表。

**[dot1p-rpr**]：802.1p优先级到RPR优先级映射表

**[dscp-dot1p**]**：**DSCP到802.1p优先级映射表。

**[dscp-dp**]：DSCP到丢弃优先级映射表。

**[dscp-dscp**]：DSCP到DSCP映射表。

**[dscp-exp**]：DSCP到EXP映射表。

**[dscp-lp**]：DSCP到本地优先级映射表。

**[dscp-rpr**]**：**DSCP到RPR优先级映射表

**[exp-dot1p**]：EXP到802.1p优先级映射表。

**[exp-dp**]：EXP到丢弃优先级映射表。

**[exp-dscp**]：EXP到DSCP映射表。

**[exp-exp**]：EXP到EXP映射表。

**[exp-lp**]：EXP到本地优先级映射表。

**[exp-rpr**]：EXP到RPR优先级映射表。

**[ippre-rpr**]**：**IP优先级到RPR优先级映射表。

**[lp-dot11e**]**：**本地优先级到802.11e优先级映射表。

**[lp-dot1p**]：本地优先级到802.1p优先级映射表。

**[lp-dp**]**：**本地优先级到丢弃优先级映射表。

**[lp-dscp**]**：**本地优先级到DSCP映射表。

**[lp-exp**]：本地优先级到EXP映射表。

**[lp-lp**]**：**本地优先级到本地优先级映射表

**[up-dot1p**]：用户优先级到802.1p优先级映射表。

**[up-dp**]：用户优先级到丢弃优先级映射表。

**[up-dscp**]：用户优先级到DSCP映射表。

**[up-exp**]：用户优先级到EXP映射表。

**[up-fc**]：用户优先级到转发类映射表。

**[up-lp**]：用户优先级到本地优先级映射表。

**[up-rpr**]：用户优先级到RPR优先级映射表。

**[up-up**]：用户优先级到用户优先级映射表。

【使用指导】

本命令需要和CAR结合在一起使用。

【举例】

\# 使用带颜色的DSCP到丢弃优先级映射表为报文获取丢弃优先级参数。

\<Sysname\> system-view

Sysname traffic behavior behavior1

Sysname-behavior-behavior1 car cir 1600

Sysname-behavior-behavior1 primap pre-defined color dscp-dp

【相关命令】

·**display qos map-table color**

·**primap color-map-dp**

·**primap pre-defined **

**QoS策略 \-- 定义流行为的命令 \-- redirect**

------------------------------------------------------------------------

**[redirect**]命令用来为流行为配置流量重定向动作。

**[undo redirect**]命令用来取消流量重定向动作配置。

【命令】

集中式设备：

**[redirect**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* [ **vlan** *vlan-id* ] \| **vsi** *vsi-name* }]]

**[undo redirect**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \| **vsi** *vsi-name* }]]

分布式设备-独立运行模式/集中式IRF设备：

**[redirect**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* [ **vlan** *vlan-id* ] \| **vsi** *vsi-name* \| **slot** *slot-number* }]]

**[undo redirect**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \| **vsi** *vsi-name* \| **slot** *slot-number* }]]

分布式设备-IRF模式：

**[redirect**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* [ **vlan** *vlan-id* ] \| **vsi** *vsi-name* \| **chassis** *chassis-number* **slot** *slot-number* }]]

**[undo redirect**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \| **vsi** *vsi-name* \| **chassis** *chassis-number* **slot** *slot-number* }]]

【缺省情况】

没有配置流量重定向动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cpu**]：重定向到CPU。

**[failover-group ***group-name*]：重定向到备份组。*group-name*表示备份组的名称，为1～63个字符的字符串，区分大小写。

**[interface**]：重定向到指定的接口。

*[interface-type interface-number*]：指定接口类型和接口编号（对于重定向到隧道来说，接口类型是**tunnel**；对于重定向到二层聚合接口来说，接口类型是**bridge-aggregation**；对于重定向到三层聚合接口来说，接口类型是**route-aggregation**）。

**[vlan*** vlan-id*]：对重定向到接口的报文封装的VLAN。*vlan-id*为封装的VLAN ID，取值范围为1～4094。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vsi*** vsi-name*]：重定向到指定VSI（Virtual Station Interface，虚拟服务器接口）。*vsi-name*：表示指定的VSI名称，为1～31个字符的字符串，区分大小写。

**[slot**]* slot-number*：重定向到指定的单板，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：重定向到指定成员设备，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：重定向到指定成员设备/PEX，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：重定向到指定成员设备上的指定单板，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[chassis**] *chassis-number* **slot** *slot-number*：重定向到指定的单板，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

在配置重定向动作时，同一个流行为中重定向类型只能为重定向到CPU、重定向到接口、重定向到VSI、重定向到单板、重定向到备份组中的一种，以最后一次配置为准。

【举例】

\# 为流行为配置流量重定向动作，重定向到CPU cpu。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database redirect cpu

\# 为流行为配置流量重定向动作，重定向到接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database redirect interface gigabitethernet1/0/1

\# 为流行为配置流量重定向动作，重定向到VSI aaa。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database redirect vsi aaa

\# 为流行为配置流量重定向动作，重定向到3号单板。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database redirect slot 3

\# 为流行为配置流量重定向动作，重定向到备份组bakgrp1。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database redirect failover-group bakgrp1

【相关命令】

·**classifier behavior**

·**qos policy**

·**traffic behavior**

**QoS策略 \-- 定义流行为的命令 \-- remark customer-vlan-id**

------------------------------------------------------------------------

**[remark customer-vlan-id**]命令用来重标记报文的CVLAN。

**[undo remark customer-vlan-id**]命令用来取消重标记报文的CVLAN。

【命令】

**[remark customer-vlan-id** *vlan-id*]

**[undo remark customer-vlan-id**]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：表示重标记报文内层VLAN（CVLAN）的编号，取值范围为1～4094。

【举例】

\# 在流行为b1上配置重标记报文的CVLAN为VLAN 111。

\<Sysname\> system-view

Sysname traffic behavior b1

Sysname-behavior-b1 remark customer-vlan-id 111

**QoS策略 \-- 定义流行为的命令 \-- remark dot1p**

------------------------------------------------------------------------

**[remark dot1p**]命令用来重新标记报文的802.1p优先级或配置内外层标签优先级复制功能。

**[undo remark dot1p**]命令用来取消标记报文的802.1p优先级或内外层标签优先级复制功能。

【命令】

**[remark **[[ **green** \| **red** \| **yellow** ] **dot1p** *dot1p-value*]]

**[undo remark **[[ **green** \| **red** \| **yellow** ] **dot1p**]]

**[remark** **dot1p** **customer-dot1p-trust**]

**[undo remark** **dot1p**]

【缺省情况】

没有配置重新标记报文的动作或没有配置内外层标签优先级复制功能。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[red**]：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[yellow**]：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[dot1p-value*]：802.1p优先级，取值范围为0～7。

**[customer-dot1p-trust**]：QoS策略应用到端口后，将内层VLAN tag的802.1p优先级复制为外层VLAN tag的802.1p优先级。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

命令**remark dot1p ***dot1p-value*和**remark dot1p customer-dot1p-trust**是覆盖关系。

如果报文只携带一层VLAN tag，则配置**remark dot1p customer-dot1p-trust**不会生效。

【举例】

\# 重新标记报文的802.1p优先级值为2。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark dot1p 2

\# 配置内外层标签优先级复制功能。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark dot1p customer-dot1p-trust

**QoS策略 \-- 定义流行为的命令 \-- remark drop-precedence**

------------------------------------------------------------------------

**[remark drop-precedence**]命令用来重新标记报文的丢弃优先级。

**[undo remark drop-precedence**]命令用来恢复缺省情况。

【命令】

**[remark drop-precedence** *drop-precedence-value*]

**[undo remark drop-precedence**]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[drop-precedence-value*]：丢弃优先级，取值范围为0～2。

【使用指导】

本命令仅应用在入方向。

【举例】

\# 重新标记报文的丢弃优先级值为2。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark drop-precedence 2

**QoS策略 \-- 定义流行为的命令 \-- remark dscp**

------------------------------------------------------------------------

**[remark dscp**]命令用来重新标记报文的DSCP值。

**[undo remark dscp**]命令用来取消标记报文的DSCP值。

【命令】

**[remark **[[ **green** \| **red** \| **yellow** ] **dscp** *dscp-value*]]

**[undo remark **[[ **green** \| **red** \| **yellow** ] **dscp**]]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[red**]：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[yellow**]：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[dscp-value*]：DSCP值，取值范围为0～63，也可以是关键字，如[表]1-5(?-580725274#_Ref163816081)所示。

表1-5 DSCP关键字与值的对应表

关键字

DSCP值（二进制）

DSCP值（十进制）

default

000000

0

af11

001010

10

af12

001100

12

af13

001110

14

af21

010010

18

af22

010100

20

af23

010110

22

af31

011010

26

af32

011100

28

af33

011110

30

af41

100010

34

af42

100100

36

af43

100110

38

cs1

001000

8

cs2

010000

16

cs3

011000

24

cs4

100000

32

cs5

101000

40

cs6

110000

48

cs7

111000

56

ef

101110

46

【举例】

\# 重新标记报文的DSCP值为6。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark dscp 6

**QoS策略 \-- 定义流行为的命令 \-- remark ip-precedence**

------------------------------------------------------------------------

**[remark ip-precedence**]命令用来重新标记报文的IP优先级。

**[undo remark ip-precedence**]命令用来取消标记报文的IP优先级。

【命令】

**[remark**[[ **green** \| **red** \| **yellow** ] **ip-precedence** *ip-precedence-value*]]

**[undo remark **[[ **green** \| **red** \| **yellow** ] **ip-precedence**]]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[red**]：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[yellow**]：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-precedence-value*]：IP优先级，取值范围为0～7。

【举例】

\# 重新标记报文的IP优先级值为6。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark ip-precedence 6

**QoS策略 \-- 定义流行为的命令 \-- remark local-precedence**

------------------------------------------------------------------------

**[remark local-precedence**]命令用来重新标记报文的本地优先级。

**[undo remark local-precedence**]命令用来取消标记报文的本地优先级。

【命令】

**[remark **[[ **green** \| **red** \| **yellow** ] **local-precedence** *local-precedence-value*]]

**[undo remark **[[ **green** \| **red** \| **yellow** ] **local-precedence**]]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[red**]：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[yellow**]：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[local-precedence-value*]：本地优先级，取值范围为0～7。

【举例】

\# 重新标记报文的本地优先级值为2。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark local-precedence 2

**QoS策略 \-- 定义流行为的命令 \-- remark qos-local-id**

------------------------------------------------------------------------

**[remark qos-local-id**]命令用来重新标记报文的QoS本地ID值。

**[undo remark qos-local-id**]命令用来恢复缺省情况。

【命令】

**[remark qos-local-id ***local-id-value*]

**[undo remark qos-local-id**]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[local-id-value*]：QoS本地ID值，取值范围为1～4095。

【使用指导】

一般情况下，在QoS策略的入方向对报文的QoS本地ID值进行标记，在QoS策略的出方向根据标记的QoS本地ID值对报文进行分类以及指定相应的流行为，两者要结合使用。

【举例】

\# 重新标记报文的QoS本地ID值为2。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark qos-local-id 2

**QoS策略 \-- 定义流行为的命令 \-- remark service-vlan-id**

------------------------------------------------------------------------

**[remark service-vlan-id**]命令用来重标记报文的SVLAN。

**[undo remark service-vlan-id**]命令用来取消重标记报文的SVLAN。

【命令】

**[remark service-vlan-id ***vlan-id*]

**[undo remark service-vlan-id**]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：表示重标记报文外层VLAN（SVLAN）的编号，取值范围为1～4094。

【举例】

\# 在流行为b1上配置重标记报文的SVLAN为VLAN 222。

\<Sysname\> system-view

Sysname traffic behavior b1

Sysname-behavior-b1 remark service-vlan-id 222

**QoS策略 \-- 定义流行为的命令 \-- traffic behavior**

------------------------------------------------------------------------

**[traffic behavior**]命令用来定义一个流行为，并进入流行为视图。

**[undo traffic behavior**]命令用来删除一个流行为。

【命令】

**[traffic behavior** *behavior-name*]

**[undo traffic behavior** *behavior-name*]

【缺省情况】

没有定义流行为。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[behavior-name*]：流行为名，为1～31个字符的字符串，区分大小写。

【举例】

\# 定义一个名为behavior1的流行为。

\<Sysname\> system-view

Sysname traffic behavior behavior1

Sysname-behavior-behavior1

【相关命令】

·**display traffic behavior**

**QoS策略 \-- 定义流行为的命令 \-- traffic-policy**

------------------------------------------------------------------------

**[traffic-policy**]命令用来在父策略流行为视图下应用一个子策略。

**[undo traffic-policy**]命令用来删除关联的子策略。

【命令】

**[traffic-policy** *policy-name*]

**[undo traffic-policy**]

【缺省情况】

没有配置嵌套策略。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，为1～31个字符的字符串，区分大小写。如果策略不存在，则自动创建该策略。

【使用指导】

通过在流行为视图下应用子策略，可以实现策略嵌套功能。即由**traffic classifier**命令定义的某一类流量，除了执行父策略中定义的行为外，还由子策略再次对该类流量进行分类，并执行子策略中定义的行为。

需要注意的是：

·在父策略行为下应用子策略时，最多只能嵌套二层策略，并且不能嵌套自己。

·一个流行为中至多只能嵌套一个子策略。

·如果子策略中配置了CBQ，那么父策略中必须配置GTS，并且配置的父策略GTS带宽必须大于子策略CBQ带宽，否则配置失败。

·嵌套策略时，如果父策略的GTS配置采用百分比形式，则子策略CBQ带宽配置不允许采用绝对值形式；如果父策略的GTS配置采用绝对值形式，则子策略CBQ带宽配置既可以采用百分比形式，也可以采用绝对值形式。

·子策略中不允许配置GTS。

·嵌套策略支持对IPv4、IPv6报文的处理。

·如果嵌套策略已经应用在接口上，则不允许删除嵌套的子策略，必须先解除子策略和父策略的嵌套关系。

【举例】

\# 配置策略嵌套，在父策略下应用子策略child。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database traffic-policy child

【相关命令】

·**traffic classifier**

·**traffic behavior**

**QoS策略 \-- 定义策略和应用策略的命令 \-- classifier behavior**

------------------------------------------------------------------------

**[classifier behavior**]命令用来为类指定流行为。

**[undo classifier**]命令用来取消为类指定的流行为。

【命令】

**[classifier**[ *classifier-name* **behavior** *behavior-name* [ **mode** { **dcbx** \| **qppb-manipulation** } ]]]

**[undo classifier*** classifier-name*]

【缺省情况】

没有为类指定流行为。

【视图】

策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[classifier-name*]：类名，为1～31个字符的字符串，区分大小写。

*[behavior-name*]：流行为名，为1～31个字符的字符串，区分大小写。

**[mode dcbx**]：表示该策略为DCBX（Data Center Bridging Exchange Protocol，数据中心桥能力交换协议）模式。有关DCBX的介绍，请参见"二层技术-以太网交换配置指导"中的"LLDP"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode qppb-manipulation**]：设置类和流行为对应关系用于匹配BGP路由策略中**apply qos-local-id**的信息。即类中**if-match qos-local-id**匹配的内容对应路由策略命令中**apply qos-local-id**命令设置的信息，具体内容请参见"三层技术-IP路由配置指导"中的"路由策略"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·策略下每个类只能与一个流行为关联。

·如果配置本命令时指定的类和流行为不存在，系统将创建一个空的类和空的流行为。

·如果**undo**命令指定的类为系统预定义类default-class，表示恢复default-class对应的流行为为系统预定义流行为be，而不是取消对应的流行为。

[·如果配置了**mode****[{ **dcbx** \| **qppb-manipulation** }]]参数，对于类和流行为的配置会存在一些特殊限制，请以设备的实际情况为准。

【举例】

\# 在策略user1中为类database指定采用流行为test。

\<Sysname\> system-view

Sysname qos policy user1

Sysname-qospolicy-user1 classifier database behavior test

\# 在策略user1中为类database指定采用流行为test，对应关系用于匹配BGP路由策略中**apply qos-local-id**的信息。

\<Sysname\> system-view

Sysname qos policy user1

Sysname-qospolicy-user1 classifier database behavior test mode qppb-manipulation

【相关命令】

·**qos policy**

**QoS策略 \-- 定义策略和应用策略的命令 \-- control-plane**

------------------------------------------------------------------------

**[control-plane**]命令用来进入控制平面视图。

【命令】

集中式设备：

**[control-plane**]

分布式设备－独立运行模式/集中式IRF设备：

**[control-plane** **slot** *slot-number*  **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[control-plane chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：指定单板。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：指定成员设备。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：指定成员设备/PEX。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定CPU，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 进入控制平面视图。（集中式设备）

\<Sysname\> system-view

Sysname control-plane

Sysname-cp

\# 进入3号板控制平面视图。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname control-plane slot 3

Sysname-cp-slot3

\# 进入3号成员设备控制平面视图。（集中式IRF设备）

\<Sysname\> system-view

Sysname control-plane slot 3

Sysname-cp-slot3

\# 进入1号成员设备3号板控制平面视图。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname control-plane chassis 1 slot 3

Sysname-cp-chassis1-slot3

**QoS策略 \-- 定义策略和应用策略的命令 \-- control-plane management**

------------------------------------------------------------------------

**[control-plane management**]命令用来进入管理口控制平面视图。

【命令】

**[control-plane management**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入管理口控制平面视图。

\<Sysname\> system-view

Sysname control-plane management

Sysname-cp-management

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy**

------------------------------------------------------------------------

**[display qos policy**]命令用来显示QoS策略的配置信息。

【命令】

集中式设备：

**[display qos policy**[ { **system-defined** \| **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos policy**[ { **system-defined** \| **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ]  **slot**]*slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display qos policy**[ { **system-defined** \| **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] ]**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[system-defined**]：系统定义策略。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[user-defined**]：用户定义策略。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

*[policy-name*]：策略名，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示所有用户定义策略的配置信息。

**[classifier*** classifier-name*]：策略中的类名，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示策略中所有类相关的配置信息。

**[slot**]* slot-number*：显示指定单板的策略的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的QoS策略的配置信息。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的策略的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备的QoS策略的配置信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的策略的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的策略的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的策略的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的QoS策略的配置信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的策略的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的策略的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上策略的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示用户定义策略的配置信息。

\<Sysname\> display qos policy user-defined

  User-defined QoS policy information:

  Policy: 1 (ID 100)

   Classifier: 1 (ID 100)

     Behavior: 1

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

   Classifier: 2 (ID 101)

     Behavior: 2

      Accounting enable: Packet

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

   Classifier: 3 (ID 102)

     Behavior: 3

      -none-

\# 显示系统定义策略的配置信息。

\<Sysname\> display qos policy system-defined

  System-defined QoS policy information:

  Policy: default (ID 0)

   Classifier: default-class (ID 0)

     Behavior: be

      -none-

   Classifier: ef (ID 1)

     Behavior: ef

      Expedited Forwarding:

        Bandwidth 20 (%) Cbs-ratio 25

   Classifier: af1 (ID 2)

     Behavior: af

      Assured Forwarding:

        Bandwidth 20 (%)

        Discard Method: Tail

   Classifier: af2 (ID 3)

     Behavior: af

      Assured Forwarding:

        Bandwidth 20 (%)

        Discard Method: Tail

   Classifier: af3 (ID 4)

     Behavior: af

      Assured Forwarding:

        Bandwidth 20 (%)

        Discard Method: Tail

   Classifier: af4 (ID 5)

     Behavior: af

      Assured Forwarding:

        Bandwidth 20 (%)

        Discard Method: Tail

表1-6 display qos policy命令显示信息描述表

字段

描述

User-defined QoS policy information

用户自定义策略的信息

System-defined QoS policy information

系统定义策略的信息

Policy

策略名

其它显示信息解释请参见 表1-1(?-524958785#_Ref298418803)和[表]1-4(?-308098617#_Ref298418812)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane**

------------------------------------------------------------------------

**[display qos policy control-plane**]命令用来显示控制平面应用QoS策略的信息。

【命令】

集中式设备：

**[display qos policy control-plane**]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos policy control-plane** **slot** *slot-number*  **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display qos policy control-plane****chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的控制平面应用QoS策略的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的控制平面应用QoS策略的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的控制平面应用QoS策略的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的控制平面应用QoS策略的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的控制平面应用QoS策略的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上控制平面应用QoS策略的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示应用到控制平面的QoS策略信息。

\<Sysname\> display qos policy control-plane

Control plane

  Direction: Inbound

  Policy: 1

   Classifier: 1

     Operator: AND

     Rule(s) :

      If-match acl 2000

     Behavior: 1

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0 (Packets) 0 (Bytes)

        Yellow packets: 0 (Packets) 0 (Bytes)

        Red packets   : 0 (Packets) 0 (Bytes)

   Classifier: 2

     Operator: AND

     Rule(s) :

      If-match not protocol ipv6

     Behavior: 2

      Accounting enable:

        0 (Packets)

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

   Classifier: 3

     Operator: AND

     Rule(s) :

      -none-

     Behavior: 3

      -none-

表1-7 display qos policy control-plane命令显示信息描述表

字段

描述

Direction

对进入控制平面（Inbound）的报文应用QoS策略

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见表 1-6(#_0_14687_18620_x1163520085)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane management**

------------------------------------------------------------------------

**[display qos policy control-plane management**]命令用于显示管理口控制平面应用的QoS策略信息。

【命令】

**[display qos policy control-plane management**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示对进入管理口控制平面的报文应用的QoS策略信息。

\<Sysname\> display qos policy control-plane management

Control plane management

  Direction: Inbound

  Policy: a

   Classifier: default-class

     Matched : 0 (Packets) 0 (Bytes)

     Operator: AND

     Rule(s) :

      If-match any

     Behavior: be

      -none-

   Classifier: a

     Matched : 3 (Packets) 180 (Bytes)

     Operator: OR

     Rule(s) :

      If-match control-plane protocol arp

      If-match control-plane protocol rip

      If-match control-plane protocol-group critical

      If-match acl 3001

      If-match control-plane protocol bgp

      If-match control-plane protocol bgp4+

      If-match control-plane protocol ftp

      If-match control-plane protocol http https icmp icmp6 ripng snmp

     Behavior: a

      Committed Access Rate:

        CIR 128 (kbps), CBS 8000 (Bytes), EBS 0 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 3 (Packets) 180 (Bytes)

        Yellow packets: 0 (Packets) 0 (Bytes)

        Red packets   : 0 (Packets) 0 (Bytes)

表1-8 display qos policy control-plane management命令显示信息描述表

字段

描述

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见表 1-6(#_0_14687_18620_x1163520085)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane management pre-defined**

------------------------------------------------------------------------

**[display qos policy control-plane management pre-defined**]命令用来显示系统预定义的管理口控制平面应用QoS策略的信息。

【命令】

**[display qos policy control-plane management pre-defined**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示系统预定义的管理口控制平面应用QoS策略的信息。

\<Sysname\> display qos policy control-plane management pre-defined

Pre-defined control plane policy management

  Protocol          Priority   Bandwidth (kbps)   Group

  Default           N/A        100000             N/A

  ARP               N/A        128                normal

  BGP               N/A        256                critical

  BGPv6             N/A        256                critical

  HTTP              N/A        512                management

  HTTPS             N/A        512                management

  ICMP              N/A        128                monitor

  ICMPv6            N/A        128                monitor

  OSPF Multicast    N/A        256                critical

  OSPF Unicast      N/A        256                critical

  OSPFv3 Multicast  N/A        256                critical

  OSFPv3 Unicast    N/A        256                critical

  RIP               N/A        1024               critical

  RIPng             N/A        256                critical

  SNMP              N/A        512                management

  SSH               N/A        512                management

  TELNET            N/A        512                management

  FTP               N/A        512                management

  TFTP              N/A        512                management

表1-9 display qos policy control-plane management pre-defined命令显示信息描述表

字段

描述

Pre-defined control plane policy management

预定义管理口控制平面策略内容

Protocol

系统预定义协议报文类型

Priority

优先级

Bandwidth

带宽

Group

协议组

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane pre-defined**

------------------------------------------------------------------------

**[display qos policy control-plane pre-defined**]命令用来显示系统预定义的控制平面应用QoS策略的信息。

【命令】

集中式设备：

**[display qos policy control-plane** **pre-defined**]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos policy control-plane** **pre-defined** [ **slot** *slot-number*  **cpu** *cpu-number* ] ]

分布式设备－IRF模式：

**[display qos policy control-plane** **pre-defined** \**[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的系统预定义的控制平面策略信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的系统预定义的控制平面策略信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的系统预定义的控制平面策略信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-numbe*r]：显示指定成员设备上指定单板的系统预定义的控制平面策略信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的系统预定义的控制平面策略信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上系统预定义的控制平面策略信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

·如果不指定槽位号，则显示所有在位单板的系统预定义的控制平面应用QoS策略的信息。（分布式设备－独立运行模式）

·如果不指定成员编号，则显示所有成员设备的系统预定义的控制平面应用QoS策略的信息。（集中式IRF设备）

·如果不指定成员编号和槽位号，则显示所有成员设备上在位单板的系统预定义的控制平面应用QoS策略的信息。（分布式设备－IRF模式）

【举例】

\# 显示3号板系统预定义的控制平面应用QoS策略的信息。（分布式设备－独立运行模式）

\<Sysname\> display qos policy control-plane pre-defined slot 3

Pre-defined control plane policy slot 3

  Protocol          Priority   Bandwidth (kbps)

  ARP               1          1000

  ARP Snooping      2          2000

  BGP               3          3000

  BGPv6             4          4000

  BPDU Tunnel       5          5000

  CDP               6          6000

  CFD               7          7000

  DHCP              0          8000

  DHCP Snooping     1          9000

  DHCPv6            2          10000

\# 显示3号成员设备系统预定义的控制平面应用QoS策略的信息。（集中式IRF设备）

\<Sysname\> display qos policy control-plane pre-defined slot 3

Pre-defined control plane policy slot 3

  Protocol          Priority   Bandwidth (kbps)

  ARP               1          1000

  ARP Snooping      2          2000

  BGP               3          3000

  BGPv6             4          4000

  BPDU Tunnel       5          5000

  CDP               6          6000

  CFD               7          7000

  DHCP              0          8000

  DHCP Snooping     1          9000

  DHCPv6            2          10000

\# 显示1号成员设备3号单板系统预定义的控制平面应用QoS策略的信息。（分布式设备－IRF模式）

\<Sysname\> display qos policy control-plane pre-defined chassis 1 slot 3

Pre-defined control plane policy chassis 1 slot 3

  Protocol          Priority   Bandwidth (kbps)

  ARP               1          1000

  ARP Snooping      2          2000

  BGP               3          3000

  BGPv6             4          4000

  BPDU Tunnel       5          5000

  CDP               6          6000

  CFD               7          7000

  DHCP              0          8000

  DHCP Snooping     1          9000

  DHCPv6            2          10000

表1-10 display qos policy control-plane pre-defined命令显示信息描述表

字段

描述

Pre-defined control plane policy

预定义控制平面策略内容

Protocol

系统预定义协议报文类型

Priority

优先级

Bandwidth

带宽

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy global**

------------------------------------------------------------------------

**[display** **qos policy global**]命令用来显示基于全局应用QoS策略的信息。

【命令】

集中式设备：

**[display qos policy global**[ [ **inbound** \| **outbound** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos policy global** [ **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

分布式设备－IRF模式：

**[display qos policy global** \**[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]：显示对全局接收到的报文应用QoS策略的信息。

**[outbound**]：显示对全局发送的报文应用QoS策略的信息。

**[slot*** slot-number*]：显示指定单板的基于全局应用QoS策略的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的基于全局应用QoS策略的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的基于全局应用QoS策略的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的基于全局应用QoS策略的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的基于全局应用QoS策略的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上基于全局应用QoS策略的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

·如果未指定显示方向，则同时显示出入两个方向基于全局应用QoS策略的信息。

·如果未指定槽位号，则显示主用主控板上基于全局应用QoS策略的信息，不显示各单板的信息。（分布式设备－独立运行模式）

·如果未指定成员编号，则显示主设备上基于全局应用QoS策略的信息，不显示各成员设备的信息。（集中式IRF设备）

·如果未指定成员编号和槽位号，则显示全局主用主控板上基于全局应用QoS策略的信息，不显示各单板的信息。（分布式设备－IRF模式）

【举例】

\# 显示基于全局应用QoS策略的信息。

\<Sysname\> display qos policy global inbound

  Direction: Inbound

  Type     : Extension

  Policy: 1

   Classifier: 1

     Operator: AND

     Rule(s) :

      If-match acl 2000

     Behavior: 1

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0 (Packets) 0 (Bytes)

        Yellow packets: 0 (Packets) 0 (Bytes)

        Red packets   : 0 (Packets) 0 (Bytes)

   Classifier: 2

     Operator: AND

     Rule(s) :

      If-match not protocol ipv6

     Behavior: 2

      Accounting enable:

        0 (Packets)

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

   Classifier: 3

     Operator: AND

     Rule(s) :

      -none-

     Behavior: 3

      -none-

表1-11 display qos policy global命令显示信息描述表

字段

描述

Direction

对接收到（Inbound）/发送（Outbound）的报文应用QoS策略

Type

策略的应用类型，与应用策略的命令对应。应用时没有指定类型时，显示信息中也没有此字段。取值有：

·Enhancement：增强型

·Extension：扩展型

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见 表1-1(?-524958785#_Ref298418803)和[表]1-4(?-308098617#_Ref298418812)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy interface**

------------------------------------------------------------------------

**[display qos policy interface**]命令用来显示接口上QoS策略的配置信息和运行情况。

【命令】

集中式设备：

**[display qos policy interface **[[ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ]   **inbound** \| **outbound** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos policy interface **[[ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]  **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

分布式设备－IRF模式：

**[display qos policy interface **[[ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口上QoS策略的配置信息和运行情况。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的QoS策略的配置信息和运行情况。输入本参数时，无法输入参数**inbound**或**outbound**。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot*** slot-number*]：显示指定单板上指定接口的QoS策略的配置信息和运行情况。*slot-number*表示单板所在的槽位号。只有当接口为VLAN接口、聚合接口等类型时才支持此参数。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备指定接口的QoS策略的配置信息和运行情况。*slot-number*表示设备在IRF中的成员编号。只有当接口为VLAN虚接口、聚合口等类型时才支持此参数。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的指定接口的QoS策略的配置信息和运行情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。只有当接口为VLAN虚接口、聚合口等类型时才支持此参数。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的指定接口的QoS策略的配置信息和运行情况。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。只有当接口为VLAN虚接口、聚合口等类型时才支持此参数。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的指定接口的QoS策略的配置信息和运行情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。只有当接口为VLAN虚接口、聚合口等类型时才支持此参数。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上QoS策略的配置信息和运行情况，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[inbound**]：显示对接口接收到的报文应用QoS策略的信息。

**[outbound**]：显示对接口发送的报文应用QoS策略的信息。

【使用指导】

·如果未指定显示方向，则同时显示出入两个方向接口上应用QoS策略的配置信息和运行情况。

·如果指定接口为Virtual-Template接口，将显示继承该Virtual-Template接口的所有Virtual-Access接口下的QoS策略的信息，Virtual-Template本身无QoS信息显示。

【举例】

\# 显示对接口GigabitEthernet1/0/1接收到的报文应用QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy interface gigabitethernet 1/0/1 inbound

Interface: GigabitEthernet1/0/1

  Direction: Inbound

  Policy: 1

   Classifier: 1

     Matched : 0 (Packets) 0 (Bytes)

     5-minute statistics:

      Forwarded: 0/0 (pps/bps)

      Dropped  : 0/0 (pps/bps)

     Operator: AND

     Rule(s) :

      If-match acl 2000

     Behavior: 1

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0 (Packets) 0 (Bytes)

        Yellow packets: 0 (Packets) 0 (Bytes)

        Red packets   : 0 (Packets) 0 (Bytes)

   Classifier: 2

     Matched : 0 (Packets) 0 (Bytes)

     5-minute statistics:

      Forwarded: 0/0 (pps/bps)

      Dropped  : 0/0 (pps/bps)

     Operator: AND

     Rule(s) :

      If-match not protocol ipv6

     Behavior: 2

      Accounting enable:

        0 (Packets)

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

   Classifier: 3

     Matched : 0 (Packets) 0 (Bytes)

     5-minute statistics:

      Forwarded: 0/0 (pps/bps)

      Dropped  : 0/0 (pps/bps)

     Operator: AND

     Rule(s) :

      -none-

     Behavior: 3

      -none-

\# 显示所有接口上QoS策略的接口的配置信息和运行情况。

\<Sysname\>dis qos policy interface

Interface: GigabitEthernet5/0/1

  Direction: Inbound

  Type     : Enhancement

  Policy: a

   Classifier: a

     Operator: AND

     Rule(s) :

      If-match any

     Behavior: a

      Mirroring:

        Mirror to the interface: GigabitEthernet5/0/10

      Committed Access Rate:

        CIR 100 (kbps), CBS 6250 (Bytes), EBS 0 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0 (Packets)

        Red packets   : 0 (Packets)

Interface: GigabitEthernet5/0/17

  Direction: Inbound

  Policy: b

   Classifier: b

     Operator: AND

     Rule(s) :

      If-match any

     Behavior: b

      Committed Access Rate:

        CIR 200 (kbps), CBS 12500 (Bytes), EBS 0 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0(Packets)

        Red packets   : 0 (Packets)

Interface: GigabitEthernet5/0/17

  Direction: Inbound

  Type     : Enhancement

  Policy: a

   Classifier: a

     Operator: AND

     Rule(s) :

      If-match any

     Behavior: a

      Mirroring:

        Mirror to the interface: GigabitEthernet5/0/10

      Committed Access Rate:

        CIR 100 (kbps), CBS 6250 (Bytes), EBS 0 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0 (Packets)

        Red packets   : 0 (Packets)

表1-12 display qos policy interface命令显示信息描述表

字段

描述

Direction

Policy应用在接口的方向

Type

策略的应用类型，与应用策略的命令对应。应用时没有指定类型时，显示信息中也没有此字段。取值有：

·Enhancement：增强型

·Extension：扩展型

Matched

符合分类规则的数据包数目

5-minute statistics

最近5分钟的流速统计信息

Forwarded

符合分类规则的成功转发报文在统计周期内的平均速率

Dropped

符合分类规则的丢弃报文在统计周期内的平均速率

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见 表1-1(?-524958785#_Ref298418803)和[表]1-4(?-308098617#_Ref298418812)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy l2vpn-pw**

------------------------------------------------------------------------

**[display qos policy l2vpn-pw**]命令用来显示L2VPN PW上QoS策略的配置信息和运行情况。

【命令】

**[display qos policy l2vpn-pw ** **peer** *ip-address* **pw-id** ]*pw-id *  **outbound**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer ***ip-address ***pw-id*** pw-id*]：显示指定PW上的QoS策略的配置信息和运行情况。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。若未指定本参数，则显示所有PW上的QoS策略的配置信息和运行情况。

**[outbound**]：显示对PW发送的报文应用的QoS策略的信息。

【使用指导】

如果未指定显示方向，则显示出方向PW上应用QoS策略的配置信息和运行情况。

【举例】

\# 显示远端PE地址为1.1.1.1、PW ID为1的PW发送报文方向上应用的QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy l2vpn-pw peer 1.1.1.1 pw-id 1 outbound

L2VPN-PW: peer 1.1.1.1, pw-id 1

  Direction: Outbound

  Policy: 1

   Classifier: 1

     Matched : 0 (Packets) 0 (Bytes)

     5-minute statistics:

      Forwarded: 0/0 (pps/bps)

      Dropped  : 0/0 (pps/bps)

     Operator: AND

     Rule(s) :

      If-match acl 2000

     Behavior: 1

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0 (Packets) 0 (Bytes)

        Yellow packets: 0 (Packets) 0 (Bytes)

        Red packets   : 0 (Packets) 0 (Bytes)

   Classifier: 2

     Matched : 0 (Packets) 0 (Bytes)

     5-minute statistics:

      Forwarded: 0/0 (pps/bps)

      Dropped  : 0/0 (pps/bps)

     Operator: AND

     Rule(s) :

      If-match not protocol ipv6

     Behavior: 2

      Accounting enable:

        0 (Packets)

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

   Classifier: 3

     Matched : 0 (Packets) 0 (Bytes)

     5-minute statistics:

      Forwarded: 0/0 (pps/bps)

      Dropped  : 0/0 (pps/bps)

     Operator: AND

     Rule(s) :

      -none-

     Behavior: 3

      -none-

表1-1 display qos policy l2vpn-pw命令显示信息描述表

字段

描述

L2VPN-PW

显示指定PW的信息，PW通过远端PE地址和PW ID唯一标识

Direction

Policy应用在PW的方向

Matched

符合分类规则的数据包数目

5-minute statistics

最近5分钟的流速统计信息

Forwarded

符合分类规则的成功转发报文在统计周期内的平均速率

Dropped

符合分类规则的丢弃报文在统计周期内的平均速率

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见 表1-1(?-524958785#_Ref298418803)和[表]1-4(?-308098617#_Ref298418812)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy user-profile**

------------------------------------------------------------------------

**[display** **qos policy** **user-profile**]命令用来显示用户上线后User Profile下应用的QoS策略的信息和运行情况。

【命令】

集中式设备：

**[display qos policy user-profile** [ **name** *profile-name*   **user-id** *user-id*  [ **inbound** \| **outbound** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **qos policy user-profile** [ **name** *profile-name*   **user-id** *user-id*   **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

分布式设备－IRF模式：

**[display** **qos policy user-profile** [ **name** *profile-name*   **user-id** *user-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

【缺省情况】

无

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***profile-name*]：指定User Profile的名称，为1～31个字符的字符串，只能包含英文字母a-z,A-Z、数字、下划线，且必须以英文字母开始，区分大小写。User Profile的名称必须全局唯一。如果未指定本参数，将显示所有UserProfile下应用的QoS策略的信息和运行情况。

**[user-id*** user-id*]：表示在线用户的ID，为系统所分配，为十六进制数。若未指定本参数，则显示所有用户在UserProfile下应用的QoS策略的信息和运行情况。

**[slot*** slot-number*]：显示指定单板上指定用户在User Profile下应用的QoS策略的信息和运行情况，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的在线用户的QoS策略的信息和运行情况。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上指定用户在User Profile下应用的QoS策略的信息和运行情况，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有成员设备上的在线用户上指定用户在User Profile下应用的QoS策略的信息和运行情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上指定用户在User Profile下应用的QoS策略的信息和运行情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有成员设备/PEX上上指定用户在User Profile下应用的QoS策略的信息和运行情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上指定用户在User Profile下应用的QoS策略的信息和运行情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有成员设备所有单板上指定用户在User Profile下应用的QoS策略的信息和运行情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上指定用户在User Profile下应用的QoS策略的信息和运行情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有单板上指定用户在User Profile下应用的QoS策略的信息和运行情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上指定用户在User Profile下应用的QoS策略的信息和运行情况，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[inbound**]：显示在线用户在入方向上应用QoS策略的信息。

**[outbound**]：显示在线用户在出方向上应用QoS策略的信息。

【使用指导】

如果未指定显示方向，则同时显示出入两个方向上应用QoS策略的配置信息和运行情况。

【举例】

\# 显示指定全局用户（从聚合口等全局口上线的用户）在User Profile下应用QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy user-profile name abc user-id 30000000 inbound

User-Profile: abc

  User ID: 0x30000000(global)

    Direction: Inbound

    Policy: p1

     Classifier: default-class

       Matched : 0 (Packets) 0 (Bytes)

       Operator: AND

       Rule(s) :

        If-match any

       Behavior: be

        -none-

\# 显示指定的非全局用户在User Profile下应用QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy user-profile name abc user-id 30000001 inbound

User-Profile: abc

  slot 2:

    User ID: 0x30000001(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

\# 显示指定User Profile下所有用户的QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy user-profile name abc inbound

User-Profile: abc

  User ID: 0x30000000(global)

    Direction: Inbound

    Policy: p1

     Classifier: default-class

       Matched : 0 (Packets) 0 (Bytes)

       Operator: AND

       Rule(s) :

        If-match any

       Behavior: be

        -none-

  slot 2:

    User ID: 0x30000001(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

  slot 3:

    User ID: 0x30000002(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

\# 显示指定单板上所有用户在User Profile abc下应用QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy user-profile name abc slot 2

User-Profile: abc

User ID: 0x30000000(global)

    Direction: Inbound

    Policy: p1

     Classifier: default-class

       Matched : 0 (Packets) 0 (Bytes)

       Operator: AND

       Rule(s) :

        If-match any

       Behavior: be

        -none-

  User ID: 0x30000001(local)

    Direction: Inbound

    Policy: p1

     Classifier: default-class

       Matched : 0 (Packets) 0 (Bytes)

       Operator: AND

       Rule(s) :

        If-match any

       Behavior: be

        -none-

\#显示所有单板上指定用户在User Profile abc下应用QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy user-profile name abc user-id 30000001

User-Profile: abc

  slot 2:

    User ID: 0x30000001(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

  slot 3:

    User ID: 0x30000001(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

\# 显示所有User Profile的在线用户的QoS策略的配置信息和运行情况。

\<Sysname\> display qos policy user-profile

User-Profile: abc

  slot 3:

    User ID: 0x30000000(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

User-Profile: a12

  slot 4:

    User ID: 0x30000001(local)

      Direction: Inbound

      Policy: p1

       Classifier: default-class

         Matched : 0 (Packets) 0 (Bytes)

         Operator: AND

         Rule(s) :

          If-match any

         Behavior: be

          -none-

       Classifier: a

        Operator: AND

        Rule(s) :

         If-match any

        Behavior: a

         Mirroring:

          Mirror to the interface: GigabitEthernet1/0/1

         Committed Access Rate:

           CIR 100 (kbps), CBS 6250 (Bytes), EBS 0 (Bytes)

           Green action  : pass

           Yellow action : pass

           Red action    : discard

           Green packets : 0 (Packets)

           Red packets   : 0 (Packets)

表1-13 display qos policy user-profile 命令显示信息描述表

字段

描述

User-Profile

User Profile名称

User ID

上线用户的ID

global

该用户从聚合口等全局口上线

local

该用户从物理口上线

Mirror to the interface

镜像到接口

CIR

承诺信息速率，单位为kbps

CBS

承诺突发尺寸，也就是容纳突发流量的令牌桶深度，单位为byte

EBS

超出突发尺寸，在双令牌桶算法中超出突发流量超过承诺突发流量的部分，单位为byte

PIR

峰值信息速率

Direction

Policy应用在User Profile的方向

Matched

符合分类规则的数据包数目

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见 表1-1(?-524958785#_Ref298418803)和[表]1-4(?-308098617#_Ref298418812)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos vlan-policy**

------------------------------------------------------------------------

**[display qos vlan-policy**]命令用来显示基于VLAN应用QoS策略的信息。

【命令】

集中式设备：

**[display qos vlan-policy **[{ **name** *policy-name* \| **vlan** [ *vlan-id* ] } [ **inbound** \| **outbound** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos vlan-policy **[{ **name** *policy-name* \| **vlan** [ *vlan-id* ] }  **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

分布式设备－IRF模式：

**[display qos vlan-policy **[{ **name** *policy-name* \| **vlan** [ *vlan-id* ] }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*    **inbound** \| **outbound** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name** *policy-name*]：显示指定策略名称的基于VLAN应用QoS策略的信息。*policy-name*表示策略名称，为1～31个字符的字符串，区分大小写。

**[vlan** *vlan-id*]：显示指定VLAN上应用QoS策略的信息。*vlan-id*为指定VLAN的ID号，取值范围为1～4094。

**[inbound**]：显示对VLAN接收到的报文应用的QoS策略信息。

**[outbound**]：显示对VLAN发送的报文应用的QoS策略信息。

**[slot*** slot-number*]：显示指定单板上基于VLAN应用QoS策略的信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上基于VLAN应用QoS策略的信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上基于VLAN应用QoS策略的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的基于VLAN应用QoS策略的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上基于VLAN应用QoS策略的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上基于VLAN应用QoS策略的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

·如果未指定显示方向，则同时显示出入两个方向基于VLAN应用QoS策略的信息。

·如果未指定槽位号，则显示主用主控板上基于VLAN应用QoS策略的信息。（分布式设备－独立运行模式）

·如果未指定成员编号，则显示主设备上基于VLAN应用QoS策略的信息。（集中式IRF设备）

·如果未指定成员编号和槽位号，则显示全局主用主控板上基于VLAN应用QoS策略的信息。（分布式设备－IRF模式）

【举例】

\# 显示VLAN 2的QoS策略信息。

\<Sysname\> display qos vlan-policy vlan 2

Vlan 2

  Direction: Outbound

  Type     : Extension

  Policy: 1

   Classifier: 1

     Operator: AND

     Rule(s) :

      If-match acl 2000

     Behavior: 1

      Marking:

        Remark dscp 3

      Committed Access Rate:

        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)

        Green action  : pass

        Yellow action : pass

        Red action    : discard

        Green packets : 0(Packets) 0(Bytes)

        Yellow packets: 0(Packets) 0(Bytes)

        Red packets   : 0(Packets) 0(Bytes)

   Classifier: 2

     Operator: AND

     Rule(s) :

      If-match not protocol ipv6

     Behavior: 2

      Accounting enable:

        0 (Packets)

      Filter enable: Permit

      Marking:

        Remark mpls-exp 4

   Classifier: 3

     Operator: AND

     Rule(s) :

      -none-

     Behavior: 3

      -none-

表1-14 display qos vlan-policy命令显示信息描述表

字段

描述

Direction

对VLAN接收到（Inbound）/发送（Outbound）的报文应用QoS策略

Type

策略的应用类型，与应用策略的命令对应。应用时没有指定类型时，显示信息中也没有此字段。取值有：

Extension：扩展型

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

其它显示信息解释请参见 表1-1(?-524958785#_Ref298418803)和[表]1-4(?-308098617#_Ref298418812)。

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos apply policy (interface view, PVC view, control plane view, control plane management view,PW view)**

------------------------------------------------------------------------

**[qos apply policy**]命令用来在接口、PVC、PW、控制平面或管理口控制平面上应用QoS策略。

**[undo qos apply policy**]命令用来取消接口、PVC、PW、控制平面或管理口控制平面上应用的QoS策略。

【命令】

**[qos apply policy*** policy-name*[ { **inbound** \| **outbound** } [ **enhancement** ]  **extension** ]]

**[undo qos apply policy**[ *policy-name* { **inbound** \| **outbound** } [ **enhancement** ]]]

【缺省情况】

没有在接口、PVC、控制平面、管理口控制平面或PW上应用QoS策略。

【视图】

接口视图/PVC视图/控制平面视图/管理口控制平面视图/交叉连接PW视图/VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，为1～31个字符的字符串，区分大小写。

**[inbound**]：对接口或控制平面或管理口控制平面接收到的报文应用QoS策略。

**[outbound**]：对接口发送的报文应用QoS策略。

**[enhancement**]：对策略增强应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[extension**]：对策略扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

策略在接口、PVC或PW上应用的规则如下：

·在应用策略时，如果策略中为确保转发和加速转发的类指定的带宽之和超过接口、PVC或PW允许的可用带宽，则在该接口、PVC或PW不可应用。如果对接口、PVC或PW修改了可用带宽，此时如果策略中为确保转发和加速转发的类指定的带宽之和超过接口、PVC或PW允许的可用带宽，则将策略删除。

·入方向的策略与类关联的行为不允许有**queue af**、**queue ef**与**queue wfq**配置，也不允许有GTS配置。

在控制平面和管理口控制平面上应用策略时，不支持配置了CBQ的策略。

在PW下应用策略时，只能应用在PW的出方向上。

在同一个接口的同一个方向上，可以同时应用增强类型和普通类型策略，意味着一个报文会被两个策略处理。增强型策略对报文的处理性能较高，但支持的参数不够丰富。

在同一个接口的同一个方向上，不能同时应用扩展类型和普通类型策略，二者取其一。扩展型策略可以使用更多的硬件资源，但支持的参数类型较少。

【举例】

\# 将策略USER1应用到接口GigabitEthernet1/0/1的出方向上。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/1 qos apply policy USER1 outbound

\# 对进入3号槽控制平面的报文应用策略aaa。

\<Sysname\> system-view

Sysname control-plane slot 3

Sysname-cp-slot3 qos apply policy aaa inbound

\# 对进入管理口控制平面的报文应用策略bbb。

\<Sysname\> system-view

Sysname control-plane management

Sysname-cp-management qos apply policy bbb inbound

\# 在PW的出方向上应用策略。

\<Sysname\> system-view

Sysname xconnect-group a

Sysname-xcg-a connection a

Sysname-xcg-a-a peer 1.1.1.1 pw-id 1

Sysname-xcg-a-a-1.1.1.1-1 qos apply policy 1 outbound

\# 将增强型策略aaa应用到接口GigabitEthernet5/0/1的出方向上。

\<Sysname\> system-view

Sysname interface GigabitEthernet5/0/1

Sysname-GigabitEthernet5/0/1qos apply policy aaa outbound enhancement

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos apply policy (user-profile view)**

------------------------------------------------------------------------

**[qos apply policy**]命令用来在User Profile下应用策略。

**[undo qos apply policy**]命令用来取消User Profile下应用的策略。

【命令】

**[qos apply policy*** policy-name*[ { **inbound** \| **outbound** }]]

**[undo qos apply policy**[ *policy-name* { **inbound** \| **outbound** }]]

【缺省情况】

没有在User Profile下应用QoS策略。

【视图】

User Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：入方向，对设备接收的上线用户流量（即上线用户发送的流量）应用策略。

**[outbound**]：出方向，对设备发送的上线用户流量（即上线用户接收的流量）应用策略。

*[policy-name*]：策略名，为1～31个字符的字符串。

【使用指导】

User Profile被删除将导致其下引用的QoS策略被删除。

【举例】

\# 对设备发送的上线用户user的流量应用策略test（该策略已经建立）。

\<Sysname\> system-view

Sysname user-profile user

Sysname-user-profile-user qos apply policy test outbound

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos apply policy global**

------------------------------------------------------------------------

**[qos apply policy global**]命令用来全局应用QoS策略。

**[undo qos apply policy global**]命令用来取消全局应用的QoS策略。

【命令】

**[qos apply policy ***policy-name*** global **[{ **inbound** \| **outbound** } [ **enhancement** ]  **extension** ]]

**[undo qos apply policy ***policy-name*[ **global** { **inbound** \| **outbound** }]]

【缺省情况】

没有在全局应用QoS策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，为1～31个字符的字符串，区分大小写。

**[inbound**]：对设备所有端口接收到的流量应用QoS策略。

**[outbound**]：对设备所有端口发送的流量应用QoS策略。

**[enhancement**]：对策略增强应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[extension**]**：**对策略扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

全局应用的QoS策略对全部流量生效。

在同一个接口的同一个方向上，可以同时应用增强类型和普通类型策略，意味着一个报文会被两个策略处理。增强型策略对报文的处理性能较高，但支持的参数不够丰富。

在全局的同一个方向上，不能同时应用扩展类型和普通类型策略，二者取其一。扩展型策略可以使用更多的硬件资源，但支持的参数类型较少。

【举例】

\# 将名为user1的扩展策略应用到全局的入方向上。

\<Sysname\> system-view

Sysname qos apply policy user1 global inbound extension

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos policy**

------------------------------------------------------------------------

**[qos policy**]命令用来定义一个策略，并进入策略视图。

**[undo qos policy**]命令用来删除一个策略。

【命令】

**[qos policy** *policy-name*]

**[undo qos policy** *policy-name*]

【缺省情况】

没有定义策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，为1～31个字符的字符串，区分大小写。

【使用指导】

如果该策略已经被应用，则不允许删除该策略，需要先在应用的位置上取消对该策略的应用，然后再使用**undo qos policy**命令删除该策略。

【举例】

\# 定义一个名为user1的策略。

\<Sysname\> system-view

Sysname qos policy user1

Sysname-qospolicy-user1

【相关命令】

·**classifier behavior**

·**qos apply policy**

·**qos apply policy global**

·**qos vlan-policy**

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos vlan-policy**

------------------------------------------------------------------------

**[qos vlan-policy**]命令用来在指定VLAN上应用QoS策略。

**[undo** **qos vlan-policy**]命令用来取消指定VLAN上应用的QoS策略。

【命令】

**[qos vlan-policy**[ *policy-name* **vlan** *vlan-id-list* { **inbound** \| **outbound** } [ **extension** ]]]

**[undo qos vlan-policy**[ *policy-name* **vlan** *vlan-id-list* { **inbound** \| **outbound** }]]

【缺省情况】

没有在指定VLAN上应用QoS策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名称，为1～31个字符的字符串，区分大小写。

*[vlan-id-list*]：VLAN ID列表，形式可以是*vlan-id ***to*** vlan-id*，其中，*vlan-id*为指定VLAN的ID号，取值范围为1～4094。可以输入多个不连续的VLAN ID，中间以空格隔开。设备最多允许用户同时指定8个VLAN ID。

**[inbound**]：对VLAN接收到的报文应用QoS策略。

**[outbound**]：对VLAN发送的报文应用QoS策略。

**[extension**]**：**对策略扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在同一个VLAN的同一个方向上，不能同时应用扩展类型和普通类型策略，二者取其一。扩展型策略可以使用更多的硬件资源，但支持的参数类型较少。

【举例】

\# 在VLAN 200、300、400、500的入方向上扩展应用VLAN策略test。

\<Sysname\> system-view

Sysname qos vlan-policy test vlan 200 300 400 500 inbound extension

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos policy control-plane**

------------------------------------------------------------------------

**[reset qos policy control-plane**]命令用来清除控制平面应用QoS策略的统计信息。

【命令】

集中式设备：

**[reset qos policy control-plane**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset qos policy control-plane** **slot** *slot-number*  **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[reset qos policy control-plane****chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：清除指定单板的基于控制平面应用QoS策略的统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：清除指定成员设备的基于控制平面应用QoS策略的统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX的基于控制平面应用QoS策略的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-numbe*r]：清除指定成员设备上指定单板的基于控制平面应用QoS策略的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-numbe*r]：清除指定单板的基于控制平面应用QoS策略的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上基于控制平面应用QoS策略的统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除控制平面的QoS策略统计信息。（集中式设备）

\<Sysname\> reset qos policy control-plane

\# 清除应用到3号板控制平面的QoS策略统计信息。（分布式设备－独立运行模式）

\<Sysname\> reset qos policy control-plane slot 3

\# 清除应用到3号成员设备控制平面的QoS策略统计信息。（集中式IRF设备）

\<Sysname\> reset qos policy control-plane slot 3

\# 清除应用到1号成员设备3号板控制平面的QoS策略统计信息。（分布式设备－IRF模式）

\<Sysname\> reset qos policy control-plane chassis 1 slot 3

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos policy control-plane management**

------------------------------------------------------------------------

**[reset qos policy control-plane management**]命令用来清除管理口控制平面QoS策略的统计信息。

【命令】

**[reset qos policy control-plane management**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除管理口控制平面QoS策略的统计信息。

\<Sysname\> reset qos policy control-plane management

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos policy global**

------------------------------------------------------------------------

**[reset qos policy global**]命令用来清除全局应用的QoS策略的统计信息。

【命令】

**[reset qos policy global **[[ **inbound** \| **outbound** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：清除全局接收到的报文应用QoS策略的统计信息。

**[outbound**]：清除全局发送的报文应用QoS策略的统计信息。

【使用指导】

如果不指定方向，则同时清除出入两个方向全局应用的QoS策略的统计信息。

【举例】

\# 清除全局入方向应用的QoS策略的统计信息。

\<Sysname\> reset qos policy global inbound

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos vlan-policy**

------------------------------------------------------------------------

**[reset qos vlan-policy**]命令用来清除VLAN应用的QoS策略的统计信息。

【命令】

**[reset qos vlan-policy **[ **vlan** *vlan-id*  [ **inbound** \| **outbound** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id*]：指定VLAN。*vlan-id*为指定VLAN的ID号，取值范围为1～4094。

**[inbound**]：清除VLAN接收到的报文应用QoS策略的统计信息。

**[outbound**]：清除对VLAN发送的报文应用QoS策略的统计信息。

【使用指导】

如果不指定方向，则同时清除出入两个方向VLAN应用的QoS策略的统计信息。

【举例】

\# 清除VLAN 2应用的QoS策略的统计信息。

\<Sysname\> reset qos vlan-policy vlan 2

**QoS策略 \-- 接口流速统计配置命令 \-- qos flow-interval**

------------------------------------------------------------------------

**[qos flow-interval**]命令用来配置接口流速统计时间。

**[undo qos flow-interval**]命令用来恢复缺省情况。

【命令】

**[qos flow-interval** *interval*]

**[undo qos flow-interval**]

【缺省情况】

接口流速统计时间为5分钟。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：流速统计时间，单位为分钟。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

我们可以统计经过QoS策略流分类后每类报文的发送和丢弃速率。假设流速统计时间为t（t默认为5分钟），则系统将统计最近t时间内每类报文发送和丢弃的平均速率，且每t/5分钟刷新一次统计速率。

子接口的流速统计时间采用主接口的统计时间。

【举例】

\# 配置接口GigabitEthernet1/0/1的流速统计时间为10分钟。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos flow-interval 10

【相关命令】

·**display qos policy interface**

\

**优先级映射 \-- 优先级映射表配置命令 \-- display qos map-table**

------------------------------------------------------------------------

**[display qos map-table**]命令用来显示指定优先级映射表配置情况。

【命令】

**[display qos map-table**[ [ **inbound** \| **outbound**   **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]：接收报文方向。

**[outbound**]：发送报文方向。

表2-1 优先级映射表

优先级映射

描述

dot11e-lp

802.11e优先级到本地优先级映射表

dot1p-dot1p

802.1p优先级到802.1p优先级映射表

dot1p-dp

802.1p优先级到丢弃优先级映射表

dot1p-dscp

802.1p优先级到DSCP映射表

dot1p-exp

802.1p优先级到EXP映射表

dot1p-lp

802.1p优先级到本地优先级映射表

dot1p-rpr

802.1p优先级到RPR优先级映射表

dscp-dot1p

DSCP到802.1p优先级映射表

dscp-dp

DSCP到丢弃优先级映射表

dscp-dscp

DSCP到DSCP映射表

dscp-exp

DSCP到EXP映射表

dscp-lp

DSCP到本地优先级映射表

dscp-rpr

DSCP到RPR优先级映射表

exp-dot1p

EXP到802.1p优先级映射表

exp-dp

EXP到丢弃优先级映射表

exp-dscp

EXP到DSCP映射表

exp-exp

EXP到EXP映射表

exp-lp

EXP到本地优先级映射表

exp-rpr

EXP到RPR优先级映射表

ippre-rpr

IP优先级到RPR优先级映射表

lp-dot11e

本地优先级到802.11e优先级映射表

lp-dot1p

本地优先级到802.1p优先级映射表

lp-dp

本地优先级到丢弃优先级映射表

lp-dscp

本地优先级到DSCP映射表

lp-exp

本地优先级到EXP映射表

lp-lp

本地优先级到本地优先级映射表

up-dot1p

用户优先级到802.1p优先级映射表

up-dp

用户优先级到丢弃优先级映射表

up-dscp

用户优先级到DSCP映射表

up-exp

用户优先级到EXP映射表

up-fc

用户优先级到转发类映射表

up-lp

用户优先级到本地优先级映射表

up-rpr

用户优先级到RPR优先级映射表

up-up

用户优先级到用户优先级映射表

****

![说明](QoS命令.files/image001.png)

各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果未指定表的类型，将显示所有映射表的配置情况。

·如果未指定方向，将显示所有方向的映射表的配置情况。

·如果未指定任何参数，即**display qos map-table**命令将显示所有映射表（以及带颜色映射表）的配置情况。

【举例】

\# 显示802.1p优先级到本地优先级映射表的配置信息。

\<Sysname\> display qos map-table dot1p-lp

MAP-TABLE NAME: dot1p-lp   TYPE: pre-define   DIRECTION: inbound

IMPORT  :  EXPORT

   0    :    2

   1    :    0

   2    :    1

   3    :    3

   4    :    4

   5    :    5

   6    :    6

   7    :    7

MAP-TABLE NAME: dot1p-lp   TYPE: pre-define   DIRECTION: outbound

IMPORT  :  EXPORT

   0    :    2

   1    :    0

   2    :    1

   3    :    3

   4    :    4

   5    :    5

   6    :    6

   7    :    7

MAP-TABLE NAME: dot1p-lp   TYPE: pre-define

IMPORT  :  EXPORT

   0    :    2

   1    :    0

   2    :    1

   3    :    3

   4    :    4

   5    :    5

   6    :    6

   7    :    7

表2-2 display qos map-table命令显示信息描述表

字段

描述

MAP-TABLE NAME

映射表的名字

TYPE

映射表的类型

DIRECTION

映射表的方向

IMPORT

映射表的输入值

EXPORT

映射表的输出值

**优先级映射 \-- 优先级映射表配置命令 \-- display qos map-table color**

------------------------------------------------------------------------

**[display qos map-table color**]命令用来显示指定带颜色优先级映射表配置情况。

【命令】

**[display qos map-table color**[[ **green** \| **yellow** \| **red**   **inbound** \| **outbound** ] ] [ **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**green**：绿色报文。

**[yellow**]：黄色报文。

**[red**]：红色报文。

**[inbound**]：接收报文方向。

**[outbound**]：发送报文方向。

其它参数请参见 表2-1(?-2075031760#_Ref298430323)。

[![说明](QoS命令.files/image001.png)]

各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

经过流量监管处理的报文被分成了三种颜色（绿色、黄色、红色），为了对不同颜色报文进行优先级映射，设备提供了多张带颜色优先级映射表，分别对应相应颜色的优先级映射关系。流量监管对报文处理的相关内容请参见流量监管章节内容。

·如果未指定表的类型，将显示所有带颜色映射表的配置情况。

·如果未指定颜色，将显示所有颜色的带颜色映射表的配置情况。

·如果未指定方向，将显示所有方向带颜色映射表的配置情况。

【举例】

\# 显示绿色报文的接收报文方向的EXP到本地优先级映射表的配置信息。

\<Sysname\> display qos map-table color green inbound exp-lp

MAP-TABLE NAME: exp-lp   TYPE: pre-define   COLOR: green   DIRECTION: inbound

IMPORT  :  EXPORT

   0    :    0

   1    :    1

   2    :    2

   3    :    3

   4    :    4

   5    :    5

   6    :    6

   7    :    7

表2-3 display qos map-table color命令显示信息描述表

字段

描述

MAP-TABLE NAME

映射表的名字

TYPE

映射表的类型

COLOR

映射表的颜色

DIRECTION

映射表的方向

IMPORT

映射表的输入值

EXPORT

映射表的输出值

**优先级映射 \-- 优先级映射表配置命令 \-- import**

------------------------------------------------------------------------

**[import**]命令用来配置指定优先级映射表的映射关系。

**[undo import**]命令用来删除配置的优先级映射表的映射关系，恢复其为缺省的映射关系。

【命令】

**[import***import-value-list* **export** *export-value*]

**[undo import** *[import-value-list*[ \| **all** }]]

【缺省情况】]

优先级映射表的映射关系请参见配置指导中的附录 B。

【视图】

优先级映射表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[import-value-list*]：输入值列表。

*[export-value*]：输出值。

**[all**]：删除配置地该映射表的所有映射关系，恢复其为缺省的映射关系。

【举例】

\# 配置802.1p优先级到丢弃优先级映射表的映射关系，与802.1p优先级4、5相对应的丢弃优先级为1。

\<Sysname\> system-view

Sysname qos map-table dot1p-dp

Sysname-maptbl-dot1p-dp import 4 5 export 1

【相关命令】

·**display qos map-table**

·**display qos map-table color**

**优先级映射 \-- 优先级映射表配置命令 \-- qos map-table**

------------------------------------------------------------------------

**[qos map-table**]命令用来进入指定的优先级映射表视图。

【命令】

**[qos map-table**[ [ **inbound** \| **outbound** ] { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：接收报文方向。

**[outbound**]：发送报文方向。

其它参数请参见 表2-1(?-2075031760#_Ref298430323)。

![说明](QoS命令.files/image001.png)

各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

每个优先级映射存在无方向、接收报文方向、发送报文方向三张不同的映射表。如果不指定方向，则表示进入无方向的优先级映射表视图。对映射表方向的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 进入接收报文方向的802.1p优先级到丢弃优先级映射表视图。

\<Sysname\> system-view

Sysname qos map-table inbound dot1p-dp

Sysname-maptbl-in-dot1p-dp

\# 进入发送报文方向的802.1p优先级到丢弃优先级映射表视图。

\<Sysname\> system-view

Sysname qos map-table outbound dot1p-dp

Sysname-maptbl-out-dot1p-dp

【相关命令】

·**display qos map-table**

·**import**

**优先级映射 \-- 优先级映射表配置命令 \-- qos map-table color**

------------------------------------------------------------------------

**[qos map-table color**]命令用来进入指定的带颜色优先级映射表视图。

【命令】

**[qos map-table**[ **color** { **green** \| **yellow** \| **red** } [ **inbound** \| **outbound** ] { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：绿色报文。

**[yellow**]：黄色报文。

**[red**]：红色报文。

**[inbound**]：接收报文方向。

**[outbound**]：发送报文方向。

其它参数请参见 表2-1(?-2075031760#_Ref298430323)。

![说明](QoS命令.files/image001.png)

各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

经过流量监管处理的报文被分成了三种颜色（绿色、黄色、红色），为了对不同颜色报文进行优先级映射，设备提供了多张带颜色优先级映射表，分别对应相应颜色的优先级映射关系。流量监管对报文处理的相关内容请参见流量监管章节内容。

每个优先级映射（颜色也相同）存在无方向、接收报文方向、发送报文方向三张不同的映射表。如果不指定方向，则表示进入无方向的优先级映射表视图。对映射表方向的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 进入绿色报文的EXP到本地优先级映射表视图。

\<Sysname\> system-view

Sysname qos map-table color green exp-lp

Sysname-maptbl-green-exp-lp

\# 进入红色报文的接收报文方向的DSCP到本地优先级映射表视图。

\<Sysname\> system-view

Sysname qos map-table color red inbound dscp-lp

Sysname-maptbl-red-in-dscp-lp

【相关命令】

·**display qos map-table color**

·**import**

**优先级映射 \-- 端口优先级配置命令 \-- qos priority**

------------------------------------------------------------------------

**[qos priority**]命令用来配置当前端口的端口优先级。

**[undo qos priority**]命令用来恢复端口优先级为缺省值。

【命令】

支持多种类型端口优先级的设备：

**[qos priority **[[\| **dp** \| **dscp** \| **exp** \| **lp** } *priority-value*]]

**[undo**[ **qos** **priority** { **dot1p** \| **dp** \| **dscp** \| **exp** \| **lp** }]]

支持一种类型端口优先级的设备：]

**[qos priority ***priority-value*]

**[undo qos priority**]

上面两种情况都支持的设备：

**[qos priority **[ **dot1p** [\| **dp** \| **dscp** \| **exp** \| **lp** ] *priority-value*]]

**[undo**[ **qos** **priority** [ **dot1p** \| **dp** \| **dscp** \| **exp** \| **lp** ]]]

【缺省情况】

支持一种类型端口优先级的设备，端口优先级的缺省值为0；支持多种类型端口优先级的设备，**lp**类型优先级的缺省值为2，**dp**类型优先级的缺省值为0，其余类型优先级没有缺省值。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-value*]：端口优先级值。当设备只支持一种类型的端口优先级时，取值范围为0～7；当设备支持多种类型的端口优先级时，各优先级的取值范围如[表]2-4(?-825556734#_Ref189542338)所示。

表2-4 各种端口优先级取值范围

端口优先级类型

*[priority-value*]取值范围

说明

**[dot1p**]（802.1p优先级）

0～7

-

**[dscp**]（DSCP优先级）

0～63

-

**[exp**]（EXP优先级）

0～7

-

**[dp**]（丢弃优先级）

0～2

丢弃优先级值越大的报文越被优先丢弃

**[lp**]（本地优先级）

0～7

本地优先级值越大的报文，进入的队列优先级越高，从而能够获得优先的调度

![说明](QoS命令.files/image001.png)

各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

对于支持多种类型端口优先级的设备，不同类型的端口优先级可以同时在同一个接口上配置，同一种类型的端口优先级配置采用覆盖方式。

需要注意的是，对于上面两种情况都支持的设备，可能会出现某种类型不支持，此时配置失败，具体请以设备的实际情况为准。

【举例】

\# 配置接口GigabitEthernet1/0/1的端口优先级为2（支持一种类型端口优先级的设备）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos priority 2

\# 配置接口GigabitEthernet1/0/1的DSCP优先级为20（支持多种类型端口优先级的设备）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos priority dscp 20

【相关命令】

·**display qos trust interface**

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark { tcp-port \| udp-port }**

------------------------------------------------------------------------

**[display qos remark **[{ **tcp-port** \| **udp-port** }]]命令用来显示所有TCP或UDP端口的报文优先级配置情况。

【命令】

**[display qos remark **[{ **tcp-port** \| **udp-port** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示TCP端口的优先级配置情况。

\<Sysname\> display qos remark tcp-port

TCP port based priorities：

 IP type   Port     DSCP   dot1p

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPv4      30       -      4

 IPv6      31-40    cs7    -

 IPAll     50       cs6    -

\# 显示UDP端口的优先级配置情况。

\<Sysname\> display qos remark udp-port

UDP port based priorities：

 IP type   Port    DSCP   dot1p

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPv4      30      -      4

 IPv6      31-40   cs7    -

 IPAll     50      cs6    -

表2-5  display qos remark { tcp-port \| udp-port }命令显示信息描述表

字段

描述

IP type

IP类型，取值情况如下：

·IPv4：表示IPv4类型的报文

·IPv6：表示IPv6类型的报文

·IPAll：表示所有的IP报文

Port

端口号

DSCP

DSCP优先级值

dot1p

dot1p优先级值

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark ip-address**

------------------------------------------------------------------------

**[display qos remark ip-address**]命令用来显示所有IP地址的报文优先级配置情况。

【命令】

**[display qos remark ip-address**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IP地址优先级的配置情况。

\<Sysname\> display qos remark ip-address

IP address based priorities:

 IP address                                       DSCP      dot1p

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 10.13.3.50/24                                    -         4

 123.17.3.50/16                                   -         4

 10::121/120                                      cs7       -

表2-6 display qos remark ip-address命令显示信息描述表

字段

描述

IP address

IP地址

DSCP

DSCP优先级值

dot1p

dot1p优先级值

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark protocol**

------------------------------------------------------------------------

**[display qos remark protocol**]命令用来显示所有协议报文优先级的配置情况。

【命令】

**[display qos remark protocol**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示协议优先级配置情况。

\<Sysname\> display qos remark protocol

Protocol priorities：

 Protocol      dot1p

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IP            -

 IPX           2

 ARP           5

 AppleTalk     -

 SNA           -

 NetBEUI       -

表2-7 display qos remark protocol命令显示信息描述表

字段

描述

Protocol

协议类型，取值包括：IP、IPX、ARP、AppleTalk、SNA和NetBEUI

dot1p

dot1p优先级值

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark vlan**

------------------------------------------------------------------------

**[display qos remark vlan**]命令用来显示所有VLAN的报文优先级配置情况。

【命令】

**[display qos remark vlan**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示VLAN的优先级配置情况。

\<Sysname\> display qos remark vlan

VLAN based priorities:

 VLAN        DSCP      dot1p

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 4           -         4

 5           cs6       -

 6           -         5

表2-7 display qos remark vlan命令显示信息描述表

字段

描述

VLAN

VLAN ID

DSCP

DSCP优先级值

dot1p

dot1p优先级值

**优先级映射 \-- 全局优先级配置命令 \-- display qos type-of-service**

------------------------------------------------------------------------

**[display qos type-of-service**]命令用来显示服务类型的配置情况。

【命令】

**[display qos type-of-service**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示服务类型的配置情况。

\<Sysname\> system-view

Sysname qos type-of-service dscp

Sysname display qos type-of-service

 Type of service: dscp

表2-8 display qos type-of-service 命令显示信息描述表

字段

描述

Type of service

服务类型，取值为**ip-precedence**或**dscp**

disabled

非使能

ip-precedence

IP优先级

dscp

DSCP优先级

**优先级映射 \-- 全局优先级配置命令 \-- qos remark { tcp-port \| udp-port }**

------------------------------------------------------------------------

**[qos remark **[{ **tcp-port** \| **udp-port** }]]命令重标记指定TCP或UDP端口号的报文优先级。

**[undo**[ **qos remark** { **tcp-port** \| **udp-port** }]]命令用来取消指定TCP或UDP端口的报文的优先级配置。

【命令】

**[qos remark **[{ **tcp-port** \| **udp-port** } [ **ipv4** \| **ipv6** ] *start-value*  **to** *end-value*  { **dot1p** *dot1p-value* \| **dscp** *dscp-value* }]]

**[undo qos remark **[{ **tcp-port** \| **udp-port** } [ **ipv4** \| **ipv6** ] *start-value*  **to** *end-value*  { **dot1p** \| **dscp** }]]

【缺省情况】

没有为指定TCP或UDP端口号的报文优先级进行重标记。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：指定匹配IP类型为IPv4的报文。

**[ipv6**]：指定匹配IP类型为IPv6的报文。如果未指定**ipv4**和**ipv6**，则表示匹配所有的IP报文。

*[start-value* [ **to** *end-value* ]]：指定一个TCP或UDP端口号范围。*start-value*表示起始端口号，取值范围为0～65535，*end-value*表示结束端口号，取值范围为0～65535，*end-value*的值要大于或等于*start-value*的值。

**[dot1p ***dot1p-value*]：802.1p优先级，取值范围为0～7。

**[dscp ***dscp-value*]：DSCP值，取值范围为0～63，也可以是关键字，如[表]1-5(?-580725274#_Ref163816081)所示。

【使用指导】

若报文同时匹配上目的端口规则和源端口规则，则匹配目的端口规则的配置生效。

【举例】

\# 重标记TCP端口号属于20～25的所有IPv6报文的802.1p优先级为4。

\<Sysname\> system-view

Sysname qos remark tcp-port ipv6 20 to 25 dot1p 4

\# 重标记UCP端口号为69的IPv4报文的802.1p优先级为4。

\<Sysname\> system-view

Sysname qos remark udp-port ipv4 69 dot1p 4

**优先级映射 \-- 全局优先级配置命令 \-- qos remark ip-address**

------------------------------------------------------------------------

**[qos remark ip-address**]命令用来重标记指定IP地址的报文优先级。

**[undo** **qos remark ip-address**]命令用来取消指定IP地址报文的优先级配置。

【命令】

**[qos remark ip-address **[{ *ipv4-address* [ *mask-length \| mask* ] \| *ipv6-address*  *prefix-length*  } { **dot1p** *dot1p-value* \| **dscp** *dscp-value* }]]

**[undo qos remark ip-address **[{ *ipv4-address* [ *mask-length \| mask* ] \| *ipv6-address*  *prefix-length*  }{ **dot1p** \| **dscp** }]]

【缺省情况】

没有为指定IP地址的报文优先级进行重标记。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：指定的IPv4地址，为点分十进制格式。

*[mask-length*]：IPv4地址的掩码长度，取值范围为1～32。

*[mask*]：IPv4地址的掩码，为点分十进制格式。

*[ipv6-address*]：指定的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为1～128。

**[dot1p ***dot1p-value*]：802.1p优先级，取值范围为0～7。

**[dscp ***dscp-value*]：DSCP值，取值范围为0～63，也可以是关键字，如表(http://press/data/infoblade/Comware%20V7平台中文/1.2.11%20ACL和QoS/1.2.11.02%20QoS/QoS命令.htm#_Ref163816081)1-5(http://press/data/infoblade/Comware%20V7平台中文/1.2.11%20ACL和QoS/1.2.11.02%20QoS/QoS命令.htm#_Ref163816081)所示。

【使用指导】

若同时匹配上源IP地址和目的IP地址时，则匹配目的IP地址的配置生效。

【举例】

\# 重标记IP地址为10.15.10.1/24的报文的802.1p优先级为4。

\<Sysname\> system-view

Sysname qos remark ip-address 10.15.10.1 24 dot1p 4

**优先级映射 \-- 全局优先级配置命令 \-- qos remark protocol**

------------------------------------------------------------------------

**[qos remark protocol**]命令用来重标记指定协议报文的优先级。

**[undo** **qos remark protocol**]命令用来取消指定协议报文的优先级配置。

【命令】

**[qos remark protocol ***protocol-name ***dot1p ***dot1p-value*]

**[undo qos remark protocol ***protocol-name ***dot1p**]

【缺省情况】

没有为指定协议报文的优先级进行重标记。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[protocol ***protocol-name*]：指定协议类型为IP、IPX、ARP、AppleTalk、SNA或NetBEUI。

**[dot1p ***dot1p-value*]**：**802.1p优先级，取值范围为0～7。

【举例】

\# 重标记ARP协议报文的802.1p优先级为4。

\<Sysname\> system-view

Sysname qos remark protocol arp dot1p 4

**优先级映射 \-- 全局优先级配置命令 \-- qos remark vlan**

------------------------------------------------------------------------

**[qos remark vlan**]命令用来重标记指定的VLAN或VLAN范围的报文的优先级。

**[undo** **qos remark vlan**]命令用来取消指定的VLAN或VLAN范围报文的优先级配置。

【命令】

**[qos remark vlan ***start-vlan-id *[ **to** *end-vlan-id*  { **dot1p** *dot1p-value* \| **dscp** *dscp-value* }]]

**[undo qos remark vlan ***start-vlan-id *[ **to** *end-vlan-id*  { **dot1p** \| **dscp** }]]

【缺省情况】

没有为VLAN内的报文的优先级进行重标记。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[start-vlan-id*]：VLAN的编号，取值范围为1～4094。

*[start-vlan-id*]**to***end-vlan-id*：指定VLAN的编号范围。*start-vlan-id*和*end-vlan-id*为VLAN的编号，取值范围为1～4094。*end-vlan-id*的值要大于或等于*start-vlan-id*的值。

**[dot1p ***dot1p-value*]：802.1p优先级，取值范围为0～7。

**[dscp ***dscp-value*]：DSCP值，取值范围为0～63，也可以是关键字，如[表]1-5(?-580725274#_Ref163816081)所示。

【举例】

\# 重标记VLAN 2内的报文的802.1p优先级为4。

\<Sysname\> system-view

Sysname qos remark vlan 2 dot1p 4

**优先级映射 \-- 全局优先级配置命令 \-- qos type-of-service**

------------------------------------------------------------------------

**[qos type-of-service**]命令用来配置设备的服务类型。

**[undo** **qos** **type-of-service**]命令用来取消服务类型的配置。

【命令】

**[qos type-of-service**[ { **ip-precedence** \| **dscp** }]]

**[undo qos type-of-service**]

【缺省情况】

没有配置设备的服务类型。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-precedence**]：全局信任IP优先级，以此优先级进行优先级映射。

**[dscp**]：全局信任DSCP优先级，以此优先级进行优先级映射。

【举例】

\# 配置服务类型为DSCP。

\<Sysname\> system-view

Sysname qos type-of-service dscp

**优先级映射 \-- 端口优先级信任模式配置命令 \-- display qos trust interface**

------------------------------------------------------------------------

**[display qos trust interface**]命令用来显示当前配置的端口优先级信任模式信息和端口优先级的信息。

【命令】

**[display qos trust** **interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的端口优先级信任模式信息。

【举例】

\# 显示当前配置的端口优先级信任模式信息（支持一种类型端口优先级的设备）。

\<Sysname\> display qos trust interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

 Port priority trust information

  Port priority:4

  Port priority trust type: exp,  Override: disable

表2-9 display qos trust interface命令显示信息描述表（支持一种类型端口优先级的设备）

字段

描述

Interface

接口名，由接口类型和接口编号构成

Port priority trust information

端口优先级信任信息

Port priority

端口优先级

Port priority trust type

端口优先级信任类型，取值为：

·auto：根据报文的类型，自动提取报文中的优先级字段

·dot11e：dot11e优先级

·dot1p：802.1p优先级

·dscp：DSCP优先级

·exp：EXP优先级

·none：不信任任何优先级

Override

是否覆盖报文本身的优先级

\# 显示当前配置的端口优先级信任模式信息（支持多种类型端口优先级的设备）。

\<Sysname\> display qos trust interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

 Port priority trust information

  Port dot1p priority: 4

  Port dscp priority: 32

  Port dp priority: 1

  Port exp priority: 7

  Port lp priority: 5

  Port priority trust type: exp,  Override: disable

表2-10 display qos trust interface命令显示信息描述表（支持多种类型端口优先级的设备）

字段

描述

Interface

接口名，由接口类型和接口编号构成

Port priority trust information

端口优先级信任信息

Port dot1p priority

端口802.1p优先级

Port dscp priority

端口DSCP优先级

Port dp priority

端口丢弃优先级

Port exp priority

端口EXP优先级

Port lp priority

端口本地优先级

Port priority trust type

端口优先级信任类型，取值为：

·auto：根据报文的类型，自动提取报文中的优先级字段

·dot11e：dot11e优先级

·dot1p：802.1p优先级

·dscp：DSCP优先级

·exp：EXP优先级

·none：不信任任何优先级

Override

是否覆盖报文本身的优先级

**优先级映射 \-- 端口优先级信任模式配置命令 \-- qos trust**

------------------------------------------------------------------------

**[qos trust**]命令用来配置端口优先级信任模式。

**[undo qos trust**]命令用来恢复缺省情况。

【命令】

**[qos trust**[ { **auto** \| **dot11e** \| **dot1p** \| **dscp** \| **exp** \| **none** } [ **override** ]]]

**[undo qos trust**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示根据报文的类型，自动提取报文中的优先级字段进行优先级映射。对于二层报文，采用802.1p优先级；对于三层报文，采用DSCP优先级；对于MPLS报文，采用EXP。

**[dot11e**]：信任802.11报文携带的dot11e优先级，以此优先级进行优先级映射。该参数只能在WLAN-ESS接口上进行配置。

**[dot1p**]：信任报文自带的802.1p优先级，以此优先级进行优先级映射。

**[dscp**]：信任IP报文自带的DSCP，以此优先级进行优先级映射。

**[exp**]：信任MPLS报文自带的EXP，以此优先级进行优先级映射。

**[none**]：不信任任何优先级。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[override**]：表示通过优先级映射表取得的优先级将覆盖报文本身的优先级，缺省为不覆盖。

![说明](QoS命令.files/image001.png)

各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在接口GigabitEthernet1/0/1上配置优先级信任模式为信任报文自带的802.1p优先级。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos trust dot1p

【相关命令】

·**display qos trust interface**

\

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- display qos car interface**

------------------------------------------------------------------------

**[display qos car interface**]命令用来显示接口的流量监管配置情况和统计信息。

【命令】

**[display qos car interface ** *interface-type interface-number* ]

【视图】

任意视图

【缺省级别】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的流量监管配置情况和统计信息。

【举例】

\# 显示接口GigabitEthernet1/0/1的流量监管配置情况和统计信息。

\<Sysname\> display qos car interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

 Direction: inbound

  Rule: If-match any

   CIR 128 (kbps), CBS 8000 (Bytes), PIR 128 (kbps), EBS 512 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

\# 显示接口GigabitEthernet1/0/2的流量监管配置情况和统计信息。

\<Sysname\> display qos car interface gigabitethernet 1/0/2

Interface: GigabitEthernet1/0/2

 Direction: inbound

  Rule: If-match any

   CIR 50 (%), CBS 600 (ms), EBS 0 (ms)，PIR 50 (%)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

表3-1 display qos car interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号结合在一起组成

Direction

指定流量监管的方向

Rule

数据包的匹配规则

CIR

承诺信息速率，当采用绝对值形式输入时，单位为kbps；当采用百分比形式时，单位为%

CBS

承诺突发尺寸，当采用绝对值形式输入时，单位为byte；当采用百分比形式时，单位为ms，实际的CBS值是*cbs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）

EBS

超出突发尺寸，当采用绝对值形式输入时，单位为byte；当采用百分比形式时，单位为ms，实际的EBS值是*ebs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）

PIR

峰值信息速率，当采用绝对值形式输入时，单位为kbps；当采用百分比形式时，单位为%

Green action

对绿色报文的动作

Yellow action

对黄色报文的动作

Red action

对红色报文的动作

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- display qos carl**

------------------------------------------------------------------------

**[display qos carl**]命令用来显示CAR列表。

【命令】

集中式设备：

**[display qos carl** [ *carl-index* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos carl** [ *carl-index*   **slot**]*slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display qos carl** [ *carl-index*  ]**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[carl-index*]：CAR列表的号码，取值范围为1～199。如果未指定本参数，将显示所有的CAR列表。

**[slot**]* slot-number*：显示指定单板的CAR列表信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的CAR列表的配置信息。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的CAR列表信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备的CAR列表的配置信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的CAR列表信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的CAR列表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的CAR列表信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显全局主用主控板上的CAR列表的配置信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的CAR列表信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的CAR列表信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上CAR列表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有的CAR列表。

\<Sysname\> display qos carl 1

List  Rules

1     destination-ip-address range 1.1.1.1 to 1.1.1.2 per-address shared-bandwidth

2     destination-ip-address subnet 1.1.1.1 22 per-address shared-bandwidth

4     dscp 1 2 3 4 5 6 7 cs1

5     mac 0000-0000-0000

6     mpls-exp 0 1 2

9     precedence 0 1 2 3 4 5 6 7

10    source-ip-address range 1.1.1.1 to 1.1.1.2

11    source-ip-address subnet 1.1.1.1 31

表1-2 display qos carl命令显示信息描述表

字段

描述

List

CAR列表号码

Rules

数据包的匹配规则

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos car (interface view)**

------------------------------------------------------------------------

**[qos** **car**]命令用来在接口上配置流量监管。

**[undo qos car**]命令用来取消接口上流量监管的配置。

【命令】

**[qos car **[{ **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-numbe*r \| **carl** *carl-index* } **cir** *committed-information-rate*  **cbs** *committed-burst-size* [ **ebs** *excess-burst-size*    **green** *action* \| **red** *action* \| **yellow** *action* ] \*]]

**[qos car **[{ **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-numbe*r \| **carl** *carl-index* } **cir** *committed-information-rate*  **cbs** *committed-burst-size*  **pir** *peak-information-rate*  **ebs** *excess-burst-size*  [ **green** *action* \| **red** *action* \| **yellow** *action* ] \*]]

**[undo qos car**[ { **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-number* \| **carl** *carl-index* }]]

【缺省情况】

接口上没有配置流量监管。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对接口接收到的数据包进行流量监管。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：对接口发送的数据包进行流量监管。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[any**]：对所有的IP数据包进行流量监管。

**[acl ** **ipv6** ] *acl-number*：对匹配ACL的数据包进行流量监管。*acl-number*为ACL编号，取值范围与设备的型号有关，请以设备的实际情况为准。若未指定**ipv6**关键字，表示IPv4 ACL；否则表示IPv6 ACL。

**[carl ***carl-index*]：对匹配CAR列表的数据包进行限速。*carl-index*为承诺访问速率列表编号，取值范围为1～199。

**[cir ***committed-information-rate*]：承诺信息速率，单位为kbps。

**[cbs** *committed-burst-size*]：承诺突发尺寸，即实际平均速率在承诺速率以内时的突发流量，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *excess-burst-size*]：过度突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率，单位为kbps。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[green ***action*]：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为**pass**。

**[red ***action*]：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为**discard**。

**[yellow ***action*]：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为**pass**。

*[action*]：对数据包采取的动作，有以下几种：

·**continue**：继续由下一个CAR策略处理。

·**discard**：丢弃数据包。

·**pass**：允许数据包通过。

·**remark-atmclp-continue** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并继续由下一个CAR策略处理，取值范围为0～1。

·**remark-atmclp-pass** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-dot1p-continue** *new-cos*：设置新的802.1P报文的优先级值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-dot1p-pass** *new-cos*：设置新的802.1P报文的优先级值，并允许数据包通过，取值范围为0～7。

·**remark-dscp-continue** *new-dscp*：设置报文新的DSCP值，并继续由下一个CAR策略处理，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。

·**remark-dscp-pass** *new-dscp*：设置报文新的DSCP值，并允许数据包通过，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。

·**remark-frde-continue** *new-frde*：设置新的FR报文的DE标志位的值，并继续由下一个CAR策略处理，取值范围为0～1。

·**remark-frde-pass** *new-frde*：设置新的FR报文的DE标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-lp-continue** *new-lp*：设置新的报文的lp标志位的值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-lp-pass** *new-lp*：设置新的报文的lp标志位的值，并允许数据包通过，取值范围为0～7。

·**remark-mpls-exp-continue** *new-exp*：设置新的MPLS报文的EXP标志位的值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-mpls-exp-pass** *new-exp*：设置新的MPLS报文的EXP标志位的值，并允许数据包通过，取值范围为0～7。

·**remark-prec-continue** *new-precedence*：设置新的IP优先级，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-prec-pass** *new-precedence*：设置新的IP优先级，并允许数据包通过，取值范围为0～7。

【使用指导】

·该命令的重复执行将在接口上配置多个CAR策略，策略的执行顺序与配置的先后顺序一致。

·CAR支持的动作与设备相关，请以设备的实际情况为准。

·不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。

【举例】

\# 在接口GigabitEthernet1/0/1的出方向上对满足ANY规则的报文进行流量监管。报文正常流速为200kbps，在第一时间可以有大于正常流量的突发流量通过，以后速率小于等于200kbps时正常发送，大于200kbps时，报文优先级改为0并发送。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos car outbound any cir 200 cbs 5000 ebs 0 green pass red remark-prec-pass 0

【相关命令】

·**display qos car**** interface**

·**qos ****carl**

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos car percent (interface view)**

------------------------------------------------------------------------

**[qos** **car percent**]命令用来采用百分比的方式在接口上配置流量监管。

**[undo qos car**]命令用来取消接口上流量监管的配置。

【命令】

**[qos car **[{ **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-numbe*r \| **carl** *carl-index* } **percent** **cir** *cir-percent*  **cbs** *cbs-time* [ **ebs** *ebs-time*    **green** *action* \| **red** *action* \| **yellow** *action* ] \*]]

**[qos car **[{ **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-numbe*r \| **carl** *carl-index* } **percent** **cir** *cir-percent*  **cbs** *cbs-time*  **pir** *pir-percent*  **ebs** *ebs-time*  [ **green** *action* \| **red** *action* \| **yellow** *action* ] \*]]

**[undo qos car**[ { **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-number* \| **carl** *carl-index* }]]

【缺省情况】

接口上没有配置百分比形式的流量监管。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对接口接收到的数据包进行流量监管。参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：对接口发送的数据包进行流量监管。参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[any**]：对所有的IP数据包进行流量监管。

**[acl ** **ipv6** ] *acl-number*：对匹配ACL的数据包进行流量监管。*acl-number*为ACL编号，取值范围与设备的型号有关，请以设备的实际情况为准。若未指定**ipv6**关键字，表示IPv4 ACL；否则表示IPv6 ACL。

**[carl ***carl-index*]：对匹配CAR列表的数据包进行限速。*carl-index*为承诺访问速率列表编号，取值范围为1～199。

**[percent** **cir** *cir-percent*]：以百分比的形式来指定承诺信息速率。取值范围为1\~100。

**[cbs** *cbs-time*]：用指定的时间（单位为ms）来设置CBS，实际的CBS值是*cbs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *ebs-time*]：用指定的时间（单位为ms）来设置EBS，实际的EBS值是*ebs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir ***pir-percent*]：以百分比的形式来指定峰值速率，取值范围为1\~100。峰值速率不能比承诺信息速率小。该参数的支持情况与设备的型号有关。

**[green ***action*]：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为**pass**。

**[red ***action*]：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为**discard**。

**[yellow ***action*]：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为**pass**。

*[action*]：对数据包采取的动作，有以下几种：

·**continue**：继续由下一个CAR策略处理。

·**discard**：丢弃数据包。

·**pass**：允许数据包通过。

·**remark-atmclp-continue** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并继续由下一个CAR策略处理，取值范围为0～1。

·**remark-atmclp-pass** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-dot1p-continue** *new-cos*：设置新的802.1P报文的优先级值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-dot1p-pass** *new-cos*：设置新的802.1P报文的优先级值，并允许数据包通过，取值范围为0～7。

·**remark-dscp-continue** *new-dscp*：设置报文新的DSCP值，并继续由下一个CAR策略处理，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。

·**remark-dscp-pass** *new-dscp*：设置报文新的DSCP值，并允许数据包通过，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。

·**remark-frde-continue** *new-frde*：设置新的FR报文的DE标志位的值，并继续由下一个CAR策略处理，取值范围为0～1。

·**remark-frde-pass** *new-frde*：设置新的FR报文的DE标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-lp-continue** *new-lp*：设置新的报文的lp标志位的值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-lp-pass** *new-lp*：设置新的报文的lp标志位的值，并允许数据包通过，取值范围为0～7。

·**remark-mpls-exp-continue** *new-exp*：设置新的MPLS报文的EXP标志位的值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-mpls-exp-pass** *new-exp*：设置新的MPLS报文的EXP标志位的值，并允许数据包通过，取值范围为0～7。

·**remark-prec-continue** *new-precedence*：设置新的IP优先级，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-prec-pass** *new-precedence*：设置新的IP优先级，并允许数据包通过，取值范围为0～7。

【使用指导】

·该命令的重复执行将在接口上配置多个CAR策略，策略的执行顺序与配置的先后顺序一致。

·CAR支持的动作与设备相关，请以设备的实际情况为准。

·不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。

【举例】

\# 在接口GigabitEthernet1/0/1的出方向上对满足ANY规则的报文进行流量监管。指定CIR 50%，CBS 1000 ms。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos car outbound any percent cir 50 cbs 1000

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos car (user-profile view,session-group-profile view)**

------------------------------------------------------------------------

**[qos** **car**]命令用来在User Profile或Session Group Profile下配置流量监管。

**[undo qos car**]命令用来取消流量监管的配置。

【命令】

**[qos car **[{ **inbound** \| **outbound** } **any** **cir** *committed-information-rate* [ **cbs** *committed-burst-size* [ **ebs** *excess-burst-size* ] ]]]

**[qos car **[{ **inbound** \| **outbound** } **any** **cir** *committed-information-rate* [ **cbs** *committed-burst-size* ] **pir** *peak-information-rate*  **ebs** *excess-burst-size* ]]

**[undo qos car**[ { **inbound** \| **outbound** }]]

【缺省情况】

没有配置流量监管。

【视图】

User Profile视图/Session Group Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对上线用户发送的报文进行限速。

**[outbound**]：对上线用户接收到的报文进行限速。

**[any**]：对所有的IP数据包进行限速。

**[cir ***committed-information-rate*]：承诺信息速率，单位为kbps。

**[cbs** *committed-burst-size*]：承诺突发尺寸，即实际平均速率在承诺速率以内时的突发流量，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *excess-burst-size*]：过度突发尺寸，单位为byte，缺省值为0 byte。取值范围与设备的型号有关，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率，单位为kbps。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

数据流量符合承诺速率时，允许数据包通过；数据流量不符合承诺速率时，丢弃数据包。

如果多次重复使用该命令，则最后一次配置生效。

Session Group Profile视图应用CAR策略时，只支持**outbound**方向。

不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。

【举例】

\# 对上线用户user接收的报文进行流量监管。报文正常流速为200kbps，允许50000byte的突发流量通过，速率小于等于200kbps时正常发送，大于200kbps时，报文被丢弃。

\<Sysname\> system-view

Sysname user-profile user

Sysname-user-profile-user qos car outbound any cir 200 cbs 50000

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos carl**

------------------------------------------------------------------------

**[qos carl**]命令用来创建或修改CAR列表。

**[undo qos carl**]命令用来删除CAR列表。

【命令】

**[qos carl**[ *carl-index* { **dscp** *dscp-list* \| **mac** *mac-address* \| **mpls-exp** *mpls-exp-value* \| **precedence** *precedence-value* \| { **destination-ip-address** \| **source-ip-address** } { **range** *start-ip-address* **to** *end-ip-address* \| **subnet** *ip-address* *mask-length* } [ **per-address** [ **shared-bandwidth** ] ] }]]

**[undo qos carl** *carl-index*]

【缺省情况】

没有配置CAR列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[carl-index*]：CAR列表号码，取值范围为1～199。

**[dscp*** dscp-list*]：DSCP取值列表。DSCP为区分服务编码点，用数字表示时，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。可以配置多个DSCP值，最多可指定8个；如果指定了多个相同的DSCP值，系统默认为一个；多个不同的DSCP值是或的关系，即只要有一个值匹配，就算匹配这条规则。

**[mac*** mac-address*]：16进制的MAC地址。

**[mpls-exp** *mpls-exp-value*]：MPLS EXP优先级，取值范围为0～7。可以配置多个MPLS EXP值，最多可指定8个；如果指定了多个相同的MPLS EXP值，系统默认为一个；多个不同的MPLS EXP值是或的关系，即只要有一个值匹配，就算匹配这条规则。

**[precedence*** precedence-value*]：优先级，取值范围为0～7。可以配置多个**precedence**值，最多可指定8个；如果指定了多个相同的**precedence**值，系统默认为一个；多个不同的**precedence**值是或的关系，即只要有一个值匹配，就算匹配这条规则。

**[destination-ip-address**]：基于目的IP地址的CAR列表。

**[source-ip-address**]：基于源IP地址的CAR列表。

**[range*** start-ip-address ***to*** end-ip-address*]：IP地址段起始地址和IP地址段终止地址。*end-ip-address*必须大于*start-ip-addres*。**range**指定的IP地址数量上限与设备的型号有关，请以设备的实际情况为准。

**[subnet*** ip-address mask-length*]：IP子网地址和IP子网地址掩码长度。取值范围与设备的型号有关，请以设备的实际情况为准。

**[per-address**]：表示对网段内逐IP地址流量进行限速，cir为各IP地址独享的限制带宽，不能被网段内其他IP流量共享。如果未指定本参数，将对整个网段的流量进行限速，cir为该网段内所有IP地址带宽之和，各个IP地址带宽按照流量大小的比例进行分配。

**[shared-bandwidth**]：表示网段内各IP地址的流量共享剩余带宽，cir为该网段内所有IP地址共享带宽之和，根据当前存在流量的IP地址数量，动态平均分配各IP地址占用的带宽。

【使用指导】

可以选择基于优先级、基于MAC地址、基于MPLS EXP优先级、基于DSCP或基于IP网段建立CAR列表。

对于不同的*carl-index*，该命令的重复执行将创建多个CAR列表，对于同一个*carl-index*，该命令的重复执行将修改CAR列表的参数。

指定单个IP地址限速请使用接口视图下**qos car acl**命令配置。

【举例】

\# 在接口GigabitEthernet1/0/1的出方向上应用CAR列表1。CAR列表1是对源地址属于子网1.1.1.0/24内每台主机限速100kbps，网段内各IP地址的流量不共享剩余带宽。

\<Sysname\> system-view

Sysname qos carl 1 source-ip-address subnet 1.1.1.0 24 per-address

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos car outbound carl 1 cir 100 cbs 6250 ebs 0 green pass red discard

\# 在接口GigabitEthernet1/0/1的出方向上应用CAR列表2。CAR列表2是对源地址属于IP地址段1.1.2.100～1.1.2.199内所有主机限速5Mbps，网段内各IP地址的流量共享剩余带宽。

\<Sysname\> system-view

Sysname qos carl 2 source-ip-address range 1.1.2.100 to 1.1.2.199 per-address shared-bandwidth

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos car outbound carl 2 cir 5000 cbs 3125 ebs 31250 green pass red discard

【相关命令】

·**display qos carl**

·**qos ****car**

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- display qos gts interface**

------------------------------------------------------------------------

**[display qos gts interface**]命令用来显示接口的流量整形配置情况和统计信息。

【命令】

**[display qos gts interface ** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的流量整形配置情况和统计信息。

【举例】

\# 显示所有接口的流量整形配置情况和统计信息。

\<Sysname\> display qos gts interface

Interface: GigabitEthernet1/0/1

 Rule: If-match acl 2001

  CIR 200 (kbps), CBS 50000 (Bytes), PIR 55000 (kbps), EBS 0 (Bytes)

  Queue Length: 100 (Packets)

  Queue Size: 70 (Packets)

  Passed   : 0 (Packets) 0 (Bytes)

  Discarded: 0 (Packets) 0 (Bytes)

  Delayed  : 0 (Packets) 0 (Bytes)

Interface: GigabitEthernet1/0/2

 Rule: If-match acl 2001

  CIR 50 (%), CBS 600 (ms), EBS 0 (ms)

  Queue Length: 100 (Packets)

  Queue Size: 70 (Packets)

  Passed   : 0 (Packets) 0 (Bytes)

  Discarded: 0 (Packets) 0 (Bytes)

  Delayed  : 0 (Packets) 0 (Bytes)

表3-2 display qos gts命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号结合在一起组成

Rule

匹配规则

CIR

承诺信息速率，当采用绝对值形式输入时，单位为kbps；当采用百分比形式时，单位为%

CBS

承诺突发尺寸，当采用绝对值形式输入时，单位为byte；当采用百分比形式时，单位为ms，实际的CBS值是*cbs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）

EBS

超出突发尺寸，当采用绝对值形式输入时，单位为byte；当采用百分比形式时，单位为ms，实际的EBS值是*ebs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）

PIR

峰值速率，当采用绝对值形式输入时，单位为kbps；当采用百分比形式时，单位为%

Queue Length

缓冲队列能够容纳的数据包的个数

Queue Size

当前缓冲区中数据包的数目

Passed

已经通过的数据包数目和字节数

Discarded

被丢弃的数据包数目和字节数

Delayed

被延迟发送的数据包数目和字节数

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- qos gts (interface view)**

------------------------------------------------------------------------

**[qos gts**]命令用来在接口上配置流量整形。

**[undo qos gts**]命令用来取消接口上流量整形的配置。

【命令】

**[qos gts **[{ **any** \| **acl** [ **ipv6** ] *acl-number* \| **queue** *queue-id* } **cir** *committed-information-rate*  **cbs** *committed-burst-size* [ **ebs** *excess-burst-size*  ]  **queue-length** *queue-length* ]]

**[qos gts **[{ **any** \| **acl** [ **ipv6** ] *acl-number* \| **queue** *queue-id* } **cir** *committed-information-rate*  **cbs** *committed-burst-size*  **pir** *peak-information-rate*  **ebs** *excess-burst-size*   **queue-length** *queue-length* ]]

**[undo qos gts **[{ **any** \| **acl** [ **ipv6** ] *acl-number* \| **queue** *queue-id* }]]

【缺省情况】

接口上没有配置流量整形。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[any**]：对所有的数据包进行流量整形。

**[acl ** **ipv6** ] *acl-number*：对匹配ACL的数据包进行流量整形。*acl-number*为ACL编号，取值范围与设备的型号有关，请以设备的实际情况为准。若未指定**ipv6**关键字，表示IPv4 ACL；否则表示IPv6 ACL。

**[queue ***queue-id*]**：**对队列queue上的数据包进行流量整形，*queue-id*为匹配的队列号。

**[cir** *committed-information-rate*]：承诺信息速率[，单位为]kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[cbs*** committed-burst-size*]：承诺突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs*** excess-burst-size*]：超出突发尺寸，在双令牌桶算法中超出承诺突发流量的部分，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率，单位为kbps。PIR必须大于等于CIR。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[queue-length** *queue-length*]：缓存队列的最大长度。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

不配置峰值速率表示所配置的是单速桶流量整形，否则表示双速桶流量整形。

【举例】

\# 在接口GigabitEthernet1/0/1上对满足ACL规则2001的报文进行流量整形。正常流速为200kbps，突发流量为50000bytes，以后速率小于等于200kbps时正常发送，速率大于200kbps时，将进入缓存队列，缓存队列长度为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos gts acl 2001 cir 200 cbs 50000 ebs 0 queue-length 100

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- qos gts percent (interface view)**

------------------------------------------------------------------------

**[qos gts percent**]命令用来采用百分比的方式在接口上配置流量整形。

**[undo qos gts**]命令用来取消接口上流量整形的配置。

【命令】

**[qos gts **[{ **any** \| **acl** [ **ipv6** ] *acl-number* \| **queue** *queue-number* } **percent** **cir** *cir-percent*  **cbs** *cbs-time* [ **ebs** *ebs-time*  ]  **queue-length** *queue-length* ]]

**[qos gts **[{ **any** \| **acl** [ **ipv6** ] *acl-number* \| **queue** *queue-number* } **percent** **cir** *cir-percent*  **cbs** *cbs-time*  **pir** *pir-percent*  **ebs** *ebs-time*   **queue-length** *queue-length* ]]

**[undo qos gts **[{ **any** \| **acl** [ **ipv6** ] *acl-number* \| **queue** *queue-number* }]]

【缺省情况】

接口上没有配置百分比形式的流量整形。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[any**]：对所有的数据包进行流量整形。

**[acl ** **ipv6** ] *acl-number*：对匹配ACL的数据包进行流量整形。*acl-number*为ACL编号，取值范围与设备的型号有关，请以设备的实际情况为准。若未指定**ipv6**关键字，表示IPv4 ACL；否则表示IPv6 ACL。

**[queue ***queue-number*]：对队列queue上的数据包进行流量整形，*queue-number*为匹配的队列号。

**[percent** **cir** *cir-percent*]：以百分比的形式来指定承诺信息速率。取值范围为1\~100。

**[cbs** *cbs-time*]：用指定的时间（单位为ms）来设置CBS，实际的CBS值是*cbs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *ebs-time*]：用指定的时间（单位为ms）来设置EBS，实际的EBS值是*ebs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir ***pir-percent*]：以百分比的形式来指定峰值速率，取值范围为1\~100。峰值速率不能比承诺信息速率小。该参数的支持情况与设备的型号有关。

**[queue-length** *queue-length*]：缓存队列的最大长度。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

不配置峰值速率表示所配置的是单速桶流量整形，否则表示双速桶流量整形。

【举例】

\# 在接口GigabitEthernet1/0/1上对所有的报文进行流量整形。指定CIR 50%，CBS 1000 ms。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos gts any percent cir 50 cbs 1000

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- qos gts(user-profile view)**

------------------------------------------------------------------------

**[qos gts**]命令用来在User Profile下配置流量整形。

**[undo qos gts**]命令用来取消User Profile流量整形的配置。

【命令】

**[qos gts cir ***committed-information-rate***** **cbs** *committed-burst-size*  **ebs** *excess-burst-size*  ]

**[undo qos gts **]

【缺省情况】

User Profile下没有配置流量整形。

【视图】

User Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cir** *committed-information-rate*]：承诺信息速率，单位为kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[cbs*** committed-burst-size*]：承诺突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs*** excess-burst-size*]：超出突发尺寸，单位为byte，缺省值为0 byte。取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 对上线用户接收的匹配队列7的报文进行流量整形。正常流速为200kbps，突发流量为50000bytes，以后速率小于等于200kbps时正常发送，速率大于200kbps时，将进入缓存队列。

\<Sysname\> system-view

Sysname user-profile user

Sysname-user-profile-user qos gts cir 200 cbs 50000

**流量监管、流量整形和限速 \-- 限速配置命令 \-- display qos lr**

------------------------------------------------------------------------

**[display qos lr**]命令用来显示接口或PW上的限速配置情况和统计信息。

【命令】

**[display qos lr **{ **interface** [ *interface-type interface-number*  \| **l2vpn-pw**  **peer** *ip-address* **pw-id** *pw-id*  }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的限速配置情况和运行统计信息。

**[peer ***ip-address ***pw-id*** pw-id*]：显示指定PW上的限速配置情况和运行统计信息。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果未指定本参数，将显示所有PW上的限速配置情况和运行统计信息。

【举例】

\# 显示所有接口的接口限速配置情况和统计信息。

\<Sysname\> display qos lr interface

Interface: GigabitEthernet1/0/1

 Direction: Inbound

  CIR 2000 (kbps), CBS 20000 (Bytes), EBS 0 (Bytes)

  Passed   : 1000 (Packets) 1000 (Bytes)

  Discarded: 1000 (Packets) 1000 (Bytes)

  Delayed  : 1000 (Packets) 1000 (Bytes)

  Active shaping: No

Interface: GigabitEthernet1/0/2

 Direction: Outbound

  CIR 50 (%), CBS 600 (ms), EBS 0 (ms)

  Passed   : 1000 (Packets) 1000 (Bytes)

  Discarded: 1000 (Packets) 1000 (Bytes)

  Delayed  : 1000 (Packets) 1000 (Bytes)

  Active shaping: No

\# 显示所有PW上的限速配置情况和统计信息。

\<Sysname\> display qos lr l2vpn-pw

L2VPN-PW: peer 1.2.3.4, pw-id 1

  Direction: Outbound

   CIR 1024 (kbps), CBS 64000 (Bytes), EBS 0 (Bytes)

   Passed   : 0 (Packets) 0 (Bytes)

   Delayed  : 0 (Packets) 0 (Bytes)

   Active shaping: No

表3-3 display qos lr命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号结合在一起组成

L2VPN-PW

显示指定PW的信息，PW通过远端PE地址和PW ID唯一标识

Direction

方向，可以是Inbound、Outbound

CIR

承诺信息速率，当采用绝对值形式输入时，单位为kbps；当采用百分比形式时，单位为%

CBS

承诺突发尺寸，当采用绝对值形式输入时，单位为byte；当采用百分比形式时，单位为ms，实际的CBS值是*cbs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）

EBS

超出突发尺寸，当采用绝对值形式输入时，单位为byte；当采用百分比形式时，单位为ms，实际的EBS值是*ebs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）

Passed

已经通过的数据包数目和字节数

Discarded

被丢弃的数据包数目和字节数

Delayed

被延迟发送的数据包数目和字节数

Active shaping

当前限速配置是否被激活，Yes表示激活，No表示未激活

**流量监管、流量整形和限速 \-- 限速配置命令 \-- qos lr**

------------------------------------------------------------------------

**[qos lr**]命令用来配置限速。

**[undo qos lr**]命令用来取消配置的限速。

【命令】

**[qos lr **[{ **inbound** \| **outbound** } **cir** *committed-information-rate* [ **cbs** *committed-burst-size* [ **ebs** *excess-burst-size* ] ]]]

**[undo qos lr**[ { **inbound** \| **outbound** }]]

【缺省情况】

没有配置限速。

【视图】

接口视图/交叉连接PW视图/VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对接收的数据流进行限速。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：对发送的数据流进行限速。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cir** *committed-information-rate*]：承诺信息速率，单位为kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[cbs*** committed-burst-size*]：承诺突发尺寸，单位为bytes。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs*** excess-burst-size*]：超出突发尺寸，在双令牌桶算法中超出承诺突发流量的部分，单位为bytes。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 对接口GigabitEthernet1/0/1上出方向的报文进行限速。正常流速为200kbps，突发流量为50000bytes，以后速率小于等于200kbps时正常发送，速率大于200kbps时，将进行限速。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos lr outbound cir 200 cbs 50000

**流量监管、流量整形和限速 \-- 限速配置命令 \-- qos lr percent**

------------------------------------------------------------------------

**[qos lr percent**]命令用来采用百分比的方式在接口上配置接口限速。

**[undo qos lr**]命令用来取消接口上配置接口限速的配置。

【命令】

**[qos lr **[{ **inbound** \| **outbound** } **percent cir** *cir-percent* [ **cbs** *cbs-time* [ **ebs** *ebs-time* ] ]]]

**[undo qos lr**[ { **inbound \| outbound** }]]

【缺省情况】

接口上没有配置百分比形式的限速。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：限制接口上入方向报文的速率。本参数的支持情况与设备的型号有关。

**[outbound**]：限制接口上出方向报文的速率。本参数的支持情况与设备的型号有关。

**[percent cir ***cir-percent*]：以百分比的形式来指定承诺信息速率。取值范围为1\~100。

**[cbs** *cbs-time*]：用指定的时间（单位为ms）来设置CBS，实际的CBS值是*cbs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *ebs-time*]：用指定的时间（单位为ms）来设置EBS，实际的EBS值是*ebs-time*乘以实际的承诺信息速率（**cir**值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir ***pir-percent*]：以百分比的形式来指定峰值速率，取值范围为1\~100。峰值速率不能比承诺信息速率小。不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。该参数的支持情况与设备的型号有关。

【举例】

\# 在接口GigabitEthernet 1/0/1上配置限制接口出方向的报文速率，指定CIR 50%，CBS 1000 ms。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos lr outbound percent cir 50 cbs 1000

\

**拥塞管理 \-- 拥塞管理公共配置命令 \-- display qos queue interface**

------------------------------------------------------------------------

**[display qos queue interface**]命令用来显示接口或PVC上队列配置情况和统计信息。

【命令】

**[display qos queue interface **[[ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的接口队列配置情况和运行统计信息。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名，*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的先进先出队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有接口下的队列信息。

\<Sysname\> display qos queue interface

Interface: GigabitEthernet1/0/1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0

  Weight: IP Precedence

  Queues: Active/Max active/Total 0/0/128

Interface: GigabitEthernet1/0/2

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

表4-1 display qos queue interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

当前出队列的相关信息

Urgent queuing

紧急队列

Protocol queuing

协议队列

FIFO queuing

先进先出队列

Size

队列中数据包的数目

Length

队列的长度

Discards

丢弃的数据包数目

Weighted Fair queuing

加权公平队列

Weight

权重类型，分为两类：IP Precedence和DSCP

Queues

WFQ队列的信息

Active

激活的WFQ队列数目

Max active

最大激活过的WFQ队列数目

Total

当前配置的WFQ队列总数

**拥塞管理 \-- 拥塞管理公共配置命令 \-- display qos queue l2vpn-pw**

------------------------------------------------------------------------

**[display qos queue l2vpn-pw**]命令用来显示PW上队列配置情况和统计信息。

【命令】

**[display qos queue l2vpn-pw ** **peer** *ip-address* **pw-id** *pw-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer ***ip-address ***pw-id*** pw-id*]：显示指定PW上的队列配置情况和统计信息。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果未指定本参数，将显示所有PW上的队列配置情况和统计信息。

【举例】

\# 显示PW下的所有队列。

\<Sysname\> display qos queue l2vpn-pw

L2VPN-PW: peer 1.1.1.1, pw-id 1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

L2VPN-PW: peer 2.2.2.2 pw-id 2

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0

  Weight: IP Precedence

  Queues: Active/Max active/Total 0/0/128

表1-3 display qos queue l2vpn-pw命令显示信息描述表

字段

描述

 

L2VPN-PW

显示指定PW的信息，PW通过远端PE地址和PW ID唯一标识

 

Output queue

当前出队列的相关信息

 

Urgent queuing

紧急队列

 

Protocol queuing

协议队列

 

Weighted Fair queuing

加权公平队列

 

Protocol queuing

协议队列

Size

队列中数据包的数目

 

Length

队列的长度

 

Discards

丢弃的数据包数目

 

Weight

权重类型，分为两类：IP Precedence和DSCP

 

Queues

WFQ队列的信息

 

Active

激活的WFQ队列数目

 

Max active

最大激活过的WFQ队列数目

 

Total

当前配置的WFQ队列总数

 

**拥塞管理 \-- 拥塞管理公共配置命令 \-- reset qos statistics l2vpn-pw**

------------------------------------------------------------------------

**[reset qos statistics l2vpn-pw**]命令用来清除PW下QoS的统计信息。

【命令】

**[reset qos statistics l2vpn-pw ** **peer** *ip-address* **pw-id** *pw-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer ***ip-address ***pw-id*** pw-id*]：清除指定PW上的QoS的统计信息。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果未指定本参数，将清除所有PW上的QoS的统计信息。

【举例】

\# 清除QoS统计计数。

\<Sysname\> reset qos statistics l2vpn-pw peer 1.1.1.1 pw-id 1

**拥塞管理 \-- FIFO队列配置命令 \-- display qos queue fifo**

------------------------------------------------------------------------

**[display qos queue fifo**]命令用来显示指定接口、指定PVC、指定PW或所有接口及PVC、所有PW上的先进先出队列配置情况和统计信息。

【命令】

**[display qos queue fifo interface **[[ [ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ] \| **l2vpn-pw**  **peer** *ip-address* **pw-id** *pw-id*  }]]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的先进先出队列配置情况和统计信息。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名，*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的先进先出队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[peer ***ip-address ***pw-id*** pw-id*]：显示指定PW上的先进先出队列配置情况和统计信息。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果未指定本参数，将显示所有PW上的先进先出队列配置情况和统计信息。

【举例】

\# 显示所有接口的先进先出队列配置情况和统计信息。

\<Sysname\> display qos queue fifo interface

Interface: GigabitEthernet1/0/2

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

\# 显示所有PW下的先进先出队列配置情况和统计信息。

\<Sysname\> display qos queue fifo l2vpn-pw

L2VPN-PW: peer 1.1.1.1, pw-id 1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

表4-2 display qos queue fifo命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

L2VPN-PW

显示指定PW的信息，PW通过远端PE地址和PW ID唯一标识

Output queue

当前出队列的相关信息

Urgent queuing

紧急队列

Protocol queuing

协议队列

FIFO queuing

先进先出队列

Size

队列中数据包的数目

Length

队列的长度

Discards

丢弃的数据包数目

**拥塞管理 \-- FIFO队列配置命令 \-- qos fifo queue-length**

------------------------------------------------------------------------

**[qos fifo queue-length**]命令用来配置先进先出队列的长度。

**[undo qos fifo queue-length**]命令用来恢复缺省情况。

【命令】

**[qos fifo queue-length*** queue-length*]

**[undo qos fifo queue-length**]

【缺省情况】

先进先出队列的长度为75。

【视图】

接口视图/PVC视图/交叉连接PW视图/VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-length*]：队列的长度，取值范围为1～1024。

【使用指导】

若是子接口，则接口需要使能LR功能以保证队列生效。

【举例】

\# 配置FIFO队列的长度为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos fifo queue-length 100

【相关命令】

·**display qos queue fifo interface**

**拥塞管理 \-- 优先级队列配置命令 \-- display qos queue pq interface**

------------------------------------------------------------------------

**[display qos queue pq interface**]命令用来显示指定接口、指定PVC或所有接口及PVC上的优先级队列配置情况和统计信息。

【命令】

**[display qos queue pq interface **[[ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口上优先级队列配置情况和统计信息。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的优先级队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

若指定接口为Virtual-Template接口，将显示继承该Virtual-Template接口的所有Virtual-Access接口下的QoS PQ的信息，Virtual-Template本身无QoS信息显示。

【举例】

\# 显示接口GigabitEthernet1/0/1的优先级队列配置情况和统计信息。

\<Sysname\> display qos queue pq interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Priority queuing: PQL 1 Size/Length/Discards

Top:  0/20/0    Middle:  0/40/0    Normal:  0/60/0    Bottom:  0/80/0

表4-3 display qos queue pq interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

出队列信息

Urgent queuing

紧急队列

Protocol queuing

协议队列

Priority queuing

优先级队列，指明使用的优先级队列列表

Size

队列中数据包数目

Length

队列大小

Discards

丢弃的数据包数目

Top

高优先级队列

Middle

中优先级队列

Normal

普通优先级队列

Bottom

低优先级队列

**拥塞管理 \-- 优先级队列配置命令 \-- display qos pql**

------------------------------------------------------------------------

**[display qos pql**]命令用来显示指定或者所有优先级队列列表的内容。

【命令】

集中式设备：

**[display qos pql** [ *pql-index* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos pql** [ *pql-index*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display qos pql** [ *pql-index*   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[pql-index*]： 优先列表的组号，取值范围为1～16。

**[slot*** slot-number*]：显示指定单板的优先级队列列表的内容，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板的优先级队列列表的内容。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的优先级队列列表的内容，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主用设备的优先级队列列表的内容。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的优先级队列列表的内容，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的优先级队列列表的内容。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的优先级队列列表的内容，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板的优先级队列列表的内容。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的优先级队列列表的内容，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的优先级队列列表的内容。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示优先列表。

\<Sysname\> display qos pql

Current PQL configuration:

List  Queue   Parameters

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1     Top     Protocol ip less-than 1000

2     Normal  Length 80

2     Bottom  Length 40

3     Middle  Inbound-interface GigabitEthernet1/0/1

4     Top     Local-precedence  7

**拥塞管理 \-- 优先级队列配置命令 \-- qos pq**

------------------------------------------------------------------------

**[qos pq**]命令用来在接口或PVC上应用优先级队列调度机制。

**[undo qos pq**]命令用来将接口或PVC上的拥塞管理策略恢复到FIFO。

【命令】

**[qos pq pql** *pql-index*]

**[undo qos pq**]

【缺省情况】

接口拥塞管理策略为FIFO。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

【使用指导】

对于同一个接口或PVC，若优先队列的应用命令的重复使用，则最新的配置生效。

可以为优先列表的组配置多条分类规则，在进行流分类时，数据流按照顺序进行匹配，如果匹配上某规则，则进入相应的队列，匹配结束；如果数据包不与任何规则匹配，则进入缺省队列。

【举例】

\# 将第12组的优先列表应用到GigabitEthernet1/0/1上。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos pq pql 12

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql default-queue**

------------------------------------------------------------------------

**[qos pql default-queue**]命令用来为未匹配任何规则的数据包指定一个缺省队列。

**[undo qos pql default-queue**]命令用来恢复缺省情况。

【命令】

**[qos pql ***pql-index*** default-queue**[ { **bottom** \| **middle** \| **normal** \| **top** }]]

**[undo qos pql** *pql-index* **default-queue**]

【缺省情况】

队列为**normal**。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

**[top**]、**middle**、**normal**、**bottom**：对应PQ的四个队列，优先级依次降低。

【使用指导】

进行流分类的时候，如果数据包不与任何规则匹配，则进入缺省队列。

对于同一个*pql-index*，该命令重复使用操作，将设定新的缺省队列。

【举例】

\# 将优先列表中第12组中无对应规则的包的缺省队列设定为bottom。

\<Sysname\> system-view

Sysname qos pql 12 default-queue bottom

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql inbound-interface**

------------------------------------------------------------------------

**[qos pql inbound-interface**]命令用来配置基于接口的分类规则。

**[undo qos pql inbound-interface**]命令用来删除相应的分类规则。

【命令】

**[qos pql ***pql-index*[ **inbound-interface** *interface-type interface-number* **queue** { **bottom** \| **middle** \| **normal** \| **top** }]]

**[undo qos pql** *pql-index* **inbound-interface** *interface-type* *interface-number*]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

**[top**]、**middle**、**normal**、**bottom**：对应PQ的四个队列,优先级依次降低。

【使用指导】

该命令按报文输入的接口进行匹配。对于同一个*pql-index*，该命令可以重复使用，为来自不同接口的报文，建立不同的分类规则*。*

【举例】

\# 配置组号为12的优先列表的分类规则，使得来自GigabitEthernet1/0/1的报文进入**middle**队列。

\<Sysname\> system-view

Sysname qos pql 12 inbound-interface gigabitethernet 1/0/1 queue middle

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql local-precedence**

------------------------------------------------------------------------

**[qos pql local-precedence**]命令用来配置基于本地优先级的分类规则。

**[undo qos pql local-precedence**]命令用来删除相应的规则。

【命令】

**[qos pql ***pql-index*[ **local-pecedence** *local-precedence-list* **queue** { **bottom** \| **middle** \| **normal** \| **top** }]]

**[undo** **qos pql** *pql-index* **local-precedence** *local-precedence-list*]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

*[local-precedence-list*]：要匹配的本地优先级的列表，最多可以输入8个*local-precedence*，取值范围为0～7。

**[top**]、**middle**、**normal**、**bottom**：对应PQ的四个队列，优先级依次降低。

【使用指导】

该命令按报文的本地优先级进行匹配。对于同一个*pql-index*，该命令可以重复使用，为不同本地优先级的报文，建立不同的分类规则*。*

【举例】

\# 配置组号为12的优先列表的分类规则，使得本地优先级等于3的报文进入**middle**队列。

\<Sysname\> system-view

Sysname qos pql 12 local-precedence 3 queue middle

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql protocol**

------------------------------------------------------------------------

**[qos pql protocol**]命令用来配置基于协议的分类规则。

**[undo qos pql protocol**]命令用来删除相应的分类规则。

【命令】

**[qos pql**[ *pql-index* **protocol** { **ip** \| **ipv6** } [ *queue-key key-value* ] **queue** { **bottom** \| **middle** \| **normal** \| **top** }]]

**[undo******qos pql**[ *pql-index* **protocol** { **ip** \| **ipv6** } [ *queue-key key-value* ]]]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

**[top**]、**middle**、**normal**、**bottom**：对应PQ的四个队列，优先级依次降低。

*[queue-key key-value*]：将IP或者IPv6报文分类进入队列。*queue-key*和*key-value*的取值见下表。当不输入*queue-key*和*key-value*时，表示所有IP或者IPv6报文进入队列。

表4-4 queue-key和key-value的取值

*[queue-key*]

*[key-value*]

说明

acl

access-list-number（2000～3999）

符合某访问控制列表定义的IP或者IPv6报文进入队列

fragments

-

分片的IP或者IPv6报文进入队列

greater-than

长度值（0～65535）

长度大于某个计数值的IP或者IPv6报文进入队列

less-than

长度值（0～65535）

长度小于某个计数值的IP或者IPv6报文进入队列

tcp

端口号（0～65535）

源或目的TCP端口号为指定的端口号的IP或者IPv6报文进入队列

udp

端口号（0～65535）

源或目的UDP端口号为指定的端口号的IP或者IPv6报文进入队列

【使用指导】

设备是以规则被配置的顺序来匹配数据包，如果发现数据包与某个规则匹配，便结束整个查找。

对于同一个*pql-index*，该命令可以重复使用，为IP数据包建立多种分类规则。

当*queue-key*指定为**tcp**或**udp**时，*key-value*的值既可以直接使用端口名称，也可以使用相关端口号。

【举例】

\# 配置组号为5的优先列表的分类规则，使满足ACL为3100规则定义的IP报文进入top队列。

\<Sysname\> system-view

Sysname qos pql 5 protocal ip acl 3100 queue top

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql protocol mpls exp**

------------------------------------------------------------------------

**[qos pql protocol mpls exp**]命令用来配置基于MPLS EXP优先级的分类规则。

**[undo qos pql protocol mpls exp**]命令用来删除相应的分类规则。

【命令】

**[qos pql ***pql-index*[ **protocol mpls exp** *exp-list* **queue** { **bottom** \| **middle** \| **normal** \| **top** }]]

**[undo******qos** **pql** *pql-index* **protocol** **mpls** exp *exp-list*]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

*[exp-list*]：要匹配的MPLS EXP优先级的报文列表，最多可以输入8个*exp*，*exp*取值范围为0～7。

**[top**]、**middle**、**normal**、**bottom**：对应PQ的四个队列，优先级依次降低。

【使用指导】

该命令按报文的MPLS EXP优先级进行匹配，对于同一个*pql-index*，该命令可以重复使用，为不同MPLS EXP优先级的报文建立不同的分类规则

【举例】

\# 配置组号为12的优先列表的分类规则，将MPLS EXP优先级为2、4的报文进入top队列。

\<Sysname\> system-view

Sysname qos pql 5 protocal mpls exp 2 4 queue top

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql queue**

------------------------------------------------------------------------

**[qos pql queue **]命令用来设置各队列的长度（所容纳的数据包个数）。

**[undo qos pql queue**]命令用来恢复队列长度的缺省值。

【命令】

**[qos pql**[ *pql-index* **queue** { **bottom** \| **middle** \| **normal** \| **top** } **queue-length** *queue-length*]]

**[undo qos pql**[ *cql-index* **queue** { **bottom** \| **middle** \| **normal** \| **top** } **queue-length**]]

【缺省情况】

高优先队列的缺省长度值为20，中优先队列的缺省长度值为40，正常优先队列的缺省长度值为60，低优先队列的缺省长度值为80。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pql-index*]：优先列表的组号，取值范围为1～16。

**[top**]、**middle**、**normal**、**bottom**：对应PQ的四个队列，优先级依次降低。

**[queue-length*** queue-length*]：队列的最大长度，取值范围为1～1024。

【使用指导】

如果队列的长度达到最大值时，后面收到的属于该队列的数据包将被丢弃。

【举例】

\# 配置优先列表第5组top队列的长度为10。

\<Sysname\> system-view

Sysname qos pql 5 queue top queue-length 10

**拥塞管理 \-- 定制队列配置命令 \-- display qos queue cq interface**

------------------------------------------------------------------------

**[display qos queue cq interface**]命令用来显示指定接口、指定PVC或所有接口及PVC上的定制队列配置情况和统计信息。

【命令】

**[display qos queue cq interface **[[ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口上定制队列配置情况和统计信息。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的定制队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

若指定接口为Virtual-Template接口，将显示继承该Virtual-Template接口的所有Virtual-Access接口下的QoS CQ的信息，Virtual-Template本身无QoS信息显示。

【举例】

\#显示接口GigabitEthernet1/0/1的定制队列配置情况和统计信息。

\<Sysname\>display qos queue cq interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Custom queuing: CQL 1 Size/Length/Discards

 1:   0/  20/0          2:   0/  20/0          3:   0/  20/0

 4:   0/  20/0          5:   0/  20/0          6:   0/  20/0

 7:   0/  20/0          8:   0/  20/0          9:   0/  20/0

10:   0/  20/0         11:   0/  20/0         12:   0/  20/0

13:   0/  20/0         14:   0/  20/0         15:   0/  20/0

16:   0/  20/0

表4-5 display qos queue cq interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

出队列信息

Urgent queuing

紧急队列

Protocol queuing

协议队列

Custom queuing

定制队列，指明使用的定制队列列表

Size

队列中数据包数目

Length

队列大小

Discards

丢弃的数据包数目

**拥塞管理 \-- 定制队列配置命令 \-- display qos cql**

------------------------------------------------------------------------

**[display qos cql**]命令用来显示指定或所有定制队列列表的内容。

【命令】

集中式设备：

**[display qos cql** [ *cql-index* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos cql** [ *cql-index*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display qos cql** [ *cql-index*   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[cql-index*]：优先列表的组号，取值范围为1～16。如果未指定本参数，则显示所有列表的内容。

**[slot*** slot-number*]：显示指定单板的定制列表的内容，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板的定制列表的内容。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的定制列表的内容，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主用设备的类的定制列表的内容。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的定制列表的内容，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的定制列表的内容。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的定制列表的内容，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板的定制列表的内容。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的定制列表的内容，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的定制列表的内容。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示所有定制列表的内容。

\<Sysname\> display qos cql

Current CQL configuration:

List  Queue  Parameters

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

2     3      Protocol ip fragments

3     6      Length 100

3     1      Inbound-interface GigabitEthernet1/0/1

4     5      Local-precedence 7

**拥塞管理 \-- 定制队列配置命令 \-- qos cq**

------------------------------------------------------------------------

**[qos cq**]命令用来在接口或PVC上应用定制队列。

**[undo qos cq**]命令用来将接口或PVC上的拥塞管理策略恢复到FIFO。

【命令】

**[qos cq cql ***cql-index*]

**[undo qos cq**]

【缺省情况】

接口拥塞管理策略为FIFO。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1\~16。

【使用指导】

对于同一个接口或PVC，若定制队列的应用命令的重复使用，则最新的配置生效。

可以为定制列表的组配置多条分类规则，在进行流分类时，数据流按照顺序进行匹配，如果匹配上某规则，则进入相应的队列，匹配结束；如果数据包不与任何规则匹配，则进入缺省队列。

若是Tunnel接口、子接口、三层聚合接口、HDLC捆绑接口、RPR逻辑接口，或是封装了PPPoE、PPPoA、PPPoEoA、PPPoFR、MPoFR（FR接口未使能帧中继流量整形功能）协议的VT、Dialer接口，则接口需要使能LR功能以保证队列生效。

【举例】

\# 将第5组的定制列表应用到GigabitEthernet1/0/1上。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos cq cql 5

**拥塞管理 \-- 定制队列配置命令 \-- qos cql default-queue**

------------------------------------------------------------------------

**[qos cql default-queue**]命令用来为未匹配任何规则的数据包指定一个缺省队列。

**[undo qos cql default-queue**]命令用来恢复缺省情况。

【命令】

**[qos cql** *cql-index* **default-queue** *queue-id*]

**[undo** **qos** **cql** *cql-index* **default-queue**]

【缺省情况】

队列号为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[queue-id*]：队列号，取值范围为1～16。

【使用指导】

在进行流分类的时候，如果数据包不与任何规则匹配，则进入缺省队列。

【举例】

\# 指定定制列表第5组的缺省队列为2。

\<Sysname\> system-view

Sysname qos cql 5 default-queue 2

**拥塞管理 \-- 定制队列配置命令 \-- qos cql inbound-interface**

------------------------------------------------------------------------

**[qos cql inbound-interface**]命令用来建立基于接口的分类规则。

**[undo qos cql inbound-interface**]命令用来删除相应的分类规则。

【命令】

**[qos cql** *cql-index* **inbound-interface** *interface-type interface-number* **queue** *queue-id*]

**[undo qos cql** *cql-index* **inbound-interface** *interface-type* *interface-number*]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[interface-type interface-number*]：指定的接口类型和接口编号*。*

*[queue-id*]：队列号，取值范围为1～16。

【使用指导】

该命令按报文输入的接口进行匹配。对于同一个*cql-index*，该命令可以重复使用，为来自不同接口的报文，建立不同的分类规则。

【举例】

\# 配置组号为5的定制列表的分类规则，将来自GigabitEthernet1/0/1的报文进入队列3。

\<Sysname\> system-view

Sysname qos cql 5 **inbound-interface** gigabitethernet 1/0/1 **queue 3**

**拥塞管理 \-- 定制队列配置命令 \-- qos cql local-precedence**

------------------------------------------------------------------------

**[qos cql local-precedence**]命令用来建立基于本地优先级的分类规则。

**[undo qos cql local-precedence**]命令用来删除相应的规则。

【命令】

**[qos cql** *cql-index* **local-precedence** *local-precedence-list* **queue** *queue-id*]

**[undo** **qos cql** *cql-index* **local-precedence** *local-precedence-list*]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[local-precedence-list*]：要匹配的本地优先级的列表，最多可以输入8个*local-precedence*，取值范围为0～7。

*[queue-id*]：定制队列的队列号，取值范围为1\~16。

【使用指导】

该命令按报文的本地优先级进行匹配。对于同一个*cql-index*，该命令可以重复使用，为不同本地优先级的报文建立不同的分类规则。

【举例】

\# 配置组号为5的定制列表的分类规则，将本地优先级等于4的报文进入队列3。

\<Sysname\> system-view

Sysname qos cql 5 local-precedence 4 queue 3

**拥塞管理 \-- 定制队列配置命令 \-- qos cql protocol**

------------------------------------------------------------------------

**[qos cql protocol**]命令用来配置基于协议的分类规则。

**[undo qos cql protocol**]命令用来删除相应的分类规则。

【命令】

**[qos cql**[ *cql-index* **protocol** { **ip** \| **ipv6** } [ *queue-key key-value* ] **queue** *queue-id*]]

**[undo******qos cql**[ *cql-index* **protocol** { **ip** \| **ipv6** } [ *queue-key key-value* ]]]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[queue-id*]：队列号，取值范围为1\~16。

*[queue-key key-value*]：将IP或者IPv6报文分类进入队列。*queue-key*和*key-value*的取值见下表。当不输入*queue-key*和*key-value*时，表示所有IP或者IPv6报文进入队列。

表4-6 queue-key和key-value的取值

*[queue-key*]

*[key-value*]

说明

acl

access-list-number（2000\~3999）

符合某访问控制列表定义的IP或者IPv6报文就进入队列

fragments

-

只要是分片的IP或者IPv6报文就进入队列

greater-than

长度值（0\~65535）

长度大于指定长度值的IP或者IPv6报文进入队列

less-than

长度值（0\~65535）

长度小于指定长度值的IP或者IPv6报文进入队列

tcp

端口号（0\~65535）

源或目的TCP端口号为指定的端口号的IP或者IPv6报文进入队列

udp

端口号（0\~65535）

源或目的UDP端口号为指定的端口号的IP或者IPv6报文进入队列

【使用指导】

系统是以规则被配置的顺序来匹配数据包，如果发现数据包与某个规则匹配，便结束整个查找。

对于同一个*cql-index*，该命令可以重复使用，为IP数据包建立多种分类规则。

当*queue-key*指定为tcp或udp时，*key-value*的值既可以直接使用端口名称，也可以使用相关端口号。

【举例】

\# 配置组号为5的定制列表的分类规则，将匹配访问控制列表3100的IP报文进入队列3。

\<Sysname\> system-view

Sysname qos cql 5 protocol ip acl 3100 queue 3

**拥塞管理 \-- 定制队列配置命令 \-- qos cql protocol mpls exp**

------------------------------------------------------------------------

**[qos cql protocol mpls exp**]命令用来配置基于MPLS EXP优先级的分类规则。

**[undo qos cql protocol mpls exp**]命令用来删除相应的分类规则**。**

【命令】

**[qos cql** *cql-index* **protocol mpls exp** *exp-list* **queue** *queue-id*]

**[undo qos cql** *cql-index* **protocol mpls exp** *exp-list*]

【缺省情况】

没有配置任何分类规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[exp-list*]：要匹配的MPLS EXP优先级的报文列表，最多可以输入8个*exp*，*exp*取值范围为0～7。

*[queue-id*]：队列号，取值范围为1～16。

【使用指导】

该命令按报文的MPLS EXP优先级进行匹配，对于同一个*cql-index*，该命令可以重复使用，为不同MPLS EXP优先级的报文建立不同的分类规则

【举例】

\# 配置组号为5的定制列表的分类规则，将MPLS EXP优先级为2、4的报文进入队列3。

\<Sysname\> system-view

Sysname qos cql 5 protocol mpls exp 2 4 queue 3

**拥塞管理 \-- 定制队列配置命令 \-- qos cql queue**

------------------------------------------------------------------------

**[qos cql queue **]命令用来设置各队列的长度（所容纳的数据包个数）**。**

**[undo qos cql queue**]命令用来恢复队列长度的缺省值。

【命令】

**[qos cql** *cql-index* **queue** *queue-id* **queue-length** *queue-length*]

**[undo qos cql ***cql-index* **queue** *queue-id* **queue-length**]

【缺省情况】

队列长度值是20。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[queue-id*]：队列号，取值范围为1～16。

*[queue-length*]：队列的最大长度，取值范围为1～1024。

【使用指导】

如果队列的长度达到最大值时，后面收到的属于该队列的数据包将被丢弃。

【举例】

\# 指定定制列表第5组队列4的长度为40。

\<Sysname\> system-view

Sysname qos cql 5 queue 4 queue-length 40

**拥塞管理 \-- 定制队列配置命令 \-- qos cql queue serving**

------------------------------------------------------------------------

**[qos cql queue serving**]命令用来设置各队列每次轮询所发送数据包的字节数。

**[undo qos cql queue serving**]命令用来恢复发送数据包数的缺省值。

【命令】

**[qos cql** *cql-index* **queue** *queue-id* **serving** *byte-count*]

**[undo******qos cql** *cql-index* **queue** *queue-id* **serving**]

【缺省情况】

发送数据包的字节数为1500。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cql-index*]：定制列表的组号，取值范围为1～16。

*[queue-id*]：队列号，取值范围为1～16。

*[byte-count*]：队列每次轮询所发送的数据包的字节数，取值范围为1～16777215。

【举例】

\# 指定定制列表第5组队列2每次轮询所发送数据包的字节数为1400。

\<Sysname\> system-view

Sysname qos cql 5 queue 2 serving 1400

**拥塞管理 \-- 加权公平队列配置命令 \-- display qos queue wfq**

------------------------------------------------------------------------

**[display qos queue wfq**]命令用来显示指定接口、指定PVC、指定PW或所有接口及PVC、所有PW上的加权公平队列配置情况和统计信息。

【命令】

**[display qos queue wfq interface**[ { [ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ] \| **l2vpn-pw**  **peer** *ip-address* **pw-id** *pw-id*  }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的加权公平队列配置情况和统计信息。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的加权公平队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[peer ***ip-address ***pw-id*** pw-id*]：显示指定PW上的加权公平队列配置情况和统计信息。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果未指定本参数，将显示所有PW上的加权公平队列配置情况和统计信息。

【举例】

\# 显示接口GigabitEthernet1/0/1的加权公平队列配置情况和统计信息。

\<Sysname\> display qos queue wfq interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0

  Weight: IP Precedence

  Queues: Active/Max active/Total 0/0/128

\# 显示所有PW下的加权公平队列配置情况和统计信息。

\<Sysname\> display qos queue wfq l2vpn-pw

L2VPN-PW: peer 1.1.1.1, pw-id 1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0

  Weight: IP Precedence

  Queues: Active/Max active/Total 0/0/128

表1-4 表4-4 display qos queue wfq命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

L2VPN-PW

显示指定PW的信息，PW通过远端PE地址和PW ID唯一标识

Output queue

当前出队列的相关信息

Urgent queuing

紧急队列

Protocol queuing

协议队列

Weighted Fair queuing

加权公平队列

Size

队列中数据包的数目

Length

队列的长度

Discards

丢弃的数据包数目

Weight

权重类型，分为两类：IP Precedence和DSCP

Queues

WFQ队列的信息

Active

激活的WFQ队列数目

Max active

最大激活过的WFQ队列数目

Total

当前配置的WFQ队列总数

**拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq**

------------------------------------------------------------------------

**[qos wfq**]命令用来在接口、PVC或PW上应用加权公平队列或修改加权公平队列的参数。

**[undo qos wfq**]命令用来恢复缺省拥塞管理机制FIFO。

【命令】

**[qos wfq **[[ **dscp** \| **precedence**   **queue-number** *total-queue-number* \| **queue-length** *max-queue-length* ] \*]]

**[undo qos wfq**]

【缺省情况】

接口/PVC上没有配置WFQ队列。

【视图】

接口视图/PVC视图/交叉连接PW视图/VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dscp**]：区分服务编码点权重类型。

**[precedence**]：IP优先级权重类型。

**[queue-length ***max-queue-length*]：队列的最大长度，即每个队列中可容纳的数据包的最大个数，超出后数据包将被丢弃，取值范围为1～1024，缺省值为64。

**[queue-number*** total-queue-number*]：队列的总数目，可取的值为：16、32、64、128、256、512、1024、2048、4096，缺省值为256。

【描述】

如果未指定权重类型，系统默认权重类型为**precedence**。

若是子接口，则接口需要使能LR功能以保证队列生效。

【举例】

\# 在接口GigabitEthernet1/0/1上应用WFQ，并设置队列长度为100，总队列个数设置为512个。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq queue-length 100 queue-number 512

【相关命令】

·**display qos ****queue wfq interface**

**拥塞管理 \-- 实时传输协议队列的配置命令 \-- display qos queue rtpq interface**

------------------------------------------------------------------------

**[display qos queue rtpq interface**]命令用来显示指定接口、指定PVC或所有接口及PVC的当前IP RTP Priority的队列信息，包括当前的RTP长度和RTP报文的丢包数。

【命令】

**[display qos queue rtpq interface **[[ *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口上当前IP RTP Priority的队列信息，包括当前的RTP长度和RTP报文的丢包数。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的当前IP RTP Priority的队列信息，包括当前的RTP长度和RTP报文的丢包数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如指定接口为Virtual-Template接口，将显示继承该Virtual-Template接口的所有Virtual-Access接口下的QoS RTP队列的信息，Virtual-Template本身无QoS信息显示。

【举例】

\# 显示当前IP RTP Priority的队列信息。

\<Sysname\> display qos queue rtpq interface

Interface: GigabitEthernet1/0/1

Output queue - RTP queuing: Size/Max/Outputs/Discards 0/0/0/0

表4-7 display qos queue rtpq interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

当前的输出队列

Size

队列中数据包数目

Max

队列中数据包的历史最大数目

Outputs

发送出去的数据包数目

Discards

丢弃的数据包数目

**拥塞管理 \-- 实时传输协议队列的配置命令 \-- qos rtpq**

------------------------------------------------------------------------

**[qos rtpq**]命令用来启动接口或PVC下RTP队列特性，为某个UDP目的端口范围的RTP报文保留一个实时业务。

**[undo qos rtpq **]命令用来关闭接口或PVC的RTP队列特性。

【命令】

**[qos rtpq start-port** *first-rtp-port-number* **end-port** *last-rtp-port-number* **bandwidth** *bandwidth* [ **cbs** *committee-burst-size* ]]

**[undo qos rtpq**]

【缺省情况】

接口或PVC上没有启动RTP队列特性。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[start-port*** first-rtp-port-numbe*r]：指定发起RTP报文的第一个UDP目的端口号，取值范围为2000～65535。

**[end-port*** last-rtp-port-number*]：指定发起RTP报文的最后一个UDP目的端口号，取值范围为2000～65535。

**[bandwidth ***bandwidth*]：RTP队列所占用的带宽，取值范围为8～1000000，单位为kbps。

**[cbs** *committee-burst-size*]：指定承诺突发尺寸，取值范围为1500～2000000字节，单位为字节。

【使用指导】

该命令主要应用于对时延敏感的应用，如实时语音传输。**qos rtpq**命令为语音业务提供最优先服务。

在配置**bandwidth**参数时，配置值通常应大于此实时业务所需的带宽总量，以预防突发流量的冲击。

【举例】

\# 在接口GigabitEthernet1/0/1上启动RTP队列特性，发起RTP报文的第一个UDP目的端口号为16384，发起RTP报文的最后一个UDP目的端口号为32767，RTP报文占用64kbps的带宽，如果输出接口拥塞，进入RTP队列。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos rtpq start-port 16384 end-port 32767 bandwidth 64

**拥塞管理 \-- 基于类的队列配置命令 \-- display qos queue cbq**

------------------------------------------------------------------------

**[display qos queue cbq**]命令用来显示指定接口、指定PVC、指定PW或所有接口与PVC、所有PW上的基于类的队列配置信息和运行情况。

【命令】

**[display qos queue cbq interface**[ { [ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ] \| **l2vpn-pw**  **peer** *ip-address* **pw-id** *pw-id*  }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的基于类的队列配置信息和运行情况。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的基于类的队列配置信息和运行情况。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[peer ***ip-address ***pw-id*** pw-id*]：显示指定PW上的加权公平队列配置情况和统计信息。*ip-address*为PW远端PE的LSR ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果未指定本参数，将显示所有PW上的基于类的队列配置情况和统计信息。

【举例】

\# 显示所有接口的基于类的队列配置信息和运行情况。

\<Sysname\> display qos queue cbq interface

Interface: GigabitEthernet1/0/1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Class Based Queuing: Size/Discards 0/0

Queue Size: EF/AF/BE 0/0/0

  BE Queues: Active/Max active/Total 0/0/256

  AF Queues: Allocated 1

  Bandwidth(kbps): Available/Max reserve 74992/75000

\# 显示所有PW下的基于类的队列配置情况和统计信息。

\<Sysname\> display qos queue cbq l2vpn-pw

L2VPN-PW: peer 1.1.1.1, pw-id 1

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - Class Based Queuing: Size/Discards 0/0

Queue Size: EF/AF/BE 0/0/0

  BE Queues: Active/Max active/Total 0/0/256

  AF Queues: Allocated 1

  Bandwidth(kbps): Available/Max reserve 74992/75000

表4-8 display qos queue cbq命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

L2VPN-PW

显示指定PW的信息，PW通过远端PE地址和PW ID唯一标识

Output queue

当前出队列的相关信息

Urgent queuing

紧急队列

Protocol queuing

协议队列

Class Based Queuing

基于类的队列

Size

队列中数据包的数目

Length

队列的长度

Discards

丢弃的数据包数目

EF

加速转发队列

AF

保证转发队列

BE

尽力转发队列

Active

BE队列当前处于激活状态的队列数

Max active

BE队列最大处于激活状态队列数

Total

BE队列总数

Bandwidth(kbps)

带宽

Available

CBQ当前可用带宽

Max reserve

CBQ最大预留带宽

**拥塞管理 \-- 基于类的队列配置命令 \-- qos reserved-bandwidth**

------------------------------------------------------------------------

**[qos reserved-bandwidth**]命令用来设置最大预留带宽占可用带宽的百分比。

**[undo qos reserved-bandwidth**]命令用来恢复缺省情况。

【命令】

**[qos reserved-bandwidth pct** *percent*]

**[undo qos reserved-bandwidth**]

【缺省情况】

最大预留带宽占可用带宽的百分比为80。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[percent*]：预留带宽占可用带宽的百分比，取值范围为1～100。

【使用指导】

为队列分配带宽时，考虑到部分带宽用于控制协议报文、二层帧头等，通常配置的最大预留带宽不大于可用带宽的80％。

建议慎重使用该命令修改最大预留带宽。如果配置的最大预留带宽过大，发送的报文加上链路层的帧头有可能大于接口最大可用带宽，导致接口无法满足需求，建议使用缺省最大预留带宽。

接口最大可用带宽通过命令**bandwidth**进行配置，具体情况请参见接口分册命令参考中的介绍。

【举例】

\# 配置GigabitEthernet1/0/1接口的最大预留带宽占可用带宽的百分比为70。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos reserved-bandwidth 70

**拥塞管理 \-- 基于类的队列配置命令 \-- queue af**

------------------------------------------------------------------------

**[queue af**]命令用来配置类采用AF队列，并配置类可确保的最小带宽。

**[undo queue af**]命令用来取消配置。

【命令】

**[queue af bandwidth**[\| ]**remaining-pct***remaining-percentage*}

**[undo queue af**]

【缺省情况】]

没有配置类采用AF队列。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：带宽，单位kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[pct** *percentage*]：可用带宽的百分比，取值范围为1～100。

**[remaining-pct ***remaining-percentage*]：剩余带宽的百分比，取值范围为1～100。

【使用指导】

当在策略下将类与**queue af**所属行为关联时，必须满足：

·同一个策略下为AF队列和EF队列指定的带宽之和必须不大于该策略所应用接口的可用带宽；

·同一个策略下为AF队列和EF队列指定的带宽百分比之和必须不大于100；

·同一个策略下AF队列和EF队列的带宽的配置必须都采用相同的值的类型，比如都采用绝对值形式，或者都采用百分比形式。

【举例】

\# 为行为database配置采用AF队列，并且确保最小带宽为200kbps。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue af bandwidth 200

【相关命令】

·**display qos queue cbq interface**

·**traffic behavior**

**拥塞管理 \-- 基于类的队列配置命令 \-- queue ef**

------------------------------------------------------------------------

**[queue ef**]命令用来配置类采用EF队列，并配置最大带宽。

**[undo queue ef**]命令用来取消配置。

【命令】

**[queue ef bandwidth** { *bandwidth* [ **cbs** *burst*  \| **pct** *percentage*  **cbs-ratio** *ratio*  }]]

**[undo queue ef**]

【缺省情况】

没有配置类采用EF队列。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：带宽，单位kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[cbs** *burst*]：指定承诺突发尺寸，单位为字节，取值范围与设备的型号有关，请以设备的实际情况为准，缺省值为*bandwidth*×25。

**[pct** *percentage*]：可用带宽的百分比，取值范围为1～100。

**[cbs-ratio ***ratio*]：允许的突发因子，取值范围为25～500，缺省值是25。

【使用指导】

该命令在流行为视图下不能与**queue af**，**queue-length**同时使用。

在策略下，缺省类default-class不能与**queue ef**所属behavior关联。

当在策略下将类与**queue ef**所属行为关联时，必须满足：

·同一个策略下为AF队列和EF队列指定的带宽之和必须不大于该策略所应用接口的可用带宽。

·同一个策略下为AF队列和EF队列指定的带宽百分比之和必须不大于100。

·同一个策略下AF队列和EF队列的带宽的配置必须都采用相同的值的类型，比如都采用绝对值形式，或者都采用百分比形式。

·对于设置百分比形式**queue ef bandwidth** **pct** *percentage* [ **cbs-ratio** *ratio* ]，CBS = 接口可用带宽×*percentage*×*ratio*÷100。

·对于设置绝对值形式**queue ef bandwidth** *bandwidth* [ **cbs** *burst* ]，CBS = *burst*，若不指定*burst*，则CBS = *bandwidth*×25。

【举例】

\# 配置报文进入EF队列，最大带宽为200kbps，承诺突发尺寸为5000bytes。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue ef bandwidth 200 cbs 5000

【相关命令】

·**display qos queue cbq interface**

·**traffic behavior**

**拥塞管理 \-- 基于类的队列配置命令 \-- queue sp**

------------------------------------------------------------------------

**[queue sp**]命令用来配置类采用SP队列。

**[undo queue sp**]用来取消配置。

【命令】

**[queue sp**]

**[undo queue sp**]

【缺省情况】

没有配置类采用SP队列。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置了该命令的行为不能与缺省类关联使用。

队列长度为固定值，取值与产品的型号有关，请以设备的实际情况为准。

在同一流行为视图下**queue ****sp**不能与**queue ef**命令同时使用。

在同一流行为视图下**queue ****sp**不能与**queue af**和**queue-length**命令同时使用。

【举例】

\# 配置报文进入SP队列。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue sp

【相关命令】

·**display qos queue cbq interface**

·**traffic behavior**

**拥塞管理 \-- 基于类的队列配置命令 \-- queue wfq**

------------------------------------------------------------------------

**[queue wfq**]命令用来为缺省类配置采用公平队列。

**[undo queue wfq**]命令用来取消配置。

【命令】

**[queue wfq ** **queue-number** *total-queue-number* ]

**[undo queue wfq**]

【缺省情况】

没有为缺省类配置采用公平队列。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[queue-number*** total-queue-number*]：公平队列的数目，可取的值为16、32、64、128、256、512、1024、2048、4096，即2的幂数，缺省值为256。

【使用指导】

配置了该命令的行为仅仅可以与缺省类关联使用，另外，该命令还可以搭配**queue-length**命令或**wred**命令使用。

【举例】

\# 为缺省类配置使用WFQ，队列数为16。

\<Sysname\> system-view

Sysname traffic behavior test

Sysname-behavior-test queue wfq queue-number 16

Sysname qos policy user1

Sysname-qospolicy-user1 classifier default-class behavior test

【相关命令】

·**display qos queue cbq interface**

·**traffic behavior**

**拥塞管理 \-- 基于类的队列配置命令 \-- queue-length**

------------------------------------------------------------------------

**[queue-length**]命令用来配置最大队列长度，丢弃方式为尾部丢弃。

**[undo queue-length**]命令用来取消该配置。

【命令】

**[queue-length** *queue-length*]

**[undo queue-length**]

【缺省情况】

丢弃方式为尾部丢弃方式，队列长度为64。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-length*]：队列最大阈值，取值范围和设备的型号有关，请以设备的实际情况为准。

【使用指导】

该命令必须在配置了**queue af**或**queue wfq**后使用。

配置**queue-length**后，若执行**undo queue af**和**undo queue wfq**命令，则**queue-length**也同时被取消。

【举例】

\# 配置尾部丢弃，队列长度最大为16。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue af bandwidth 200

Sysname-behavior-database queue-length 16

【相关命令】

·**queue****af**

·**queue wfq**

**拥塞管理 \-- 基于类的队列配置命令 \-- wred**

------------------------------------------------------------------------

**[wred**]命令用来配置丢弃方式为加权随机早期检测。

**[undo** **wred**]命令用来取消该配置。

【命令】

**[wred**[ [ **dscp** \| **ip-precedence** ]]]

**[undo wred**]

【缺省情况】

没有配置WRED动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dscp**]：表明在为一个包计算丢弃概率时使用的是DSCP值。

**[ip-precedence**]：表明在为一个包计算丢弃概率时使用的是IP优先级值。缺省情况下使用的是**ip-precedence**。

【使用指导】

该命令必须在配置了**queue af**或**queue wfq**后使用。**wred**和**queue-length**这两个命令不能同时有效。取消该配置时将删除WRED相关的其他配置。

【举例】

\# 配置采用加权早期检测方式，丢弃概率以IP优先级计算。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue wfq

Sysname-behavior-database wred

【相关命令】

·**queue af**

·**queue wfq**

**拥塞管理 \-- 基于类的队列配置命令 \-- wred dscp**

------------------------------------------------------------------------

**[wred dscp**]命令用来设置WRED各DSCP的下限、上限和丢弃概率。

**[undo wred dscp**]命令用来恢复缺省情况。

【命令】

**[wred dscp** *dscp-value* **low-limit** *low-limit* **high-limit** *high-limit* [ **discard-probability** *discard-prob* ]]

**[undo wred dscp ***dscp-value*]

【缺省情况】

下限缺省值为10，上限缺省值为30，丢弃概率缺省值为10。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DSCP值，取值范围为0～63，也可以是关键字，如[表]1-5(?-580725274#_Ref163816081)所示。

**[low-limit ***low-limit*]：WRED下限，单位为报文个数，取值范围为1～1024。

**[high-limit*** high-limit*]：WRED上限，单位为报文个数，取值范围为1～1024。

**[discard-probability*** discard-prob*]：丢弃概率，取值范围为1～255。

【使用指导】

进行本命令配置以前，必须已用**wred dscp**命令使能了基于DSCP的WRED丢弃方式。

取消**wred**配置，**wred dscp**配置同时被取消。

取消**queue af**或**queue wfq**配置，丢弃参数的配置同时被取消。

【举例】

\# 设置DSCP为3的报文的队列下限为20，上限为40，丢弃概率为15。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue wfq

Sysname-behavior-database wred dscp

Sysname-behavior-database wred dscp 3 low-limit 20 high-limit 40 discard-probability 15

【相关命令】

·**queue af**

·**queue wfq**

·**wred**

**拥塞管理 \-- 基于类的队列配置命令 \-- wred ip-precedence**

------------------------------------------------------------------------

**[wred ip-precedence**]命令用来设置WRED各优先级的下限、上限和丢弃概率。

**[undo wred ip-precedence**]命令用来恢复缺省情况。

【命令】

**[wred ip-precedence** *precedence* **low-limit** *low-limit* **high-limit** *high-limit* [ **discard-probability** *discard-prob* ]]

**[undo wred ip-precedence** *precedence*]

【缺省情况】

下限缺省值为10，上限缺省值为30，丢弃概率缺省值为10。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[precedence*]：IP优先级，取值范围为0～7。

**[low-limit*** low-limit*]：WRED下限，单位为报文个数，取值范围为1～1024。

**[high-limit*** high-limit*]：WRED上限，单位为报文个数，取值范围为1～1024。

**[discard-probability*** discard-prob*]：丢弃概率，取值范围为1～255。

【使用指导】

进行本命令配置以前，必须已用**wred**命令使能了基于IP优先级的WRED丢弃方式。

取消**wred**配置，**wred ip-precedence**配置同时被取消。

取消**queue af**或**queue wfq**配置，丢弃参数的配置同时被取消。

【举例】

\# 设置优先级为3的报文的队列下限为20，上限为40，丢弃概率为15。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue wfq

Sysname-behaviro-database wred ip-precedence

Sysname-behavior-database wred ip-precedence 3 low-limit 20 high-limit 40 discard-probability 15

【相关命令】

·**queue af**

·**queue wfq**

·**wred**

**拥塞管理 \-- 基于类的队列配置命令 \-- wred weighting-constant**

------------------------------------------------------------------------

**[wred weighting-constant**]命令用来设置WRED计算平均队列长度的指数。

**[undo wred weighting-constant**]命令用来恢复缺省情况。

【命令】

**[wred weighting-constant** *exponent*]

**[undo wred weighting-constant**]

【缺省情况】

WRED计算平均队列长度的指数为9。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[exponent*]：指数，取值范围为1～16。

【使用指导】

需配置了**queue af**或**queue wfq**，并已用**wred**使能了WRED丢弃方式。

如果取消**wred**配置，**wred weighting-constant**配置同时被取消。

【举例】

\# 配置计算平均队列长度的指数为6。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue af bandwidth 200

Sysname-behavior-database wred ip-precedence

Sysname-behavior-database wred weighting-constant 6

【相关命令】

·**queue af**

·**queue wfq**

·**wred**

**拥塞管理 \-- 报文信息预提取命令 \-- qos pre-classify**

------------------------------------------------------------------------

**[qos pre-classify**]命令用来开启报文信息预提取功能。

**[undo qos pre-classify**]命令用来关闭报文信息预提取功能。

【命令】

**[qos pre-classify**]

**[undo qos** **pre-classify**]

【缺省情况】

报文信息预提取功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在Tunnel接口上使能报文信息预提取功能。

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 qos pre-classify

\

**硬件实现拥塞管理 \-- 严格优先级队列配置命令 \-- display qos queue sp**

------------------------------------------------------------------------

**[display qos queue sp interface**]命令用来显示接口的SP（Strict Priority，严格优先级）队列配置情况。

【命令】

**[display qos queue sp interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的SP队列配置情况。

【举例】

\# 显示GigabitEthernet1/0/1的严格优先级队列配置情况。

\<Sysname\> display qos queue sp interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

 Output queue: Strict Priority queuing

表5-1 display qos queue sp interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

当前出队列类型

**硬件实现拥塞管理 \-- 严格优先级队列配置命令 \-- qos sp**

------------------------------------------------------------------------

**[qos sp**]命令用来在接口上配置严格优先队列。

**[undo qos sp**]命令用来恢复接口上缺省的队列算法。

【命令】

**[qos sp**]

**[undo qos sp**]

【缺省情况】

接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1上应用SP模式的队列调度。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos sp

【相关命令】

·**display qos queue sp interface**

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- display qos queue wrr interface**

------------------------------------------------------------------------

**[display qos queue wrr interface**]命令用来显示接口的WRR（Weighted Round Robin，加权轮询）队列配置情况。

【命令】

**[display qos queue wrr interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的WRR队列配置情况。

【举例】

\# 显示接口GigabitEthernet1/0/1的WRR队列配置情况。

\<Sysname\> display qos queue wrr interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

 Output queue: Weighted Round Robin queuing

 Queue ID        Queue    name      Group           Weight

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 0               be              1               1

 1               af1             1               1

 2               af2             1               1

 3               af3             1               1

 4               af4             1               1

 5               ef              1               1

 6               cs6             1               1

 7               cs7             sp              N/A

表5-2 display qos queue wrr interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

当前出队列类型

Queue ID

队列号

Queue name

队列名字

Group

分组号，说明队列属于哪一个分组，缺省情况下，队列所属的分组号为1

Weight

各个队列的调度权重，当前WRR队列调度权重的计算方式为Weight， N/A表示该队列采用SP调度算法

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- qos wrr**

------------------------------------------------------------------------

**[qos wrr**]命令用于在接口上使能WRR队列，并指明当前WRR队列调度权重的计算方式。

**[undo qos wrr**]命令用于在接口上取消WRR队列，恢复缺省的队列算法。

【命令】

**[qos wrr **[{ **byte-count** \| **weight** }]]

**[undo qos wrr **[{ **byte-count** \| **weight** }]]

【缺省情况】

接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[byte-count**]：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[weight**]：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

必须先使用**qos wrr**命令在接口上使能WRR队列，然后才能进行WRR配置。

【举例】

\# 在接口GigabitEthernet1/0/1上使能WRR队列，并按照权重进行计算。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wrr weight

\# 在接口GigabitEthernet1/1上使能WRR队列，并按照每次轮询可发送的字节数进行计算。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/1

Sysname-GigabitEthernet1/0/1 qos wrr byte-count

【相关命令】

·**display qos queue wrr interface**

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- qos wrr { byte-count \| weight }**

------------------------------------------------------------------------

**[qos wrr **[{ **byte-count** \| **weight** }]]命令用来配置WRR队列或修改WRR队列的参数。

**[undo qos wrr**]命令用来恢复缺省情况。

【命令】

支持WRR分组：

**[qos wrr ***queue-id*[ **group** { **1** \| **2** } { **byte-count** \| **weight** } *schedule-value*]]

**[undo qos wrr ***queue-id*]

不支持WRR分组：

**[qos wrr ***queue-id*[ { **byte-count** \| **weight** } *schedule-value*]]

**[undo qos wrr ***queue-id*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[group**[ { **1** \| **2** }]]：表示该队列属于哪个WRR优先组，缺省为group 1。其中group 1表示该队列属于WRR优先组1，group 2表示该队列属于WRR优先组2。各组之间执行优先级调度，由组1至组2优先级依次降低。支持的组数，根据设备类型的不同可能不同。

**[byte-count**]：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[weight**]：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[schedule-value*]：配置队列的调度权重，取值范围和缺省的调度权重值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

必须先使用**qos wrr**命令在接口上使能WRR队列，然后才能进行本配置。

*[queue-id*]除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

表5-3 *queue-id*数字和关键字对应表

*[queue-id*]数字

*[queue-id*]关键字

0

be

1

af1

2

af2

3

af3

4

af4

5

ef

6

cs6

7

cs7

【举例】

\# 在接口GigabitEthernet1/0/1上应用WRR队列，并按照每次轮询可发送的字节数进行计算，配置队列0的调度权重为100，分组为1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wrr byte-count

Sysname-GigabitEthernet1/0/1 qos wrr 0 group 1 byte-count 100

【相关命令】

·**display qos queue wrr interface**

·**qos wrr**

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- qos wrr group sp**

------------------------------------------------------------------------

**[qos wrr group sp**]命令用来配置队列加入SP组，采用严格优先级调度算法。

**[undo qos wrr group sp**]命令用来恢复缺省情况。

【命令】

**[qos wrr ***queue-id* **group sp**]

**[undo qos wrr ***queue-id*]

【缺省情况】

接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[sp**]：队列加入SP组，采用严格优先级调度算法。

【使用指导】

此命令需要在端口队列为WRR调度模式下使用。

SP组与普通WRR优先组不同，加入SP组的端口队列采用严格优先级调度算法，不再采用加权轮循调度算法。调度时先调度SP组，然后调度其他WRR优先组。

必须先使用**qos wrr**命令在接口上使能WRR队列，然后才能进行本配置。

*[queue-id*]除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

【举例】

\# 在接口GigabitEthernet1/0/1上应用WRR队列，并配置队列0加入SP组进行严格优先级调度。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wrr weight

Sysname-GigabitEthernet1/0/1 qos wrr 0 group sp

【相关命令】

·**display qos queue wrr interface**

·**qos wrr**

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- display qos queue wfq interface**

------------------------------------------------------------------------

**[display qos queue wfq interface**]命令用来显示接口的WFQ配置情况。

【命令】

**[display qos queue wfq interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的WFQ配置情况。

【举例】

\# 显示接口GigabitEthernet1/1的加权公平队列配置情况。

\<Sysname\> display qos queue wfq interface gigabitethernet 1/1

Interface: GigabitEthernet1/0/1

 Output queue: Hardware Weighted Fair Queuing

 Queue ID        Queue name      Group           Byte count      Min Bandwidth

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 0               be              1               1               64

 1               af1             1               1               64

 2               af2             1               1               64

 3               af3             1               1               64

 4               af4             1               1               64

5               ef              1               1               64

 6               cs6             1               1               64

 7               cs7             1               1               64

表5-4 display qos queue wfq interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

当前出队列类型

Queue ID

队列号

Queue name

队列名字

Group

分组号，说明队列属于哪一个分组，缺省情况下，队列所属的分组号为1

Byte-count

队列调度权重值

当前WFQ队列调度权重的计算方式为Byte-count

Min-Bandwidth

队列的最小保证带宽值

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos bandwidth queue**

------------------------------------------------------------------------

**[qos bandwidth queue**]命令用来配置端口队列的最小带宽保证。

**[undo qos bandwidth queue**]命令用来恢复缺省情况。

【命令】

**[qos bandwidth queue ***queue-id*** min ***bandwidth-value*]

**[undo qos bandwidth queue ***queue-id*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[min*** bandwidth-value*]：最小保证带宽值，单位为kbps。端口流量拥塞时能够保证的最小队列带宽。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

必须先使用**qos wfq**命令在接口上使能WFQ队列，然后才能进行本配置。

【举例】

\# 在接口GigabitEthernet1/0/1上配置队列0的最小保证带宽值为100kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq weight

Sysname-GigabitEthernet1/0/1 qos bandwidth queue 0 min 100

【相关命令】

·**qos wfq**

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq**

------------------------------------------------------------------------

**[qos wfq**]命令用来在接口上使能WFQ队列，并指明当前WFQ队列调度权重的计算方式。

**[undo qos wfq**]命令用来在接口上取消WFQ队列，恢复缺省的队列算法。

【命令】

**[qos wfq **[{ **byte-count** \| **weight** }]]

**[undo qos wfq **[{ **byte-count** \| **weight** }]]

【缺省情况】

接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[byte-count**]：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[weight**]：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

必须先使用**qos wfq**命令在接口上使能WFQ队列，然后才能进行WFQ配置。

【举例】

\# 在接口GigabitEthernet1/0/1上使能WFQ队列，并按照权重进行计算。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq weight

\# 在接口GigabitEthernet1/0/1上使能WFQ队列，并按照每次轮询可发送的字节数进行计算。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq byte-count

【相关命令】

·**display qos queue wfq interface**

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq { byte-count \| weight }**

------------------------------------------------------------------------

**[qos wfq **[{ **byte-count** \| **weight** }]]命令用来配置WFQ队列或修改WFQ队列的参数。

**[undo qos wfq**]命令用来恢复缺省情况。

【命令】

支持WFQ分组：

**[qos wfq ***queue-id ***group**[ { **1** \| **2** } { **byte-count** \| **weight** } *schedule-value*]]

**[undo qos wfq ***queue-id*]

不支持WFQ分组：

**[qos wfq ***queue-id*[ { **byte-count** \| **weight** } *schedule-value*]]

**[undo qos wfq ***queue-id*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[group**[ { **1** \| **2** }]]：表示该队列属于哪个WFQ优先组，缺省为group 1。其中group 1表示该队列属于WFQ优先组1，group 2表示该队列属于WFQ优先组2。各组之间执行优先级调度，由组1至组2优先级依次降低。支持的组数，根据设备类型的不同可能不同。

**[byte-count**]：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[weight**]：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[schedule-value*]：配置队列的调度权重，缺省的调度权重值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

必须先使用**qos wfq**命令在接口上使能WFQ队列，然后才能进行本配置。

*[queue-id*]除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

【举例】

\# 在接口GigabitEthernet1/0/1上应用WFQ队列，并按照每次轮询可发送的字节数进行计算，配置队列0的调度权重为100，分组为1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq byte-count

Sysname-GigabitEthernet1/0/1 qos wfq 0 group 1 byte-count 100

【相关命令】

·**display qos queue wfq interface**

·**qos bandwidth queue**

·**qos wfq**

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq group sp**

------------------------------------------------------------------------

**[qos wfq group sp**]命令用来配置队列加入SP组，采用严格优先级调度算法。

**[undo qos wfq group sp**]命令用来恢复缺省情况。

【命令】

**[qos wfq ***queue-id* **group sp**]

**[undo qos wfq ***queue-id*]

【缺省情况】

接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[sp**]：队列加入SP组，采用严格优先级调度算法。

【使用指导】

此命令需要在端口队列为WFQ调度模式下使用。

SP组与普通WFQ优先组不同，加入SP组的端口队列采用严格优先级调度算法，不再采用加权轮循调度算法。调度时先调度SP组，然后调度其他WFQ优先组。

必须先使用**qos wfq**命令在接口上使能WFQ队列，然后才能进行本配置。

*[queue-id*]除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

【举例】

\# 在接口GigabitEthernet1/0/1上应用WFQ队列，并配置队列0加入SP组进行严格优先级调度。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq weight

Sysname-GigabitEthernet1/0/1 qos wfq 0 group sp

【相关命令】

·**display qos queue wfq interface**

·**qos bandwidth queue**

·**qos wfq**

**硬件实现拥塞管理 \-- 最小带宽保证队列配置命令 \-- display qos queue gmb interface**

------------------------------------------------------------------------

**[display qos queue gmb interface**]命令用来显示接口的队列最小带宽配置情况。

【命令】

**[display qos queue gmb interface** \*[interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type* *interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的队列最小带宽配置情况。

【举例】

\# 显示接口GigabitEthernet1/0/1上的队列最小保证带宽配置情况。

\<Sysname\> display qos queue gmb interface gigabitethernet 1/1

Interface: GigabitEthernet1/0/1

 Output queue: Guaranteed Minimum Bandwidth queuing

 Queue ID   Queue name   Min bandwidth

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 0          be           2

 1          af1          3

 2          af2          30

 3          af3          10

 4          af4          10

 5          ef           10

 6          cs6          10

 7          cs7          strict

表5-5 display qos queue gmb interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Output queue

当前出队列类型

Queue ID

队列ID

Queue name

队列名字

Min bandwidth

队列的最小保证带宽值

**硬件实现拥塞管理 \-- 最小带宽保证队列配置命令 \-- qos gmb**

------------------------------------------------------------------------

**[qos gmb**]命令用来使能接口的GMB调度模式。

**[undo** **qos gmb**]命令用来取消接口的GMB调度模式。

【命令】

**[qos gmb **]

**[undo qos gmb**]

【缺省情况】

没有配置GMB模式。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

必须先使用**qos gmb**命令在接口上使能GMB模式，才能进行队列的最小带宽保证配置。

【举例】

\# 在接口GigabitEthernet1/0/1上使能GMB。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos gmb

**硬件实现拥塞管理 \-- 最小带宽保证队列配置命令 \-- qos gmb min-bandwidth**

------------------------------------------------------------------------

**[qos gmb min-bandwidth**]命令用来配置指定队列的最小带宽保证。

**[undo** **qos gmb** ]命令用来恢复缺省配置。

【命令】

**[qos gmb**[ *queue-id* **min-bandwidth** { **percent** *percent* \| **strict** }]]

**[undo qos gmb ***queue-id*]

【缺省情况】

没有配置队列最小带宽保证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[percent** *percent*]：以百分比的形式为指定队列配置最小保证带宽。

**[strict**]：表示不指定具体的带宽，此队列占用自己所需要的带宽，剩余带宽由其他队列分配。

【使用指导】

必须先使用**qos gmb**命令在接口上使能GMB模式，然后才能进行本配置。

任意队列都可以配置成strict，但一个接口只能有一个队列为strict。*queue-id*除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

【举例】

\# 在接口GigabitEthernet1/0/1上为队列0设置10%的最小保证带宽。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos gmb

Sysname-GigabitEthernet1/0/1 qos gmb 0 min-bandwidth percent 10

\# 在接口GigabitEthernet1/0/1上为队列1设置strict模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos gmb

 Sysname-GigabitEthernet1/0/1 qos gmb 1 min-bandwidth strict

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- bandwidth queue**

------------------------------------------------------------------------

![说明](QoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bandwidth queue**]命令用来配置队列调度策略下队列的最小带宽保证。

**[undo bandwidth queue**]命令用来恢复缺省情况。

【命令】

**[bandwidth queue ***queue-id*** min ***bandwidth-value*]

**[undo bandwidth queue ***queue-id*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

队列调度策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[min*** bandwidth-value*]：最小保证带宽值，单位为kbps。端口流量拥塞时能够保证的最小队列带宽。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置队列1的最小保证带宽为128kbps。

\<Sysname\> system-view

Sysname qos qmprofile myprofile

Sysname-qmprofile-myprofile bandwidth queue 1 min 128

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- display qos qmprofile configuration**

------------------------------------------------------------------------

**[display qos qmprofile configuration**]命令用来显示队列调度策略的配置情况。

【命令】

集中式设备：

**[display qos qmprofile ** **four-queue** ] **configuration**  *profile-name*

分布式设备－独立运行模式/集中式IRF设备：

**[display qos qmprofile ** **four-queue** ] **configuration**  *profile-name*  [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display qos qmprofile ** **four-queue** ] **configuration**  *profile-name*  [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[four-queue**]：显示四队列调度策略的配置情况，若未指定该参数，则显示八队列调度策略的配置情况。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[profile-name*]：队列调度策略名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示所有队列调度策略的配置情况。

**[slot*** slot-number*]：显示指定单板的队列调度策略的配置情况。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的队列调度策略的配置情况。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的队列调度策略的配置情况。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备的队列调度策略的配置情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的队列调度策略的配置情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的队列调度策略的配置情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的队列调度策略的配置情况。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的队列调度策略的配置情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的队列调度策略的配置情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的队列调度策略的配置情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定CPU号。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示队列调度策略myprofile的配置情况。

\<Sysname\> display qos qmprofile configuration myprofile

Queue management profile: myprofile (ID 1)

 Queue ID    Type    Group    Schedule  Schedule  Min           Max         Service

                              unit      value     bandwidth     bandwidth   type

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 be          SP      N/A      N/A        N/A      64            10000       STB

 af1         WFQ     1        byte-countN/A      100           10000       STB

af2         WRR     1        weight     100      100           10000       VoIP

 af3         WRR     1        weight     100      100           10000       HSI

 af4         WRR     1        weight     50       100           10000       HSI

ef          WRR     1        weight     50       100           10000       STB

 cs6         WRR     1        weight     100      100           10000       STB

 cs7         WRR     1        weight     50       100           10000       HSI

\# 显示所有四队列调度策略的配置情况。

\<Sysname\> display qos qmprofile four-queue configuration

Queue management profile: b (ID 1) four-queue

 Queue ID  Type  Group  Schedule   Schedule  Min           Max          Service

                        unit       value     bandwidth     bandwidth    type

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 be        SP    N/A    N/A        N/A       64            64           HSI

 af1       SP    N/A    N/A        N/A       64            64           HSI

 af2       SP    N/A    N/A        N/A       64            64           HSI

 ef        WRR   2      byte-count 64        100           1000         VoIP

表5-6 display qos qmprofile configuration命令显示信息描述表

字段

描述

Queue management profile

队列调度策略名称

Queue ID

队列号

Type

队列调度类型，包括SP（严格优先级）、WRR（加权轮询调度）、WFQ（加权公平队列）

对队列调度类型的支持情况与设备的型号有关，请以设备的实际情况为准

Group

优先组，N/A表示无效

Schedule unit

队列调度单位，包括weight和byte-count，N/A表示无效

Schedule vlaue

·队列调度单位为weight时，表示权重值

·队列调度单位为byte-count时，表示字节个数

·N/A表示无效

Min Bandwidth

最小保证带宽

Max bandwidth

最大带宽值

Service type

服务类型，包括HSI、STB、VoIP

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- display qos qmprofile interface**

------------------------------------------------------------------------

**[display qos qmprofile interface**]命令用来显示接口的队列调度策略的配置情况。

【命令】

**[display qos qmprofile interface ** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的队列调度策略的配置情况。

【举例】

\# 显示指定接口的队列调度策略的配置情况。

\<Sysname\> display qos qmprofile interface gigabitethernet 1/0/1

Interface: GigabitEthernet1/0/1

 Queue management profile: myprofile

表5-7 display qos qmprofile interface命令显示信息描述表

字段

描述

Interface

接口名称

Queue management profile

队列调度策略名称

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- qos apply qmprofile(interface view)**

------------------------------------------------------------------------

**[qos apply qmprofile**]命令用来在接口上应用队列调度策略。

**[undo qos apply qmprofile**]命令用来恢复缺省情况。

【命令】

**[qos apply qmprofile ***profile-name*]

**[undo qos apply qmprofile**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：队列调度策略名称，为1～31个字符的字符串，区分大小写。

【使用指导】

每个接口只能应用一个队列调度策略。

【举例】

\# 在接口上应用队列调度策略myprofile。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos apply qmprofile myprofile

【相关命令】

·**display qos qmprofile interface**

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- qos apply qmprofile(session-group-profile view)**

------------------------------------------------------------------------

**[qos apply qmprofile**]命令用来在Session Group Profile上应用队列调度策略。

**[undo qos apply qmprofile**]命令用来恢复缺省情况。

【命令】

**[qos apply qmprofile ** **four-queue** ] *profile-name*

**[undo qos apply qmprofile**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

Session Group Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[four-queue**]：表示在Session Group Profile上应用四队列调度策略。

*[profile-name*]：队列调度策略名称，为1～31个字符的字符串，区分大小写。

【使用指导】

·每个Session Group Profile只能应用一个队列调度策略。

·Session Group Profile上可以应用四队列或八队列的队列调度策略。

【举例】

\# 在Session Group Profile上应用四队列调度策略myprofile。

\<Sysname\> system-view

Sysname user-profile a123 type session-group

Sysname-session-group-profile-a123 qos apply qmprofile four-queue myprofile

\# 在Session Group Profile上应用八队列调度策略myprofile。

\<Sysname\> system-view

Sysname user-profile a123 type session-group

Sysname-session-group-profile-a123 qos apply  qmprofile myprofile

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- qos qmprofile**

------------------------------------------------------------------------

**[qos qmprofile**]命令用来创建用户自定义的队列调度策略，并进入相应的队列调度策略视图。

**[undo qos qmprofile**]命令用来删除用户自定义的队列调度策略。

【命令】

**[qos qmprofile ***profile-name * **type four-queue** ]

**[undo qos qmprofile ***profile-name*]

【缺省情况】

不存在用户自定义的队列调度策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：队列调度策略名称，为1～31个字符的字符串，区分大小写。

**[type four-queue**]：指定创建的队列调度策略类型为四队列调度策略。

【使用指导】

不能删除已经应用到接口的队列调度策略，必须先在应用的接口上取消对该队列调度策略的应用，然后再删除该队列调度策略。

不能删除已经应用到Session Group Profile的队列调度策略，必须先在应用的Session Group Profile上取消对该队列调度策略的应用，然后再删除该队列调度策略。

【举例】

\# 创建自定义的队列调度策略myprofile，并进入队列调度策略视图。

\<Sysname\> system-view

Sysname qos qmprofile myprofile

Sysname-qmprofile-myprofile

\# 创建自定义的四队列调度策略myprofile，并进入四队列调度策略视图。

\<Sysname\> system-view

Sysname qos qmprofile myprofile type four-queue

Sysname-qmprofile-four-queue-myprofile

【相关命令】

·**display qos qmprofile interface**

·**queue**

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- queue**

------------------------------------------------------------------------

**[queue**]命令用来配置队列调度参数。

**[undo queue**]命令用来恢复缺省情况。

【命令】

**[queue ***queue-id*****[ [ **group** *group-id*  { **weight \| byte-count** } *schedule-value* \| **wrr** **group** *group-id* { **weight \| byte-count** } *schedule-value* } [ **max-bandwidth** *bandwidth-value* \| **service-type** *service-type-value* ] \*]]

**[undo queue ***queue-id*]

【缺省情况】]

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

队列调度策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[sp**]：配置队列为严格优先级调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[wfq**]：配置队列为加权公平调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[wrr**]：配置队列为加权轮询调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[group*** group-id*]：优先组号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[byte-count**]：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[weight**]：表示按照权重新进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[schedule-value*]：配置队列的调度权重。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[max-bandwidth** *bandwidth-value*]：最大限制带宽，单位为kbps。

**[service-type ***service-type-value*]：服务类型。包括HSI（High Speed Internet，高速上网）、STB（Set Top Box，机顶盒）、VoIP（Voice Over Internet Protocol，在IP网络上传送语音）。

【使用指导】

*[queue-id*]除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

【举例】

\# 创建自定义的队列调度策略myprofile，并配置队列0为严格优先级调度。

\<Sysname\> system-view

Sysname qos qmprofile myprofile

Sysname-qmprofile-myprofile queue 0 sp

\# 创建自定义的队列调度策略myprofile，并配置队列1为加权轮询调度，权重为100，分组为1。

\<Sysname\> system-view

Sysname qos qmprofile myprofile

Sysname-qmprofile-myprofile queue 1 wrr group 1 weight 100

【相关命令】

·**display qos qmprofile interface**

·**qos qmprofile**

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- queue(four-queue qmprofile view)**

------------------------------------------------------------------------

**[queue**]命令用来配置队列调度参数。

**[undo queue**]命令用来恢复缺省情况。

【命令】

**[queue**[ *queue-id* { **sp** \| **wrr** **group** *group-id* { **weight** \| **byte-count** } *schedule-value* } [ **min-bandwidth** *bandwidth-value* \| **max-bandwidth** *bandwidth-value* \| **service-type** *service-type-value* ] \*]]

**[undo queue ***queue-id*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

四队列调度策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[sp**]：配置队列为严格优先级调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[wrr**]：配置队列为加权轮询调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[group*** group-id*]：WRR优先组号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[weight**]：表示按照权重新进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[byte-count**]：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[schedule-value*]：配置队列的调度权重。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[min bandwidth*** bandwidth-value*]：最小保证带宽值，单位为kbps。端口流量拥塞时能够保证的最小队列带宽。

**[max bandwidth ***bandwidth-value*]：最大限制带宽，单位为kbps。

**[service-type*** service-type-value*]：服务类型。包括HSI（High Speed Internet，高速上网）、STB（SetTop Box，机顶盒）、VoIP（Voice Over Internet Protocol，在IP网络上传送语音）。

【使用指导】

对同一个队列多次配置时，后一次配置会覆盖前面的配置，以最后一次配置为准。

*[queue-id*]除了支持数字外，还支持直接输入关键字，具体情况请参见[表]5-3(?1813098140#_Ref293562576)。

【举例】

\# 创建自定义的四队列调度策略myprofile，并配置队列0为严格优先级调度，最小带宽为40，服务类型为HSI。

\<Sysname\> system-view

Sysname qos qmprofile myprofile type four-queue

Sysname-qmprofile-four-queue-myprofile queue 0 sp min bandwidth 40 service-type hsi

\# 创建自定义的四队列调度策略myprofile，并配置队列1为加权轮询调度，权重为63，分组为1, 最小保证带宽为40，服务类型为HSI。

\<Sysname\> system-view

Sysname qos qmprofile myprofile type four-queue

Sysname-qmprofile-four-queue-myprofile queue 1 wrr group 1 weight 63 min bandwidth 40 service-type hsi

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- queue af**

------------------------------------------------------------------------

**[queue af**]命令用来配置类进行确保转发（Assured-forwarding），并配置类可确保的最小带宽。

**[undo queue af**]命令用来取消配置。

【命令】

**[queue af bandwidth** *bandwidth* [ **pir** *peak-information-rate* ]]

**[undo queue af**]

【缺省情况】

没有配置类进行确保转发。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：可确保的最小带宽，单位kbps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率，单位为kbps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

当在策略下将类与**queue af**所属行为关联时，必须满足：同一个策略下为确保转发（**queue af**）和加速转发（**queue ef**）的类指定的带宽之和必须不大于该策略所应用接口的可用带宽。

【举例】

\# 为行为database配置确保转发，并且确保最小带宽为200kbps。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue af bandwidth 200

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- queue ef**

------------------------------------------------------------------------

**[queue ef**]命令用来配置类进行加速转发（Expedited-forwarding），报文进入绝对优先级队列，并配置最大带宽。

**[undo queue ef**]命令用来取消配置。

【命令】

**[queue ef bandwidth** *bandwidth* [ **cbs** *burst*   **pir** *peak-information-rate* ]]

**[undo queue ef**]

【缺省情况】

没有配置类进行加速转发。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：带宽，单位kbps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[cbs** *burst*]：指定承诺突发尺寸，单位为字节。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率，单位为kbps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

**[queue ef**]命令用来配置加速转发（Expedited-forwarding），报文进入绝对优先级队列，并配置最大带宽。**undo queue ef**命令用来取消配置。

本命令的注意事项如下。

·该命令在流行为视图下不能与**queue af**同时使用。

·同一个策略下为确保转发（**queue af**）和加速转发（**queue ef**）的类指定的带宽之和必须不大于该策略所应用接口的可用带宽。

·对于设置绝对值形式**queue ef bandwidth** *bandwidth* [ **cbs** *burst* ]，CBS = *burst*，若不指定*burst*，则CBS = *bandwidth*×25。

【举例】

\# 配置报文进入优先级队列，最大带宽为200kbps，*burst*为5000bytes。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue ef bandwidth 200 cbs 5000

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- queue wfq**

------------------------------------------------------------------------

**[queue wfq**]命令用来为缺省类配置采用公平队列。

**[undo queue wfq**]命令用来取消配置。

【命令】

**[queue wfq**]

**[undo queue wfq**]

【缺省情况】

没有为缺省类配置采用公平队列。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 为流行为test配置WFQ。

\<Sysname\> system-view

Sysname traffic behavior test

Sysname-behaviro-test queue wfq

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- weight**

------------------------------------------------------------------------

**[weight**]命令用来配置WFQ的权重。

**[undo weight**]命令用来恢复缺省情况。

【命令】

**[weight** weight-value]

**[undo weight**]

【缺省情况】

对于AF和EF，WFQ的权重为1；对于BE，WFQ的权重为0。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[weight-value*]：权重的值。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在AF最小可保证带宽和峰值速率之间的流量采用WFQ调度；在EF最大带宽和峰值速率之间的流量采用WFQ调度。

【举例】

\# 配置流行为database1采用AF，最小可保证带宽为200kbps，峰值速率为500kbps，200～500kbps之间的流量采用WFQ，其权重为100。

\<Sysname\> system-view

Sysname traffic behavior database1

Sysname-behavior-database1 queue af bandwidth 200 pir 500

Sysname-behavior-database1 weight 100

\# 配置流行为database2采用EF，最大带宽为400kbps，峰值速率为800kbps，400～800kbps之间的流量采用WFQ，其权重为200。

\<Sysname\> system-view

Sysname traffic behavior database2

Sysname-behavior-database2 queue ef bandwidth 400 pir 800

Sysname-behavior-database2 weight 200

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- wred**

------------------------------------------------------------------------

**[wred**]命令用来配置丢弃方式为加权随机早期检测。

**[undo** **wred**]命令用来取消该配置。

【命令】

**[wred**[ [ **dscp** \| **ip-precedence** ]]]

**[undo wred**]

【缺省情况】

没有配置WRED动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dscp**]：表明在为一个包计算丢弃概率时使用的是DSCP值。

**[ip-precedence**]：表明在为一个包计算丢弃概率时使用的是IP优先级值，缺省情况下使用的是ip-precedence。

【使用指导】

该命令必须在配置了**queue af**或**queue wfq**后使用。当接口上应用了配置WRED的策略后，原有的接口级的WRED配置失效。

【举例】

\# 配置采用加权早期检测方式，丢弃概率以IP优先级计算。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database queue wfq

Sysname-behavior-database wred

**硬件实现拥塞管理 \-- 低时延队列调度模式配置命令 \-- queue low-latency enable**

------------------------------------------------------------------------

**[queue low-latency enable**]命令用来开启低时延队列调度模式。

**[undo queue low-latency enable**]命令用来关闭低时延队列调度模式。

【命令】

**[queue low-latency enable**]

**[undo queue low-latency enable**]

【缺省情况】

低时延队列调度模式处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在对转发时延性能要求较高的场景下，可开启低时延队列调度模式，使得系统获得更高的转发时延性能。

支持MDC的设备，本命令只有缺省MDC支持。MDC的相关内容请参见"基本配置指导"中的"MDC"。

【举例】

\# 开启低时延队列调度模式。

\<Sysname\> system-view

Sysname queue low-latency enable

****

\

**拥塞避免 \-- WRED配置命令 \-- display qos wred interface**

------------------------------------------------------------------------

**[display qos wred interface**]命令用来显示指定接口、指定PVC或所有接口及PVC的WRED配置情况和统计信息。

【命令】

**[display qos wred interface**[ [ *interface-type interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的WRED配置情况和统计信息。

**[pvc****[{ *pvc-name* \| *vpi/vci* }]]：显示指定ATM接口上的指定PVC的信息，只有当接口为ATM接口时才能指定本参数。*pvc-name*表示PVC名。*vpi/vci*表示VPI/VCI值。如果未指定本参数，将显示指定ATM接口上所有PVC的WRED配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有接口的WRED配置情况和统计信息。

\<Sysname\> display qos wred interface

Interface: GigabitEthernet1/0/4

 Current WRED configuration:

 Exponent: 9 (1/512)

 Pre  Low   High  Dis-prob Random-discard  Tail-discard

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0    10    30    10       0               0

1    10    30    10       0               0

2    10    30    10       0               0

3    10    30    10       0               0

4    10    30    10       0               0

5    10    30    10       0               0

6    10    30    10       0               0

7    10    30    10       0               0

Interface: GigabitEthernet1/0/3

 Current WRED configuration:

 Applied WRED table name: q1

表1-5 display qos wred interface命令显示信息描述表

字段

描述

Interface

接口名，由接口类型和接口编号组成

Exponent

计算平均队列长度的指数

Pre

报文的IP优先级

Low

队列下限

High

队列上限

Dis-prob

计算丢弃概率时的分母

Random-discard

随机丢弃的报文的数目

Tail-discard

尾丢弃报文的数目

Current WRED configuration

当前WRED的配置情况

Applied WRED table name

当前应用的WRED表的名称

**拥塞避免 \-- WRED配置命令 \-- qos wred enable**

------------------------------------------------------------------------

**[qos wred enable**]命令用来在接口或PVC上使能WRED。

**[undo qos wred enable**]命令用来恢复缺省的队列丢弃方法。

【命令】

**[qos wred **[[ **dscp** \| **ip-precedence** ] **enable**]]

**[undo qos wred **[[ **dscp** \| **ip-precedence** ] **enable**]]

【缺省情况】

队列丢弃方法为尾丢弃。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dscp**]：表明计算丢弃概率时使用的是DSCP值。

**[ip-precedence**]：表明计算丢弃概率时使用的是IP优先级值。缺省情况下使用的是**ip-precedence**。

【使用指导】

有的产品本命令在可直接配置；有的产品必须先在接口上配置**qos wfq**命令，才能配置本命令。具体情况和设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在GigabitEthernet1/0/1接口上使能WRED，丢弃概率以IP优先级计算。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq queue-length 100 queue-number 512

Sysname-GigabitEthernet1/0/1 qos wred ip-precedence enable

【相关命令】

·**display qos wred interface**

·**qos wred enable**

**拥塞避免 \-- WRED配置命令 \-- qos wred dscp**

------------------------------------------------------------------------

**[qos wred dscp**]命令用来设置各DSCP优先级的下限、上限和丢弃概率。

**[undo qos wred dscp**]命令用来恢复缺省情况。

【命令】

**[qos wred dscp** *dscp-value* **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]

**[undo qos wred dscp** *dscp-value*]

【缺省情况】

下限缺省值为10，上限缺省值为30，丢弃概率缺省值为10。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DSCP值，取值范围为0～63，也可以是关键字，如[表]1-5(?-580725274#_Ref163816081)所示。

**[low-limit ***low-limit*]：WRED下限，单位为报文个数，取值范围为1～1024。

**[high-limit*** high-limit*]：WRED上限，单位为报文个数，取值范围为1～1024。

**[discard-probability*** discard-prob*]：丢弃概率，取值范围为1～255。

【使用指导】

必须先使用**qos wred dscp enable**在接口或PVC上应用基于DSCP的WRED后，才可以进行本配置。阈值限制的是平均队列长度。

【举例】

\# 在接口上设置DSCP优先级为63的报文的队列下限为20，上限为40，丢弃概率为15。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq queue-length 100 queue-number 512

Sysname-GigabitEthernet1/0/1 qos wred dscp enable

Sysname-GigabitEthernet1/0/1 qos wred dscp 63 low-limit 20 high-limit 40 discard-probability 15

【相关命令】

·**display qos wred interface**

·**qos wred enable**

**拥塞避免 \-- WRED配置命令 \-- qos wred ip-precedence**

------------------------------------------------------------------------

**[qos wred ip-precedence**]命令用来设置IP优先级的下限、上限和丢弃概率。

**[undo qos wred ip-precedence**]命令用来恢复缺省情况。

【命令】

**[qos wred ip-precedence** *ip-precedence* **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]

**[undo qos wred ip-precedence** *ip-precedence*]

【缺省情况】

下限缺省值为10，上限缺省值为30，丢弃概率缺省值为10。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-precedence*** ip-precedence*]：IP优先级，取值范围为0～7。

**[low-limit*** low-limit*]：WRED下限，单位为报文个数，取值范围为1～1024。

**[high-limit*** high-limit*]：WRED上限，单位为报文个数，取值范围为1～1024。

**[discard-probability*** discard-prob*]：丢弃概率，取值范围为1～255。

【使用指导】

必须先使用**qos wred enable**在接口或PVC上应用基于IP优先级的WRED后，才可以进行本配置。阈值限制的是平均队列长度。

【举例】

\# 在接口上设置IP优先级为3的报文的队列下限为20，上限为40，丢弃概率为15。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq queue-length 100 queue-number 512

Sysname-GigabitEthernet1/0/1 qos wred ip-precedence enable

Sysname-GigabitEthernet1/0/1 qos wred ip-precedence 3 low-limit 20 high-limit 40 discard-probability 15

【相关命令】

·**display qos wred interface**

·**qos wred enable**

**拥塞避免 \-- WRED配置命令 \-- qos wred weighting-constant**

------------------------------------------------------------------------

**[qos wred weighting-constant**]命令用来设置WRED计算平均队列长度的指数。

**[undo qos wred weighting-constant**]命令用来恢复缺省情况。

【命令】

**[qos wred weighting-constant** *exponent*]

**[undo qos wred weighting-constant**]

【缺省情况】

WRED计算平均队列长度的指数为9。

【视图】

接口视图/PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[weighting-constant*** exponent*]：计算平均队列长度的指数，取值范围为1～16。

【使用指导】

必须先使用**qos wred enable**在接口或PVC上应用WRED后，才可以配置WRED的参数。

【举例】

\# 在GigabitEthernet1/0/1接口上配置计算平均队列长度的指数为6。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wfq queue-length 100 queue-number 512

Sysname-GigabitEthernet1/0/1 qos wred enable

Sysname-GigabitEthernet1/0/1 qos wred weighting-constant 6

【相关命令】

·**display qos wred interface**

·**qos wred enable**

**拥塞避免 \-- WRED表配置命令 \-- display qos wred table**

------------------------------------------------------------------------

**[display qos wred table**]命令用来显示WRED表的配置情况。

【命令】

集中式设备：

**[display qos wred table** [ **name** *table-name* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qos wred table** [ **name** *table-name*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display qos wred table** [ **name** *table-name*   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** table-name*]：WRED表的名字。如果未指定本参数，则显示所有WRED表配置情况。

**[slot*** slot-number*]：显示指定单板的WRED表配置情况。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的WRED表配置情况。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的WRED表配置情况。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备的WRED表配置情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的WRED表配置情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的WRED表配置情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的WRED表配置情况。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的WRED表配置情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的WRED表配置情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的WRED表配置情况。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示WRED表1的配置情况，表1是一个已经配置好的WRED参数表。

\<Sysname\> display qos wred table name 1

Table name: 1

Table type: Queue based WRED

QID   gmin  gmax  gprob  ymin  ymax  yprob  rmin  rmax  rprob  exponent  ECN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0     100   1000  10     100   1000  10     100   1000  10     9         N

1     100   1000  10     100   1000  10     100   1000  10     9         N

2     100   1000  10     100   1000  10     100   1000  10     9         N

3     100   1000  10     100   1000  10     100   1000  10     9         N

4     100   1000  10     100   1000  10     100   1000  10     9         N

5     100   1000  10     100   1000  10     100   1000  10     9         N

6     100   1000  10     100   1000  10     100   1000  10     9         N

7     100   1000  10     100   1000  10     100   1000  10     9         N

表6-1 display qos wred table命令显示信息描述表

字段

描述

Table name

WRED表名

Table type

WRED表类型

QID

队列ID

gmin

绿色报文的队列下限

gmax

绿色报文的队列上限

gprob

绿色报文的丢弃概率

ymin

黄色报文的队列下限

ymax

黄色报文的队列上限

yprob

黄色报文的丢弃概率

rmin

红色报文的队列下限

rmax

红色报文的队列上限

rprob

红色报文的丢弃概率

exponent

计算平均队列长度指数

ECN

是否对该队列开启了拥塞通知功能，Y表示开启，N表示未开启

**拥塞避免 \-- WRED表配置命令 \-- qos wred apply**

------------------------------------------------------------------------

**[qos wred apply**]命令用来在接口上应用WRED全局表。

**[undo qos wred apply**]命令用来恢复接口缺省的尾丢弃模式，它同时取消WRED表的应用。

【命令】

**[qos wred apply** [ *table-name* ]]

**[undo qos wred apply**]

【缺省情况】

接口没有应用WRED全局表，即接口采用尾丢弃。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[table-name*]：WRED表的名称。

【使用指导】

如果不指定WRED表的名称，则在接口上应用缺省WRED表。

【举例】

\# 在接口GigabitEthernet1/0/1上应用WRED表。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos wred apply table1

【相关命令】

·**display qos wred interface**

·**display qos wred table**

·**qos wred table**

**拥塞避免 \-- WRED表配置命令 \-- qos wred table**

------------------------------------------------------------------------

**[qos wred table**]命令用来创建全局WRED表，同时进入该WRED表视图。

**[undo qos wred table**]命令用来删除全局WRED表。

【命令】

**[qos wred** **queue** **table** *table-name*]

**[undo qos wred queue table** *table-name*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[queue**]：基于队列的表，拥塞时根据报文所在队列进行随机丢弃。

**[table ***table-name*]：指定表的名称。

【使用指导】

·设备不允许删除正在使用的表。如果想删除正在使用的表，请先在接口上取消应用的WRED表。

·缺省WRED表可以通过**display qos wred table**命令显示，不允许修改和删除。

【举例】

\# 创建基于queue的WRED表queue-table1。

\<Sysname\> system-view

Sysname qos wred queue table queue-table1

Sysname-wred-table-queue-table1

【相关命令】

·**display qos wred table**

**拥塞避免 \-- WRED表配置命令 \-- queue**

------------------------------------------------------------------------

**[queue**]命令用来配置基于队列的WRED表的内容。

**[undo queue**]命令用来恢复缺省情况。

【命令】

**[queue** *queue-id* [ **drop-level** *drop-level*  **low-limit** *low-limit* **high-limit** *high-limit*  **discard-probability** *discard-prob* ]]

**[undo queue **[{ *queue-id* \| **all** }]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

WRED表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列编号。

**[drop-level ***drop-level*]：丢弃级别，在进行报文丢弃时参考的参数，0对应绿色报文、1对应黄色报文、2对应红色报文。如果未指定本参数，后续配置的参数对该队列所有丢弃级别的报文都生效。

**[low-limit*** low-limit*]：队列平均长度的下限。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

**[high-limit*** high-limit*]：队列平均长度的上限。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[discard-probability*** discard-prob*]：丢弃概率的分母，取值越大，计算出的丢弃概率越小。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

当队列平均长度小于下限时，不丢弃报文。当队列平均长度在上限和下限之间时，设备随机丢弃报文，队列越长，丢弃概率越高。当队列平均长度超过上限时，丢弃所有到来的报文。

【举例】

\# 配置基于队列的WRED表queue-table1中队列1的丢弃参数：丢弃级别为1，队列平均长度的下限为10，队列平均长度的上限为20，丢弃概率的分母为30%。

\<Sysname\> system-view

Sysname qos wred queue table queue-table1

Sysname-wred-table-queue-table1 queue 1 drop-level 1 low-limit 10 high-limit 20 discard-probability 30

【相关命令】

·**display qos wred table**

·**qos wred table**

**拥塞避免 \-- WRED表配置命令 \-- queue ecn**

------------------------------------------------------------------------

**[queue ecn**]命令用来对指定队列开启拥塞通知功能。

**[undo queue ecn**]命令用来恢复缺省情况。

【命令】

**[queue** *queue-id* **ecn**]

**[undo queue ***queue-id ***ecn**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

WRED表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列编号，取值范围为0～7。

【使用指导】

在报文的发送端和接收端都支持ECN功能时，设备可以通过对ECN域的识别和标记将拥塞状况告知终端，避免拥塞加剧。

【举例】

\# 在WRED表queue-table1中，对队列1开启拥塞通知功能。

\<Sysname\> system-view

Sysname qos wred queue table queue-table1

Sysname-wred-table-queue-table1 queue 1 ecn

【相关命令】

·**display qos wred table**

·**qos wred table**

**拥塞避免 \-- WRED表配置命令 \-- queue weighting-constant**

------------------------------------------------------------------------

**[queue weighting-constant**]命令用来配置计算平均队列长度的指数。

**[undo queue weighting-constant**]命令用来恢复缺省情况。

【命令】

**[queue** *queue-id* **weighting-constant** *exponent* ]

**[undo queue ***queue-id ***weighting-constant**]

【缺省情况】

计算平均队列长度的指数为9。

【视图】

WRED表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[queue-id*]：队列编号。

**[weighting-constant*** exponent*]：计算平均队列长度的指数，*exponent*的取值范围和设备的型号有关，请以设备的实际情况为准。

【使用指导】

平均队列长度的指数越大，计算平均队列长度时对队列的实时变化越不敏感。计算队列平均长度的公式为：平均队列长度=（以前的平均队列长度×（1-1/[2^n^]））＋（当前队列长度×（1/[2^n^]））。其中n表示指数。

【举例】

\# 在WRED表queue-table1中，配置计算平均队列长度的指数为12。

\<Sysname\> system-view

Sysname qos wred queue table queue-table1

Sysname-wred-table-queue-table1 queue 1 weighting-constant 12

【相关命令】

·**display qos wred table**

·**qos wred table**

\

**全局CAR \-- 全局CAR配置命令 \-- car name**

------------------------------------------------------------------------

**[car** **name**]命令用来配置全局CAR动作。

**[undo car**]用来删除全局CAR动作。

【命令】

**[car**]**name ***car-name *[[ **hierarchy-car** *hierarchy-car-name* [ **mode** { **and** \| **or** } ] ]]

**[undo car**]

【缺省情况】

没有配置全局CAR动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[car-name*]：聚合CAR的名称，首字符需要以字母开头，为1～31个字符的字符串，区分大小写。

*[hierarchy-car-name*]：分层CAR的名称，首字符需要以字母开头，为1～31个字符的字符串，区分大小写。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[mode**]：分层CAR和聚合CAR动作的合作模式。有**and**和**or**两种模式，默认为**and**模式。

·**and**：在该模式下，对于多条数据流应用同一个分层CAR，必须每条流满足各自的聚合CAR配置，同时各流量之和又满足分层CAR的配置，流量才能正常通过。

·**or**：在该模式下，对于多条数据流应用同一个分层CAR，只要每条流满足各自的聚合CAR配置或者各流量之和满足分层CAR配置，流量即可正常通过。

【举例】

\# 配置流行为be1的聚合CAR动作为aggcar-1。

\<Sysname\> system-view

Sysname traffic behavior be1

Sysname-behavior-be1 car name aggcar-1

\# 配置流行为be1的聚合CAR动作为aggcar-1，分层CAR动作为hcar，合作模式为or。

\<Sysname\> system-view

Sysname traffic behavior be1

Sysname-behavior-be1 car name aggcar-1 hierarchy-car hcar mode or

【相关命令】

·**display qos car name**

·**display traffic behavior user-defined**

**全局CAR \-- 全局CAR配置命令 \-- display qos car name**

------------------------------------------------------------------------

**[display qos car name**]命令用来显示全局CAR的配置和统计信息。

【命令】

**[display qos car name** [ *car-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[car-name*]：全局CAR的名称，首字符需要以字母开头，为1～31个字符的字符串，区分大小写。显示指定全局CAR的配置和统计信息。如果未指定本参数，将显示所有全局CAR的配置和统计信息，包含聚合CAR和分层CAR。

【举例】

\# 显示全局CAR的配置和统计信息。（集中式设备）

\<Sysname\> display qos car name

 Name: a

  Mode: aggregative

   CIR 33 (kbps) CBS: 2062 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

  Slot 0:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

 Name: b

  Mode: hierarchy

   CIR 55 (kbps) CBS: 3437 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

  Slot 0:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

\# 显示全局CAR的配置和统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display qos car name

 Name: a

  Mode: aggregative

   CIR 33 (kbps) CBS: 2062 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

  Slot 0:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

  Slot 1:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

  Slot 2:

   Apply failed

 Name: b

  Mode: hierarchy

   CIR 55 (kbps) CBS: 3437 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

  Slot 0:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

  Slot 1:

   Apply failed

  Slot 2:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

\# 显示全局CAR的配置和统计信息。（分布式设备－IRF模式）

\<Sysname\> display qos car name

 Name: a

  Mode: aggregative

   CIR 33 (kbps) CBS: 2062 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

  Chassis 1 Slot 0:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

  Chassis 2 Slot 1:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

  Chassis 2 Slot 2:

   Apply failed

 Name: b

  Mode: hierarchy

   CIR 55 (kbps) CBS: 3437 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)

   Green action  : pass

   Yellow action : pass

   Red action    : discard

  Chassis 1 Slot 0:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

  Chassis 2 Slot 1:

   Apply failed

  Chassis 2 Slot 2:

   Green packets : 0 (Packets), 0 (Bytes)

   Yellow packets: 0 (Packets), 0 (Bytes)

   Red packets   : 0 (Packets), 0 (Bytes)

表7-1 display qos car name命令显示信息描述表

字段

描述

Name

全局CAR的名称

Mode

全局CAR的类型

·aggregative：聚合CAR

·hierarchy：分层CAR

CIR  CBS  PIR  EBS

流量监管流量的参数配置

Green action

对绿色报文的动作

·discard：丢弃报文

·pass：允许报文通过

Yellow action

对黄色报文的动作

·discard：丢弃报文

·pass：允许报文通过

Red action

对红色报文的动作

·discard：丢弃报文

·pass：允许报文通过

Green packets

绿色报文的流量统计

Yellow packets

黄色报文的流量统计

Red packets

红色报文的流量统计

**全局CAR \-- 全局CAR配置命令 \-- qos car (interface view)**

------------------------------------------------------------------------

**[qos** **car**]命令用来在接口上应用聚合CAR。

**[undo qos car**]命令用来删除接口上应用的聚合CAR。

【命令】

**[qos car**[ { **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-number* } **name** *car-name*]]

**[undo qos car **[{ **inbound** \| **outbound** } { **any** \| **acl** [ **ipv6** ] *acl-number* }]]

【缺省情况】

没有在接口上应用聚合CAR。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对接口接收到的数据包应用聚合CAR。

**[outbound**]：对接口发送的数据包应用聚合CAR。

**[any**]：对所有的IP数据包应用聚合CAR。

**[acl ***acl-number*]：对匹配IPv4 ACL的数据包应用聚合CAR。*acl-number*为IPv4 ACL编号，取值范围为2000～5999。

**[acl ipv6 ***acl-number*]：对匹配IPv6 ACL的数据包应用聚合CAR。*acl-number*为IPv6 ACL编号，取值范围为2000～3999。

**[name*** car-name*]：聚合CAR的名称，首字符需要以字母开头，为1～31个字符的字符串，区分大小写。

【使用指导】

用户可以在接口上重复执行本命令，从而在接口上应用多个聚合CAR，各个聚合CAR的执行顺序与配置顺序一致。

【举例】

\# 在GigabitEthernet1/0/1的入方向上对满足ACL规则2000的报文应用聚合CAR策略aggcar-1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos car inbound ACL 2000 name aggcar-1

【相关命令】

·**display qos car interface**

**全局CAR \-- 全局CAR配置命令 \-- qos car (system view)**

------------------------------------------------------------------------

**[qos car**]命令用来配置聚合CAR或分层CAR。

**[undo** **qos car**]命令用来取消聚合CAR或分层CAR的配置。

【命令】

**[qos car ***car-name *[{ **aggregative** \| **hierarchy** } **cir** *committed-information-rate* [ **cbs** *committed-burst-size* [ **ebs** *excess-burst-size* ]   **green** *action* \| **red** *action* \| **yellow** *action* ] \*]]

**[qos car ***car-name *[{ **aggregative** \| **hierarchy** } **cir** *committed-information-rate* [ **cbs** *committed-burst-size* ] **pir** *peak-information-rate*  **ebs** *excess-burst-size*  [ **green** *action* \| **red** *action* \| **yellow** *action* ] \*]]

**[undo qos car ***car-name*]

【缺省情况】

没有配置聚合CAR或分层CAR。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[car-name*]：全局CAR的名称，首字符需要以字母开头，为1～31个字符的字符串，区分大小写。

**[aggregative**]：该全局CAR为聚合模式。

**[hierarchy**]：该全局CAR为分层模式。

**[cir ***committed-information-rate*]：承诺信息速率，单位为kbps。取值范围与设备的型号有关，请以设备的实际情况为准。

**[cbs** *committed-burst-size*]：承诺突发尺寸，即实际平均速率在承诺速率以内时的突发流量，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[ebs** *excess-burst-size*]：过度突发尺寸，单位为byte。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[pir** *peak-information-rate*]：峰值速率，单位为kbps。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。

**[green ***action*]：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为**pass**。

**[red ***action*]：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为**discard**。

**[yellow ***action*]：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为**pass**。

*[action*]：对数据包采取的动作，有以下几种：

·**discard**：丢弃数据包。

·**pass**：允许数据包通过。

·**remark-atmclp-continue** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并继续由下一个CAR策略处理，取值范围为0～1。

·**remark-atmclp-pass** *new-atmclp*：设置新的ATM报文的CLP标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-dot1p-continue** *new-cos*：设置新的802.1P报文的优先级值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-dot1p-pass** *new-cos*：设置新的802.1P报文的优先级值，并允许数据包通过，取值范围为0～7。

·**remark-dscp-continue** *new-dscp*：设置报文新的DSCP值，并继续由下一个CAR策略处理，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。

·**remark-dscp-pass** *new-dscp*：设置报文新的DSCP值，并允许数据包通过，取值范围为0～63；用文字表示时，可以选取**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**、**default**、**ef**。

·**remark-frde-continue** *new-frde*：设置新的FR报文的DE标志位的值，并继续由下一个CAR策略处理，取值范围为0～1。

·**remark-frde-pass** *new-frde*：设置新的FR报文的DE标志位的值，并允许数据包通过，取值范围为0～1。

·**remark-mpls-exp-continue** *new-exp*：设置新的MPLS报文的EXP标志位的值，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-mpls-exp-pass** *new-exp*：设置新的MPLS报文的EXP标志位的值，并允许数据包通过，取值范围为0～7。

·**remark-prec-continue** *new-precedence*：设置新的IP优先级，并继续由下一个CAR策略处理，取值范围为0～7。

·**remark-prec-pass** *new-precedence*：设置新的IP优先级，并允许数据包通过，取值范围为0～7。

【使用指导】

·聚合CAR配置需要在接口上应用或在策略中引用后才能生效。

·分层CAR配置需要在策略中引用后才能生效。

·不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。

【举例】

\# 配置聚合CAR采取的CAR参数取值，**cir**取值为200，**cbs**取值为2000，对于红色报文采取丢弃的动作。

\<Sysname\> system-view

Sysname qos car aggcar-1 aggregative cir 200 cbs 2000 red discard

\# 配置分层CAR采取的CAR参数取值，**cir**取值为120，**cbs**取值为4000。

\<Sysname\> system-view

Sysname qos car h-car hierarchy cir 120 cbs 4000

【相关命令】

·**display qos car name**

**全局CAR \-- 全局CAR配置命令 \-- reset qos car name**

------------------------------------------------------------------------

**[reset qos car name**]命令用来清除全局CAR的统计信息。

【命令】

**[reset qos car name** [ *car-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[car-name*]：全局CAR的名称，首字符需要以字母开头，为1～31个字符的字符串，区分大小写。清除指定全局CAR的统计信息。如果未指定本参数，将清除所有全局CAR的统计信息，包含聚合CAR和分层CAR。

【举例】

\# 清除全局CAR aggcar-1的配置信息。

\<Sysname\> reset qos car name aggcar-1

\

**报文统计配置命令 \-- 报文统计配置命令 \-- display qos traffic-counter**

------------------------------------------------------------------------

**[display qos traffic-counter**]命令用来显示报文统计信息和计数器的配置信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number*]]

分布式设备－IRF模式：

**[display qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]：入方向报文统计。

**[outbound**]：出方向报文统计。

**[counter0**]**：**计数器0。

**[counter1**]**：**计数器1。

**[slot*** slot-number*]：显示指定单板的报文统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的报文统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的报文统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的报文统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的报文统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示4号板的出方向报文统计信息和计数器0的配置信息。

\<Sysname\> display qos traffic-counter outbound counter0 slot 4

Slot 4 outbound counter0 mode:

 Interface: all

 VLAN: all

 Local precedence: all

 Drop priority: all

 Traffic-counter summary:

  Unicast: 1 packets

  Multicast: 1 packets

  Broadcast: 1 packets

  Control packets: 1 packets

  Bridge egress filtered packets: 1 packets

  Tail drop packets: 1 packets

  Tail drop multicast packets: 1 packets

  Forwarding restrictions packets: 1 packets

表8-1 display qos traffic-counter命令显示信息描述表

字段

描述

Slot 4 outbound counter0 mode

单板上某计数器统计出方向流量的监控对象

Interface

本计数器所统计的接口

VLAN

本计数器所统计的VLAN

Local precedence

本计数器所统计的本地优先级

Drop priority

本计数器所统计的丢弃优先级

Traffic-counter summary

本计数器统计信息汇总

Unicast

单播报文数

Multicast

组播报文数

Broadcast

广播报文数

Control packets

控制报文数

Bridge egress filtered packets

下行桥过滤报文数

Tail drop packets

尾丢弃报文数

Tail drop multicast packets

尾丢弃组播报文数

Forwarding restrictions packets

禁止转发报文数

**报文统计配置命令 \-- 报文统计配置命令 \-- qos traffic-counter**

------------------------------------------------------------------------

**[qos traffic-counter**]命令用来使能报文统计功能，并指定统计的流量类型。

**[undo qos traffic-counter**]命令用来关闭报文统计功能。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number* [ **drop-priority** *drop-priority* \| **interface** *interface-type interface-number* \| **local-precedence** *local-precedence* \| **vlan** *vlan-id* ] \*]]

**[undo qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number*]]

分布式设备－IRF模式：

**[qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number* [ **drop-priority** *drop-priority* \| **interface** *interface-type interface-number* \| **local-precedence** *local-precedence* \| **vlan** *vlan-id* ] \*]]

**[undo qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number*]]

【缺省情况】

报文统计功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：入方向报文统计。

**[outbound**]：出方向报文统计。

**[counter0**]：计数器0。

**[counter1**]：计数器1。

**[slot*** slot-number*]：在指定单板上使能报文统计功能。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：在指定成员设备上使能报文统计功能。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：在指定成员设备/PEX上使能报文统计功能。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：在指定成员设备的指定单板上使能报文统计功能。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：在指定单板上使能报文统计功能。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[drop-priority*** drop-priority*]：丢弃优先级，取值范围为0～2。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[interface*** interface-type interface-number*]：指定绑定的端口类型和端口编号。

**[local-precedence*** local-precedence*]：本地优先级，取值范围为0～7。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[vlan*** vlan-id*]：VLAN ID，取值范围为1～4094。

【使用指导】

一块单板提供两组计数器用于统计单板流量，监控的对象可以是端口、VLAN、本地优先级和丢弃优先级。

·当不指定端口时，则监控单板上所有端口的流量。

·当不指定VLAN时，则监控所有VLAN的流量。

·当不指定本地优先级时，则监控所有本地优先级的流量。

·当不指定丢弃优先级时，则监控所有丢弃优先级的流量。

需要注意的是，使用**qos traffic-counter**命令重新设置某单板的监控对象后，计数器的值会自动清空。

【举例】

\# 配置4号板的计数器0统计GigabitEthernet4/1/1端口的出方向流量。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname qos traffic-counter outbound counter0 slot 4 interface gigabitethernet 4/1/1

\# 配置4号成员设备的计数器0统计GigabitEthernet4/1/1端口的出方向流量。（集中式IRF设备）

\<Sysname\> system-view

Sysname qos traffic-counter outbound counter0 slot 4 interface gigabitethernet 4/1/1

\# 配置1号成员设备4号板的计数器0统计GigabitEthernet1/4/1/1端口的出方向流量。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname qos traffic-counter outbound counter0 chassis 1 slot 4 interface gigabitethernet 1/4/1/1

**报文统计配置命令 \-- 报文统计配置命令 \-- reset qos traffic-counter**

------------------------------------------------------------------------

**[reset qos traffic-counter**]命令用来清除报文统计计数器的统计信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number*]]

分布式设备－IRF模式：

**[reset qos traffic-counter**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：入方向报文统计。

**[outbound**]：出方向报文统计。

**[counter0**]：计数器0。

**[counter1**]：计数器1。

**[slot*** slot-number*]：清除指定单板的报文统计计数器的统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：清除指定成员设备的报文统计计数器的统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX的报文统计计数器的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的报文统计计数器的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的报文统计计数器的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 清除4号板的出方向报文统计计数器的统计信息。（分布式设备－独立运行模式）

\<Sysname\> reset qos traffic-counter outbound counter0 slot 4

\# 清除4号成员设备的出方向报文统计计数器的统计信息。（集中式IRF设备）

\<Sysname\> reset qos traffic-counter outbound counter0 slot 4

\# 清除1号成员设备4号板的出方向报文统计计数器的统计信息。（分布式设备－IRF模式）

\<Sysname\> reset qos traffic-counter outbound counter0 chassis 1 slot 4

\

**端口队列统计 \-- 端口队列统计配置命令 \-- display qos queue-statistics interface outbound**

------------------------------------------------------------------------

**[display qos queue-statistics interface outbound**]命令用来显示端口队列出方向的统计信息。

【命令】

**[display qos queue-statistics** **interface** [ *interface-type interface-number*  **outbound**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的队列出方向统计信息。

【举例】

\# 显示接口GigabitEthernet1/0/1的队列出方向统计信息。

\<Sysname\> display qos queue-statistics interface gigabitethernet 1/0/1 outbound

Interface: GigabitEthernet1/0/1

 Direction: outbound

 Forwarded: 0 packets, 0 bytes

 Dropped: 1 packets, 1 bytes

 Queue 0

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 1

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 2

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 3

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 4

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 5

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 6

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

 Queue 7

  Forwarded: 0 packets, 0 bytes

  Dropped: 1 packets, 1 bytes

  Green forwarded: 0 packets, 0 bytes

  Green dropped: 0 packets, 0 bytes

  Yellow forwarded: 0 packets, 0 bytes

  Yellow dropped: 0 packets, 0 bytes

  Red forwarded: 0 packets, 0 bytes

  Red dropped: 0 packets, 0 bytes

  Total queue length: 0 packets

  Current queue length: 0 packets, 0% use ratio

表9-1 display qos queue-statistics interface outbound命令显示信息描述表

字段

描述

Interface

端口队列统计的端口

Direction

端口队列统计的方向

Forwarded

转发的数据包数目和字节数

Dropped

丢弃的数据包数目和字节数

Queue 0、Queue 1、Queue 2、Queue 3、Queue 4、Queue 5、Queue 6、Queue 7

某端口队列统计信息

Green forwarded

绿色报文转发的数据包数目和字节数

Green dropped

绿色报文丢弃的数据包数目和字节数

Yellow forwarded

黄色报文转发的数据包数目和字节数

Yellow dropped

黄色报文丢弃的数据包数目和字节数

Red forwarded

红色报文转发的数据包数目和字节数

Red dropped

红色报文丢弃的数据包数目和字节数

Total queue length

队列总长度

Current queue length

当前队列长度

use ratio

队列使用率

【相关命令】

·**reset counters interface**（接口管理命令参考/以太网接口）

**端口队列统计 \-- 端口队列统计配置命令 \-- qos queue-statistics**

------------------------------------------------------------------------

**[qos queue-statistics **[{ **inbound** \| **outbound** }]]命令用来使能端口队列统计功能。

**[undo qos queue-statistics **[{ **inbound** \| **outbound** }]]命令用来关闭端口队列统计功能。

【命令】

**[qos queue-statistics**[ { **inbound** \| **outbound** }]]

**[undo qos queue-statistics**[ { **inbound** \| **outbound** }]]

【缺省情况】

端口队列统计功能处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：使能入方向端口队列统计功能。

**[outbound**]：使能出方向端口队列统计功能。

【举例】

\# 使能出方向端口队列统计功能。

\<Sysname\> system-view

Sysname qos queue-statistics outbound

【相关命令】

·**display qos queue-statistics** **interface**** outbound**

**端口队列统计 \-- 端口队列统计配置命令 \-- reset qos queue-statistics interface outbound**

------------------------------------------------------------------------

**[reset qos queue-statistics interface outbound**]命令用来清除端口队列出方向的统计信息。

【命令】

**[reset qos queue-statistics interface**] \*[interface-type interface-number*  ]**outbound**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将清除所有接口的队列出方向统计信息。

【举例】

\# 清除所有接口的队列统计计数

\<Sysname\> reset qos queue-statistics interface outbound

\# 清除接口Ten-GigabitEthernet 9/0/1的队列统计计数

\<Sysname\> reset qos queue-statistics interface Ten-GigabitEthernet 9/0/1 outbound

**QPPB \-- QPPB配置命令 \-- bgp-policy**

------------------------------------------------------------------------

![说明](QoS命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bgp-policy**]命令用来配置QPPB功能，即通过BGP传播路由策略中设置的**apply ip-precedence**和**apply qos-local-id**信息。

**[undo bgp-policy**]命令用来取消配置。

【命令】

**[bgp-policy**[ { **destination** \| **source** } { **ip-prec-map** \| **ip-qos-map** } \*]]

**[undo bgp-policy**[ { **destination** \| **source** } [ **ip-prec-map** \| **ip-qos-map** ] \*]]

**[bgp-policy**[ { **destination** \| **source** } **ip-prec-map ip-qos-map**]]

**[undo bgp-policy**[ { **destination** \| **source** } [ **ip-prec-map ip-qos-map** ]]]

【缺省情况】

没有配置QPPB功能。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination**]：使用目的IP查找路由。

**[source**]：使用源IP查找路由。如果指定本参数，则以源IP为目的进行反向查找。

**[ip-prec-map**]：设置IP优先级。

**[ip-qos-map**]：设置QoS本地ID。

【使用指导】

本配置只在接口入方向生效。

MPLS L3VPN网络中，PE公网接口入方向QoS业务在本配置之前进行；其他网络环境中QoS业务在本配置之后进行。

如果存在两条**bgp-policy**命令，分别指定source和destination，后者的设置操作会覆盖前者。

【举例】

\# 在接口GigabitEthernet1/0/1上根据源IP查找路由获得IP优先级和QoS本地ID。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bgp-policy source ip-prec-map ip-qos-map

【相关命令】

·**apply ip-precedence**（三层技术-IP路由命令参考/路由策略）

·**apply qos-local-id**（三层技术-IP路由命令参考/路由策略）

·**route-policy **（三层技术-IP路由命令参考/路由策略）

