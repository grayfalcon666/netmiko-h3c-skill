<!-- CMD-INDEX
  active instance                     | OpenFlow实例视图/OpenFlow OAP实例视图 | L36
  classification                      | OpenFlow实例视图     | L78
  controller address                  | OpenFlow实例视图     | L140
  controller auxiliary                | OpenFlow实例视图     | L210
  controller connect interval         | OpenFlow实例视图     | L270
  controller echo-request interval    | OpenFlow实例视图/OpenFlow OAP实例视图 | L312
  controller mode                     | OpenFlow实例视图     | L354
  datapath-id                         | OpenFlow实例视图/OpenFlow OAP实例视图 | L404
  default table-miss permit           | OpenFlow实例视图/OpenFlow OAP实例视图 | L446
  description                         | OpenFlow实例视图/OpenFlow OAP实例视图 | L488
  display openflow auxiliary          | 任意视图             | L530
  display openflow controller         | 任意视图             | L658
  display openflow flow-table         | 任意视图             | L810
  display openflow group              | 任意视图             | L1472
  display openflow instance           | 任意视图             | L1624
  display openflow meter              | 任意视图             | L2026
  display openflow oap-context        | 任意视图             | L2170
  display openflow summary            | 任意视图             | L2272
  fail-open mode                      | OpenFlow实例视图     | L2366
  flow-entry max-limit                | OpenFlow实例视图/OpenFlow OAP实例视图 | L2410
  flow-table                          | OpenFlow实例视图     | L2452
  forbidden port                      | OpenFlow实例视图     | L2510
  in-band management vlan             | OpenFlow实例视图     | L2558
  listening port                      | OpenFlow实例视图/OpenFlow OAP实例视图 | L2604
  mac-ip dynamic-mac aware            | OpenFlow实例视图     | L2654
  mac-learning forbidden              | OpenFlow实例视图     | L2696
  openflow instance                   | 系统视图             | L2734
  openflow instance oap-instance      | 系统视图             | L2776
  openflow lossless enable            | 系统视图             | L2814
  openflow-instance                   | 接口视图             | L2868
  port                                | OpenFlow实例视图     | L2910
  reset openflow instance controller statistics | 用户视图             | L2952
-->

**OpenFlow \-- OpenFlow配置命令 \-- active instance**

------------------------------------------------------------------------

**[active instance**]命令用来激活OpenFlow实例。

**[undo active instance**]命令用来取消配置。

【命令】

**[active instance**]

**[undo active instance**]

【缺省情况】

未激活OpenFlow实例。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

新配置的实例信息（如VLAN配置、Table配置）必须通过重新激活实例来生效。若当前实例已经与控制器建立连接，激活新配置后会重新建立连接。

【举例】

\# 激活OpenFlow实例1。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 active instance

**OpenFlow \-- OpenFlow配置命令 \-- classification**

------------------------------------------------------------------------

**[classification**]命令用来配置OpenFlow实例的类型。

**[undo classification**]命令用来取消配置。

【命令】

**[classification **[{ **global** \| **port** \| **vlan** *vlan-id* [ **mask** *vlan-mask* ]  **loosen**  }]]

**[undo classification**]

【缺省情况】

没有配置OpenFlow实例的类型。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[global**]：全局实例。

**[port**]：接口实例，实例按接口划分。

**[vlan**]：VLAN实例，实例按VLAN划分。

*[vlan-id*]：VLAN ID，取值范围为1～4094。

*[vlan-mask*]：VLAN掩码，取值范围为0～4095，缺省值为4095。

**[loosen**]：loosen模式。配置loosen模式后，如果接口所在VLAN与实例配置VLAN存在交集，则接口就属于OpenFlow实例。没有配置loosen模式时，只有当实例配置的VLAN是接口所在VLAN的子集，该接口才属于OpenFlow实例。

【使用指导】

多次执行该命令，后配置覆盖前配置。

VLAN & mask为实际生效VLAN区间。mask比特位为1表示符合，可以不连续；比特位为0表示忽略。生效VLAN区间，可通过**display openflow instance**查看。

【举例】

\# 配置OpenFlow VLAN实例1对应的的VLAN为255，掩码为7。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 classification vlan 255 mask 7

【相关命令】

·**display openflow ****instance**

**OpenFlow \-- OpenFlow配置命令 \-- controller address**

------------------------------------------------------------------------

**[controller address**]命令用来配置主连接。

**[undo controller address**]命令用来取消配置。

【命令】

**[controller ***controller-id*** address**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } [ **port** *port-number*   **local address** { **ip** *local-ip-address* \| **ipv6** *local-ipv6-address* } [ **port** *local-port- number* ] ]  **ssl** *ssl-policy-name*   **vrf** *vrf-name* ]]

**[undo controller ***controller-id ***address**]

【缺省情况】

没有配置主连接。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[controller-id*]：控制器的ID号，取值范围为0～63。

**[ip**]*ip-address*：控制器的IP地址。

**[ipv6**]*ipv6-address*：控制器的IPv6地址。

**[port**]*port-number*：控制器建立连接使用的端口号，取值范围为1～65535，缺省值为6633。

**[local address**]：指交换机与控制器连接的源IP地址，当交换机与控制器之间存在多条链路可以连接时，只要有一条链路能够连接，OpenFlow就不会断开连接。

**[ip** *local-*]*ip-address*：源IP地址。

**[ipv6** *local-*]*ipv6-address*：源IPv6地址。

**[port** *local-*]*port-number*：源端口号，取值范围为0～65535，缺省值为0。

**[ssl**]* ssl-policy-name*：安全连接的客户端安全策略，用于控制器认证交换机，每个控制器连接配置独立的安全策略。*ssl-policy-name*为1～31个字符的字符串，不区分大小写。

**[vrf **]*vrf-name*：指定控制器所在的VRF，*vrf-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示控制器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

多次执行该命令可以添加多个控制器，与每个控制器仅允许建立一个主连接。

主连接一般用于控制消息的处理（下发流表项、获取数据、信息上报等）。

建议控制器的IP地址使用单播地址，否则交换机和控制器之间可能无法建立连接。

建议源IP地址使用单播地址，且该IP地址是OpenFlow实例下一个端口的IP地址，否则交换机和控制器之间可能无法建立连接。

【举例】

\# 配置实例1的控制器1的IP地址为1.1.1.1，端口号为6666。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 controller 1 address ip 1.1.1.1 port 6666

**OpenFlow \-- OpenFlow配置命令 \-- controller auxiliary**

------------------------------------------------------------------------

**[controller auxiliary**]命令用来配置辅助连接。

**[undo controller auxiliary**]命令用来取消配置。

【命令】

**[controller**[ *id* **auxiliary** *auxiliary-id* **transport** { **tcp** \| **udp** \| **ssl** *ssl-policy-name* } [ **address** { **ip** *ip-address* \| **ipv6** *ipv6-address* } ]  **port** *port-number* ]]

**[undo** **controller** *id* **auxiliary** *auxiliary-id*]

【缺省情况】

没有配置辅助连接。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[controller ***id*]：实例下controller的编号，取值范围为0～63。

**[auxiliary ***auxiliary-id*]：辅助连接编号，取值范围为1～255。

**[ssl **]*ssl-policy-name*：SSL策略的名称，为1～31字符的字符串，不区分大小写。

**[ip ***ip-address*]：控制器的IPv4地址。

**[ipv6 ***ipv6-address*]：控制器的IPv6地址。

**[port **]*port-number*：控制器的端口号，取值范围为1～65535。

【使用指导】

OpenFlow通道可以由一个主连接和多个辅助连接组成。辅助连接用于提高控制器和OpenFlow交换机的通信能力。

辅助连接命令行和主连接命令行不做额外的检查处理。如果配置冲突，辅助连接将无法建立。

辅助连接的目的地址和端口号可以和主连接不一致。目的地址和端口号未配置时，和主连接一致。

【举例】

\# 为实例1下编号为10控制器配置编号为1的辅助连接。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 controller 10 auxiliary 1 transport tcp

**OpenFlow \-- OpenFlow配置命令 \-- controller connect interval**

------------------------------------------------------------------------

**[controller connect interval**]命令用来配置OpenFlow实例与控制器重连尝试的时间间隔。

**[undo controller connect interval**]命令用来恢复缺省情况。

【命令】

**[controller connect interval **]*interval-value*

**[undo controller connect interval**]

【缺省情况】

OpenFlow实例与控制器重连尝试的时间间隔为60秒。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：重连尝试的时间间隔，取值范围为10～120，单位为秒。

【举例】

\# 配置实例1与控制器重连尝试的时间间隔为10秒。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 controller connect interval 10

**OpenFlow \-- OpenFlow配置命令 \-- controller echo-request interval**

------------------------------------------------------------------------

**[controller echo-request interval**]命令用来配置发送Echo request报文的时间间隔。

**[undo controller echo-request interval**]命令用来恢复缺省情况。

【命令】

**[controller echo-request interval ***interval-value*]

**[undo controller echo-request interval**]

【缺省情况】

发送Echo request报文的时间间隔为5秒。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：发送Echo request报文的时间间隔，取值范围为1～10，单位为秒。

【举例】

\# 配置实例1发送Echo request报文的时间间隔为10秒。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 controller echo-request interval 10

**OpenFlow \-- OpenFlow配置命令 \-- controller mode**

------------------------------------------------------------------------

**[controller mode**]命令用来配置实例内的多个控制器的连接模式。

**[undo controller mode**]命令用来恢复缺省情况。

【命令】

**[controller mode****multiple**[ \| **single** }]

**[undo controller mode**]

【缺省情况】]

连接模式为Multiple。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[multiple**]：多连接模式。

**[single**]：单连接模式。

【使用指导】

当连接模式是Single时，一次仅连接一个控制器，其它作为备份，仅当连接断开才根据ID顺序连接备份控制器，直到连接成功。

当连接模式为Multiple时，同时连接所有控制器，当一个或者多个控制器失效或者连接断开时，仍然能保证OpenFlow交换机正常工作。

【举例】

\# 配置实例1的控制器连接模式为Single。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 controller mode single

**OpenFlow \-- OpenFlow配置命令 \-- datapath-id**

------------------------------------------------------------------------

**[datapath-id**]命令用来配置OpenFlow实例的Datapath ID。

**[undo datapath-id**]命令用来恢复缺省情况。

【命令】

**[datapath-id ***id*]

**[undo datapath-id**]

【缺省情况】

OpenFlow实例的Datapath ID是由实例ID和设备桥MAC组成，前16个比特是实例ID，后48个比特是设备桥MAC。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[id*]：OpenFlow实例的Datapath ID，取值范围为1～0xFFFFFFFFFFFFFFFF。

【举例】

\# 配置实例1的Datapath ID为0x123456。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 datapath-id 123456

**OpenFlow \-- OpenFlow配置命令 \-- default table-miss permit**

------------------------------------------------------------------------

**[default table-miss permit**]命令用来配置OpenFlow实例缺省的table miss 动作。

**[undo default table-miss permit**]命令用来恢复缺省情况。

【命令】

**[default table-miss permit**]

**[undo default table-miss permit**]

【缺省情况】

缺省table miss动作为丢弃。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果配置了本命令，则实例下所有流表的缺省table miss动作为走正常二三层转发；如果没有配置本命令，则实例下所有流表的缺省table miss动作为丢弃。

【举例】

\# 配置OpenFlow实例1的缺省table miss动作。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 default table-miss permit

**OpenFlow \-- OpenFlow配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置OpenFlow实例的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

没有配置OpenFlow实例的描述信息。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：OpenFlow实例的描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置实例1的描述信息为test-desc。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 description test-desc

**OpenFlow \-- OpenFlow配置命令 \-- display openflow auxiliary**

------------------------------------------------------------------------

**[display openflow auxiliary**]命令用来显示OpenFlow实例的辅助连接信息和收发的报文统计信息等。

【命令】

**[display** **openflow** **instance** *instance-id* **auxiliary** [ *controller-id* [ **auxiliary** *auxiliary-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[instance**]*instance-id*：OpenFlow实例号，取值范围为1～4094。

*[controller-id*]：控制器编号，取值范围为0～63。

**[auxiliary ***auxiliary-id*]：辅助连接编号，取值范围为1～255。

【举例】

\# 显示OpenFlow实例100的控制器辅助连接信息。

\<Sysname\> display openflow instance 100 auxiliary

Controller ID: 1    Auxiliary connection number: 2

 Auxiliary connection ID : 1

  Controller IP address  : 192.168.49.48

  Controller port        : 6633

  Connect type           : TCP

  Connect state          : Established

  Packets sent           : 9

  Packets received       : 9

  SSL policy             : \--

 Auxiliary connection ID : 2

  Controller IP address  : 192.168.49.49

   Controller port       : 6633

   Connect type          : TCP

   Connect state         : Established

   Packets sent          : 9

   Packets received      : 9

   SSL policy            : \--

表1-1 display openflow auxiliary命令显示描述表

字段

描述

Controller ID

控制器ID

Auxiliary connection number

辅助连接总数量

Auxiliary connection ID

辅助连接的ID

Controller IP address

已经配置在实例下的Controller的IP地址

Controller port

当前连接Controller的TCP端口号

Connect type

连接类型，

·TCP：使用TCP连接Controller

·SSL：使用SSL连接Controller

·UDP：使用UDP连接Controller

Connect state

连接状态：

·Idle：未建立连接

·Established：成功建立连接

Packets sent

Controller发送的报文的计数

Packets received

Controller接收的报文的计数

SSL policy

用于SSL连接的SSL策略的名称

**OpenFlow \-- OpenFlow配置命令 \-- display openflow controller**

------------------------------------------------------------------------

**[display openflow controller**]命令用来显示OpenFlow实例对应的控制器信息。

【命令】

**[display openflow** { **instance** *instance-id* { **controller** [ *controller-id*  \| **listened** } \| **oap-instance** **listened** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

*[controller-id*]：控制器的ID号，取值范围为0～63。如果未指定本参数，将显示实例下所有控制器的信息。

**[listened**]：实例启动的服务端连接的客户端。

**[oap-instance**]：OpenFlow OAP实例。

【举例】

\# 显示OpenFlow实例100对应的控制器信息。

\<Sysname\> display openflow instance 100 controller

OpenFlow instance ID: 100

 Reconnect interval : 60 (s)

 Echo interval      : 5  (s)

 Controller ID           : 1

 Controller IP address   : 192.168.49.49

 Controller port         : 6633

 Local IP address        : 192.0.0.1

 Local port              : 5566

 Controller role         : Equal

 Connect type            : TCP

 Connect state           : Established

 Packets sent            : 9

 Packets received        : 9

 SSL policy              : \--

 VRF name                : \--

表1-1 display openflow controller命令显示信息描述表

字段

描述

OpenFlow instance ID

OpenFlow实例号

Reconnect interval

实例内所有控制器的断开重连时间间隔，单位为秒

Echo interval

实例内所有控制器发送保活报文的时间间隔，单位为秒

Controller ID

控制器的ID号

Controller IP address

OpenFlow实例对应的控制器的IP地址

Controller port

当前连接控制器的TCP端口号

Local IP address

OpenFlow实例对应的控制器的源IP地址

Local port

当前连接控制器的源TCP端口号

Controller role

控制器的角色：

·\--：未连接，未配置角色

·Equal：控制器的角色是Equal

·Master：控制器的角色是Master

·Slave：控制器的角色是Slave

Connect type

连接类型，

·TCP：使用TCP连接控制器

·SSL：使用SSL连接控制器

Connect state

连接状态：

·Idle：未建立连接

·Established：成功建立连接

Packets sent

已经向控制器发送的报文的计数

Packets received

已经接收控制器的报文的计数

SSL policy

用于SSL连接的SSL策略的名称

VRF name

控制器所在的VRF名称

**OpenFlow \-- OpenFlow配置命令 \-- display openflow flow-table**

------------------------------------------------------------------------

**[display openflow flow-table**]命令用来显示OpenFlow实例的流表信息。

【命令】

**[display openflow instance**[ { *instance-id* \| **oap-instance** } **flow-table** [ *table-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

**[oap-instance**]：OpenFlow OAP实例。

*[table-id*]：流表ID，取值范围为0～254。如果未指定本参数，将显示所有流表的信息。

【举例】

\# 显示OpenFlow实例100的所有流表信息。

\<Sysname\> display openflow instance 100 flow-table

Instance 100 flow table information:

Table 0 information:

 Table type: MAC-IP, flow entry count: 1, total flow entry count: 2

MissRule (default) Flow entry information:

 cookie: 0x0, priority: 0, hard time: 0, idle time: 0, flags: reset_counts

[ \|no_pkt_counts\|no_byte_counts, byte count: \--, packet count: \--]

Match information: any

Instruction information:

 Write actions:

  Drop

Flow entry rule 1 information:

 cookie: 0x0, priority: 1, hard time: 0, idle time: 0, flags: none,

 byte count: \--, packet count: \--

Match information:

 Ethernet destination MAC address: 0000-0000-0001

 Ethernet destination MAC address mask: ffff-ffff-ffff

 VLAN ID: 100, mask: 0xfff

Instruction information:

 Write actions:

  Output interface: GE1/0/4

 Write metadata/mask: 0x0000000000000001/0xffffffffffffffff

 Goto table: 1

Table 1 information:

 Table type: Extensibility, flow entry count: 2, total flow entry count: 2

MissRule (default) Flow entry information:

 cookie: 0x0, priority: 0, hard time: 0, idle time: 0, flags: none,

 byte count: \--, packet count: 60

Match information: any

Instruction information:

 Write actions:

  Drop

Flow entry rule 1 information:

 cookie: 0x0, priority: 0, hard time: 0, idle time: 0, flags: flow_send_rem

[ \|check_overlap, byte count: \--, packet count: 1]

Match information:

 Input interface: GE1/0/3

 Ethernet source MAC address: 0000-0000-0001

 Ethernet source MAC address mask: ffff-ffff-ffff

Instruction information:

 Set meter: 100

 Apply actions:

  Output interface: GE1/0/4

 Write actions:

  Output interface: Controller, send length: 128 bytes

表1-2 display openflow flow-table命令显示信息描述表

字段

描述

Table information

流表信息

Table type

流表类型：

·MAC-IP：MAC-IP流表

·Extensibility：Extensibility流表

flow entry count

控制器下发的流表项个数

total flow entry count

流表中流表项总个数

Flow entry rule information

流表项信息

cookie

流表项cookie

priority

流表项的优先级，数值越大，优先级越高

hard time

流表项的hard time超时时间，单位为秒，0代表永不超时。当定时器超时后就清除该流表项，无论该流表项是否匹配到数据流

idle time

流表项的idle time超时时间，单位为秒，0代表永不超时。如果idle time超时时间内没有数据流匹配到该流表项，该流表项被清除

flags

流表项的标志位：

·flow_send_rem：发送流表项删除消息

·check_overlap：检查流表项重复

·reset_counts：重置流表项统计信息

·no_pkt_counts：不统计报文计数

·no_byte_counts：不统计字节计数

·none：无标志位

byte count

匹配当前流表项的字节计数

packet count

匹配当前流表项的报文计数

Match information

匹配规则信息（ 表1-3(?995838192#_Ref349812296)）

Instruction information

动作指令集信息

Set meter

应用指定的Meter表

Write metadata

写入元数据，元数据用来在不同流表间传递信息

Write metadata mask

元数据掩码

Goto table

进入下一级流表

Clear actions

清除动作集中的所有动作

Apply actions

立即执行动作序列中的动作（ 表1-4(?995838192#_Ref349812331)）

Write actions

更改动作集中的所有动作（ 表1-4(?995838192#_Ref349812331)）

表1-3 流表项匹配规则信息

匹配字段名称

匹配掩码字段名称

描述

Input interface

无

入端口（ 表1-5(?995838192#_Ref349812380)）

Physical input interface

无

入物理端口

Metadata

Metadata mask

元数据/掩码

Ethernet destination MAC address

Ethernet destination MAC address mask

以太网目的MAC地址/掩码

Ethernet source MAC address

Ethernet source MAC address mask

以太网源MAC地址/掩码

Ethernet type

无

以太网类型

VLAN ID

mask

VLAN ID/掩码

VLAN PCP

无

VLAN优先级

IP DSCP

无

DSCP（Differentiated Services Code Point，区分服务编码点）值

IP ECN

无

IP头的ECN（Explicit Congestion Notification，显式拥塞通知）值

IP protocol

无

IPv4或IPv6协议号

IPv4 source address

mask

IPv4源地址/掩码

IPv4 destination address

mask

IPv4目的地址/掩码

TCP source port

mask

TCP源端口

TCP destination port

mask

TCP目的端口

UDP source port

mask

UDP源端口

UDP destination port

mask

UDP目的端口

SCTP source port

mask

SCTP（Stream Control Transmission Protocol，流控制传输协议）源端口

SCTP destination port

mask

SCTP目的端口

ICMPv4 type

无

ICMPv4类型

ICMPv4 code

无

ICMPv4代号

ARP opcode

无

ARP操作类型

ARP source IPv4 address

mask

ARP源IP地址

ARP target IPv4 address

mask

ARP目标IP地址

ARP source MAC address

ARP source MAC address  mask

ARP源MAC地址

ARP target MAC address

ARP target MAC address mask

ARP目的MAC地址

IPv6 source address

IPv6 source address mask

IPv6源地址

IPv6 destination address

IPv6 destination address mask

IPv6目的地址

IPv6 flow label

mask

IPv6流标签

ICMPv6 type

无

ICMPv6类型

ICMPv6 code

无

ICMPv6代号

IPv6 ND target address

无

IPv6邻居发现协议报文的目的IP地址

IPv6 ND source MAC address

无

IPv6邻居发现协议报文的源MAC地址

IPv6 ND target MAC address

无

IPv6邻居发现协议的目的MAC地址

MPLS label

无

MPLS第一个头部的标签

MPLS tc

无

MPLS第一个头部的TC（Traffic Class，流量等级）

Tunnel ID

mask

与一个逻辑口相关的MetaData

IPv6 extension header

mask

IPv6扩展头

Output interface

无

出接口

VRF index

无

VPN索引

Fragment

无

分片标志

Physical output interface

无

出物理端口

CVLAN ID

mask

CVLAN ID/掩码

表1-4 流表项动作类型

动作名称

描述

Drop

丢弃报文（非协议Action）

Output interface

从指定端口发送报文（ 表1-5(?995838192#_Ref349812380)）

send length

当output类型为Controller时，指定上送报文的字节长度

Group

根据指定Group表处理报文

Set queue

将流表项映射到指定队列ID

Set field

修改报文指定的域

Set MPLS TTL

设定MPLS的TTL域值

Set IP TTL

设定IP头的TTL域值

Push VLAN tag

添加一个新的VLAN Tag

Push MPLS tag

添加一个新的MPLS Tag

Pop MPLS tag

删除最外层的MPLS Tag

Push PBB tag

添加一个新的PBB服务Tag

Pop VLAN tag

删除最外层的VLAN Tag

Pop PBB tag

删除最外层PBB服务Tag

Decrement MPLS TTL

MPLS的TTL减一

Decrement IP TTL

IP的TTL减一

Copy TTL inwards

将最外层的TTL拷贝到紧接最外层

Copy TTL outwards

将紧接最外层的TTL拷贝到最外层

表1-5 流表项端口类型

![说明](OpenFlow命令.files/image001.png)

具体支持情况和设备的型号有关，请以设备的实际情况为准。

端口名称

入端口

出端口

说明

In port

不支持

支持

报文从入接口转发

Table

不支持

支持

报文重新进入流表进行匹配

Normal

不支持

支持

报文正常转发

Flood

不支持

支持

报文广播发送

All

不支持

支持

报文从所有接口发送

Controller

支持

支持

报文上送控制器

Local

支持

支持

报文上送本地CPU

Any

不支持

不支持

接口通配描述，不能作为入接口以及出接口

（端口名称）

支持

支持

实例有效端口，包含物理接口和逻辑接口（如聚合接口）

**OpenFlow \-- OpenFlow配置命令 \-- display openflow group**

------------------------------------------------------------------------

**[display openflow group**]命令用来显示OpenFlow实例的Group表项信息。

【命令】

**[display**[ **openflow** **instance** { *instance-id* \| **oap-instance** } **group** [ *group-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

**[oap-instance**]：OpenFlow OAP实例。

*[group-*id]：Group ID，取值范围为0～0xffffff00。如果未指定本参数，将显示实例所有Group表项的信息。

【举例】

\# 显示OpenFlow实例100的Group表项信息。

\<Sysname\> display openflow instance 100 group

Instance 100 group table information:

 Group count: 2

Group entry 103:

 Type: All, byte count: 55116, packet count: 401

 Bucket 1 information:

Action count 1, watch port: any, watch group: any

Byte count 55116, packet count 401

  Output interface: BAGG100

 Bucket 2 information:

 Action count 1, watch port: any, watch group: any

  Byte count \--, packet count \--

  Output interface: Controller, send length: 128 bytes

 Referencedinformation:

  Count: 3

  Flow table 0

  Flow entry: 1, 2, 3

Group entry 104:

 Type: All, byte count: 0, packet count: 0

 Bucket 1 information:

  Action count 1, watch port: any, watch group: any

  Byte count \--, packet count \--

  Output interface: Controller, send length: 128 bytes

 Referencedinformation:

  Count: 0

表1-6 display openflow group命令显示信息描述表

字段

描述

Group count

当前实例包含的Group表项的总个数

Type

当前Group表项的类型，

·All：执行所有动作桶，用于组播或者广播

·Select：自动选择一个动作桶执行

·Indirect：始终执行固定的动作桶

·Fast failover：始终执行第一个活跃的动作桶

Bucket

Group表项包含的bucket

Action count

当前bucket包含的action的个数

Byte count

group/bucket的字节统计计数，"\--"表示不支持

packet count

group/bucket的报文统计计数，"\--"表示不支持

watch port

影响bucket的live状态的端口

watch group

影响bucket的live状态的group ID

Output interface

Group表项中包含的出端口

Referenced information

Group表项被流表项引用的信息

Count

引用Group表项的流表项的总个数

Flow table

引用Group表项的流表项所在的流表ID

Flow entry

引用Group表项的流表项ID列表

**OpenFlow \-- OpenFlow配置命令 \-- display openflow instance**

------------------------------------------------------------------------

**[display openflow instance**]命令用来显示OpenFlow实例的详细信息。

【命令】

**[display openflow instance **[[ *instance-id* \| **oap-instance** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。如果未指定本参数，将显示所有实例的详细信息。

**[oap-instance**]：OpenFlow OAP实例。

【举例】

\# 显示所有OpenFlow实例的详细信息。

\<Sysname\> display openflow instance

Instance 100 verbose information:

Configuration information:

 Description   : test-desc

 Active status : Active

 Inactive configuration:

  Classification: VLAN, total VLANs(1)

   3

  Flow table:

   Table ID(type): 0(MAC-IP)

   Table ID(type): 1(Extensibility)

 Active configuration:

  Classification: VLAN, loosen mode, total VLANs(1)

   2

  In-band management VLAN, total VLANs(0)

   Empty VLAN

  Connect mode: Multiple

  MAC-address learning: Disabled

  Flow table:

   Table ID(type): 0(MAC-IP), count: 0

  Flow-entry max-limit: 65535

  Datapath ID: 0x0000001234567891

  Default table-miss: Drop

  Forbidden port: None

Port information:

 GigabitEthernet1/0/3

Active channel information:

 Controller 1 IP address: 192.168.49.49  port: 6633

 Controller 2 IP address: 192.168.43.49  port: 6633

Instance 200 verbose information:

Configuration information:

 Description   : test

 Active status : Active

 Inactive configuration:

  Classification: VLAN, total VLANs(1)

   1

  Flow table:

   Table ID(type): 0(MAC-IP)

   Table ID(type): 1(Extensibility)

 Active configuration:

  Classification: VLAN, total VLANs(1)

   4

  In-band management VLAN, total VLANs(0)

   Empty VLAN

  Connect mode: Multiple

  MAC-address learning: Disabled

  Flow table:

   Table ID(type): 0(MAC-IP), count: 0

  Flow-entry max-limit: 65535

  Datapath ID: 0x0000001234567890

  Default table-miss: Permit

  Forbidden port: VLAN interface

Port information:

 GigabitEthernet0/1/3

Active channel information:

 Fail-open mode: Secure

Instance 300 verbose information:

Configuration information:

 Description   : test

 Active status : Active

 Inactive configuration:

  None

 Active configuration:

  Classification: VLAN, total VLANs(4)

   8, 10, 12, 14

  In-band management VLAN, total VLANs(1)

   10

  Connect mode: Multiple

  MAC-address learning: Disabled

  Flow table:

   Table ID(type): 0(MAC-IP), count: 0

  Flow-entry max-limit: 65535

  Datapath ID: 0x0000001234567801

  Default table-miss: Drop

  Forbidden port: None

Port information:

 GigabitEthernet0/1/3

Active channel information:

 Failopen mode: Secure

Instance 400 information:

Configuration information:

 Description   : \--

 Active status : inactive

 Inactive configuration:

  Classification: Port

  Port configuration information:

   GigabitEthernet2/0/1

   GigabitEthernet2/0/2

   GigabitEthernet2/0/3

  In-band management VLAN, total VLANs(0)

   empty VLAN

  Connect mode: multiple

  MAC address learning: Enabled

  Flow table:

   Table ID(type): 0(Extensibility)

  Flow-entry max-limit: 65535

  Datapath ID: 0x000100e001000000

Active configuration:

  none

Instance 500 information:

Configuration information:

 Description   : \--

 Active status : active

 Inactive configuration:

  none

 Active configuration:

  Classification: Port

  In-band management VLAN, total VLANs(0)

   empty VLAN

  Connect mode: multiple

  MAC address learning: Enabled

  Flow table:

   Table ID(type): 0(Extensibility), count: 0

  Flow-entry max-limit: 65535

  Datapath ID: 0x000100e001000000

Port information:

 GigabitEthernet2/0/1

 GigabitEthernet2/0/2

 GigabitEthernet2/0/3

Active channel information:

 Failopen mode: secure

表1-7 display openflow instance命令显示信息描述表

字段

描述

Configuration information

配置信息

Description

实例的描述信息

Active status

实例状态：

·Active：激活

·Inactive：未激活

Inactive configuration

未生效的实例配置

Active configuration

已生效的实例配置

Classification: VLAN, total VLANs

实例VLAN信息及VLAN总个数

Classification: Port

实例处于Port模式

loose mode

处于loosen模式

In-band management VLAN, total VLANs

带内管理VLAN列表及VLAN个数

Connect mode

控制器连接模式：

·Single：串行

·Multiple：并行

MAC-address learning

MAC地址学习：

·Enabled：允许

·Disabled：禁止

Flow table

实例的流表信息

Table ID(type)

流表ID，类型

·MAC-IP：MAC-IP类型流表

·Extensibility：Extensibility类型流表

count

对应流表的流表项总个数

Flow-entry max-limit

当前实例的流表最大个数限制

Datapath ID

当前实例的Datapath ID

Default table-miss

缺省table miss动作：

·Permit：允许

·Drop：丢弃

Forbidden port

禁止上送Controller的端口类型：

·VLAN interface：VLAN接口

·Virtual Switch Interface：VSI接口

Port information

已加入实例的端口的名称列表

Active channel information

生效的控制通道信息

IP address

已经配置在实例下的的控制器的IP地址

Port

当前连接Controller的TCP端口号

Fail-open mode

连接中断时的运行模式：

·Standalone：标准模式

·Secure：安全模式

**OpenFlow \-- OpenFlow配置命令 \-- display openflow meter**

------------------------------------------------------------------------

**[display openflow meter**]命令用来显示OpenFlow实例的Meter表项信息。

【命令】

**[display openflow instance **[{ *instance-id* \| **oap-instance** } **meter** [ *meter-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

**[oap-instance**]：OpenFlow OAP实例。

*[meter-*id]：Meter ID，取值范围为0～0xffff0000。如果未指定本参数，将显示实例所有Meter表项的信息。

【举例】

\# 显示OpenFlow实例100的Meter表项信息。

\<Sysname\> display openflow instance 100 meter

Meter flags: KBPS  \-- Rate value in kb/s, PKTPS \-- Rate value in packet/sec

             BURST \-- Do burst size,      STATS \-- Collect statistics

Instance 100 meter table information:

 meter entry count: 2

Meter entry 100 information:

 Meter flags: KBPS

 Band 1 information

 Type: drop, rate: 1024, burst size: 65536

 Byte count: \--, packet count: \--

 Referencedinformation:

  Count: 3

  Flow table: 0

  Flow entry: 1, 2, 3

Meter entry 200 information:

 Meter flags: KBPS

 Band 1 information

 Type: drop, rate: 10240, burst size: 655360

 Byte count: \--, packet count: \--

 Referenced information:

  Count: 0

表1-8 display openflow meter命令显示信息描述表

字段

描述

Meter entry count

当前实例包含的Meter表项的总个数

Meter flags

当前Meter表项的所携带的flags：

·KBPS：速率值以kbps为单位

·PKTPS：速率值以packet/sec（包/秒）为单位

·BURST：帧大小

·STATS：收集统计信息

Band

Meter表项包含的band

Type

band类型：

·drop：丢弃数据包

·dscp_remark：修改数据包IP头部的dscp

rate

速率

burst size

帧大小

Byte count

band的字节统计计数，"\--"表示不支持

packet count

band的报文统计计数，"\--"表示不支持

Reference information

Meter表项被流表项引用的信息

Count

引用Meter表项的流表项的总个数

Flow table

引用Meter表项的流表项所在的流表ID

Flow entry

引用Meter表项的流表项ID列表

**OpenFlow \-- OpenFlow配置命令 \-- display openflow oap-context**

------------------------------------------------------------------------

**[display openflow oap-context**]命令显示OAP的Context信息。

【命令】

**[display openflow oap-context **[[ **oap-interface** *oap-interface-type oap-interface-number* \| **in-interface** *in-interface-type in-interface-number* \| **out-interface** *out-interface-type out-interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[oap-interface** *oap-interface-type oap-interface-number*]：OAP接口。

**[in-interface** *in-interface-type in-interface-number*]：入接口。

**[out-interface*** out-interface-type out-interface-number*]：出接口。

【使用指导】

如果未指定任何接口，则显示所有OAP Context信息。

【举例】

\# 显示OpenFlow的OAP Context信息。

\<Sysname\> display openflow oap-context

Total number: 2

 OAP client: 3

  Input interface  : GigabitEthernet1/0/1

  Output interface : GigabitEthernet1/0/2

  OAP interface    : GigabitEthernet1/0/3

  VRF name         : \--

  OAP context      : 0xFFFFFFFFFFFFFFFF

OAP client: 4

  Input interface  : GigabitEthernet1/0/1

  Output interface : GigabitEthernet1/0/2

  OAP interface    : GigabitEthernet1/0/3

  VRF name         : \--

  OAP context      : 0xFFFFFFFFFFFFFFFF

表1-2 display openflow instance oap-mode context命令显示描述表

字段

描述

Total number

控制器（OAP client）的总数

Controller

控制器的编号

Input interface

入接口的接口名

Output interface

出接口的接口名

OAP interface

OAP接口的接口名

VRF name

绑定的Vpn接口索引

OAP context

分配的OAP context

**OpenFlow \-- OpenFlow配置命令 \-- display openflow summary**

------------------------------------------------------------------------

**[display openflow summary**]命令用来显示OpenFlow实例的概要信息。

【命令】

**[display openflow summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示OpenFlow概要信息。

\<Sysname\> display openflow summary

Fail Open mode: Se \-- secure mode, Sa \-- standalone mode

Reactive flags: Y \-- Need active instance,

                N \-- Needn\'t active instance

ID    Status    Datapath-ID         Channel    Table num  Port num  Reactive

1     Active    0x0000000100001221  Connected  2          8         Y

10    Inactive  -                   -          -          -         -

4094  Active    0x00000ffe00001221  Fail(Sa)   2          0         N

OAP   Active    0x0000100200001221  Fail(Sa)   1          8         N

表1-9 display openflow summary命令显示信息描述表

字段

描述

ID

实例ID或OAP实例

Status

实例激活状态

·Active：实例已经激活

·Inactive：实例尚未激活

Datapath-ID

实例的Datapath ID，未激活实例无取值

Channel

与控制器连接通道的状态，未激活实例无取值

·Connected：与控制器已经建立安全通道

·Fail(Se)：连接通道断开，连接中断模式为Secure模式

·Fail(Sa)：连接通道断开，连接中断模式为Standalone模式

Table-num

实例中流表数目，未激活实例无取值

Port-num

属于该实例的接口数目，未激活实例无取值

Reactive

是否在激活实例后重新更改了配置，需要重新激活

·Y：配置已经改变了，需要重新激活

·N：配置未改变，不需要重新激活

**OpenFlow \-- OpenFlow配置命令 \-- fail-open mode**

------------------------------------------------------------------------

**[fail-open mode**]命令用来配置交换机与控制器连接中断时的运行模式。

**[undo fail-open mode**]命令用来恢复缺省情况。

【命令】

**[fail-open mode**[ { **secure** \| **standalone** }]]

**[undo** **fail-open** **mode**]

【缺省情况】

OpenFlow实例建立时，缺省为Secure模式，且为该实例下发Table Miss表项（动作为drop）。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[secure**]：Secure模式，连接断开后，交换机根据流表项转发。

**[standalone**]：Standalone模式，连接断开后，交换机正常转发。

【举例】

\# 配置交换机与控制器连接中断时的运行模式为Standalone模式。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 fail-open mode standalone

**OpenFlow \-- OpenFlow配置命令 \-- flow-entry max-limit**

------------------------------------------------------------------------

**[flow-entry max-limit**]命令用来配置Extensibility表的流表项个数上限。

**[undo flow-entry max-limit**]命令用来恢复缺省情况。

【命令】

**[flow-entry** **max-limit** *limit-value*]

**[undo** **flow-entry** **max-limit**]

【缺省情况】

本命令的缺省情况和设备的型号有关，请以设备的实际情况为准。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit-value*]：流表项上限值。取值范围和设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置Extensibility表的流表项个数上限为256。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 flow-entry max-limit 256

**OpenFlow \-- OpenFlow配置命令 \-- flow-table**

------------------------------------------------------------------------

**[flow-table**]命令用来动态配置实例下的流表类型和ID。

**[undo flow-table**]命令用来恢复缺省情况。

【命令】

**[flow-table****extensibility ***extensibility-table-id*****[\| ]**mac-ip** *mac-ip-table-id* }&\<1-n\>

**[undo flow-table**]

【缺省情况】]

实例包含了一个Extensibility流表，流表ID为0。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[extensibility **]*extensibility-table-id*：Extensibility流表ID，取值范围为0～254。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-ip**] *mac-ip-table-id*：MAC-IP流表ID，取值范围为0～254。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

&\<1-n\>：表示前面的参数最多可以输入n次，n的取值范围和设备的型号有关，请以设备的实际情况为准。需要注意的是，对于MAC-IP流表，只能输入一次。

![说明](OpenFlow命令.files/image001.png)

有的产品只支持先输入**mac-ip**后输入**extensibility**，不支持先输入**extensibility**后输入**mac-ip**。具体和设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户激活实例之前配置当前实例将要使用的流表类型以及与之对应的流表ID。

多次配置本命令，新配置将覆盖旧配置。

输入的Extensibility流表ID要大于MAC-IP流表ID。

【举例】

\# 配置实例1流表类型为MAC-IP表ID为0，Extensibility表ID为1。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 flow-table mac-ip 0 extensibility 1

**OpenFlow \-- OpenFlow配置命令 \-- forbidden port**

------------------------------------------------------------------------

![说明](OpenFlow命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[forbidden port**]命令用来配置禁止上送Controller的端口类型。

**[undo forbidden port**]命令用来取消该配置。

【命令】

**[forbidden port **[{ **vlan-interface** \| **vsi-interface** } \*]]

**[undo forbidden port**]

【缺省情况】

所有接口都上送Controller。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan-interface**]：VLAN接口。

**[vsi-interface**]：VSI接口。

【举例】

\# 配置OpenFlow实例1禁止上送VLAN接口。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 forbidden port vlan-interface

**OpenFlow \-- OpenFlow配置命令 \-- in-band management vlan**

------------------------------------------------------------------------

**[in-band management vlan**]命令用来配置带内管理VLAN。

**[undo in-band management vlan**]命令用来取消该配置。

【命令】

**[in-band management vlan **{ *vlan-id* [ **to** *vlan-id*  } &\<1-10\>]]

**[undo in-bandmanagement vlan**]

【缺省情况】

没有配置带内管理VLAN。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：VLAN ID，取值范围为1～4094。

【使用指导】

缺省情况下，OpenFlow实例内的VLAN都是进行OpenFlow转发的，实例无法通过这些VLAN与控制器建立连接。配置带内管理VLAN后，这些VLAN内流量是正常转发的，可以用于实例与控制器建立连接。

【举例】

\# 在实例1中配置VLAN 10为带内管理VLAN。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 in-band management vlan 10

**OpenFlow \-- OpenFlow配置命令 \-- listening port**

------------------------------------------------------------------------

**[listening prot**]命令用来为OpenFlow实例启动SSL服务器。

**[undo listening port**]命令用来取消该配置。

【命令】

**[listening port ***port-number*** ssl ***ssl-policy-name*]

**[undo listening port**]

【缺省情况】

OpenFlow实例下没有启动SSL服务器。

【视图】

OpenFlow实例视图/OpenFlow OAP实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[port ***port-number*]：服务器的端口号，取值范围为1～65535。

**[ssl **]*ssl-policy-name*：SSL策略的名称，为1～31字符的字符串，不区分大小写。

【使用指导】

没有启动SSL服务器时，设备作为TCP/SSL客户端主动连接控制器（SSL服务器，需要相应配置）；启动SSL服务器之后，设备作为SSL服务器端被动等待控制器（SSL客户端）连接。

一个实例只能启动一个SSL服务器。必须先删掉已有配置才能进行新的配置。

【举例】

\# 为OpenFlow实例1启动端口号为20000的SSL服务器。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 listening port 20000 ssl ssl_name

**OpenFlow \-- OpenFlow配置命令 \-- mac-ip dynamic-mac aware**

------------------------------------------------------------------------

**[mac-ip dynamic-mac aware**]命令用来配置支持动态MAC地址。

**[undo mac-ip dynamic-mac aware**]命令用来恢复缺省情况。

【命令】

**[mac-ip dynamic-mac aware**]

**[undo mac-ip dynamic-mac aware**]

【缺省情况】

不支持动态MAC地址，即忽略控制器下发的此类消息。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

此功能仅在支持MAC-IP流表情况下，决定是否支持控制器在查询或者删除流表项时包含动态MAC地址（动态MAC表项变化不需要上报控制器）。

【举例】

\# 配置实例1支持动态MAC地址。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 mac-ip dynamic-mac aware

**OpenFlow \-- OpenFlow配置命令 \-- mac-learning forbidden**

------------------------------------------------------------------------

**[mac-learning forbidden**]命令用来在实例配置的VLAN上禁止MAC地址学习。

**[undo mac-learning forbidden**]命令用来恢复缺省情况。

【命令】

**[mac-learning forbidden**]

**[undo mac-learning forbidden**]

【缺省情况】

实例配置的VLAN上允许MAC地址学习。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置实例1禁止MAC地址学习。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 mac-learning forbidden

**OpenFlow \-- OpenFlow配置命令 \-- openflow instance**

------------------------------------------------------------------------

**[openflow instance**]命令用来创建OpenFlow实例，并进入OpenFlow实例视图。

**[undo openflow instance**]命令用来删除OpenFlow实例。

【命令】

**[openflow instance** *instance-id*]

**[undo openflow instance** *instance-id*]

【缺省情况】

没有配置OpenFlow实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

【举例】

\# 创建OpenFlow实例1，并进入OpenFlow实例视图。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1

**OpenFlow \-- OpenFlow配置命令 \-- openflow instance oap-instance**

------------------------------------------------------------------------

**[openflow instance** **oap-instance**]命令用来创建OpenFlow OAP实例，并进入OpenFlow OAP实例视图。

**[undo openflow instance oap-instance**]命令用来删除OpenFlow OAP实例。

【命令】

**[openflow instance oap-instance**]

**[undo openflow instance oap-instance**]

【缺省情况】

没有配置OpenFlow OAP实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 创建OpenFlow OAP实例，并进入OpenFlow OAP实例视图。

\<Sysname\> system-view

Sysname openflow instance oap-instance

Sysname-of-inst-oap

**OpenFlow \-- OpenFlow配置命令 \-- openflow lossless enable**

------------------------------------------------------------------------

![说明](OpenFlow命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[openflow lossless enable**]命令用来开启OpenFlow的无丢包模式。

**[undo openflow lossless enable**]命令用来恢复缺省情况。

【命令】

**[openflow lossless enable**]

**[undo openflow lossless enable**]

【缺省情况】

没有开启OpenFlow的无丢包模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在某些设备的OpenFlow场景中，OpenFlow的流表下发过程中设备可能会出现丢包，从而引发很多问题，比如流量误上送Controller，导致误下发OpenFlow表项等，此时需要开启OpenFlow的无丢包模式。在无丢包模式下，设备不会丢包，OpenFlow在实际网络中可以正常使用，但是匹配能力会受限制，比如不能匹配IPv6地址。

在非OpenFlow场景中，请不要开启OpenFlow的无丢包模式，否则会影响转发效率和能力级匹配。

不同设备的OpenFlow场景是否需要使用此配置不同，请根据实际需要配置。

要使配置生效，必须在配置后重启设备。在重启设备前，请保存当前配置。

【举例】

\# 开启OpenFlow的无丢包模式。

\<Sysname\> system-view

Sysname openflow lossless enable

 Enable lossless traffic function? [Y/N:y]

 For the setting to take effect, save the configuration, and then reboot the device.

**OpenFlow \-- OpenFlow配置命令 \-- openflow-instance**

------------------------------------------------------------------------

**[openflow-instance**]命令用来在接口下绑定OpenFlow实例。

**[undo openflow-instance**]命令用来取消该配置。

【命令】

**[openflow-instance** *instance-id*]

**[undo openflow-instance** *instance-id*]

【缺省情况】

接口下没有绑定OpenFlow实例。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

【举例】

\# OpenFlow实例1已存在，且为接口模式，配置接口GigabitEthernet1/0/1下绑定实例1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 openflow-instance 1

**OpenFlow \-- OpenFlow配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来在实例下绑定接口。

**[undo port**]命令用来取消该配置。

【命令】

**[port** *interface-type interface-number1* [ **to** *interface-type interface-number2* ]]

**[undo port*** interface-type interface-number1* [ **to** *interface-type interface-number2* ]]

【缺省情况】

实例下没有绑定接口。

【视图】

OpenFlow实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number1 * **to** *interface-type interface-number2* ]：接口类型和编号，*interface-number2*的值要大于或等于*interface-number1*的值。

【举例】

\# OpenFlow实例下绑定接口GigabitEthernet1/0/1到GigabitEthernet1/0/3。

\<Sysname\> system-view

Sysname openflow instance 1

Sysname-of-inst-1 port gigabitethernet 1/0/1 to gigabitethernet 1/0/3

**OpenFlow \-- OpenFlow配置命令 \-- reset openflow instance controller statistics**

------------------------------------------------------------------------

**[reset openflow instance controller statistics**]命令用来清除控制器发送和接收报文的统计计数。

【命令】

**[reset openflow instance** { *instance-id* { **controller** [ *controller-id*  \| **listened** } \| **oap-instance** **listened** } **statistics**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4094。

*[controller-id*]：控制器的ID号，取值范围为0～63。如果未指定本参数，清除实例下所有控制器发送和接收报文的统计计数。

**[listened**]：实例启动的服务端连接的客户端。

**[oap-instance**]：OpenFlow OAP实例。

【举例】

\# 清除OpenFlow实例1对应的所有控制器发送和接收报文的统计计数。

\<Sysname\> reset openflow instance 1 controller statistics

\# 清除OAP实例启动的服务端连接的客户端发送和接收报文的统计计数。

\<Sysname\> reset openflow instance oap-instance listened statistics

