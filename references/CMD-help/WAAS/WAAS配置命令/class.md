
**WAAS \-- WAAS配置命令 \-- class**

------------------------------------------------------------------------

**[class**]命令用来配置WAAS策略引用的指定类，并进入WAAS策略类动作视图。

**[undo class**]命令用来取消WAAS策略对指定类的引用。

【命令】

**[class ***class-name * **insert-before** *existing-class* ]

**[undo class ***class-name*]

【缺省情况】

WAAS策略未引用任何类。

【视图】

WAAS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：[指定引用的类名称，为]1～63个字符的字符串，不区分大小写，该类必须存在。

**[insert-before** *existing-class*]：表示插入到指定类之前，*existing-class*表示WAAS策略已引用的类名称。

【使用指导】

·WAAS策略支持引用预定义类。（预定义类参见表 1-7(?-326408526#_Ref401328623)）

·报文流量匹配类时，按照引用的类的排序进行匹配，匹配上任一个类，则按照相应动作处理报文流量。

·通过本命令，可对WAAS策略已引用的多个类进行排序。

·如果WAAS策略未为引用的类配置任何动作，则该类不参与所属策略对报文流量的匹配。

·建议用户通过执行此命令进入预定义类动作视图，通过修改预定义类的方式完成配置。

【举例】

\# 配置WAAS策略引用预定义类AFS，并进入其动作视图。

\<Sysname\> system-view

Sysname waas policy waas_global

Sysname-waaspolicy-waas_global class AFS

Sysname-waaspolicy-waas_global-AFS

\# 配置WAAS策略引用预定义类AOL，将其插入到AFS之前，并进入AOL动作视图。

\<Sysname\> system-view

Sysname waas policy waas_global

Sysname-waaspolicy-waas_global class AOL insert-before AFS

Sysname-waaspolicy-waas_global-AOL

\# WAAS策略已依次引用预定义类AFS、AOL，调整class顺序，将AOL插入到AFS之前，并进入AOL类动作视图。

\<Sysname\> system-view

Sysname waas policy waas_global

Sysname-waaspolicy-waas_global class AOL insert-before AFS

Sysname-waaspolicy-waas_global-AOL

【相关命令】

·**display waas policy**

·**waas class**

·**waas policy**

**WAAS \-- WAAS配置命令 \-- display waas class**

------------------------------------------------------------------------

**[display waas class**]命令用来显示WAAS类的信息。

【命令】

**[display waas class ** *class-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[class-name*]：指定WAAS类的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有WAAS类的信息。

【举例】

\# 显示类class1的信息。

\<Sysname\> display waas class class1

WAAS class: class1

  match 1 tcp source 1.1.1.1/24 port 50000 60000

  match 6 tcp destination 2.2.2.2 port 1 1024

  match 11 tcp source 1001::1111/96 port 50000 60000

  match 16 tcp destination 2002::2222 port 1 1024

表1-1 display waas class命令显示信息描述表

字段

描述

WAAS class

WAAS类的名称

match

WAAS类包含的匹配规则

【相关命令】

·**match tcp**

·**waas class**

**WAAS \-- WAAS配置命令 \-- display waas policy**

------------------------------------------------------------------------

**[display waas policy**]命令用来显示WAAS策略的信息。

【命令】

**[display waas policy** [ *policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：指定WAAS策略的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，将显示所有WAAS策略的信息。

【举例】

\# 显示指定WAAS策略po1的信息。

\<Sysname\> display waas policy po1

WAAS policy: po1

  class cl1

    optimize TFO DRE LZ

  class cl2

    optimize TFO DRE

  class cl3

    passthrough

  class cl4

    optimize TFO LZ

  class cl5

表1-2 display waas policy命令显示信息描述表

字段

描述

WAAS policy

WAAS策略的名称

class

WAAS策略引用的class名称

optimize

class配置的优化方式，取值包括：

·TFO：表示流传输优化方式，仅支持TCP流传输优化。

·DRE：表示消除冗余数据优化方式。

·LZ：表示数据压缩优化方式。

passthrough

class直接旁路动作，不做任何优化处理

【相关命令】

·**class**

·**optimize**

·**passthrough**

·**waas policy**

**WAAS \-- WAAS配置命令 \-- display waas session**

------------------------------------------------------------------------

**[display waas session**]命令用来显示WAAS会话信息。

【命令】

集中式设备：

**[display waas session **[{ **ipv4** \| **ipv6** } [ **client-ip** *client-ip* ]  **client-port** *client-port*   **server-ip**]

*[server-ip*****  **server-port** *server-port*   **peer-id** *peer-id*   **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display waas session **[{ **ipv4** \| **ipv6** } [ **client-ip** *client-ip* ]  **client-port** *client-port*   **server-ip**]

*[server-ip*****  **server-port** *server-port*   **peer-id** *peer-id*   **verbose**   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display waas session **[{ **ipv4** \| **ipv6** } [ **client-ip** *client-ip* ]  **client-port** *client-port*   **server-ip**]

*[server-ip*****  **server-port** *server-port*   **peer-id** *peer-id*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IPv4会话信息。

**[ipv6**]：显示IPv6会话信息。

**[client-ip ***client-ip*]：显示指定客户端地址的会话信息，*client-ip*表示客户端IP地址。

**[client-port ***client-port*]：显示指定客户端端口号的会话信息，*client-port*表示客户端端口号，取值范围为1～65535。

**[server-ip ***server-ip*]：显示指定服务器端地址的会话信息，*server-ip*表示服务器端IP地址。

**[server-port ***server-port*]：显示指定服务器端端口号的会话信息，*server-port*表示服务器端端口号，取值范围为1～65535。

**[peer-id ***peer-id*]：显示指定对端设备的WAAS会话信息，*peer-id*表示对端设备的桥MAC地址，格式为H-H-H。

**[verbose**]：显示WAAS会话的详细信息。如果不指定本参数，则显示WAAS会话的简要信息。

**[slot ***slot-number*]：显示指定单板的会话信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的会话信息。（分布设备-独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的会话信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示所有成员设备上的会话信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的会话信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示所有成员设备/PEX上的会话信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的会话信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的会话信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的会话信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟槽位号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示所有单板上的会话信息。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

显示所有满足指定条件的会话的信息。如果除IPv4或IPv6外没有指定任何参数，将显示所有IPv4或IPv6的会话信息。

【举例】

\# 显示IPv4会话的简要信息。

\<Sysname\> display waas session ipv4

Peer ID: 0021-90ad-0012

Start Time: Fri Mar 21 10:43:05 2014

Source IP/Port: 1.1.1.1/34572

Destination IP/Port: 2.2.2.2/80

Peer ID: 0011-10ad-0012

Start Time: Fri Mar 21 10:45:05 2014

Source IP/Port: 2.2.1.1/34572

Destination IP/Port: 3.2.2.3/80

Total 2 sessions found.

\# 显示IPv4会话的详细信息。

\<Sysname\> display waas session ipv4 verbose

Peer ID: 0021-90ad0-01221

Start Time: Fri Mar 21 11:43:05 2014

Source IP/Port: 1.1.1.1/34572

Destination IP/Port: 2.2.2.2/80

LAN interface: Serial1/0/1

WAN interface: Serial1/0/2

Configured Policy: TFO DRE LZ

Negotiated Policy: TFO DRE LZ

LAN-\>WAN bytes: Original   104884      Optimized  88594

WAN-\>LAN bytes: Original   744588      Optimized  3355445

LZ section：

  Encode status：

    Bytes in: 0

    Bytes out: 0

    Bypass bytes: 400

    Space saved: 0%

    Average Latency: 0 usec

  Decode status：

    Bytes in: 329

    Bytes out: 393

    Bypass bytes: 63

    Space saved: 16%

    Average Latency: 2 usec

DRE section：

  Encode status：

    Bytes in: 0

    Bytes out: 0

    Bypass bytes: 314

    Space saved: 0%

    Average latency: 0 usec

  Decode status：

    Bytes in: 399

    Bytes out: 332

    Bypass bytes: 0

    Space saved: 0%

    Chunk miss: 0

Collision: 0

    Average latency: 23 usec

Peer ID: 0011-10ad-0012

Start Time: Fri Mar 21 11:43:05 2014

Source IP/Port: 2.2.1.1/34572

Destination IP/Port: 3.2.2.3/80

LAN interface: Serial1/0/1

WAN interface: Serial1/0/2

Configured Policy: TFO DRE LZ

Negotiated Policy: TFO DRE LZ

LAN-\>WAN bytes: Original   104884      Optimized  88594

WAN-\>LAN bytes: Original   744588      Optimized  3355445

LZ section：

  Encode status：

    Bytes in: 0

    Bytes out: 0

    Bypass bytes: 400

    Space saved: 0%

    Average Latency: 0 usec

  Decode status：

    Bytes in: 329

    Bytes out: 393

    Bypass bytes: 63

    Space saved: 16%

    Average Latency: 2 usec

DRE section：

  Encode status：

    Bytes in: 0

    Bytes out: 0

    Bypass bytes: 314

    Space saved: 0%

    Average latency: 0 usec

  Decode status：

    Bytes in: 399

    Bytes out: 332

    Bypass bytes: 0

    Space saved: 0%

    Chunk miss: 0

Collision: 0

    Average latency 23 usec

Total 2 sessions found.

表1-3 display waas session命令显示信息描述表

字段

描述

Peer ID

对端设备ID，即设备的桥MAC地址，用来唯一标识一台对端设备

Start time

WAAS会话建立时间

Source IP/Port

客户端IP地址/端口号

Destination IP/Port

服务器端IP地址/端口号

LAN interface

LAN侧接口

WAN interface

WAN侧接口

Configured Policy

本端设备配置的优化方式，取值包括：

·TFO：表示流传输优化方式，仅支持TCP流传输优化

·DRE：表示消除冗余数据优化方式

·LZ：表示数据压缩优化方式

Negotiated Policy

与对端设备协商后的优化动作，取值包括：

·TFO：表示流传输优化方式，仅支持TCP流传输优化

·DRE：表示消除冗余数据优化方式

·LZ：表示数据压缩优化方式

协商后的优化方式取两端WAAS设备配置优化方式的交集

LAN-\>WAN bytes

LAN侧接口到WAN侧接口的数据统计：

·Original：表示原始字节数

·Optimized：表示优化后的字节数

WAN-\>LAN bytes

WAN侧接口到LAN侧接口的数据统计：

·Original：表示原始字节数

·Optimized：表示优化后的字节数

LZ section

LZ统计信息

DRE section

DRE统计信息

Encode status

压缩统计信息

Decode status

解压缩统计信息

Bytes in

输入字节数

Bytes out

输出字节数

Bypass bytes

未匹配上字典的字节数

Space saved

压缩率，计算公式：

·压缩：(1 - (Bytes out / Bytes in)) \* 100

·解压：(1 - (Bytes in/ Bytes out)) \* 100

Average Latency

最后一次压缩或者解压的平均延迟时间，单位为微秒

Chunk miss

无法根据字典索引找到字典表项累计次数

Collision

解码后数据校验失败累计次数

Total sessions

当前建立的会话总数

**WAAS \-- WAAS配置命令 \-- display waas statistics dre**

------------------------------------------------------------------------

**[display waas statistics dre**]命令用来显示DRE统计信息。

【命令】

集中式设备：

**[display waas statistics dre ** **peer** *peer-id* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display waas statistics dre ** **peer** *peer-id* ]  **slot** *slot-number*

分布式设备－IRF模式：

**[display waas statistics dre ** **peer** *peer-id* ]  **chassis** *chassis-number* **slot** *slot-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer ***peer-id*]：显示指定对端设备的DRE统计信息，*peer-id*表示设备的MAC地址，形式为H-H-H。如果未指定本参数，则显示设备上所有DRE的统计信息。

**[slot ***slot-number*]：显示指定单板上的DRE统计信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的DRE统计信息。（分布设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的DRE统计信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示所有成员设备上的DRE统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的DRE统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示所有成员设备/PEX上的DRE统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的DRE统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的DRE统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的DRE统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟槽位号，*slot-number*表示单板或者PEX所在的槽位号。如果不指定本参数，将显示所有单板上的DRE统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示设备上所有DRE的统计信息。

\<Sysname\> display waas statistics dre

Peer-ID: 0016-9d38-ca1d

Peer version: 1.0

Cache in storage: 614017 bytes

Index number: 11513600

Age: 3 weeks, 5 days, 21 hours, 22 minutes, 40 seconds

Total connections: 24

Active connections: 1

Encode Statistics：

  Dre msgs: 64

  Bytes in: 67344 bytes

  Bytes out: 8840 bytes

  Bypass bytes: 35714 bytes

  Bytes Matched: 59355 bytes

  Space saved: 13%

  Average latency: 2191 usec

Decode Statistics：

  Dre msgs: 318

  Bytes in: 8494760 bytes

  Bytes out: 13780812 bytes

  Bypass bytes: 35556 bytes

  Space saved: 38%

  Average latency: 1471 usec

Peer-ID: 0d38-9d38-ca1d

Peer version: 1.0

Cache in storage: 614017 bytes

Index number: 11513600

Age: 3 weeks, 5 days, 21 hours, 22 minutes, 40 seconds

Total connections: 24

Active connections: 1

Encode Statistics：

  Dre msgs: 64

  Bytes in: 67344 bytes

  Bytes out: 8840 bytes

  Bypass bytes: 35714 bytes

  Bytes Matched: 59355 bytes

  Space saved: 13%

  Average latency: 2191 usec

Decode Statistics：

  Dre msgs: 318

  Bytes in: 8494760 bytes

  Bytes out: 13780812 bytes

  Bypass bytes: 35556 bytes

  Space saved: 38%

  Average latency: 1471 usec

\# 显示指定对端设备的DRE统计信息。

\<Sysname\> display waas statistics dre peer 0016-9d38-ca1d

Peer-ID: 0016-9d38-ca1d

Peer version: 1.0

Cache in storage: 614017 bytes

Index number: 11513600

Age: 3 weeks, 5 days, 21 hours, 22 minutes, 40 seconds

Total connections: 24

Active connections: 1

Encode Statistics：

  Dre msgs: 64

  Bytes in: 67344 bytes

  Bytes out: 8840 bytes

  Bypass bytes: 35714 bytes

  Bytes Matched: 59355 bytes

  Space saved: 13%

  Average latency: 2191 usec

Decode Statistics：

  Dre msgs: 318

  Bytes in: 8494760 bytes

  Bytes out: 13780812 bytes

  Bypass bytes: 35556 bytes

  Space saved: 38%

  Average latency: 1471 usec

表1-4 display waas statistics dre命令显示信息描述表

字段

描述

Peer-ID

对端设备ID，即设备的桥MAC地址，用来唯一标识一台对端设备

Peer version

对端设备的WAAS版本号

Cache in storage

元数据占用的空间大小，单位为字节

Index number

元数据块索引的个数

Age

peer节点存在时间

Total connections

DER连接总数

Active connections

DRE活动连接数

Encode Statistics

压缩统计信息

Decode Statistics

解压缩统计信息

Dre msgs

数据块个数

Bytes in

输入字节数

Bytes out

输出字节数

Bypass bytes

未匹配上字典的字节数

Bytes Matched

匹配上字典的字节数

Space saved

压缩率，计算公式：

·压缩：(1 - (Bytes out / Bytes in)) \* 100

·解压：(1 - (Bytes in/ Bytes out)) \* 100

Average latency

最后一次压缩或者解压的平均延迟时间，单位为微秒

【相关命令】

·**reset waas statistics dre**

**WAAS \-- WAAS配置命令 \-- display waas status**

------------------------------------------------------------------------

**[display waas status**]命令用来显示WAAS全局状态。

【命令】

**[display waas status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示WAAS全局状态。

\<Sysname\> display waas status

WAAS Version: 1.0

Local ID: 02e0-011a-0000

DRE Status: Disabled

LZ Status: Disabled

BlackList Status: Disabled

Total Active connections: 7889

Total data storage size: 1468006400 bytes

Total index number: 11513600

Blacklist Hold-time：5 minutes

Interfaces             Applied policy

Serial1/0/1            waas_global

Serial1/0/2            waas_default

Serial2/0/5            waas_global

Total policy interfaces: 3

表1-5 display waas status命令显示信息描述表

字段

描述

WAAS Version

WAAS版本号

Local ID

本端ID，即WAAS设备的桥MAC地址，用来唯一标识一台WAAS设备。

DRE Status

是否开启WAAS数据冗余消除功能：

·Enabled：表示已开启

·Disabled：表示未开启

LZ Status

是否开启WAAS数据压缩功能功能：

·Enabled：表示已开启

·Disabled：表示未开启

BlackList Status

是否开启自动发现黑名单功能：

·Enabled：表示已开启

·Disabled：表示未开启

Total Active connections

当前的WAAS活动连接数

Total data storage size

所有元数据所占空间的大小，单位为字节。元数据即为字典索引对应的原始数据

Total index number

元数据对应的所有字典索引的个数

Blacklist Hold-time

黑名单表项的老化时间，单位为分钟

Interfaces

已应用WAAS策略的接口列表

Applied policy

接口应用策略列表

Total policy interfaces

应用WAAS策略的接口总数

**WAAS \-- WAAS配置命令 \-- display waas tfo auto-discovery blacklist**

------------------------------------------------------------------------

**[display waas tfo auto-discovery blacklist**]命令用来显示黑名单信息。

【命令】

集中式设备：

**[display waas tfo auto-discovery blacklist **[{ **ipv4** \| **ipv6** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display waas tfo auto-discovery blacklist **[{ **ipv4** \| **ipv6** } [ **slot** *slot-number* ]]]

分布式设备－IRF模式：

**[display waas tfo auto-discovery blacklist**[ { **ipv4** \| **ipv6** } [ **chassis** *chassis-number* **slot** *slot-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IPv4黑名单信息。

**[ipv6**]：显示IPv6黑名单信息。

**[slot ***slot-number*]：显示指定单板的黑名单信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的黑名单信息。（分布设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的黑名单信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示所有成员设备上的黑名单信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的黑名单信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示所有成员设备/PEX上的黑名单信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的黑名单信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的黑名单信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的黑名单信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟槽位号，*slot-number*表示单板/PEX所在的槽位号。如果不指定本参数，将显示所有单板上的黑名单信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示所有IPv4黑名单信息。

\<Sysname\> display waas tfo auto-discovery blacklist ipv4

Server IP address/Port           Insert Time

1.1.1.1/8080                     Fri Mar 21 10:43:05 2014

1.1.1.2/8080                     Fri Mar 21 10:43:06 2014

2.2.2.2/443                      Fri Mar 21 10:20:37 2014

Total 3 entries found.

表1-6 display waas auto-discovery blacklist命令显示信息描述表

字段

描述

Server IP address/Port

服务器IP地址/端口号

Insert Time

黑名单表项的生成时间

Total 3 entries found

黑名单表项的总数

【相关命令】

·**reset waas tfo auto-discovery blacklist**

·**waas tfo auto-discovery blacklist enable**

·**waas tfo auto-discovery blacklist hold-time**

**WAAS \-- WAAS配置命令 \-- match tcp**

------------------------------------------------------------------------

**[match tcp**]命令用来创建匹配流分类的规则。

**[undo match**]命令用来删除创建的匹配流分类规则。

【命令】

**[match** [ *match-id*  **tcp** { **any** \| **destination** \| **source** } [ **ip-address** *ip-address* [ *mask-length* \| *mask* ] \| **ipv6-address** *ipv6-address*  *prefix-length*  ]  **port** *port-list* ]]

**[undo match** *match-id*]

【缺省情况】

未创建匹配流分类的规则。

【视图】

WAAS类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-id*]：指定匹配流分类规则的编号，取值范围为1～65535，是match规则的唯一标识。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。

**[tcp**]：匹配TCP报文流量。

**[any**]：指定匹配规则的源或目的地址、端口号。

**[source**]：指定匹配规则的源地址、源端口号。

**[destination**]：指定匹配规则的目的地址、目的端口号。

**[ip-address** *ip-address*]：指定匹配规则的IPv4地址。

*[mask-length*]：指定子网掩码长度，取值范围为0～32，缺省值为32。

*[mask*]：指定子网掩码，缺省值为255.255.255.255。

**[ipv6-address** *ipv6-address*]：指定匹配规则的IPv6地址。

*[prefix-length*]：指定前缀长度，取值范围为0～128，缺省值为128。

**[port** *port-list*]：指定匹配规则的端口号列表。表示方式为*port-list* = { *port-number* [ **to** *port-number*  } &\<1-10\>]，其中*port-number*表示端口号，取值范围是1～65535，&\<1-10\>表示前面的参数最多可以输入10次。当使用**to**关键字指定端口号范围时，起始端口号必须小于或等于结束端口号。如果未指定本参数，则匹配所有端口号。

【使用指导】

需要注意的是：

·指定匹配类型为源或目的时，需要至少指定IP地址、端口号两者中的一个。

·指定匹配类型为any时，如果指定IP地址、端口号，则表示匹配源IP地址、端口号，或匹配目的IP地址、端口号。

·不允许配置编号不同，但是内容完全相同的match规则。

·WAAS类最多可创建65535条match规则，按照match规则的创建顺序进行匹配，匹配上其中任意一条，则认为匹配上了该类。

【举例】

\# 创建类http_class的匹配规则：匹配源地址为192.168.0.1/16，源端口号为80和8000～8080的tcp流量。

\<Sysname\> system-view

Sysname waas class http_class

Sysname-waasclass-http_class match tcp source ip-address 192.168.0.1 16 port 80 8000 to 8080

\# 创建类http_class的匹配规则：匹配所有TCP流量。

\<Sysname\> system-view

Sysname waas class http_class

Sysname-waasclass-http_class match tcp any

【相关命令】

·**display waas class**

·**waas class**

**WAAS \-- WAAS配置命令 \-- optimize**

------------------------------------------------------------------------

**[optimize**]命令用来配置WAAS类的优化方式。

**[undo optimize**]命令用来恢复缺省情况。

【命令】

**[optimize tfo **[[ **dre** \| **lz** ] \*]]

**[undo optimize**]

【缺省情况】

WAAS类未配置任何优化方式。

【视图】

WAAS策略类动作视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tfo**]**：**流传输优化方式，仅支持TCP流传输优化。

**[dre**]：消除冗余数据优化方式。

**[lz**]：数据压缩优化方式。

【使用指导】

需要注意的是：

·该命令与**passthrough**命令二者只能选其一，如果同时配置了这两条命令，则后配置的生效。

·该命令受优化控制功能状态的影响，如果用户配置了优化动作，而对应的优化控制功能处于关闭状态，则不能对匹配的报文流量进行相应的优化处理。

·对于匹配了黑名单的流量，通过**optimize**命令配置优化动作后，不会对指定流量进行优化。

【举例】

\# 配置WAAS类AFS的优化方式为TFO、DRE和LZ。

\<Sysname\> system-view

Sysname waas policy waas_global

Sysname-waaspolicy-waas_global class AFS

Sysname-waaspolicy-waas_global-AFS optimize tfo dre lz

【相关命令】

·**c****lass**

·**display waas policy**

·**passthrough**

·**waas policy******

·**waas tfo optimize dre**

·**waas tfo optimize lz**

**WAAS \-- WAAS配置命令 \-- passthrough**

------------------------------------------------------------------------

**[passthrough**]命令用来配置WAAS类的直接旁路动作。

**[undo passthrough**]命令用来恢复缺省情况。

【命令】

**[passthrough**]

**[undo passthrough**]

【缺省情况】

未配置直接旁路动作。

【视图】

WAAS策略类动作视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

直接旁路动作就是对匹配WAAS类的报文流量不进行任何优化处理，直接转发。本命令与**optimize**命令二者只能选其一，如果同时配置了这两条命令，则后配置的生效。

【举例】

\# 配置WAAS类AFS的优化方式为直接旁路。

\<Sysname\> system-view

Sysname waas policy waas_global

Sysname-waaspolicy-waas_global class AFS

Sysname-waaspolicy-waas_global-AFS passthrough

【相关命令】

·**class**

·**display waas policy**

·**optimize**

·**waas policy******

**WAAS \-- WAAS配置命令 \-- reset waas cache dre**

------------------------------------------------------------------------

**[reset waas cache dre**]命令用来清除DRE的数据字典。

【命令】

**[reset waas cache dre ** **peer** *peer-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer ***peer-id*]：清除指定对端设备的DRE数据字典，*peer-id*表示设备的桥MAC地址，形式为H-H-H。如果未指定本参数，则清除设备上所有DRE的数据字典。

【举例】

\# 清除对端设备为0789-445d-effa的DER数据字典。

\<Sysname\> reset waas cache dre peer 0789-445d-effa

【相关命令】

·**display waas statistics dre**

**WAAS \-- WAAS配置命令 \-- reset waas statistics dre**

------------------------------------------------------------------------

**[reset waas statistics dre**]命令用来清除DRE统计信息。

【命令】

**[reset waas statistics dre ** **peer** *peer-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer ***peer-id*]：清除指定对端设备的DRE统计信息，*peer-id*表示对端设备的桥MAC地址，形式为H-H-H。如果未指定本参数，则清除设备上所有DRE的统计信息。

【举例】

\# 清除设备上所有DRE的统计信息。

\<Sysname\> reset waas statistics dre

【相关命令】

·**display waas statistics dre**

**WAAS \-- WAAS配置命令 \-- reset waas tfo auto-discovery blacklist**

------------------------------------------------------------------------

**[reset waas tfo auto-discovery blacklist**]命令用来清除所有的黑名单表项。

【命令】

**[reset waas tfo auto-discovery blacklist**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 清除所有的黑名单表项。

\<Sysname\> reset waas tfo auto-discovery blacklist

【相关命令】

·**display waas tfo auto-discovery blacklist**

·**waas tfo auto-discovery blacklist enable**

·**waas tfo auto-discovery blacklist hold-time**

**WAAS \-- WAAS配置命令 \-- waas apply policy**

------------------------------------------------------------------------

**[waas apply policy**]命令用来在接口上应用WAAS策略。

**[undo waas apply policy**]命令用来恢复缺省情况。

【命令】

**[waas apply policy ** *policy-name* ]

**[undo waas apply policy**]

【缺省情况】

接口上未应用任何WAAS策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：指定WAAS策略的名称，为1～63个字符的字符串，不区分大小写，且该策略必须存在。如果不指定本参数，则在接口上应用预定义策略waas_default。

【使用指导】

WAAS设备应用策略的接口连接广域网，未应用策略的接口连接局域网。对从广域网侧发送或接收的报文流量会与广域网接口所引用的策略进行匹配。但如果指定流量经过设备的入接口和出接口都连接广域网或者局域网，则不对报文进行优化。

【举例】

\# 在接口GigabitEthernet1/0/1上应用WAAS策略global_policy。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 waas apply policy global_policy

【相关命令】

·**display waas policy**

·**display waas status**

·**waas policy**

**WAAS \-- WAAS配置命令 \-- waas class**

------------------------------------------------------------------------

**[waas class**]命令用来创建WAAS类，并进入WAAS类视图。

**[undo waas class**]命令用来删除指定的WAAS类。

【命令】

**[waas class** *class-name*]

**[undo waas class** *class-name*]

【缺省情况】

只存在预定义类。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：指定WAAS类的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·如果指定的类不存在，创建该类并进入其视图，否则直接进入其视图。如果创建的class未配置任何match规则，则该类不参与所属策略对报文流量的匹配。

·建议用户通过本命令进入WAAS预定义类视图，修改预定义类配置。（预定义类参见表 1-7(?-326408526#_Ref401328623)）

【举例】

\# 创建WAAS类waas_global，并进入其视图。

\<Sysname\> system-view

Sysname waas class waas_global

Sysname-waasclass-waas_global

【相关命令】

·**class**

·**display waas class**

**WAAS \-- WAAS配置命令 \-- waas config remove-all**

------------------------------------------------------------------------

**[waas config remove-all**]命令用来删除WAAS所有配置。

【命令】

**[waas config** **remove-all**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过本命令删除WAAS特性的所有配置数据和运行数据，并使WAAS进程退出。

【举例】

\# 删除WAAS所有配置。

\<Sysname\> system-view

Sysname waas config remove-all

The command will clear all the WAAS configuration. Continue? [Y/N:y]

**WAAS \-- WAAS配置命令 \-- waas config restore-default**

------------------------------------------------------------------------

**[waas config restore-default**]命令用来还原WAAS的预定义配置。

【命令】

**[waas config restore-default**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

还原WAAS的预定义配置是把WAAS预定义策略和预定义类的配置还原到WAAS进程第一次启动时的配置，不修改用户自定义的配置。

需要注意的是，配置本命令时，需保证所有接口未应用任何策略，否则恢复失败。

【举例】

\# 还原WAAS预定义配置。

\<Sysname\> system-view

Sysname waas config restore-default

The command will restore all the WAAS configuration to default. Continue? [Y/N:y]

**WAAS \-- WAAS配置命令 \-- waas policy**

------------------------------------------------------------------------

**[waas policy**]命令用来创建WAAS策略，并进入WAAS策略视图。

**[undo waas policy**]命令用来删除指定的WAAS策略。

【命令】

**[waas policy ***policy-name*]

**[undo waas policy ***policy-name*]

【缺省情况】

只存在预定义策略waas_default。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：指定WAAS策略的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

需要注意的是：

·如果指定的策略不存在，创建该策略并进入其视图，否则直接进入其视图。

·删除指定策略时，如果该策略应用于接口，则应先取消策略在接口上的应用再删除，否则删除失败。

·建议用户通过此命令进入预定义策略的视图，采用修改预定义策略的方式完成策略配置。预定义策略是WAAS进程在第一次启动时系统创建的策略，策略名称为waas_default，默认引用所有的预定义类。

表1-7 预定义策略

预定义类

优化方式

源端口号

目的端口号

Kerberos

Pass-through

-

88、464、543、544、749、754、888、2053

SASL

Pass-through

-

3659

TACACS

Pass-through

-

49

Amanda

TFO

-

10080

BackupExpress

TFO

-

6123

CommVault

TFO

-

8400-8403

Connected-DataProtector

TFO

-

16384

IBM-TSM

TFO+LZ+DRE

-

1500-1502

Legato-NetWorker

TFO

-

7937、7938、, 7939

Legato-RepliStor

TFO

-

7144、7145

Veritas-BackupExec

TFO

-

1125、3527、6101、6102、6106

Veritas-NetBackup

TFO

-

13720、13721、13782、13785

PDMWorks

LZ+TFO+DRE

-

30000、40000

Cisco-CallManager

Pass-through

-

2443、2748

SIP-secure

Pass-through

-

5061

VoIP-Control

Pass-through

-

1300、1718-1720, 2000-2002,2428, 5060,11000-11999

CU-SeeMe

Pass-through

-

7640、7642、7648、7649

ezMeeting

Pass-through

-

10101-10103、26260-26261

GnomeMeeting

Pass-through

-

30000-30010

Intel-Proshare

Pass-through

-

5713-5717

MS-NetMeeting

Pass-through

-

522、1503、1731

VocalTec

Pass-through

-

1490、6670、22555、25793

SSL-Shell

Pass-through

-

614

Telnet

Pass-through

-

23、107、513

Telnets

Pass-through

-

992

Unix-Remote-Execution

Pass-through

-

512、514

Documentum

LZ+TFO+DRE

-

1489

Filenet

LZ+TFO+DRE

-

32768-32774

ProjectWise-FileTransfer

LZ+TFO+DRE

-

5800

LDAP

LZ+TFO+DRE

-

389、8404

LDAP-Global-Catalog

LZ+TFO+DRE

-

3268

LDAP-Global-Catalog-Secure

Pass-through

-

3269

LDAP-secure

Pass-through

-

636

HP-OpenMail

LZ+TFO+DRE

-

5729、5755、5757、5766, 5767、5768

Internet-Mail

LZ+TFO+DRE

-

25、110、143、220

Internet-Mail-secure

TFO

-

465、993、995

Lotus-Notes

LZ+TFO+DRE

-

1352

MDaemon

LZ+TFO+DRE

-

3000、3001

NNTP

LZ+TFO+DRE

-

119

NNTP-secure

TFO

-

563

Novell-Groupwise

LZ+TFO+DRE

-

1099、1677、2800、3800, 7100、7101、7180、7181、7205、9850

PCMail-Server

LZ+TFO+DRE

-

158

QMTP

LZ+TFO+DRE

-

209

X400

LZ+TFO+DRE

-

102

SAP

LZ+TFO+DRE

-

3200-3219、3221-3224、3226-3267、3270-3282、3284-3305、3307-3388、3390-3399、3600-3659、3662-3699

Siebel

LZ+TFO+DRE

-

2320、2321、8448

AFS

LZ+TFO+DRE

-

7000-7009

Apple-AFP

LZ+TFO+DRE

-

548

CIFS-non-wafs

LZ+TFO+DRE

-

139、445

NFS

LZ+TFO+DRE

-

2049

Novell-NetWare

LZ+TFO+DRE

-

524

Sun-RPC

Pass-through

-

111

BFTP

LZ+TFO+DRE

-

152

FTP

Pass-through

-

21

FTP-Data

LZ+TFO+DRE

20

FTPS

TFO

-

990

FTPS-Data

Pass-through

989

Simple-FTP

LZ+TFO+DRE

-

115

TFTP

LZ+TFO+DRE

-

69

TFTPS

TFO

-

3713

AOL

Pass-through

-

5190-5193

Apple-iChat

Pass-through

-

5297、5298

IRC

Pass-through

-

531、6660-6669

Jabber

Pass-through

-

5222、5269

Lotus-Sametime-Connect

Pass-through

-

1533

MS-Chat

Pass-through

-

6665、6667

MSN-Messenger

Pass-through

-

1863、6891-6900

Yahoo-Messenger

Pass-through

-

5000、5001、5050、5100

DNS

Pass-through

-

53

iSNS

Pass-through

-

3205

Service-Location

Pass-through

-

427

WINS

Pass-through

-

42、137、1512

Cisco-NetFlow

Pass-through

-

7544、7545

Basic-TCP-services

Pass-through

-

1-19

BGP

LZ+TFO+DRE

-

179

MS-Message-Queuing

LZ+TFO+DRE

-

1801、2101、2103、2105

NTP

Pass-through

-

123

Other-Secure

Pass-through

-

261、44,、684、695、994、2252、2478、2479、2482、2484、2679、2762、2998、3077、3078、3183、3191、3220、3410、3424、3471、3496,3509、3529、3539、3660、3661、3747、3864、3885、3896、3897、3995、4031、5007、5989、5990、7674、9802、12109

SOAP

LZ+TFO+DRE

-

7627

Symantec-AntiVirus

LZ+TFO+DRE

-

2847、2848、2967、2968, 38037, 38292

BitTorrent

Pass-through

-

6881--6889, 6969

eDonkey

Pass-through

-

4661、4662

Gnutella

Pass-through

-

6346--6349、6355、5634

Grouper

Pass-through

-

8038

HotLine

Pass-through

-

5500--5503

Kazaa

Pass-through

-

1214

Laplink-ShareDirect

Pass-through

-

2705

Napster

Pass-through

-

6666、6677、6700、6688, 7777、8875

Qnext

Pass-through

-

44、5555

SoulSeek

Pass-through

-

2234、5534

WASTE

Pass-through

-

1337

WinMX

Pass-through

-

6699

AppSocket

LZ+TFO+DRE

-

9100

IPP

LZ+TFO+DRE

-

631

SUN-Xprint

LZ+TFO+DRE

-

8100

Unix-Printing

LZ+TFO+DRE

-

170, 515

Altiris-CarbonCopy

Pass-through

-

1680

Apple-NetAssistant

Pass-through

-

3283

Citrix-ICA

LZ+TFO+DRE

-

1494、2598

ControlIT

TFO

-

799

Danware-NetOp

TFO

-

6502

Laplink-Host

TFO

-

1547

Laplink-PCSync

TFO

-

8444

Laplink-PCSync-secure

TFO

-

8443

MS-Terminal-Services

TFO

-

3389

Netopia-Timbuktu

TFO

-

407、1417--1420

PCAnywhere

TFO

-

73、5631、5632、65301

RAdmin

TFO

-

4899

Remote-Anything

TFO

-

3999、4000

Vmware-VMConsole

TFO

-

902

VNC

TFO

-

5801--5809、6900--6909

XWindows

TFO

-

6000--6063

Double-Take

LZ+TFO+DRE

-

1100、1105

EMC-Celerra-Replicator

LZ+TFO+DRE

-

8888

MS-Content-Replication-Service

TFO

-

560、507

Netapp-SnapMirror

LZ+TFO+DRE

-

10565--10569

Remote-Replication-Agent

TFO

-

5678

Rsync

TFO

-

873

Borland-Interbase

LZ+TFO+DRE

-

3050

IBM-DB2

LZ+TFO+DRE

-

523

InterSystems-Cache

LZ+TFO+DRE

-

1972

MS-SQL

LZ+TFO+DRE

-

1433

MySQL

LZ+TFO+DRE

-

3306

Oracle

LZ+TFO+DRE

-

66、1521、1525

Pervasive-SQL

LZ+TFO+DRE

-

1583

PostgreSQL

LZ+TFO+DRE

-

5432

Scalable-SQL

LZ+TFO+DRE

-

3352

SQL-Service

LZ+TFO+DRE

-

156

Sybase-SQL

LZ+TFO+DRE

-

1498、2439、2638、3968

UniSQL

LZ+TFO+DRE

-

1978、1979

HTTPS

TFO

-

443

SSH

TFO

-

22

EMC-SRDFA-IP

LZ+TFO+DRE

-

1748

FCIP

LZ+TFO+DRE

-

3225

iFCP

LZ+TFO+DRE

-

3420

iSCSI

LZ+TFO+DRE

-

3260

Liquid-Audio

LZ+TFO+DRE

-

18888

MS-NetShow

LZ+TFO+DRE

-

1755

RTSP

LZ+TFO+DRE

-

554、8554

VDOLive

LZ+TFO+DRE

-

7000

BMC-Patrol

Pass-through

-

6161、6162、6767、6768, 8160、8161、10128

HP-OpenView

Pass-through

-

7426--7431、7501、7510

HP-Radia

LZ+TFO+DRE

-

3460、3461、3464、3466

IBM-NetView

Pass-through

-

729--731

IBM-Tivoli

LZ+TFO+DRE

-

94、627、1580、1581、1965

LANDesk

LZ+TFO+DRE

-

9535、9593--9595

NetIQ

Pass-through

-

2220、2735、10113--10116

Netopia-netOctopus

Pass-through

-

1917、1921

Novell-ZenWorks

LZ+TFO+DRE

-

517、1761--1763、2037, 2544、8039

WAAS-FlowMonitor

TFO

-

7878

WBEM

Pass-through

-

5987、5988

Clearcase

LZ+TFO+DRE

-

371

CVS

LZ+TFO+DRE

-

2401

CIFS

LZ+TFO+DRE

-

139、445

HTTP

LZ+TFO+DRE

-

80、3128、8000、8001、8080

HTTPS

TFO

-

443

L2TP

TFO

-

1701

OpenVPN

TFO

-

1194

PPTP

TFO

-

1723

【举例】

\# 进入WAAS预定义策略视图。

\<Sysname\> system-view

Sysname waas policy waas_default

Sysname-waaspolicy-waas_default

【相关命令】

·**display waas policy**

**WAAS \-- WAAS配置命令 \-- waas tfo auto-discovery blacklist enable**

------------------------------------------------------------------------

**[waas tfo auto-discovery blacklist enable**]命令用来开启自动发现黑名单功能。

**[undo waas tfo auto-discovery blacklist enable**]命令用来关闭自动发现黑名单功能。

【命令】

**[waas tfo auto-discovery blacklist enable**]

**[undo waas tfo auto-discovery blacklist enable**]

【缺省情况】

自动发现黑名单功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当本端设备配置了WAAS策略并应用于接口时，如果本端设备不能通过此接口与对端设备建立TCP连接，那么系统自动将请求的服务器接口的IP地址和端口号加入黑名单，对匹配黑名单的流量不做任何优化。

在建立TCP连接的三次握手过程中，本端发送携带特定TCP选项的请求报文后，如果发生下列情况，则认为连接建立失败：

·在指定时间内未作出有效应答。

·对端设备关闭了TCP连接。

【举例】

\# 开启WAAS自动发现黑名单功能。

\<Sysname\> system-view

Sysname waas tfo auto-discovery blacklist enable

【相关命令】

·**display waas tfo auto-discovery blacklist**

**WAAS \-- WAAS配置命令 \-- waas tfo auto-discovery blacklist hold-time**

------------------------------------------------------------------------

**[waas tfo auto-discovery blacklist hold-time**]命令用来配置黑名单表项的老化时间。

**[undo waas tfo auto-discovery blacklist hold-time**]命令用来恢复缺省情况。

【命令】

**[waas tfo auto-discovery blacklist hold-time ***minutes*]

**[undo waas tfo auto-discovery blacklist hold-time**]

【缺省情况】

黑名单表项的老化时间为5分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：指定黑名单表项的老化时间，取值范围为1～10080，单位为分钟。

【使用指导】

黑名单表项具有一定的生存时间，超出老化时间，黑名单表项被系统自动删除，当有新连接接入时，设备通过发现黑名单功能构建新的黑名单表项。

【举例】

\# 配置WAAS黑名单表项的老化时间为30分钟。

\<Sysname\> system-view

Sysname waas tfo auto-discovery blacklist hold-time 30

【相关命令】

·**display waas tfo auto-discovery blacklist**

·**waas tfo auto-discovery blacklist enable**

**WAAS \-- WAAS配置命令 \-- waas tfo base-congestion-window**

------------------------------------------------------------------------

**[waas tfo base-congestion-window**]命令用来配置超时重传时慢启动的初始拥塞窗口大小。

**[undo waas tfo base-congestion-window**]命令用来恢复缺省情况。

【命令】

**[waas tfo base-congestion-window ***segments*]

**[undo waas tfo base-congestion-window**]

【缺省情况】

初始拥塞窗口为2。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[segments*]*：*超时重传时慢启动的初始拥塞窗口大小，取值范围为1～10，单位为最大报文段个数。

【使用指导】

拥塞窗口的大小取决于网络的拥塞程度和发送速度，并且动态的在变化。设置合理的慢启动初始拥塞窗口，当拥塞发生后，能够较快的恢复到网络最大传输能力。

【举例】

\# 配置超时重传时慢启动的初始拥塞窗口为3。

\<Sysname\> system-view

Sysname waas tfo base-congestion-window 3

**WAAS \-- WAAS配置命令 \-- waas tfo keepalive**

------------------------------------------------------------------------

**[waas tfo keepalive**]命令用来开启TFO的保活功能。

**[undo waas tfo keepalive**]命令用来关闭TFO的保活功能。

【命令】

**[waas tfo keepalive**]

**[undo waas tfo keepalive**]

【缺省情况】

TFO的保活功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启TFO的保活功能后，系统启动保活定时器。当定时器超时后，如果通信双方仍没有数据传输，则向对端设备发送保活报文，使连接不断开。

【举例】

\# 开启TFO的保活功能。

\<Sysname\> system-view

Sysname waas tfo keepalive

**WAAS \-- WAAS配置命令 \-- waas tfo optimize dre**

------------------------------------------------------------------------

**[waas tfo optimize dre**]命令用来开启WAAS消除数据冗余功能。

**[undo waas tfo optimize dre**]命令用来关闭WAAS消除数据冗余功能。

【命令】

**[waas tfo optimize dre**]

**[undo waas tfo optimize dre**]

【缺省情况】

WAAS消除数据冗余功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有WAAS消除数据冗余功能处于开启状态时，WAAS策略下所配置的消除数据冗余优化方式才会生效。

【举例】

\# 关闭WAAS消除数据冗余功能。

\<Sysname\> system-view

Sysname undo waas tfo optimize dre

【相关命令】

·**display waas status**

**WAAS \-- WAAS配置命令 \-- waas tfo optimize lz**

------------------------------------------------------------------------

**[waas tfo optimize lz**]命令用来开启WAAS数据压缩功能。

**[undo waas tfo optimize lz**]命令用来关闭WAAS数据压缩功能。

【命令】

**[waas tfo optimize lz**]

**[undo waas tfo optimize lz**]

【缺省情况】

WAAS数据压缩功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有WAAS数据压缩功能处于开启状态时，WAAS策略下所配置的数据压缩优化方式才会生效。

【举例】

\# 关闭WAAS数据压缩功能。

\<Sysname\> system-view

Sysname undo waas tfo optimize lz

【相关命令】

·**display waas status**

**WAAS \-- WAAS配置命令 \-- waas tfo receive-buffer**

------------------------------------------------------------------------

**[waas tfo receive-buffer**]命令用来配置TFO的接收缓冲区大小。

**[undo waas tfo receive-buffer**]命令用来恢复缺省情况。

【命令】

**[waas tfo receive-buffer ***buffer-size*]

**[undo waas tfo receive-buffer**]

【缺省情况】

TFO的接收缓冲区为64KB。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[buffer-size*]*：*TFO的接收缓冲区大小，取值范围为32～16384，单位为KB。

【使用指导】

用户可以通过调整接收缓冲区的大小来影响线路的吞吐量。

【举例】

\# 调整TFO的接收缓冲区为1024KB。

\<Sysname\> system-view

Sysname waas tfo receive-buffer 1024

